"""Deterministic, unpainted review geometry drawn from the candidate JSON."""
import json,math,hashlib,colorsys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import inherited_checks as g
R=Path(__file__).resolve().parent
P=json.loads((R/'eurydica-plan-v7b.json').read_bytes())
OLD=json.loads(Path('D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/Archive/Build Plan v5/eurydica-plan.json').read_bytes())
INK='#263b3e';PAPER='#f6f3eb';ROAD='#dfd6bf';GRASS='#a4bb88'
ROOFS={'green':'#507861','warm_red':'#bb705b','plum':'#886c88','brown':'#82694f'}
def font(n,bold=False):return ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),n)
def tint(i):return tuple(int(v*255) for v in colorsys.hsv_to_rgb((i*.61803398875)%1,.34,.82))
def badge(d,pt,n,color,rad=16):
 x,y=pt;d.ellipse((x-rad,y-rad,x+rad,y+rad),fill=color,outline=INK,width=2)
 d.text((x,y),str(n),font=font(17,True),anchor='mm',fill=INK)
def canvas(w,h,title,subtitle):
 im=Image.new('RGB',(w,h),PAPER);d=ImageDraw.Draw(im)
 d.text((55,35),title,font=font(38,True),fill=INK)
 d.text((57,88),subtitle,font=font(21),fill=INK)
 return im,d

def meadow(im,p,project):
 """Render the JSON's boolean meadow layer, including holes for all used ground."""
 cover=p['green'].get('continuous_cover')
 if not cover:return
 for domain in cover['domains']:
  mask=Image.new('L',im.size);draw=ImageDraw.Draw(mask);h=domain['height_m']
  draw.polygon([project(v,h) for v in domain['polygon']],fill=255)
  for poly in cover['exclusions']:draw.polygon([project(v,h) for v in poly],fill=0)
  im.paste('#c1cda6',(0,0,im.width,im.height),mask)

def screen(d,p,project):
 spec=p.get('hq_screen')
 if not spec:return
 for line in spec['polylines']:
  pts=[project(v,.6) for v in line]
  d.line(pts,fill='#647551',width=6,joint='curve')
  for a,b in zip(line,line[1:]):
   n=max(1,math.ceil(math.dist(a,b)/2))
   for i in range(n+1):
    v=[a[k]+(b[k]-a[k])*i/n for k in (0,1)];x,y=project(v,.6)
    d.ellipse((x-2,y-2,x+2,y+2),fill='#76664d')

def propdraw(d,a,project):
 f=a['footprint'];h=.7;pts=[project(v,h) for v in g.boxpoly(f)];typ=a['type']
 timber=any(s in typ for s in ('timber','lumber','sawhorse','bench'))
 stone=any(s in typ for s in ('stone','material','scrap'))
 col='#a08a65' if timber else '#9b9a8c' if stone else '#a18b68'
 if a['id'].startswith('allotment_'):col='#928973'
 if stone:
  # Stacked stone/material mounds, not anonymous grey collision boxes.
  for dx,dz,rad in ((.32,.5,.32),(.64,.53,.29),(.5,.37,.27)):
   cx=f[0]+(f[2]-f[0])*dx;cz=f[1]+(f[3]-f[1])*dz
   mound=[[cx+math.cos(i*math.pi/4)*(f[2]-f[0])*rad,cz+math.sin(i*math.pi/4)*(f[3]-f[1])*rad] for i in range(8)]
   d.polygon([project(v,h) for v in mound],fill=col,outline='#77786a')
  return
 d.polygon(pts,fill=col,outline='#796f5e')
 if timber:
  for t in (.25,.5,.75):
   d.line([project([f[0],f[1]+(f[3]-f[1])*t],h),project([f[2],f[1]+(f[3]-f[1])*t],h)],fill='#786343',width=2)
 elif 'crate' in typ:
  d.line([pts[0],pts[2]],fill='#756143',width=2);d.line([pts[1],pts[3]],fill='#756143',width=2)
 elif 'cart' in typ:
  for v in pts:
   x,y=v;d.ellipse((x-3,y-3,x+3,y+3),fill='#665e51')
def topdraw(im,p,origin,scale,ext,labels=False,clustered=True):
 d=ImageDraw.Draw(im);ox,oy=origin;x0,z0,x1,z1=ext
 def xy(v):return (ox+(v[0]-x0)*scale,oy+(v[1]-z0)*scale)
 def poly(v,fill,outline=None):d.polygon([xy(a) for a in v],fill=fill,outline=outline)
 poly(p['extent'],'#e9e3d5')
 for t in p['terrain']['terraces']:
  if t['id'] not in ('south','company_platform'):poly(t['polygon'],'#dedccd','#bcc1b1')
 for t in p['terrain']['cliffs']:poly(t['polygon'],'#969c94','#717c74')
 meadow(im,p,lambda v,h:xy(v))
 if p.get('plan_revision')in ('v7','v7b'):
  for s in p['green']['spaces']:
   for v in s['polygons']:poly(v,GRASS if s['kind']!='allotment' else '#c1b98d')
 else:
  for a in p['green'].get('lawns',[]):poly(a['polygon'],'#c1cfae')
  for a in p.get('small_plots',[]):poly(a['polygon'],GRASS)
 poly(p['river']['polygon'],'#82aebb');poly(p['waterworks']['feeder_polygon'],'#82aebb')
 for c in p.get('clusters',[]) if clustered else []:
  if 'court_polygon' in c:poly(c['court_polygon'],'#d5c8ae')
 for s in p.get('squares',[]):poly(s['polygon'],'#d6cbb7')
 if p.get('plan_revision')in ('v7','v7b'):poly(next(z['polygon'] for z in p['ground_zones'] if z['id']=='red_tree_bed'),'#a8b581')
 for r in p['routes']:
  pts=[xy(a) for a in r['centreline']];w=max(1,round(r['width_m']*scale))
  d.line(pts,fill='#a49a89',width=w+2)
  d.line(pts,fill='#eddfbb' if r['id']=='main_road' else ROAD,width=w)
  for a in pts[1:-1]:d.ellipse([a[0]-w/2,a[1]-w/2,a[0]+w/2,a[1]+w/2],fill=ROAD)
 poly(p['hq_reservation']['polygon'],'#e4cf9a',INK)
 screen(d,p,lambda v,h:xy(v))
 for a in p['props']:
  if 'footprint' in a:
   if p.get('plan_revision')=='v7b':propdraw(d,a,lambda v,h:xy(v))
   else:poly(g.boxpoly(a['footprint']),'#918775')
  elif 'position' in a:
   x,y=xy(a['position']);rr=max(1,a.get('collision_radius_m',.2)*scale);d.ellipse((x-rr,y-rr,x+rr,y+rr),fill='#776c58')
 colors={c['id']:tint(i) for i,c in enumerate(p.get('clusters',[]))}
 for b in p['buildings']:
  for f in b.get('collision_rectangles',[b['footprint']]):
   v=[g.rotate(a,b) for a in g.boxpoly(f)]
   poly(v,colors.get(b.get('cluster_id'),ROOFS.get(b['roof_palette'],'#806f65')) if clustered else ROOFS.get(b['roof_palette'],'#806f65'),INK)
  if labels:
   a=xy(b['door_position']);d.ellipse((a[0]-2,a[1]-2,a[0]+2,a[1]+2),fill='#fffdf7')
 for t in p['green']['trees']:
  a=xy(t['position']);rr=t.get('canopy_radius_m',2)*scale
  d.ellipse((a[0]-rr,a[1]-rr,a[0]+rr,a[1]+rr),fill='#a65042' if t['id']=='tree_08' else '#66805c',outline='#516b4d')
 for wall in p['city_wall']['segments']:d.line([xy(a) for a in wall],fill='#756b60',width=max(2,round(1.2*scale)))
 if labels:
  for i,c in enumerate(p['clusters']):
   bb=[b for b in p['buildings'] if b['id'] in c['building_ids']]
   cx=sum((b['footprint'][0]+b['footprint'][2])/2 for b in bb)/len(bb)
   zz=min(b['footprint'][1] for b in bb)-3
   badge(d,xy([cx,zz]),i+1,tint(i))
  rr=p['hq_reservation']['polygon'];xx,yy=xy([(rr[0][0]+rr[2][0])/2,(rr[0][1]+rr[2][1])/2]);d.text((xx,yy),'HQ\nreserve',font=font(16,True),anchor='mm',fill=INK,align='center')
 return xy
def legend(d,x,y,clusters=True):
 d.text((x,y),'DISTRICT  /  CLUSTER',font=font(22,True),fill=INK);y+=46
 names={a['id']:a['name'] for a in P['districts']}
 for i,c in enumerate(P['clusters']):
  badge(d,(x+17,y+15),i+1,tint(i));d.text((x+45,y),c['name'],font=font(21,True),fill=INK)
  d.text((x+45,y+27),names[c['district']]+'  |  '+str(len(c['building_ids']))+' buildings',font=font(16),fill='#5c6965');y+=67
 d.text((x,y+10),'Green: meadow / organic groves\nOchre: main road / screened HQ\nWhite dots: doors | Stock: four piles',font=font(18),fill=INK,spacing=7)
def mainmap():
 im,d=canvas(2460,2110,'EURYDICA / CLUSTER PLAN v7b','Candidate for owner review  |  metres  |  north up  |  86 buildings / 21 groups')
 xy=topdraw(im,P,(65,155),6.6,(-118,-140,151,137),True)
 legend(d,1900,163)
 d.text((65,2040),'N    0',font=font(20,True),fill=INK)
 d.line((145,2050,277,2050),fill=INK,width=4);d.text((290,2040),'20 m',font=font(20),fill=INK)
 d.text((700,2040),'Phase 1: south-bank homes / market / Guild     Phase 2: work yards and north bank',font=font(19),fill=INK)
 im.save(R/'cluster-map-v7b.png')
def comparison():
 v=json.loads((R/'eurydica-plan.json').read_bytes());m=json.loads((R/'check-result-v7b.json').read_bytes())
 im,d=canvas(3200,1920,'EURYDICA / v7 TO v7b','Same scale, same 86 buildings and 21 groups | five branch families | candidate for owner review')
 ext=(-118,-140,151,137)
 for x,p,title,key in [(55,v,'v7 / original candidate','roads_before'),(1650,P,'v7b / refined candidate','roads_after')]:
  d.text((x,143),title,font=font(31,True),fill=INK)
  met=m[key];d.text((x,187),f"Roads {met['length_m']:,.0f} m | union area {met['union_area_m2']:,.0f} sq m",font=font(23),fill=INK)
  topdraw(im,p,(x,245),5.5,ext,False,True)
  d.line((x+30,1815,x+140,1815),fill=INK,width=4);d.text((x+155,1801),'20 m',font=font(20),fill=INK)
 d.text((55,1870),'Both views: north up; 5.5 pixels per metre. Gate-to-river distance stays 130.8 m. No Godot integration.',font=font(25),fill=INK)
 im.save(R/'v7-vs-v7b.png')
def bird():
 im,d=canvas(2580,1740,'EURYDICA / NORTH-FACING MASSING v7b','Simple geometry study  |  camera looks north, 40 degrees down  |  roof colours retained  |  candidate')
 scale=7.0;theta=math.radians(40)
 def xy(v,h=0):return (60+(v[0]+118)*scale,230+(v[1]+140)*math.sin(theta)*scale-h*math.cos(theta)*scale)
 def poly(v,h,fill,outline=None):d.polygon([xy(a,h) for a in v],fill=fill,outline=outline)
 poly(P['extent'],0,'#e4decf')
 for t in P['terrain']['terraces']:
  pts=t['polygon'];h=t['height_m']
  for a,b in g.edges(pts):d.polygon([xy(a),xy(b),xy(b,h),xy(a,h)],fill='#a69b87',outline='#938c7d')
  poly(pts,h,'#ddd8c6')
 for t in P['terrain']['cliffs']:
  poly(t['polygon'],t['crest_m'],'#9da28f')
  a,b=t['polygon'][2:4];d.polygon([xy(a,4),xy(b,4),xy(b,16),xy(a,16)],fill='#7f8c7c')
 poly(P['river']['polygon'],-4,'#83aebb');poly(P['waterworks']['feeder_polygon'],2.4,'#83aebb')
 meadow(im,P,xy)
 for s in P['green']['spaces']:
  for a in s['polygons']:poly(a,s['ground_y_m'],GRASS if s['kind']!='allotment' else '#b8b386')
 for c in P['clusters']:
  if 'court_polygon' in c:
   h=next(b['ground_y_m'] for b in P['buildings'] if b['id'] in c['building_ids']);poly(c['court_polygon'],h,'#d2c4aa')
 poly(next(z['polygon'] for z in P['ground_zones'] if z['id']=='red_tree_bed'),0,'#a8b581')
 for r,i,a,b in g.segments(P):
  v=g.strip(a,b,r['width_m']);hs=[r['heights_m'][i],r['heights_m'][i+1],r['heights_m'][i+1],r['heights_m'][i]]
  d.polygon([xy(q,h) for q,h in zip(v,hs)],fill='#eddfbb' if r['id']=='main_road' else ROAD)
 poly(P['hq_reservation']['polygon'],.6,'#e3c98d',INK)
 screen(d,P,xy)
 # Draw individual objects from back to front for the straight-north camera.
 objects=[]
 for b in P['buildings']:objects.append(((b['footprint'][1]+b['footprint'][3])/2,'building',b))
 for t in P['green']['trees']:objects.append((t['position'][1],'tree',t))
 for a in P['props']:
  if 'footprint' in a:objects.append(((a['footprint'][1]+a['footprint'][3])/2,'prop',a))
 for _,kind,b in sorted(objects,key=lambda t:t[0]):
  if kind=='tree':
   pos=b['position'];h=b.get('ground_y_m',0);a=xy(pos,h);c=xy(pos,h+b['height_m']*.8);rr=b['canopy_radius_m']*scale
   d.line((a,c),fill='#776c54',width=4);d.ellipse((c[0]-rr,c[1]-rr*.72,c[0]+rr,c[1]+rr*.72),fill='#a64e42' if b['id']=='tree_08' else '#65845a',outline='#4e704d')
   continue
  if kind=='prop':propdraw(d,b,xy);continue
  base=b['ground_y_m'];h=base+b['height_m'];roof=b['roof_height_m'];col=ROOFS[b['roof_palette']]
  for f in b.get('collision_rectangles',[b['footprint']]):
   v=[g.rotate(q,b) for q in g.boxpoly(f)]
   # Front and side walls; roof ridge runs north/south.
   for i in [3,1,2]:
    a,c=v[i],v[(i+1)%4];d.polygon([xy(a,base),xy(c,base),xy(c,h),xy(a,h)],fill='#bdb295' if i!=2 else '#d4c7a9',outline='#726d5d')
   x0,z0,x1,z1=f;rn=g.rotate([(x0+x1)/2,z0],b);rs=g.rotate([(x0+x1)/2,z1],b)
   d.polygon([xy(v[0],h),xy(v[3],h),xy(rs,h+roof),xy(rn,h+roof)],fill=col,outline='#485346')
   rgb=tuple(int(col[i:i+2],16) for i in (1,3,5));light=tuple(min(255,int(a*1.17)) for a in rgb)
   d.polygon([xy(rn,h+roof),xy(rs,h+roof),xy(v[2],h),xy(v[1],h)],fill=light,outline='#485346')
   d.polygon([xy(v[3],h),xy(v[2],h),xy(rs,h+roof)],fill='#c9ba9b',outline='#746c5a')
  if b['id']=='watch_tower':
   a=xy([0,-66.95],base+20);d.ellipse((a[0]-8,a[1]-8,a[0]+8,a[1]+8),fill='#efe4bc',outline=INK)
 for i,c in enumerate(P['clusters']):
  bb=[b for b in P['buildings'] if b['id'] in c['building_ids']];x=sum((b['footprint'][0]+b['footprint'][2])/2 for b in bb)/len(bb);z=max(b['footprint'][3] for b in bb)+3
  badge(d,xy([x,z],bb[0]['ground_y_m']),i+1,tint(i),14)
 legend(d,2040,165)
 d.text((60,1585),'Green / plum / warm-red / brown roofs follow retained facade uses. Groves occupy the gaps between groups.',font=font(22),fill=INK)
 d.text((60,1625),'Orthographic review projection at the gameplay direction; not a Godot capture or final perspective/occlusion test.',font=font(21),fill=INK)
 im.save(R/'bird-view-sketch-v7b.png')

if __name__=='__main__':
 mainmap();comparison();bird()
 manifest=dict(plan_sha256=hashlib.sha256((R/'eurydica-plan-v7b.json').read_bytes()).hexdigest(),
  renderer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  comparison=dict(pixels_per_metre=5.5,world_extent=[-118,-140,151,137],same_scale=True,versions=['v7','v7b']),
  bird_view=dict(direction='north',down_angle_degrees=40,projection='orthographic massing study'),images={})
 for name in ('cluster-map-v7b.png','bird-view-sketch-v7b.png','v7-vs-v7b.png'):
  manifest['images'][name]=dict(size=list(Image.open(R/name).size),sha256=hashlib.sha256((R/name).read_bytes()).hexdigest())
 (R/'render-manifest-v7b.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print('REVIEW_RENDER_PASS')

