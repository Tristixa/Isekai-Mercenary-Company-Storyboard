"""Refine the existing candidate only. No writes outside the v7 run directory."""
import sys,json,copy,math,random,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as g
from geometry_v7b import *
R=Path(__file__).resolve().parent
V=json.loads((R/'eurydica-plan.json').read_bytes());P=copy.deepcopy(V)
B={b['id']:b for b in P['buildings']};VB={b['id']:b for b in V['buildings']}
P.update(plan_revision='v7b',source_v7_sha256=hashlib.sha256((R/'eurydica-plan.json').read_bytes()).hexdigest())
if not (R/'source-manifest-v7b.json').exists():
 (R/'source-manifest-v7b.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in R.iterdir() if f.is_file() and 'v7b' not in f.name},indent=2))

# The centre of every group remains local to v7. Angles follow the nearby frontage.
# Gate arch, clock, appointment and Guild staging remain fixed constraint anchors.
spec={
 'gate_cluster':(0,0,0), 'guild_compound':(-5,0,-.5),
 'lodging_row':(-5,1,0),'arrival_court':(10,1,1),
 'red_tree_court':(-5,-1,0),'market_row':(5,1,0),
 'market_homes':(-10,1,0),'service_lane':(5,1,0),
 'service_homes':(-10,1,0),'arrival_west_court':(5,-1,-1),
 'guild_neighbours':(-5,0,0),'arrival_garden_court':(-10,1.5,0),
 'service_garden_row':(5,1,0),'market_riverside':(5,0,1),
 'workshop_yard':(-5,-.7,0),'quay_row':(5,1,1),
 'civic_plaza':(0,0,0),'old_city_row':(-5,0,0),
 'residential_a':(10,0,0),'residential_b':(-5,-.6,0),
 'waterworks_group':(5,0,0)}
transforms={}
for c in P['clusters']:
 bs=[B[id] for id in c['building_ids']]
 pivot=[sum((b['footprint'][i]+b['footprint'][i+2])/2 for b in bs)/len(bs) for i in (0,1)]
 yaw,dx,dz=spec[c['id']];transforms[c['id']]=(pivot,yaw,[dx,dz])
 c['frontage_yaw_deg']=yaw;c['v7b_pivot']=pivot
 for i,b in enumerate(bs):
  if b['id'] in ('south_gate','watch_tower'):continue
  f=b['footprint'];w,d=f[2]-f[0],f[3]-f[1];ctr=transform([(f[0]+f[2])/2,(f[1]+f[3])/2],pivot,yaw,[dx,dz])
  b['footprint']=[ctr[0]-w/2,ctr[1]-d/2,ctr[0]+w/2,ctr[1]+d/2];b['yaw_deg']=yaw
  b['door_position']=transform(b['door_position'],pivot,yaw,[dx,dz])
 if 'court_polygon' in c and c['id']!='guild_compound':c['court_polygon']=[transform(p,pivot,yaw,[dx,dz]) for p in c['court_polygon']]

# A few half-metre steps and five-degree turns within groups, accepted only when
# they keep all original sizes, collision freedom and <=2m neighbouring walls.
from check_plan import gap
rng=random.Random(731)
for c in P['clusters']:
 if c['id'] in ('gate_cluster','guild_compound','civic_plaza'):continue
 for idx,id in enumerate(c['building_ids']):
  if idx%2==0:continue
  b=B[id];saved=copy.deepcopy(b)
  for ang,dx,dz in [(5,.25,0),(-5,-.25,.25),(0,.5,0),(0,0,.4)]:
   b.clear();b.update(copy.deepcopy(saved));b['yaw_deg']+=ang
   b['footprint']=[v+(dx if i%2==0 else dz) for i,v in enumerate(b['footprint'])]
   bs=[B[j] for j in c['building_ids']]
   if any(overlap(g.footprint(x),g.footprint(y)) for i,x in enumerate(bs) for y in bs[i+1:]):continue
   if all(min(gap(g.footprint(x),g.footprint(y)) for y in bs if y!=x)<=2.000001 for x in bs):break
  else:b.clear();b.update(saved)

# Ground-owned courts track rotations; narrative staging remains in its original
# Guild positions. District envelopes are descriptive bounds, not moved terrain.
for id in ('service_home_0','service_home_3'):
 b=B[id];b['footprint']=[v+(1.5 if i%2==0 else 0) for i,v in enumerate(b['footprint'])]
B['washing']['footprint']=[v+(-.8 if i%2==0 else 0) for i,v in enumerate(B['washing']['footprint'])]
B['infill_home_19']['footprint']=[v+(-1 if i%2==0 else 0) for i,v in enumerate(B['infill_home_19']['footprint'])]
for id,ang in [('guard_shelter',5),('street_home_1',-5),('infill_home_11',5),('toll_records',5),('civic_guard',-5),('notice_shelter',5)]:B[id]['yaw_deg']=ang
cs={c['id']:c for c in P['clusters']}
for z in P['ground_zones']:
 for cid,c in cs.items():
  if z['id']==cid+'_surface' and 'court_polygon' in c:z['polygon']=copy.deepcopy(c['court_polygon'])
 if z['id']=='red_tree_bed':z['polygon']=[transform(p,*transforms['red_tree_court']) for p in z['polygon']]
for s in P['squares']:
 if s['id']=='red_tree_court':s['polygon']=copy.deepcopy(cs['red_tree_court']['court_polygon'])
red=next(t for t in P['green']['trees'] if t['id']=='tree_08');red['position']=transform(red['position'],*transforms['red_tree_court'])
next(l for l in P['landmarks'] if l['id']=='red_tree')['position']=red['position']
for d in P['districts']:
 pts=[v for b in P['buildings'] if b['district']==d['id'] for v in g.footprint(b)]+d['bounds']
 x,z,X,Z=bounds(pts);d['bounds']=g.boxpoly([x-.05,z-.05,X+.05,Z+.05])
next(d for d in P['districts'] if d['id']=='workshops')['bounds']=g.boxpoly([-113,40,-66,98])

P['routes']=[]
def route(id,pts,width=4.5,phase=1,ys=None,surface='paved_local',kind='street',owner=None,branch=None):
 pts=[list(p) for i,p in enumerate(pts) if not i or math.dist(p,pts[i-1])>1e-8]
 ys=ys or [0]*len(pts)
 r=dict(id=id,centreline=pts,width_m=width,heights_m=ys,grade=[(v-u)/math.dist(a,b) for u,v,a,b in zip(ys,ys[1:],pts,pts[1:])],surface=surface,kind=kind,phase=phase,walkable=True)
 if owner:r['owner']=owner
 if branch:r['branch_group']=branch
 P['routes'].append(r);return r
route('gate_arch',[[0,126],[0,118]],4.6,kind='gate_passage')
# Smooth sampled spine (junctions lie exactly on its sampled segments).
spine=[]
for z in range(118,-6,-3):
 x=2.4*math.sin((118-z)*math.pi/61.5)
 spine.append([x,z])
spine[-1]=[0,-5]
route('main_road',spine,7,surface='paved_main')
def onmain(z):
 for a,b in zip(spine,spine[1:]):
  if b[1]<=z<=a[1]:return [a[0]+(b[0]-a[0])*(z-a[1])/(b[1]-a[1]),z]
j={n:onmain(z) for n,z in {1:75,2:15,3:60,4:104,5:108,6:68}.items()}
for n,pt in j.items():
 next(v for v in P['junctions'] if v['id']==n)['position']=pt
 next(v for v in P['approved_connections'] if v['id']==n)['junction']=pt
route('join5',[j[5],[-12,108],[-24,108]],5,ys=[0,0,.6],branch='guild_gate')
route('gate_side',[[0,118],[-5,114],[-16,113]],4,branch='guild_gate')
# Shared arrival branch: west court arm and east arrival / Guild neighbours arm.
route('join1',[j[1],[-8,84],[-18,87],[-28,85]],4.5,branch='arrival_courts')
route('join4',[j[4],[19,102],[27,100],[48,99],[68,99]],4.5,branch='arrival_courts')
route('service_public_loop',[[68,99],[86,92],[88,82]],4,branch='arrival_courts')
# Service branch stops inside the lane; rear sides have no perimeter road.
route('join3',[j[3],[21,58],[42,51],[67,48],[87.5,46],[89,35],[90,24],[90.5,18]],4.5,branch='service')
# Working branch has two retained cross-district connections, one common arm.
route('join6_apron',[j[6],[-10,57],[-28,54],[-45,57]],4.5,branch='workshops_quays')
route('join6',[[-45,57],[-62,62],[-68,65]],4.5,2,surface='earth',branch='workshops_quays')
route('join2_apron',[j[2],[-8,9],[-28,7],[-45,10]],4.5,branch='workshops_quays')
route('join2_earth',[[-45,10],[-65,9],[-82,10]],4.5,2,surface='earth',branch='workshops_quays')
fixed=['old_bridge','civic_approach','civic_old_ramp','civic_res_ramp','watch_stairs','view_deck','dock_ramp','dock_deck']
for old in V['routes']:
 if old['id'] in fixed:
  r=copy.deepcopy(old)
  P['routes'].append(r)
route('dock_access',[[-82,10],[-80,5]],4,2,surface='earth',branch='workshops_quays')
# Only one intentional north-bank loop. Its north leg serves Old City frontage;
# the western segment supplies the existing watch stairs, all at the fixed 4m.
route('old_city_walk',[[-40,-60],[-49,-69],[-54,-89],[-78,-91],[-102,-89],[-102,-70]],4,2,[4]*6,branch='north_bank')
route('old_park',[[-102,-70],[-82,-65],[-62,-61],[-40,-60]],4,2,[4]*4,branch='north_bank')
route('residential_walk',[[40,-60],[49,-73],[55,-85],[71,-84],[91,-88],[104,-88]],4,2,[4]*6,branch='north_bank')
route('north_riverside',[[104,-88],[104,-69],[100,-52],[122,-52]],4,2,[4]*4,branch='north_bank')
# Small public court alleys are dead-ended; only these, never cluster rings.
for id,pts,h,phase in [
 ('arrival_court_lane',[[43,99.24],[44,90],[44,82],[44,80]],0,1),
 ('west_court_lane',[[-28,85],[-28,76]],0,1),
 ('market_homes_lane',[[42,51],[47,42],[46,26],[43,23]],0,1),
 ('red_tree_court_access',[onmain(31),[-12,31],[-24.5,33],[-26,26]],0,1),
 ('service_homes_lane',[[88,82],[88,74]],0,1),
 ('residential_a_lane',[[55,-85],[47,-89],[43,-98]],4,2),
 ('residential_b_lane',[[71,-84],[73,-94]],4,2),
 ('orchard_lane',[[-62,62],[-47,56],[-45,51]],0,1),
 ('waterkeeper_lane',[[104,-88],[105,-95],[105,-114],[91,-114]],4,2),
 ('civic_plaza_lane',[[0,-60],[7,-65],[7,-78],[-4,-78],[-4,-87],[-20,-87],[-20,-75]],2,2),
 ('service_garden_access',[[88,82],[105,88],[106,77]],0,1),
 ('allotment_lane',[[106,77],[106,57],[144,55],[144,39],[141,39]],0,1),
 ('quay_court',[[-82,10],[-68,15],[-68,34],[-80,38],[-99,38]],0,2),
 ('guild_court_aisle',[[-24,108],[-43,108]],.6,1),
 ('bridge_homes_court',[onmain(13),[22,13],[31,11],[31,-1]],0,1),
 ('workshop_court',[[-68,65],[-78,65],[-86,66]],0,2)]:
 route(id,pts,2,phase,[h]*len(pts),kind='alley')
# The arrival branch is diagonal here; snap its court alley to that exact segment.
rr=next(r for r in P['routes'] if r['id']=='arrival_court_lane')
rr['centreline'][0]=[43,99+(48-43)/21]
for r in P['routes']:
 if r.get('branch_group') and r['id']!='join5':r['width_m']=4

S=[(b['id'],[g.rotate(v,b) for v in g.boxpoly(f)]) for b in P['buildings'] for f in b.get('collision_rectangles',[b['footprint']])]
if '--layout-only' in sys.argv:
 (R/'layout-draft-v7b.json').write_text(json.dumps(P,indent=2))
 print('LAYOUT_ONLY');sys.exit(0)
blocked=[s for _,s in S]+[P['river']['polygon'],P['waterworks']['feeder_polygon'],P['hq_reservation']['polygon']]
blocked_bounds=[(s,bounds(s)) for s in blocked]
def clearline(a,b,w=2):
 if math.dist(a,b)<1e-8:return False
 poly=g.strip(a,b,w)
 x,z,X,Z=bounds(poly)
 return not any(overlap(poly,s) for s,(u,v,U,V) in blocked_bounds if min(X,U)>max(x,u)+1e-7 and min(Z,V)>max(z,v)+1e-7)

# Print backbone collisions early; do not paper over failures with door routing.
for r,i,a,b in g.segments(P):
 for id,s in S:
  if overlap(g.strip(a,b,r['width_m']),s):print('BACKBONE_COLLISION',r['id'],id,flush=True)

for b in P['buildings']:
 if b['id']=='south_gate':continue
 x,z,X,Z=b['footprint'];original=b['door_face'];choices=[]
 for face,fraction in [(f,t) for f in [original]+[f for f in ('s','n','e','w') if f!=original] for t in (.5,.25,.75,.125,.875)]:
  local={'s':[x+(X-x)*fraction,Z],'n':[x+(X-x)*fraction,z],'e':[X,z+(Z-z)*fraction],'w':[x,z+(Z-z)*fraction]}[face]
  normal={'s':[0,1],'n':[0,-1],'e':[1,0],'w':[-1,0]}[face]
  door=g.rotate(local,b);out=g.rotate([local[i]+normal[i]*1.6 for i in (0,1)],b)
  for r,i,a,c in g.segments(P):
   if r['kind'] in ('stairs','dock','gate_passage'):continue
   q,t=nearest(out,a,c);h=r['heights_m'][i]+t*(r['heights_m'][i+1]-r['heights_m'][i])
   if abs(h-b['ground_y_m'])>.001:continue
   for mid in ([],[[out[0],q[1]]],[[q[0],out[1]]]):
    pts=[q]+mid+[out,door];pts=[p for i,p in enumerate(pts) if not i or math.dist(p,pts[i-1])>.001]
    if all(clearline(a,c) for a,c in zip(pts,pts[1:])):
     length=sum(math.dist(a,c) for a,c in zip(pts,pts[1:]));choices.append((length+(0 if face==original else 2)+(0 if fraction==.5 else .5),pts,face,door))
 if not choices:print('NO_DOOR',b['id'],flush=True);continue
 _,pts,face,door=min(choices,key=lambda a:a[0]);b['door_face']=face;b['door_position']=door;b['door_route']='door_'+b['id']
 route(b['door_route'],pts,2,b['phase'],[b['ground_y_m']]*len(pts),kind='door_approach',owner=b['id'])

# Place-bound markers move with their group except the fixed Guild story circle.
for m in P['markers']:
 if m['scene']!='city' or m['id'].startswith('civic_terrace/'):continue
 place=m.get('place_binding')
 if place in B and place not in ('south_gate','stables'):
  b=B[place];door=b['door_position'];local=g.rotate(door,b,True);normal={'s':[0,1],'n':[0,-1],'e':[1,0],'w':[-1,0]}[b['door_face']]
  loc=[local[i]+normal[i]*2 for i in (0,1)]
  if m['id'].endswith(('457','483')):loc[1 if b['door_face'] in ('w','e') else 0]+=1.5
  m['position']=g.rotate(loc,b)
 elif place in cs and place not in ('guild_compound','gate_cluster'):m['position']=transform(m['position'],*transforms[place])
for n in P['npc_spots']:
 m=next(m for m in P['markers'] if m['id']==n['marker_id']);n['position']=m['position'];n['height_m']=m['height_m']
for portal in P['portals']:
 if 'city_building' in portal:portal['city_position']=B[portal['city_building']]['door_position']
P['walk_time'].update(start=onmain(118),finish=onmain(28))
# Insert exact measurement nodes; the graph retains every route segment.
main=next(r for r in P['routes'] if r['id']=='main_road')
for pt in [P['walk_time']['finish']]+list(j.values()):
 for i,(a,b) in enumerate(zip(main['centreline'],main['centreline'][1:])):
  if g.distance(pt,a,b)<1e-7 and math.dist(pt,a)>1e-7 and math.dist(pt,b)>1e-7:main['centreline'].insert(i+1,pt);break
main['heights_m']=[0]*len(main['centreline']);main['grade']=[0]*(len(main['centreline'])-1)
P['arrival_route']['waypoints']=[[0,132],[0,122]]+[onmain(z) for z in (108,75,28)]+[[0,-5]]

# Props are packed together beside their owning buildings, not sprinkled in a grid.
roadpolys=[g.strip(a,b,r['width_m']) for r,i,a,b in g.segments(P)]
occupied=[]
bed=next(z['polygon'] for z in P['ground_zones'] if z['id']=='red_tree_bed')
from PIL import Image,ImageDraw
import numpy as np
packmask=Image.new('1',(1120,1120));packdraw=ImageDraw.Draw(packmask)
def mpoly(poly):packdraw.polygon([((x+120)*4,(z+140)*4) for x,z in poly],fill=1)
for poly in blocked+roadpolys+[bed]:mpoly(poly)
for m in P['markers']:
 if m['scene']=='city':
  x,z=m['position'];mpoly(g.boxpoly([x-.85,z-.85,x+.85,z+.85]))
def prop_ok(poly,region=None):
 return (not region or all(g.inside(v,region) for v in poly)) and not any(overlap(poly,s) for s in blocked+roadpolys+occupied+[bed]) and all(not g.inside(m['position'],poly) and min(g.distance(m['position'],a,b) for a,b in g.edges(poly))>.8 for m in P['markers'] if m['scene']=='city')
def pack(a,rect,region=None):
 f=a.get('footprint');w,d=(f[2]-f[0],f[3]-f[1]) if f else (a.get('collision_radius_m',.25)*2,)*2
 x,z,X,Z=rect
 mask=np.asarray(packmask)
 options=[]
 for zz in range(int(z*2),int((Z-d)*2)+1):
  for xx in range(int(x*2),int((X-w)*2)+1):
   xx/=2;zz0=zz/2;poly=g.boxpoly([xx,zz0,xx+w,zz0+d])
   if mask[max(0,int((zz0+140)*4)):int((zz0+d+140)*4)+1,max(0,int((xx+120)*4)):int((xx+w+120)*4)+1].any():continue
   if a['id'].startswith('workshop_') and min(gap(poly,g.footprint(B[id])) for id in cs['workshop_yard']['building_ids'])>3.5:continue
   if prop_ok(poly,region):
    if f:a['footprint']=[xx,zz0,xx+w,zz0+d]
    else:a['position']=[xx+w/2,zz0+d/2]
    poly=g.boxpoly([xx-.12,zz0-.12,xx+w+.12,zz0+d+.12]);occupied.append(poly);mpoly(poly);return True
 return False

# Preserve each stock / prop ID. Four coherent work stations are explicitly named.
pile_regions={'timber':[-113,40,-67,60],'stone':[-113,74,-74,92],
 'crates':[-113,48,-93,61],'carts':[-91,79,-66,98]}
P['workshop_piles']=[]
for id,rect in pile_regions.items():P['workshop_piles'].append(dict(id=id,name=id.title()+' station',polygon=g.boxpoly(rect),prop_ids=[]))
work_clear=g.boxpoly([-88,62,-76,69])
P['workshop_clear_court']=work_clear
occupied.append(work_clear)
mpoly(work_clear)
for a in sorted(P['props'],key=lambda a: -((a['footprint'][2]-a['footprint'][0])*(a['footprint'][3]-a['footprint'][1])) if 'footprint' in a else 0):
 id=a['id']
 if id.startswith('allotment_') or id=='company_fence':continue
 if id.startswith('workshop_'):
  typ=a['type'];group='timber' if any(s in typ for s in ('timber','lumber','sawhorse')) else 'stone' if any(s in typ for s in ('stone','material','scrap')) else 'carts' if typ in ('cart','work_area') else 'crates'
  ok=pack(a,pile_regions[group]);a['pile_id']=group
  if not ok and group=='crates':
   group='carts';ok=pack(a,pile_regions[group]);a['pile_id']=group
  if not ok:print('PROP_FAIL',id,group,flush=True)
  next(p for p in P['workshop_piles'] if p['id']==group)['prop_ids'].append(id)
 elif id.startswith('quays_') or id=='cart_quay':
  if not (pack(a,[-111,32,-69,46]) or pack(a,[-68,15,-47,43])):print('PROP_FAIL',id,flush=True)
 elif a.get('cluster_location')=='red_tree_court' or id in ('market_stall','market_bench'):
  court=cs['red_tree_court']['court_polygon'];a['cluster_location']='red_tree_court'
  if not pack(a,bounds(court),court):print('PROP_FAIL',id,flush=True)
 elif id in ('equipment_bench','company_banner','gate_banner'):continue
 elif id.startswith('lamp_'):
  if not pack(a,[-7,0,7,117]):print('PROP_FAIL',id,flush=True)
 elif id=='cart_arrival':pack(a,[20,61,27,74])
 elif id=='clinic_planter':pack(a,[69,36,72,43])
 elif id=='food_planter':pack(a,[73,12,84,17])
 elif id=='old_park_bench':a['position']=[-94,-56]
 elif id=='view_bench':a['position']=[-111,-51]

for z in P['ground_zones']:
 if z['id']=='working_court':z['polygon']=g.boxpoly([-113,40,-66,98])
 if z['id']=='receiving_yard':z['polygon']=g.boxpoly([-113,-9,-45,47])
 z['blend_width_per_edge_m']=[0]*len(z['polygon'])
for pile in P['workshop_piles']:
 pile['polygon']=hull([v for a in P['props'] if a['id'] in pile['prop_ids'] for v in g.boxpoly(a['footprint'])])
# Hedge lies just outside the untouched reserve. East opening is a future gate.
rp=P['hq_reservation']['polygon'];x,z,X,Z=bounds(rp)
P['hq_screen']={'id':'hq_reserve_screen','kind':'hedge_and_timber_fence','height_m':1.3,'width_m':.5,
 'polylines':[[[X+.7,z+8],[X+.7,z-.7],[x-.7,z-.7],[x-.7,Z+.7],[X+.7,Z+.7],[X+.7,z+12]]],
 'opening':[[X+.7,z+8],[X+.7,z+12]],'reserve_remains_unbuilt':True}
P['green']['trees']=[red];P['green']['hedges']=[]
P['v7b_changes']={'candidate_only':True,'branch_groups':['guild_gate','arrival_courts','service','workshops_quays','north_bank'],
 'topology_note':'Six approved connection IDs remain; shared branches have multiple district attachments. The historic service_public_loop ID now denotes a dead-ended public arm.',
 'fixed_anchor_exceptions':['Gate arch and wall remain aligned','Clock tower and appointment staging remain fixed','Guild story positions remain fixed while building frontage angles five degrees'],
 'green_model':'Continuous grass ground between cluster envelopes, with separately modelled organic groves; courtyard earth/paving remains inside each group.'}
from landscape_v7b import build as landscape
landscape(P,V)
for d in P['districts']:
 bs=[b for b in P['buildings'] if b['district']==d['id']];d['label_position']=[sum((b['footprint'][i]+b['footprint'][i+2])/2 for b in bs)/len(bs) for i in (0,1)]
 pts=[v for r in P['routes'] if not r.get('owner') for v in r['centreline'] if g.inside(v,d['bounds'])]
 d['access_point']=min(pts,key=lambda pt:math.dist(pt,d['label_position']))
(R/'eurydica-plan-v7b.json').write_text(json.dumps(P,indent=2)+'\n',encoding='utf-8')
print('BUILD_V7B_WRITTEN',len(P['buildings']),len(P['routes']),flush=True)
