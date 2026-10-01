import json,sys,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
P=json.loads((R/'eurydica-plan.json').read_bytes());B=json.loads((R/'baseline/approved-v4/eurydica-plan.json').read_bytes());M=json.loads((R/'check-result.json').read_text())
intro='''# Eurydica Build Plan v5 — candidate

## v5 changes

29 September 2026. This is a localized candidate based on the owner-approved v4 (28 September). The v4 text below is retained byte-for-byte as historical context; this section supersedes it only for the six requested refinements. JSON is authoritative. No game or storyboard files were modified.

1. **Market frontage:** `infill_home_12` becomes a provisions shop; `infill_home_06` a small sundries shop; `street_home_8` a bakery; `infill_home_23` a small cloth shop. Green roofs follow their business use. All four keep their exact footprint, yaw, height, door and route. The cloth shop uses the existing southern seam at z116.5–123.5, immediately beyond the approximate z115 limit, avoiding any new building. Existing provisions, tavern and Repair & Supply retain their identities. Four new candidate facade contracts match the existing dimensions. Three clusters of three awning stalls occupy the red-tree court, widened spine edge and southern market seam. Each has separate crates, baskets and a barrow. Their footprints include awnings; the full 8 m travel strip and all door approaches remain clear.
2. **Gap activity (round-1 density correction):** `spine_service_allotments` now fills a **30 ? 42 m / 1,260 m?** patch, with **10 varied beds**, a low perimeter fence, a **3 m east-side public gate**, tool shed, water butt, compost and two fruit trees at the southern edge. Existing trees remain byte-identical. Bed-to-bed gaps are at least 2 m; a connected 1.2 m body corridor reaches every bed and facility from the Service Lanes. **Workshop and Quays each have 20 props**, clustered beside building walls, stock and workstations. Quays adds barrels, rope, crates and timber, a lean-to, three carts, weighing bench and hand hoist on the northern water side; its footprint reaches z=-3, seven metres back from the retained river edge. Workshop adds stone/timber stacks, sawhorses, three wall benches plus an east bench, drying rack, scrap piles and a tool shed. The 6 m work loop and every retained door approach stay clear. Open central working ground remains intentional.

3. **Roof kit:** all 83 buildings receive `roof_kit`. Reuse gable/shed dormers, squat stone chimneys, recessed upper bays and a modest corner roof variant. Tavern and Old Hall have the strongest combination; selected homes use attachments at roughly one in three, work buildings stay restrained, and the clock tower keeps its existing silhouette. Recessed bays and attachments must remain within the existing plan/height envelope. The two party-wall homes retain flush seams; no new eaves over shared walls. Roof colours change only on the four market businesses. See `roof-kit-schedule.md`; mesh/occlusion checks remain later production work.
4. **Civic stage:** five leaders in a shallow south-facing arc, Commander facing them, five officers behind him, envoy beside the leaders, and a nonphysical camera ground anchor. All 12 figure anchors are in the existing clock plaza, at ground y=2 m. Minimum centre spacing is 1.80 m; using 0.5 m body diameters leaves 1.30 m clear between bodies, exceeding 1.2 m. The tower and notice shelter remain clear. No plaza polygon change is needed. Temporary scene occupants are not permanent collision props. The camera hint does not replace the approved city camera contract.
5. **Envoy arrival:** `south_gate/envoy_arrival` sits just inside the gate at (-1.5,296); `guild_courtyard/envoy` sits at (-27,290), clear of Elsie's existing staging. All original markers remain unchanged.
6. **Adventurer quarters:** the Guild two-bed upper-floor dormitory and its stair are `player_access: false`, reason `adventurers' quarters`. New future portal policy records bind the Dorm Annex and Larger Dorm to the same restriction, with NPC access allowed. Their future coordinates are deliberately unresolved until construction inside the unchanged reserved parcels. Existing Guild/Tavern entry portals are untouched. Two evening NPC spots each occupy the Guild main room, Guild courtyard and tavern common room. Candidate evening start is 18:00; the owner-fixed cutoff is 21:00 exclusive. Two separate courtyard grass resting patches support resting/injured adventurers using field-sleep sprites.

### Verification and review

`check_plan.py --self-test` prints **PLAN_CHECK_PASS**. It retains v4's geometry, graph, rotation, tower, timing and facade checks and adds a strict v4 edit allowlist, footprint collisions, zone checks, awning cluster counts, new-marker reachability, figure spacing, access flags, evening schedules and resting footprints. Negative controls deliberately violate routes, stalls, roof kits, figure spacing, access, schedules and zones; new controls remove yard props, beds and stall accessories or block the public garden gate. Accepted round-1 features outside props and the allotment zone are checked against the archived candidate.

The gate-to-market route is unchanged: **217.808 m / 68.065 seconds at 3.2 m/s**, inside 45–90 s. Phase 1, HQ reservation, districts, routes, six junctions, terrain and all pre-existing coordinates are retained. `byte-diff-summary.md/.json` list every changed/added ID and prove unchanged JSON spans at byte level. `byte-edit-manifest.json` records offsets. `baseline/approved-v4/` preserves the approved source package.

`eurydica-plan.svg/.png` and the four `review/` diagram pairs are deterministic JSON renders: market/red-tree court, allotments, Workshop/Quays yards, Civic Terrace group. They are measured planning diagrams, not new painted finish concepts or engine captures. The inherited v4 illustrations remain under `baseline/approved-v4/review/` as historical references. No image-generation step was used.

[Before/after review links](review/README.md) compare the four revised diagrams against `superseded/round-1/review/`. The replaced JSON, images, verification reports and build scripts are archived in `superseded/round-1/`.

`markers.md` is a candidate retaining the existing marker document and appending the new names, scene bindings and coordinates. All v5 outputs await owner approval. Runtime access enforcement, NPC schedules, meshes, art and camera behavior are not installed by this planning task.

---

'''
(R/'Eurydica Build Plan.md').write_bytes(intro.encode('utf-8')+(R/'baseline/approved-v4/Eurydica Build Plan.md').read_bytes())
source=Path('D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/markers.md').read_bytes()
lines=['','', '## v5 candidate additions — 29 September 2026','','Qualified IDs below are exact JSON IDs. Coordinates are (x,z) metres in the stated scene; north is -z. These append to the original marker text above. The two existing interior portal mappings remain unchanged.']
groups=[('Civic Terrace (Alliance appointment)','civic_terrace/'),('South Gate (envoy arrival)','south_gate/'),('Guild courtyard (envoy, evening and resting)','guild_courtyard/'),('Guild interior (evening adventurers)','guild_interior/'),('Tavern interior (evening adventurers)','tavern_interior/')]
for title,prefix in groups:
 lines+=['','## '+title,'']
 for m in P['markers'][len(B['markers']):]:
  if not m['id'].startswith(prefix):continue
  desc='suggested nonphysical diorama push-in ground anchor; look toward Commander' if m.get('kind')=='camera_hint' else 'grass resting patch for resting/injured adventurer; field-sleep sprite permitted' if m.get('rest_spot') else 'adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive' if 'evening' in m['id'] else 'behind the Commander' if 'officers_' in m['id'] else 'shallow leadership arc' if 'leaders_' in m['id'] else 'beside the leaders' if m['id']=='civic_terrace/envoy' else 'faces the leadership arc' if m['id']=='civic_terrace/commander' else 'just inside the gate' if prefix=='south_gate/' else "courtyard arrival, clear of Elsie's staging"
  lines.append(f"- `{m['id']}`: {desc}; {m['scene']} ({m['position'][0]}, {m['position'][1]}), ground y={m['height_m']} m"+(f", facing {m['facing']}" if 'facing' in m else '')+'.')
(R/'markers.md').write_bytes(source+'\n'.join(lines).encode('utf-8')+b'\n')
lines=['# Roof-kit candidate schedule','','Every entry retains the existing footprint, yaw, roof colour (except the four authorized market uses) and total height. Attachments fit within those bounds; bays are recessed within the upper wall envelope. Empty lists intentionally mean no attachment. No smoke, lights or new ground collision are baked in.','','| Building ID | Use | Dormers | Chimneys | Bays | Variant |','|---|---|---|---|---|---|']
for b in P['buildings']:
 k=b['roof_kit'];lines.append('| `'+b['id']+'` | '+b['role']+' | '+', '.join(k['dormers'])+' | '+', '.join(k['chimneys'])+' | '+', '.join(k['bays'])+' | '+k['roof_variant']+' |')
(R/'roof-kit-schedule.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(R/'README.md').write_text('''# Eurydica Build Plan v5 — candidate

Localized update of owner-approved v4. Awaiting owner approval; no runtime integration.

- [Build plan and six changes](Eurydica%20Build%20Plan.md)
- [Authoritative JSON](eurydica-plan.json)
- [Full plan PNG](eurydica-plan.png) / [SVG](eurydica-plan.svg)
- [Market and red-tree court](review/market-red-tree-court.png)
- [Allotments](review/spine-service-allotments.png)
- [Workshop and Quays yards](review/workshop-quays-yards.png)
- [Civic ceremony layout](review/civic-terrace-group.png)
- [Round-1 before/after links](review/README.md)
- [Marker candidate](markers.md) / [Roof-kit schedule](roof-kit-schedule.md)
- [Byte-level preservation and every changed/added ID](byte-diff-summary.md)
- [Check measurements and negative controls](check-result.json)

Reviews are top-down measured diagrams rendered from JSON, not painted concept images. The baseline folder is a byte copy of v4, including historical reviews. Four new review areas only; nothing published to the storyboard or game.

With Python 3.10+ and Pillow: `python check_plan.py --self-test`, `python render_plan.py`, `python write_docs.py`, then `node verify_run.mjs preservation` and `node verify_run.mjs delivery`. On this machine `verify_run.mjs` resolves the existing sprite-gen Python environment. Source checks read the approved v3/v4 and storyboard contracts; no source files are written. `build_v5.py` reproduces the surgical JSON edits; `prepare_checks.py` extends the inherited v4 checker.

The walk remains 68.065 s. The ceremony has 1.80 m centre spacing / 1.30 m body-edge spacing, with no plaza changes. `GATES.md` records completion evidence. V5 does not approve new art or implement NPC/access behavior in the game.
''',encoding='utf-8')
sys.dont_write_bytecode=True
import check_v5
result=check_v5.byte_report()
report=[ 'Eurydica v5 density fixes complete; candidate awaiting owner approval.', 'Run: D:/Codex/IMC/runs/eurydica-plan-v5/ (JSON, build plan, README, markers and roof-kit schedule).', 'Density fixes: 20 props per yard, 10 allotment beds with facilities, and three clusters of three stalls plus accessories; accepted v5 locks retained.', 'PLAN_CHECK_PASS; walk 68.065 s; civic spacing 1.80 m centres / 1.30 m body edges; plaza unchanged.', f"BYTE_DIFF_PASS: {result['retained_bytes']:,}/{result['source_bytes']:,} source bytes retained; all changed/added IDs listed in byte-diff-summary.md.", 'Four updated review pairs with before/after links; replaced JSON/images in superseded/round-1; project/storyboard untouched.' ]
(R.parent.parent/'handoff/eurydica-plan-v5-fixes-last.txt').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('DOCS_PASS')
