"""JSON-only deterministic geometry renderer: same polygons in PNG and SVG."""
import sys,json,html,math,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
from PIL import Image,ImageDraw,ImageFont
import inherited_checks as g
R=Path(__file__).resolve().parent
P=json.loads((R/'eurydica-plan.json').read_bytes());B=json.loads((R/'baseline/approved-v4/eurydica-plan.json').read_bytes())
M=json.loads((R/'check-result.json').read_text());SHA=hashlib.sha256((R/'eurydica-plan.json').read_bytes()).hexdigest()
newprops=P['props'][len(B['props']):];newmarks=P['markers'][len(B['markers']):]
roof=dict(green='#477d62',plum='#94778f',warm_red='#bc7c65',brown='#947454')
colors=dict(grass='#dce6c3',paving='#ebe3d2',earth='#e0ccb0',dressed_stone='#d9dad0',garden_bed='#b7c898')
class Canvas:
 def __init__(self,w,h):
  self.w,self.h=w,h;self.im=Image.new('RGB',(w,h),'#faf8f0');self.d=ImageDraw.Draw(self.im);self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><rect width="100%" height="100%" fill="#faf8f0"/>']
 def text(self,pos,s,size=20,color='#273f3b',bold=False):
  font=ImageFont.truetype('C:/Windows/Fonts/arial'+('bd' if bold else '')+'.ttf',size);self.d.text(pos,s,font=font,fill=color);self.svg.append(f'<text x="{pos[0]:.2f}" y="{pos[1]+size*.84:.2f}" font-family="Arial" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{html.escape(s)}</text>')
 def poly(self,pts,color,outline='#a49d8b',width=1):
  self.d.polygon(pts,fill=color);self.d.line(pts+[pts[0]],fill=outline,width=width);self.svg.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="{color}" stroke="{outline}" stroke-width="{width}"/>')
 def line(self,pts,color,width=2):
  self.d.line(pts,fill=color,width=width);self.svg.append('<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
 def circle(self,pos,r,color,outline='#384d42'):
  x,y=pos;self.d.ellipse([x-r,y-r,x+r,y+r],fill=color,outline=outline,width=1);self.svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{color}" stroke="{outline}"/>')
 def save(self,name):
  self.im.save(R/(name+'.png'));(R/(name+'.svg')).write_text('\n'.join(self.svg+['</svg>']),encoding='utf-8')
def panel(c,bounds,viewport,labels=None,ceremony=False,full=False):
 x0,z0,x1,z1=bounds;left,top,w,h=viewport;s=min(w/(x1-x0),h/(z1-z0));left+=(w-(x1-x0)*s)/2
 def xy(pt):return (left+(pt[0]-x0)*s,top+(pt[1]-z0)*s)
 def visible(pts):return min(v[0] for v in pts)<=x1 and max(v[0] for v in pts)>=x0 and min(v[1] for v in pts)<=z1 and max(v[1] for v in pts)>=z0
 # Render on an isolated image/SVG viewport; clip all geometry to bounds in both formats.
 temp=Canvas(math.ceil((x1-x0)*s),math.ceil((z1-z0)*s))
 c.svg.append(f'<defs><clipPath id="clip{len(c.svg)}"><rect x="{left}" y="{top}" width="{temp.w}" height="{temp.h}"/></clipPath></defs>')
 clip=f'clip{len(c.svg)-1}';c.svg.append(f'<g clip-path="url(#{clip})">')
 origd=c.d;c.d=temp.d
 # Draw PIL with coordinates local to the clipped viewport; SVG keeps global positions.
 class LocalDraw:
  def polygon(self,pts,**kw):temp.d.polygon([(x-left,y-top) for x,y in pts],**kw)
  def line(self,pts,**kw):temp.d.line([(x-left,y-top) for x,y in pts],**kw)
  def ellipse(self,rect,**kw):temp.d.ellipse([rect[0]-left,rect[1]-top,rect[2]-left,rect[3]-top],**kw)
  def text(self,pos,*args,**kw):temp.d.text((pos[0]-left,pos[1]-top),*args,**kw)
 c.d=LocalDraw()
 for z in sorted(P['ground_zones'],key=lambda a:a.get('priority',0)):
  if visible(z['polygon']):c.poly([xy(v) for v in z['polygon']],colors[z['material']],colors[z['material']])
 for poly in [P['river']['polygon'],P['waterworks']['feeder_polygon']]:
  if visible(poly):c.poly([xy(v) for v in poly],'#afd0d4','#7caaaf')
 for cliff in P['terrain']['cliffs']:
  if visible(cliff['polygon']):c.poly([xy(v) for v in cliff['polygon']],'#9da499','#7c857b')
 for a in P['squares']:
  if visible(a['polygon']):c.poly([xy(v) for v in a['polygon']],'#f3e8ce','#ba9a60',2)
 for r,i,a,b in g.segments(P):
  pts=g.strip(a,b,r['width_m'])
  if visible(pts):c.poly([xy(v) for v in pts],'#ddd8cb' if r['surface']!='earth' else '#c9b38f','#beb7a5')
 if ceremony:
  pts=next(a['polygon'] for a in P['squares'] if a['id']=='clock_plaza');c.line([xy(v) for v in pts+[pts[0]]],'#ba9a60',3)
 for b in P['buildings']:
  pts=g.footprint(b)
  if not visible(pts):continue
  c.poly([xy(v) for v in pts],roof[b['roof_palette']],'#4c5147',2)
  c.circle(xy(b['door_position']),max(2,.18*s),'#fff6cc')
  if b['id']=='south_gate':c.poly([xy(v) for v in b['walk_through_opening']],'#ddd8cb')
 for t in P['green']['trees']:
  if visible([t['position']]):c.circle(xy(t['position']),max(2,t['canopy_radius_m']*s),'#bd7355' if t['palette'].startswith('copper') else '#93ac7e');c.circle(xy(t['position']),max(1,t['trunk_collision_radius_m']*s),'#735740')
 for prop in B['props']:
  if prop.get('position') and visible([prop['position']]):c.circle(xy(prop['position']),max(2,prop['collision_radius_m']*s),'#90846e')
 for a in newprops:
  poly=g.boxpoly(a['footprint'])
  if visible(poly):
   col='#678b66' if a['type']=='raised_produce_bed' else '#f7ecc1' if a['type']=='market_stall' else '#b88754'
   c.poly([xy(v) for v in poly],col,'#5b653f',2)
   f=a['footprint'];typ=a['type'];cx=(f[0]+f[2])/2;cz=(f[1]+f[3])/2
   if typ in ('timber_pile','timber_stack','lumber_drying_rack','raised_produce_bed'):
    for t in (.25,.5,.75):
     z=f[1]+(f[3]-f[1])*t;c.line([xy([f[0]+.15,z]),xy([f[2]-.15,z])],'#4f6a45' if typ=='raised_produce_bed' else '#735434',max(1,round(s*.1)))
   if typ in ('crate_stack','crates','tool_shed','covered_lean_to','stacked_materials'):
    c.line([xy([f[0],f[1]]),xy([f[2],f[3]])],'#735434',1);c.line([xy([f[2],f[1]]),xy([f[0],f[3]])],'#735434',1)
   if typ in ('barrel_group','rope_coils','baskets','water_butt'):
    c.circle(xy([cx,cz]),max(1,min(f[2]-f[0],f[3]-f[1])*s*.3),'#c1a47b')
   if typ=='fruit_tree':c.circle(xy([cx,cz]),s*.95,'#809b65');c.circle(xy([cx,cz]),max(1,s*.15),'#785d3e')
   if typ in ('low_fence','open_gate'):c.line([xy([f[0],f[1]]),xy([f[2],f[3]])],'#66734c',max(2,round(s*.15)))
   if typ=='hand_hoist':c.line([xy([cx,f[3]]),xy([cx,f[1]]),xy([f[2],f[1]])],'#514739',max(2,round(s*.3)))
   if typ in ('cart','barrow'):
    for x in (f[0],f[2]):c.circle(xy([x,cz]),max(1,s*.2),'#514739')
   if a['type']=='market_stall':
    f=a['footprint']
    for x in (f[0]+.4,f[0]+1.0):c.line([xy([x,f[1]]),xy([x,f[3]])],'#849d75',max(1,round(s*.15)))
 for m in newmarks:
  if m['scene']!='city' or not visible([m['position']]):continue
  pos=m['position'];color='#745588' if m.get('kind')=='camera_hint' else '#e8bf59' if 'leaders_' in m['id'] else '#416c91' if 'officers_' in m['id'] else '#ba604a'
  c.circle(xy(pos),max(3,.25*s),color)
  if ceremony:
   facing=1 if m.get('facing')=='south' else -1
   c.line([xy(pos),xy([pos[0],pos[1]+facing*.6])],color,3)
 if full:
  for wall in P['city_wall']['segments']:c.line([xy(v) for v in wall],'#53695a',4)
  for wall in P['terrain']['retaining_walls']:c.line([xy(v) for v in wall['polyline']],'#708273',3)
  for hedge in P['green']['hedges']:c.line([xy(v) for v in hedge['polyline']],'#5b7951',2)
  for u in P['hq_reservation']['upgrades']:c.line([xy(v) for v in u['polygon']+[u['polygon'][0]]],'#b45d88',3)
  pts=P['phase_1']['polygon'];c.line([xy(v) for v in pts+[pts[0]]],'#c89532',3)
  for b in P['buildings']:
   if b['id'] in ('tavern','company_house','lodging','south_gate','watch_tower','stables'):
    f=b['footprint'];c.text(xy([f[0],f[3]+1]),b['display_name'],14,bold=True)
 if labels:
  for label,pos in labels:
   c.circle(xy(pos),12,'#faf8f0');x,y=xy(pos);c.text((x-4.5*len(label),y-8),label,16,bold=True)
 c.d=origd;c.im.paste(temp.im,(round(left),round(top)));c.svg.append('</g>')
 c.line([(left,top),(left+temp.w,top),(left+temp.w,top+temp.h),(left,top+temp.h),(left,top)],'#b9b4a8',2)
 c.text((left+10,top+10),'N ^',18,bold=True)
 distance=2 if ceremony else 10 if x1-x0<100 else 50
 y=top+temp.h-28;c.line([(left+15,y),(left+15+distance*s,y)],'#273f3b',3);c.text((left+15,y-25),f'{distance} m',17)
 return xy
def heading(c,title,subtitle):
 c.text((45,30),title,34,bold=True);c.text((45,80),subtitle,19);c.text((45,c.h-33),'CANDIDATE | JSON geometry authoritative | SHA-256 '+SHA,14)
def notes(c,items,x=1000,y=160,size=19):
 for line in items:c.text((x,y),line,size);y+=size+13

c=Canvas(2100,2470);heading(c,'EURYDICA / BUILD PLAN v5','Approved v4 layout with localized market, props, roof-kit and story additions. North up; metres.')
panel(c,[-115,-130,135,312],(45,130,1230,2250),full=True)
notes(c,['LOCALIZED CANDIDATE','83 buildings / footprints retained','126 routes / six junctions retained','59 markers: 36 retained + 23 new','79 new props / one allotment zone','','MARKET','Four green-roof business adaptations','Three awning clusters / three each','All route and door strips clear','','WORK AND HOUSEHOLD ROUTINES','Ten beds / fence / gate / facilities','20 props in each working yard','Six evening spots; depart at 21:00','Two Guild courtyard resting patches','','STORY STAGE','12 figures before the clock tower','1.80 m minimum centre spacing','1.30 m minimum body-edge spacing','Plaza polygon unchanged','','LOCKS','Gate-market: 217.808 m / 68.065 s','28 m clock tower / unchanged position','HQ expansion polygons unchanged','Dorm access recorded on rooms/portals','','ROOF COLOURS','Green: public / businesses','Plum: homes / Guild','Warm red: service / old homes','Brown: working buildings','','See the four local review diagrams.','Roof kits are specified in JSON;','this plan depicts ground footprints.','No generated illustration or runtime edit.'],x=1340,y=150,size=23)
c.save('eurydica-plan')

c=Canvas(1480,1250);heading(c,'MARKET / RED-TREE COURT','Four facade/use changes. Existing footprints, doors, route widths and red tree retained.')
labels=[];legend=[]
ids=['infill_home_12','infill_home_06','street_home_8','infill_home_23']
for i,id in enumerate(ids,1):
 b=next(b for b in P['buildings'] if b['id']==id);f=b['footprint'];labels.append((str(i),[(f[0]+f[2])/2,(f[1]+f[3])/2]));legend.append(f'{i}  {b["display_name"]}')
for label,pos,description in [('A',[-5.9,86.7],'Court cluster'),('B',[5.7,99.7],'Widened-edge cluster'),('C',[6.2,109.7],'Southern seam cluster')]:
 labels.append((label,pos));legend.append(label+'  '+description)
panel(c,[-24,63,24,126],(40,145,840,1020),labels)
notes(c,legend+['','A / B / C: three awnings each','Crates, baskets + barrow per cluster','','Awnings included in footprints.','Grey = preserved travel strips.','Gold = red-tree court boundary.','Pale dots = existing door positions.','','4 sits at the southern market seam','(footprint z116.5-123.5 m).','Existing Repair & Supply retained.'],x=920,y=170,size=19)
c.save('review/market-red-tree-court')

c=Canvas(1480,1000);heading(c,'SPINE / SERVICE LANES ALLOTMENTS','One household growing patch with walkable tending aisles; no route or building changes.')
labels=[];legend=[]
for i,prop in enumerate([a for a in newprops if a['type']=='raised_produce_bed'],1):
 f=prop['footprint'];labels.append((str(i),[(f[0]+f[2])/2,(f[1]+f[3])/2]))
for label,id in [('S','allotment_tools'),('W','allotment_water_butt'),('C','allotment_compost')]:
 a=next(a for a in newprops if a['id']==id);f=a['footprint'];labels.append((label,[(f[0]+f[2])/2,(f[1]+f[3])/2]))
panel(c,[0,66,72,119],(40,145,880,750),labels)
notes(c,['30 x 42 m / 1,260 m2 growing patch','1-10: varied produce / herb beds','S: tool shed  W: water butt','C: compost heap','','Low fence around the patch','3 m public gate on the east edge','At least 2 m between bed footprints','All beds reachable with 1.2 m body','','Two fruit trees on the southern edge','Existing trees retained in place','Existing shops and routes retained.'],x=965,y=170,size=19)
c.save('review/spine-service-allotments')

c=Canvas(1650,1710);heading(c,'WORKSHOP / QUAYS YARDS','20 props per yard, clustered at walls and workstations. Work loops and door approaches retained.')
for x,prefix,bounds,title in [(45,'quays',[-110,-15,-35,109],'QUAYS'),(850,'workshop',[-110,116,-57,265],'WORKSHOP')]:
 props=[a for a in newprops if a['id'].startswith(prefix+'_')];labels=[]
 for i,a in enumerate(props,1):
  f=a['footprint'];labels.append((str(i),[(f[0]+f[2])/2,(f[1]+f[3])/2]))
 c.text((x,135),title,24,bold=True);panel(c,bounds,(x,180,750,1040),labels)
 for col in range(2):
  notes(c,[str(i+1)+'  '+a['type'].replace('_',' ') for i,a in enumerate(props) if i//10==col],x=x+15+col*365,y=1250,size=17)
c.save('review/workshop-quays-yards')

c=Canvas(1550,1060);heading(c,'CIVIC TERRACE / ALLIANCE APPOINTMENT','12 figures in the unchanged clock plaza. Diagram shows 0.5 m body discs and facing directions.')
labels=[]
for m in newmarks:
 if not m['id'].startswith('civic_terrace/'):continue
 short=m['id'].split('/')[-1];label='L'+short[-1] if short.startswith('leaders') else 'O'+short[-1] if short.startswith('officers') else 'C' if short=='commander' else 'E' if short=='envoy' else 'cam'
 labels.append((label,[m['position'][0],m['position'][1]-.5]))
xy=panel(c,[-10,-76,25,-59],(40,170,1020,650),ceremony=True)
for label,point in labels:
 x,y=xy(point);c.text((x-10,y-10),label,17,bold=True)
notes(c,['L1-L5: leaders, facing south','C: Commander, facing north','O1-O5: officers behind Commander','E: envoy beside leaders','cam: push-in ground anchor','','Minimum centre distance: 1.80 m','Minimum body-edge gap: 1.30 m','Tower / notice shelter remain clear.','All anchors on walkable plaza ground.','All outdoor markers reach the routes.','','Camera anchor is nonphysical.','Story staging is temporary.','No plaza or building changes needed.'],x=1090,y=180,size=18)
c.text((65,860),'Clock tower: footprint x -3..3, z -73..-67. Notice shelter: x 19..23, z -66..-63.',21)
c.text((65,903),'Gold outline: approved plaza. Grey strips: existing approaches. North is negative z.',21)
c.save('review/civic-terrace-group')
(R/'map-provenance.json').write_text(json.dumps(dict(plan_sha256=SHA,renderer='render_plan.py',method='Identical JSON polygons for PNG and SVG; no image generation',reviews=['market-red-tree-court','spine-service-allotments','workshop-quays-yards','civic-terrace-group']),indent=2)+'\n')
print('MAP_RENDER_PASS')
