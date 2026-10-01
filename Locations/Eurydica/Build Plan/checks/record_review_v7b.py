"""Record the completed visual inspection of the three final review images."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
review={
 'result':'pass','owner_approval':False,'status':'candidate',
 'plan_sha256':sha(R/'eurydica-plan-v7b.json'),
 'images':{name:sha(R/name) for name in sorted(('cluster-map-v7b.png','bird-view-sketch-v7b.png','v7-vs-v7b.png'))},
 'reference':{'path':'D:/Storyboards/Isekai Mercenary Company/Research/Eurydica City References/f03 illustrated.jpg',
  'role':'Clustered layout, winding road and green gaps; not rendering style'},
 'observations':[
  'The main route remains visually dominant. South-bank perimeter lanes are removed; front court accesses read as short branches. The sole northern circuit encloses a communal garden, not a building group.',
  'All 21 numbered groups retain their v7 locations and membership. Roof groups turn and step relative to one another; the straight-north oblique view shows the same yaw changes as the plan.',
  'Continuous light meadow and darker, rounded concave groves replace rectangular grove plots. The previously bare strip behind the civic terrace is now planted. Tree spacing and canopy sizes vary.',
  'Timber stock, crate/tools, stone/material piles and carts sit along workshop edges around a clear working court. Log lines, crate crosses, stone mounds and cart wheels distinguish purpose without changing collision sizes.',
  'The HQ reserve stays visibly clear within a low boundary screen with edge trees and an opening toward the Guild. The red tree remains in its green-earth court bed.',
  'All titles, cluster legends, scale bars and comparison labels fit. The comparison uses identical extents and pixels per metre; the oblique view uses retained roof colours and 40-degree downward projection.',
 ],
 'limits':['Unpainted geometry review, as requested.','Not a Godot capture, runtime occlusion test or owner approval.']
}
review['reference']['sha256']=sha(Path(review['reference']['path']))
path=R/'visual-review-v7b.json';path.write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
gate=R/'GATES-v7b.md';text=gate.read_text(encoding='utf-8-sig')
start=text.index('- [ ] G3:') if '- [ ] G3:' in text else text.index('- [x] G3:')
prefix=text[:start];block=text[start:];title=block.splitlines()[0].replace('- [ ]','- [x]')
evidence='Viewed all three final PNGs, including the repaired north meadow and stock piles; v7 style and f03 grouping reviewed. visual-review-v7b.json sha256='+sha(path)+'; owner approval remains pending.'
gate.write_text(prefix+title+'\n  EVIDENCE: '+evidence+'\n',encoding='utf-8')
print('VISUAL_REVIEW_RECORDED')
