"""Localized, byte-preserving edits to the owner-approved v4 JSON."""
import json, copy, sys, hashlib, math
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as geo
R=Path(__file__).resolve().parent
B=R/'baseline/approved-v4'
raw=(B/'eurydica-plan.json').read_bytes().decode('utf-8')
old=json.loads(raw);p=copy.deepcopy(old)
MARKET={'infill_home_12':('market_provisions','Provisions shop'), 'infill_home_06':('market_small_shop_east','Small sundries shop'), 'street_home_8':('market_bakery','Bakery'), 'infill_home_23':('market_small_shop_south','Small cloth shop')}
for i,b in enumerate(p['buildings']):
 if b['id'] in MARKET:
  facade,name=MARKET[b['id']]
  b.update(facade_id=facade,display_name=name,role=name,roof_palette='green',asset_status='candidate business facade adaptation',roof_binding_note='v5 business use: green roof; original dimensions, door and yaw retained.')
  f=b['footprint'];p['new_facades'].append(dict(id=facade,footprint_m=[f[2]-f[0],f[3]-f[1]],wall_height_m=b['height_m'],door_face=b['door_face'],roof='green',status='candidate needed',display_name=name))
 kit=dict(dormers=[],chimneys=[],bays=[],roof_variant='existing',bounds_rule='Within existing footprint, yaw and total height envelope; no new ground collision.',source='v3/review/jrpg-gap-analysis.md / rank 2')
 if b['id'] in ('tavern','old_hall'):
  kit.update(dormers=['gable','shed'],chimneys=['squat_stone'],bays=['recessed_upper_bay'],roof_variant='modest_corner')
 elif b['id'] in MARKET:
  kit['dormers']=['shed' if i%2 else 'gable'];kit['chimneys']=['squat_stone'] if b['id']=='street_home_8' else [];kit['bays']=['recessed_upper_bay'] if b['id']=='infill_home_06' else []
 elif 'home' in b['id'] or b['id']=='lodging':
  if i%3==0:kit['dormers']=['gable' if i%2 else 'shed'];kit['chimneys']=['squat_stone']
 elif b['id'] in ('tool_repair','food_shop','clinic','company_house'):kit['chimneys']=['squat_stone']
 b['roof_kit']=kit

def marker(id,pos,scene='city',height=0,**kw):
 m=dict(id=id,name=id.split('/')[-1],scene=scene,position=pos,height_m=height,source='v5 candidate / owner 2026-09-29',**kw);p['markers'].append(m);return m
for i,(x,z) in enumerate(zip([-3.6,-1.8,0,1.8,3.6],[-65.6,-66,-66.2,-66,-65.6]),1):marker(f'civic_terrace/leaders_{i}',[x,z],height=2,facing='south',figure_radius_m=.25)
marker('civic_terrace/commander',[0,-63.8],height=2,facing='north',figure_radius_m=.25)
for i,x in enumerate([-3.6,-1.8,0,1.8,3.6],1):marker(f'civic_terrace/officers_{i}',[x,-61.8],height=2,facing='north',figure_radius_m=.25)
marker('civic_terrace/envoy',[5.4,-65.1],height=2,facing='south',figure_radius_m=.25)
marker('civic_terrace/camera_hint',[0,-61.1],height=2,facing='north',kind='camera_hint',look_at_marker='civic_terrace/commander',camera_elevation_m=5,push_in_m=1.0,note='Ground anchor, not a physical actor; retain approved camera contract.')
marker('south_gate/envoy_arrival',[-1.5,296],facing='north')
marker('guild_courtyard/envoy',[-27,290],height=.6,facing='west')
guild=next(i for i in p['interiors'] if i['id']=='guild_interior')
for r in guild['rooms']:
 if r['id']=='two_bed_dormitory':r.update(player_access=False,access_reason="adventurers' quarters")
guild['vertical_links'][0].update(player_access=False,access_reason="adventurers' quarters")
# Future portals carry access policy without touching reserved parcel records.
for id in ('dorm_annex','larger_dorm'):
 p['portals'].append(dict(id=id+'_portal',reservation_id=id,phase='future',player_access=False,access_reason="adventurers' quarters",npc_access=True,placement='Resolve inside the unchanged reserved parcel when built; no new coordinate in this candidate.'))
for prefix,scene,positions,h,room in [('guild_interior','guild_interior',[[-2,1.5],[2,1.5]],0,'main_room'),('guild_courtyard','city',[[-29,292],[-25,292]],.6,'courtyard_staging'),('tavern_interior','tavern_interior',[[-2.5,-3],[2.5,-3]],0,'common_room')]:
 for i,pos in enumerate(positions,1):
  id=f'{prefix}/adventurer_evening_{i}';marker(id,pos,scene,h,room_id=room)
  p['npc_spots'].append(dict(id=id,marker_id=id,scene=scene,position=pos,height_m=h,room_id=room,character='Adventurer',schedule=dict(start='18:00',end='21:00',end_exclusive=True,start_status='candidate evening start; owner fixed end at 21:00')))
for i,pos in enumerate([[-38,291.5],[-24,288.5]],1):marker(f'guild_courtyard/rest_{i}',pos,height=.6,rest_spot=True,surface='grass',footprint=[pos[0]-.6,pos[1]-1,pos[0]+.6,pos[1]+1],sprite_use='field-sleep',occupants='resting or injured adventurer')

def prop(id,typ,rect,**kw):
 rec=dict(id=id,type=typ,footprint=rect,scene='city',height_m=0,**kw);p['props'].append(rec);return rec
# Entire stall footprint includes its awning; each group has two separate stalls.
for id,rects,where in [('market_court',[[-6.9,86,-5.1,87.4],[-6.9,89,-5.1,90.4]],'red_tree_court'),('market_edge',[[4.8,99,6.6,100.4],[4.8,102,6.6,103.4]],'spine widened edge')]:
 for i,rect in enumerate(rects,1):prop(f'{id}_stall_{i}','market_stall',rect,cluster_id=id,cluster_location=where,awning='cream-sage' if id=='market_court' else 'cream-muted-ochre',contents='produce baskets' if i==1 else 'cloth and dry goods',footprint_includes_awning=True)
zone=dict(id='spine_service_allotments',polygon=geo.boxpoly([29,82,45,100]),material='garden_bed',height_m=0,walkable=True,blend_width_per_edge_m=[.4]*4,priority=2,purpose='Allotments between Market Spine and Service Lanes; walkable tending aisles between raised beds.')
p['ground_zones'].append(zone)
for i,(x,z) in enumerate([(31,85),(37,85),(31,92),(37,92)],1):prop(f'allotment_bed_{i}','raised_produce_bed',[x,z,x+4,z+3],zone_id=zone['id'],contents='herbs and vegetables',owner='Service Lanes households')
prop('allotment_tools','tool_crates',[42,96,44,97.5],zone_id=zone['id'],owner='Service Lanes households')
for district,items in [('workshop', [('timber_pile',[-103,156,-94,159]),('stacked_materials',[-101,211,-93,215]),('crates',[-69,184,-65,188]),('work_area',[-101,229,-93,233]),('cart',[-70,238,-67,240])]),('quays',[('timber_pile',[-103,63,-95,67]),('stacked_materials',[-69,76,-63,80]),('crates',[-102,13,-96,17]),('work_area',[-64,12,-56,17]),('cart',[-69,93,-66,95])])]:
 for typ,rect in items:prop(f'{district}_{typ}',typ,rect,zone_id='working_court' if district=='workshop' else 'receiving_yard',owner='Workshop crews' if district=='workshop' else 'Quay receivers',routine='Sorted stock and maintained working equipment; preserve all work-loop strips.')

from density_fixes import apply
apply(p, prop, geo)

# Parse spans without normalizing whitespace, numeric spellings or Unicode.
spans={};decoder=json.JSONDecoder()
def parse(i,path=()):
 while raw[i].isspace():i+=1
 start=i
 if raw[i]=='{':
  i+=1
  while True:
   while raw[i].isspace():i+=1
   if raw[i]=='}':i+=1;break
   key,j=decoder.raw_decode(raw,i);i=j
   while raw[i].isspace() or raw[i]==':':i+=1
   i=parse(i,path+(key,))
   while raw[i].isspace():i+=1
   if raw[i]==',':i+=1
 elif raw[i]=='[':
  i+=1;n=0
  while True:
   while raw[i].isspace():i+=1
   if raw[i]==']':i+=1;break
   i=parse(i,path+(n,));n+=1
   while raw[i].isspace():i+=1
   if raw[i]==',':i+=1
 else:_,i=decoder.raw_decode(raw,i)
 spans[path]=(start,i);return i
parse(0)
edits=[]
def diff(a,b,path=()):
 if a==b:return
 start,end=spans[path]
 if isinstance(a,dict) and isinstance(b,dict):
  assert a.keys()<=b.keys()
  for k in a:diff(a[k],b[k],path+(k,))
  extra={k:v for k,v in b.items() if k not in a}
  if extra:edits.append((end-1,end-1,', '+json.dumps(extra,ensure_ascii=False)[1:-1],list(path)+['+fields']))
 elif isinstance(a,list) and isinstance(b,list):
  assert len(b)>=len(a)
  for n,v in enumerate(a):diff(v,b[n],path+(n,))
  if len(b)>len(a):edits.append((end-1,end-1,(', ' if a else '')+', '.join(json.dumps(v,ensure_ascii=False) for v in b[len(a):]),list(path)+['+items']))
 else:edits.append((start,end,json.dumps(b,ensure_ascii=False),list(path)))
diff(old,p);edits.sort()
output=[];cursor=0;manifest=[];offset=0
for start,end,replacement,path in edits:
 output.append(raw[cursor:start]);output.append(replacement)
 bs=len(raw[:start].encode());be=len(raw[:end].encode());newstart=bs+offset
 manifest.append(dict(path=path,old_start=bs,old_end=be,new_start=newstart,new_end=newstart+len(replacement.encode())))
 offset+=len(replacement.encode())-(be-bs);cursor=end
output.append(raw[cursor:]);result=''.join(output).encode()
assert json.loads(result)==p
(R/'eurydica-plan.json').write_bytes(result)
(R/'byte-edit-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('BUILD_V5_PASS',len(edits),'localized byte edits')
