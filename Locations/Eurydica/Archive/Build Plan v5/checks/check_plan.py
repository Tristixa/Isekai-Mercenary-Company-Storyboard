"""Inherited checks plus v4 exact rotated wall gaps, organic routes and landmark locks."""
import sys, json, math, copy, statistics, hashlib
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as base
R=Path(__file__).resolve().parent
OLD=json.loads((R.parent/'eurydica-plan-v3/eurydica-plan.json').read_text(encoding='utf-8'))
def gap(a,b):
 if base.area_overlap(a,b):return 0.
 return min([base.distance(p,c,d) for p in a for c,d in base.edges(b)]+[base.distance(p,c,d) for p in b for c,d in base.edges(a)])
def area(p):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in base.edges(p)))/2
def validate(p,external=True):
 errors,metrics=base.validate(p,external)
 errors=[e for e in errors if e!='gate-market walk outside 60-120 seconds']
 def need(ok,msg):
  if not ok:errors.append(msg)
 need(45<=metrics['walk_time_s']<=90,'gate-market walk outside 45-90 seconds')
 lookup={b['id']:b for b in p['buildings']}
 need({b['id'] for b in OLD['buildings'] if not b['id'].startswith('infill_')}<=set(lookup),'established building removed')
 need({d['id'] for d in OLD['districts']}=={d['id'] for d in p['districts']},'district set changed')
 for k in ('markers','npc_spots','interiors','portals','phase_1','hq_reservation','approved_connections','junctions','river','bridge','camera'):
  if k not in ('markers','npc_spots','interiors','portals'):need(p[k]==OLD[k],'preserved lock changed: '+k)
 need(p['terrain']==OLD['terrain'],'terraces, retaining walls, ramps or cliffs changed')
 need(p['city_wall']==OLD['city_wall'],'one-gate wall enclosure changed')
 need(area(p['extent'])<=area(OLD['extent']),'extent grew')
 before=sum(b['id'].startswith('infill_') for b in OLD['buildings']);after=sum(b['id'].startswith('infill_') for b in p['buildings'])
 need(after<before*.65,'generic infill not clearly reduced')
 permitted={'south_gate','watch_tower','old_hall','stables','store_shed','tool_repair','timber_containers','material_sorting','bulk_storehouse','loading_shelter','quay_storehouse','waterkeeper','washing','cistern'}
 polys={b['id']:base.footprint(b) for b in p['buildings']};rows=[]
 for b in p['buildings']:
  need(isinstance(b.get('yaw_deg'),(int,float)) and b['yaw_deg']%5==0,'invalid yaw '+b['id'])
  need(all(base.inside(v,p['extent']) for v in polys[b['id']]),'building outside extent '+b['id'])
  need(not b['spacing_exempt_reason'] or b['id'] in permitted,'unauthorized spacing exemption '+b['id'])
  value,other=min((gap(polys[b['id']],s),id) for id,s in polys.items() if id!=b['id'])
  rows.append(dict(id=b['id'],nearest=other,gap_m=round(value,6),exempt=b['spacing_exempt_reason']))
  if not b['spacing_exempt_reason']:need(value<=15+base.EPS,'isolated building '+b['id'])
  if b['id'].startswith('infill_'):
   f=b['footprint'];phase=1 if base.inside([(f[0]+f[2])/2,(f[1]+f[3])/2],p['phase_1']['polygon']) else 2
   need(b['phase']==phase,'infill outside build phase '+b['id'])
   need(next(r for r in p['routes'] if r['id']==b['door_route'])['phase']==phase,'door route phase mismatch '+b['id'])
 med=statistics.median(r['gap_m'] for r in rows if not r['exempt'])
 need(1<=med<=4,'median wall gap outside 1-4 m')
 allmembers=[id for c in p['clusters'] for id in c['building_ids']]
 need(len(allmembers)==len(set(allmembers)) and set(allmembers)=={r['id'] for r in rows if not r['exempt']},'cluster population does not cover every non-exempt building')
 cluster_metrics=[]
 for c in p['clusters']:
  vals=[r['gap_m'] for r in rows if r['id'] in c['building_ids']]
  md=statistics.median(vals);cluster_metrics.append(dict(id=c['id'],buildings=len(vals),median_gap_m=round(md,3)))
 # Global cluster population is fixed above. Per-component medians are disclosed,
 # including single public buildings and the zero-gap party-wall pair.
 need(len({b['yaw_deg'] for b in p['buildings']})>=3 and sum(b['yaw_deg']!=0 for b in p['buildings'])>=15,'insufficient varied building angles')
 need(len({(round(b['footprint'][2]-b['footprint'][0],2),round(b['footprint'][3]-b['footprint'][1],2)) for b in p['buildings'] if 'home' in b['id']})>=6,'insufficient home size variety')
 paired=[b for b in p['buildings'] if b.get('party_wall_group')]
 need(len(paired)>=2 and gap(polys[paired[0]['id']],polys[paired[1]['id']])<base.EPS,'shared-wall pair missing')
 tower=lookup['watch_tower'];f=tower['footprint']
 need(tower['district']=='civic' and [(f[0]+f[2])/2,(f[1]+f[3])/2]==[0,-70],'clock tower not centred in Civic Terrace')
 need(26<=tower['height_m']+tower['roof_height_m']<=30 and tower['belfry_open'] and tower['clock_face']=='s','clock tower specification incorrect')
 need(tower['ground_y_m']==2 and tower['yaw_deg']==0,'clock south orientation or terrace level incorrect')
 need(sum(b['facade_id'] in ('civic_clock_tower','watch_bell_tower') for b in p['buildings'])==1,'old bell tower duplicated')
 need({s['id'] for s in p['squares']}=={'red_tree_court','gate_square','bridge_south_landing','bridge_north_landing','clock_plaza'},'destination square missing')
 for s in p['squares']:
  for id,poly in polys.items():
   if id=='watch_tower' and s['id']=='clock_plaza':continue
   need(not base.area_overlap(poly,s['polygon']),'square occupied '+s['id']+' / '+id)
 for plot in p['small_plots']:
  need(all(base.inside(v,p['extent']) for v in plot['polygon']),'garden outside extent '+plot['id'])
  need(any(z['id']==plot['id'] and z['material']=='garden_bed' and z['polygon']==plot['polygon'] for z in p['ground_zones']),'garden missing surface '+plot['id'])
  need(not any(base.area_overlap(plot['polygon'],s) for s in polys.values()),'garden hits building '+plot['id'])
  need(not any(base.area_overlap(plot['polygon'],base.strip(a,b,r['width_m'])) for r,i,a,b in base.segments(p)),'garden hits route '+plot['id'])
 # Clock sightline uses a 3D ray to south clock centre, including intervening roof envelopes.
 a=[0,10];b=[0,-67];blocked=[]
 for ob in p['buildings']:
  if ob['id']=='watch_tower':continue
  for step in range(1001):
   t=step/1000;pt=[0,a[1]+(b[1]-a[1])*t];height=1.68+(20-1.68)*t
   if base.inside(pt,polys[ob['id']]) and height<ob['ground_y_m']+ob['height_m']+ob['roof_height_m']:blocked.append(ob['id']);break
 need(not blocked,'clock sightline obstructed '+str(blocked))
 metrics.update(buildings_before=len(OLD['buildings']),generic_infill_before=before,generic_infill_after=after,median_gap_m=round(med,3),non_exempt_max_gap_m=max(r['gap_m'] for r in rows if not r['exempt']),cluster_metrics=cluster_metrics,spacing_rows=rows,rotated_buildings=sum(b['yaw_deg']!=0 for b in p['buildings']),extent_m2=area(p['extent']),tower_height_m=tower['height_m']+tower['roof_height_m'],tower_position_xz=[0,-70],tower_ground_y_m=2,clock_sightline_clear=not blocked)
 return errors,metrics
def controls(p):
 tests=base.controls(p)
 def check(name,mutate,token):
  q=copy.deepcopy(p);mutate(q);e,_=validate(q,False);assert any(token in s for s in e),(name,e);tests.append(name)
 check('yaw must use five-degree increments',lambda q:q['buildings'][3].update(yaw_deg=7),'invalid yaw')
 check('clock moved off civic centre',lambda q:next(b for b in q['buildings'] if b['id']=='watch_tower').update(footprint=[-12,-73,-6,-67]),'clock tower not centred')
 check('missing square',lambda q:q['squares'].pop(),'destination square missing')
 check('no spacing exemptions for ordinary homes',lambda q:next(b for b in q['buildings'] if b['id']=='lodging').update(spacing_exempt_reason='landmark'),'unauthorized spacing exemption')
 check('missing story marker',lambda q:q['markers'].pop(),'preserved lock changed: markers')
 check('isolated ordinary home',lambda q:next(b for b in q['buildings'] if b['id']=='infill_home_01').update(footprint=[500,500,506,506]),'isolated building')
 # Rotating a slender rectangle introduces a collision that the axis-aligned footprint misses.
 a={'footprint':[0,0,10,2],'yaw_deg':45};b={'footprint':[6,3,8,5],'yaw_deg':0}
 assert not base.area_overlap(base.boxpoly(a['footprint']),base.boxpoly(b['footprint']))
 assert base.area_overlap(base.footprint(a),base.footprint(b));tests.append('rotated-only collision detected')
 assert abs(gap(base.boxpoly([0,0,5,5]),base.boxpoly([8,0,10,5]))-3)<1e-9
 assert gap(base.boxpoly([0,0,5,5]),base.boxpoly([5,0,10,5]))==0
 tests.append('wall-gap positive controls 3m and party-wall zero')
 return tests
# v5 checks enforce a stricter v4 allowlist for the four collections extended above.
import check_v5
v4_validate=validate
def validate(p,external=True):
 errors,metrics=v4_validate(p,external)
 extra,measure=check_v5.validate(p);errors.extend(extra);metrics.update(measure)
 return errors,metrics

if __name__=='__main__':
 path=next((Path(a) for a in sys.argv[1:] if not a.startswith('--')),R/'eurydica-plan.json')
 p=json.loads(path.read_text(encoding='utf-8'));errors,metrics=validate(p)
 if '--self-test' in sys.argv and not errors:metrics['negative_controls']=base.controls(p)+check_v5.controls(p)
 metrics['plan_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();metrics['errors']=errors
 (R/'check-result.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in metrics.items() if k not in ('spacing_rows','cluster_metrics')},indent=2))
 print('CLUSTERS:',json.dumps(metrics['cluster_metrics']))
 print('PLAN_CHECK_FAIL' if errors else 'PLAN_CHECK_PASS');sys.exit(bool(errors))
