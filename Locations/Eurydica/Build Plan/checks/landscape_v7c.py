"""Rebuild meadow masks and plant overlapping canopy groves with open intervals."""
import math,random,copy
import inherited_checks as g
from geometry_v7b import bounds,overlap,hull
def build(p,v):
 from landscape_v7b import build as baseline
 # Baseline rebuilds organic green boundaries against the changed routes.
 source=copy.deepcopy(v)
 yard=next(s for s in p['green']['spaces'] if s['id']=='spine_service_allotments')
 next(s for s in source['green']['spaces'] if s['id']=='spine_service_allotments')['polygons']=copy.deepcopy(yard['polygons'])
 p['green']['trees']=[copy.deepcopy(next(t for t in v['green']['trees'] if t['id']=='tree_08'))]
 baseline(p,source)
 cover=p['green']['continuous_cover'];cover['exclusions']+=[p['storeyard_edge']['polygon']]
 blockers=cover['exclusions']+[p['river']['polygon']]
 for m in p['markers']:
  if m['scene']=='city':
   x,z=m['position'];blockers.append(g.boxpoly([x-1,z-1,x+1,z+1]))
 bb=[(a,bounds(a)) for a in blockers]
 def ground(pt):
  domains=[d for d in cover['domains'] if g.inside(pt,d['polygon'])]
  return domains[-1]['height_m'] if domains else None
 def valid(pt,margin=1):
  x,z=pt
  if ground(pt) is None or not g.inside(pt,p['extent']) or abs(x)<6 and z<-40:return False
  return not any(g.inside(pt,a) or min(g.distance(pt,u,v) for u,v in g.edges(a))<margin for a,(u,v,U,V) in bb if u-margin<=x<=U+margin and v-margin<=z<=V+margin)
 oldtrees=p['green']['trees'];p['green']['trees']=[oldtrees[0]];rng=random.Random(7303)
 groves=[];centres=[]
 candidates=[[rng.uniform(-108,126),rng.uniform(-116,120)] for _ in range(1400)]
 # Broad clearings first. Groves occupy a compact footprint, leaving a meadow belt.
 candidates=[pt for pt in candidates if valid(pt,3)]
 rng.shuffle(candidates)
 for centre in candidates:
  if any(math.dist(centre,c)<19 for c in centres):continue
  pts=[];target=rng.randint(12,22)
  for _ in range(400):
   a=rng.uniform(0,2*math.pi);rad=6.7*math.sqrt(rng.random());pt=[centre[0]+rad*math.cos(a),centre[1]+rad*.85*math.sin(a)]
   if not valid(pt,1.3) or any(math.dist(pt,q)<1.7 for q in pts) or any(math.dist(pt,t['position'])<2 for t in p['green']['trees']):continue
   # A connected overlapping canopy component, not a nominal group of singles.
   if pts and min(math.dist(pt,q) for q in pts)>4:continue
   pts.append(pt)
   if len(pts)>=target:break
  if len(pts)<8:continue
  gid='grove_v7c_'+str(len(groves)+1);ids=[];centres.append(centre)
  for pt in pts:
   id='v7c_tree_'+str(len(p['green']['trees']));ids.append(id)
   p['green']['trees'].append(dict(id=id,position=pt,type='tree-broad',height_m=rng.uniform(4.4,6.5),ground_y_m=ground(pt),canopy_radius_m=rng.uniform(2.2,2.7),trunk_collision_radius_m=.25,palette='green',space_id=gid,grove_id=gid))
  groves.append(dict(id=gid,tree_ids=ids,centre=centre,canopy_envelope=hull([[pt[0]+2.5*math.cos(i*math.pi/4),pt[1]+2.5*math.sin(i*math.pi/4)] for pt in pts for i in range(8)])))
  if len(groves)>=25:break
 # A few existing accent trees survive at the HQ screen and along the main road.
 accents=[t for t in oldtrees if t.get('space_id')=='hq_edge']
 accents += [t for t in oldtrees if abs(t['position'][0])<12 and 0<t['position'][1]<110][:4]
 for t in accents:
  if valid(t['position'],.7) and all(math.dist(t['position'],q['position'])>3 for q in p['green']['trees']):p['green']['trees'].append(t)
 # Small planted island beside the tower: pavement surrounds it, staging stays clear.
 for i,pt in enumerate([[9,-72.7],[9.5,-70.2]]):
  p['green']['trees'].append(dict(id='civic_tree_v7c_'+str(i),position=pt,type='tree-broad',height_m=4,ground_y_m=2,canopy_radius_m=1.5,trunk_collision_radius_m=.25,palette='green',space_id='civic_green_east'))
 p['green']['groves']=groves
 p['green']['planting_note']='Dense clumps of 8-25 overlapping canopies; continuous open meadow between compact groves; sparse frontage accents.'
