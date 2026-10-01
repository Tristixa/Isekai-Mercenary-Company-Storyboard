"""Bind the completed manual image review and read-only source inventory."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((R/'render-manifest.json').read_bytes())
assert manifest['plan_sha256']==digest(R/'eurydica-plan.json')
refs=Path('D:/Storyboards/Isekai Mercenary Company/Research/Eurydica City References')
names=['f01 Top Down.jpg','f02 bird view.jpg','f03 illustrated.jpg','f04 walled city.webp']
review=dict(verdict='reviewed_candidate',date='2026-10-01',plan_sha256=manifest['plan_sha256'],images={name:digest(R/name) for name in manifest['images']},references_reviewed=names,notes='visual-review.md',owner_approved=False)
(R/'visual-review.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
base=Path('D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/Archive/Build Plan v5')
paths=[refs/name for name in names]+[refs/'README.md',base/'eurydica-plan.json',base/'Eurydica Build Plan.md',base/'checks/check_plan.py',base/'checks/check_v5.py',base/'checks/inherited_checks.py',Path('D:/Storyboards/Isekai Mercenary Company/Environment Assets/Eurydica/Approved Facades v1/facades-spec.json')]
(R/'source-manifest.json').write_text(json.dumps(dict(files=[dict(path=str(p),sha256=digest(p)) for p in paths]),indent=2)+'\n',encoding='utf-8')
print('REVIEW_AND_SOURCE_BINDINGS_WRITTEN')
