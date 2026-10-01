"""Named intercluster gardens, clipped in 2 m cells then merged into rectangles.

These are planting regions, never per-building lawn pads. Reported areas are
the exact sum of disjoint rectangles, not the unclipped design envelopes.
"""
import math, random
import inherited_checks as g

def build(p):
 from check_plan import overlap, bounds
 p['green']['hedges']=[]
 p['green']['lawns']=[]
 p['green']['spaces']=[]
 blockers=[g.footprint(b) for b in p['buildings']]
 # A whole group and its court exclude planting, including its narrow seams.
 for c in p['clusters']:
  pts=[v for b in p['buildings'] if b['id'] in c['building_ids'] for v in g.footprint(b)]
  if 'court_polygon' in c:pts+=c['court_polygon']
  blockers.append(g.boxpoly(bounds(pts)))
 blockers += [g.strip(a,b,r['width_m']+1) for r,i,a,b in g.segments(p)]
 blockers += [p['river']['polygon'],p['waterworks']['feeder_polygon'],p['hq_reservation']['polygon']]
 blockers += [t['polygon'] for t in p['terrain']['cliffs']]
 for a in p['props']:
  if 'footprint' in a:blockers.append(g.boxpoly(a['footprint']))
  elif 'position' in a:
   x,z=a['position'];blockers.append(g.boxpoly([x-1,z-1,x+1,z+1]))
 for m in p['markers']:
  if m['scene']=='city':
   x,z=m['position'];blockers.append(g.boxpoly([x-1,z-1,x+1,z+1]))
 occupied=[]
 regions=[
 ('old_city_orchard','Old City communal orchard',[-100,-87,-59,-63],'old_city'),
 ('old_city_river_grove','Old City river grove',[-99,-58,-59,-42],'old_city'),
 ('old_city_east_garden','Old City terrace gardens',[-53,-115,-33,-66],'old_city'),
 ('civic_east_garden','Civic east garden',[11,-98,28,-66],'civic'),
 ('civic_west_garden','Civic west garden',[-28,-98,-22,-67],'civic'),
 ('civic_river_gardens','Civic river gardens',[-28,-56,28,-42],'civic'),
 ('residential_grove','Residential shared grove',[33,-79,99,-64],'residential'),
 ('residential_court_garden','Between the residential courts',[53,-115,61,-93],'residential'),
 ('waterworks_east_orchard','Waterworks orchard',[113,-115,127,-57],'waterworks'),
 ('north_east_bank','North riverbank gardens',[33,-49,102,-42],'residential'),
 ('quay_orchard_buffer','Quay and orchard buffer',[-65,25,-46,33],'arrival'),
 ('west_wall_grove','West wall grove',[-110,100,-82,121],'company'),
 ('arrival_shared_garden','Arrival shared garden',[-39,45,-11,54],'arrival'),
 ('arrival_west_garden','West arrival garden',[-63,62,-44,84],'arrival'),
 ('arrival_south_garden','Arrival and Guild garden',[-40,90,-12,97],'arrival'),
 ('arrival_east_orchard','Arrival east orchard',[60,61,72,95],'arrival'),
 ('arrival_market_garden','Between market and arrival',[29,49,60,67],'arrival'),
 ('market_east_grove','Market and service grove',[63,13,71,45],'market'),
 ('market_north_garden','Bridge-side garden',[32,-7,64,10],'market'),
 ('service_north_orchard','Service north orchard',[74,-7,126,9],'service'),
 ('service_court_garden','Service court garden',[74,42,101,57],'service'),
 ('service_south_orchard','Service south orchard',[76,85,101,96],'service'),
 ('service_east_grove','Service east grove',[121,59,128,94],'service'),
 ('gate_east_grove','Inner-wall east grove',[80,103,127,121],'company'),
 ('gate_south_garden','Gate inner-wall garden',[26,117,75,122],'company'),
 ]
 for id,name,rect,dist in regions:
  x0,z0,x1,z1=rect;cells=set()
  for z in range(z0,z1-1,2):
   for x in range(x0,x1-1,2):
    poly=g.boxpoly([x,z,x+2,z+2])
    if all(g.inside(v,p['extent']) for v in poly) and not any(overlap(poly,a) for a in blockers+occupied):cells.add((x,z))
  polys=[]
  while cells:
   x,z=min(cells,key=lambda c:(c[1],c[0]));X=x+2
   while (X,z) in cells:X+=2
   Z=z+2
   while all((u,Z) in cells for u in range(x,X,2)):Z+=2
   for u in range(x,X,2):
    for v in range(z,Z,2):cells.remove((u,v))
   polys.append(g.boxpoly([x,z,X,Z]))
  if not polys:continue
  height=2 if dist=='civic' else 4 if z1<0 else 0
  p['green']['spaces'].append(dict(id=id,name=name,kind='intercluster_garden',district=dist,polygons=polys,ground_y_m=height))
  occupied+=polys
  for i,poly in enumerate(polys):
   zid=id+'_'+str(i+1)
   p['ground_zones'].append(dict(id=zid,polygon=poly,material='grass',walkable=True,height_m=height,priority=6,blend_width_per_edge_m=[0]*4,named_green_space=True,green_space_id=id))
   p['green']['lawns'].append(dict(id=zid,polygon=poly))
  rng=random.Random(id)
  for _ in range(int((x1-x0)*(z1-z0)/12)):
   pt=[round(rng.uniform(x0+1,x1-1),2),round(rng.uniform(z0+1,z1-1),2)]
   if not any(g.inside(pt,a) for a in polys):continue
   if any(math.dist(pt,t['position'])<5 for t in p['green']['trees']):continue
   canopy=rng.uniform(1.7,2.6)
   if any(g.inside(pt,a) or min(g.distance(pt,v,w) for v,w in g.edges(a))<canopy for a in blockers):continue
   p['green']['trees'].append(dict(id=id+'_tree_'+str(len(p['green']['trees'])),position=pt,type='tree-broad',height_m=round(rng.uniform(4,7),2),ground_y_m=height,canopy_radius_m=round(canopy,2),trunk_collision_radius_m=.25,palette='green',space_id=id))
 # Explicitly named exceptions are the required tree bed and resting patches.
 bed=next(z for z in p['ground_zones'] if z['id']=='red_tree_bed')
 p['green']['spaces'].append(dict(id='red_tree_bed',name='Open red-tree grass-and-earth bed',kind='named_green_space',polygons=[bed['polygon']],ground_y_m=0))
 for m in p['markers']:
  if m.get('rest_spot'):
   id=m['id'].split('/')[-1]+'_grass';poly=g.boxpoly(m['footprint'])
   p['green']['spaces'].append(dict(id=id,name='Guild '+m['name']+' resting grass',kind='named_green_space',polygons=[poly],ground_y_m=.6))
   p['ground_zones'].append(dict(id=id,polygon=poly,material='grass',walkable=True,height_m=.6,priority=8,blend_width_per_edge_m=[0]*4,named_green_space=True,green_space_id=id))
 allot=next(z for z in p['ground_zones'] if z['id']=='spine_service_allotments')
 allot['named_green_space']=True
 p['green']['spaces'].append(dict(id=allot['id'],name='Service household allotments (beds and tending aisles)',kind='allotment',polygons=[allot['polygon']],ground_y_m=0))
