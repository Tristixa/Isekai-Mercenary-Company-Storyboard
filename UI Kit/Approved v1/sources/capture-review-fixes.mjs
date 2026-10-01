import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {openPage} from './cdp.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const manifest=JSON.parse(fs.readFileSync(root+'/kit.json'));
const items=manifest.pieces.filter(p=>p.group==='tier2');
const browser=await openPage('about:blank',{width:1440,height:650});
try{
const assets={};for(const file of ['sheets/tier2.png','mockups/mock-ledger.png',...['stun','reputation','leadership','boss','ongoing','time'].map(n=>'kit/icons/'+n+'_24.png')])assets[file]=fs.readFileSync(root+'/'+file).toString('base64');
await browser.evaluate(`(async()=>{
 const assets=${JSON.stringify(assets)},items=${JSON.stringify(items)};
 document.body.style.margin='0';const c=document.createElement('canvas');c.width=1440;c.height=650;document.body.append(c);const g=c.getContext('2d');g.fillStyle='#F1E2BC';g.fillRect(0,0,1440,650);
 const images={};for(const [file,b64]of Object.entries(assets)){const im=new Image();im.src='data:image/png;base64,'+b64;await im.decode();images[file]=im}
 g.fillStyle='#2A2117';g.font='24px Georgia';g.fillText('Fixes 2026-09-28 / native export detail',24,34);
 for(const [j,name]of ['stamp_accepted','stamp_complete','stamp_expired','rare_badge'].entries()){const i=items.findIndex(p=>p.piece===name);g.drawImage(images['sheets/tier2.png'],0,120+i*220,350,155,j*360,60,350,155)}
 for(const [j,pair]of [['stun','reputation'],['leadership','boss'],['ongoing','time']].entries()){const x=24+j*460;g.fillStyle='#2A2117';g.fillText(pair.join(' / '),x,252);for(const [k,n]of pair.entries()){const im=images['kit/icons/'+n+'_24.png'];g.drawImage(im,x+k*150,270);g.imageSmoothingEnabled=false;g.drawImage(im,x+k*150,310,96,96);g.imageSmoothingEnabled=true}}
 g.fillStyle='#2A2117';g.fillText('Selected Roster / hovered Requests',24,451);g.drawImage(images['mockups/mock-ledger.png'],1420,305,400,200,24,460,400,190);
 g.fillText('Native 24 px glyphs above; 4x pixel inspection below.',500,460);
})()`);
await browser.shot(root+'/sources/review-fixes-detail.png');
}finally{browser.close()}
