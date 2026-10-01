"""v7 extension of the v5 checker. Reuses its exact SAT, rotation and route graph.

Historical v3/v4 byte equality, obsolete fixed southern coordinates, and density
targets are superseded by the v7 brief. They are replaced with explicit baseline
identity/terrain invariants, not filtered out of a failing validation run.
"""
import sys,json,math,copy,hashlib,statistics
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as g
R=Path(__file__).resolve().parent
SOURCE=Path('D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/Archive/Build Plan v5')
OLD=json.loads((SOURCE/'eurydica-plan.json').read_bytes())
EPS=1e-5
def area(p):return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in g.edges(p)))/2
def bounds(p):return min(x for x,z in p),min(z for x,z in p),max(x for x,z in p),max(z for x,z in p)
def overlap(a,b):
 x,z,X,Z=bounds(a);u,v,U,V=bounds(b)
 return min(X,U)>max(x,u)+EPS and min(Z,V)>max(z,v)+EPS and g.area_overlap(a,b)
def gap(a,b):
 if overlap(a,b):return 0.
 return min([g.distance(p,c,d) for p in a for c,d in g.edges(b)]+[g.distance(p,c,d) for p in b for c,d in g.edges(a)])
def closest(a,b):
 out=[]
 for rev,p,q in [(False,a,b),(True,b,a)]:
  for v in p:
   for c,d in g.edges(q):
    dx,dz=d[0]-c[0],d[1]-c[1];t=max(0,min(1,((v[0]-c[0])*dx+(v[1]-c[1])*dz)/(dx*dx+dz*dz)))
    w=[c[0]+t*dx,c[1]+t*dz];out.append((math.dist(v,w),w if rev else v,v if rev else w))
 return min(out,key=lambda x:x[0])
def solids(p):return [(b['id'],[g.rotate(v,b) for v in g.boxpoly(f)]) for b in p['buildings'] for f in b.get('collision_rectangles',[b['footprint']])]
def roadseparates(a,b,p):
 _,v,w=closest(a,b)
 return any(g.inside([v[0]+(w[0]-v[0])*i/20,v[1]+(w[1]-v[1])*i/20],g.strip(c,d,r['width_m'])) for r,k,c,d in g.segments(p) if r['kind'] in ('street','gate_passage') for i in range(1,20))
def walkable(pt,p,ss,prop_polys=None,radius=0):
 if not any(z['walkable'] and g.inside(pt,z['polygon']) for z in p['ground_zones']):return False
 if any(not z['walkable'] and g.inside(pt,z['polygon']) for z in p['ground_zones']):return False
 if g.inside(pt,p['river']['polygon']) and not any(r['id']=='old_bridge' and g.inside(pt,g.strip(a,b,r['width_m'])) for r,i,a,b in g.segments(p)):return False
 if g.inside(pt,p['waterworks']['feeder_polygon']) and not g.inside(pt,p['waterworks']['covered_crossing']['polygon']):return False
 for s in [s for _,s in ss]+(prop_polys or []):
  if g.inside(pt,s) or radius and min(g.distance(pt,a,b) for a,b in g.edges(s))<radius-EPS:return False
 return True
def validate(p,full=True):
 errors=[];metrics={};need=lambda v,s:errors.append(s) if not v else None
 b={v['id']:v for v in p['buildings']};old={v['id']:v for v in OLD['buildings']};cs={c['id']:c for c in p['clusters']};ss=solids(p)
 need(p['status']=='candidate','candidate status required');need(p['schema_version']==OLD['schema_version'],'base schema version changed')
 for key in ('buildings','markers','npc_spots','props','routes','clusters','ground_zones'):
  ids=[a['id'] for a in p[key]];need(len(ids)==len(set(ids)),'duplicate IDs '+key)
 for id,o in old.items():
  need(id in b,'missing building '+id)
  if id not in b:continue
  q=b[id]
  for k in ('facade_id','role','display_name','height_m','roof_height_m','roof_palette','roof_kit','chapter_availability'):
   need(q.get(k)==o.get(k),'identity/use/roof changed '+id+' '+k)
  need(all(abs(a-c)<EPS for a,c in zip([q['footprint'][2]-q['footprint'][0],q['footprint'][3]-q['footprint'][1]],[o['footprint'][2]-o['footprint'][0],o['footprint'][3]-o['footprint'][1]])),'building resized '+id)
 spec=json.loads(Path('D:/Storyboards/Isekai Mercenary Company/Environment Assets/Eurydica/Approved Facades v1/facades-spec.json').read_text(encoding='utf-8-sig'))['buildings']
 for id in b.keys()-old.keys():
  q=b[id];need(q['facade_id'] in spec,'unapproved added facade '+id)
  if q['facade_id'] in spec:
   need([q['footprint'][2]-q['footprint'][0],q['footprint'][3]-q['footprint'][1]]==spec[q['facade_id']]['footprint_m'],'added facade dimensions '+id)
  need(q['roof_palette']==('warm_red' if q['district']=='service' else 'plum'),'added roof rule '+id)
 need([d['id'] for d in p['districts']]==[d['id'] for d in OLD['districts']],'ten districts and order changed')
 need(p['arrival_route']['names']==OLD['arrival_route']['names'],'arrival district order changed')
 for c in OLD['approved_connections']:
  n=next((v for v in p['approved_connections'] if v['id']==c['id']),{})
  need(n.get('route_ids')==c['route_ids'] and n.get('description')==c['description'],'connection topology changed '+str(c['id']))
  need(all(id in {r['id'] for r in p['routes']} for id in c['route_ids']),'missing connection route '+str(c['id']))
 for k in ('river','bridge','waterworks','camera','interiors','finish','new_facades'):need(p[k]==OLD[k],'protected data changed '+k)
 for k in ('terraces','retaining_walls','ramps','stairs','cliffs'):
  for v in OLD['terrain'][k]:
   if v['id'] in ('south','company_platform','company_west','company_south') or v['id'].startswith('join5'):continue
   need(v in p['terrain'][k],'fixed terrain changed '+v['id'])
 for id in ('old_bridge','civic_old_ramp','civic_res_ramp','watch_stairs','view_deck','dock_ramp','dock_deck'):
  need(next((r for r in p['routes'] if r['id']==id),{})==next(r for r in OLD['routes'] if r['id']==id),'fixed route changed '+id)
 need(b['watch_tower']['footprint']==old['watch_tower']['footprint'] and b['watch_tower']['ground_y_m']==2 and b['watch_tower']['clock_face']=='s' and b['watch_tower']['belfry_open'],'clock tower lock')
 for k in ('markers','npc_spots','props'):
  need({a['id'] for a in OLD[k]}<={a['id'] for a in p[k]},'lost IDs '+k)
 for m in OLD['markers']:
  q=next((a for a in p['markers'] if a['id']==m['id']),{})
  for k in m:
   if k not in ('position','height_m','footprint'):need(q.get(k)==m[k],'story marker metadata changed '+m['id']+' '+k)
  if m['id'].startswith('civic_terrace/') or m['scene']!='city':need(q==m,'fixed appointment/interior marker '+m['id'])
 for n in p['npc_spots']:
  m=next((a for a in p['markers'] if a['id']==n['marker_id']),{})
  need(n['position']==m.get('position'),'NPC binding '+n['id'])
  o=next(a for a in OLD['npc_spots'] if a['id']==n['id']);need(n['schedule']==o['schedule'],'NPC schedule '+n['id'])
 for a in OLD['props']:
  q=next(v for v in p['props'] if v['id']==a['id'])
  for k in ('type','awning','contents','footprint_includes_awning'):need(q.get(k)==a.get(k),'prop identity '+a['id']+' '+k)
  if 'footprint' in a:need(all(abs(x-y)<EPS for x,y in zip([a['footprint'][2]-a['footprint'][0],a['footprint'][3]-a['footprint'][1]],[q['footprint'][2]-q['footprint'][0],q['footprint'][3]-q['footprint'][1]])),'prop resized '+a['id'])
 for q in p['portals']:
  if 'city_building' in q:need(q['city_position']==b[q['city_building']]['door_position'],'portal binding '+q['id'])
  elif q['id'] in ('dorm_annex_portal','larger_dorm_portal'):need(q.get('player_access') is False,'dormitory player_access '+q['id'])
 membership=[id for c in p['clusters'] for id in c['building_ids']]
 need(len(membership)==len(set(membership)) and set(membership)==set(b),'cluster membership coverage')
 schedule={'gate_cluster','guild_compound','lodging_row','arrival_court','red_tree_court','market_row','market_homes','service_lane','service_homes','workshop_yard','quay_row','civic_plaza','old_city_row','residential_a','residential_b','waterworks_group'}
 need(schedule<=cs.keys(),'cluster schedule missing')
 rows=[]
 for c in p['clusters']:
  need(3<=len(c['building_ids'])<=8,'cluster size '+c['id'])
  vals=[]
  for id in c['building_ids']:
   if id not in b:continue
   q=b[id];need(q.get('cluster_id')==c['id'],'cluster binding '+id)
   d=min((gap(g.footprint(q),g.footprint(b[j])),j) for j in c['building_ids'] if j!=id and j in b)
   if id not in ('south_gate','watch_tower'):need(d[0]<=2+EPS,'cluster wall gap '+id+' '+str(round(d[0],3)));vals.append(d[0])
   rows.append(dict(id=id,cluster=c['id'],nearest=d[1],gap_m=round(d[0],6)))
  cpoly=[g.footprint(b[id]) for id in c['building_ids'] if id in b]
 for i,a in enumerate(p['clusters']):
  for c in p['clusters'][i+1:]:
   distance,ida,idb=min((gap(g.footprint(b[x]),g.footprint(b[y])),x,y) for x in a['building_ids'] for y in c['building_ids'])
   if distance<8-EPS:need(roadseparates(g.footprint(b[ida]),g.footprint(b[idb]),p),'intercluster gap '+a['id']+' / '+c['id']+' '+str(round(distance,3)))
 for i,(id,a) in enumerate(ss):
  need(all(g.inside(v,p['extent']) for v in a),'building outside extent '+id)
  for jd,c in ss[i+1:]:need(not overlap(a,c),'building overlap '+id+' / '+jd)
  need(not overlap(a,p['river']['polygon']) and not overlap(a,p['waterworks']['feeder_polygon']),'building in water '+id)
  need(not overlap(a,p['hq_reservation']['polygon']),'HQ occupied '+id)
  for t in p['terrain']['cliffs']:need(not overlap(a,t['polygon']),'building on cliff '+id)
 for r,i,a,c in g.segments(p):
  w=r['width_m'];need(w>=2,'route width '+r['id'])
  if r['id']=='main_road':need(6<=w<=8,'main road width')
  strip=g.strip(a,c,w)
  for id,s in ss:need(not overlap(strip,s),'route hits building '+r['id']+' / '+id)
  if overlap(strip,p['river']['polygon']):need(r['id']=='old_bridge','unbridged river crossing '+r['id'])
  if overlap(strip,p['waterworks']['feeder_polygon']):need(r['id']=='north_riverside','uncovered feeder crossing '+r['id'])
  need(not overlap(strip,p['hq_reservation']['polygon']),'route through HQ reserve '+r['id'])
  need(abs(r['grade'][i]-(r['heights_m'][i+1]-r['heights_m'][i])/math.dist(a,c))<EPS,'incorrect route grade '+r['id'])
  need(r['kind']=='stairs' or abs(r['grade'][i])<=.05001,'route slope '+r['id'])
 gate=b['south_gate'];gate_dist=gate['footprint'][1]-max(z for x,z in p['river']['polygon']);need(120<=gate_dist<=150,'gate-to-river distance')
 need(p['city_wall']['gates']==['south_gate'] and sum(v['facade_id']=='gatehouse' for v in b.values())==1,'single gate')
 need(all(b[id]['phase']==1 for id in ('south_gate','company_house','stables','store_shed','lodging','tavern','clinic','food_shop')),'phase 1 coverage')
 for c in p['clusters']:
  if c['phase']==1:
   need(all(g.inside(v,p['phase_1']['polygon']) for id in c['building_ids'] for v in g.footprint(b[id])),'phase polygon '+c['id'])
  if c['id'] in ('workshop_yard','quay_row'):need(all(not g.inside([(b[id]['footprint'][0]+b[id]['footprint'][2])/2,(b[id]['footprint'][1]+b[id]['footprint'][3])/2],p['phase_1']['polygon']) for id in c['building_ids']),'phase 2 inside phase 1 '+c['id'])
 ppolys=[]
 for a in p['props']:
  if 'footprint' in a:poly=g.boxpoly(a['footprint'])
  elif 'position' in a and a['type']!='banner':
   x,z=a['position'];r=a.get('collision_radius_m',.1);poly=g.boxpoly([x-r,z-r,x+r,z+r])
  else:continue
  for id,s in ss:need(not overlap(poly,s),'prop hits building '+a['id']+' / '+id)
  for r,i,v,w in g.segments(p):need(not overlap(poly,g.strip(v,w,r['width_m'])),'prop blocks route '+a['id']+' / '+r['id'])
  for id,s in ppolys:need(not overlap(poly,s),'prop overlap '+a['id']+' / '+id)
  need(not overlap(poly,p['hq_reservation']['polygon']),'prop in HQ '+a['id']);ppolys.append((a['id'],poly))
  if a.get('zone_id'):
   z=next((z for z in p['ground_zones'] if z['id']==a['zone_id']),None);need(z is not None and all(g.inside(v,z['polygon']) for v in poly),'prop outside zone '+a['id'])
 for m in p['markers']:
  if m['scene']=='city':need(walkable(m['position'],p,ss,[poly for id,poly in ppolys],.25),'marker off walkable ground '+m['id'])
 for t in p['green']['trees']:
  need(walkable(t['position'],p,ss,[poly for id,poly in ppolys]),'tree collision '+t['id'])
  need(not any(g.inside(t['position'],c['polygon']) for c in p['terrain']['cliffs']),'tree on cliff '+t['id'])
  for r,i,a,c in g.segments(p):need(g.distance(t['position'],a,c)>=r['width_m']/2+t['trunk_collision_radius_m']-EPS,'tree blocks route '+t['id'])
 red=next(t for t in p['green']['trees'] if t['id']=='tree_08');bed=next((z for z in p['ground_zones'] if z['id']=='red_tree_bed'),{})
 need(bed.get('material')=='grass_earth' and g.inside(red['position'],bed.get('polygon',[])),'red tree needs open ground bed')
 need(bed.get('priority',0)>max([z.get('priority',0) for z in p['ground_zones'] if z['material']=='paving' and g.inside(red['position'],z['polygon'])]+[0]),'red tree paving override')
 need(len(p['green'].get('spaces',[]))>0,'named intercluster green missing')
 greenarea=sum(area(s) for space in p['green'].get('spaces',[]) for s in space['polygons'])
 if full:
  G,heights=g.graph(p);start=min(G,key=lambda pt:math.dist(pt,[0,122]));reach=g.shortest(G,start)
  need(len(reach)==len(G),'disconnected route graph')
  for pt,hs in heights.items():need(max(v for _,v in hs)-min(v for _,v in hs)<.015,'route elevation discontinuity '+str(pt))
  for q in p['buildings']:
   if q['id']=='south_gate':continue
   need(g.key(q['door_position']) in reach,'door not reachable '+q['id'])
   r=next((r for r in p['routes'] if r['id']==q.get('door_route')),{})
   need(r.get('owner')==q['id'] and abs(r.get('heights_m',[999])[-1]-q['ground_y_m'])<EPS,'door binding/height '+q['id'])
  def connector(pt):
   cand=[]
   for r,i,a,c in g.segments(p):
    if g.key(a) not in reach:continue
    dx,dz=c[0]-a[0],c[1]-a[1];t=max(0,min(1,((pt[0]-a[0])*dx+(pt[1]-a[1])*dz)/(dx*dx+dz*dz)));v=[a[0]+t*dx,a[1]+t*dz];cand.append((math.dist(pt,v),v))
   for d,v in sorted(cand)[:50]:
    n=max(1,math.ceil(d/.25))
    samples=[[pt[0]+(v[0]-pt[0])*i/n,pt[1]+(v[1]-pt[1])*i/n] for i in range(n+1)]
    if all(walkable(q,p,ss,[s for id,s in ppolys],.25) and all(math.dist(q,t['position'])>=.25+t['trunk_collision_radius_m'] for t in p['green']['trees']) for q in samples):return v
   return None
  for m in p['markers']:
   if m['scene']=='city':need(connector(m['position']) is not None,'marker unreachable '+m['id'])
  metrics['graph_nodes']=len(G)
  a,bp=map(g.key,[p['walk_time']['start'],p['walk_time']['finish']]);dist=g.shortest(G,a).get(bp,float('inf'))
  metrics.update(gate_market_walk_m=round(dist,3),gate_market_walk_s_at_3_2=round(dist/3.2,3),gate_market_stroll_s_at_2=round(dist/2,3))
 metrics.update(buildings=len(b),buildings_before=len(old),added_buildings=sorted(b.keys()-old.keys()),clusters=len(cs),districts=len(p['districts']),markers=len(p['markers']),npc_spots=len(p['npc_spots']),props=len(p['props']),gate_river_m=round(gate_dist,3),spacing_rows=rows,median_cluster_wall_gap_m=round(statistics.median(v['gap_m'] for v in rows if v['id'] not in ('south_gate','watch_tower')),4),green_area_m2=round(greenarea,2),green_locations=[dict(id=s['id'],name=s['name'],area_m2=round(sum(area(a) for a in s['polygons']),2)) for s in p['green'].get('spaces',[])])
 from detail_checks import validate as details
 more,extra=details(p,OLD,full);errors.extend(more);metrics.update(extra)
 return errors,metrics
def controls(p):
 tests=[]
 def bad(name,mutate,token,full=False):
  q=copy.deepcopy(p);mutate(q);e,_=validate(q,full);assert any(token in x for x in e),(name,e);tests.append(name)
 bad('missing original identity',lambda q:q['buildings'][1].update(role='Different use'),'identity/use/roof')
 bad('ordinary building isolated',lambda q:next(b for b in q['buildings'] if b['id']=='lodging').update(footprint=[400,400,410,408]),'cluster wall gap')
 bad('missing scheduled cluster',lambda q:q['clusters'].pop(0),'cluster schedule')
 bad('overlapping buildings',lambda q:q['buildings'][1].update(footprint=q['buildings'][2]['footprint']),'building overlap')
 bad('river marker',lambda q:next(m for m in q['markers'] if m['id']=='city/main_street').update(position=[40,-25]),'marker off walkable')
 bad('missing roof kit',lambda q:q['buildings'][1].pop('roof_kit'),'identity/use/roof')
 bad('paved red tree',lambda q:next(z for z in q['ground_zones'] if z['id']=='red_tree_bed').update(material='paving'),'red tree needs')
 bad('terrain moved',lambda q:q['river'].update(water_y_m=0),'protected data')
 bad('civic marker moved',lambda q:next(m for m in q['markers'] if m['id']=='civic_terrace/commander').update(position=[10,-63.8]),'fixed appointment')
 bad('dorm access opened',lambda q:next(a for a in q['portals'] if a['id']=='dorm_annex_portal').update(player_access=True),'dormitory player_access')
 bad('prop blocks street',lambda q:next(a for a in q['props'] if a['id']=='market_court_stall_1').update(footprint=[-1,26,1,28]),'prop blocks route')
 bad('missing green spaces',lambda q:q['green'].update(spaces=[]),'named intercluster green')
 bad('door off wall',lambda q:next(b for b in q['buildings'] if b['id']=='lodging').update(door_position=[10,66]),'door off exact face')
 bad('building assigned outside district',lambda q:next(b for b in q['buildings'] if b['id']=='old_hall').update(district='market'),'district containment')
 bad('junction order reversed',lambda q:next(j for j in q['junctions'] if j['id']==4).update(position=[0,110]),'six connection order')
 bad('green area duplicated',lambda q:q['green']['spaces'].append(copy.deepcopy(q['green']['spaces'][0])),'green area double-count')
 bad('Guild bench relation changed',lambda q:next(m for m in q['markers'] if m['id']=='city/bench_east').update(position=[-36,114]),'Guild staging relation')
 bad('allotment aisle geometry changed',lambda q:next(a for a in q['props'] if a['id']=='allotment_bed_1').update(footprint=[112,13,130,25]),'allotment internal layout')
 bad('marker height changed',lambda q:next(m for m in q['markers'] if m['id']=='city/main_street').update(height_m=5),'marker ground height')
 bad('disconnected route',lambda q:q['routes'].append(dict(id='isolated_control',centreline=[[120,115],[120,117]],width_m=2,surface='paved_local',heights_m=[0,0],grade=[0],phase=1,kind='street',walkable=True)),'disconnected route graph',True)
 bad('crossing route heights disagree',lambda q:next(r for r in q['routes'] if r['id']=='gate_arch').update(heights_m=[1,1]),'route elevation discontinuity',True)
 assert abs(gap(g.boxpoly([0,0,5,5]),g.boxpoly([8,0,10,5]))-3)<EPS
 assert gap(g.boxpoly([0,0,5,5]),g.boxpoly([5,0,10,5]))==0
 tests.append('positive 3 m and party-wall 0 m controls')
 return tests
if __name__=='__main__':
 path=next((Path(a) for a in sys.argv[1:] if not a.startswith('--')),R/'eurydica-plan.json')
 p=json.loads(path.read_bytes());errors,metrics=validate(p)
 if '--self-test' in sys.argv and not errors:metrics['negative_controls']=controls(p)
 metrics.update(plan_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),errors=errors)
 (R/'check-result.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in metrics.items() if k not in ('spacing_rows','green_locations')},indent=2))
 print('PLAN_CHECK_FAIL' if errors else 'PLAN_CHECK_PASS');sys.exit(bool(errors))
