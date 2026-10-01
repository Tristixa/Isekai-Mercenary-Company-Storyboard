"""Continuous intercluster meadow, flowing grove polygons and non-grid trees."""
import math,random,copy
import inherited_checks as g
from geometry_v7b import bounds,overlap,hull

def build(p,v):
 # Named rest beds, red tree and allotments survive; rectangular grove fills go.
 keep={'red_tree_bed','spine_service_allotments'}
 oldspaces=[s for s in v['green']['spaces'] if s['kind']!='intercluster_garden']
 keep.update(s['id'] for s in oldspaces)
 p['ground_zones']=[z for z in p['ground_zones'] if not z.get('named_green_space') or z['id'] in keep]
 p['green']['spaces']=[];p['green']['lawns']=[]
 for s in oldspaces:
  s=copy.deepcopy(s)
  if s['id']=='red_tree_bed':s['polygons']=[next(z['polygon'] for z in p['ground_zones'] if z['id']=='red_tree_bed')]
  p['green']['spaces'].append(s)
  for i,poly in enumerate(s['polygons']):p['green']['lawns'].append(dict(id=s['id']+'_'+str(i),polygon=poly))
 envelopes=[]
 for c in p['clusters']:
  pts=[pt for b in p['buildings'] if b['id'] in c['building_ids'] for pt in g.footprint(b)]+c.get('court_polygon',[])
  poly=hull(pts);c['ground_envelope']=poly
  envelopes.append(poly)
 props=[]
 for a in p['props']:
  if 'footprint' in a:props.append(g.boxpoly(a['footprint']))
  elif 'position' in a:
   x,z=a['position'];r=a.get('collision_radius_m',.25);props.append(g.boxpoly([x-r,z-r,x+r,z+r]))
 roads=[g.strip(a,b,r['width_m']) for r,i,a,b in g.segments(p)]
 excludes=envelopes+roads+props+[p['hq_reservation']['polygon'],p['waterworks']['feeder_polygon']]+[t['polygon'] for t in p['terrain']['cliffs']]+[s['polygon'] for s in p['squares']]
 # Work stations and the central court are used ground, not leftover bare gaps.
 excludes += [a['polygon'] for a in p['workshop_piles']]+[p['workshop_clear_court']]
 excludes += [z['polygon'] for z in p['ground_zones'] if z['id'] in ('courtyard_staging','spine_service_allotments')]
 domains=[{'id':'south_meadow','polygon':p['south_bank_boundary'],'height_m':0}]
 north=next(z for z in p['ground_zones'] if z['id']=='north_base')
 domains.append({'id':'north_base_meadow','polygon':north['polygon'],'height_m':north['height_m']})
 for t in p['terrain']['terraces']:
  if t['id'] not in ('south','company_platform'):domains.append({'id':t['id']+'_meadow','polygon':t['polygon'],'height_m':t['height_m']})
 # Boolean ground polygons avoid lossy cell rectangles or thousands of triangles.
 # Within domains, everything outside listed solid/court/route masks is grass.
 p['green']['continuous_cover']={'material':'grass','operation':'union(domains) minus union(exclusions)',
  'domains':domains,'exclusions':excludes,'walkable':True,'priority':1,
  'purpose':'All intercluster gaps are meadow; dense organic groves are a planting layer over it.'}
 blockers=excludes+[p['river']['polygon']]
 for m in p['markers']:
  if m['scene']=='city':
   x,z=m['position'];blockers.append(g.boxpoly([x-1,z-1,x+1,z+1]))
 block_bounds=[(a,bounds(a)) for a in blockers]
 def ground(pt):
  ts=[d for d in domains if g.inside(pt,d['polygon'])]
  return ts[-1]['height_m'] if ts else None
 def valid(pt,margin=0):
  if ground(pt) is None or not g.inside(pt,p['extent']):return False
  x,z=pt
  return not any(g.inside(pt,a) or margin and min(g.distance(pt,v,w) for v,w in g.edges(a))<margin for a,(u,v,U,V) in block_bounds if u-margin<=x<=U+margin and v-margin<=z<=V+margin)
 occupied=[];rng=random.Random(717)
 for old in v['green']['spaces']:
  if old['kind']!='intercluster_garden':continue
  x,z,X,Z=bounds([v for poly in old['polygons'] for v in poly]);cx,cz=(x+X)/2,(z+Z)/2
  candidates=[[cx,cz]]+[[rng.uniform(x,X),rng.uniform(z,Z)] for _ in range(40)]
  free=[pt for pt in candidates if valid(pt,1)]
  if not free:continue
  centre=max(free,key=lambda p:min(min(g.distance(p,a,b) for a,b in g.edges(poly)) for poly in blockers))
  poly=[]
  for k in range(36):
   a=2*math.pi*k/36;cap=8+5*(1+math.sin(3*a+.7))/2+4*(1+math.sin(5*a+1.2))/2
   dist=1
   while dist<cap:
    pt=[centre[0]+math.cos(a)*dist,centre[1]+math.sin(a)*dist]
    if not valid(pt,.6) or any(g.inside(pt,p) for p in occupied):break
    dist+=.7
   radius=max(.5,dist-1)
   poly.append([centre[0]+math.cos(a)*radius,centre[1]+math.sin(a)*radius])
  poly=[pt for a,b in g.edges(poly) for pt in ([.75*a[i]+.25*b[i] for i in (0,1)],[.25*a[i]+.75*b[i] for i in (0,1)])]
  for _ in range(15):
   if not any(overlap(poly,b) for b in blockers+occupied):break
   poly=[[centre[i]+(v[i]-centre[i])*.92 for i in (0,1)] for v in poly]
  else:continue
  occupied.append(poly)
  s=dict(id=old['id'],name=old['name'],district=old.get('district'),kind='intercluster_garden',polygons=[poly],ground_y_m=ground(centre))
  p['green']['spaces'].append(s)
  p['ground_zones'].append(dict(id=s['id']+'_organic',polygon=poly,material='grass',height_m=s['ground_y_m'],priority=6,walkable=True,blend_width_per_edge_m=[.6]*len(poly),named_green_space=True,green_space_id=s['id']))
  p['green']['lawns'].append(dict(id=s['id']+'_organic',polygon=poly))
 # Blue-noise rejection sampling: varying minimum spacing, no planting lattice.
 # Trees occur throughout the meadow and individually beside frontages/roads.
 candidates=[]
 for _ in range(1800):candidates.append([rng.uniform(-111,128),rng.uniform(-117,122)])
 for pt in candidates:
  radius=rng.uniform(1.65,2.5)
  if not valid(pt,radius+.25):continue
  if any(math.dist(pt,t['position'])<rng.uniform(4.5,7) for t in p['green']['trees']):continue
  if abs(pt[0])<7 and pt[1]<-40:continue # retained bridge-clock view
  space=next((s['id'] for s in p['green']['spaces'] if any(g.inside(pt,a) for a in s['polygons'])),'intercluster_meadow')
  p['green']['trees'].append(dict(id='v7b_tree_'+str(len(p['green']['trees'])),position=pt,type='tree-broad',height_m=rng.uniform(4,6.8),ground_y_m=ground(pt),canopy_radius_m=radius,trunk_collision_radius_m=.25,palette='green',space_id=space))
 # Reserve edge trees grow outside the future construction parcels.
 x,z,X,Z=bounds(p['hq_reservation']['polygon'])
 for i,pt in enumerate([[x-3,z+4],[x-3,z+11],[x-3,z+19],[(x+X)/2,z-3],[X-3,z-3]]):
  if valid(pt,.6) and not any(math.dist(pt,t['position'])<3 for t in p['green']['trees']):
   p['green']['trees'].append(dict(id='hq_edge_tree_'+str(i),position=pt,type='tree-broad',height_m=5,ground_y_m=ground(pt),canopy_radius_m=1.8,trunk_collision_radius_m=.25,palette='green',space_id='hq_edge'))
