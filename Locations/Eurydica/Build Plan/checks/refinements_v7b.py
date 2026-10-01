"""Additional measured v7b acceptance, including explicit negative controls."""
import sys,json,math,statistics,copy
from pathlib import Path
sys.dont_write_bytecode=True
from PIL import Image,ImageDraw
import numpy as np
import inherited_checks as g
from geometry_v7b import overlap,area,bounds,hull
R=Path(__file__).resolve().parent
V=json.loads((R/'eurydica-plan.json').read_bytes())

def length(r):return sum(math.dist(a,b) for a,b in zip(r['centreline'],r['centreline'][1:]))

def mask(polys,scale=5):
 im=Image.new('1',(int(270*scale),int(280*scale)));d=ImageDraw.Draw(im)
 for poly in polys:d.polygon([((x+120)*scale,(z+140)*scale) for x,z in poly],fill=1)
 return np.asarray(im)

def roadmetrics(p):
 # Include bridge, deck, ramps, alleys and door spurs in BOTH versions.
 polys=[g.strip(a,b,r['width_m']) for r,i,a,b in g.segments(p)]
 return dict(length_m=round(sum(length(r) for r in p['routes']),3),
  summed_strip_area_m2=round(sum(length(r)*r['width_m'] for r in p['routes']),2),
  union_area_m2=round(float(mask(polys,10).sum())/100,2),union_sample_m=.1,
  routes=len(p['routes']),door_length_m=round(sum(length(r) for r in p['routes'] if r.get('owner')),3))

def validate(p,full=True):
 errors=[];m={}
 def need(ok,msg):
  if not ok:errors.append(msg)
 b={b['id']:b for b in p['buildings']};vb={b['id']:b for b in V['buildings']}
 need([c['id'] for c in p['clusters']]==[c['id'] for c in V['clusters']],'v7b cluster list/order changed')
 for c,o in zip(p['clusters'],V['clusters']):
  need(c['building_ids']==o['building_ids'],'v7b cluster membership changed '+c['id'])
  centre=lambda ids,bs:[statistics.mean((bs[id]['footprint'][i]+bs[id]['footprint'][i+2])/2 for id in ids) for i in (0,1)]
  need(math.dist(centre(c['building_ids'],b),centre(o['building_ids'],vb))<=5,'v7b cluster displaced '+c['id'])
 for key in ('river','bridge','waterworks','camera','interiors','hq_reservation'):
  need(p[key]==V[key],'v7b protected baseline '+key)
 for c in V['terrain']['terraces']:
  if c['id'] not in ('south','company_platform'):need(c in p['terrain']['terraces'],'v7b north terrace moved')
 need(p['status']=='candidate' and p['plan_revision']=='v7b','v7b candidate/revision')
 groups={r.get('branch_group') for r in p['routes'] if r.get('branch_group')}
 need(groups=={'guild_gate','arrival_courts','service','workshops_quays','north_bank'},'v7b five branch groups')
 for r in p['routes']:
  if r.get('branch_group') and r['id'] not in ('civic_approach','civic_old_ramp','civic_res_ramp'):need(4<=r['width_m']<=5,'v7b branch width '+r['id'])
  if r.get('owner') or r['kind']=='alley':need(2<=r['width_m']<=3,'v7b alley width '+r['id'])
 main=next(r for r in p['routes'] if r['id']=='main_road')
 need(main['centreline'][0]==[0,118] and main['centreline'][-1]==[0,-5] and 6<=main['width_m']<=8,'v7b gate bridge main road')
 need(max(x for x,z in main['centreline'])-min(x for x,z in main['centreline'])>=4,'v7b gently winding road missing')
 before=roadmetrics(V);after=roadmetrics(p)
 m['roads_before']=before;m['roads_after']=after
 m['road_length_reduction_percent']=round((1-after['length_m']/before['length_m'])*100,2)
 m['road_area_reduction_percent']=round((1-after['union_area_m2']/before['union_area_m2'])*100,2)
 need(after['length_m']<before['length_m']*.85,'v7b insufficient road length reduction')
 need(after['union_area_m2']<before['union_area_m2']*.85,'v7b insufficient road area reduction')
 lengths=[length(r) for r in p['routes'] if r.get('owner')]
 m['door_spur_max_m']=round(max(lengths),3);m['door_spur_median_m']=round(statistics.median(lengths),3)
 need(max(lengths)<=22,'v7b door spur too long')
 need(statistics.median(lengths)<=7,'v7b typical door spur too long')
 # Perimeter exposure: compare non-door road proximity at front/back hull edges.
 # Check the removed loop geometry explicitly; misleading legacy IDs are allowed.
 for id in ('service_public_loop','old_park'):
  n=next(r for r in p['routes'] if r['id']==id);o=next(r for r in V['routes'] if r['id']==id)
  need(length(n)<length(o)*.85,'v7b perimeter lane retained '+id)
 need(not any(r['id']=='residential_link' for r in p['routes']),'v7b extra residential ring retained')
 if full:
  graph,_=g.graph(p);adj={v:sorted(set(q for q,_,_ in es),key=lambda q:math.atan2(q[1]-v[1],q[0]-v[0])) for v,es in graph.items()}
  visited=set();faces=[]
  for u in adj:
   for v in adj[u]:
    if (u,v) in visited:continue
    a,bp=u,v;face=[]
    for _ in range(len(graph)*4):
     if (a,bp) in visited:break
     visited.add((a,bp));face.append(list(a));neighbours=adj[bp]
     a,bp=bp,neighbours[(neighbours.index(a)-1)%len(neighbours)]
     if (a,bp)==(u,v):break
    signed=sum(a[0]*bp[1]-a[1]*bp[0] for a,bp in g.edges(face))/2 if len(face)>2 else 0
    if signed>1:faces.append(face)
  m['bounded_route_faces']=len(faces)
  for c in p['clusters']:
   centres=[[(b[id]['footprint'][i]+b[id]['footprint'][i+2])/2 for i in (0,1)] for id in c['building_ids']]
   need(not any(all(g.inside(pt,face) for pt in centres) for face in faces),'v7b road ring encloses cluster '+c['id'])
 yaws=[v.get('yaw_deg',0) for v in b.values() if v['id'] not in ('south_gate','watch_tower')]
 need(len(set(yaws))>=5 and sum(v!=0 for v in yaws)>=len(yaws)*.75,'v7b stagger/angle variety missing')
 need(all(abs(v/5-round(v/5))<1e-6 for v in yaws),'v7b angles are not 5 degree steps')
 m['building_yaws_deg']=sorted(set(yaws));m['angled_nonlandmarks']=sum(v!=0 for v in yaws)
 groves=[poly for s in p['green']['spaces'] if s['kind']=='intercluster_garden' for poly in s['polygons']]
 def irregular(poly):
  x,z,X,Z=bounds(poly);return 1-area(poly)/((X-x)*(Z-z))
 def concave(poly):return area(poly)/area(hull(poly))<.99
 m['green_irregularity']={'definition':'1 - polygon area / axis-aligned bounding-box area; 0 means rectangle',
  'before_mean':round(statistics.mean(irregular(poly) for s in V['green']['spaces'] if s['kind']=='intercluster_garden' for poly in s['polygons']),4),
  'after_mean':round(statistics.mean(map(irregular,groves)),4) if groves else 0,
  'concave_groves':sum(map(concave,groves)),'groves':len(groves)}
 need(len(groves)>=18 and m['green_irregularity']['after_mean']>=.2 and sum(map(concave,groves))>=len(groves)*.7,'v7b organic green shapes missing')
 cover=p['green'].get('continuous_cover',{})
 need(cover.get('material')=='grass' and cover.get('operation')=='union(domains) minus union(exclusions)','v7b continuous intercluster green missing')
 if cover:
  domain=mask([d['polygon'] for d in cover['domains']]);exclusion=mask(cover['exclusions'])
  grass=domain & ~exclusion
  m['continuous_intercluster_green_m2']=round(float(grass.sum())/25,2)
  # Reconstruct all non-green uses independently. Any non-green unexplained gap fails.
  expected=[c['ground_envelope'] for c in p['clusters']]
  expected += [g.strip(a,b,r['width_m']) for r,i,a,b in g.segments(p)]
  expected += [g.boxpoly(a['footprint']) for a in p['props'] if 'footprint' in a]
  for a in p['props']:
   if 'position' in a:
    x,z=a['position'];r=a.get('collision_radius_m',.25);expected.append(g.boxpoly([x-r,z-r,x+r,z+r]))
  expected += [p['hq_reservation']['polygon'],p['waterworks']['feeder_polygon']]+[t['polygon'] for t in p['terrain']['cliffs']]+[s['polygon'] for s in p['squares']]
  expected += [a['polygon'] for a in p['workshop_piles']]+[p['workshop_clear_court']]
  expected += [z['polygon'] for z in p['ground_zones'] if z['id'] in ('courtyard_staging','spine_service_allotments')]
  # The land domain is reconstructed from the actual base ground, not trusted
  # from the author's cover list (which could itself omit an entire region).
  land=mask([z['polygon'] for z in p['ground_zones'] if z['id'] in ('south_base','north_base')])
  bare=land & ~mask(expected) & ~grass
  m['unassigned_intercluster_gap_m2']=round(float(bare.sum())/25,2)
  need(not bare.any(),'v7b bare intercluster gap')
 points=[t['position'] for t in p['green']['trees'] if t['id']!='tree_08']
 nn=[min(math.dist(a,b) for j,b in enumerate(points) if j!=i) for i,a in enumerate(points)]
 m['tree_spacing_cv']=round(statistics.pstdev(nn)/statistics.mean(nn),4)
 need(m['tree_spacing_cv']>.1,'v7b regular tree grid')
 piles=p.get('workshop_piles',[]);need(3<=len(piles)<=4,'v7b workshop pile count')
 assigned=[id for a in piles for id in a['prop_ids']]
 need(len(assigned)==len(set(assigned)) and set(assigned)=={a['id'] for a in p['props'] if a['id'].startswith('workshop_')},'v7b workshop pile coverage')
 for a in piles:
  for id in a['prop_ids']:
   prop=next(q for q in p['props'] if q['id']==id)
   need(all(g.inside(v,a['polygon']) for v in g.boxpoly(prop['footprint'])),'v7b prop outside pile '+id)
   need(not overlap(g.boxpoly(prop['footprint']),p['workshop_clear_court']),'v7b workshop court blocked '+id)
   from check_plan_v7b import gap
   need(min(gap(g.boxpoly(prop['footprint']),g.footprint(q)) for q in p['buildings'] if q['cluster_id']=='workshop_yard')<=3.5,'v7b workshop stock away from buildings '+id)
 need(area(p['workshop_clear_court'])>=70,'v7b working court too small')
 screen=p.get('hq_screen',{});need(screen.get('kind')=='hedge_and_timber_fence' and screen.get('reserve_remains_unbuilt'),'v7b HQ screen missing')
 need(sum(t.get('space_id')=='hq_edge' for t in p['green']['trees'])>=3,'v7b HQ edge trees missing')
 for line in screen.get('polylines',[]):
  for a,bp in zip(line,line[1:]):
   poly=g.strip(a,bp,screen['width_m'])
   need(not overlap(poly,p['hq_reservation']['polygon']),'v7b screen occupies reserve')
   need(not any(overlap(poly,g.strip(a,bp,r['width_m'])) for r,i,a,bp in g.segments(p)),'v7b screen blocks route')
   need(not any(overlap(poly,g.footprint(b)) for b in p['buildings']),'v7b screen hits building')
 return errors,m

def controls(p):
 tests=[]
 for name,mutate,token in [
  ('lost membership',lambda q:q['clusters'][1]['building_ids'].pop(),'cluster membership'),
  ('all axis aligned',lambda q:[b.update(yaw_deg=0) for b in q['buildings']],'angle variety'),
  ('extra long road',lambda q:q['routes'].append(dict(id='control',centreline=[[120,0],[120,600]],width_m=5,kind='street')),'road length'),
  ('missing meadow',lambda q:q['green'].pop('continuous_cover'),'continuous intercluster'),
  ('omitted north meadow region',lambda q:q['green']['continuous_cover'].update(domains=[d for d in q['green']['continuous_cover']['domains'] if d['id']!='north_base_meadow']),'bare intercluster'),
  ('missing HQ screen',lambda q:q.pop('hq_screen'),'HQ screen'),
  ('missing stock station',lambda q:q['workshop_piles'].pop(),'pile coverage')]:
  q=copy.deepcopy(p);mutate(q);errors,_=validate(q,False)
  assert any(token in e for e in errors),(name,errors);tests.append(name)
 return tests
