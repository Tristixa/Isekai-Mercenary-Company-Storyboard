import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {openPage,sleep} from './cdp.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..').replaceAll('\\','/');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const baseline=JSON.parse(fs.readFileSync(root+'/history/v1-60-ticks/baseline.json'));
const tracks=['tl_track_enemy','tl_track_party'];
const allowed=new Set(tracks.flatMap(n=>['kit/battle/'+n+'.png','kit/battle/'+n+'@1x.png','sources/generated/'+n+'.png']).concat('sheets/battle-ring.png'));
for(const n of tracks)for(const suffix of ['.png','@1x.png'])assert.equal(hash(fs.readFileSync(root+'/history/v1-60-ticks/'+n+suffix)),baseline.hashes['kit/battle/'+n+suffix]);
let html=fs.readFileSync(root+'/sources/render.html','utf8');
const start=html.indexOf('//',html.indexOf('TOKENS='));
assert.ok(start>0);
html=html.slice(0,start)+fs.readFileSync(root+'/sources/art.js','utf8')+'</script>';
fs.writeFileSync(root+'/sources/render.html',html);
let browser=await openPage('file:///'+root+'/sources/render.html');
try{
 let status;for(let i=0;i<120;i++){status=await browser.evaluate('document.getElementById("result")?.textContent');if(status==='READY')break;if(status&&status!=='WAIT')throw Error(status);await sleep(250)}
 assert.equal(status,'READY');
 for(const f of await browser.evaluate('Object.keys(OUT)')){
  const data=Buffer.from(await browser.evaluate(`OUT[${JSON.stringify(f)}]`),'base64');
  if(allowed.has(f))fs.writeFileSync(root+'/'+f,data);
  else assert.equal(hash(data),baseline.hashes[f],f+' unchanged render');
 }
 const manifest=await browser.evaluate('MANIFEST');
 for(const p of manifest.pieces){const old=baseline.manifest.pieces.find(q=>q.piece===p.piece);assert.deepEqual(tracks.includes(p.piece)?{...p,notes:old.notes}:p,old);}
 fs.writeFileSync(root+'/kit-battle.json',JSON.stringify(manifest,null,2));
 const geometry=await browser.evaluate('GEOMETRY');
 for(const side of ['enemy','party'])assert.deepEqual(geometry.ticks[side].map(t=>[t.angle,t.long]),Array.from({length:24},(_,i)=>[i*15,i%2===0]));
 fs.writeFileSync(root+'/sources/geometry.json',JSON.stringify(geometry,null,2));
}finally{browser.close()}
browser=await openPage('file:///'+root+'/mockups/battle-ring.html',{width:1280,height:720});
try{
 for(let i=0;i<120;i++){if(await browser.evaluate('window.BATTLE_READY===true'))break;await sleep(250)}
 assert.equal(await browser.evaluate('window.BATTLE_READY===true'),true);
 await browser.shot(root+'/mockups/battle-ring.png');
 fs.writeFileSync(root+'/sources/proof-check.json',JSON.stringify(await browser.evaluate('window.PROOF_CHECK'),null,2));
}finally{browser.close()}
let unchanged=0;
for(const [f,h] of Object.entries(baseline.hashes))if(!allowed.has(f)){assert.equal(hash(fs.readFileSync(root+'/'+f)),h);unchanged++;}
fs.writeFileSync(root+'/sources/revision-verification.json',JSON.stringify({status:'pass',unchanged_other_piece_files:unchanged,backup_pngs:4,ticks_per_track:24,long_per_track:12,short_per_track:12,angles:'aligned, clockwise from top, every 15 degrees',manifest_changes:'two track notes only'},null,2));
console.log('BATTLE_V1B_RENDERED; 42 other piece files unchanged; four backups verified');
