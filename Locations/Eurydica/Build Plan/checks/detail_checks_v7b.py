"""Semantic and surface checks added after reviewing the resumed v7 checker."""
import math,statistics,hashlib,json,copy
import inherited_checks as g

def validate(p,old,full=True):
 from check_plan_v7b import overlap,gap,bounds,area,solids
 errors=[];metrics={}
 def need(ok,s):
  if not ok:errors.append(s)
 bs={b['id']:b for b in p['buildings']};cs={c['id']:c for c in p['clusters']};ds={d['id']:d for d in p['districts']};ms={m['id']:m for m in p['markers']}
 from check_plan_v7b import SOURCE
 need(p['source_v5_sha256']==hashlib.sha256((SOURCE/'eurydica-plan.json').read_bytes()).hexdigest(),'source v5 digest mismatch')
 ss=solids(p);routes=[(r,g.strip(a,b,r['width_m'])) for r,i,a,b in g.segments(p)]
 props=[]
 for a in p['props']:
  if 'footprint' in a:props.append((a,g.boxpoly(a['footprint'])))
  elif 'position' in a and a['type']!='banner':
   x,z=a['position'];r=a.get('collision_radius_m',.1);props.append((a,g.boxpoly([x-r,z-r,x+r,z+r])))
 for b in p['buildings']:
  need(all(g.inside(v,ds[b['district']]['bounds']) for v in g.footprint(b)),'district containment '+b['id'])
  c=cs.get(b.get('cluster_id'));need(c is not None and c['district']==b['district'],'cluster district '+b['id'])
  x,z,X,Z=b['footprint'];pt=g.rotate(b['door_position'],b,True);face=b['door_face']
  onface=abs(pt[0]-(x if face=='w' else X))<1e-5 and z<=pt[1]<=Z if face in ('w','e') else abs(pt[1]-(z if face=='n' else Z))<1e-5 and x<=pt[0]<=X
  need(onface,'door off exact face '+b['id'])
  if b['id']!='south_gate':
   r=next((r for r in p['routes'] if r.get('owner')==b['id']),None)
   if r:
    need(math.dist(r['centreline'][-1],b['door_position'])<1e-5,'door route endpoint '+b['id'])
    need(r['width_m']>=2 and all(r['walkable'] for _ in [0]),'door clearance '+b['id'])
  need(bool(b.get('roof_kit')),'roof kit missing '+b['id'])
 # Exact required functions, retaining v5's historic stable IDs.
 required={'guild_compound':{'company_house','store_shed','stables'},'red_tree_court':{'tavern','infill_home_12','street_home_8','provisions'},'market_row':{'repair_supply','infill_home_06','infill_home_23'},'service_lane':{'food_shop','clinic','service_home_0','service_home_3'},'workshop_yard':{'tool_repair','timber_containers','material_sorting'},'quay_row':{'bulk_storehouse','quay_storehouse','loading_shelter'},'civic_plaza':{'watch_tower','toll_records','civic_guard','notice_shelter'},'old_city_row':{'old_hall','old_home_0','old_home_1','old_home_2'},'waterworks_group':{'waterkeeper','washing','cistern'}}
 for id,ids in required.items():need(id in cs and ids<=set(cs[id]['building_ids']),'cluster scheduled functions '+id)
 # All six branch attachments follow their original south-to-north ordering.
 js={j['id']:j['position'] for j in p['junctions']}
 need(set(js)==set(range(1,7)),'six junction IDs')
 need(all(js[a][1]>js[b][1] for a,b in zip([5,4,1,6,3],[4,1,6,3,2])),'six connection order')
 main=next(r for r in p['routes'] if r['id']=='main_road')
 for rec in p['approved_connections']:
  pt=js[rec['id']]
  need(rec['junction']==pt and any(g.distance(pt,a,b)<1e-5 for a,b in zip(main['centreline'],main['centreline'][1:])),'junction on main road '+str(rec['id']))
  need(any(g.distance(pt,a,b)<1e-5 for r,i,a,b in g.segments(p) if r['id'] in rec['route_ids']),'connection attaches '+str(rec['id']))
 # Same-size HQ parcels, all unbuilt and immediately adjacent to the Guild.
 reserve=p['hq_reservation'];oldres=old['hq_reservation']
 need(abs(area(reserve['polygon'])-area(oldres['polygon']))<1e-5,'HQ reservation area changed')
 need(gap(reserve['polygon'],g.footprint(bs['stables']))<=8,'HQ reservation not beside Guild')
 for i,u in enumerate(reserve['upgrades']):
  ou=next(v for v in oldres['upgrades'] if v['id']==u['id'])
  need({k:v for k,v in u.items() if k!='polygon'}=={k:v for k,v in ou.items() if k!='polygon'},'HQ upgrade metadata '+u['id'])
  need(abs(area(u['polygon'])-area(ou['polygon']))<1e-5 and all(g.inside(v,reserve['polygon']) for v in u['polygon']),'HQ parcel bounds '+u['id'])
  need(not any(overlap(u['polygon'],v['polygon']) for v in reserve['upgrades'][i+1:]),'HQ parcel overlap')
 # Three-sided court: north businesses, west tavern, south provisions; tree on open ground.
 court=cs['red_tree_court']['court_polygon']
 # Enclosure is measured in the group's local frame after rotating the court.
 from geometry_v7b import transform
 c=cs['red_tree_court'];pivot=c['v7b_pivot'];yaw=c['frontage_yaw_deg']
 local=lambda pt:transform(pt,[pivot[0]-1,pivot[1]],-yaw,[1,0])
 x,z,X,Z=bounds([local(pt) for pt in court])
 sidebounds={id:bounds([local(pt) for pt in g.footprint(bs[id])]) for id in c['building_ids']}
 need(sidebounds['tavern'][2]<=x+.6 and sidebounds['provisions'][1]>=Z-.6 and all(sidebounds[id][3]<=z+.6 for id in ('infill_home_12','street_home_8')),'red-tree three-sided enclosure')
 for a,poly in props:
  if a.get('cluster_location')=='red_tree_court':need(all(g.inside(v,court) for v in poly),'market stall outside court '+a['id'])
 # Retain appointment space and the longitudinal clock view.
 plaza=next(s['polygon'] for s in p['squares'] if s['id']=='clock_plaza')
 need(plaza==next(s['polygon'] for s in old['squares'] if s['id']=='clock_plaza'),'clock plaza moved')
 for id,poly in ss:
  if id!='watch_tower':need(not overlap(poly,plaza),'clock plaza occupied '+id)
 for a,poly in props:need(not overlap(poly,plaza),'clock plaza prop '+a['id'])
 figs=[m for m in p['markers'] if m['id'].startswith('civic_terrace/') and m.get('kind')!='camera_hint']
 need(len(figs)==12,'civic figure count')
 metrics['civic_min_body_clearance_m']=round(min(math.dist(a['position'],b['position'])-.5 for i,a in enumerate(figs) for b in figs[i+1:]),3)
 need(metrics['civic_min_body_clearance_m']>=1.2,'civic body clearance')
 sight=next(s for s in p['sightlines'] if s['id']=='bridge_to_clock')
 for id,poly in ss:
  if id=='watch_tower':continue
  for i in range(301):
   t=i/300;pt=[sight['from_xz'][j]+t*(sight['target_xz'][j]-sight['from_xz'][j]) for j in (0,1)]
   y=sight['eye_y_m']+t*(sight['target_y_m']-sight['eye_y_m'])
   if g.inside(pt,poly):need(y>bs[id]['ground_y_m']+bs[id]['height_m']+bs[id]['roof_height_m'],'clock sightline blocked '+id);break
 for tree in p['green']['trees']:
  a,b=sight['from_xz'],sight['target_xz'];dx,dz=b[0]-a[0],b[1]-a[1];pt=tree['position'];t=max(0,min(1,((pt[0]-a[0])*dx+(pt[1]-a[1])*dz)/(dx*dx+dz*dz)))
  if g.distance(pt,a,b)<tree['canopy_radius_m']:need(sight['eye_y_m']+t*(sight['target_y_m']-sight['eye_y_m'])>tree.get('ground_y_m',0)+tree['height_m'],'clock sightline tree '+tree['id'])
 # Guild processing, bench circle, envoy and resting locations move together.
 oldmarks={m['id']:m for m in old['markers']}
 guild=[m for m in p['markers'] if m.get('place_binding')=='guild_compound']
 for m in guild:
  om=oldmarks[m['id']];need(math.dist(m['position'],[om['position'][0],om['position'][1]-175])<1e-5 and m['height_m']==.6,'Guild staging relation '+m['id'])
 bench=next(a for a in p['props'] if a['id']=='equipment_bench')['position']
 need(ms['city/bench_east']['position'][0]>bench[0] and ms['city/bench_west']['position'][0]<bench[0] and ms['city/bench_south']['position'][1]>bench[1],'Guild bench orientation')
 stage=next(z['polygon'] for z in p['ground_zones'] if z['id']=='courtyard_staging')
 for m in p['markers']:
  if m.get('rest_spot'):
   poly=g.boxpoly(m['footprint']);need(all(g.inside(v,stage) for v in poly),'rest footprint outside Guild')
   need(not any(overlap(poly,s) for id,s in ss) and not any(overlap(poly,s) for a,s in props) and not any(overlap(poly,s) for r,s in routes),'rest body blocked '+m['id'])
   need(any(z['material']=='grass' and all(g.inside(v,z['polygon']) for v in poly) for z in p['ground_zones']),'rest grass missing')
 for m in p['markers']:
  if m['scene']!='city':continue
  need(all(math.dist(m['position'],t['position'])>=.25+t['trunk_collision_radius_m'] for t in p['green']['trees']),'marker tree clearance '+m['id'])
  # Use a route/deck at the point when present, else highest-priority ground.
  heights=[g.segheight(r,i,m['position']) for r,i,a,b in g.segments(p) if g.distance(m['position'],a,b)<1e-5]
  if not heights:
   zones=[z for z in p['ground_zones'] if g.inside(m['position'],z['polygon'])]
   if zones:heights=[max(zones,key=lambda z:z.get('priority',0))['height_m']]
  need(bool(heights) and min(abs(m['height_m']-h) for h in heights)<.015,'marker ground height '+m['id'])
 # Named greens are disjoint and never occupy cluster seams, routes or reserves.
 greens=[]
 for s in p['green'].get('spaces',[]):
  for poly in s['polygons']:
   need(all(g.inside(v,p['extent']) for v in poly),'green outside extent '+s['id'])
   need(not any(overlap(poly,a) for id,a in ss),'green overlaps building '+s['id'])
   need(not any(overlap(poly,a) for r,a in routes),'green overlaps route '+s['id'])
   need(not overlap(poly,reserve['polygon']),'green occupies HQ '+s['id'])
   if s['kind']=='intercluster_garden':
    for c in p['clusters']:
     from geometry_v7b import hull
     pts=[v for id in c['building_ids'] for v in g.footprint(bs[id])]+c.get('court_polygon',[])
     need(not overlap(poly,hull(pts)),'lawn inside cluster '+s['id'])
   need(not any(overlap(poly,a) for _,a in greens),'green area double-count '+s['id'])
   greens.append((s['id'],poly))
 for z in p['ground_zones']:
  if z['material'] in ('grass','grass_earth'):
   need(z.get('named_green_space') and any(z['polygon']==poly for id,poly in greens),'unnamed lawn surface '+z['id'])
 for z in p['green'].get('lawns',[]):need(any(z['polygon']==poly for id,poly in greens),'stale lawn polygon '+z['id'])
 need(not p['green']['hedges'],'stale v5 hedge geometry')
 for a,poly in props:
  need(all(g.inside(v,p['extent']) for v in poly),'prop outside extent '+a['id'])
  if a['id'].startswith('workshop_'):need(all(g.inside(v,ds['workshops']['bounds']) for v in poly),'workshop prop district '+a['id'])
  if a['id'].startswith('quays_'):need(all(g.inside(v,ds['quays']['bounds']) for v in poly),'quay prop district '+a['id'])
 # Allotment layout translates rigidly: this preserves all bed/aisle dimensions.
 allot=[a for a in p['props'] if a['id'].startswith('allotment_')];op={a['id']:a for a in old['props']}
 for a in allot:
  need(all(abs(v-w-d)<1e-5 for v,w,d in zip(a['footprint'],op[a['id']]['footprint'],[82,-62,82,-62])),'allotment internal layout '+a['id'])
 gate=next(a for a in allot if a['id']=='allotment_gate');need(gate['opening_position']==[141,39] and gate['clear_width_m']==3,'allotment gate binding')
 if full:
  # 1.2 m body corridor on a 0.5 m lattice from the gate into every bed aisle.
  obstacles=[poly for a,poly in props if a['id'].startswith('allotment_')]
  def clear(pt):return not any(g.inside(pt,poly) or min(g.distance(pt,a,b) for a,b in g.edges(poly))<.6-1e-5 for poly in obstacles)
  start=(280,78);todo=[start];seen={start}
  while todo:
   x,z=todo.pop()
   for q in ((x+1,z),(x-1,z),(x,z+1),(x,z-1)):
    if q in seen or not(223<=q[0]<=282 and 24<=q[1]<=104) or not clear([q[0]/2,q[1]/2]):continue
    seen.add(q);todo.append(q)
  for a in allot:
   if 'fence' in a['id'] or a['id']=='allotment_gate':continue
   poly=g.boxpoly(a['footprint']);need(any(min(g.distance([x/2,z/2],v,w) for v,w in g.edges(poly))<=1.5 for x,z in seen),'allotment aisle unreachable '+a['id'])
  metrics['allotment_reachable_half_m_cells']=len(seen)
  basewalk=copy.deepcopy(old);walk=old['walk_time']
  for pt in (walk['start'],walk['finish']):
   for r in basewalk['routes']:
    for i,(a,b) in enumerate(zip(r['centreline'],r['centreline'][1:])):
     if g.distance(pt,a,b)<1e-6 and pt!=a and pt!=b:
      h=g.segheight(r,i,pt);r['centreline'].insert(i+1,pt);r['heights_m'].insert(i+1,h);break
  oldgraph,_=g.graph(basewalk);oldlength=g.shortest(oldgraph,g.key(walk['start']))[g.key(walk['finish'])]
  metrics.update(v5_gate_market_walk_m=round(oldlength,3),v5_gate_market_walk_s=round(oldlength/walk['speed_m_s'],3))
 pop=[b for b in old['buildings'] if b['id'] not in ('south_gate','watch_tower')]
 before=[min(gap(g.footprint(b),g.footprint(c)) for c in old['buildings'] if c['id']!=b['id']) for b in pop]
 after=[min(gap(g.footprint(b),g.footprint(c)) for c in p['buildings'] if c['id']!=b['id']) for b in p['buildings'] if b['id'] not in ('south_gate','watch_tower')]
 metrics.update(v5_all_nearest_median_m=round(statistics.median(before),4),v7_all_nearest_median_m=round(statistics.median(after),4),v5_nonlandmarks_with_neighbour_at_2m=sum(d<=2+1e-5 for d in before),v7_nonlandmarks_with_neighbour_at_2m=sum(d<=2+1e-5 for d in after),nonlandmark_population_before=len(before),nonlandmark_population_after=len(after),trees=len(p['green']['trees']),named_green_spaces=len(p['green']['spaces']),extent_area_m2=area(p['extent']),v5_extent_area_m2=area(old['extent']),building_area_m2=sum(area(g.footprint(b)) for b in p['buildings']),v5_building_area_m2=sum(area(g.footprint(b)) for b in old['buildings']),north_green_area_m2=sum(area(poly) for s in p['green']['spaces'] for poly in s['polygons'] if max(v[1] for v in poly)<-40))
 metrics['v5_gate_river_m']=round(next(b['footprint'][1] for b in old['buildings'] if b['id']=='south_gate')-max(z for x,z in old['river']['polygon']),3)
 return errors,metrics

