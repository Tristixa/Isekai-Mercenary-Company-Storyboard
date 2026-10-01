"""Append the scoped candidate record and requested six-line handoff report."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
P=json.loads((R/'eurydica-plan-v7c.json').read_bytes());M=json.loads((R/'check-result-v7c.json').read_bytes())
assert not M['errors']
digest=hashlib.sha256((R/'eurydica-plan-v7c.json').read_bytes()).hexdigest()
assert M['plan_sha256']==digest
a=M['roads_after'];before=M['roads_before'];b=M['roads_v7b']
doc=f'''

## v7c — final four-point refinement

**Candidate for owner review. No Godot or storyboard files changed; owner approval pending.**

Source: `eurydica-plan-v7b.json`, SHA-256 `{P['source_v7b_sha256']}`.
Candidate: `eurydica-plan-v7c.json`, SHA-256 `{digest}`.
Reviewed layout reference: `D:/Storyboards/Isekai Mercenary Company/Research/Eurydica City References/f03 illustrated.jpg`.
The reference guides the soft road bends and grouped foliage; these images remain deterministic geometry reviews drawn from the plan.

### The four changes

1. The 7 m main road makes two soft S-curves with approximately ±7 m lateral displacement. The South Gate endpoint `[0,118]` and Old Bridge endpoint `[0,-5]` stay fixed. Lodging and market frontage clusters shift 2.5 m east as rigid groups; their existing angles, buildings and internal gaps are retained. Doors and their shared approaches are recalculated against the curved road.
2. Five connected branch networks serve Guild/gate/neighbours, arrival/orchard courts, Service Lanes/homes/garden row, workshop/quay yards, and the north bank. The two Guild arms share the same main-road attachment; the workshop branch grows out of the arrival/orchard branch. The duplicated quay-to-main-road link, service-to-arrival return and old park return are removed. The north bank has one principal civic/old-city/residential circuit with waterworks and retained deck access. Short door spurs and narrow court alleys remain explicit geometry, and unused terminal paving is pruned. Maximum door spur: **{M['door_spur_max_m']:.3f} m**, median **{M['door_spur_median_m']:.3f} m**. Shared alleys are included in all totals.
3. **{M['grove_trees']} of {M['trees']} trees ({M['grove_tree_percent']:.2f}%)** occupy **{M['grove_count']} groves**. Every grove has 8–25 trees and a connected set of overlapping canopies. Open meadow separates the clumps. The red tree, HQ-edge accents and two civic trees remain individually identifiable.
4. The civic paving surface itself and the clock-plaza polygon now share an irregular boundary fitted to the tower and adjacent civic frontages. A small planted island with two trees sits inside the eastern edge. All Alliance appointment markers retain their exact positions and spacing on paving. The south-east enclosure becomes an irregular household yard with broken hedges, stepped produce groups, a tool/stock group and a west-side opening. The source calls this `spine_service_allotments`; existing uses and all object IDs are retained. The five old fence runs are stored as short panel stacks beside the shed, conserving their original total lengths rather than keeping a rectangular fence.

### Road measurements and the requested aim

| Whole network, same measurement method | v7 | v7b | v7c |
|---|---:|---:|---:|
| Centreline length (m) | {before['length_m']:.3f} | {b['length_m']:.3f} | {a['length_m']:.3f} |
| Union paved/route footprint (m²) | {before['union_area_m2']:.2f} | {b['union_area_m2']:.2f} | {a['union_area_m2']:.2f} |
| Sum of strip areas before overlaps (m²) | {before['summed_strip_area_m2']:.2f} | {b['summed_strip_area_m2']:.2f} | {a['summed_strip_area_m2']:.2f} |

Relative to v7: **{M['road_length_reduction_percent']:.2f}% less length and {M['road_area_reduction_percent']:.2f}% less area**.
**The 35% reduction aim is not met.** The checked layout retains every door, the fixed bridge/ramps/decks, and the requested north-bank circuit. No road is omitted from measurement to improve the percentage. This is a measured shortfall, not a claim that further reduction is impossible. Union area uses the inherited 0.1 m raster sampling; length includes every route record, including shared court links and door spurs.

### Verification and retained constraints

`PLAN_CHECK_PASS`: {M['buildings']} buildings, {M['clusters']} clusters, {M['markers']} markers, {M['npc_spots']} NPC bindings and {M['props']} props. All v7b cluster membership lists remain identical. All {M['nonlandmark_population_after']} ordinary buildings retain a neighbour within 0–2 m; median wall gap is {M['median_cluster_wall_gap_m']:.3f} m. Graph reachability covers all doors and city markers. Gate-to-river distance is **{M['gate_river_m']:.1f} m**. Minimum civic body clearance remains **{M['civic_min_body_clearance_m']:.1f} m**.

Inherited geometry, collision, elevation, identity, marker/NPC, Guild staging, HQ reservation, roof, terrain, red-tree and yard-access checks remain active. Task-superseded assertions are explicitly replaced: six historic attachments are remapped to current branches; the fixed plaza outline becomes exact appointment/paving checks; rigid allotment translation becomes dimension/material-conservation and accessible-aisle checks; the old local garden-ring IDs become current loop geometry. No errors are filtered from a failed check run. The 35% aim is reported separately from safety/functional pass status.

The current check result records inherited negative controls and v7c controls for flattened roads, missing groves, lost civic planting, a rectangular yard and missing pile groups. `source-manifest-v7c.json` and `Eurydica Build Plan-before-v7c.md` verify preservation of every prior run file and the prior document prefix. The delivery checker binds plan, checker, renderer and reviewed image hashes.

### Review files

- `cluster-map-v7c.png` — numbered north-up cluster map with doors, grove planting and revised yards.
- `bird-view-sketch-v7c.png` — north-facing massing at 40° down, with retained roof palettes.
- `v7b-vs-v7c.png` — equal extents and 5.5 pixels per metre on both sides, with measured road totals.

These are candidate geometry sketches, not a Godot capture or runtime camera/occlusion approval. Nothing is installed until the owner approves.
'''
backup=(R/'Eurydica Build Plan-before-v7c.md').read_bytes()
(R/'Eurydica Build Plan.md').write_bytes(backup+doc.encode('utf-8'))
lines=[
 f'V7C CANDIDATE: 86 buildings, 21 unchanged clusters, 59 markers; eurydica-plan-v7c.json SHA-256 {digest}.',
 f'PLAN_CHECK_PASS: all doors/markers reachable; wall gaps 0-2 m; Alliance clearance {M["civic_min_body_clearance_m"]:.1f} m; gate-to-river {M["gate_river_m"]:.1f} m.',
 f'ROADS: {a["length_m"]:.3f} m / {a["union_area_m2"]:.2f} m2; {M["road_length_reduction_percent"]:.2f}% / {M["road_area_reduction_percent"]:.2f}% below v7; 35% aim NOT MET; five connected branch groups, spurs <=12 m.',
 f'FORM: two +/-7 m S-curves; {M["grove_trees"]}/{M["trees"]} trees ({M["grove_tree_percent"]:.2f}%) in {M["grove_count"]} groves; irregular civic paving and hedged south-east yard with grouped stock.',
 'DELIVERY: cluster-map-v7c.png, bird-view-sketch-v7c.png, v7b-vs-v7c.png; v7c section appended to Eurydica Build Plan.md; prior files preserved.',
 'STATUS: candidate only, owner approval pending; no Godot or storyboard changes; report and candidate saved in the requested locations.'
]
(R.parent.parent/'handoff/eurydica-plan-v7c-last.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('V7C_DOCUMENT_AND_SIX_LINE_REPORT_WRITTEN')
