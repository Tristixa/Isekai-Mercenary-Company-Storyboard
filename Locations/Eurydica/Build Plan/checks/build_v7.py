"""Deterministic layout authoring. Only writes beside this file; source is read-only."""
import sys,json,copy,math,hashlib,heapq,random
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as g
_sat=g.area_overlap
def fast_overlap(a,b):
 if max(v[0] for v in a)<=min(v[0] for v in b)+1e-6 or max(v[0] for v in b)<=min(v[0] for v in a)+1e-6 or max(v[1] for v in a)<=min(v[1] for v in b)+1e-6 or max(v[1] for v in b)<=min(v[1] for v in a)+1e-6:return False
 return _sat(a,b)
g.area_overlap=fast_overlap
R=Path(__file__).resolve().parent
SOURCE=Path('D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/Archive/Build Plan v5')
OLD=json.loads((SOURCE/'eurydica-plan.json').read_bytes())
P=copy.deepcopy(OLD); B={b['id']:b for b in P['buildings']}; OB={b['id']:b for b in OLD['buildings']}
P.update(status='candidate',plan_revision='v7',source_v5_sha256=hashlib.sha256((SOURCE/'eurydica-plan.json').read_bytes()).hexdigest())
P['clusters']=[]
def box(a):return g.boxpoly(a)
def move_poly(poly,dx,dz):return [[round(x+dx,6),round(z+dz,6)] for x,z in poly]
def place(id,x,z,face='s',district=None):
 b=B[id];f=b['footprint'];w,d=f[2]-f[0],f[3]-f[1]
 b.update(footprint=[x,z,x+w,z+d],yaw_deg=0,door_face=face,spacing_exempt_reason='landmark' if id in ('south_gate','watch_tower') else '')
 if district:b['district']=district
 b['ground_y_m']=2 if b['district']=='civic' else 4 if b['district'] in ('old_city','residential','waterworks') else .6 if id in ('company_house','stables','store_shed') else 0
 b['door_position']={'s':[x+w/2,z+d],'n':[x+w/2,z],'e':[x+w,z+d/2],'w':[x,z+d/2]}[face]
 b.pop('party_wall_group',None)
 return b
def cluster(id,dist,name,purpose,placements,court=None,phase=1):
 ids=[]
 for bid,x,z,face in placements:
  b=place(bid,x,z,face,dist);b.update(cluster_id=id,phase=phase);ids.append(bid)
 c=dict(id=id,district=dist,name=name,purpose=purpose,building_ids=ids,phase=phase)
 if court:c['court_polygon']=box(court)
 P['clusters'].append(c)
def add_house(id,template='arrival_home_1'):
 b=copy.deepcopy(OB[template]);b.update(id=id,display_name=id.replace('_',' ').title(),role='House',asset_status='exists',source_concept='Approved facade reuse for v7 cluster completion')
 P['buildings'].append(b);B[id]=b

# Gate inner face 120.8; south river edge -10: 130.8 m. Gate proportions unchanged.
cluster('gate_cluster','company','Gate cluster','Guarded entry; houses hug both sides of the inner wall',[
 ('south_gate',-6.2,120.8,'s'),('guard_shelter',-10.7,119.7,'n'),('street_home_1',7,115.2,'n'),('infill_home_11',-17.7,117.2,'n')])
B['south_gate']['collision_rectangles']=[[-6.2,120.8,-2.3,123.2],[2.3,120.8,6.2,123.2]]
B['south_gate']['walk_through_opening']=box([-2.3,120.8,2.3,123.2])
cluster('guild_compound','company','Guild compound','Guild yard, processing corner and stables; expansion parcels immediately west',[
 ('company_house',-33.75,99.25,'e'),('store_shed',-38.25,99.25,'s'),('stables',-49.75,99.25,'s')],[-50,105.5,-22,118])
cluster('lodging_row','arrival','Lodging row','Continuous east frontage for arriving travellers',[
 ('lodging',8,63,'w'),('street_home_0',8,72,'w'),('street_home_2',8,81,'w'),('infill_home_22',8,90,'w')])
cluster('arrival_court','arrival','Arrival court','Six homes enclose a small shared court off a short lane',[
 ('arrival_home_1',30,70,'s'),('arrival_home_2',39,70,'s'),('infill_home_03',48,70,'s'),
 ('arrival_home_3',30,77,'e'),('infill_home_18',48,78,'w'),('street_home_3',30,86,'e')],[39.5,77,47.5,96])
cluster('red_tree_court','market','Red-tree court','Tavern and three food shops ring an open-earth red tree plaza on three sides',[
 ('tavern',-39,23,'e'),('infill_home_12',-29,14,'s'),('street_home_8',-23,14,'s'),('provisions',-29,35,'n')],[-30,23,-10,35])
cluster('market_row','market','Market row','Continuous main-road shopfront opposite the tree court',[
 ('repair_supply',8,20,'w'),('infill_home_06',8,33,'w'),('infill_home_23',8,40,'w'),('market_home_violet',8,48,'w')])
cluster('market_homes','market','Market homes','Six homes around a compact rear court',[
 ('market_home_0',31,13,'s'),('market_home_1',41,13,'s'),('market_home_east',51,13,'s'),
 ('infill_home_04',31,22,'e'),('infill_home_05',48,22,'w'),('infill_home_08',31,31,'e')],[38,22,48,39])
cluster('service_lane','service','Service lane','Clinic and food shop face two warm-roof homes across one paved lane',[
 ('food_shop',75,20,'e'),('clinic',73,30,'e'),('service_home_0',90,20,'w'),('service_home_3',90,29,'w')])
cluster('service_homes','service','Service homes','Five warm-roof households beside the shared allotments',[
 ('service_home_1',76,60,'s'),('service_home_2',85,60,'s'),('infill_home_01',94,60,'s'),
 ('infill_home_02',76,69,'e'),('infill_home_07',94,69,'w')],[82,69,94,82])
# Retained surplus v5 houses are grouped, not discarded or hidden in the scheduled clusters.
cluster('arrival_west_court','arrival','West arrival court','Retained Arrival Ward homes around an earth court',[
 ('company_neighbor',-40,61,'s'),('infill_home_09',-31,61,'s'),('infill_home_10',-24,61,'s'),
 ('street_home_4',-40,68,'e'),('infill_home_15',-24,71,'w'),('street_home_5',-40,77,'e')],[-30,71,-24,87])
cluster('guild_neighbours','company','Guild neighbours','Five retained homes on an inner-wall lane',[
 ('street_home_6',28,106,'n'),('street_home_7',38,106,'n'),('infill_home_16',48,106,'n'),
 ('infill_home_29',55,106,'n'),('infill_home_30',62,106,'n')])
cluster('arrival_garden_court','arrival','Orchard court','Remaining Arrival Ward homes face a small court beside the orchard',[
 ('infill_home_20',-67,36,'s'),('infill_home_21',-54,36,'s'),('infill_home_25',-67,46,'e'),('infill_home_26',-54,43,'w')],[-54,50,-47,58])
add_house('service_added_home','arrival_home_1')
cluster('service_garden_row','service','Garden service row','Two retained homes and one approved-facade addition beside public gardens',[
 ('infill_home_13',111,62,'w'),('infill_home_24',111,70,'w'),('service_added_home',111,79,'w')])
cluster('market_riverside','market','Bridge-side homes','Four homes mark the approach to the Old Bridge',[
 ('infill_home_28',9,-4,'s'),('infill_home_27',9,4,'w')],None,phase=1)
add_house('bridge_home_01','arrival_home_1');add_house('bridge_home_02','arrival_home_1')
for id,x,z in [('bridge_home_01',20,-4),('bridge_home_02',20,3)]:
 place(id,x,z,'s','market');B[id].update(cluster_id='market_riverside',phase=1);P['clusters'][-1]['building_ids'].append(id)
cluster('workshop_yard','workshops','Workshop yard','Three workshops touch the edges of a working court',[
 ('tool_repair',-110,59,'e'),('timber_containers',-91,48,'s'),('material_sorting',-91,72,'n')],[-92,59,-68,72],2)
cluster('quay_row','quays','Quay row','Storehouses and loading shelter form a river-edge frontage',[
 ('bulk_storehouse',-109,-4,'e'),('quay_storehouse',-109,15,'e'),('loading_shelter',-90,15,'s')],[-90,28,-68,45],2)
cluster('civic_plaza','civic','Civic plaza','Clock landmark, toll, guard and notice shelter around the unchanged appointment plaza',[
 ('watch_tower',-3,-73,'s'),('toll_records',-17,-80,'w'),('civic_guard',-17,-71,'w'),('notice_shelter',-10,-84,'n')],None,2)
cluster('old_city_row','old_city','Old City row','Inn and old timber homes share a continuous south-facing street',[
 ('old_home_0',-105,-109,'s'),('old_home_1',-97,-109,'s'),('old_home_2',-88,-109,'s'),('old_hall',-79,-109,'s')],[-106,-100,-61,-89],2)
cluster('residential_a','residential','Residential A','Western courtyard households',[
 ('res_home_0',33,-110,'s'),('res_home_3',42,-110,'s'),('infill_home_19',33,-101,'e')],[40,-101,51,-87],2)
cluster('residential_b','residential','Residential B','Eastern courtyard households',[
 ('res_home_1',64,-111,'s'),('res_home_2',73,-111,'s'),('infill_home_14',64,-102,'e'),('infill_home_17',76,-102,'w')],[71,-102,76,-86],2)
cluster('waterworks_group','waterworks','Waterworks group','Keeper, washing shelter and cistern beside the fixed feeder',[
 ('cistern',89,-109,'s'),('waterkeeper',95,-109,'w'),('washing',94,-101,'s')],None,2)

# Preserve roofs on all retained buildings, even when a historic cross-district home is regrouped.
for b in P['buildings']:
 if b['id'] in OB:b['roof_palette']=OB[b['id']]['roof_palette']
 else:b['roof_palette']='warm_red' if b['district']=='service' else 'plum'
assert all(b.get('cluster_id') in {c['id'] for c in P['clusters']} for b in P['buildings'])

# District topology is retained; south envelopes are redrawn to contain new cluster groupings.
for bid in ('infill_home_28','infill_home_27','bridge_home_01','bridge_home_02'):
 b=B[bid];place(bid,b['footprint'][0],b['footprint'][1]-4,b['door_face'])
district_boxes={'company':[-78,98,78,125],'arrival':[-67,30,66,101],'market':[-43,-10,66,60],'workshops':[-113,47,-67,98],'quays':[-113,-10,-43,47],'service':[67,15,127,101]}
for d in P['districts']:
 if d['id'] in district_boxes:d['bounds']=box(district_boxes[d['id']])
P['extent']=box([-114,-135,132,127]);P['south_bank_boundary']=box([-113,-10,130,124])
P['city_wall']['segments']=[[[-113,-10],[-113,124],[-6.2,124]],[[6.2,124],[130,124],[130,-10]]]
P['phase_1']['polygon']=[[-67,30],[-43,30],[-43,-10],[129,-10],[129,125],[-67,125]]
P['phase_1']['includes']=['South Gate','Guild Edge','Arrival Ward','Market Spine','Service Lanes']
# The Guild court and its narrative geometry translate rigidly by -175 m in z.
P['hq_reservation']['polygon']=move_poly(OLD['hq_reservation']['polygon'],-15,-141)
for a,o in zip(P['hq_reservation']['upgrades'],OLD['hq_reservation']['upgrades']):a['polygon']=move_poly(o['polygon'],-15,-141)
guild_platform=box([-78,98,-18,123])
P['terrain']['terraces']=[t for t in P['terrain']['terraces'] if t['id'] not in ('south','company_platform')]+[
 dict(id='south',polygon=P['south_bank_boundary'],height_m=0,priority=1),dict(id='company_platform',polygon=guild_platform,height_m=.6,priority=2)]
P['terrain']['retaining_walls']=[w for w in P['terrain']['retaining_walls'] if not w['id'].startswith('company_')]
P['terrain']['ramps']=[r for r in P['terrain']['ramps'] if not r['id'].startswith('join5')]

P['routes']=[]
def route(id,pts,width=4,phase=1,ys=None,surface='paved_local',kind='street',owner=None):
 ys=ys or [0]*len(pts)
 r=dict(id=id,centreline=pts,width_m=width,surface=surface,heights_m=ys,grade=[(b-a)/math.dist(p,q) for a,b,p,q in zip(ys,ys[1:],pts,pts[1:])],phase=phase,kind=kind,walkable=True)
 if owner:r['owner']=owner
 P['routes'].append(r);return r
route('gate_arch',[[0,126],[0,118]],4.6,kind='gate_passage')
spine=[[0,118],[0,108],[-.4,104],[-1,98],[1,87],[0,75],[-7/15,68],[-1,60],[0,50],[-1,40],[0,28],[1,15],[0,5],[0,-5]]
route('main_road',spine,7,surface='paved_main')
route('join1',[[0,75],[-7,75],[-7,89],[-68,89],[-68,65]],4.5,surface='earth')
route('join2_apron',[[1,15],[-7,15],[-7,8],[-45,8]],4.5)
route('join2_earth',[[-45,8],[-45,10],[-85,10]],4.5,2,surface='earth')
route('join3',[[-1,60],[23,60],[65,50],[87.5,50],[87.5,18]],4.5)
route('join4',[[-.4,104],[21,104],[23,99],[68,99]],4.5)
route('service_public_loop',[[68,99],[105,99],[105,50],[65,50]],4.5)
route('join5',[[0,108],[-12,108],[-24,108]],5,ys=[0,0,.6])
P['terrain']['ramps'].append(dict(id='join5_segment_1',route_id='join5',polyline=[[-12,108],[-24,108]],width_m=5,length_m=12,rise_m=.6,grade=.05))
route('join6_apron',[[-7/15,68],[-7,68],[-7,55],[-45,55]],4.5)
route('join6',[[-45,55],[-45,58],[-68,58],[-68,65]],4.5,2,surface='earth')
for n,pos in {1:[0,75],2:[1,15],3:[-1,60],4:[-.4,104],5:[0,108],6:[-7/15,68]}.items():
 next(j for j in P['junctions'] if j['id']==n)['position']=pos
 next(j for j in P['approved_connections'] if j['id']==n)['junction']=pos
fixed=['old_bridge','civic_approach','civic_old_ramp','civic_res_ramp','watch_stairs','view_deck','dock_ramp','dock_deck']
for r in OLD['routes']:
 if r['id'] in fixed:P['routes'].append(copy.deepcopy(r))
route('dock_access',[[-80,10],[-80,5]],4,2,surface='earth')
route('old_city_walk',[[-40,-60],[-55,-60],[-55,-89],[-102,-89],[-102,-70]],4,2,[4]*5)
route('old_park',[[-55,-60],[-55,-49],[-102,-49],[-102,-70]],4,2,[4]*4)
route('residential_walk',[[40,-60],[55,-60],[55,-88],[40,-88]],4,2,[4]*4)
route('north_riverside',[[55,-60],[100,-60],[100,-52],[122,-52]],5,2,[4]*4)
route('waterworks_walk',[[100,-52],[104,-52],[104,-87],[72,-87]],3,2,[4]*4)
route('residential_link',[[55,-88],[55,-81],[72,-81],[72,-87]],3,2,[4]*4)
route('arrival_court_lane',[[43,99],[43,80]],2.5)
route('west_court_lane',[[-28,89],[-28,75]],2.5)
route('market_homes_lane',[[65,50],[65,43],[44,43],[44,25]],2.5)
route('service_homes_lane',[[88,99],[88,73]],2.5)
route('residential_a_lane',[[45,-88],[45,-99]],2.5,2,[4,4])
route('residential_b_lane',[[72,-87],[72,-99]],2.5,2,[4,4])
route('orchard_lane',[[-68,65],[-69,65],[-69,34]],4)
route('waterkeeper_lane',[[104,-87],[105,-93],[105,-113],[91,-113]],2,2,[4]*4)
route('civic_plaza_lane',[[0,-60],[7,-64],[7,-78],[-4,-78],[-4,-87],[-20,-87],[-20,-75]],2.5,2,[2]*7)

# Court surfaces: building-owned forecourts are earth/paving, never isolated lawn pads.
P['ground_zones']=[]
def zone(id,poly,material='earth',height=0,priority=2,**kw):
 z=dict(id=id,polygon=poly,material=material,height_m=height,walkable=True,blend_width_per_edge_m=[0]*len(poly),priority=priority,**kw);P['ground_zones'].append(z);return z
zone('south_base',P['south_bank_boundary'])
zone('north_base',box([-113,-120,130,-40]),'dressed_stone',4)
zone('civic_ground',box([-30,-100,30,-40]),'dressed_stone',2,3)
zone('courtyard_staging',move_poly(next(z['polygon'] for z in OLD['ground_zones'] if z['id']=='courtyard_staging'),0,-175),'earth',.6,4)
zone('guild_platform',guild_platform,'earth',.6,3)
for c in P['clusters']:
 if 'court_polygon' in c:zone(c['id']+'_surface',c['court_polygon'],'paving' if c['district'] not in ('workshops','quays','company') else 'earth',4 if c['phase']==2 and c['district'] not in ('workshops','quays') else .6 if c['id']=='guild_compound' else 0)
P['squares']=[copy.deepcopy(s) for s in OLD['squares'] if s['id'] in ('clock_plaza','bridge_south_landing','bridge_north_landing')]
P['squares'] += [dict(id='red_tree_court',polygon=box([-30,23,-10,35]),purpose='Three-sided court; stalls and open ground tree bed'),dict(id='gate_square',polygon=box([-7,111,7,118]),purpose='Gate orientation')]
zone('red_tree_bed',box([-21.5,26,-16.5,31]),'grass_earth',priority=8,purpose='Unpaved open grass-and-earth bed; no paving or raised planter',named_green_space=True)
red=copy.deepcopy(next(t for t in OLD['green']['trees'] if t['id']=='tree_08'));red['position']=[-19,28.5]
P['green']['trees']=[red];P['green']['spaces']=[]
next(l for l in P['landmarks'] if l['id']=='red_tree')['position']=red['position']

# Door approaches: retain geometry and graph routines from v5; make connected obstacle-free access.
def solids():return [(b['id'],[g.rotate(v,b) for v in box(f)]) for b in P['buildings'] for f in b.get('collision_rectangles',[b['footprint']])]
S=solids()
def clearline(a,b,w=2,ignore=None):
 if math.dist(a,b)<1e-8:return False
 poly=g.strip(a,b,w)
 return not any(id!=ignore and g.area_overlap(poly,s) for id,s in S) and not g.area_overlap(poly,P['river']['polygon']) and not g.area_overlap(poly,P['waterworks']['feeder_polygon']) and not g.area_overlap(poly,P['hq_reservation']['polygon'])
def nearest(pt,a,b):
 dx,dz=b[0]-a[0],b[1]-a[1];t=max(0,min(1,((pt[0]-a[0])*dx+(pt[1]-a[1])*dz)/(dx*dx+dz*dz)))
 return [round(a[0]+t*dx,6),round(a[1]+t*dz,6)],t
for b in P['buildings']:
 if b['id']=='south_gate':continue
 x0,z0,x1,z1=b['footprint'];original_face=b['door_face']
 choices=[]
 for face in [original_face]+[f for f in ('s','n','e','w') if f!=original_face]:
  door={'s':[(x0+x1)/2,z1],'n':[(x0+x1)/2,z0],'e':[x1,(z0+z1)/2],'w':[x0,(z0+z1)/2]}[face]
  normal={'n':[0,-1],'s':[0,1],'w':[-1,0],'e':[1,0]}[face];out=[door[0]+normal[0]*1.6,door[1]+normal[1]*1.6]
  for r,i,a,c in g.segments(P):
   if r.get('owner') or r['kind'] in ('stairs','dock','gate_passage'):continue
   q,t=nearest(out,a,c);h=r['heights_m'][i]+t*(r['heights_m'][i+1]-r['heights_m'][i])
  # Any elevation transition is explicitly graded, not snapped onto a raised terrace.
   if abs(h-b['ground_y_m'])>.001:continue
   for mid in ([],[[out[0],q[1]]],[[q[0],out[1]]]):
    pts=[q]+mid+[out,door];pts=[p for i,p in enumerate(pts) if not i or math.dist(p,pts[i-1])>.001]
    if all(clearline(a,c,2, b['id'] if c==door else None) for a,c in zip(pts,pts[1:])):
    # Final strip may touch the owning wall but may never penetrate it.
     if g.area_overlap(g.strip(pts[-2],door,2),next(s for id,s in S if id==b['id'])):continue
     choices.append((sum(math.dist(a,c) for a,c in zip(pts,pts[1:]))+(0 if face==original_face else 3),pts,h,face,door))
 if not choices:
  print('NO DOOR ROUTE',b['id'],door);continue
 _,pts,h,face,door=min(choices,key=lambda a:a[0]);b['door_face']=face;b['door_position']=door;ys=[h]+[b['ground_y_m']]*(len(pts)-1)
 # Spread height smoothly over entire approach.
 lens=[0]
 for a,c in zip(pts,pts[1:]):lens.append(lens[-1]+math.dist(a,c))
 ys=[h+(b['ground_y_m']-h)*d/lens[-1] for d in lens]
 b['door_route']='door_'+b['id'];route(b['door_route'],pts,2,b['phase'],ys,kind='door_approach',owner=b['id'])

# Story markers stay bound to their named place; civic appointment markers are byte-identical.
anchor={'city/scene4_line_251':'clinic','city/scene4_line_329':'food_shop','city/scene4_line_457':'food_shop','city/scene4_line_384':'repair_supply','city/scene4_line_483':'repair_supply','city/scene4_line_280':'stables','city/scene4_line_495':'stables'}
for m in P['markers']:
 if m['scene']!='city' or m['id'].startswith('civic_terrace/'):continue
 id=m['id'];old=next(a for a in OLD['markers'] if a['id']==id)
 if id in anchor:
  b=B[anchor[id]];o=OB[b['id']];dx=old['position'][0]-o['door_position'][0];dz=old['position'][1]-o['door_position'][1]
  face=b['door_face'];normal={'n':[0,-1],'s':[0,1],'w':[-1,0],'e':[1,0]}[face]
  m['position']=[b['door_position'][0]+normal[0]*2,b['door_position'][1]+normal[1]*2]
  if id.endswith(('457','483','495')):m['position'][1 if face in ('w','e') else 0]+=2
  m['height_m']=b['ground_y_m'];m['place_binding']=b['id']
 elif id.startswith('guild_courtyard/') or (old['height_m']==.6):
  m['position']=move_poly([old['position']],0,-175)[0]
  if 'footprint' in m:m['footprint']=[m['footprint'][0],m['footprint'][1]-175,m['footprint'][2],m['footprint'][3]-175]
  m['place_binding']='guild_compound'
 elif old['position'][1]>290:m['position']=[old['position'][0],old['position'][1]-178];m['place_binding']='south_gate'
 elif id=='city/scene4_line_219':m['position']=[-26,28];m['place_binding']='red_tree_court'
 elif id=='city/scene4_line_439':m['position']=[-12,29];m['place_binding']='red_tree_court'
 elif id=='city/scene4_line_478':m['position']=[45,-90];m['place_binding']='residential_a'
for n in P['npc_spots']:
 m=next(m for m in P['markers'] if m['id']==n['marker_id']);n['position']=m['position'];n['height_m']=m['height_m']
for portal in P['portals']:
 if 'city_building' in portal:portal['city_position']=B[portal['city_building']]['door_position']
P['arrival_route']['waypoints']=[[0,132],[0,122],[0,108],[0,75],[0,28],[0,-5]]
P['walk_time'].update(start=[0,118],finish=[0,28],speed_m_s=3.2,note='Retained v5 speed; report route length and optional 2 m/s strolling comparison without changing runtime.')

# Props keep all IDs, types, stock and awning dimensions. Place deliberately in their owning courts.
P['props']=copy.deepcopy(OLD['props'])
route_polys=[g.strip(a,b,r['width_m']) for r,i,a,b in g.segments(P)]
occupied=[]
def prop_ok(poly):
 return not any(g.area_overlap(poly,s) for _,s in S) and not any(g.area_overlap(poly,s) for s in route_polys+occupied) and not g.area_overlap(poly,P['hq_reservation']['polygon']) and not g.area_overlap(poly,box([-21.5,26,-16.5,31])) and all(not g.inside(m['position'],poly) and min(g.distance(m['position'],a,b) for a,b in g.edges(poly))>.8 for m in P['markers'] if m['scene']=='city')
def pack(a,region):
 f=a.get('footprint');w,d=(f[2]-f[0],f[3]-f[1]) if f else (a.get('collision_radius_m',.25)*2,)*2
 x0,z0,x1,z1=region
 for z in [z0+i*.5 for i in range(int((z1-z0-d)*2)+1)]:
  for x in [x0+i*.5 for i in range(int((x1-x0-w)*2)+1)]:
   poly=box([x,z,x+w,z+d])
   if prop_ok(poly):
    if f:a['footprint']=[x,z,x+w,z+d]
    else:a['position']=[x+w/2,z+d/2]
    occupied.append(box([x-.3,z-.3,x+w+.3,z+d+.3]));return True
 return False
zone('working_court',box([-112,33,-67,98]))
zone('receiving_yard',box([-111,-5,-46,47]))
# Allotments retain their complete internal layout and tending aisle widths, rigidly translated.
allot=copy.deepcopy(next(z for z in OLD['ground_zones'] if z['id']=='spine_service_allotments'))
allot['polygon']=move_poly(allot['polygon'],48,-58);allot['gate_position']=[107,43];P['ground_zones'].append(allot)
# This initial allotment placement is revised below if it conflicts with the service lane.
for a in P['props']:
 id=a['id']
 if id.startswith('allotment_'):
  f=a['footprint'];a['footprint']=[f[0]+48,f[1]-58,f[2]+48,f[3]-58]
  continue
 if id.startswith('workshop_'):assert pack(a,[-112,48,-68,97]),id
 elif id.startswith('quays_') or id=='cart_quay':
  assert pack(a,[-110,34,-69,46]) or pack(a,[-69,15,-47,30]),id
 elif id.startswith(('market_court_','market_edge_','market_south_')) or id in ('market_stall','market_bench'):
  a['cluster_location']='red_tree_court';pack(a,[-29.5,23.5,-10.5,34.5])
 elif id=='company_fence':a['polyline']=move_poly(a['polyline'],-15,-141)
 elif id=='equipment_bench':a['position']=[-34,114]
 elif id=='company_banner':a['position']=[-23,104]
 elif id=='gate_banner':a['position']=[5,122]
 elif id=='old_park_bench':a['position']=[-94,-56]
 elif id=='view_bench':a['position']=[-111,-51]
 elif id=='cart_arrival':pack(a,[20,61,26,74])
 elif id=='clinic_planter':pack(a,[69,36,72,43])
 elif id=='food_planter':pack(a,[73,14,84,18])
 elif id.startswith('lamp_'):
  i=len([o for o in occupied]);pack(a,[-6,1,6,118])

# Allotments are on the east green strip, just beyond the homes; preserve actual bed sizes.
for z in P['ground_zones']:
 if z['id']=='spine_service_allotments':z['polygon']=move_poly(z['polygon'],34,-4);z['gate_position']=[141,39]
for a in P['props']:
 if a['id'].startswith('allotment_'):
  f=a['footprint'];a['footprint']=[f[0]+34,f[1]-4,f[2]+34,f[3]-4]
# Widen the south-east wall for the named public allotment; north-bank extent remains unchanged.
P['south_bank_boundary']=[[-113,-10],[130,-10],[145,10],[145,57],[130,57],[130,124],[-113,124]]
P['extent']=[[-114,-135],[132,-135],[132,8],[147,8],[147,59],[132,59],[132,127],[-114,127]]
P['city_wall']['segments'][1]=[[6.2,124],[130,124],[130,57],[145,57],[145,10],[130,-10]]
next(z for z in P['ground_zones'] if z['id']=='south_base')['polygon']=P['south_bank_boundary']
next(t for t in P['terrain']['terraces'] if t['id']=='south')['polygon']=P['south_bank_boundary']
route('allotment_lane',[[105,55],[144,55],[144,39],[141,39]],3)
next(a for a in P['props'] if a['id']=='allotment_gate')['opening_position']=[141,39]
next(d for d in P['districts'] if d['id']=='service')['bounds']=box([67,10,145,101])
P['phase_1']['polygon']=[[-67,30],[-43,30],[-43,-10],[130,-10],[145,10],[145,57],[129,57],[129,125],[-78,125],[-78,98],[-67,98]]

for z in P['ground_zones']:z['blend_width_per_edge_m']=[0]*len(z['polygon'])
P['small_plots']=[]
from landscape_v7 import build as landscape
landscape(P)
for d in P['districts']:
 owned=[b for b in P['buildings'] if b['district']==d['id']]
 d['label_position']=[round(sum(b['footprint'][0] for b in owned)/len(owned),2),round(sum(b['footprint'][1] for b in owned)/len(owned),2)]
 d['access_point']=min((pt for r in P['routes'] if not r.get('owner') for pt in r['centreline'] if g.inside(pt,d['bounds'])),key=lambda pt:math.dist(pt,d['label_position']))
P['sightlines'][1]['description']='Seven-metre main road gently bends; roofs retain v5 heights and kits.'
P['walk_time']['note']='v7 actual travel time is measured in check-result.json. The inherited 45-90 second v5 target is historical; the owner now fixes a 120-150 m gate-to-river distance. Runtime speed remains 3.2 m/s; no speed change is authorized.'
P['v7_changes']=dict(layout='New clustered layout; no v6 reuse or uniform building shrink',added_buildings=[b['id'] for b in P['buildings'] if b['id'] not in OB],candidate_only=True,reference_scale='f01 has no trustworthy dimensional anchor; comparison includes only v5 and v7',checker_migration='Retain inherited_checks geometry/graph functions; replace historical fixed-coordinate and v4 byte-allowlist validation with explicit v7 rules.',roof_note='Retained facade/roof identity is authoritative when a historic home joins a neighbouring district cluster.')
(R/'eurydica-plan.json').write_text(json.dumps(P,indent=2)+'\n',encoding='utf-8')
print('BUILD_V7_WRITTEN',len(P['buildings']),len(P['clusters']))
