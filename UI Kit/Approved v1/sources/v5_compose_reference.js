const W=1920,H=1080,P='#F1E2BC',INK='#2A2117',GOLD='#E0B04A';
const names=['Anselm Voigt','Nell Larkin','Severa Kaltenbach','Otto Grimbald'];
const output={},qa={text:[],sprites:[],pieces:[],notes:[]};let ctx,variant,screen;
const canvas=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return c};
const exportPNG=(name,c)=>output[name]=c.toDataURL('image/png').split(',')[1];
const rgb=h=>h.match(/[0-9a-f]{2}/gi).map(n=>parseInt(n,16));
const lum=a=>a.map(n=>{n/=255;return n<=.04045?n/12.92:((n+.055)/1.055)**2.4}).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0);
const contrast=(a,b)=>{a=lum(rgb(a));b=lum(rgb(b));return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)};
function rect(x,y,w,h,col){ctx.fillStyle=col;ctx.fillRect(x,y,w,h)}
function line(x,y,x2,y2,col='#A68D60',width=1){ctx.strokeStyle=col;ctx.lineWidth=width;ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x2,y2);ctx.stroke()}
function text(s,x,y,size=26,{font='Alegreya',color=INK,bg=P,align='left',role='body',angle=0}={}){
 font=font==='Marcellus'?PAIR.heading:font==='Alegreya'?PAIR.body:font; const weight=font===PAIR.heading?PAIR.weight:400; ctx.save();ctx.fillStyle=color;ctx.font=`${weight} ${size}px ${font}`;ctx.textBaseline='middle';ctx.textAlign=align;
 const width=ctx.measureText(s).width; const m=ctx.measureText(s); const glyphBox={left:m.actualBoundingBoxLeft,right:m.actualBoundingBoxRight,ascent:m.actualBoundingBoxAscent,descent:m.actualBoundingBoxDescent};ctx.translate(x,y);ctx.rotate(angle);ctx.fillText(s,0,0);ctx.restore();
 qa.text.push({variant,screen,text:s,x,y,size,font,color,bg,align,role,width,glyphBox,pairing:PAIR.id,contrast:contrast(color,bg)});
}
function heading(s,x,y,size=30,extra={}){text(s,x,y,size,{font:'Marcellus',role:'header',...extra})}
function diamond(x,y,size,col){ctx.fillStyle=col;ctx.beginPath();ctx.moveTo(x,y-size);ctx.lineTo(x+size,y);ctx.lineTo(x,y+size);ctx.lineTo(x-size,y);ctx.closePath();ctx.fill()}
let assets={},I={};
const masks={},shapes={};
const opacity=()=>variant==='A'?.35:.525;
function path(points,col,width=1,close=false,fill=false){ctx.beginPath();points.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));if(close)ctx.closePath();ctx.strokeStyle=col;ctx.lineWidth=width;if(fill){ctx.fillStyle=col;ctx.fill()}else ctx.stroke()}
function mask(name,w,h,draw,shape=false){const old=ctx,c=canvas(w,h);ctx=c.getContext('2d');draw(w,h);(shape?shapes:masks)[name]=c;exportPNG('pieces/'+(shape?'shapes/':'masks/')+name+'.png',c);qa.pieces.push({name,width:w,height:h,kind:shape?'shape':'mask'});ctx=old}
function makeAssets(){
 drawnAssets();
 mask('quill',37,62,()=>{path([[4,57],[10,29],[33,3],[31,25],[4,57]],'#FFFFFF',2);line(4,57,30,9,'#FFFFFF',2);for(let i=0;i<5;i++)line(10+i*4,43-i*7,24+i*2,35-i*6,'#FFFFFF',1)});
 mask('quill-tip',37,62,()=>path([[3,60],[5,47],[12,52]],'#FFFFFF',1,true,true));
 mask('card',320,240,()=>rect(1,1,318,238,'#FFFFFF'),true);
 mask('band',320,68,()=>rect(1,1,318,66,'#FFFFFF'),true);
 mask('ribbon-body',493,128,()=>path([[4,23],[483,2],[469,111],[17,126],[37,75]],'#FFFFFF',1,true,true),true);
 mask('help-ribbon-body',1117,73,()=>path([[2,36],[95,4],[1022,4],[1115,36],[1022,69],[95,69]],'#FFFFFF',1,true,true),true);
 mask('button-hint-tab',208,61,()=>path([[18,1],[207,1],[193,60],[1,60]],'#FFFFFF',1,true,true),true);
 mask('stat-plate',320,72,()=>path([[10,1],[310,1],[319,10],[319,62],[310,71],[10,71],[1,62],[1,10]],'#FFFFFF',1,true,true),true);
 mask('minimap-ring',242,242,()=>{ctx.strokeStyle='#FFFFFF';ctx.lineWidth=2;ctx.beginPath();ctx.arc(121,121,112,0,7);ctx.stroke()},true);
 mask('face-frame',144,144,()=>{ctx.strokeStyle='#FFFFFF';ctx.lineWidth=2;ctx.strokeRect(5,5,134,134);ctx.lineWidth=1;ctx.strokeRect(10,10,124,124)},true);
 mask('select-band',852,137,()=>rect(1,1,850,135,'#FFFFFF'),true);
}
function tint(im,x,y,w,h,col,alpha=1){const c=canvas(im.width,im.height),g=c.getContext('2d');g.drawImage(im,0,0);g.globalCompositeOperation='source-in';g.fillStyle=col;g.fillRect(0,0,c.width,c.height);ctx.save();ctx.globalAlpha=alpha;ctx.drawImage(c,x,y,w,h);ctx.restore()}
function ornament(n,x,y,w,h,col='#D7CCC8',a=opacity()){const m=ctx.getTransform(),p=[[x,y],[x+w,y],[x,y+h],[x+w,y+h]].map(([a,b])=>[m.a*a+m.c*b+m.e,m.b*a+m.d*b+m.f]);(qa.decorations??=[]).push({variant,screen,n,alpha:a,color:col,box:[Math.min(...p.map(a=>a[0])),Math.min(...p.map(a=>a[1])),Math.max(...p.map(a=>a[0])),Math.max(...p.map(a=>a[1]))]});tint(masks[n],x,y,w,h,col,a)}
function piece(n,x,y,w,h){
 if(n==='small-face-frame'){tint(shapes['face-frame'],x,y,w,h,'#A68D60');return}
 if(n==='quill'){tint(masks.quill,x,y,w,h,INK);tint(masks['quill-tip'],x,y,w,h,GOLD);return}
 if(n==='clock-medallion-wreath'){ctx.save();ctx.globalAlpha=.9;ctx.fillStyle=P;ctx.beginPath();ctx.arc(x+w/2,y+h/2,w*.49,0,7);ctx.fill();ctx.restore();ornament('clock-wreath',x,y,w,h,'#A68D60');return}
 if(n==='minimap-ring'){tint(shapes[n],x,y,w,h,'#A68D60');return}
 if(n==='selected-row-glow'){tint(shapes['select-band'],x,y,w,h,'#DCEBEE');line(x,y,x,y+h,'#3F6EC1',3);return}
 if(n==='title-ribbon'){titleRibbon(x,y,w,h);return;} if(false){tint(shapes['ribbon-body'],x,y,w,h,'#102B45');ornament('ribbon-end',x+46,y+24,50,h-47,'#3F6EC1');ornament('ribbon-end',x+w-85,y+13,45,h-35,'#3F6EC1');return}
 if(n==='help-ribbon'){helpRibbon(x,y,w,h);return;} if(false){tint(shapes['help-ribbon-body'],x,y,w,h,P);ornament('help-ribbon-end',x,y+4,85,h-8);ctx.save();ctx.translate(x+w,y);ctx.scale(-1,1);ornament('help-ribbon-end',0,4,85,h-8);ctx.restore();return}
 if(n==='button-hint-tab'){tint(shapes[n],x,y,w,h,P,screen==='world-hud'?.9:1);path([[x+18,y],[x+w*.29,y],[x+w*.23,y+h],[x,y+h]],'#102B45',1,true,true);return}
}
function card(x,y,w,h){rect(x,y,w,h,P);ctx.strokeStyle='#A68D60';ctx.lineWidth=1;ctx.strokeRect(x+.5,y+.5,w-1,h-1);ctx.save();ctx.globalAlpha=.5;ctx.strokeRect(x+4.5,y+4.5,w-9,h-9);ctx.restore();tile('diamond-row',x+9,y+2,w-18,7,'#A68D60',strength(.4));for(const [xx,yy,sx,sy]of [[x+9,y+9,1,1],[x+w-9,y+9,-1,1],[x+9,y+h-9,1,-1],[x+w-9,y+h-9,-1,-1]]){ctx.save();ctx.translate(xx,yy);ctx.scale(sx,sy);ctx.beginPath();ctx.rect(0,0,28,150);ctx.rect(0,0,150,20);ctx.clip();ornament('corner-large',0,0,150,150,'#A68D60');ctx.restore()}}
function plate(x,y,w,h){tint(shapes['stat-plate'],x,y,w,h,P,screen==='world-hud'?.9:1);ornament('corner-small',x+4,y+4,31,31);ctx.save();ctx.translate(x+w-4,y+h-4);ctx.rotate(Math.PI);ornament('corner-small',0,0,31,31);ctx.restore()}
function header(s,x,y,w){rect(x,y,w,68,'#102B45');tile('lattice',x,y,w,68,'#3F6EC1',strength(.14));ornament('header-flourish',x+12,y+21,78,26,'#3F6EC1',strength(.4));ornament('header-flourish',x+w-154,y+17,140,38,'#3F6EC1',strength(.4));line(x,y+67,x+w,y+67,'#A68D60');tile('diamond-row',x,y+69,w,9,'#A68D60',strength(.4));heading(s,x+110,y+38,30,{color:'#F1E2BC',bg:'#102B45'})}
// The approved PNGs are enlarged exports. Reduce once to a display grid,
// then enlarge by exact whole numbers. Full source is retained before chest clipping.
const grids={'Anselm Voigt':{div:8,cx:29,top:3},'Nell Larkin':{div:9,cx:20,top:11},'Severa Kaltenbach':{div:10,cx:39,top:2},'Otto Grimbald':{div:8,cx:36,top:3}};
function face(n,x,y,scale=3){const im=I[n],cfg=scale===4?{div:11,cx:16,top:9}:grids[n],c=canvas(Math.round(im.width/cfg.div),Math.round(im.height/cfg.div)),g=c.getContext('2d');g.imageSmoothingEnabled=false;g.drawImage(im,0,0,c.width,c.height);const d=g.getImageData(0,0,c.width,c.height);for(let i=0;i<d.data.length;i+=4){const r=d.data[i],v=d.data[i+1],b=d.data[i+2];if((r>180&&v<70&&b>180)||(r<90&&v>140&&b<90))d.data[i+3]=0;}g.putImageData(d,0,0);exportPNG('sources/display-grid-'+n.replaceAll(' ','-')+'-'+scale+'.png',c);ctx.drawImage(faceBacking,x-7,y-10,160,154);ctx.save();ctx.beginPath();ctx.rect(x+4,y+(scale===4?6:-6),136,140);ctx.clip();ctx.imageSmoothingEnabled=false;const dx=x+72-cfg.cx*scale,dy=y+(scale===4?8:-4)-cfg.top*scale;ctx.drawImage(c,dx,dy,c.width*scale,c.height*scale);ctx.restore();qa.sprites.push({variant,screen,name:n,scale,nearest:true,source:[im.width,im.height],grid:[c.width,c.height],reductionDivisor:cfg.div,draw:[dx,dy,c.width*scale,c.height*scale],clip:[x+10,y+10,124,124]})}
function minimap(){const mx=1782,my=144;ctx.save();ctx.beginPath();ctx.arc(mx,my,110,0,7);ctx.clip();ctx.globalAlpha=.9;rect(mx-112,my-112,224,224,P);ctx.globalAlpha=1;
 path([[mx-112,my+50],[mx-64,my+40],[mx-35,my+53],[mx+4,my+82],[mx+67,my+71],[mx+111,my+92]],'#DCEBEE',21);
 path([[mx-108,my-25],[mx-69,my-42],[mx-15,my-39],[mx+27,my-2],[mx+82,my+13],[mx+110,my+1]],'#A68D60',10);
 path([[mx-17,my-105],[mx-19,my-68],[mx-15,my-39],[mx-37,my+8],[mx-34,my+51],[mx-60,my+101]],'#A68D60',9);
 path([[mx-37,my+8],[mx+20,my+30],[mx+59,my+4],[mx+73,my-61]],'#A68D60',8);
 for(const [x,y,w,h]of [[-81,-78,38,25],[-5,-83,36,25],[46,-77,33,39],[-89,0,29,29],[-9,-11,21,23],[54,30,35,26],[-8,46,27,17]]){rect(mx+x,my+y,w,h,'#D2B77D');ctx.strokeStyle='#A68D60';ctx.strokeRect(mx+x,my+y,w,h)}
 ctx.strokeStyle='#A68D60';ctx.lineWidth=1;ctx.beginPath();ctx.arc(mx+35,my-34,23,0,7);ctx.stroke();for(const [x,y,r]of [[29,-38,9],[39,-40,8],[35,-30,10]]){ctx.fillStyle='#E15A5A';ctx.beginPath();ctx.arc(mx+x,my+y,r,0,7);ctx.fill()}
 path([[mx-31,my+31],[mx-23,my+12],[mx-15,my+31],[mx-23,my+26]],'#102B45',1,true,true);ctx.restore();piece('minimap-ring',1661,24,242,242)}

function hint(key,label,x,y,w=208){piece('button-hint-tab',x,y,w,61);text(key,x+w*.16,y+31,24,{align:'center',color:'#F1E2BC',bg:'#102B45'});text(label,x+w*.34,y+31,25)}
function stamina(x,y,count){for(let i=0;i<4;i++){rect(x+i*30,y,25,15,'#D2B77D');ctx.strokeStyle=INK;ctx.lineWidth=1;ctx.strokeRect(x+i*30,y,25,15);if(i<count)rect(x+i*30+2,y+2,21,11,'#102B45')}}
function worldBackground(blur=false){ctx.save();if(blur)ctx.filter='blur(6px)';const im=I.world;const scale=Math.max(W/im.width,H/im.height);ctx.drawImage(im,(W-im.width*scale)/2,(H-im.height*scale)/2,im.width*scale,im.height*scale);ctx.restore();if(blur){ctx.save();ctx.globalAlpha=.30;rect(0,0,W,H,INK);ctx.restore()}}
function world(){screen='world-hud';const c=canvas(W,H);ctx=c.getContext('2d');worldBackground();
 piece('clock-medallion-wreath',28,22,198,198);
 ctx.strokeStyle=GOLD;ctx.lineWidth=4;ctx.beginPath();ctx.arc(126,119,68,-Math.PI/2,-Math.PI/2+Math.PI*2*((14+20/60-7)/13));ctx.stroke();
 text('DAY',126,80,22,{align:'center'});text('3',126,113,44,{align:'center',role:'number'});text('14:20',126,152,27,{align:'center',role:'number'});
 plate(225,34,707,99);text('Purse',255,62,22);text('2,500 G',385,97,31,{align:'right',role:'number'});text('Rep',441,62,22);text('0',467,97,31,{align:'right',role:'number'});text('Morale',541,62,22);text('60',604,97,31,{align:'right',role:'number'});text('Rank',710,62,22);text('F',766,97,31,{align:'right'});
 for(const x of [414,511,671])line(x,61,x,106,'#A68D60');
 plate(238,140,337,61);text('Pause',279,172,24);for(const [i,s]of ['1x','2x','4x'].entries()){if(i===0){rect(360,153,53,36,'#102B45');line(360,190,413,190,'#DCEBEE',3)}text(s,385+i*62,172,26,{align:'center',role:'number',color:i===0?P:INK,bg:i===0?'#102B45':P})}
 plate(583,140,347,61);text('Battle pace',612,172,24);text('1x',881,172,26,{align:'right',role:'number'});
 for(const [j,label]of ['Meet Mae at the tavern','Boarhide Vest for Anselm'].entries()){const y=239+j*68;plate(36,y,610,62);text(j===0?'Objective':'Pinned',62,y+32,24);line(162,y+17,162,y+45,'#A68D60');text(label,180,y+32,27)}
 plate(36,388,536,69);rect(54,408,6,26,'#E15A5A');text('Alert',75,424,25);text('Operation returned',157,424,27);
 minimap();
 plate(1643,259,265,61);text('N  ·  Eurydica',1775,291,25,{align:'center'});
 hint('E','Talk',879,421,154);hint('Tab','Ongoing',1442,984,222);hint('Esc','Ledger',1675,984,207);
 exportPNG(variant+'/world-hud.png',c);return c;
}
function section(label,x,y){const grad=ctx.createLinearGradient(x,0,x+690,0);grad.addColorStop(0,'#D2B77D');grad.addColorStop(1,'#D2B77D00');ctx.fillStyle=grad;ctx.fillRect(x-8,y-20,720,40);ornament('section-icon',x+170,y-14,28,28,'#A68D60',strength(.4));heading(label,x,y,29)}
function roster(){screen='roster';const c=canvas(W,H);ctx=c.getContext('2d');worldBackground(true);
 piece('title-ribbon',22,13,493,128);heading('Roster',248,77,45,{color:'#F1E2BC',bg:'#102B45',align:'center',angle:-.055});
 plate(80,137,254,72);ctx.save();ctx.beginPath();ctx.arc(117,173,25,0,7);ctx.clip();rect(89,143,56,56,P);ctx.drawImage(I.elsie,390,150,285,285,89,145,54,54);ctx.restore();heading('Elsie',160,174,28);
 tabs();
 plate(1606,144,265,61);icon('time',1627,162,28);text('Clock paused',1750,176,24,{align:'center'});
 card(35,236,903,720);header('Adventurers',49,246,875);heading('Name',230,337,28);heading('HP',729,337,28,{align:'right'});heading('Stamina',766,337,28);
 const hp=['180/180','120/150','90/175','205/205'];const jobs=['Vanguard','Ranger','Warden','Breaker'];
 for(let i=0;i<4;i++){const y=365+i*140;
 if(i===1)piece('selected-row-glow',57,y-2,852,137);
 face(names[i],74,y-4);const bg=i===1?'#DCEBEE':P;heading(names[i],234,y+43,29,{bg});text(jobs[i],234,y+87,24,{bg});
 ctx.save();ctx.font=`${PAIR.weight} 29px ${PAIR.heading}`;ctx.globalAlpha=.4;ctx.setLineDash([2,6]);line(234+ctx.measureText(names[i]).width+14,y+46,616,y+46,INK);ctx.restore();
 text(hp[i],738,y+45,28,{align:'right',role:'number',bg});stamina(766,y+36,[3,2,1,4][i]);
 if(i===2)text('! Fatigued',766,y+87,22,{bg});else text(['Ready','Selected','','Ready'][i],766,y+87,22,{bg});
 if(i===1)piece('quill',35,y+32,44,64);if(i<3){line(226,y+129,891,y+129,'#FFF4D8');line(226,y+130,891,y+130,'#B49A68');}
 }
 rect(916,365,4,535,'#D2B77D');rect(916,365,4,535,'#A68D60');rect(778,905,113,27,P);text('1–4 of 4',884,918,24,{align:'right',role:'number'});
 card(1008,236,874,720);header('Adventurer dossier',1022,246,846);face('Nell Larkin',1045,326,4);
 heading('Nell Larkin',1221,357,37);text('Ranger  ·  Ranged',1221,402,27);text('Available',1221,442,25);text('Rank',1789,356,24,{align:'right'});icon('rank',1803,340,32);line(1047,489,1840,489);
 section('Condition',1047,522);icon('hp',1047,551,28);text('HP',1083,565,26);text('120 / 150',1404,565,29,{align:'right',role:'number'});bar(1121,582,283,16,.8,'#43A65E');icon('stamina',1446,551,28);text('Stamina',1480,565,26);stamina(1702,558,2);
 section('Attributes',1047,629);for(const [i,[label,value,fraction]]of [['ATK','16',.64],['DEF','8',.32],['Rate','1.0',.5]].entries()){const y=673+i*43;text(label,1047,y,26);bar(1236,y-8,323,16,fraction,'#648CA8');text(value,1640,y,28,{align:'right',role:'number'})}
 line(1047,784,1840,784);section('Tracker',1047,816);text('+10% chance of a group of the hunt target;',1047,850,25);text('+10% find chance when scouting',1047,880,25);
 hint('X','Rest',1661,881,194);
 piece('help-ribbon',306,980,1117,73);icon('info',379,1003,28);text('Rest restores all four stamina bars at day’s end.',864,1019,25,{align:'center',role:'help'});hint('Esc','Back',1648,984,223);
 exportPNG('roster.png',c);return c;
}
const strength=a=>a*(variant==='B'?1.5:1);
function processed(name,w,h,crop){
 const im=I['draw-'+name],c=canvas(im.width,im.height),g=c.getContext('2d');g.drawImage(im,0,0);
 const d=g.getImageData(0,0,c.width,c.height);let l=c.width,t=c.height,r=0,b=0;
 for(let y=0;y<c.height;y++)for(let x=0;x<c.width;x++){let i=(y*c.width+x)*4;const a=(d.data[i]+d.data[i+1]+d.data[i+2])/3<175?255:0;d.data[i]=d.data[i+1]=d.data[i+2]=255;d.data[i+3]=a;if(a){l=Math.min(l,x);r=Math.max(r,x);t=Math.min(t,y);b=Math.max(b,y)}}g.putImageData(d,0,0);
 const box=crop?crop.map((v,i)=>v*(i%2?c.height:c.width)):[l,t,r-l+1,b-t+1];
 const out=canvas(w,h),o=out.getContext('2d');o.imageSmoothingEnabled=true;o.imageSmoothingQuality='high';o.drawImage(c,...box,0,0,w,h);return out;
}
function reflect(c,both=false){const o=canvas(c.width*2,c.height*(both?2:1)),g=o.getContext('2d');g.drawImage(c,0,0);g.save();g.translate(o.width,0);g.scale(-1,1);g.drawImage(c,0,0);g.restore();if(both){g.save();g.translate(0,o.height);g.scale(1,-1);g.drawImage(o,0,0,o.width,c.height,0,0,o.width,c.height);g.restore()}return o}
function drawnAssets(){
 for(const [n,w,h]of [['corner-large',150,150],['corner-small',68,68],['ribbon-left',28,104],['header-flourish',140,42],['help-end',100,42],['clock-wreath',198,198]])masks[n]=processed(n,w,h);
 const rc=canvas(28,104),rg=rc.getContext('2d');rg.translate(28,0);rg.scale(-1,1);rg.drawImage(masks['ribbon-left'],0,0);masks['ribbon-right']=rc;
 // Crop the flower from the generated small corner for tiny section medallions.
 masks['section-icon']=processed('corner-small',28,28,[.138,.142,.121,.103]);
 masks.lattice=reflect(processed('lattice',64,64,[.25,.25,.25,.25]),true);
 masks['diamond-row']=reflect(processed('diamond-row',18,20,[.425,.452,.075,.088]));
 for(const [n,c]of Object.entries(masks)){exportPNG('pieces/masks/'+n+'.png',c);qa.pieces.push({name:n,width:c.width,height:c.height,kind:'generated-mask'});if(['lattice','diamond-row'].includes(n))exportPNG('pieces/tiles/'+n+'.png',c)}
}
function tile(n,x,y,w,h,col,a){const im=masks[n];ctx.save();ctx.beginPath();ctx.rect(x,y,w,h);ctx.clip();let tw=im.width,th=im.height;if(n==='diamond-row'){tw=im.width*h/im.height;th=h}for(let yy=y;yy<y+h;yy+=th)for(let xx=x;xx<x+w;xx+=tw)ornament(n,xx,yy,tw,th,col,a);ctx.restore()}
function titleRibbon(x,y,w,h){
 tint(shapes['ribbon-body'],x,y,w,h,'#102B45');
 const old=ctx,c=canvas(w,h);ctx=c.getContext('2d');tile('lattice',0,0,w,h,'#3F6EC1',strength(.14));ctx.globalCompositeOperation='destination-in';ctx.drawImage(shapes['ribbon-body'],0,0,w,h);ctx=old;ctx.drawImage(c,x,y);
 ornament('ribbon-left',x+42,y+21,26,92,'#3F6EC1',strength(.4));ornament('ribbon-right',x+w-65,y+10,26,92,'#3F6EC1',strength(.4));
}
function helpRibbon(x,y,w,h){tint(shapes['help-ribbon-body'],x,y,w,h,P);const old=ctx,c=canvas(w,h);ctx=c.getContext('2d');ornament('help-end',9,19,100,37,'#A68D60',strength(.35));ctx.save();ctx.translate(w-9,19);ctx.scale(-1,1);ornament('help-end',0,0,100,37,'#A68D60',strength(.35));ctx.restore();tile('diamond-row',110,7,w-220,7,'#A68D60',strength(.25));tile('diamond-row',110,h-14,w-220,7,'#A68D60',strength(.25));ctx.globalCompositeOperation='destination-in';ctx.drawImage(shapes['help-ribbon-body'],0,0,w,h);ctx=old;ctx.drawImage(c,x,y)}
function reviewSheet(){
 const names=Object.keys(masks).filter(n=>!n.startsWith('quill')),c=canvas(1600,names.length*530+80);ctx=c.getContext('2d');rect(0,0,c.width,c.height,P);heading('Generated ornament masks · native 100% and 200%',28,36,30);screen='review';variant='A';
 for(const [i,n]of names.entries()){const y=80+i*530;heading(n,24,y+26,28);for(const [j,bg]of [P,'#102B45'].entries()){const x=24+j*790;rect(x,y+50,765,470,bg);const col=j?'#3F6EC1':'#A68D60',im=masks[n];tint(im,x+22,y+74,im.width,im.height,col);tint(im,x+260,y+74,im.width*2,im.height*2,col);text('100%',x+22,y+496,22,{color:j?'#F1E2BC':INK,bg});text('200%',x+260,y+496,22,{color:j?'#F1E2BC':INK,bg})}}
 exportPNG('review/ornaments-sheet.png',c);
 const rep=canvas(1000,540);ctx=rep.getContext('2d');rect(0,0,1000,540,P);tile('lattice',20,20,960,380,'#A68D60',1);tile('diamond-row',20,450,960,20,'#A68D60',1);exportPNG('review/tile-repeats.png',rep);
}



﻿// Original native Canvas UI pieces; no reference screenshot pixels are used.
const NAVY='#102B45', stains=[], icons={};let watermark,faceBacking,neutralClock,filledSelection;
const PAIRS=[{id:"A",heading:"Marcellus",body:"AlegreyaSans",weight:400,label:"Marcellus / Alegreya Sans · current"},{id:"B",heading:"Cinzel",body:"EBGaramond",weight:400,label:"Cinzel / EB Garamond"},{id:"C",heading:"CormorantGaramond",body:"AlegreyaSerif",weight:600,label:"Cormorant Garamond SemiBold / Alegreya"},{id:"D",heading:"Marcellus",body:"EBGaramond",weight:400,label:"Marcellus / EB Garamond"},{id:"E",heading:"IMFellEnglishSC",body:"CrimsonPro",weight:400,label:"IM Fell English SC / Crimson Pro"}];
let PAIR=PAIRS[0];
function rng(seed){return()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296}}
function asset(name,w,h,fn){const old=ctx,c=canvas(w,h);ctx=c.getContext('2d');fn(w,h);ctx=old;exportPNG(name,c);return c}
function circle(x,y,r,c){ctx.fillStyle=c;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill()}
function buildLayers(){
 for(let k=0;k<8;k++)stains.push(asset(`layers/stains/stain-${k+1}.png`,512,512,()=>{
  const r=rng(4900+k*721);for(let j=0;j<68;j++){const x=100+r()*300,y=100+r()*300,rad=22+r()*92;const g=ctx.createRadialGradient(x,y,0,x,y,rad);g.addColorStop(0,'rgba(89,57,24,.19)');g.addColorStop(.48,'rgba(104,71,36,.08)');g.addColorStop(1,'rgba(104,71,36,0)');ctx.fillStyle=g;ctx.beginPath();ctx.ellipse(x,y,rad,rad*(.55+r()*.5),r()*6.28,0,6.28);ctx.fill()}
 }));
 watermark=asset('layers/watermark.png',512,512,()=>{
  const im=I.ownerWatermark, z=Math.min(480/im.width,480/im.height);ctx.drawImage(im,(512-im.width*z)/2,(512-im.height*z)/2,im.width*z,im.height*z);
  ctx.globalCompositeOperation='source-in';rect(0,0,512,512,INK);ctx.globalCompositeOperation='source-over';
 });
 neutralClock=asset('pieces/tier-1/clock-medallion-wreath.png',I['v1-clock-medallion-wreath'].width,I['v1-clock-medallion-wreath'].height,()=>{
  ctx.drawImage(I['v1-clock-medallion-wreath'],0,0);const d=ctx.getImageData(0,0,ctx.canvas.width,ctx.canvas.height);for(let i=0;i<d.data.length;i+=4){const lum=(d.data[i]+d.data[i+1]+d.data[i+2])/3;const v=Math.round(91+lum/255*19);d.data[i]=v;d.data[i+1]=v;d.data[i+2]=v-2;}ctx.putImageData(d,0,0);
 });
 filledSelection=asset('pieces/tier-2/selected-row-glow.png',852,137,()=>{
  // Entire row is filled. The luminous edge is secondary, with no outline ring.
  const g=ctx.createLinearGradient(0,0,852,0);g.addColorStop(0,'#9BCBF2CC');g.addColorStop(.08,'#C7E7FFEA');g.addColorStop(.5,'#DCEBEEF5');g.addColorStop(.92,'#C7E7FFEA');g.addColorStop(1,'#9BCBF2CC');ctx.fillStyle=g;ctx.fillRect(0,0,852,137);
  const e=ctx.createLinearGradient(0,0,0,137);e.addColorStop(0,'#A0D5FF99');e.addColorStop(.14,'#CBEAFF00');e.addColorStop(.86,'#CBEAFF00');e.addColorStop(1,'#A0D5FF99');ctx.fillStyle=e;ctx.fillRect(0,0,852,137);
  ctx.globalCompositeOperation='destination-in';const f=ctx.createLinearGradient(0,0,0,137);f.addColorStop(0,'#FFFFFF40');f.addColorStop(.14,'#FFFFFFF5');f.addColorStop(.3,'#FFFFFFFF');f.addColorStop(.7,'#FFFFFFFF');f.addColorStop(.86,'#FFFFFFF5');f.addColorStop(1,'#FFFFFF40');ctx.fillStyle=f;ctx.fillRect(0,0,852,137);ctx.globalCompositeOperation='source-over';
 });
 faceBacking=asset('pieces/tier-2/face-backing.png',160,154,()=>{const g=ctx.createRadialGradient(76,61,18,76,73,89);g.addColorStop(0,'#102B45EA');g.addColorStop(.48,'#102B45BB');g.addColorStop(1,'#102B4500');ctx.fillStyle=g;ctx.fillRect(0,0,160,154)});
 for(const n of ['title-ribbon'])asset('pieces/tier-1/'+n+'.png',I['v1-'+n].width,I['v1-'+n].height,()=>ctx.drawImage(I['v1-'+n],0,0));
 for(const n of ['quill'])asset('pieces/tier-2/'+n+'.png',I['v1-'+n].width,I['v1-'+n].height,()=>ctx.drawImage(I['v1-'+n],0,0));
}
function iconDraw(n){
 // Small engraved seal: clipped corners, inset rule and tailored internal cuts.
 path([[5,0],[27,0],[32,5],[32,27],[27,32],[5,32],[0,27],[0,5]],NAVY,1,true,true);
 path([[5,2],[27,2],[30,5],[30,27],[27,30],[5,30],[2,27],[2,5]],'#657785',.7,true);
 ctx.strokeStyle=P;ctx.fillStyle=P;ctx.lineWidth=2.2;ctx.lineCap='round';ctx.lineJoin='round';
 const poly=p=>path(p,P,2,true,true);
 if(n==='coin'){circle(16,16,10,GOLD);ctx.strokeStyle=NAVY;ctx.lineWidth=1.8;ctx.beginPath();ctx.arc(16,16,7,0,6.28);ctx.stroke();line(16,11,16,21,NAVY,2);line(13,13,19,13,NAVY,1);line(13,19,19,19,NAVY,1);for(let a=0;a<8;a++){const z=a*Math.PI/4;circle(16+9*Math.cos(z),16+9*Math.sin(z),.5,NAVY)}}
 if(n==='reputation'){poly([[16,5],[20,12],[27,13],[22,19],[23,27],[16,23],[9,27],[10,19],[5,13],[12,12]]);path([[16,8],[16,18],[23,14]],'#B49A68',1);path([[16,18],[21,24]],NAVY,1)}
 if(n==='morale'){circle(16,16,10,P);circle(12,13,1.5,NAVY);circle(20,13,1.5,NAVY);ctx.strokeStyle=NAVY;ctx.beginPath();ctx.arc(16,16,5,.15,Math.PI-.15);ctx.stroke();path([[8,11],[10,8],[13,7]],'#B49A68',1)}
 if(n==='rank'){poly([[7,5],[25,5],[25,20],[16,28],[7,20]]);path([[9,7],[23,7],[23,19],[16,25],[9,19]],'#B49A68',.8,true);rect(12,10,3,11,NAVY);rect(15,10,6,2.5,NAVY);rect(15,14.5,5,2.5,NAVY)}
 if(n==='time'){ctx.beginPath();ctx.arc(16,16,10,0,6.28);ctx.stroke();line(16,9,16,16,P,2.5);line(16,16,21,19,P,2.5);for(let i=0;i<4;i++){const a=i*Math.PI/2;line(16+8*Math.cos(a),16+8*Math.sin(a),16+10*Math.cos(a),16+10*Math.sin(a),P,1)}}
 if(n==='info'){circle(16,8,1.8,P);rect(14.5,13,3,12,P)}
 if(n==='success'){path([[7,17],[13,23],[25,9]],P,3.5)}
 if(n==='warning'){poly([[16,4],[29,27],[3,27]]);rect(14.5,12,3,7,NAVY);circle(16,23,1.6,NAVY)}
 if(n==='critical'){poly([[10,3],[22,3],[29,10],[29,22],[22,29],[10,29],[3,22],[3,10]]);line(11,11,21,21,NAVY,3);line(21,11,11,21,NAVY,3)}
 if(n==='rare'){poly([[16,3],[28,13],[16,29],[4,13]]);path([[7,13],[25,13],[16,26],[12,13],[16,6],[20,13]],NAVY,1.6)}
 if(n==='scroll'){poly([[9,5],[25,5],[25,24],[21,28],[7,28],[7,10]]);ctx.strokeStyle=P;ctx.strokeRect(4,5,7,6);line(13,12,21,12,NAVY,2);line(13,17,21,17,NAVY,2);line(11,23,20,23,NAVY,2)}
 if(n==='pin'){poly([[12,4],[24,8],[21,12],[22,19],[17,20],[10,28],[11,18],[6,16],[12,11]])}
 if(n==='hp'){ctx.beginPath();ctx.moveTo(16,27);ctx.bezierCurveTo(-5,13,7,0,16,10);ctx.bezierCurveTo(25,0,37,13,16,27);ctx.fill()}
 if(n==='stamina'){poly([[18,3],[7,18],[14,18],[12,29],[26,12],[18,12]])}
}
function makeIcons(){for(const n of ['coin','reputation','morale','rank','time','info','success','warning','critical','rare','scroll','pin','hp','stamina']){
 icons[n]=asset('icons/'+n+'.png',32,32,()=>iconDraw(n));asset('icons/'+n+'-24.png',24,24,()=>{ctx.scale(.75,.75);iconDraw(n)});
 }for(const scale of [1,2])asset('icons-sheet'+(scale===2?'@2x':'')+'.png',896*scale,170*scale,()=>{ctx.scale(scale,scale);rect(0,0,896,170,P);Object.keys(icons).forEach((n,i)=>{const x=14+i*63;ctx.drawImage(icons[n],x,22);ctx.drawImage(I['unused']||icons[n],x,75,24,24);ctx.font='13px AlegreyaSans';ctx.fillStyle=INK;ctx.fillText(n,x,131)})});
}
function icon(n,x,y,size=32){ctx.drawImage(icons[n],x,y,size,size);(qa.icons??=[]).push({screen,name:n,size,x,y})}
function layerStains(x,y,w,h,seed){const r=rng(seed);ctx.save();ctx.beginPath();ctx.rect(x,y,w,h);ctx.clip();ctx.globalCompositeOperation='multiply';for(let i=0;i<4;i++){const pick=Math.floor(r()*8),a=.12+r()*.12,angle=r()*6.28,xx=x+r()*w,yy=y+r()*h;ctx.save();ctx.globalAlpha=a;ctx.translate(xx,yy);ctx.rotate(angle);ctx.drawImage(stains[pick],-w*.45,-h*.4,w*.9,h*.8);ctx.restore();(qa.layers??=[]).push({screen,seed,pick,alpha:a,angle,blend:'multiply'})}ctx.restore()}
function layerWatermark(x,y,w,h){ctx.save();ctx.globalAlpha=.05;const z=Math.min(w,h)*.74;ctx.drawImage(watermark,x+(w-z)/2,y+(h-z)/2,z,z);ctx.restore()}
function frame(x,y,w,h){ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=1;ctx.strokeRect(x+.5,y+.5,w-1,h-1);for(let i=1;i<15;i++){ctx.globalAlpha=.045*(1-i/15);ctx.strokeStyle='#70481D';ctx.lineWidth=2;ctx.strokeRect(x+i,y+i,w-i*2,h-i*2)}ctx.restore();for(const [xx,yy,sx,sy]of [[x+6,y+6,1,1],[x+w-6,y+6,-1,1],[x+6,y+h-6,1,-1],[x+w-6,y+h-6,-1,-1]]){ctx.save();ctx.translate(xx,yy);ctx.scale(sx,sy);ctx.beginPath();ctx.rect(0,0,17,120);ctx.rect(0,0,120,17);ctx.clip();ornament('corner-large',0,0,120,120,'#937642',.32);ctx.restore()}}
function card(x,y,w,h){rect(x,y,w,h,P);layerStains(x,y,w,h,x===35?871:1409);layerWatermark(x,y,w,h);frame(x,y,w,h)}
function plate(x,y,w,h){ctx.save();ctx.fillStyle=P;ctx.beginPath();ctx.moveTo(x+9,y);ctx.lineTo(x+w,y);ctx.lineTo(x+w,y+h-9);ctx.lineTo(x+w-9,y+h);ctx.lineTo(x,y+h);ctx.lineTo(x,y+9);ctx.closePath();ctx.fill();ctx.strokeStyle='#8D784F';ctx.lineWidth=1;ctx.stroke();ctx.restore();(qa.plain??=[]).push({screen,x,y,w,h,tier:3})}
function piece(n,x,y,w,h){if(n==='clock-medallion-wreath'){ctx.drawImage(neutralClock,x,y,w,h);return}if(n==='selected-row-glow'){ctx.drawImage(filledSelection,x,y,w,h);return}if(['title-ribbon','quill'].includes(n)){ctx.drawImage(I['v1-'+n],x,y,w,h);return}
 if(n==='minimap-ring'){ctx.strokeStyle=NAVY;ctx.lineWidth=3;ctx.beginPath();ctx.arc(x+w/2,y+h/2,w*.465,0,6.28);ctx.stroke();return}
 if(n==='button-hint-tab'){tint(shapes[n],x,y,w,h,P);path([[x+18,y],[x+w*.29,y],[x+w*.23,y+h],[x,y+h]],NAVY,1,true,true);path([[x+18,y+.7],[x+w-.7,y+.7],[x+w-15,y+h-.7],[x+.7,y+h-.7]],'#796849',1.4,true);return}
 if(n==='help-ribbon'){tint(shapes['help-ribbon-body'],x,y,w,h,P);diamond(x+50,y+h/2,9,NAVY);diamond(x+w-50,y+h/2,9,NAVY);return}}
function header(s,x,y,w){rect(x,y,w,68,NAVY);circle(x+40,y+34,23,P);ctx.drawImage(icons[s==='Adventurers'?'reputation':'scroll'],x+24,y+18,32,32);tile('lattice',x+73,y,w-73,68,P,.145);tile('diamond-row',x,y+70,w,10,'#8E7440',.75);heading(s,x+85,y+37,30,{color:P,bg:NAVY})}
function band(x,y,w){const g=ctx.createLinearGradient(x,0,x+w,0);g.addColorStop(0,'#40566A');g.addColorStop(.37,'#40566A');g.addColorStop(1,'#40566A00');ctx.fillStyle=g;ctx.fillRect(x,y,w,40);ctx.save();ctx.beginPath();ctx.rect(x,y,w,40);ctx.clip();for(let i=0;i<w;i+=22){ctx.globalAlpha=.12*(1-i/w);line(x+i,y,x+i+40,y+40,P);line(x+i,y+40,x+i+40,y,P)}ctx.restore()}
function section(label,x,y){band(x-8,y-20,720);heading(label,x+13,y,29,{color:P,bg:'#40566A'})}
function bar(x,y,w,h,f,col){rect(x,y,w,h,NAVY);ctx.strokeStyle='#8E7440';ctx.lineWidth=1;ctx.strokeRect(x+.5,y+.5,w-1,h-1);rect(x+3,y+3,(w-6)*f,h-6,col)}
function stamina(x,y,count){for(let i=0;i<4;i++){bar(x+i*30,y,25,15,1,i<count?NAVY:'#D2B77D');if(i<count){ctx.save();ctx.beginPath();ctx.rect(x+i*30+3,y+3,19,9);ctx.clip();ctx.globalAlpha=.55;ctx.drawImage(I['v1-title-ribbon'],140,76,110,32,x+i*30+3,y+3,19,9);ctx.restore()}}}
function tabShape(x,y,active){ctx.save();if(active){ctx.shadowColor='#62B8F5';ctx.shadowBlur=20}path([[x,y-(active?47:35)],[x+(active?86:77),y],[x,y+(active?47:35)],[x-(active?86:77),y]],NAVY,1,true,true);ctx.restore();if(active){ctx.strokeStyle=GOLD;ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x,y-47);ctx.lineTo(x+86,y);ctx.lineTo(x,y+47);ctx.lineTo(x-86,y);ctx.closePath();ctx.stroke()}}
function tabs(){rect(610,157,688,30,NAVY);text('Q',626,172,24,{color:P,bg:NAVY});text('E',1277,172,24,{color:P,bg:NAVY});['All','Hunters','Scouts'].forEach((s,i)=>{const x=729+i*206;tabShape(x,172,i===0);heading(s,x,172,28,{align:'center',color:P,bg:NAVY})})}
function world(){screen='world-hud';const c=canvas(W,H);ctx=c.getContext('2d');worldBackground();
 piece('clock-medallion-wreath',28,22,198,198);circle(126,119,61,P);ctx.strokeStyle=GOLD;ctx.lineWidth=4;ctx.beginPath();ctx.arc(126,119,68,-Math.PI/2,1.97);ctx.stroke();text('DAY',126,80,22,{align:'center'});text('3',126,113,44,{align:'center',role:'number'});text('14:20',126,152,27,{align:'center',role:'number'});
 statPlate(225,34,707,99);for(const [i,[label,value,n]]of [['Purse','2,500 G','coin'],['Rep','0','reputation'],['Morale','60','morale'],['Rank','','rank']].entries()){const x=256+i*165; text(label,x,59,22,{color:P,bg:NAVY});icon(n,x,81,32);if(value)text(value,x+42,98,31,{role:'number',color:P,bg:NAVY});if(i<3)line(x+149,52,x+149,115,'#657785')}
 controlBorder(238,140,337,61);icon('time',252,157,28);controlText('Pause',288,172,24);for(const [i,s]of ['1x','2x','4x'].entries()){if(i===0)rect(358,141,55,59,NAVY);controlText(s,385+i*62,172,26,{align:'center',role:'number',selected:i===0})}
 controlBorder(583,140,347,61);controlText('Battle pace',612,172,24);rect(851,141,63,59,NAVY);controlText('1x',883,172,26,{align:'center',role:'number',selected:true});
 for(const [j,label]of ['Meet Mae at the tavern','Boarhide Vest for Anselm'].entries()){const y=239+j*68;plate(36,y,610,62);icon(j?'pin':'scroll',54,y+15,32);text(j?'Pinned':'Objective',101,y+32,22);line(194,y+16,194,y+46,'#B49A68');text(label,210,y+32,27)}
 notification(36,388,536,69);icon('success',54,407,32);captureToastBackground(101,424,'Operation returned',27);text('Operation returned',101,424,27,{color:'#F7F3E8',bg:'#252525'});
 minimap();plate(1643,259,265,61);text('N  ·  Eurydica',1775,291,25,{align:'center'});hint('E','Talk',879,421,154);hint('Tab','Ongoing',1442,984,222);hint('Esc','Ledger',1675,984,207);exportPNG('world-hud.png',c);return c;
}
function exportPieces(){
 asset('pieces/tier-2/paper.png',903,720,()=>rect(0,0,903,720,P));asset('pieces/tier-2/frame.png',903,720,()=>frame(0,0,903,720));asset('pieces/tier-2/header-band.png',875,80,()=>header('Adventurers',0,0,875));asset('pieces/tier-2/heading-band.png',720,40,()=>band(0,0,720));asset('pieces/tier-2/bar-track.png',323,16,()=>bar(0,0,323,16,0,P));asset('pieces/tier-2/stamina-segments.png',120,15,()=>stamina(0,0,3));
 asset('pieces/tier-2/tab-active.png',188,110,()=>tabShape(94,55,true));asset('pieces/tier-2/tab-inactive.png',160,76,()=>tabShape(80,38,false));
 asset('pieces/tier-3/stat-plate.png',707,99,()=>statPlate(0,0,707,99));asset('pieces/tier-3/objective.png',610,62,()=>plate(0,0,610,62));asset('pieces/tier-3/notification.png',536,69,()=>notification(0,0,536,69));asset('pieces/tier-3/time-controls.png',337,61,()=>{controlBorder(0,0,337,61);rect(120,1,55,59,NAVY)});asset('pieces/tier-3/battle-pace.png',347,61,()=>{controlBorder(0,0,347,61);rect(268,1,63,59,NAVY)});
 asset('pieces/tier-3/help-ribbon.png',1117,73,()=>piece('help-ribbon',0,0,1117,73));asset('pieces/tier-3/button-hint.png',208,61,()=>piece('button-hint-tab',0,0,208,61));
}
function layerDemo(){asset('review/layers-demo.png',1920,650,()=>{rect(0,0,1920,650,'#0B1D2D');heading('Content card · five independent layers',38,44,32,{color:P,bg:NAVY});['Paper','+ Stains','+ Watermark','+ Frame','+ Content'].forEach((s,i)=>{const x=27+i*379,y=114,w=354,h=460;rect(x,y,w,h,P);if(i>=1)layerStains(x,y,w,h,871);if(i>=2)layerWatermark(x,y,w,h);if(i>=3)frame(x,y,w,h);if(i>=4){rect(x+10,y+12,w-20,55,NAVY);icon('scroll',x+23,y+24,30);heading('Tracker',x+67,y+42,29,{color:P,bg:NAVY});text('Hunt target',x+24,y+132,26);text('+10%',x+w-24,y+176,34,{align:'right',role:'number'});line(x+24,y+212,x+w-24,y+212,'#B49A68');text('Scouting find chance',x+24,y+255,26);text('+10%',x+w-24,y+300,34,{align:'right',role:'number'})}heading(s,x+10,610,28,{color:P,bg:NAVY})})})}
function statPlate(x,y,w,h){
 rect(x,y,w,h,NAVY);ctx.strokeStyle='#9D947F';ctx.lineWidth=1.4;ctx.strokeRect(x+.7,y+.7,w-1.4,h-1.4);
 for(const side of [0,1]){ctx.save();ctx.translate(side?x+w-6:x+6,y+9);if(side)ctx.scale(-1,1);ornament('corner-small',0,0,22,36,'#ACA38D',.65);ctx.translate(0,h-18);ctx.scale(1,-1);ornament('corner-small',0,0,22,36,'#ACA38D',.65);ctx.restore()}
}
function controlBorder(x,y,w,h){ctx.save();ctx.strokeStyle=P;ctx.lineWidth=1.2;ctx.shadowColor='#000000';ctx.shadowBlur=2;ctx.strokeRect(x+.6,y+.6,w-1.2,h-1.2);ctx.restore()}
function controlText(s,x,y,size,opt={}){
 // A narrow dark glyph keyline maintains legibility over the transparent world.
 if(!opt.selected){ctx.save();ctx.font=`400 ${size}px ${PAIR.body}`;ctx.textAlign=opt.align||'left';ctx.textBaseline='middle';ctx.lineJoin='round';ctx.lineWidth=3;ctx.strokeStyle='#161B20';ctx.strokeText(s,x,y);ctx.restore()}
 text(s,x,y,size,{...opt,color:P,bg:opt.selected?NAVY:'#161B20'});
}
function notification(x,y,w,h){const g=ctx.createLinearGradient(x,0,x+w,0);g.addColorStop(0,'#000000C7');g.addColorStop(.72,'#000000C7');g.addColorStop(1,'#00000000');ctx.fillStyle=g;ctx.fillRect(x,y,w,h)}
function captureToastBackground(x,y,s,size){
 ctx.save();ctx.font=`400 ${size}px ${PAIR.body}`;ctx.textBaseline='middle';const m=ctx.measureText(s),xx=Math.floor(x-m.actualBoundingBoxLeft),yy=Math.floor(y-m.actualBoundingBoxAscent),w=Math.ceil(m.actualBoundingBoxLeft+m.actualBoundingBoxRight)+1,h=Math.ceil(m.actualBoundingBoxAscent+m.actualBoundingBoxDescent)+1;
 const d=ctx.getImageData(xx,yy,w,h).data;let min=Infinity,maxL=0;for(let i=0;i<d.length;i+=4){const l=lum([d[i],d[i+1],d[i+2]]);maxL=Math.max(maxL,l);min=Math.min(min,(lum(rgb('#F7F3E8'))+.05)/(l+.05))}
 (qa.notificationContrast??=[]).push({pairing:PAIR.id,box:[xx,yy,w,h],minContrast:min,maxBackgroundLuminance:maxL,method:'every composited background pixel in glyph bounding rectangle before text'});ctx.restore();
}
function specimen(){screen='specimen';asset('fonts/specimen.png',1920,1760,()=>{
 rect(0,0,1920,1760,'#0B1D2D');PAIR=PAIRS[0];heading('FGC · Typography at play size',40,47,38,{color:P,bg:NAVY});text('Five pairings on v5 parchment · 100% native size · lining figures enabled',40,93,26,{color:P,bg:NAVY});
 for(let i=0;i<5;i++){
  const x=40+(i%2)*940,y=174+Math.floor(i/2)*520,w=900,h=442;
  PAIR=PAIRS[0];text(PAIRS[i].id+'  '+PAIRS[i].label,x,y-26,24,{color:P,bg:NAVY});
  PAIR=PAIRS[i];card(x,y,w,h);header('Adventurer dossier',x+14,y+12,w-28);section('Condition',x+38,y+121);
  heading('Nell Larkin',x+30,y+180,37);text('Ranger · Ranged · Available',x+30,y+228,27);
  text('Rest restores all four stamina bars at day’s end.',x+30,y+272,25);
  text('0123456789 2,500 G 120/150 08:00 1.0',x+30,y+327,28,{role:'number'});
  text('0 o O   ·   8 S   ·   08:00  120/150',x+30,y+384,24,{role:'number'});
  const metrics={pairing:PAIR.id,font:PAIR.body,at24:{}};ctx.font=`400 24px ${PAIR.body}`;ctx.textBaseline='alphabetic';for(const ch of ['0','o','O','8','S']){const m=ctx.measureText(ch);metrics.at24[ch]={width:m.width,ascent:m.actualBoundingBoxAscent,descent:m.actualBoundingBoxDescent}}(qa.figureMetrics??=[]).push(metrics);
 }
 PAIR=PAIRS[0];const x=980,y=1214;card(x,y,900,442);header('Reading the specimen',x+14,y+12,872);
 const notes=['Header 30 px · section 29 px · name 37 px','Body 25–27 px · numbers 28 px · probe 24 px','Compare zero with lowercase o; eight with capital S.','C adds a calligraphic heading with a firmer serif body.','Both alternate screens use C at the same UI sizes.','Candidate only · no font choice is approved.'];
 notes.forEach((t,i)=>text(t,x+30,y+116+i*50,25));
 PAIR=PAIRS[0];text('A: current baseline   /   B–E: owner-requested alternatives   /   zoom to 100% for comparison',40,1718,25,{color:P,bg:NAVY});
 });PAIR=PAIRS[0];
}
(async()=>{try{
 for(const p of PAIRS){await document.fonts.load(`${p.weight} 28px ${p.heading}`);await document.fonts.load(`400 28px ${p.body}`)}
 qa.fontsLoaded=PAIRS.every(p=>document.fonts.check(`${p.weight} 28px ${p.heading}`)&&document.fonts.check(`400 28px ${p.body}`));
 qa.fontPairings=PAIRS;qa.liningFeatures='"lnum" 1, "onum" 0';
 for(const [k,src]of Object.entries(SOURCES)){const im=new Image();im.src=src;await im.decode();I[k]=im}
 variant='v5';screen='pieces';makeAssets();buildLayers();makeIcons();exportPieces();
 for(const k of Object.keys(output))if(k.includes('face-frame'))delete output[k];
 const a=world(),b=roster();screen='review';layerDemo();
 asset('compare.png',1920,1152,()=>{rect(0,0,1920,1152,NAVY);heading('v4 · Starting candidate',28,34,29,{color:P,bg:NAVY});heading('v5 · Fine-fit candidate',988,34,29,{color:P,bg:NAVY});ctx.drawImage(I.oldWorld,0,72,960,540);ctx.drawImage(a,960,72,960,540);ctx.drawImage(I.oldRoster,0,612,960,540);ctx.drawImage(b,960,612,960,540)});
 // Alternate is a font substitution only, preserving all positions and sizes.
 PAIR=PAIRS[2];variant='v5-alt-C';const altWorld=world(),altRoster=roster();exportPNG('world-hud-alt-font.png',altWorld);exportPNG('roster-alt-font.png',altRoster);exportPNG('world-hud.png',a);exportPNG('roster.png',b);
 specimen();
 window.RENDERED={outputs:output,qa};document.getElementById('result').textContent='READY';
 }catch(e){document.getElementById('result').textContent=JSON.stringify({error:e.stack})}})();
