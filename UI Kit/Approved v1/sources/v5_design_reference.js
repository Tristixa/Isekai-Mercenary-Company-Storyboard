// Original native Canvas UI pieces; no reference screenshot pixels are used.
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
