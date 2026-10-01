# Eurydica Build Plan v7c (current)

> **Status:** the owner approved v7c on 2026-10-01. `eurydica-plan.json` here is v7c (SHA-256 `8e11a664…`), installed from the Codex run `D:/Codex/IMC/runs/eurydica-plan-v7/`. The sections below are the run record (v7, then the v7b and v7c passes), so the word "candidate" in them is historical. The Godot town is not rebuilt from v7c yet. Review images are in `review/`; checkers and the check result are in `checks/`.

## The original v7 package

Owner review package, 1 October 2026. JSON is authoritative. This candidate is not owner-approved and has not been installed in Godot. All original v5 building dimensions, identities, uses and roof kits are retained. This is a new clustered layout; it does not reuse the rejected v6 approach.

## v7 changes

The south bank is organized as a gate group, Guild compound, lodging frontage, arrival courts, red-tree court, market shop row and household blocks. Retained surplus homes form five supplemental groups, rather than remaining isolated. North-bank buildings form five groups around the fixed civic landmark and terraces; shared orchards and groves fill the interstitial ground.

Buildings retain their individual v5 dimensions. Layout yaw is reset to zero to make continuous street fronts and shared-wall seams. The nearest non-landmark neighbour within each group is at most 2 m away. Separate groups have at least 8 m wall clearance, except where an explicit road separates them. The new named green spaces replace v5’s blanket base lawns and per-house garden/hedge layout.

The task’s explicit clustered-city rule supersedes the environment skill’s general open-space ratio. No footprint scaling, facade invention, game rebuilding or painted image generation was used.

### Cluster schedule

The following table includes every building, using stable v5 IDs. Numbers match both review maps.

| No. | Cluster ID / name | District / phase | Buildings | Form and purpose |
|---|---|---|---|---|
| 1 | `gate_cluster` — Gate cluster | Guild Edge / 1 | `south_gate`, `guard_shelter`, `street_home_1`, `infill_home_11` | Guarded entry; houses hug both sides of the inner wall |
| 2 | `guild_compound` — Guild compound | Guild Edge / 1 | `company_house`, `store_shed`, `stables` | Guild yard, processing corner and stables; expansion parcels immediately west |
| 3 | `lodging_row` — Lodging row | Arrival Ward / 1 | `lodging`, `street_home_0`, `street_home_2`, `infill_home_22` | Continuous east frontage for arriving travellers |
| 4 | `arrival_court` — Arrival court | Arrival Ward / 1 | `arrival_home_1`, `arrival_home_2`, `infill_home_03`, `arrival_home_3`, `infill_home_18`, `street_home_3` | Six homes enclose a small shared court off a short lane |
| 5 | `red_tree_court` — Red-tree court | Market Spine / 1 | `tavern`, `infill_home_12`, `street_home_8`, `provisions` | Tavern and three food shops ring an open-earth red tree plaza on three sides |
| 6 | `market_row` — Market row | Market Spine / 1 | `repair_supply`, `infill_home_06`, `infill_home_23`, `market_home_violet` | Continuous main-road shopfront opposite the tree court |
| 7 | `market_homes` — Market homes | Market Spine / 1 | `market_home_0`, `market_home_1`, `market_home_east`, `infill_home_04`, `infill_home_05`, `infill_home_08` | Six homes around a compact rear court |
| 8 | `service_lane` — Service lane | Service Lanes / 1 | `food_shop`, `clinic`, `service_home_0`, `service_home_3` | Clinic and food shop face two warm-roof homes across one paved lane |
| 9 | `service_homes` — Service homes | Service Lanes / 1 | `service_home_1`, `service_home_2`, `infill_home_01`, `infill_home_02`, `infill_home_07` | Five warm-roof households beside the shared allotments |
| 10 | `arrival_west_court` — West arrival court | Arrival Ward / 1 | `company_neighbor`, `infill_home_09`, `infill_home_10`, `street_home_4`, `infill_home_15`, `street_home_5` | Retained Arrival Ward homes around an earth court |
| 11 | `guild_neighbours` — Guild neighbours | Guild Edge / 1 | `street_home_6`, `street_home_7`, `infill_home_16`, `infill_home_29`, `infill_home_30` | Five retained homes on an inner-wall lane |
| 12 | `arrival_garden_court` — Orchard court | Arrival Ward / 1 | `infill_home_20`, `infill_home_21`, `infill_home_25`, `infill_home_26` | Remaining Arrival Ward homes face a small court beside the orchard |
| 13 | `service_garden_row` — Garden service row | Service Lanes / 1 | `infill_home_13`, `infill_home_24`, `service_added_home` | Two retained homes and one approved-facade addition beside public gardens |
| 14 | `market_riverside` — Bridge-side homes | Market Spine / 1 | `infill_home_28`, `infill_home_27`, `bridge_home_01`, `bridge_home_02` | Four homes mark the approach to the Old Bridge |
| 15 | `workshop_yard` — Workshop yard | Workshop Quarter / 2 | `tool_repair`, `timber_containers`, `material_sorting` | Three workshops touch the edges of a working court |
| 16 | `quay_row` — Quay row | Quays & Storeyards / 2 | `bulk_storehouse`, `quay_storehouse`, `loading_shelter` | Storehouses and loading shelter form a river-edge frontage |
| 17 | `civic_plaza` — Civic plaza | Civic Terrace / 2 | `watch_tower`, `toll_records`, `civic_guard`, `notice_shelter` | Clock landmark, toll, guard and notice shelter around the unchanged appointment plaza |
| 18 | `old_city_row` — Old City row | Old City Streets / 2 | `old_home_0`, `old_home_1`, `old_home_2`, `old_hall` | Inn and old timber homes share a continuous south-facing street |
| 19 | `residential_a` — Residential A | Residential Quarter / 2 | `res_home_0`, `res_home_3`, `infill_home_19` | Western courtyard households |
| 20 | `residential_b` — Residential B | Residential Quarter / 2 | `res_home_1`, `res_home_2`, `infill_home_14`, `infill_home_17` | Eastern courtyard households |
| 21 | `waterworks_group` — Waterworks group | Waterworks & Gardens / 2 | `cistern`, `waterkeeper`, `washing` | Keeper, washing shelter and cistern beside the fixed feeder |

The four existing market facade bindings retain their stable IDs: `infill_home_12` = market_provisions, `street_home_8` = market_bakery, `infill_home_06` = market_small_shop_east, and `infill_home_23` = market_small_shop_south. The red-tree group puts the tavern to the west, provisions to the south, and bakery/provisions shop to the north. Its nine awning stalls and accessories occupy the court; the tree itself stands in a 25 m² open grass-and-earth bed, above paving in surface priority.

### Measured before and after

Both nearest-neighbour medians below use the same rule: all buildings except South Gate and clock tower, with each building compared to every other building. This differs slightly from v5’s historical exempt-building population. Distances use wall polygons, including v5 rotations, not centres.

| Metric | v5 | v7 |
|---|---:|---:|
| Buildings | 83 | 86 |
| Building footprint area, m² | 6375.01 | 6519.01 |
| Total plan extent, m² (includes river/cliff) | 91346 | 65217 |
| Median nearest wall gap, m | 2.3557 | 1.0000 |
| Ordinary buildings with a neighbour within 2 m | 10/81 | 84/84 |
| Explicit v7 clusters | Not the v7 schedule | 21 (3–6 buildings each) |
| Gate inner face to river edge, m | 308.8 | 130.8 |
| Gate-to-market walk, m | 217.808 | 90.446 |
| Same walk at retained 3.2 m/s, seconds | 68.065 | 28.265 |

At a 2 m/s stroll, the new gate-to-market path takes 45.223 seconds. The inherited v5 45–90-second target at 3.2 m/s is **not met** by this shorter bank; it is retained in JSON as historical metadata, explicitly superseded by the owner’s 120–150 m gate-to-river constraint. No runtime movement speed is changed. The same-scale sheet makes this size change visible rather than enlarging v7 to fill the old footprint.

### Added buildings

| Stable ID | Approved facade reuse | Footprint | Roof |
|---|---|---|---|
| `bridge_home_01` | `house_violet` | 8 × 6 m | plum |
| `bridge_home_02` | `house_violet` | 8 × 6 m | plum |
| `service_added_home` | `house_violet` | 8 × 6 m | warm_red |

The service addition uses the approved `house_violet` footprint with the Service Lanes warm-red roof override, as retained service infill already does. All retained facades and roof colours remain unchanged.

### Roads, topology and terrain

One 7 m main road gently bends between South Gate and Old Bridge. Four-to-five-metre branches serve the workshop, quays and service loop; courts use 2–3 m alleys. Individual 2 m door approaches are access strips, not additional arterial roads. The six connection IDs, route-ID sets and purposes are unchanged; their junction order from south to north is **5 → 4 → 1 → 6 → 3 → 2**.

| Connection | New junction (x, z), m | Retained route IDs |
|---|---|---|
| 1 | (0.000, 75) | `join1` |
| 2 | (1.000, 15) | `join2_earth`, `join2_apron` |
| 3 | (-1.000, 60) | `join3` |
| 4 | (-0.400, 104) | `service_public_loop`, `join4` |
| 5 | (0.000, 108) | `join5` |
| 6 | (-0.467, 68) | `join6`, `join6_apron` |

The river, Old Bridge, north terraces, retaining walls, ramps, stairs, rear cliff, waterworks feeder and covered crossing retain v5 geometry. The tower remains centred at (0, −70), ground y=2 m. Alliance appointment markers are unchanged, including figure spacing and camera anchor. The clock plaza remains clear of other buildings and props, and the bridge-axis clock sightline is checked against building envelopes and tree canopies.

The Guild platform is relaid at y=0.6 m with the explicit approach ramp. Its unchanged-size 552 m² HQ reservation is immediately west of the compound at x=−77…−54, z=99…123. The three upgrade parcels, construction rules and dormitory restrictions remain. Reservation land is kept clear of buildings, roads, trees and props.

### Narrative, use and activity

All 59 marker IDs, 24 NPC-spot IDs and 103 prop IDs remain. Interior geometry and markers are unchanged. Guild processing, bench, envoy and evening/rest staging translate together by −175 m in z; shop/stable markers follow their relocated doors. All city markers have clear body space, surface heights and connections to the gate’s route graph. The two resting grass patches remain within Guild courtyard staging.

Player access stays false for the existing dormitory/stair and future dorm portals. NPC schedules and chapter availability remain unchanged. All roof kits, stall awnings, stock props and allotment beds retain their dimensions and uses. Workshop and quay props are within their working zones and district bounds. The ten-bed allotment translates rigidly, preserving its 3 m east gate and original tending aisles; a 1.2 m body corridor is flood-filled to every facility.

### Green-space accounting

There are 29 named green spaces totalling **11,937.80 m²**, including **5,588.00 m²** on the north bank. This is the sum of disjoint explicit polygons, including the allotment’s beds and tending aisles and the two small Guild rest patches; it is not a claim that all of that area is lawn. 237 tree records include the red tree. Intercluster regions are clipped around roads, whole cluster envelopes, props, markers and the HQ reserve. Contiguous accepted 2 m authoring cells are merged into rectangles; the exact polygon areas are checked for overlap before summing.

| Named location | Area, m² |
|---|---:|
| Old City communal orchard | 828.00 |
| Old City river grove | 392.00 |
| Old City terrace gardens | 916.00 |
| Civic east garden | 512.00 |
| Civic west garden | 180.00 |
| Civic river gardens | 616.00 |
| Residential shared grove | 812.00 |
| Between the residential courts | 112.00 |
| Waterworks orchard | 812.00 |
| North riverbank gardens | 408.00 |
| Quay and orchard buffer | 144.00 |
| West wall grove | 560.00 |
| Arrival shared garden | 144.00 |
| West arrival garden | 396.00 |
| Arrival and Guild garden | 112.00 |
| Arrival east orchard | 408.00 |
| Between market and arrival | 216.00 |
| Market and service grove | 196.00 |
| Bridge-side garden | 512.00 |
| Service north orchard | 832.00 |
| Service court garden | 116.00 |
| Service south orchard | 200.00 |
| Service east grove | 204.00 |
| Inner-wall east grove | 828.00 |
| Gate inner-wall garden | 192.00 |
| Open red-tree grass-and-earth bed | 25.00 |
| Guild rest_1 resting grass | 2.40 |
| Guild rest_2 resting grass | 2.40 |
| Service household allotments (beds and tending aisles) | 1260.00 |

### Checker migration and evidence

The package retains v5’s `inherited_checks.py` unchanged as the standard-library polygon, rotation, route-graph and shortest-path kernel. `v5-check-plan-source.txt` preserves the prior entry point for provenance. Its absent sibling-version dependencies, historical byte allowlist and fixed 300 m southern coordinates cannot be used as v7 layout rules. `check_plan.py` replaces those obsolete rules explicitly and calls `detail_checks.py`; it does not filter failures out of the old run.

The v7 checks enforce source identity and facade dimensions, roof kits, district order and containment, all scheduled cluster functions, cluster size/membership/gaps, road separation, overlaps, connected doors, exact door faces, slopes and graph elevation continuity, marker and rest-body clearance, phase containment, protected northern geometry, unchanged appointments, HQ parcels, dorm restrictions, green area/placement and allotment aisle reachability. Negative controls deliberately damage these features and must be rejected.

Latest validation: **PLAN_CHECK_PASS**, zero errors, 335 route-graph nodes. 22 control cases recorded in `check-result.json`. Report and render manifests bind the delivered plan with SHA-256 `9306873357d4e6998a98169a00651118efde44dfb6024331e6be902b18f74444`.

### Review images and limits

- `cluster-map.png`: north-up tinted groups, numbered cluster/district legend, roads, doors, greens and HQ reserve.
- `same-scale-comparison.png`: v5 and v7 at exactly 4 px/m using the same world bounds. f01 is deliberately omitted because its dimensional scale cannot be established reliably.
- `bird-view-sketch.png`: boxes, roof colours and tree blobs seen northward at 40° down. This uses an orthographic massing projection to show the whole town consistently; it is not a gameplay-perspective capture.

Owner references f01–f04 were opened and studied. f03 guides the district → cluster → building hierarchy; the references guide layout only, not painted style. This package is a reviewable construction plan. Facade face/door adaptation, shared-wall eave suppression, final roof meshes, perspective occlusion/cutaways, physics and playable feel still require the later approved Godot blockout. Those are not claimed as tested here.

## Reproduce

Run in this directory with Python 3.10+ and Pillow:

```text
python -B build_v7.py
python -B check_plan.py --self-test
python -B render_review.py
python -B write_delivery.py
python -B check_delivery.py --preflight
```

After final visual review, `write_delivery.py --report` replaces the six-line handoff report. `run_gates.mjs` executes the two reviewed check commands and records their real output fingerprints locally; it uses no global approval store, respecting the task’s write boundary.


## v7b refinements

**Candidate for owner review, 2026-10-01. No Godot or storyboard changes.**
The v7 cluster list, order and membership are retained: 86 buildings in 21 groups, all ten districts, all six approved connection IDs, 59 markers, 24 NPC spots and 103 props. Each group's centroid remains within 5 m of v7. No buildings were added or removed for this pass; facade dimensions, uses, roofs, interior/dormitory restrictions and upgrade parcels are retained. The gate-to-river distance stays **130.8 m**.

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
| Total centreline length | 2,485.672 m | 2,057.752 m |
| Total road union area | 8,193.38 m² | 6,482.19 m² |
| Sum of length × width, before overlap removal | 8,911.33 m² | 6,938.56 m² |
| Door-approach centreline length | 774.000 m | 472.497 m |

Length falls **17.22%** and road area falls **20.89%**. Union areas use identical 0.1 m raster sampling of swept route strips, so they are estimates rather than analytic polygon-union areas. The totals include protected bridges, ramps, decks, stairs and every door spur. Route record count is not a street count: individual door bindings retain separate IDs. Median door-spur length is 4.620 m; the longest is 21.578 m. The gate-to-market walk is 90.345 m, or 28.233 seconds at the unchanged 3.2 m/s.

### Organic groups

Frontage angles and small local steps follow the winding streets and court approaches. 72 of 84 non-landmark buildings have nonzero yaw; the angle vocabulary is -10, -5, 0, 5, 10, 15 degrees, in 5-degree steps. The median nearest wall gap inside clusters is 0.732 m; every non-landmark has a neighbour within 2 m. Intercluster separation remains at least 8 m unless a road separates the groups.

The gate arch stays aligned with the existing wall; its neighbouring buildings turn slightly. The clock tower, Alliance appointment markers, plaza and north-bank terrain stay fixed while the other civic buildings turn. The Guild's story staging and bench/resting positions remain fixed, with its building frontage turned 5 degrees. These anchors take precedence over rotating an entire landmark group as a rigid block. Rotated footprints and roofs are rendered from the same JSON as the checks.

### Organic green

Rectangular grove plots are replaced with **23 flowing, concave grove polygons**, with rounded bays and lobes. Their average irregularity is **0.3442**, versus **0.0000** in v7. The measure is `1 - polygon area / axis-aligned bounding-box area`; a rectangle scores zero. Concavity is separately tested against each polygon's convex hull, so simply rotating a rectangle cannot satisfy this check.

A continuous, walkable meadow covers **32,951.20 m²** between the groups. The JSON stores this as `green.continuous_cover`: union the domain polygons, then subtract the listed cluster envelopes, routes, structures, designated courts, allotments and reserve. This explicit boolean ground layer fills all intercluster gaps without grass seams between individual buildings. It is a candidate schema extension for a future approved builder; it has not been installed in Godot. The checker reconstructs the exclusions independently and finds **0.00 m²** of unassigned intercluster ground at 0.2 m sampling.

The 293 trees use deterministic varied-spacing placement, with grove groups and individual trees at cluster edges and beside roads. Nearest-neighbour spacing coefficient of variation is 0.3359; a regular lattice would approach zero. Tree trunks, route corridors, markers and the clock view are checked. The red tree remains in its named open grass-and-earth bed; the Guild resting grass and Service allotment layout are retained.

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


## v7c — final four-point refinement

**Candidate for owner review. No Godot or storyboard files changed; owner approval pending.**

Source: `eurydica-plan-v7b.json`, SHA-256 `05b11964b92a3669d1e5ad2489fb63e152a49ba1dc6e7448abfd6df6be6ed133`.
Candidate: `eurydica-plan-v7c.json`, SHA-256 `8e11a66429a94a8e61110bd51e0071d4aba664647e1e64a7ea0080c63eeb87b5`.
Reviewed layout reference: `D:/Storyboards/Isekai Mercenary Company/Research/Eurydica City References/f03 illustrated.jpg`.
The reference guides the soft road bends and grouped foliage; these images remain deterministic geometry reviews drawn from the plan.

### The four changes

1. The 7 m main road makes two soft S-curves with approximately ±7 m lateral displacement. The South Gate endpoint `[0,118]` and Old Bridge endpoint `[0,-5]` stay fixed. Lodging and market frontage clusters shift 2.5 m east as rigid groups; their existing angles, buildings and internal gaps are retained. Doors and their shared approaches are recalculated against the curved road.
2. Five connected branch networks serve Guild/gate/neighbours, arrival/orchard courts, Service Lanes/homes/garden row, workshop/quay yards, and the north bank. The two Guild arms share the same main-road attachment; the workshop branch grows out of the arrival/orchard branch. The duplicated quay-to-main-road link, service-to-arrival return and old park return are removed. The north bank has one principal civic/old-city/residential circuit with waterworks and retained deck access. Short door spurs and narrow court alleys remain explicit geometry, and unused terminal paving is pruned. Maximum door spur: **10.636 m**, median **3.324 m**. Shared alleys are included in all totals.
3. **413 of 424 trees (97.41%)** occupy **25 groves**. Every grove has 8–25 trees and a connected set of overlapping canopies. Open meadow separates the clumps. The red tree, HQ-edge accents and two civic trees remain individually identifiable.
4. The civic paving surface itself and the clock-plaza polygon now share an irregular boundary fitted to the tower and adjacent civic frontages. A small planted island with two trees sits inside the eastern edge. All Alliance appointment markers retain their exact positions and spacing on paving. The south-east enclosure becomes an irregular household yard with broken hedges, stepped produce groups, a tool/stock group and a west-side opening. The source calls this `spine_service_allotments`; existing uses and all object IDs are retained. The five old fence runs are stored as short panel stacks beside the shed, conserving their original total lengths rather than keeping a rectangular fence.

### Road measurements and the requested aim

| Whole network, same measurement method | v7 | v7b | v7c |
|---|---:|---:|---:|
| Centreline length (m) | 2485.672 | 2057.752 | 1900.417 |
| Union paved/route footprint (m²) | 8193.38 | 6482.19 | 6237.66 |
| Sum of strip areas before overlaps (m²) | 8911.33 | 6938.56 | 6682.22 |

Relative to v7: **23.55% less length and 23.87% less area**.
**The 35% reduction aim is not met.** The checked layout retains every door, the fixed bridge/ramps/decks, and the requested north-bank circuit. No road is omitted from measurement to improve the percentage. This is a measured shortfall, not a claim that further reduction is impossible. Union area uses the inherited 0.1 m raster sampling; length includes every route record, including shared court links and door spurs.

### Verification and retained constraints

`PLAN_CHECK_PASS`: 86 buildings, 21 clusters, 59 markers, 24 NPC bindings and 103 props. All v7b cluster membership lists remain identical. All 84 ordinary buildings retain a neighbour within 0–2 m; median wall gap is 0.732 m. Graph reachability covers all doors and city markers. Gate-to-river distance is **130.8 m**. Minimum civic body clearance remains **1.3 m**.

Inherited geometry, collision, elevation, identity, marker/NPC, Guild staging, HQ reservation, roof, terrain, red-tree and yard-access checks remain active. Task-superseded assertions are explicitly replaced: six historic attachments are remapped to current branches; the fixed plaza outline becomes exact appointment/paving checks; rigid allotment translation becomes dimension/material-conservation and accessible-aisle checks; the old local garden-ring IDs become current loop geometry. No errors are filtered from a failed check run. The 35% aim is reported separately from safety/functional pass status.

The current check result records inherited negative controls and v7c controls for flattened roads, missing groves, lost civic planting, a rectangular yard and missing pile groups. `source-manifest-v7c.json` and `Eurydica Build Plan-before-v7c.md` verify preservation of every prior run file and the prior document prefix. The delivery checker binds plan, checker, renderer and reviewed image hashes.

### Review files

- `cluster-map-v7c.png` — numbered north-up cluster map with doors, grove planting and revised yards.
- `bird-view-sketch-v7c.png` — north-facing massing at 40° down, with retained roof palettes.
- `v7b-vs-v7c.png` — equal extents and 5.5 pixels per metre on both sides, with measured road totals.

These are candidate geometry sketches, not a Godot capture or runtime camera/occlusion approval. Nothing is installed until the owner approves.
