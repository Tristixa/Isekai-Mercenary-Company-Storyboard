"""Artifact freshness and preservation checks; never approves the candidate."""
import sys,json,hashlib
from pathlib import Path
from PIL import Image
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
plan=R/'eurydica-plan-v7b.json';p=json.loads(plan.read_bytes());digest=sha(plan)
check=json.loads((R/'check-result-v7b.json').read_bytes())
assert check['plan_sha256']==digest and not check['errors'],'Plan checks stale/failing'
assert len(check.get('negative_controls',[]))>=22,'Inherited controls incomplete'
assert len(check.get('v7b_negative_controls',[]))>=6,'Refinement controls incomplete'
for name,d in check['checker_sources'].items():assert sha(R/name)==d,'Checker source changed '+name
source=json.loads((R/'source-manifest-v7b.json').read_bytes())
for name,d in source.items():
 if name=='Eurydica Build Plan.md':continue
 assert sha(R/name)==d,'Original v7 file changed '+name
backup=R/'Eurydica Build Plan-before-v7b.md';doc=R/'Eurydica Build Plan.md'
assert sha(backup)==source[doc.name],'Original document backup mismatch'
assert doc.read_bytes().startswith(backup.read_bytes()),'Original document content changed'
text=doc.read_text(encoding='utf-8');assert text.count('## v7b refinements')==1
for s in ('PLAN_CHECK_PASS','Candidate for owner review','continuous_cover','5.5 pixels per metre'):
 assert s in text,'Missing documentation '+s
manifest=json.loads((R/'render-manifest-v7b.json').read_bytes())
assert manifest['plan_sha256']==digest,'Stale render geometry'
assert manifest['renderer_sha256']==sha(R/'render_review_v7b.py'),'Renderer changed after output'
names={'cluster-map-v7b.png','bird-view-sketch-v7b.png','v7-vs-v7b.png'}
assert names==set(manifest['images'])
for name in names:
 path=R/name;im=Image.open(path);im.verify();im=Image.open(path)
 assert list(im.size)==manifest['images'][name]['size'] and min(im.size)>=1600
 assert sha(path)==manifest['images'][name]['sha256'],'Image checksum mismatch '+name
 assert len(im.resize((120,120)).getcolors(14400) or [])>40,'Blank/flat image '+name
assert manifest['comparison']['same_scale'] and manifest['comparison']['pixels_per_metre']==5.5
assert manifest['bird_view']['direction']=='north' and manifest['bird_view']['down_angle_degrees']==40
review=json.loads((R/'visual-review-v7b.json').read_bytes())
assert review['plan_sha256']==digest and review['result']=='pass','Visual review missing/stale'
assert review['images']=={name:sha(R/name) for name in sorted(names)},'Images changed after visual review'
assert len(review['observations'])>=4
report=Path('D:/Codex/IMC/handoff/eurydica-plan-v7b-last.txt').read_text(encoding='utf-8').splitlines()
assert len(report)==6 and all(report),'Report must contain exactly six nonempty lines'
assert 'PLAN_CHECK_PASS' in report[1] and 'owner approval' in report[-1]
from refinements_v7b import roadmetrics,V
assert roadmetrics(V)==check['roads_before'] and roadmetrics(p)==check['roads_after'],'Road measures stale'
assert f"{check['roads_after']['length_m']:.3f}" in report[2]
assert f"{check['green_irregularity']['after_mean']:.4f}" in report[3]
print('DELIVERY_CHECK_PASS: three reviewed images, matching plan/checks, unchanged v7 originals, updated document, six-line report')
