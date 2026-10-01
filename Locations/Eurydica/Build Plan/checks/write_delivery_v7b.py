"""Document the measured candidate. The only outside-run write is the requested report."""
import sys,json,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parent
p=json.loads((R/'eurydica-plan-v7b.json').read_bytes());m=json.loads((R/'check-result-v7b.json').read_bytes())
assert not m['errors']
assert m['plan_sha256']==hashlib.sha256((R/'eurydica-plan-v7b.json').read_bytes()).hexdigest()
before=m['roads_before'];after=m['roads_after'];green=m['green_irregularity']
doc=R/'Eurydica Build Plan.md';backup=R/'Eurydica Build Plan-before-v7b.md'
if not backup.exists():backup.write_bytes(doc.read_bytes())
section=f'''

## v7b refinements

**Candidate for owner review, 2026-10-01. No Godot or storyboard changes.**
The v7 cluster list, order and membership are retained: {m['buildings']} buildings in {m['clusters']} groups, all ten districts, all six approved connection IDs, {m['markers']} markers, {m['npc_spots']} NPC spots and {m['props']} props. Each group's centroid remains within 5 m of v7. No buildings were added or removed for this pass; facade dimensions, uses, roofs, interior/dormitory restrictions and upgrade parcels are retained. The gate-to-river distance stays **{m['gate_river_m']:.1f} m**.

The controlling reference is **THE LAYOUT RULE** in `D:/Storyboards/Isekai Mercenary Company/Research/Eurydica City References/README.md`, with `f03 illustrated.jpg` inspected again for close, staggered house groups, a winding main road and green gaps. These review images retain v7's plain plan/massing style; they are geometry studies, not painted production art.

### Roads and access

The 7 m main road follows a gently winding sampled curve from the South Gate to the unchanged Old Bridge. Five branch families organise the secondary roads:

| Family | Function |
| --- | --- |
| Guild and gate | Guild delivery ramp and inner gate frontage |
| Arrival courts | West court and east arrival courts, with the Guild-neighbour frontage |
| Service | Market-to-Service lane frontage |
| Workshops and quays | The two retained supply/market connections serving work yards and river loading |
| North bank | Civic approach and fixed ramps serving the Old City circuit and residential/waterworks arm |

New secondary streets are 4 m wide, with the retained Guild delivery access at 5 m; the fixed north-bank ramps retain their original geometry. Court alleys and door spurs are 2 m wide. Shared approaches replace repeated parallel door routes. There is **one bounded route face**, the intended Old City garden circuit, and no route cycle encloses an entire building cluster. The east service perimeter and residential ring are removed. The historical `service_public_loop` ID remains for connection compatibility but is now a short dead-ended arm. Six district connections can share five branch families; their IDs, order, descriptions and endpoint functions remain intact.

| Road measure (all routes, same definition for both plans) | v7 | v7b |
| --- | ---: | ---: |
| Total centreline length | {before['length_m']:,.3f} m | {after['length_m']:,.3f} m |
| Total road union area | {before['union_area_m2']:,.2f} m² | {after['union_area_m2']:,.2f} m² |
| Sum of length × width, before overlap removal | {before['summed_strip_area_m2']:,.2f} m² | {after['summed_strip_area_m2']:,.2f} m² |
| Door-approach centreline length | {before['door_length_m']:,.3f} m | {after['door_length_m']:,.3f} m |

Length falls **{m['road_length_reduction_percent']:.2f}%** and road area falls **{m['road_area_reduction_percent']:.2f}%**. Union areas use identical 0.1 m raster sampling of swept route strips, so they are estimates rather than analytic polygon-union areas. The totals include protected bridges, ramps, decks, stairs and every door spur. Route record count is not a street count: individual door bindings retain separate IDs. Median door-spur length is {m['door_spur_median_m']:.3f} m; the longest is {m['door_spur_max_m']:.3f} m. The gate-to-market walk is {m['gate_market_walk_m']:.3f} m, or {m['gate_market_walk_s_at_3_2']:.3f} seconds at the unchanged 3.2 m/s.

### Organic groups

Frontage angles and small local steps follow the winding streets and court approaches. {m['angled_nonlandmarks']} of 84 non-landmark buildings have nonzero yaw; the angle vocabulary is {', '.join(str(a) for a in m['building_yaws_deg'])} degrees, in 5-degree steps. The median nearest wall gap inside clusters is {m['median_cluster_wall_gap_m']:.3f} m; every non-landmark has a neighbour within 2 m. Intercluster separation remains at least 8 m unless a road separates the groups.

The gate arch stays aligned with the existing wall; its neighbouring buildings turn slightly. The clock tower, Alliance appointment markers, plaza and north-bank terrain stay fixed while the other civic buildings turn. The Guild's story staging and bench/resting positions remain fixed, with its building frontage turned 5 degrees. These anchors take precedence over rotating an entire landmark group as a rigid block. Rotated footprints and roofs are rendered from the same JSON as the checks.

### Organic green

Rectangular grove plots are replaced with **{green['groves']} flowing, concave grove polygons**, with rounded bays and lobes. Their average irregularity is **{green['after_mean']:.4f}**, versus **{green['before_mean']:.4f}** in v7. The measure is `1 - polygon area / axis-aligned bounding-box area`; a rectangle scores zero. Concavity is separately tested against each polygon's convex hull, so simply rotating a rectangle cannot satisfy this check.

A continuous, walkable meadow covers **{m['continuous_intercluster_green_m2']:,.2f} m²** between the groups. The JSON stores this as `green.continuous_cover`: union the domain polygons, then subtract the listed cluster envelopes, routes, structures, designated courts, allotments and reserve. This explicit boolean ground layer fills all intercluster gaps without grass seams between individual buildings. It is a candidate schema extension for a future approved builder; it has not been installed in Godot. The checker reconstructs the exclusions independently and finds **{m['unassigned_intercluster_gap_m2']:.2f} m²** of unassigned intercluster ground at 0.2 m sampling.

The {m['trees']} trees use deterministic varied-spacing placement, with grove groups and individual trees at cluster edges and beside roads. Nearest-neighbour spacing coefficient of variation is {m['tree_spacing_cv']:.4f}; a regular lattice would approach zero. Tree trunks, route corridors, markers and the clock view are checked. The red tree remains in its named open grass-and-earth bed; the Guild resting grass and Service allotment layout are retained.

### Workshop yard and HQ screen

All 20 workshop prop IDs are retained in four purposeful stations: timber and drying/sawing stock, stone/material stock, crates/tools, and carts/working equipment. Their equipment stays against workshop edges; the **84 m²** central working court is free of stock. Review drawings distinguish logs, crates, carts and stone instead of presenting all props as scattered grey blocks.

The HQ expansion reservation and its three upgrade parcels are byte-identical to v7 and remain unbuilt. A low hedge/timber-fence screen sits outside the parcel edges, with a 4 m future access opening and trees along the outside edge. Neither the screen nor trees intrude on reserved construction ground or block routes.

### Verification and deliverables

`check_plan_v7b.py` extends the v7 checker; the original checker and v7 JSON are preserved. It retains identity, dimensions, district/connection topology, protected terrain, door-wall geometry, swept-route collision, graph reachability/height, story staging, marker walkability, NPC bindings, roof/interior rules, red-tree bed, HQ and allotment tests. The v7b extension adds baseline cluster equality, bounded displacement, width/hierarchy, road reductions, short door spurs, enclosed-cluster road-cycle rejection, staggered angles, concave green shapes, continuous meadow coverage, varied tree spacing, purposeful stock stations and an unobstructed HQ screen. It prints **PLAN_CHECK_PASS** only when all checks pass. Negative controls exercise both inherited and refinement failures; details and actual counts are in `check-result-v7b.json`.

- `eurydica-plan-v7b.json`: candidate geometry and explicit meadow/screen/stock records.
- `cluster-map-v7b.png`: labelled, cluster-tinted north-up plan.
- `bird-view-sketch-v7b.png`: north-facing massing study, 40 degrees down, retained roof colours.
- `v7-vs-v7b.png`: both candidates at 5.5 pixels per metre and identical world extents.
- `check-result-v7b.json`, `render-manifest-v7b.json`, `visual-review-v7b.json`, `GATES-v7b.md`: measured and visual evidence bound to the candidate.
- `Eurydica Build Plan-before-v7b.md`: unchanged pre-refinement document; this section is appended to its original bytes.

Reproduce from this directory using `C:/Users/Tristixa-/.codex/skills/sprite-gen/.venv/Scripts/python.exe -B` followed by `build_v7b.py`, `check_plan_v7b.py --self-test`, `render_review_v7b.py`, and `write_delivery_v7b.py`. Render inspection and `check_delivery_v7b.py` complete the review. The owner must approve this candidate before any Godot integration.
'''
doc.write_bytes(backup.read_bytes()+section.encode('utf-8'))
report=[
 'EURYDICA v7b CANDIDATE: 86 buildings / 21 unchanged clusters; no Godot or storyboard writes.',
 f"PLAN_CHECK_PASS: 59 markers, 24 NPC spots, all doors reachable; gate-to-river {m['gate_river_m']:.1f} m.",
 f"Road length {before['length_m']:.3f} -> {after['length_m']:.3f} m (-{m['road_length_reduction_percent']:.2f}%); union area {before['union_area_m2']:.2f} -> {after['union_area_m2']:.2f} m2 (-{m['road_area_reduction_percent']:.2f}%).",
 f"Green irregularity {green['before_mean']:.4f} -> {green['after_mean']:.4f}; {green['groves']} concave groves, continuous meadow, varied trees; four workshop piles and screened HQ reserve.",
 'Deliverables: eurydica-plan-v7b.json, cluster-map-v7b.png, bird-view-sketch-v7b.png, v7-vs-v7b.png; Eurydica Build Plan.md updated.',
 'Folder: D:/Codex/IMC/runs/eurydica-plan-v7/ | Candidate awaits owner approval; v7 originals preserved.'
]
Path('D:/Codex/IMC/handoff/eurydica-plan-v7b-last.txt').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('DELIVERY_WRITTEN_V7B')
