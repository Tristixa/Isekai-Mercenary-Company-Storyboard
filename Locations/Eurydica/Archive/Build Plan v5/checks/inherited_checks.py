"""Independent geometry/graph checker, standard-library only. No project writes.
Run with Python 3.10+: check_plan.py [plan.json] [--self-test].
Collision uses swept route strips and building solids, not just centre points.
"""
import json, math, sys, re, copy, heapq
from pathlib import Path
ROOT=Path(__file__).resolve().parent
EPS=1e-6
def edges(poly):return list(zip(poly,poly[1:]+poly[:1]))
def inside(p,poly):
 x,y=p;odd=False
 for a,b in edges(poly):
  if distance(p,a,b)<EPS:return True
  if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:odd=not odd
 return odd
def distance(p,a,b):
 dx,dy=b[0]-a[0],b[1]-a[1];den=dx*dx+dy*dy
 t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/den)) if den else 0
 return math.dist(p,[a[0]+t*dx,a[1]+t*dy])
def boxpoly(r):a,b,c,d=r;return [[a,b],[c,b],[c,d],[a,d]]
def rotate(p,b,inverse=False):
 f=b['footprint'];cx,cz=(f[0]+f[2])/2,(f[1]+f[3])/2
 a=math.radians(b.get('yaw_deg',0))*(-1 if inverse else 1);c,s=math.cos(a),math.sin(a)
 x,z=p[0]-cx,p[1]-cz
 return [cx+c*x-s*z,cz+s*x+c*z]
def footprint(b):return [rotate(p,b) for p in boxpoly(b['footprint'])]
def area_overlap(a,b):
 # Convex polygon separating-axis test; touching boundaries have zero area.
 for poly in (a,b):
  for p,q in edges(poly):
   axis=[p[1]-q[1],q[0]-p[0]]
   aa=[v[0]*axis[0]+v[1]*axis[1] for v in a];bb=[v[0]*axis[0]+v[1]*axis[1] for v in b]
   if min(max(aa),max(bb))-max(min(aa),min(bb))<=EPS:return False
 return True
def strip(a,b,width):
 dx,dz=b[0]-a[0],b[1]-a[1];l=math.hypot(dx,dz);ox,oz=-dz/l*width/2,dx/l*width/2
 return [[a[0]+ox,a[1]+oz],[b[0]+ox,b[1]+oz],[b[0]-ox,b[1]-oz],[a[0]-ox,a[1]-oz]]
def key(p):return tuple(round(v,8) for v in p)
def segments(P):
 return [(r,i,a,b) for r in P['routes'] for i,(a,b) in enumerate(zip(r['centreline'],r['centreline'][1:]))]
def segheight(r,i,p):
 a,b=r['centreline'][i:i+2];return r['heights_m'][i]+math.dist(a,p)/math.dist(a,b)*(r['heights_m'][i+1]-r['heights_m'][i])
def graph(P):
 ss=segments(P);nodes=set()
 for r,i,a,b in ss:nodes.update([key(a),key(b)])
 # General segment intersections support curved (piecewise-linear) streets.
 for _,_,a,b in ss:
  for _,_,c,d in ss:
   u=[b[0]-a[0],b[1]-a[1]];v=[d[0]-c[0],d[1]-c[1]];den=u[0]*v[1]-u[1]*v[0]
   if abs(den)>EPS:
    w=[c[0]-a[0],c[1]-a[1]];t=(w[0]*v[1]-w[1]*v[0])/den;s=(w[0]*u[1]-w[1]*u[0])/den
    if -EPS<=t<=1+EPS and -EPS<=s<=1+EPS:nodes.add(key((a[0]+t*u[0],a[1]+t*u[1])))
 G={p:[] for p in nodes};heights={p:[] for p in nodes}
 for r,i,a,b in ss:
  ns=sorted([p for p in nodes if distance(p,a,b)<EPS],key=lambda p:math.dist(a,p))
  for p in ns:heights[p].append((r['id'],segheight(r,i,p)))
  for p,q in zip(ns,ns[1:]):
   d=math.hypot(math.dist(p,q),segheight(r,i,q)-segheight(r,i,p))
   G[p].append((q,d,r['id']));G[q].append((p,d,r['id']))
 return G,heights
def shortest(G,start):
 distances={start:0};queue=[(0,start)]
 while queue:
  d,p=heapq.heappop(queue)
  if d>distances[p]:continue
  for q,w,_ in G[p]:
   nd=d+w
   if nd<distances.get(q,float('inf')):distances[q]=nd;heapq.heappush(queue,(nd,q))
 return distances
def validate(P,external=True):
 errors=[];metrics={}
 def need(ok,msg):
  if not ok:errors.append(msg)
 required=['extent','districts','routes','junctions','terrain','river','bridge','city_wall','buildings','green','ground_zones','props','markers','npc_spots','phase_1','interiors','approved_connections']
 for k in required:need(k in P,'missing field '+k)
 if errors:return errors,metrics
 need(P['status']=='candidate','new plan must remain candidate')
 for col in ('districts','routes','buildings','markers','props'):
  ids=[v['id'] for v in P[col]];need(len(ids)==len(set(ids)),'duplicate IDs '+col)
 solids=[]
 for b in P['buildings']:
  need(b['footprint'][2]>b['footprint'][0] and b['footprint'][3]>b['footprint'][1],'invalid footprint '+b['id'])
  for r in b.get('collision_rectangles',[b['footprint']]):solids.append((b['id'],[rotate(p,b) for p in boxpoly(r)]))
  d=next(d for d in P['districts'] if d['id']==b['district'])
  need(all(inside(p,d['bounds']) for p in footprint(b)),'building outside owning district '+b['id'])
 for i,(id,a) in enumerate(solids):
  for jd,b in solids[i+1:]:need(not area_overlap(a,b),'building overlap '+id+' / '+jd)
 for r,i,a,b in segments(P):
  need(r['surface'] in ('paved_main','paved_local','earth'),'surface enum '+r['id'])
  need(r['width_m']>=3,'route width <3 '+r['id'])
  need(abs(r['grade'][i]-(r['heights_m'][i+1]-r['heights_m'][i])/math.dist(a,b))<1e-5,'incorrect grade '+r['id'])
  need(r['kind']=='stairs' or abs(r['grade'][i])<=.05001,'cart/step-free slope exceeds 5% '+r['id'])
  poly=strip(a,b,r['width_m'])
  for id,solid in solids:need(not area_overlap(poly,solid),'route hits building '+r['id']+' / '+id)
  # Every river intersection requires the sole real bridge deck.
  if area_overlap(poly,P['river']['polygon']):need(r['id']==P['bridge']['route_id'],'route crosses water without bridge '+r['id'])
  if area_overlap(poly,P['waterworks']['feeder_polygon']):
   need(r['id']==P['waterworks']['covered_crossing']['route_id'],'uncovered feeder crossing '+r['id'])
 G,heights=graph(P)
 for p,hs in heights.items():need(max(v for _,v in hs)-min(v for _,v in hs)<.015,'grade discontinuity at '+str(p)+' '+str(hs))
 start=min(G,key=lambda p:math.dist(p,[0,300]));reachable=shortest(G,start)
 need(len(reachable)==len(G),'disconnected route graph')
 for d in P['districts']:
  good=[p for p in G if p in reachable and inside(p,d['bounds'])]
  need(bool(good),'district not connected to South Gate '+d['id'])
 for b in P['buildings']:
  if b['id']=='south_gate':continue
  need(key(b['door_position']) in reachable,'door cannot reach graph '+b['id'])
  r=next((r for r in P['routes'] if r['id']==b.get('door_route')),None)
  need(r is not None and r['owner']==b['id'],'missing door access '+b['id'])
  if r:need(abs(r['heights_m'][-1]-b['ground_y_m'])<EPS,'door height mismatch '+b['id'])
  x0,z0,x1,z1=b['footprint'];p=rotate(b['door_position'],b,True);f=b['door_face']
  need(abs(p[0]-(x0 if f=='w' else x1))<EPS if f in ('w','e') else abs(p[1]-(z0 if f=='n' else z1))<EPS,'door off face '+b['id'])
 gate=[b for b in P['buildings'] if b['facade_id']=='gatehouse'];lod=[b for b in P['buildings'] if b['facade_id']=='lodging']
 need(len(gate)==1 and P['city_wall']['gates']==['south_gate'],'one gate required')
 need(len(lod)==1 and lod[0]['footprint'][0]>4,'one lodging east of spine required')
 need(all(b['roof_palette']=='green' for b in gate+lod),'gate/lodging shared green roofs')
 need(all(b['roof_palette']=='brown' for b in P['buildings'] if b['district'] in ('quays','workshops')),'working district brown roofs')
 lookup={b['id']:b for b in P['buildings']}
 def centre(b):f=b['footprint'];return [(f[0]+f[2])/2,(f[1]+f[3])/2]
 for id,limit in [('company_house',40),('stables',30)]:
  b=lookup[id];d=math.dist(centre(b),centre(lookup['south_gate']))
  metrics[id+'_gate_distance_m']=round(d,3)
  need(d<=limit,id+' exceeds gate proximity limit')
  need(b['footprint'][3]<300.4,id+' must be inside south wall')
 need(lookup['company_house']['display_name']=='Guild house','Guild display name')
 need(next(d for d in P['districts'] if d['id']=='company')['name']=='Guild Edge','Guild district name')
 need(lookup['lodging']['district']=='arrival' and 112<centre(lookup['lodging'])[1]<205,'lodging not at former Guild latitude')
 need(P['arrival_route']['names']==['Outskirts','South Gate','Guild Edge','Arrival Ward','Market Spine','Old Bridge'],'v2 arrival route order')
 for b in P['buildings']:
  expected='warm_red' if b['district']=='service' or b['id'].startswith(('old_home_','res_home_')) or ('home' in b['id'] and b['district'] in ('old_city','residential')) else 'brown' if b['district'] in ('quays','workshops') or b['id'] in ('stables','store_shed','waterkeeper','washing') else 'plum' if 'home' in b['id'] or b['id'] in ('company_house','company_neighbor') else 'green'
  if b['id'] in ('infill_home_12','infill_home_06','street_home_8','infill_home_23') and b['facade_id'].startswith('market_'):expected='green'
  need(b['roof_palette']==expected,'roof colour rule '+b['id'])
 it=next(i for i in P['interiors'] if i['id']=='guild_interior')
 officers=next((r for r in it['rooms'] if r['id']=='officers_room'),{})
 need(officers.get('occupants')==['Tristitia','Mae','Elsie'] and officers.get('available_from_start'),'starting shared officers room')
 need(any(m['id']=='guild_interior/officers_room_door' for m in P['markers']),'officers_room_door missing')
 upgrades=P['hq_reservation'].get('upgrades',[])
 need({u['id'] for u in upgrades}=={'dorm_annex','larger_dorm','officers_quarters_ii'},'three HQ reservations required')
 for i,u in enumerate(upgrades):
  need(all(inside(p,P['hq_reservation']['polygon']) for p in u['polygon']),'upgrade outside reservation '+u['id'])
  need(not any(area_overlap(u['polygon'],solid) for _,solid in solids),'upgrade occupied by building '+u['id'])
  need(not any(area_overlap(u['polygon'],strip(a,b,r['width_m'])) for r,_,a,b in segments(P)),'upgrade blocks access '+u['id'])
  need(not any(area_overlap(u['polygon'],v['polygon']) for v in upgrades[i+1:]),'upgrade parcels overlap')
 need(P['phase_1'].get('phase')==1 and all(lookup[id]['phase']==1 for id in ('south_gate','company_house','store_shed','stables','guard_shelter','lodging','tavern')),'v2 phase 1 coverage')
 need(set(j['id'] for j in P['junctions'])==set(range(1,7)),'junction ids 1-6')
 expected={1:['join1'],2:['join2_earth','join2_apron'],3:['join3'],4:['service_public_loop','join4'],5:['join5'],6:['join6','join6_apron']}
 expected_points={1:[0,155],2:[0,25],3:[0,70],4:[0,205],5:[0,285],6:[0,105]}
 route_ids={r['id'] for r in P['routes']}
 for n,ids in expected.items():
  rec=next((c for c in P['approved_connections'] if c['id']==n),{})
  need(rec.get('route_ids')==ids and all(id in route_ids for id in ids),'approved connection missing '+str(n))
  need(any(rid in ids for links in G.values() for _,_,rid in links),'approved connection has no graph edge '+str(n))
  point=key(expected_points[n]);need(any(rid in ids for _,_,rid in G.get(point,[])),'approved connection not at required spine junction '+str(n))
 j={j['id']:j['position'] for j in P['junctions']}
 need(j[6][1]>j[3][1] and j[2][1]<j[3][1],'south-bank junction ordering')
 need(all(r['surface']!='earth' for r in P['routes'] if r['id'] in ['join3','join4','service_public_loop','household_access']),'Service Lanes must be paved')
 court=next(z['polygon'] for z in P['ground_zones'] if z['id']=='household_court')
 need(not any(area_overlap(strip(a,b,r['width_m']),court) for r,i,a,b in segments(P) if r['id']=='service_public_loop'),'public route crosses household court')
 def outdoor_walk(p):
  if any(inside(p,s) for _,s in solids):return False
  if inside(p,P['river']['polygon']):return any(inside(p,strip(a,b,r['width_m'])) for r,i,a,b in segments(P) if r['id']=='old_bridge')
  if inside(p,P['waterworks']['feeder_polygon']) and not inside(p,P['waterworks']['covered_crossing']['polygon']):return False
  return any(z['walkable'] and inside(p,z['polygon']) for z in P['ground_zones']) and not any(not z['walkable'] and inside(p,z['polygon']) for z in P['ground_zones'])
 def marker_reaches_graph(p):
  # Find a visible walkable connector to a reachable centreline; no travel through a building/water.
  candidates=[]
  for r,i,a,b in segments(P):
   dx,dz=b[0]-a[0],b[1]-a[1];length2=dx*dx+dz*dz
   t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dz)/length2));q=[a[0]+t*dx,a[1]+t*dz]
   if key(a) in reachable:candidates.append((math.dist(p,q),q))
  for length,q in sorted(candidates)[:24]:
   steps=max(1,math.ceil(length/.25))
   if all(outdoor_walk([p[0]+(q[0]-p[0])*k/steps,p[1]+(q[1]-p[1])*k/steps]) for k in range(steps+1)):return True
  return False
 for m in P['markers']:
  p=m['position']
  if m['scene']=='city':
   need(outdoor_walk(p),'marker off walkable ground '+m['id'])
   need(marker_reaches_graph(p),'marker cannot reach route graph '+m['id'])
  else:
   it=next((i for i in P['interiors'] if i['id']==m['scene']),None)
   need(it and inside(p,it['walkable_polygon']) and not any(inside(p,o) for o in it['obstacles']),'interior marker off ground '+m['id'])
 for z in P['ground_zones']:need(len(z['blend_width_per_edge_m'])==len(z['polygon']) and min(z['blend_width_per_edge_m'])>=0,'invalid blend edges '+z['id'])
 for t in P['green']['trees']:
  need(outdoor_walk(t['position']),'tree on obstacle/water '+t['id'])
  need(not any(inside(t['position'],c['polygon']) for c in P['terrain']['cliffs']),'tree on cliff '+t['id'])
  need(all(distance(t['position'],a,b)>=r['width_m']/2+t['trunk_collision_radius_m'] for r,i,a,b in segments(P)),'tree trunk blocks route '+t['id'])
 for p in P['props']:
  if 'position' in p:
   need(outdoor_walk(p['position']) or p['id']=='gate_banner','prop inside solid/water '+p['id'])
   if p['type'] not in ('banner',):need(all(distance(p['position'],a,b)>=r['width_m']/2+p['collision_radius_m'] for r,i,a,b in segments(P)),'prop blocks route '+p['id'])
 # Measured gate to market: inject exact endpoints by splitting the graph.
 Q=copy.deepcopy(P)
 for pt in [P['walk_time']['start'],P['walk_time']['finish']]:
  for r in Q['routes']:
   for i,(a,b) in enumerate(zip(r['centreline'],r['centreline'][1:])):
    if distance(pt,a,b)<EPS and pt!=a and pt!=b:
     y=segheight(r,i,pt);r['centreline'].insert(i+1,pt);r['heights_m'].insert(i+1,y);break
 GG,_=graph(Q);length=shortest(GG,key(P['walk_time']['start'])).get(key(P['walk_time']['finish']),float('inf'))
 metrics.update(buildings=len(P['buildings']),districts=len(P['districts']),routes=len(P['routes']),markers=len(P['markers']),graph_nodes=len(G),walk_distance_m=round(length,3),walk_time_s=round(length/P['walk_time']['speed_m_s'],3),new_facade_ids=len(P['new_facades']))
 need(60<=metrics['walk_time_s']<=120,'gate-market walk outside 60-120 seconds')
 if external:
  src=Path('D:/Storyboards/Isekai Mercenary Company')
  spec=json.loads((src/'Environment Assets/Eurydica/Approved Facades v1/facades-spec.json').read_text(encoding='utf-8-sig'))['buildings']
  for b in P['buildings']:
   if b['facade_id'] in spec and b['facade_id'] not in ('house_green','house_violet'):
    c=spec[b['facade_id']];f=b['footprint']
    need(all(abs(x-y)<EPS for x,y in zip([f[2]-f[0],f[3]-f[1]],c['footprint_m'])) and b['height_m']==c['wall_height_m'],'approved dimensions changed '+b['id'])
  lines=(src/'Locations/Eurydica/markers.md').read_text(encoding='utf-8-sig').splitlines();section='';wanted=[]
  for line in lines:
   if line.startswith('## '):section=line
   m=re.match(r'- `([^`]+)`',line)
   if m and 'Outskirts' not in section:
    scene='tavern_interior' if 'Tavern' in section else 'guild_interior' if 'interior' in section else 'city'
    wanted.append(scene+'/'+m[1])
  need(set(wanted)<=set(m['id'] for m in P['markers']),'source marker coverage incomplete')
  s4=(src/'Manuscript/Chapter 1 - New Beginning/Scene 4 Day 2-5.md').read_text(encoding='utf-8-sig').splitlines()
  wanted4={(n,line[7:]) for n,line in enumerate(s4,1) if line.startswith('Where: ')}
  need(wanted4=={(m['source_line'],m['where']) for m in P['markers'] if 'where' in m},'Scene 4 Where coverage mismatch')
  for t in P['green']['trees']:need((src/t['source']/(t['type']+'.png')).exists(),'missing Mosswood type '+t['type'])
 return errors,metrics
def controls(P):
 tests=[]
 def run(name,mutate,token):
  q=copy.deepcopy(P);mutate(q);errs,_=validate(q,False);assert any(token in e for e in errs),(name,errs);tests.append(name)
 run('building collision',lambda q:q['buildings'].append(dict(q['buildings'][1],id='bad_overlap')),'building overlap')
 run('route obstruction',lambda q:q['buildings'][1].update(footprint=[-1,280,1,284]),'route hits building')
 run('narrow route',lambda q:q['routes'][1].update(width_m=2),'route width')
 run('water marker',lambda q:q['markers'][0].update(position=[50,-25]),'marker off')
 run('door disconnect',lambda q:q['buildings'][1].update(door_position=[111,310]),'door cannot')
 run('missing join',lambda q:q.update(routes=[r for r in q['routes'] if r['id']!='join1']),'approved connection missing')
 run('isolated north bank',lambda q:q.update(routes=[r for r in q['routes'] if r['id']!='old_bridge']),'disconnected route graph')
 run('wrong lodging bank',lambda q:next(b for b in q['buildings'] if b['id']=='lodging').update(footprint=[-20,250,-10,258]),'one lodging east')
 run('duplicate gate',lambda q:q['buildings'].append(dict(q['buildings'][0],id='extra_gate')),'one gate')
 run('grade mismatch',lambda q:q['routes'][1]['heights_m'].__setitem__(0,5),'incorrect grade')
 run('Guild too far from gate',lambda q:next(b for b in q['buildings'] if b['id']=='company_house').update(footprint=[-34,144,-26,152]),'company_house exceeds gate proximity')
 run('stables too far from gate',lambda q:next(b for b in q['buildings'] if b['id']=='stables').update(footprint=[39,276,47,284]),'stables exceeds gate proximity')
 run('missing shared room',lambda q:next(i for i in q['interiors'] if i['id']=='guild_interior').update(rooms=[]),'starting shared officers room')
 run('wrong roof',lambda q:next(b for b in q['buildings'] if b['id']=='company_house').update(roof_palette='green'),'roof colour rule')
 return tests
if __name__=='__main__':
 file=next((Path(a) for a in sys.argv[1:] if not a.startswith('--')),ROOT/'eurydica-plan.json')
 try:P=json.loads(file.read_text(encoding='utf-8-sig'));errors,metrics=validate(P)
 except Exception as exc:print('PLAN_CHECK_FAIL',type(exc).__name__,str(exc));sys.exit(1)
 for error in errors:print('FAIL:',error)
 print(json.dumps(metrics,indent=2))
 if errors:sys.exit(1)
 if '--self-test' in sys.argv:
  tests=controls(P);print('Negative controls rejected: '+', '.join(tests));metrics['negative_controls']=len(tests)
 print('PLAN_CHECK_PASS: geometry, door access, connected districts, markers, widths, six joins, single gate and east lodging.')
 (ROOT/'check-result.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
