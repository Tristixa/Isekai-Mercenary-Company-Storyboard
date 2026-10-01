"""Four scoped revisions of the v7b candidate. All writes stay in this run."""
import sys,json,math,copy,random,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as g
from geometry_v7b import bounds,overlap,hull,nearest
R=Path(__file__).resolve().parent
V=json.loads((R/'eurydica-plan-v7b.json').read_bytes());P=copy.deepcopy(V)
manifest=R/'source-manifest-v7c.json'
if not manifest.exists():
 manifest.write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in R.iterdir() if f.is_file() and 'v7c' not in f.name},indent=2))
backup=R/'Eurydica Build Plan-before-v7c.md'
if not backup.exists():backup.write_bytes((R/'Eurydica Build Plan.md').read_bytes())
P.update(plan_revision='v7c',source_v7b_sha256=hashlib.sha256((R/'eurydica-plan-v7b.json').read_bytes()).hexdigest())
B={b['id']:b for b in P['buildings']};C={c['id']:c for c in P['clusters']}
oldroutes={r['id']:r for r in V['routes']}
def xmain(z):return 7*math.sin(4*math.pi*(118-z)/123)
def onmain(z):return [xmain(z),z]
P['routes']=[]
def route(id,pts,w=4,h=0,kind='street',group=None,owner=None,ys=None):
 pts=[list(q) for i,q in enumerate(pts) if not i or math.dist(q,pts[i-1])>1e-7]
 ys=ys or [h]*len(pts)
 r=dict(id=id,centreline=pts,width_m=w,heights_m=ys,grade=[(v-u)/math.dist(a,b) for u,v,a,b in zip(ys,ys[1:],pts,pts[1:])],surface='paved_main' if id=='main_road' else 'paved_local',kind=kind,phase=2 if h else 1,walkable=True)
 if group:r['branch_group']=group
 if owner:r['owner']=owner
 P['routes'].append(r);return r
def retained(id):
 r=copy.deepcopy(oldroutes[id]);P['routes'].append(r);return r
# Frontage groups move as rigid clusters, preserving every internal wall gap.
for cid,dx in [('lodging_row',2.5),('market_row',2.5)]:
 c=C[cid];c['v7c_shift']=[dx,0]
 for id in c['building_ids']:
  b=B[id];b['footprint']=[v+(dx if i%2==0 else 0) for i,v in enumerate(b['footprint'])];b['door_position'][0]+=dx
 for key in ('court_polygon','ground_envelope'):
  if key in c:c[key]=[[x+dx,z] for x,z in c[key]]
 for m in P['markers']:
  if m.get('place_binding') in c['building_ids'] or m.get('place_binding')==cid:m['position'][0]+=dx
retained('gate_arch')
zs=sorted(set(list(range(-5,119))+[j['position'][1] for j in P['junctions']]+[28,13,31]),reverse=True)
spine=[onmain(z) for z in zs];spine[0]=[0,118];spine[-1]=[0,-5]
route('main_road',spine,7)
# Five catchments. Shared streets replace duplicate returns; court paths remain narrow.
route('join5',[onmain(108),[-12,108],[-24,108]],4,group='guild_gate',ys=[0,0,.6])
route('join4',[onmain(108),[19,102],[27,100],[48,99],[68,99]],4,group='guild_gate')
route('gate_side',[[0,118],[-5,114],[-16,113]],2,kind='alley')
route('join1',[onmain(75),[-8,84],[-18,87],[-28,85]],4,group='arrival_courts')
route('join6_apron',[[-28,85],[-28,88],[-47,88],[-47,60],[-45,57]],4,group='arrival_courts')
route('join6',[[-45,57],[-62,62],[-68,65]],4,group='workshops_quays')
route('join3',[onmain(60),[21,58],[42,51],[67,48],[87.5,46],[89,35],[90,24],[90.5,18]],4,group='service')
# The northern quay approach duplicated the workshop access: link the two yards locally.
route('working_link',[[-68,65],[-70,59],[-71,45],[-71,34],[-68,34]],4,group='workshops_quays')
route('quay_court',[[-68,34],[-68,15],[-82,10],[-80,5]],2,kind='alley')
route('quay_loading',[[-68,34],[-80,38],[-99,38]],2,kind='alley')
for id in ('old_bridge','civic_approach','civic_old_ramp','civic_res_ramp','watch_stairs','view_deck','dock_ramp','dock_deck'):retained(id)
for id in ('old_city_walk','residential_walk','north_riverside'):
 retained(id)
# Replace the local old-city garden ring with a cross-bank loop behind the civic group.
route('north_loop',[[-54,-89],[-30,-90],[10,-90],[50,-86],[55,-85]],4,group='north_bank',ys=[4,4,2,4,4])
# No loop round the old-city cluster; watch deck remains reached by its frontage.
for id in ('arrival_court_lane','west_court_lane','market_homes_lane','red_tree_court_access','service_homes_lane','residential_a_lane','residential_b_lane','orchard_lane','guild_court_aisle','workshop_court'):
 r=retained(id)
 if id=='red_tree_court_access':r['centreline'][0]=onmain(31)
route('service_public_loop',[[87.5,46],[106,49],[106,77],[88,82]],4,group='service')
route('service_garden_access',[[106,77],[108,77]],2,kind='alley')
route('allotment_lane',[[106,49],[109,39]],2,kind='alley')
route('waterkeeper_lane',[[104,-88],[105,-95],[105,-103]],2,h=4,kind='alley')
route('civic_plaza_lane',[[0,-60],[-6,-63],[-6,-78],[-4,-80],[-4,-88]],2,h=2,kind='alley')

route('bridge_homes_court',[onmain(13),[22,13],[31,11],[31,0]],2,kind='alley')
# Legacy junction records are retained as landmarks on the main road. Superseded
# quay/arrival shortcuts are explicitly replaced by the current catchment paths.
for j in P['junctions']:j['position']=onmain(j['position'][1])
for c in P['approved_connections']:
 c['junction']=next(j['position'] for j in P['junctions'] if j['id']==c['id'])
 c['v7b_route_ids']=c['route_ids']
 if c['id']==2:c['route_ids']=['join6_apron','join6','working_link'];c['attachment_junction_id']=1;c['route_ids']=['join1','join6_apron','join6','working_link']
 elif c['id']==4:c['route_ids']=['join4'];c['attachment_junction_id']=5
 elif c['id']==6:c['route_ids']=['join1','join6_apron','join6'];c['attachment_junction_id']=1
 else:c['attachment_junction_id']=c['id']
# Irregular paved outline closely fits tower and civic frontages; appointment body
# circles retain the exact v7b positions and remain wholly on paving.
plaza=[[-8,-79],[-4,-80],[4,-79],[11.5,-76],[12,-71],[11.5,-68],[10,-66],[8,-62],[5,-59.8],[-4.5,-60],[-8,-62],[-8.7,-68],[-7.5,-72]]
next(s for s in P['squares'] if s['id']=='clock_plaza')['polygon']=plaza
civic_ground=next(z for z in P['ground_zones'] if z['id']=='civic_ground');civic_ground['polygon']=copy.deepcopy(plaza);civic_ground['blend_width_per_edge_m']=[.4]*len(plaza)
P['civic_planters']=[{'id':'civic_green_east','polygon':[[7.5,-74],[10.5,-74],[11.5,-71],[10.5,-68.5],[8.5,-69]],'height_m':2}]
# The south-east rectangular allotment/storeyard retains all object IDs and uses.
# Freestanding old fence panels become three grouped edge stacks; a low broken
# hedge supplies the new irregular outline. Two metres remain between bed groups.
yard=[[111.5,12],[130,10],[139,13],[141,23],[139.5,33],[143,40],[140,52],[129,54],[113,51],[110,44],[113,34],[110.5,23]]
space=next(s for s in P['green']['spaces'] if s['id']=='spine_service_allotments');space['polygons']=[yard]
zone=next(s for s in P['ground_zones'] if s['id']=='spine_service_allotments');zone['polygon']=yard
for l in P['green']['lawns']:
 if l['id'].startswith('spine_service_allotments'):l['polygon']=yard
props={a['id']:a for a in P['props']}
# Reuse each old fence as stacked 3m panels beside the tool shed. Its original
# run length is conserved in the inventory; the smaller stack footprint is real.
for i,a in enumerate(a for a in P['props'] if a['type']=='low_fence' and a['id'].startswith('allotment_')):
 f=a['footprint'];length=max(f[2]-f[0],f[3]-f[1]);a['original_footprint_v7b']=f
 a['stored_panels']={'total_length_m':length,'panel_count':math.ceil(length/3),'maximum_panel_length_m':3}
 a['footprint']=[127,31+i*.65,130,31.4+i*.65];a['v7c_group']='tool_and_panel_stock'
# Bed groups step with the irregular edge, retaining bed dimensions and use.
for id,dx,dz in [('allotment_bed_2',-1,1),('allotment_bed_3',0,3),('allotment_bed_4',1,1),('allotment_bed_6',-1,1),('allotment_bed_8',1,1),('allotment_bed_9',0,1)]:
 a=props[id];a['footprint']=[v+(dx if i%2==0 else dz) for i,v in enumerate(a['footprint'])]
P['storeyard_piles']=[{'id':'north_produce','prop_ids':['allotment_bed_1','allotment_bed_2','allotment_bed_3','allotment_bed_4']},{'id':'south_produce','prop_ids':['allotment_bed_5','allotment_bed_7','allotment_bed_8','allotment_bed_9','allotment_bed_10']},{'id':'tool_and_panel_stock','prop_ids':[a['id'] for a in P['props'] if a.get('stored_panels')]+['allotment_tools','allotment_water_butt','allotment_compost']},{'id':'east_produce','prop_ids':['allotment_bed_6']}]
props['allotment_gate']['footprint']=[110.5,35,110.8,37.4];props['allotment_gate']['opening_position']=[111,39];props['allotment_gate'].pop('zone_id',None)
P['storeyard_edge']={'polygon':yard,'width_m':.5,'height_m':1.1,'hedge_polylines':[[[111.5,12],[130,10],[139,13],[141,23],[139.5,33]],[[143,40],[140,52],[129,54]],[[113,51],[110,44]],[[113,34],[110.5,23],[111.5,12]]], 'opening':[[111,37.5],[111,40.5]],'identity_note':'Legacy spine_service_allotments: existing produce beds, tools, fruit trees and fence panels retained.'}
# Avoid the old panel-sized rectangles in the review: panels are preserved physical
# pieces lying in edge stock, while hedge geometry is a separate placement layer.
# Retain lamps at their existing individually packed positions; shift only if
# the new road consumes their position (packing below checks all solids).

S=[(b['id'],[g.rotate(v,b) for v in g.boxpoly(f)]) for b in P['buildings'] for f in b.get('collision_rectangles',[b['footprint']])]
blocked=[s for _,s in S]+[P['river']['polygon'],P['waterworks']['feeder_polygon'],P['hq_reservation']['polygon']]
from check_plan_v7b import gap
roads=[g.strip(a,b,r['width_m']) for r,i,a,b in g.segments(P)]
occupied=[]
for prop in P['props']:
 if 'footprint' in prop:poly=g.boxpoly(prop['footprint'])
 elif 'position' in prop:
  x,z=prop['position'];rad=prop.get('collision_radius_m',.15);poly=g.boxpoly([x-rad,z-rad,x+rad,z+rad])
 else:continue
 if any(overlap(poly,rd) for rd in roads) or any(overlap(poly,solid) for _,solid in S):
  f=bounds(poly);w,d=f[2]-f[0],f[3]-f[1];options=[]
  for dx in range(-30,31):
   for dz in range(-30,31):options.append((dx*dx+dz*dz,dx*.5,dz*.5))
  for _,dx,dz in sorted(options):
   q=g.boxpoly([f[0]+dx,f[1]+dz,f[2]+dx,f[3]+dz])
   if not all(g.inside(v,P['extent']) for v in q):continue
   other=[g.boxpoly(a['footprint']) for a in P['props'] if a['id']!=prop['id'] and 'footprint' in a]
   if any(overlap(q,s) for s in blocked+roads+other+occupied):continue
   if prop['id'].startswith('workshop_') and min(gap(q,g.footprint(B[id])) for id in C['workshop_yard']['building_ids'])>3.5:continue
   if prop.get('zone_id') and not all(g.inside(v,next(z['polygon'] for z in P['ground_zones'] if z['id']==prop['zone_id'])) for v in q):continue
   if 'footprint' in prop:prop['footprint']=[f[0]+dx,f[1]+dz,f[2]+dx,f[3]+dz]
   else:prop['position']=[prop['position'][0]+dx,prop['position'][1]+dz]
   poly=q;break
  else:print('PROP_REPACK_FAIL',prop['id'])
 occupied.append(poly)
for pile in P['workshop_piles']:pile['polygon']=hull([v for a in P['props'] if a['id'] in pile['prop_ids'] for v in g.boxpoly(a['footprint'])])
prop_polys=[g.boxpoly(a['footprint']) if 'footprint' in a else g.boxpoly([a['position'][0]-a.get('collision_radius_m',.15),a['position'][1]-a.get('collision_radius_m',.15),a['position'][0]+a.get('collision_radius_m',.15),a['position'][1]+a.get('collision_radius_m',.15)]) for a in P['props'] if 'footprint' in a or 'position' in a]
blocked_bounds=[(s,bounds(s)) for s in blocked+prop_polys]
def clearline(a,b,w=2):
 if math.dist(a,b)<1e-8:return False
 poly=g.strip(a,b,w);x,z,X,Z=bounds(poly)
 return not any(overlap(poly,s) for s,(u,v,U,V) in blocked_bounds if min(X,U)>max(x,u)+1e-7 and min(Z,V)>max(z,v)+1e-7)
for r,i,a,b in g.segments(P):
 for id,s in S:
  if overlap(g.strip(a,b,r['width_m']),s):print('BACKBONE_COLLISION',r['id'],id,flush=True)
 if abs(r['grade'][i])>.05001 and r['kind']!='stairs':print('SLOPE',r['id'],r['grade'][i])

# Reuse v7b's exact-face door search, minimise actual length and share approaches.
# A long frontage connector is an explicit in-cluster alley; final door spurs <=12m.
for b in P['buildings']:
 if b['id']=='south_gate':continue
 x,z,X,Z=b['footprint'];original=b['door_face'];choices=[]
 segs=list(g.segments(P))
 for face,fraction in [(f,t) for f in [original]+[f for f in ('s','n','e','w') if f!=original] for t in (.5,.25,.75,.125,.875,.0625,.9375)]:
  local={'s':[x+(X-x)*fraction,Z],'n':[x+(X-x)*fraction,z],'e':[X,z+(Z-z)*fraction],'w':[x,z+(Z-z)*fraction]}[face]
  normal={'s':[0,1],'n':[0,-1],'e':[1,0],'w':[-1,0]}[face]
  door=g.rotate(local,b);out=g.rotate([local[i]+normal[i]*1.1 for i in (0,1)],b)
  for r,i,a,c in segs:
   if r['kind'] in ('stairs','dock','gate_passage'):continue
   q,t=nearest(out,a,c);h=r['heights_m'][i]+t*(r['heights_m'][i+1]-r['heights_m'][i])
   if abs(h-b['ground_y_m'])>.001 or math.dist(q,door)>25:continue
   for mid in ([],[[out[0],q[1]]],[[q[0],out[1]]]):
    pts=[q]+mid+[out,door];pts=[p for i,p in enumerate(pts) if not i or math.dist(p,pts[i-1])>.001]
    ln=sum(math.dist(a,c) for a,c in zip(pts,pts[1:]))
    if ln>25 or choices and ln>=choices[0][0]:continue
    if all(clearline(a,c) for a,c in zip(pts,pts[1:])):
     choices=[(ln,pts,face,door)]
 if not choices:print('NO_DOOR',b['id'],flush=True);continue
 ln,pts,face,door=choices[0];b['door_face']=face;b['door_position']=door;b['door_route']='door_'+b['id']
 if ln>12:
  route('court_link_'+b['id'],pts[:-1],2,h=b['ground_y_m'],kind='alley')['cluster_id']=b['cluster_id'];pts=pts[-2:]
 route(b['door_route'],pts,2,h=b['ground_y_m'],kind='door_approach',owner=b['id'])
for n in P['npc_spots']:
 m=next(m for m in P['markers'] if m['id']==n['marker_id']);n['position']=m['position']
for portal in P['portals']:
 if 'city_building' in portal:portal['city_position']=B[portal['city_building']]['door_position']
for d in P['districts']:
 pts=d['bounds']+[v for b in P['buildings'] if b['district']==d['id'] for v in g.footprint(b)]
 x,z,X,Z=bounds(pts);d['bounds']=g.boxpoly([x-.01,z-.01,X+.01,Z+.01])
P['walk_time'].update(start=[0,118],finish=onmain(28))
P['arrival_route']['waypoints']=[[0,132],[0,122]]+[onmain(z) for z in (108,75,28)]+[[0,-5]]
for r in P['routes']:r['grade']=[(v-u)/math.dist(a,b) for u,v,a,b in zip(r['heights_m'],r['heights_m'][1:],r['centreline'],r['centreline'][1:])]
if '--layout-only' in sys.argv:
 (R/'layout-draft-v7c.json').write_text(json.dumps(P,indent=2));print('LAYOUT_WRITTEN');sys.exit()
from simplify_v7c import prune
prune(P)
from landscape_v7c import build
build(P,V)
P['v7c_changes']={'candidate_only':True,'reference':'f03 illustrated.jpg','main_road_amplitude_m':7,'main_road_cycles':2,'branch_groups':['guild_gate','arrival_courts','service','workshops_quays','north_bank'],'superseded_checks':['Six historic street attachments replaced by five functional catchments; retained junction IDs are remapped explicitly.','Clock plaza polygon lock replaced by unchanged appointment positions, paving coverage and clearances.','Rigid rectangular allotment layout replaced by object identity/size preservation, pile grouping and body-clear access to all contents.','Old garden-ring IDs replaced by one north-bank circuit.']}
(R/'eurydica-plan-v7c.json').write_text(json.dumps(P,indent=2)+'\n',encoding='utf-8')
print('BUILD_V7C_WRITTEN',len(P['routes']),flush=True)
