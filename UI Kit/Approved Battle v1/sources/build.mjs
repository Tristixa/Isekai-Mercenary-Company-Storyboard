import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..').replaceAll('\\','/');
const old='D:/Codex/IMC/runs/ui-kit-v1', mock='D:/Codex/IMC/runs/battle-ui-mockup-v2';
const approved='D:/Storyboards/Isekai Mercenary Company/UI Kit/Approved v1';
const provenance=[];
function copy(src,dest){const b=fs.readFileSync(src);fs.mkdirSync(path.dirname(root+'/'+dest),{recursive:true});fs.writeFileSync(root+'/'+dest,b);provenance.push({source:src,file:dest,sha256:crypto.createHash('sha256').update(b).digest('hex')});}
for(const n of ['clock','mask_header_flourish','mask_corner_small','stain_1'])copy(old+'/sources/reused/'+n+'.png','sources/reused/'+n+'.png');
for(const n of ['bg','boar','bust0','bust1','bust2'])copy(mock+'/'+n+'.png','sources/reused/'+n+'.png');
for(const n of ['CormorantGaramond-SemiBold.otf','Alegreya[wght].ttf','alegreya-OFL.txt','cormorantgaramond-OFL.txt'])copy(old+'/sources/fonts/'+n,'sources/fonts/'+n);
for(const n of ['README.md','Codex run notes.md','kit.json'])copy(approved+'/'+n,'sources/approved/'+n);
for(const n of ['mockup.html','mockup-battle.png','zoom-ring.png','zoom-party.png'])copy(mock+'/'+n,'sources/reference/'+n);
copy('D:/Download/battlemenu-grandia.jpg','sources/reference/grandia.jpg');
copy("C:/Users/Tristixa-/Pictures/Screenshots/Ignore the blue symbol at bottom right, it's the channel logo.png",'sources/reference/kh-gauge.png');
copy(old+'/sources/kit.js','sources/reference/approved-kit.js');
fs.writeFileSync(root+'/sources/provenance.json',JSON.stringify(provenance,null,2));
fs.writeFileSync(root+'/sources/cdp.mjs',fs.readFileSync(old+'/sources/cdp.mjs','utf8').replaceAll(old,root));
const input=Object.fromEntries(provenance.filter(p=>p.file.startsWith('sources/reused')).map(p=>[path.basename(p.file,'.png'),'data:image/png;base64,'+fs.readFileSync(root+'/'+p.file).toString('base64')]));
const manifest=JSON.parse(fs.readFileSync(approved+'/kit.json'));
const fonts=`@font-face{font-family:Heading;src:url('fonts/CormorantGaramond-SemiBold.otf');font-weight:600}@font-face{font-family:Body;src:url('fonts/Alegreya[wght].ttf');font-weight:400 900}`;
fs.writeFileSync(root+'/sources/render.html',`<!doctype html><meta charset="utf-8"><style>${fonts}body{margin:0}</style><pre id="result">WAIT</pre><script>const INPUT=${JSON.stringify(input)},TOKENS=${JSON.stringify(manifest.tokens)};${fs.readFileSync(root+'/sources/art.js','utf8')}</script>`);
const {openPage,sleep}=await import('./cdp.mjs');
let browser=await openPage('file:///'+root+'/sources/render.html');
try{
 let status;for(let i=0;i<120;i++){status=await browser.evaluate('document.getElementById("result").textContent');if(status!=='WAIT')break;await sleep(250)}
 if(status!=='READY')throw Error(status+' '+browser.logs.join('\n'));
 for(const file of await browser.evaluate('Object.keys(OUT)')){fs.mkdirSync(path.dirname(root+'/'+file),{recursive:true});fs.writeFileSync(root+'/'+file,Buffer.from(await browser.evaluate(`OUT[${JSON.stringify(file)}]`),'base64'));}
 fs.writeFileSync(root+'/kit-battle.json',JSON.stringify(await browser.evaluate('MANIFEST'),null,2));
 fs.writeFileSync(root+'/sources/geometry.json',JSON.stringify(await browser.evaluate('GEOMETRY'),null,2));
}finally{browser.close()}
// Preserve the original layout document, replacing only the ring and gauge placeholders.
let html=fs.readFileSync(mock+'/mockup.html','utf8').replace(/<link href="https:[^>]+>/,'');
html=html.replace('</style>',`@font-face{font-family:'Cormorant Garamond';src:url('../sources/fonts/CormorantGaramond-SemiBold.otf');font-weight:600 700}@font-face{font-family:'Alegreya Sans';src:url('../sources/fonts/Alegreya[wght].ttf');font-weight:400 900}\n.stage{background-image:url('../sources/reused/bg.png')}\n.tl{width:240px;height:240px}.tl canvas{width:240px;height:240px}.ring canvas{width:104px;height:104px}.ring .skillfull{background:none;padding:0;box-shadow:none;width:48px;height:18px;display:grid;place-items:center;right:-6px;bottom:-2px;font-size:10px;color:#07131f}.ring .skillfull:before{content:'';position:absolute;inset:0;background:url('../kit/battle/gauge_skill_ready.png') center/100% 100%;z-index:-1}.tag{font-size:15px}\n</style>`);
html=html.replace(/src="(bust\d|boar)\.png"/g,'src="../sources/reused/$1.png"');
const proof=fs.readFileSync(root+'/sources/proof.js','utf8');
html=html.replace('</body>',`<script>${proof}</script></body>`);
fs.mkdirSync(root+'/mockups',{recursive:true});fs.writeFileSync(root+'/mockups/battle-ring.html',html);
browser=await openPage('file:///'+root+'/mockups/battle-ring.html',{width:1280,height:720});
try{for(let i=0;i<120;i++){if(await browser.evaluate('window.BATTLE_READY===true'))break;await sleep(250)}if(!await browser.evaluate('window.BATTLE_READY===true'))throw Error(browser.logs.join('\n'));await browser.shot(root+'/mockups/battle-ring.png');fs.writeFileSync(root+'/sources/proof-check.json',JSON.stringify(await browser.evaluate('window.PROOF_CHECK'),null,2));}finally{browser.close()}
console.log('BUILD_COMPLETE');
