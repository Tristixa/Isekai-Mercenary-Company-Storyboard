"""v5 invariants and negative controls, layered over v4 geometry checks."""
import sys,json,math,copy,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as g
R=Path(__file__).resolve().parent
OLD=json.loads((R/'baseline/approved-v4/eurydica-plan.json').read_bytes())
MARKET={'infill_home_12':'market_provisions','infill_home_06':'market_small_shop_east','street_home_8':'market_bakery','infill_home_23':'market_small_shop_south'}
def changes(a,b,path=()):
 if type(a)!=type(b):return [(path,a,b)]
 if isinstance(a,dict):return sum((changes(a[k],b[k],path+(k,)) if k in a and k in b else [(path+(k,),a.get(k),b.get(k))] for k in a.keys()|b.keys()),[])
 if isinstance(a,list):return sum((changes(a[i],b[i],path+(i,)) if i<len(a) and i<len(b) else [(path+(i,),a[i] if i<len(a) else None,b[i] if i<len(b) else None)] for i in range(max(len(a),len(b)))),[])
 return [] if a==b else [(path,a,b)]
def permitted(path,a,b):
 if path[0]=='buildings':
  id=OLD['buildings'][path[1]]['id'];return path[2]=='roof_kit' or (id in MARKET and path[2] in {'facade_id','role','display_name','roof_palette','asset_status','roof_binding_note'})
 if path[0] in ('markers','npc_spots','props','ground_zones','new_facades','portals'):return isinstance(path[1],int) and path[1]>=len(OLD[path[0]]) and a is None
 if path[0]=='interiors' and len(path)==5 and path[2] in ('rooms','vertical_links'):
  item=OLD['interiors'][path[1]][path[2]][path[3]]
  return item['id'] in ('two_bed_dormitory','dorm_stair') and path[4] in ('player_access','access_reason')
 return False
def new_records(p,key):return p[key][len(OLD[key]):]
def validate(p):
 errors=[];metrics={}
 def need(v,s):
  if not v:errors.append(s)
 for path,a,b in changes(OLD,p):need(permitted(path,a,b),'unauthorized change '+str(path))
 for key in ('markers','npc_spots','props','ground_zones','portals','new_facades'):
  ids=[v['id'] for v in p[key]];need(len(ids)==len(set(ids)),'duplicate '+key)
 buildings={b['id']:b for b in p['buildings']}
 for id,facade in MARKET.items():
  b=buildings[id];need(b['facade_id']==facade and b['roof_palette']=='green','market business '+id)
 for b in p['buildings']:
  kit=b.get('roof_kit',{});need(set(kit)>={'dormers','chimneys','bays','roof_variant','bounds_rule'},'roof kit missing '+b['id'])
  need(all(v in ('gable','shed') for v in kit.get('dormers',[])) and all(v=='squat_stone' for v in kit.get('chimneys',[])) and all(v=='recessed_upper_bay' for v in kit.get('bays',[])),'roof kit enum '+b['id'])
 need(len({json.dumps(b.get('roof_kit',{}),sort_keys=True) for b in p['buildings']})>=5,'roof kit variety')
 solids=[poly for b in p['buildings'] for poly in [[g.rotate(v,b) for v in g.boxpoly(f)] for f in b.get('collision_rectangles',[b['footprint']])]]
 routes=[(r,g.strip(a,b,r['width_m'])) for r,i,a,b in g.segments(p)]
 added=new_records(p,'props'); polys={a['id']:g.boxpoly(a['footprint']) for a in added}
 def walk(pt):
  return any(z['walkable'] and g.inside(pt,z['polygon']) for z in p['ground_zones']) and not any(not z['walkable'] and g.inside(pt,z['polygon']) for z in p['ground_zones']) and not any(g.inside(pt,s) for s in solids) and not g.inside(pt,p['river']['polygon']) and not g.inside(pt,p['waterworks']['feeder_polygon'])
 for prop in added:
  poly=polys[prop['id']];f=prop['footprint']
  need(f[0]<f[2] and f[1]<f[3],'prop footprint '+prop['id'])
  need(all(walk(v) for v in poly),'prop not on usable ground '+prop['id'])
  for r,s in routes:need(not g.area_overlap(poly,s),'prop obstructs route '+prop['id']+' / '+r['id'])
  for s in solids:need(not g.area_overlap(poly,s),'prop overlaps building '+prop['id'])
  need(not g.area_overlap(poly,p['hq_reservation']['polygon']),'prop occupies HQ reserve '+prop['id'])
  for plot in p['small_plots']:need(not g.area_overlap(poly,plot['polygon']),'prop occupies retained garden '+prop['id'])
  for prior in OLD['props']:
   if 'position' in prior:need(not g.inside(prior['position'],poly) and min(g.distance(prior['position'],a,b) for a,b in g.edges(poly))>=prior.get('collision_radius_m',0),'prop overlaps existing prop '+prop['id'])
  for t in p['green']['trees']:need(not g.inside(t['position'],poly) and min(g.distance(t['position'],a,b) for a,b in g.edges(poly))>=t['trunk_collision_radius_m'],'prop hits tree '+prop['id'])
  if prop.get('zone_id'):
   zone=next(z for z in p['ground_zones'] if z['id']==prop['zone_id']);need(all(g.inside(v,zone['polygon']) for v in poly),'prop outside owning zone '+prop['id'])
 for i,a in enumerate(added):
  for b in added[i+1:]:need(not g.area_overlap(polys[a['id']],polys[b['id']]),'prop overlap '+a['id']+' / '+b['id'])
 clusters={a['cluster_id'] for a in added if a['type']=='market_stall'}
 need(clusters=={'market_court','market_edge','market_south'},'stall clusters missing')
 for id in clusters:
  members=[a for a in added if a.get('cluster_id')==id and a['type']=='market_stall'];need(3<=len(members)<=4 and all(a.get('awning') and a.get('footprint_includes_awning') for a in members),'stall cluster specification '+id)
  need({a['type'] for a in added if a.get('cluster_id')==id}>={'crates','baskets','barrow'},'stall accessories '+id)
 court=next(s['polygon'] for s in p['squares'] if s['id']=='red_tree_court')
 need(any(all(g.inside(v,court) for v in polys[a['id']]) for a in added if a.get('cluster_location')=='red_tree_court'),'court stalls missing')
 zones=new_records(p,'ground_zones');need(len(zones)==1 and zones[0]['id']=='spine_service_allotments','allotment ground zone missing')
 for z in zones:
  need(all(g.inside(v,p['extent']) for v in z['polygon']),'zone outside extent')
  for s in solids:need(not g.area_overlap(z['polygon'],s),'zone hits building')
  for r,s in routes:need(not g.area_overlap(z['polygon'],s),'zone blocks route '+r['id'])
  for plot in p['small_plots']:need(not g.area_overlap(z['polygon'],plot['polygon']),'zone overlays existing garden '+plot['id'])
 for prefix in ('workshop','quays'):need({a['type'] for a in added if a['id'].startswith(prefix+'_')}>={'stacked_materials','timber_pile','crates','work_area','cart'},'yard activity incomplete '+prefix)
 from density_checks import validate_density
 density_errors,density_metrics=validate_density(p,OLD)
 errors.extend(density_errors);metrics.update(density_metrics)
 marks={m['id']:m for m in p['markers']};newmarks=new_records(p,'markers')
 expected={f'civic_terrace/{role}_{i}' for role in ('leaders','officers') for i in range(1,6)}|{'civic_terrace/commander','civic_terrace/envoy','civic_terrace/camera_hint','south_gate/envoy_arrival','guild_courtyard/envoy'}
 need(expected<=marks.keys(),'story markers missing')
 plaza=next(s['polygon'] for s in p['squares'] if s['id']=='clock_plaza')
 figures=[m for m in newmarks if m['id'].startswith('civic_terrace/') and m.get('kind')!='camera_hint']
 distances=[math.dist(a['position'],b['position']) for i,a in enumerate(figures) for b in figures[i+1:]]
 metrics['civic_min_centre_spacing_m']=min(distances);metrics['civic_min_body_edge_spacing_m']=min(distances)-.5
 need(len(figures)==12 and min(distances)-.5>=1.2,'civic figure spacing below 1.2 m edge-to-edge')
 for m in figures:
  pos=m['position'];need(g.inside(pos,plaza) and min(g.distance(pos,a,b) for a,b in g.edges(plaza))>=.25,'figure outside plaza '+m['id'])
  need(m['facing']==('south' if 'leaders_' in m['id'] or m['id'].endswith('/envoy') else 'north'),'civic facing '+m['id'])
  for s in solids:need(min(g.distance(pos,a,b) for a,b in g.edges(s))>=.25,'figure too close to building '+m['id'])
 need(g.inside(marks['civic_terrace/camera_hint']['position'],plaza),'camera ground anchor outside plaza')
 need(294<=marks['south_gate/envoy_arrival']['position'][1]<298.8,'envoy not inside gate')
 court=next(z['polygon'] for z in p['ground_zones'] if z['id']=='courtyard_staging')
 need(g.inside(marks['guild_courtyard/envoy']['position'],court),'envoy outside Guild courtyard')
 # Reachable paths account for new props and retained trees/props, unlike v4 point-only checks.
 obstacle_polys=list(polys.values())
 def unobstructed(pt,radius=.25):
  if not walk(pt):return False
  for poly in obstacle_polys+solids:
   if g.inside(pt,poly) or min(g.distance(pt,a,b) for a,b in g.edges(poly))<radius:return False
  for prop in OLD['props']:
   if 'position' in prop and prop['type']!='banner' and math.dist(pt,prop['position'])<radius+prop.get('collision_radius_m',0):return False
  for t in p['green']['trees']:
   if math.dist(pt,t['position'])<radius+t['trunk_collision_radius_m']:return False
  return True
 def connector(pos):
  targets=[]
  for r,i,a,b in g.segments(p):
   dx,dz=b[0]-a[0],b[1]-a[1];t=max(0,min(1,((pos[0]-a[0])*dx+(pos[1]-a[1])*dz)/(dx*dx+dz*dz)));q=[a[0]+t*dx,a[1]+t*dz];targets.append((math.dist(pos,q),q))
  for dist,q in sorted(targets)[:40]:
   n=max(1,math.ceil(dist/.15))
   if all(unobstructed([pos[0]+(q[0]-pos[0])*i/n,pos[1]+(q[1]-pos[1])*i/n]) for i in range(n+1)):return q
  return None
 connections={}
 for m in p['markers']:
  for prop in added:
   if m['scene']=='city':need(not g.inside(m['position'],polys[prop['id']]) and min(g.distance(m['position'],a,b) for a,b in g.edges(polys[prop['id']]))>=.6,'prop crowds marker '+m['id'])
 for m in newmarks:
  if m['scene']=='city':
   q=connector(m['position']);need(q is not None,'new marker unreachable '+m['id']);connections[m['id']]=q
  else:
   it=next(it for it in p['interiors'] if it['id']==m['scene']);need(g.inside(m['position'],it['walkable_polygon']) and not any(g.inside(m['position'],o) for o in it['obstacles']),'new interior marker off ground '+m['id'])
   room=next(r for r in it['rooms'] if r['id']==m['room_id']);need(g.inside(m['position'],room['polygon']),'evening marker outside common room '+m['id'])
 for m in newmarks:
  if m['id'].startswith('guild_courtyard/'):
   need(g.inside(m['position'],court),'courtyard marker outside staging '+m['id'])
   for id in ('city/elsie_side','city/bench_east','city/bench_south','city/bench_west','city/scene4_line_115'):
    need(math.dist(m['position'],marks[id]['position'])>=1.2,'Elsie staging crowded '+m['id'])
 rest=[m for m in newmarks if m.get('rest_spot')];need(len(rest)==2,'resting spots missing')
 for m in rest:
  need(m['surface'] in ('grass','bench') and m['sprite_use']=='field-sleep','rest spot specification')
  for v in g.boxpoly(m['footprint']):need(g.inside(v,court) and unobstructed(v,.1),'rest body clearance '+m['id'])
  for r,s in routes:need(not g.area_overlap(g.boxpoly(m['footprint']),s),'rest body blocks route '+m['id'])
 evening=new_records(p,'npc_spots');need(len(evening)==6,'six evening spots required')
 for scene in ('guild_interior','city','tavern_interior'):need(sum(s['scene']==scene for s in evening)==2,'evening distribution '+scene)
 for s in evening:
  need(s['marker_id'] in marks and s['position']==marks[s['marker_id']]['position'],'evening marker binding '+s['id']);need(s['schedule']['end']=='21:00' and s['schedule']['end_exclusive'] is True,'evening cutoff '+s['id'])
 guild=next(i for i in p['interiors'] if i['id']=='guild_interior')
 restricted=[next(r for r in guild['rooms'] if r['id']=='two_bed_dormitory'),guild['vertical_links'][0]]+[next((v for v in p['portals'] if v['id']==id+'_portal'),{}) for id in ('dorm_annex','larger_dorm')]
 need(all(r.get('player_access') is False and r.get('access_reason')=="adventurers' quarters" for r in restricted),'dormitory player access')
 metrics.update(added_props=len(added),added_markers=len(newmarks),evening_spots=len(evening),rest_spots=len(rest),plaza_polygon_changed=False,marker_connectors=connections)
 return errors,metrics
def controls(p):
 tests=[]
 def test(name,mutate,token):
  q=copy.deepcopy(p);mutate(q);e,_=validate(q);assert any(token in s for s in e),(name,e);tests.append(name)
 test('retained route mutation',lambda q:q['routes'][0].update(width_m=9),'unauthorized change')
 test('stall on spine',lambda q:next(a for a in q['props'] if a['id']=='market_court_stall_1').update(footprint=[-1,86,1,88]),'prop obstructs route')
 test('roof kit missing',lambda q:q['buildings'][0].pop('roof_kit'),'roof kit missing')
 test('ceremony figures collide',lambda q:next(m for m in q['markers'] if m['id']=='civic_terrace/commander').update(position=[0,-66.2]),'civic figure spacing')
 test('dorm reopened',lambda q:next(i for i in q['interiors'] if i['id']=='guild_interior')['rooms'][-1].update(player_access=True),'dormitory player access')
 test('evening too late',lambda q:q['npc_spots'][-1]['schedule'].update(end='22:00'),'evening cutoff')
 test('allotment across road',lambda q:q['ground_zones'][-1].update(polygon=g.boxpoly([-2,80,2,95])),'zone blocks route')
 test('stall awning missing',lambda q:next(a for a in q['props'] if a['id']=='market_court_stall_1').update(awning=''),'stall cluster specification')
 from density_checks import controls_density
 tests.extend(controls_density(p,validate))
 return tests

def byte_report(write=True):
 a=(R/'baseline/approved-v4/eurydica-plan.json').read_bytes();b=(R/'eurydica-plan.json').read_bytes();p=json.loads(b)
 edits=json.loads((R/'byte-edit-manifest.json').read_text());ac=bc=0;count=0;blocks=[]
 for e in edits:
  aa=a[ac:e['old_start']];bb=b[bc:e['new_start']];assert aa==bb,('retained bytes changed',e['path']);count+=len(aa)
  blocks.append(dict(old_start=ac,new_start=bc,bytes=len(aa),sha256=hashlib.sha256(aa).hexdigest()));ac=e['old_end'];bc=e['new_end']
 assert a[ac:]==b[bc:];count+=len(a[ac:]);blocks.append(dict(old_start=ac,new_start=bc,bytes=len(a[ac:]),sha256=hashlib.sha256(a[ac:]).hexdigest()))
 delta=changes(OLD,p);assert all(permitted(*d) for d in delta),'unauthorized semantic change'
 # Enumerate entity IDs independently from the byte-edit manifest.
 changed_ids={};added_ids={}
 for k in ('buildings','ground_zones','markers','npc_spots','props','new_facades','interiors','portals'):
  changed_ids[k]=[v['id'] for i,v in enumerate(p[k][:len(OLD[k])]) if v!=OLD[k][i]]
  added_ids[k]=[v['id'] for v in p[k][len(OLD[k]):]]
 changed_ids['rooms_and_links']=['guild_interior/two_bed_dormitory','guild_interior/dorm_stair']
 result=dict(source_sha256=hashlib.sha256(a).hexdigest(),candidate_sha256=hashlib.sha256(b).hexdigest(),source_bytes=len(a),candidate_bytes=len(b),retained_bytes=count,removed_or_replaced_bytes=len(a)-count,inserted_or_replacement_bytes=len(b)-count,edit_count=len(edits),unchanged_spans=blocks,changed_ids=changed_ids,added_ids=added_ids,changed_paths=[list(d[0]) for d in delta])
 prior_raw=(R/'superseded/round-1/eurydica-plan.json').read_bytes();prior=json.loads(prior_raw)
 revision={}
 for key in ('props','ground_zones'):
  previous={a['id']:a for a in prior[key]};current={a['id']:a for a in p[key]}
  revision[key]={'changed':[id for id in previous if current.get(id)!=previous[id]],'added':[id for id in current if id not in previous],'removed':[id for id in previous if id not in current]}
 result['round_1_revision']={'source_sha256':hashlib.sha256(prior_raw).hexdigest(),'collections':revision,'other_collections_equal':all(p[k]==prior[k] for k in prior if k not in ('props','ground_zones'))}
 assert result['round_1_revision']['other_collections_equal']
 assert (R/'Eurydica Build Plan.md').read_bytes().endswith((R/'baseline/approved-v4/Eurydica Build Plan.md').read_bytes())
 if write:
  (R/'byte-diff-summary.json').write_text(json.dumps(result,indent=2)+'\n')
  lines=['# Byte-level preservation report','',f"Source: `{result['source_sha256']}`",f"Candidate: `{result['candidate_sha256']}`",'',f"{count:,} / {len(a):,} source JSON bytes retained verbatim, in {len(blocks)} checked spans. {len(a)-count:,} source bytes replaced; {len(b)-count:,} bytes inserted/replaced. {len(edits)} surgical edits; no global JSON reserialization.",'','Every semantic difference is checked against the six-item allowlist. All original routes, junctions, districts, coordinates, building footprints/yaws/heights, terrain, phase-1 polygon, clock tower geometry, HQ reservation and existing markers/portals are unchanged. The added roof_kit field is the only edit on buildings outside the four market businesses. HQ access is attached to new future portals, leaving reservation bytes intact. The v4 build-plan document is retained as an exact byte suffix.','','## Every changed ID']
  for k,ids in changed_ids.items():
   if ids:lines+=['',f'**{k}**',*['- `'+id+'`' for id in ids]]
  lines+=['','## Every added ID']
  for k,ids in added_ids.items():
   if ids:lines+=['',f'**{k}**',*['- `'+id+'`' for id in ids]]
  lines+=['','## Density correction versus initial v5','','Every other collection is exactly equal to the archived initial v5. No IDs were removed.']
  for key,delta in revision.items():
   for kind,ids in delta.items():
    if ids:lines+=['',f'**{key}: {kind}**',*['- `'+id+'`' for id in ids]]
  lines+=['','Exact changed JSON paths and byte-span offsets/hashes: `byte-diff-summary.json` and `byte-edit-manifest.json`.','The baseline directory is a byte copy of the approved v4 delivery; its older illustrations are historical references only.']
  (R/'byte-diff-summary.md').write_text('\n'.join(lines)+'\n')
 print('BYTE_DIFF_PASS');return result
