import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const v5=path.resolve(root,'../ui-style-test-v5');
const project='D:/Storyboards/Isekai Mercenary Company';
const inputs={};
function source(key,file){inputs[key]=file}
for(const [key,file] of Object.entries({world:'HD-2D Proof/out/style-test/A-tavern.png',forest:'Environment Assets/Hylaea/Codex Concept.png',commander:'Characters/Officers/Commander(Player Character)/Base.png',mae:'Characters/Officers/Steady Mae/Happy.png',elsie:'Characters/Officers/Elsie/Base.png',wolf:'Enemy Sprites/Forest Wolf/Idle.png',boar:'Enemy Sprites/Boar/Start - Idle.png'}))source(key,project+'/'+file);
for(const n of ['Anselm Voigt','Nell Larkin','Severa Kaltenbach','Otto Grimbald']){
 source('left_'+n,v5+'/sources/display-grid-'+n.replaceAll(' ','-')+'-3.png');
 const dir=project+'/Character Sprites/Recruitable Staff/Adventurers/'+n+'/';
 source('front_'+n,fs.existsSync(dir+'Idle Front - Native.png')?dir+'Idle Front - Native.png':fs.existsSync(dir+'Idle Front.png')?dir+'Idle Front.png':dir+'Base Sprite - Native.png');
 source('full_'+n,fs.existsSync(dir+'Idle Left - Native.png')?dir+'Idle Left - Native.png':dir+'Idle Left.png');
}
for(const [key,file] of Object.entries({ribbon:'pieces/tier-1/title-ribbon.png',clock:'pieces/tier-1/clock-medallion-wreath.png',quill:'pieces/tier-2/quill.png',selection:'pieces/tier-2/selected-row-glow.png',watermark:'layers/watermark.png'}))source(key,v5+'/'+file);
for(const n of ['corner-large','corner-small','lattice','diamond-row','header-flourish','help-end','ribbon-left','ribbon-right'])source('mask_'+n.replaceAll('-','_'),v5+'/pieces/masks/'+n+'.png');
for(let i=1;i<=8;i++)source('stain_'+i,v5+'/layers/stains/stain-'+i+'.png');
const fonts=[['Heading','CormorantGaramond-SemiBold.otf',600],['Body','Alegreya[wght].ttf','400 900']];
source('forest',project+'/Environment Assets/Hylaea/Approved Calibration v1/logical/Far Background.png');
source('forest_ground',project+'/Environment Assets/Hylaea/Approved Calibration v1/logical/Ground Tile.png');
source('tavern',project+'/Locations/Eurydica/concepts/eurydica-tavern-interior-approved.png');
fs.mkdirSync(root+'/sources/fonts',{recursive:true});fs.mkdirSync(root+'/sources/reused',{recursive:true});
const provenance=[];
for(const [key,file]of Object.entries(inputs)){
 const target='sources/reused/'+key.toLowerCase().replaceAll(' ','_')+'.png';
 const bytes=fs.readFileSync(file);fs.writeFileSync(root+'/'+target,bytes);
 provenance.push({key,source:file,file:target,sha256:crypto.createHash('sha256').update(bytes).digest('hex')});
}
let fontCSS='';
for(const [family,file,weight]of fonts){const bytes=fs.readFileSync(v5+'/fonts/'+file);fs.writeFileSync(root+'/sources/fonts/'+file,bytes);fontCSS+=`@font-face{font-family:${family};src:url(data:font/${file.endsWith('otf')?'otf':'ttf'};base64,${bytes.toString('base64')});font-weight:${weight};font-feature-settings:"lnum" 1,"onum" 0;}\n`;}
for(const name of ['alegreya-OFL.txt','cormorantgaramond-OFL.txt'])fs.copyFileSync(v5+'/fonts/'+name,root+'/sources/fonts/'+name);
fs.writeFileSync(root+'/sources/provenance.json',JSON.stringify(provenance,null,2));
// Reuse v5's local browser renderer; its profile directory is relocated into this run.
fs.writeFileSync(root+'/sources/cdp.mjs',fs.readFileSync(v5+'/cdp.mjs','utf8').replaceAll('D:/Codex/IMC/runs/ui-style-test-v5',root.replaceAll('\\','/')));
fs.copyFileSync(v5+'/compose.js',root+'/sources/v5_compose_reference.js');
fs.copyFileSync(v5+'/design.js',root+'/sources/v5_design_reference.js');
const sources=Object.fromEntries(provenance.map(p=>[p.key,'data:image/png;base64,'+fs.readFileSync(root+'/'+p.file).toString('base64')]));
const logic=fs.readFileSync(root+'/sources/kit.js','utf8');
fs.writeFileSync(root+'/sources/render.html',`<!doctype html><meta charset="utf-8"><style>${fontCSS}body{margin:0;font-variant-numeric:lining-nums}</style><pre id="result">WAIT</pre><script>const SOURCES=${JSON.stringify(sources)};${logic}</script>`);
const {openPage,sleep}=await import('./cdp.mjs');
const browser=await openPage('file:///'+root.replaceAll('\\','/')+'/sources/render.html',{width:1920,height:1080});
try{
 let status;for(let i=0;i<180;i++){status=await browser.evaluate('document.getElementById("result").textContent');if(status!=='WAIT')break;await sleep(300)}
 if(status!=='READY')throw Error(status+' '+browser.logs.join('\n'));
 for(const file of await browser.evaluate('Object.keys(OUT)')){const b64=await browser.evaluate(`OUT[${JSON.stringify(file)}]`);fs.mkdirSync(path.dirname(root+'/'+file),{recursive:true});fs.writeFileSync(root+'/'+file,Buffer.from(b64,'base64'));}
 for(const [file,expr] of [['kit.json','MANIFEST'],['sources/qa.json','QA']])fs.writeFileSync(root+'/'+file,JSON.stringify(await browser.evaluate(expr),null,2));
 console.log('BUILD_OK',await browser.evaluate('MANIFEST.pieces.length'), 'pieces;',await browser.evaluate('Object.keys(OUT).length'),'PNGs');
}finally{browser.close()}
