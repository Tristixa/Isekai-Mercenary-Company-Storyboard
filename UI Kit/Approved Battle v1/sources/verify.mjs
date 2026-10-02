import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {openPage} from './cdp.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const required=['tl_act_plate','tl_bezel','tl_track_enemy','tl_track_party','tl_divider','tl_act_zone','tl_pointer','tl_hub','tl_marker_party','tl_marker_enemy','tl_marker_party_glow','tl_marker_enemy_glow','tl_flag_skill','gauge_frame','gauge_hp_track','gauge_skill_track','gauge_skill_ready'];
const m=JSON.parse(fs.readFileSync(root+'/kit-battle.json'));
function coverage(pieces){assert.deepEqual(pieces.map(p=>p.piece).sort(),[...required].sort())}
coverage(m.pieces);assert.throws(()=>coverage(m.pieces.slice(1)));
for(const p of m.pieces){for(const k of ['piece','file','group','tier','size','margins','stretch'])assert.ok(k in p);assert.equal(p.stretch,false);assert.deepEqual(p.margins,[0,0,0,0]);assert.equal(p.group,'battle');assert.deepEqual(p.size,p.use_size.map(v=>v*2));assert.deepEqual(p.anchor,p.size.map(v=>v/2));}
const files=Object.fromEntries(m.pieces.flatMap(p=>[[p.piece,'data:image/png;base64,'+fs.readFileSync(root+'/'+p.file).toString('base64')],[p.piece+'@1x','data:image/png;base64,'+fs.readFileSync(root+'/'+p.file_1x).toString('base64')]]));
const browser=await openPage('about:blank');let result;
try{result=await browser.evaluate(`(async()=>{
 const files=${JSON.stringify(files)},M=${JSON.stringify(m.pieces)},D={},checks=[];
 const ok=(v,msg)=>{if(!v)throw Error(msg);checks.push(msg)};
 for(const [name,src] of Object.entries(files)){const im=await new Promise((res,rej)=>{const i=new Image();i.onload=()=>res(i);i.onerror=rej;i.src=src});const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);const d=g.getImageData(0,0,c.width,c.height).data;D[name]={w:c.width,h:c.height,d};let zero=0,visible=0,partial=0;for(let i=3;i<d.length;i+=4){if(!d[i])zero++;else visible++;if(d[i]>0&&d[i]<255)partial++}const p=M.find(p=>p.piece===name.replace('@1x',''));ok(im.width===p.size[0]/(name.endsWith('@1x')?2:1)&&im.height===p.size[1]/(name.endsWith('@1x')?2:1),name+' dimensions');ok(zero>0&&visible>0&&partial>0,name+' meaningful alpha');ok(d[3]===0&&d[(c.width-1)*4+3]===0&&d[(c.width*(c.height-1))*4+3]===0,name+' clear corners');}
 const px=(n,x,y)=>{const q=D[n],i=(Math.floor(y)*q.w+Math.floor(x))*4;return Array.from(q.d.slice(i,i+4))};
 const polar=(n,r,a,c=240)=>px(n,c+r*Math.sin(a*Math.PI/180),c-r*Math.cos(a*Math.PI/180));
 for(const n of ['tl_bezel','tl_track_enemy','tl_track_party','tl_divider','tl_act_zone','tl_pointer','tl_hub'])ok(D[n].w===480&&D[n].h===480,n+' shared canvas');
 for(const n of ['tl_bezel','tl_track_enemy','tl_track_party','tl_divider']){const q=D[n];let x0=999,y0=999,x1=-1,y1=-1;for(let y=0;y<q.h;y++)for(let x=0;x<q.w;x++)if(q.d[(y*q.w+x)*4+3]>20){x0=Math.min(x0,x);y0=Math.min(y0,y);x1=Math.max(x1,x);y1=Math.max(y1,y)}ok(Math.abs((x0+x1)/2-239.5)<1&&Math.abs((y0+y1)/2-239.5)<1,n+' measured concentric alpha bounds')}
 const white=p=>p[3]>150&&Math.min(...p.slice(0,3))>140&&Math.max(...p.slice(0,3))-Math.min(...p.slice(0,3))<100;
 const tickCounts={};
 for(const [n,r] of [['tl_track_enemy',100],['tl_track_party',71]]){let total=0,long=0;for(let i=0;i<120;i++){let hit=false,big=false;for(let da=-.35;da<=.35;da+=.07){hit ||= white(polar(n,2*(r+4.1),i*3+da));big ||= white(polar(n,2*(r-5.2),i*3+da));}ok(hit===(i%5===0),n+' tick occupancy at '+i*3+' degrees');ok(big===(i%10===0),n+' long tick occupancy at '+i*3+' degrees');if(hit)total++;if(big)long++}ok(total===24,n+' twenty-four white ticks');ok(long===12,n+' twelve long ticks');tickCounts[n]={total,long}}
 function clearDisk(n,c,r){for(let y=c-r;y<c+r;y++)for(let x=c-r;x<c+r;x++)if(Math.hypot(x+.5-c,y+.5-c)<r-1&&px(n,x,y)[3]>0)return false;return true}
 ok(clearDisk('tl_hub',240,59),'hub 60px portrait aperture');ok(clearDisk('gauge_frame',104,69),'gauge 70px portrait aperture');for(const n of ['tl_marker_party','tl_marker_enemy'])ok(clearDisk(n,48,33),n+' 34px portrait aperture');
 for(const n of ['tl_marker_party_glow','tl_marker_enemy_glow']){let valid=true;for(let i=0;i<D[n].d.length;i+=4)if(D[n].d[i+3]&&!(D[n].d[i]===255&&D[n].d[i+1]===255&&D[n].d[i+2]===255))valid=false;ok(valid,n+' white-alpha mask')}
 ok(polar('tl_act_plate',171,330)[3]===255,'ACT plate centered between tracks at 330 degrees');ok(polar('tl_act_plate',171,150)[3]===0,'ACT plate opposite side clear');
 for(const a of [0,90,180,270])ok(polar('tl_hub',76,a)[3]===255,'hub quarter-point stud '+a);
 ok(px('tl_hub',240,316)[3]===255,'NEXT gilded plate under portrait');
 ok(polar('tl_act_zone',170,330)[3]===255,'ACT opaque gold bridge');ok(polar('tl_act_zone',170,180)[3]===0,'ACT no opposite wedge');ok(polar('tl_pointer',226,300)[3]>0,'pointer at zone start');
 for(const n of ['gauge_hp_track','gauge_skill_track']){const r=n.includes('hp')?82:98;let occupied=0;for(let a=0;a<360;a++)if(polar(n,r,a,104)[3]>100)occupied++;ok(occupied>=268&&occupied<=272,n+' measured 270-degree sweep');ok(polar(n,r,180,104)[3]===0,n+' bottom opening')}
 return {checks:checks.length,tickCounts,results:checks};
 })()`);}finally{browser.close()}
function size(p){const b=fs.readFileSync(root+'/'+p);return [b.readUInt32BE(16),b.readUInt32BE(20)]}
assert.deepEqual(size('mockups/battle-ring.png'),[1280,720]);assert.deepEqual(size('sheets/battle-ring.png'),[2080,2030]);
const proof=JSON.parse(fs.readFileSync(root+'/sources/proof-check.json'));assert.equal(proof.fonts_loaded,true);assert.deepEqual(proof.ring_use_size,[240,240]);for(const n of required.filter(n=>!['tl_marker_enemy_glow','gauge_skill_ready'].includes(n)))assert.ok(proof.draws.some(d=>d.piece===n),n+' used in proof');
fs.writeFileSync(root+'/sources/verification.json',JSON.stringify({status:'pass',pieces:m.pieces.length,png_exports:Object.keys(files).length,negative_control:'missing piece rejected',...result,sheet:[2080,2030],mockup:[1280,720]},null,2));
console.log('BATTLE_ASSETS_VERIFIED',m.pieces.length,'pieces;',Object.keys(files).length,'exports;',result.checks,'pixel checks');
