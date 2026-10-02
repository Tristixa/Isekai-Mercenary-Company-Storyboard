import fs from 'node:fs';
import crypto from 'node:crypto';
const root='D:/Codex/IMC/runs/ui-battle-ring-v1';
const read=p=>fs.readFileSync(root+'/'+p,'utf8'),write=(p,s)=>fs.writeFileSync(root+'/'+p,s);
const dir=root+'/history/v1b-hub';fs.mkdirSync(dir,{recursive:true});
if(!fs.existsSync(dir+'/baseline.json')){
 const manifest=JSON.parse(read('kit-battle.json')),hashes={};
 for(const p of manifest.pieces)for(const f of [p.file,p.file_1x,'sources/generated/'+p.piece+'.png'])hashes[f]=crypto.createHash('sha256').update(fs.readFileSync(root+'/'+f)).digest('hex');
 write('history/v1b-hub/baseline.json',JSON.stringify({manifest,hashes},null,2));
 for(const suffix of ['.png','@1x.png'])fs.copyFileSync(root+'/kit/battle/tl_hub'+suffix,dir+'/tl_hub'+suffix);
}
let art=read('sources/art.js');
const start=art.indexOf(" make('tl_hub'"),end=art.indexOf(" for(const side",start);
art=art.slice(0,start)+` make('tl_act_plate',240,240,()=>{const [x,y]=pos(85.5,330);g.save();g.translate(x,y);g.rotate(-30*Math.PI/180);gildedPlate(0,0,36,18);g.restore()},{...ringOpts,notes:ringOpts.notes+' Blank gilded ACT plate centered at radius 85.5, angle 330 degrees, across both tracks in the 300-360 segment. Center [77.25,45.955] use; rotation -30 degrees; plate 36x18, local text-safe [-14,-6,28,12]. Engine ACT: 12px Cormorant Garamond SemiBold, centered, dark ink. Rotate with ACT zone.'});
 make('tl_hub',240,240,()=>{
  ring(120,38,7,gold());
  circle(120,120,32.2,grad(160,180,[[0,T.navy_700],[.45,T.navy_900],[1,T.navy_950]]),4.4);
  circle(120,120,30.5,T.navy_950,1);circle(120,120,33.8,T.parchment_300,.55);
  circle(120,120,39.8,T.gold_500,.6);texture(240,240,12,.17);
  for(const a of [45,135,225,315]){const [x,y]=pos(38,a);g.save();g.translate(x,y);g.rotate(a*Math.PI/180);tint(I.mask_header_flourish,-7,-1.65,14,3.3,T.parchment_100,.7);g.restore()}
  for(const a of [0,90,180,270]){const [x,y]=pos(38,a);circle(x,y,1.6,T.ink);circle(x,y,1.15,T.gold_400);circle(x-.3,y-.35,.45,T.parchment_100)}
  for(let s of [-1,1])for(let i=0;i<3;i++)leaf(120+s*(15+i*5),155-i*3,s*(20+i*16),.58);
  gildedPlate(120,158,36,16);tint(I.mask_header_flourish,111,166,18,3,T.gold_400,.85);
 },{...ringOpts,notes:ringOpts.notes+' Transparent 60px portrait opening, unchanged center. Rich gilded rim, restrained bezel filigree, four quarter-point studs, deeper navy field with soft inner bevel. Blank matching gilded NEXT plate centered [120,158], 36x16 use; text-safe [106,152,28,12]. No text or emblems baked in. Draw bust behind.'});
`+art.slice(end);
const helper=`function gildedPlate(x,y,w,h){g.save();g.translate(x,y);g.beginPath();g.moveTo(-w/2+3,-h/2);g.lineTo(w/2-3,-h/2);g.lineTo(w/2,0);g.lineTo(w/2-3,h/2);g.lineTo(-w/2+3,h/2);g.lineTo(-w/2,0);g.closePath();g.fillStyle=grad(0,h,[[0,T.parchment_200],[.45,T.gold_400],[1,T.gold_500]]);g.fill();g.strokeStyle=T.ink;g.lineWidth=1.5;g.stroke();g.save();g.clip();texture(w,h,73,.12);g.restore();line(-w/2+4,-h/2+1.5,w/2-4,-h/2+1.5,T.parchment_100,.7);line(-w/2+4,h/2-1.5,w/2-4,h/2-1.5,T.ink,.65);g.restore()}
`;
art=art.replace('function timeline(){',helper+'function timeline(){').replace('canvas(2080,1650)','canvas(2080,2030)');write('sources/art.js',art);
let proof=read('sources/proof.js').replace("const names=['tl_bezel'","const names=['tl_act_plate','tl_bezel'");
proof=proof.replace("txt(g,'NEXT',120,158,8);txt(g,'ACT',57,16,10,'#F1E2BC');",`draw(g,'tl_act_plate',0,0,240,240);g.save();g.textAlign='center';g.textBaseline='middle';g.font="600 11px 'Cormorant Garamond'";g.fillStyle='#2A2117';g.fillText('NEXT',120,158);g.translate(77.25,120-85.5*Math.cos(Math.PI/6));g.rotate(-Math.PI/6);g.font="600 12px 'Cormorant Garamond'";g.fillText('ACT',0,0);g.restore();`);
write('sources/proof.js',proof);
let html=read('mockups/battle-ring.html');const ps=html.lastIndexOf('(async()=>{');html=html.slice(0,ps)+proof+'</script></body></html>';write('mockups/battle-ring.html',html);
let v=read('sources/verify.mjs').replace("const required=['tl_bezel'","const required=['tl_act_plate','tl_bezel'").replaceAll('[2080,1650]','[2080,2030]');write('sources/verify.mjs',v);
write('sources/verify-delivery.mjs',read('sources/verify-delivery.mjs').replace('ui-battle-ring-v1b-last.txt','ui-battle-ring-v1c-last.txt'));
