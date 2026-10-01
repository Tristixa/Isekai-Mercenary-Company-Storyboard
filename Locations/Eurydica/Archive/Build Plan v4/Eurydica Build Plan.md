# Eurydica Build Plan v4

Candidate — 28 September 2026. The JSON and script-rendered SVG/PNG govern construction. The bird’s-eye views are finish and composition candidates. No project documents, live textures, geometry or runtime audio were changed.

## v4 changes

- **124 → 83 buildings**, retaining all 53 established v3 buildings and replacing its 71 generic additions with **30 compact satellites**. Added infill falls 57.75%; the total falls 33.06%. No district is invented.
- **48 buildings rotate** in 5° steps. Cottages, narrow three-storey townhouses, wider homes and 12 × 9 m shared dwellings replace uniform infill. Existing named facade dimensions remain intact. Two Old City houses share a wall; suppress windows and eaves along that party wall.
- Gently curving polylines replace the straight spine and several local roads. The main spine stays 8 m wide, predominantly north–south and plainly legible from the fixed straight-north camera. Side lanes follow small bends instead of a repeated rectangular street grid. Six approved junction coordinates remain unchanged.
- Five small destinations are explicit polygons: red-tree court beside the tavern, Guild-side gate square, south bridge landing, north bridge landing and clock plaza. The red tree at (−7,93) remains beside the tavern; its trunk does not obstruct the travel strip.
- **41 irregular, owned gardens** replace 719 grid-like microplot surfaces. Houses sit close at their street edges; rear spaces become gardens and shared courts. Broad work yards remain for their original purpose. The v3 lawn-percentage target is removed, not relabelled as a new density criterion. Base earth is common ground, not a direction to paint a continuous barren expanse.
- The existing `watch_tower` moves from **(−102,−85), Old City**, to **(0,−70), centre of Civic Terrace**. It becomes a **28 m clock tower**, with a south clock, open belfry and distinct green cap. There is no second tower at the old site.
- The enclosure is **not shrunk again**: the v3 stepped extent remains 91,346 m², within a 246 × 442 m bounding box. This preserves the six junctions, working courts, terraces and every marker. Reduced building count and closer local spacing are independent of city extent.

## Rotation and geometry contract

North is −z; east is +x; metres throughout. `footprint = [x0,z0,x1,z1]` stores the unrotated rectangle at its world centre. Compute local offsets from that centre, then apply `x′ = cos(yaw)*x − sin(yaw)*z`, `z′ = sin(yaw)*x + cos(yaw)*z`. Positive `yaw_deg` is clockwise on the north-up plan. In Godot use `rotation.y = -deg_to_rad(yaw_deg)`. All values are multiples of five degrees.

Door faces are named in local space; `door_position` is already in world space. Do not rotate it twice. Route paths are world coordinates. The checker inverse-rotates each door to verify its local wall; it checks rotated polygons against buildings, routes, gardens, districts and the extent. The gate retains its two solid piers and walk-through opening rather than becoming one solid footprint.

Polylines are the authoritative walk/collision paths. The diagram connects their actual vertices; do not substitute a spline that cuts corners into buildings. Extra spline smoothing, roof overhang clearance and collision require a later Godot blockout pass. Shared-wall neighbours require a roof seam with no overlapping eaves.

## Spacing evidence

The median nearest-neighbour wall gap is **2.348 m**. Maximum nearest-neighbour gap among non-exempt buildings is **7.128 m**, below 15 m. Distances are exact shortest Euclidean distances between the rotated wall rectangles, not centres or axis-aligned bounding boxes. Touching party walls count as zero.

Every ordinary building participates; only the gatehouse, Old Hall, clock tower and named working-yard structures are exempt from the isolation limit. The allowlist is enforced. The population and each nearest neighbour appear in `spacing-schedule.csv`; complete component medians appear in `check-result.json`. Components are connected at a 15 m wall gap. The reported 1–4 m requirement applies to the overall cluster population. Disclosed exceptions in component medians are the zero-gap terrace pair and the individual gate guard/toll building; they remain under the separate 15 m isolation limit. The checker does not hide party-wall zeros or remove unfavourable ordinary buildings from the median.

## Arrival, districts and six connections

Outskirts → South Gate → Guild Edge → Arrival Ward → Market Spine → Old Bridge. The Guild house stays at (−30,278), **37.202 m** from the gate; stables at (18,285), **23.431 m** away. Limits are 40 m and 30 m respectively. The lodging house remains east of the spine in Arrival Ward at (14,148). The reused Guild house keeps its modest plum-roof house identity.

| Connection | Locked spine junction | Retained route IDs |
|---|---|---|
| 1 | (0,155) | join1 |
| 2 | (0,25) | join2_earth, join2_apron |
| 3 | (0,70) | join3 |
| 4 | (0,205) | service_public_loop, join4 |
| 5 | (0,285) | join5 |
| 6 | (0,105) | join6, join6_apron |

All ten district IDs, all six connection records and all junction positions are retained. Service Lanes remain paved; the public loop avoids the private household court. Local roads retain 4–5 m widths, work loop 6 m, door approaches at least 3 m, main spine and bridge 8 m; gate arch 4.6 m. Curved streets retain grade metadata and connected door routes.

## Clock tower, plaza and sightlines

Stable building ID `watch_tower`; new facade ID `civic_clock_tower`. Rectangle 6 × 6 m, yaw 0°, centre (0,−70), ground y=2 m. Shaft including open belfry: 23 m; swept pyramidal green cap and finial: 5 m; total **28 m above ground**, crown world y=30 m. The belfry opens between 19 and 23 m above its foundation. South clock diameter 2.6 m, centre 18 m above ground (world y=20 m), on face z=−67. The south door enters from (0,−60).

The clock plaza wraps the tower inside Civic Terrace; toll and guard premises flank it. The notice shelter moves beside the civic guard to (21,−64.5), with its threshold at y=3.05 matching the existing east ramp and a small raised foundation. No existing terrace, retaining wall or ramp is removed. The Old City watch stairs and viewing deck retain their story markers; the vacated bell-tower site is open old-city ground.

The checked sightline runs from south-bank (0,10), eye y=1.68, along the Old Bridge axis to the south clock at (0,−67), world y=20. It clears all intervening building roof envelopes. The tower is the tallest building and dominates the north bank. Foreground cutaway remains necessary for the gameplay camera in normal streets; this plan does not implement it. Bell ringing at 09:00, 12:00, 15:00 and 18:00 is future runtime audio and is deliberately outside this task.

## Gate-to-market walk

The route graph shortest path from **(0,300)** to **(0,84)** measures **217.808 m**, or **68.065 s at 3.2 m/s**, inside 45–90 s. The new bends add 1.808 m to v3’s straight 216 m route. Exact endpoints are injected into the graph, arbitrary segment intersections are supported, and edge lengths include height. This is uninterrupted movement without dialogue or stops.

## Terrain and earlier locks

South ground y=0; Guild plinth y=0.6. River z=−40…−10, water y=−3, bed y=−5. Old Bridge remains the single river crossing, 8 × 40 m, rising 2 m at 5%. Civic ground y=2; retained 40 m ramps lead to y=4 Old City and residential terraces. Watch/view platform remains y=5.2, with eight 0.15 m risers. Dock drops 0.6 m over 12 m. Rear cliff rises y=4→16 and remains treeless. The covered feeder crossing is not another river bridge.

Phase 1 is unchanged: South Gate, Guild Edge, Arrival Ward, southern Market Spine and Service Lanes access. New houses and their door routes inherit phase from this polygon. All **36 markers**, NPC spots, portal positions, interior geometry and narrative metadata match v3 exactly. Marker access is checked against walkable ground and the reachable route graph.

Guild interior retains Commander room, the starting shared officers’ room for **Tristitia, Mae and Elsie**, the stair/hall strip and two-bed attic dormitory. `guild_interior/officers_room_door` remains present. The clear expansion reservation still contains Dorm Annex, Larger Dorm and Officers’ Quarters II, with costs, prerequisites and timing unchanged. No building or route enters those parcels. Elsie’s courtyard staging is retained without training targets.

## Approved finish and roof rules

Walls follow `Approved Finish v2/walls-A`: storybook warm plaster, broad timber and dressed stone, softened edges, selective shutters, window boxes, pictogram signs, ivy and restrained wear. Roofs follow `roof-B/green.png`: detailed visible shingle courses and ridge caps. No pixel grid, quantization or pixel-unfake.

| Roof | Binding |
|---|---|
| Green | Public/business, gate, lodging, tavern, civic premises, Old Hall, clock tower, cistern |
| Plum | Southern homes and reused Guild house |
| Brown | Workshops, quays, stables, work sheds, waterkeeper, washing shelter |
| Warm red | Service Lanes district override; Old City and northern residential homes |

The approved wall/roof finish anchors and location concepts were attached to built-in image generation with separate roles. Prompt files and copied references are in `review/`. The first illustration’s unintended east river inlet and high gate-side house were corrected to exterior woodland and a low brown stable. No characters are included.

The illustration is an assembled review image and may show river water and daylight shading. Production must keep water, lights, fixture emissions and character shadows engine-owned. The candidate is **not** a production base, facade sheet, exact building census, or a Godot capture. It simplifies very small doors and roof seams; build from JSON, not pixels. The image-generated comparison is a presentation board rather than a pixel-difference test. Native review image dimensions are recorded in `review/image-provenance.json`; no upscaled production-master claim is made.

## Reproduction and validation

Use Python 3.10+ with Pillow; installed interpreter: `C:/Users/Tristixa-/.codex/skills/sprite-gen/.venv/Scripts/python.exe`. From this folder run `build_plan.py`, `check_plan.py --self-test`, `render_plan.py`, `write_docs.py`, then `check_delivery.py`, each with `-B` to avoid bytecode writes. Capture checker stdout to `check-output.txt` before writing docs. The builder reads v3 only; artwork is retained and is not regenerated by these scripts.

`inherited_checks.py` is the copied v2 checker carried by v3, adapted locally for rotated solids/doors, arbitrary street intersections and old-home roof binding. `check_plan.py` replaces the obsolete walk window and lawn target, while retaining the prior geometric, source-facade, marker, grade, district, gate, lodging, roof, HQ and phase checks. It adds yaw, count reduction, exact spacing, preserved-lock equality, squares, garden geometry and tower/sightline checks. **22 negative/positive controls pass.** Geometry checks do not certify image fidelity or gameplay camera occlusion.

### Actual checker output

```text
{
  "company_house_gate_distance_m": 37.202,
  "stables_gate_distance_m": 23.431,
  "buildings": 83,
  "districts": 10,
  "routes": 126,
  "markers": 36,
  "graph_nodes": 320,
  "walk_distance_m": 217.808,
  "walk_time_s": 68.065,
  "new_facade_ids": 17,
  "buildings_before": 124,
  "generic_infill_before": 71,
  "generic_infill_after": 30,
  "median_gap_m": 2.348,
  "non_exempt_max_gap_m": 7.127763,
  "rotated_buildings": 48,
  "extent_m2": 91346.0,
  "tower_height_m": 28,
  "tower_position_xz": [
    0,
    -70
  ],
  "tower_ground_y_m": 2,
  "clock_sightline_clear": true,
  "negative_controls": [
    "building collision",
    "route obstruction",
    "narrow route",
    "water marker",
    "door disconnect",
    "missing join",
    "isolated north bank",
    "wrong lodging bank",
    "duplicate gate",
    "grade mismatch",
    "Guild too far from gate",
    "stables too far from gate",
    "missing shared room",
    "wrong roof",
    "yaw must use five-degree increments",
    "clock moved off civic centre",
    "missing square",
    "no spacing exemptions for ordinary homes",
    "missing story marker",
    "isolated ordinary home",
    "rotated-only collision detected",
    "wall-gap positive controls 3m and party-wall zero"
  ],
  "plan_sha256": "db5a41c61b8850f783d0a7321444321f4ee5fa0ede3d5236a83fbb188e334444",
  "errors": []
}
CLUSTERS: [{"id": "cluster_01", "buildings": 8, "median_gap_m": 2.325}, {"id": "cluster_02", "buildings": 10, "median_gap_m": 2.356}, {"id": "cluster_03", "buildings": 2, "median_gap_m": 3.202}, {"id": "cluster_04", "buildings": 5, "median_gap_m": 2.04}, {"id": "cluster_05", "buildings": 4, "median_gap_m": 2.575}, {"id": "cluster_06", "buildings": 1, "median_gap_m": 7.128}, {"id": "cluster_07", "buildings": 2, "median_gap_m": 2.356}, {"id": "cluster_08", "buildings": 2, "median_gap_m": 2.186}, {"id": "cluster_09", "buildings": 8, "median_gap_m": 2.424}, {"id": "cluster_10", "buildings": 4, "median_gap_m": 1.938}, {"id": "cluster_11", "buildings": 2, "median_gap_m": 2.5}, {"id": "cluster_12", "buildings": 2, "median_gap_m": 2.333}, {"id": "cluster_13", "buildings": 4, "median_gap_m": 2.337}, {"id": "cluster_14", "buildings": 3, "median_gap_m": 1.862}, {"id": "cluster_15", "buildings": 8, "median_gap_m": 2.352}, {"id": "cluster_16", "buildings": 3, "median_gap_m": 0.0}, {"id": "cluster_17", "buildings": 1, "median_gap_m": 5.0}]
PLAN_CHECK_PASS
```
