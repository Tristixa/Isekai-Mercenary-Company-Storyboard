"""Verify the delivered v7c candidate, preservation, truthful target and reviews."""
import json,hashlib
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
p=json.loads((R/'eurydica-plan-v7c.json').read_bytes());digest=sha(R/'eurydica-plan-v7c.json')
c=json.loads((R/'check-result-v7c.json').read_bytes())
assert c['plan_sha256']==digest and not c['errors']
assert len(c.get('negative_controls',[]))>=22 and len(c.get('v7b_negative_controls',[]))>=12
for name,h in c['checker_sources'].items():assert sha(R/name)==h,'stale checker '+name
source=json.loads((R/'source-manifest-v7c.json').read_bytes())
for name,h in source.items():
 if name!='Eurydica Build Plan.md':assert sha(R/name)==h,'prior file changed '+name
backup=R/'Eurydica Build Plan-before-v7c.md'
assert sha(backup)==source['Eurydica Build Plan.md']
doc=(R/'Eurydica Build Plan.md').read_bytes()
assert doc.startswith(backup.read_bytes())
text=doc.decode('utf-8');assert text.count('## v7c — final four-point refinement')==1
for token in ('PLAN_CHECK_PASS','35% reduction aim is not met',digest,'5.5 pixels per metre','owner approval pending'):assert token in text,token
manifest=json.loads((R/'render-manifest-v7c.json').read_bytes())
assert manifest['plan_sha256']==digest and manifest['renderer_sha256']==sha(R/'render_review_v7c.py')
names={'cluster-map-v7c.png','bird-view-sketch-v7c.png','v7b-vs-v7c.png'}
assert names==set(manifest['images'])
for name in names:
 im=Image.open(R/name);im.verify();im=Image.open(R/name)
 assert list(im.size)==manifest['images'][name]['size'] and min(im.size)>=1600
 assert sha(R/name)==manifest['images'][name]['sha256']
 assert len(im.resize((120,120)).getcolors(14400) or [])>40
assert manifest['comparison']['same_scale'] and manifest['comparison']['versions']==['v7b','v7c']
assert manifest['comparison']['pixels_per_metre']==5.5
review=json.loads((R/'visual-review-v7c.json').read_bytes())
assert review['plan_sha256']==digest and review['result']=='reviewed_candidate'
assert review['owner_approval'] is False and review['images']=={n:sha(R/n) for n in sorted(names)}
assert len(review['observations'])>=4
report=(R.parent.parent/'handoff/eurydica-plan-v7c-last.txt').read_text(encoding='utf-8').splitlines()
assert len(report)==6 and all(report)
assert 'PLAN_CHECK_PASS' in report[1] and '35% aim NOT MET' in report[2] and 'owner approval pending' in report[-1]
from refinements_v7c import roadmetrics,V,V7
assert roadmetrics(p)==c['roads_after'] and roadmetrics(V)==c['roads_v7b'] and roadmetrics(V7)==c['roads_before']
assert f"{c['roads_after']['length_m']:.3f}" in report[2]
assert p['status']=='candidate' and p['v7c_changes']['candidate_only']
print('DELIVERY_CHECK_PASS: checked candidate, three matching reviewed images, preserved originals, appended plan and six-line report; 35% aim shortfall disclosed')
