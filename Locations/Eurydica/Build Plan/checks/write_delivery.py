"""Produce the measured candidate documentation; report is an explicit final step."""
import json,hashlib,sys
from pathlib import Path
R=Path(__file__).resolve().parent
P=json.loads((R/'eurydica-plan.json').read_bytes());M=json.loads((R/'check-result.json').read_bytes())
assert not M['errors'] and M['plan_sha256']==hashlib.sha256((R/'eurydica-plan.json').read_bytes()).hexdigest()
names={d['id']:d['name'] for d in P['districts']}
lines=['# Eurydica Build Plan v7 — clustered city candidate','',
'Owner review package, 1 October 2026. JSON is authoritative. This candidate is not owner-approved and has not been installed in Godot. All original v5 building dimensions, identities, uses and roof kits are retained. This is a new clustered layout; it does not reuse the rejected v6 approach.','',
'## v7 changes','',
'The south bank is organized as a gate group, Guild compound, lodging frontage, arrival courts, red-tree court, market shop row and household blocks. Retained surplus homes form five supplemental groups, rather than remaining isolated. North-bank buildings form five groups around the fixed civic landmark and terraces; shared orchards and groves fill the interstitial ground.','',
'Buildings retain their individual v5 dimensions. Layout yaw is reset to zero to make continuous street fronts and shared-wall seams. The nearest non-landmark neighbour within each group is at most 2 m away. Separate groups have at least 8 m wall clearance, except where an explicit road separates them. The new named green spaces replace v5’s blanket base lawns and per-house garden/hedge layout.','',
'The task’s explicit clustered-city rule supersedes the environment skill’s general open-space ratio. No footprint scaling, facade invention, game rebuilding or painted image generation was used.','',
'### Cluster schedule','',
'The following table includes every building, using stable v5 IDs. Numbers match both review maps.','',
'| No. | Cluster ID / name | District / phase | Buildings | Form and purpose |',
'|---|---|---|---|---|']
for i,c in enumerate(P['clusters']):
 lines.append(f"| {i+1} | `{c['id']}` — {c['name']} | {names[c['district']]} / {c['phase']} | {', '.join('`'+id+'`' for id in c['building_ids'])} | {c['purpose']} |")
lines+=['',
'The four existing market facade bindings retain their stable IDs: `infill_home_12` = market_provisions, `street_home_8` = market_bakery, `infill_home_06` = market_small_shop_east, and `infill_home_23` = market_small_shop_south. The red-tree group puts the tavern to the west, provisions to the south, and bakery/provisions shop to the north. Its nine awning stalls and accessories occupy the court; the tree itself stands in a 25 m² open grass-and-earth bed, above paving in surface priority.','',
'### Measured before and after','',
'Both nearest-neighbour medians below use the same rule: all buildings except South Gate and clock tower, with each building compared to every other building. This differs slightly from v5’s historical exempt-building population. Distances use wall polygons, including v5 rotations, not centres.','',
'| Metric | v5 | v7 |','|---|---:|---:|',
f"| Buildings | {M['buildings_before']} | {M['buildings']} |",
f"| Building footprint area, m² | {M['v5_building_area_m2']:.2f} | {M['building_area_m2']:.2f} |",
f"| Total plan extent, m² (includes river/cliff) | {M['v5_extent_area_m2']:.0f} | {M['extent_area_m2']:.0f} |",
f"| Median nearest wall gap, m | {M['v5_all_nearest_median_m']:.4f} | {M['v7_all_nearest_median_m']:.4f} |",
f"| Ordinary buildings with a neighbour within 2 m | {M['v5_nonlandmarks_with_neighbour_at_2m']}/{M['nonlandmark_population_before']} | {M['v7_nonlandmarks_with_neighbour_at_2m']}/{M['nonlandmark_population_after']} |",
f"| Explicit v7 clusters | Not the v7 schedule | {M['clusters']} (3–6 buildings each) |",
f"| Gate inner face to river edge, m | {M['v5_gate_river_m']:.1f} | {M['gate_river_m']:.1f} |",
f"| Gate-to-market walk, m | {M['v5_gate_market_walk_m']:.3f} | {M['gate_market_walk_m']:.3f} |",
f"| Same walk at retained 3.2 m/s, seconds | {M['v5_gate_market_walk_s']:.3f} | {M['gate_market_walk_s_at_3_2']:.3f} |",
'',
f"At a 2 m/s stroll, the new gate-to-market path takes {M['gate_market_stroll_s_at_2']:.3f} seconds. The inherited v5 45–90-second target at 3.2 m/s is **not met** by this shorter bank; it is retained in JSON as historical metadata, explicitly superseded by the owner’s 120–150 m gate-to-river constraint. No runtime movement speed is changed. The same-scale sheet makes this size change visible rather than enlarging v7 to fill the old footprint.",
'',
'### Added buildings','',
'| Stable ID | Approved facade reuse | Footprint | Roof |','|---|---|---|---|']
for id in M['added_buildings']:
 b=next(b for b in P['buildings'] if b['id']==id);f=b['footprint'];lines.append(f"| `{id}` | `{b['facade_id']}` | {f[2]-f[0]:g} × {f[3]-f[1]:g} m | {b['roof_palette']} |")
lines+=['',
'The service addition uses the approved `house_violet` footprint with the Service Lanes warm-red roof override, as retained service infill already does. All retained facades and roof colours remain unchanged.','',
'### Roads, topology and terrain','',
'One 7 m main road gently bends between South Gate and Old Bridge. Four-to-five-metre branches serve the workshop, quays and service loop; courts use 2–3 m alleys. Individual 2 m door approaches are access strips, not additional arterial roads. The six connection IDs, route-ID sets and purposes are unchanged; their junction order from south to north is **5 → 4 → 1 → 6 → 3 → 2**.','',
'| Connection | New junction (x, z), m | Retained route IDs |','|---|---|---|---|']
# Correct the table separator to three columns.
lines[-1]='|---|---|---|'
for c in sorted(P['approved_connections'],key=lambda c:c['id']):lines.append(f"| {c['id']} | ({c['junction'][0]:.3f}, {c['junction'][1]:g}) | {', '.join('`'+r+'`' for r in c['route_ids'])} |")
lines+=['',
'The river, Old Bridge, north terraces, retaining walls, ramps, stairs, rear cliff, waterworks feeder and covered crossing retain v5 geometry. The tower remains centred at (0, −70), ground y=2 m. Alliance appointment markers are unchanged, including figure spacing and camera anchor. The clock plaza remains clear of other buildings and props, and the bridge-axis clock sightline is checked against building envelopes and tree canopies.','',
'The Guild platform is relaid at y=0.6 m with the explicit approach ramp. Its unchanged-size 552 m² HQ reservation is immediately west of the compound at x=−77…−54, z=99…123. The three upgrade parcels, construction rules and dormitory restrictions remain. Reservation land is kept clear of buildings, roads, trees and props.','',
'### Narrative, use and activity','',
f"All {M['markers']} marker IDs, {M['npc_spots']} NPC-spot IDs and {M['props']} prop IDs remain. Interior geometry and markers are unchanged. Guild processing, bench, envoy and evening/rest staging translate together by −175 m in z; shop/stable markers follow their relocated doors. All city markers have clear body space, surface heights and connections to the gate’s route graph. The two resting grass patches remain within Guild courtyard staging.",
'',
'Player access stays false for the existing dormitory/stair and future dorm portals. NPC schedules and chapter availability remain unchanged. All roof kits, stall awnings, stock props and allotment beds retain their dimensions and uses. Workshop and quay props are within their working zones and district bounds. The ten-bed allotment translates rigidly, preserving its 3 m east gate and original tending aisles; a 1.2 m body corridor is flood-filled to every facility.','',
'### Green-space accounting','',
f"There are {M['named_green_spaces']} named green spaces totalling **{M['green_area_m2']:,.2f} m²**, including **{M['north_green_area_m2']:,.2f} m²** on the north bank. This is the sum of disjoint explicit polygons, including the allotment’s beds and tending aisles and the two small Guild rest patches; it is not a claim that all of that area is lawn. {M['trees']} tree records include the red tree. Intercluster regions are clipped around roads, whole cluster envelopes, props, markers and the HQ reserve. Contiguous accepted 2 m authoring cells are merged into rectangles; the exact polygon areas are checked for overlap before summing.",
'',
'| Named location | Area, m² |','|---|---:|']
for s in M['green_locations']:lines.append(f"| {s['name']} | {s['area_m2']:.2f} |")
lines+=['',
'### Checker migration and evidence','',
'The package retains v5’s `inherited_checks.py` unchanged as the standard-library polygon, rotation, route-graph and shortest-path kernel. `v5-check-plan-source.txt` preserves the prior entry point for provenance. Its absent sibling-version dependencies, historical byte allowlist and fixed 300 m southern coordinates cannot be used as v7 layout rules. `check_plan.py` replaces those obsolete rules explicitly and calls `detail_checks.py`; it does not filter failures out of the old run.','',
'The v7 checks enforce source identity and facade dimensions, roof kits, district order and containment, all scheduled cluster functions, cluster size/membership/gaps, road separation, overlaps, connected doors, exact door faces, slopes and graph elevation continuity, marker and rest-body clearance, phase containment, protected northern geometry, unchanged appointments, HQ parcels, dorm restrictions, green area/placement and allotment aisle reachability. Negative controls deliberately damage these features and must be rejected.','',
f"Latest validation: **PLAN_CHECK_PASS**, zero errors, {M['graph_nodes']} route-graph nodes. {len(M.get('negative_controls',[]))} control cases recorded in `check-result.json`. Report and render manifests bind the delivered plan with SHA-256 `{M['plan_sha256']}`.",
'',
'### Review images and limits','',
'- `cluster-map.png`: north-up tinted groups, numbered cluster/district legend, roads, doors, greens and HQ reserve.',
'- `same-scale-comparison.png`: v5 and v7 at exactly 4 px/m using the same world bounds. f01 is deliberately omitted because its dimensional scale cannot be established reliably.',
'- `bird-view-sketch.png`: boxes, roof colours and tree blobs seen northward at 40° down. This uses an orthographic massing projection to show the whole town consistently; it is not a gameplay-perspective capture.',
'',
'Owner references f01–f04 were opened and studied. f03 guides the district → cluster → building hierarchy; the references guide layout only, not painted style. This package is a reviewable construction plan. Facade face/door adaptation, shared-wall eave suppression, final roof meshes, perspective occlusion/cutaways, physics and playable feel still require the later approved Godot blockout. Those are not claimed as tested here.','',
'## Reproduce','',
'Run in this directory with Python 3.10+ and Pillow:','',
'```text','python -B build_v7.py','python -B check_plan.py --self-test','python -B render_review.py','python -B write_delivery.py','python -B check_delivery.py --preflight','```','',
'After final visual review, `write_delivery.py --report` replaces the six-line handoff report. `run_gates.mjs` executes the two reviewed check commands and records their real output fingerprints locally; it uses no global approval store, respecting the task’s write boundary.','']
(R/'Eurydica Build Plan.md').write_text('\n'.join(lines),encoding='utf-8')
readme=f'''# Eurydica v7 — candidate ready for owner review

The new layout retains all 83 v5 building identities and adds three approved-facade homes: **{M['buildings']} buildings in {M['clusters']} clusters**. Gate-to-river distance is **{M['gate_river_m']:.1f} m**. No Godot or storyboard files were changed.

Start with [the cluster map](cluster-map.png), then [the same-scale comparison](same-scale-comparison.png) and [the north-facing massing view](bird-view-sketch.png).

- [Build plan and metrics](Eurydica%20Build%20Plan.md)
- [Authoritative candidate JSON](eurydica-plan.json)
- [Validation result](check-result.json) — PLAN_CHECK_PASS, zero errors
- [Checker](check_plan.py), [additional checks](detail_checks.py), [delivery check](check_delivery.py)
- [Render provenance](render-manifest.json), [visual review](visual-review.md), [acceptance gates](GATES.md)

The plan is a candidate, not owner approval. Claude must wait for owner approval before rebuilding the town. The fixed river, north terrain, clock tower and Alliance staging remain; the shorter southern layout is visible at equal scale. Read the build plan’s walk-time note: the shorter bank yields {M['gate_market_walk_s_at_3_2']:.3f} seconds from gate to market at the unchanged 3.2 m/s speed.

`RESUME.md` records the final handoff state. Authoring scripts and the inherited checker are retained so this package can be reproduced.
'''
(R/'README.md').write_text(readme,encoding='utf-8')
if '--report' in sys.argv:
 assert len(M.get('negative_controls',[]))>=22
 report=[
 'COMPLETE — Eurydica v7 clustered-city candidate; owner approval pending; no Godot installation.',
 f"Layout: {M['buildings']} buildings ({M['buildings_before']} retained + {len(M['added_buildings'])} homes), {M['clusters']} clusters, {M['districts']} districts; gate-to-river {M['gate_river_m']:.1f} m.",
 f"Checks: PLAN_CHECK_PASS; zero errors; {len(M['negative_controls'])} control cases; {M['markers']} markers, {M['npc_spots']} NPC spots and {M['props']} props retained.",
 f"Green: {M['green_area_m2']:.2f} m2 in {M['named_green_spaces']} named spaces ({M['north_green_area_m2']:.2f} m2 north bank); ordinary-building median cluster gap {M['median_cluster_wall_gap_m']:.1f} m.",
 'Review: cluster-map.png, same-scale-comparison.png, bird-view-sketch.png, Eurydica Build Plan.md and README.md in D:/Codex/IMC/runs/eurydica-plan-v7/.',
 f"Plan SHA-256: {M['plan_sha256']}; gate-to-market {M['gate_market_walk_m']:.3f} m / {M['gate_market_walk_s_at_3_2']:.3f} s at retained 3.2 m/s (historical v5 timing target superseded)."]
 (R.parent.parent/'handoff/eurydica-plan-v7-last.txt').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('DELIVERY_DOCS_WRITTEN')
