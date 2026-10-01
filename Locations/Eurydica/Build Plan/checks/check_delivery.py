"""Verify the actual review package, source lock, image hashes and final report."""
import json,hashlib,sys
from pathlib import Path
from PIL import Image,ImageStat
R=Path(__file__).resolve().parent
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
required=['eurydica-plan.json','check_plan.py','detail_checks.py','inherited_checks.py','check-result.json','cluster-map.png','same-scale-comparison.png','bird-view-sketch.png','Eurydica Build Plan.md','README.md','GATES.md','render-manifest.json','visual-review.md','visual-review.json','source-manifest.json','build_v7.py','landscape_v7.py','render_review.py','write_delivery.py','run_gates.mjs','RESUME.md']
for name in required:assert (R/name).is_file() and (R/name).stat().st_size>30,'missing/empty '+name
p=json.loads((R/'eurydica-plan.json').read_bytes());m=json.loads((R/'check-result.json').read_bytes());renders=json.loads((R/'render-manifest.json').read_bytes());review=json.loads((R/'visual-review.json').read_bytes())
h=digest(R/'eurydica-plan.json')
assert m['errors']==[] and m['plan_sha256']==h==renders['plan_sha256']==review['plan_sha256'],'stale plan/result/render/review'
assert p['status']=='candidate' and p['v7_changes']['candidate_only'] is True
assert len(m['negative_controls'])>=22 and len(set(m['negative_controls']))==len(m['negative_controls']),'missing controls'
assert m['buildings']==len(p['buildings']) and m['clusters']==len(p['clusters'])
assert m['markers']==len(p['markers']) and m['npc_spots']==len(p['npc_spots']) and m['props']==len(p['props'])
assert renders['comparison']['pixels_per_metre']==4 and renders['comparison']['same_scale']
assert renders['bird_view']['direction']=='north' and renders['bird_view']['down_angle_degrees']==40
for name,spec in renders['images'].items():
 assert digest(R/name)==spec['sha256']==review['images'][name],'stale image review '+name
 with Image.open(R/name) as im:
  im.load();assert list(im.size)==spec['size'] and min(im.size)>1000
  assert max(ImageStat.Stat(im).stddev)>15,'blank image '+name
sources=json.loads((R/'source-manifest.json').read_bytes())
for record in sources['files']:
 assert digest(Path(record['path']))==record['sha256'],'source changed '+record['path']
base=Path('D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/Archive/Build Plan v5')
assert p['source_v5_sha256']==digest(base/'eurydica-plan.json')
assert digest(R/'inherited_checks.py')==digest(base/'checks/inherited_checks.py'),'geometry kernel changed'
doc=(R/'Eurydica Build Plan.md').read_text(encoding='utf-8');readme=(R/'README.md').read_text(encoding='utf-8')
for id in [c['id'] for c in p['clusters']]+m['added_buildings']:assert '`'+id+'`' in doc,'undocumented '+id
for token in [h,f"{m['green_area_m2']:,.2f}",f"{m['north_green_area_m2']:,.2f}",f"{m['gate_river_m']:.1f}",'## v7 changes','**not met**','not owner-approved','PLAN_CHECK_PASS']:assert token in doc,'missing disclosure '+token
assert 'candidate' in readme and 'same-scale-comparison.png' in readme
assert review['verdict']=='reviewed_candidate' and len(review['references_reviewed'])==4
if '--preflight' not in sys.argv:
 report=(R.parent.parent/'handoff/eurydica-plan-v7-last.txt').read_text(encoding='utf-8').splitlines()
 assert len(report)==6 and report[0].startswith('COMPLETE') and 'INCOMPLETE' not in '\n'.join(report)
 for token in [h,str(m['buildings'])+' buildings',str(m['clusters'])+' clusters',f"{m['green_area_m2']:.2f}",'PLAN_CHECK_PASS','owner approval pending']:
  assert token in '\n'.join(report),'report mismatch '+token
print('DELIVERY_CHECK_PASS')
