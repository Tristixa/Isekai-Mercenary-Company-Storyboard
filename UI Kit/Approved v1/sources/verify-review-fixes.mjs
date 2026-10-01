// Review-specific assertions supplement the original coverage/corner/contrast verifier.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=f=>fs.readFileSync(root+'/'+f), json=f=>JSON.parse(read(f));
const m=json('kit.json'),qa=json('sources/qa.json'),source=read('sources/kit.js').toString();
const before='superseded/before-fixes-2026-09-28/';
const lookup=new Map(m.pieces.map(p=>[p.piece,p]));
const text=qa.text.filter(t=>t.screen.startsWith('mock')||['roster','world-hud'].includes(t.screen));
const forbidden=t=>/\bcompany\b/i.test(t);
assert.ok(forbidden('The Company'),'negative control for forbidden wording');
assert.ok(text.every(t=>!forbidden(t.text)));
assert.ok(qa.text.filter(t=>t.screen==='kit').every(t=>!forbidden(t.text)));
assert.ok(text.some(t=>t.screen==='mock-ledger'&&t.text==='Your Guild'));
const battle=qa.draws.filter(d=>d.screen==='mock-battle');
assert.ok(!battle.some(d=>d.piece==='rare_badge'));
assert.ok(text.some(t=>t.screen==='mock-battle'&&t.text==='Dire Boar'));
assert.ok(text.some(t=>t.screen==='mock-battle'&&t.text==='Forest Wolf'));
assert.ok(source.includes("[['wolf',245,539,250],['boar',525,567,330]]"));
const front=qa.formation.filter(p=>p.row==='front').sort((a,b)=>a.y-b.y),back=qa.formation.filter(p=>p.row==='back');
assert.deepEqual(front.map(p=>p.name),['Anselm Voigt','Severa Kaltenbach','Otto Grimbald']);
assert.equal(back.length,1);assert.equal(back[0].name,'Nell Larkin');
assert.ok(front.every(p=>p.bounds[2]<back[0].bounds[0]));
for(let i=1;i<front.length;i++){assert.ok(front[i].x>front[i-1].x);assert.ok(front[i].y>front[i-1].y);assert.ok(front[i-1].bounds[2]<front[i].bounds[0])}
assert.ok(qa.formation.every(p=>p.bounds[2]<1395));
assert.ok(lookup.has('rare_badge'));
const changedGlyphs=['stun','leadership','ongoing'];
for(const [name,pair] of [['stun','reputation'],['leadership','boss'],['ongoing','time']])for(const size of [24,32,48]){
 const f=lookup.get(name+'_'+size).file;
 assert.ok(!read(f).equals(read(lookup.get(pair+'_'+size).file)),name+' clashes');
 assert.ok(!read(f).equals(read(before+f)),name+' not redrawn');
}
for(const name of ['insight','information','negotiation','commerce'])for(const size of [24,32,48]){
 const f=lookup.get(name+'_'+size).file;assert.ok(read(f).equals(read(before+f)),name+' changed');
}
for(const name of ['accepted','complete','expired']){
 const p=lookup.get('stamp_'+name);assert.equal(p.mask,true);assert.equal(p.stretch,false);
 assert.equal(p.tint_token,name==='expired'?'danger':'ink');
}
assert.ok(qa.draws.some(d=>d.screen==='mock-request'&&d.piece==='stamp_accepted'&&d.tint_token==='ink'));
assert.ok(source.includes("state==='selected'?.48"));
assert.ok(source.includes("state==='selected'?T.blue_select"));
// Decode and compare the atlas to each source image in the same browser used by the builder.
const {openPage}=await import('./cdp.mjs');
const browser=await openPage('about:blank');
try{
 const images={};for(const e of m.icon_atlas.entries)images[e.icon]=read(lookup.get(e.icon+'_48').file).toString('base64');
 images.atlas=read(m.icon_atlas.file).toString('base64');
 const result=await browser.evaluate(`(async()=>{
  const images=${JSON.stringify(images)},entries=${JSON.stringify(m.icon_atlas.entries)};
  const canvases={};for(const [key,b64]of Object.entries(images)){const im=new Image();im.src='data:image/png;base64,'+b64;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);canvases[key]=g}
  for(const e of entries){const [x,y,w,h]=e.rect,a=canvases.atlas.getImageData(x,y,w,h).data,b=canvases[e.icon].getImageData(0,0,w,h).data;if(!a.every((v,i)=>v===b[i]))throw Error('Atlas mismatch '+e.icon)}
  return entries.length;
 })()`);assert.equal(result,m.icon_atlas.entries.length);
}finally{browser.close()}
const allowed=new Set(['sources/kit.js','sources/render.html','sources/qa.json','sources/verification.json','kit.json','README.md','review.html','kit/icons/icons_atlas_48.png','kit/tier1/ledger_highlight_selected.png','sheets/tier1.png','sheets/tier2.png','sheets/icons.png','mockups/mock-battle.png','mockups/mock-ledger.png','mockups/mock-request.png',...changedGlyphs.flatMap(n=>[24,32,48].map(s=>'kit/icons/'+n+'_'+s+'.png')),...['accepted','complete','expired'].map(n=>'kit/tier2/stamp_'+n+'.png')]);
const changed=[];
function walk(dir,rel=''){for(const ent of fs.readdirSync(dir,{withFileTypes:true})){const f=rel+ent.name;if(ent.isDirectory())walk(path.join(dir,ent.name),f+'/');else {assert.ok(fs.existsSync(root+'/'+f),'removed original '+f);if(!read(f).equals(read(before+f))){assert.ok(allowed.has(f),'unrelated file changed '+f);changed.push(f)}}}}
walk(root+'/'+before);
const result={status:'passed',atlas_cells_compared:m.icon_atlas.entries.length,changed_original_files:changed,unrelated_original_changes:0,backup:before,forbidden_label_negative_control:'passed',related_pairs_unchanged:true};
fs.writeFileSync(root+'/sources/review-fixes-verification.json',JSON.stringify(result,null,2));
console.log('REVIEW_FIXES_VERIFIED',JSON.stringify(result));
