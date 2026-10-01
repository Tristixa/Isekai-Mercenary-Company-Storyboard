# Eurydica Outskirts — persistent location brief

Stable proposed location ID: `eurydica_outskirts`. Artwork revision: `candidate-v1`, 2026-09-28. Status: **two concepts for review; neither approved**. This ID is a proposal, not a verified runtime binding.

## Purpose and classification

Chapter 1, Scene 1: the Commander wakes beside a tree at night. Tristitia watches, leaves into Hylaea to finish her hunt, returns after the one-hour fade, then leads him toward Eurydica's South Gate. Preserve the Commander's lying, sitting, kneeling, standing and seated gestures with his bag equipped. The hunt remains offstage; no bandits, camp or combat set is added.

**Playable exterior:** a small fixed-staging area with a short traversable connection to the road. The metric plot is 30 m east–west by 40 m north–south, 1,200 m². Conversation staging is fixed; authored push-ins and two-shots move the camera, and exploration may follow the short road approach. Thus this is not a literal motionless single-screen background or a large city map. The manuscript locks control during the opening; traversable geometry does not introduce a new free-exploration beat before its walk cues.

Eurydica is narratively ten minutes away. The local plot ends before the city. `road_gate` is the departure/fade marker, not the physical gate. The South Gate/main_street arrival and pan are a separate location, outside these deliverables. No exact world distance is inferred from the dialogue or accelerated game clock.

## Sources and precedence

- Full manuscript read: `D:/Storyboards/Isekai Mercenary Company/Manuscript/Chapter 1 - New Beginning/Scene 1 - Opening.md`.
- Current GDD: `D:/Storyboards/Isekai Mercenary Company/Game Design/IMC GDD.md`, especially approved proof camera, §2.4 painted environments, §2.6 dialogue staging, and Hylaea's South Gate connection.
- Requested skill: `D:/Godot Projects/IMC-Companion-Skill-Environment/SKILL.md`, with project-contract, rendering-contract, playable-camera and game-appearance references.
- Approved Hylaea: `Environment Assets/Hylaea/Approved Calibration v1/`, **clean sheets and full-resolution objects only**. Never pixel8 or logical assets.
- Approved city (at the time): the 3D-era Arrival Ward concept `eurydica-arrival-ward-approved.png`, since removed from the project (2026-10-01; in git history only). This one concept includes both Arrival Ward and South Gate. Match the modest green-roof arch and pale wall, not the diagonal district camera.
- Approved architectural paint: `Environment Assets/Eurydica/Approved Facades v1/gatehouse/s.png` and the set's README; roof/wall identities remain compatible with that set.

The explicit handoff and newer GDD painted/camera decisions override the skill's older generic orthographic default. The retained game-appearance pair is attached for simple shapes and readability, not to replace clean Hylaea paint. Source copies and SHA-256 records are in `references/provenance.json`; exact attached roles and prompts are in `prompts.md`.

## Camera, coverage and scale

Perspective, heading straight north, no horizontal rotation; Godot offset `(0,18.4,21.8)` m from the target, vertical FOV 30°, depression approximately 40.17°, viewport 1280×800 (16:10). World coordinates in the plan are `(east,north)` and map to Godot `(east,height,-north)`. Ground height is 0 m in this proposed flat staging area.

Typical actor height is 1.68 m. At target distance 28.53 m, a screen-facing billboard is approximately 87.9 px high, rising to approximately 91–92 px at the proposed markers in the guide; the handoff/GDD's 93 px is an approximate target. An upright geometric person projects differently from a camera-facing sprite. Preserve native sprite density rather than resizing the camera to force an exact 93 px measurement.

`references/gameplay-camera-guide.png` is computed from these parameters and the JSON; its outlined rectangles are scale rulers only, not Commander or Tristitia designs. Clean concepts contain no characters. Concept art follows the gameplay projection visually; it does not certify pixel-exact registration to the JSON or Godot.

The entire 30×40 m plot does not fit this camera at gameplay distance. The concept is a local crop of the tree/road area; it must not be scaled down into a whole-map overview. The full site is documented by the plan PNG.

Shot plan:

| Shot | Target and staging |
|---|---|
| Exploration/shared overview | Guide target `(-1,14)`; tree on left, north road on right, woods access on west. |
| Shared dialogue / two-shot | Frame midpoint `(-2.85,12.4)`; markers 3.13 m apart. Follow GDD §2.6 by easing closer/lower toward 28–30° while keeping north heading. Both standing silhouettes must stay clear. |
| Push-in Commander | Target `tree_rest`; use clear south/east side of trunk. Preserve lie/sit silhouette, emote clearance and bag; do not put a foreground bough across him. |
| Tristitia exit/return | Travel west through `woods_edge`; reverse route to `tris_watch`. The script's post-fade enter resolves at `tris_watch`, so no extra visible return beat is required. |
| Departure | Short east/northeast link to `road_gate`, then north/up-screen. Stagger arrivals rather than stack both actors on the exact marker. Fade to South Gate arrival scene. |

Keep lower dialogue-panel and portrait space visually quiet. Actual HUD margins require the current runtime overlay: the old screenshot is only a readability reference. No UI is baked into clean art. Dialogue-camera interpolation, close framing and canopy cutaway remain runtime validation tasks.

**Distant skyline caveat:** a 40° downward camera with a 30° vertical FOV cannot see a flat-world horizon. The wall/gate is therefore proposed as an independent art-directed scenic matte above/beyond the traversable plane, not metric gate geometry at the north border. The plan draws it beyond an explicit break. Do not tilt the gameplay camera up to include a sky. A night-sky/wall strip may extend above the crop for later authored shots; exact card height, parallax and masking await engine validation. Neither concept establishes the physical distance to Eurydica.

Provider outputs are retained at native size (see `qa-report.json`; requested 1280×800 framing, delivered 1586×992 clean candidates). These are review images, not final production masters. Future modular production should use the handoff's 16:10 viewport, at least a 1920×1200 local-view master if a raster master is needed, and enough independent ground/card coverage for the full plot and closest shot. Do not stretch a default 1920×1080 master or enlarge one full-site still for camera travel. Architectural facades retain the approved 64 px/m contract; organic cutout density and anchors must be measured per object.

## Night, palette and materials

Night under broad cool moonlight. The Guild's lighting is implemented by the engine: no baked light pools, emissive windows, lantern halos, bloom, shafts or dynamic cast shadows in production assets. The concepts preview broad night colour and form shading only. No water, fire or new light fixture is required.

| Role | A: silver-sage shelter | B: indigo-olive verge |
|---|---|---|
| Dominant | Deep forest `#253D42` | Ink indigo `#202E43` |
| Secondary | Sage foliage `#6B7D64` | Muted olive `#687051` |
| Ground | Quiet cool earth `#62675D` | Warm-grey earth `#666054` |
| Accent | Silver slate `#9EA9A3` | Weathered bark `#84745F` |
| Distant city | Violet slate `#424E69` | Blue-grey `#38465B` |

These are direction swatches, not a quantization palette. Preserve clean painted moss, grouped foliage and subdued bark planes. Use broad road wear and a few stone fragments to express regular travel; ancient roots and moss express forest age. No invented Guild outpost or new settlement ownership. Eurydica's restrained curved roof is the distant fantasy identity anchor.

## Reuse inventory

All relative paths in this table are beneath `D:/Storyboards/Isekai Mercenary Company/Environment Assets/Hylaea/Approved Calibration v1/`.

| Asset | Proposed use / scale |
|---|---|
| `objects/tree-broad.png` from `clean/Tree Variants.png` | Waking tree at `(-5,15)`, proposed 6.8 m high, 1.3 m trunk/root collision radius; 3.4 m canopy envelope. The approved silhouette is suitable; no new hero tree is required by default. |
| `objects/tree-tall.png` | West/south edge, 7.5 m. |
| `objects/tree-leaning.png` | West/north edge, 6.5 m. |
| `objects/tree-young.png` | Sparse east boundary, 4 m. |
| `objects/mid-broad.png` and `clean/Mid Trees.png` | Western forest depth; individual mid-broad at 6 m. Depth strips remain outside walking lanes. |
| `clean/Ground Tile.png` | Quiet forest soil, starting repeat size 6.3 m from the GDD. Review tiling at actual camera; do not reuse pixel8 seam evidence as proof for the clean texture. |
| `objects/rock-medium.png` | One low outer-edge rock, approximately 0.8 m high. |
| `objects/fern-wide.png` | Western boundary fern, approximately 0.7 m high. |
| `objects/bush-low.png`, `objects/grass-short.png` | Optional sparse perimeter dressing only; no new collider or obstruction across routes. |
| `clean/Far Background.png` | Forest-only palette/depth reuse if needed; the daytime panorama is not a finished night city strip. |

All scales/anchors are proposed, not a claim that the old scene's bindings fit this new camera. `objects/` are already extracted full-resolution cutouts; `clean/` keeps source sheets. Bottom-centre planting must be checked against visible roots. Do not redraw approved source objects merely to make a candidate. Generated concepts interpret the references; they are not literal composites of those cutouts.

## New assets and separation

1. **Night distant-city/wall backdrop strip:** modest green-roof gate aligned with north road, restrained pale wall, low-contrast distance; optional sky extension kept separate and outside this gameplay crop. Prepare independently from ground and forest, not a new giant gate model. Reuse approved facade shapes/colours.
2. **Road-edge ground transition tile/mask:** broad compacted earth fading into Hylaea soil, tileable north–south; no lamps, roots, shrubs or light patches baked in. Keep the resting pad level and quiet.
3. **Conditional waking-tree root/canopy separation:** if existing cutout cannot preserve the lie/sit silhouette during close shots, split its canopy/occluder and adjust its root collision without replacing its identity. Only commission a new larger tree if the owner later finds existing scale unsuitable.

Future production should preserve a ground-only base, separate transparent trees/props, separate city and forest cards, and independently editable/contact shadows. These deliverables are intentionally assembled composition candidates; no modular production export or game integration is implied.

## Open space, markers and route

The metric plan reserves three edge planting pockets totalling 216 m² plus the waking-tree collider. That leaves about 81.6% clear footprint under the simplified collider model. This is a plan-space estimate, not a pixel count: tall canopies occupy more of the camera image. The denser GDD Hylaea field/battle framing does not authorize blocking this scene's speakers or escape/departure paths. Keep near trunks out of the central foreground sightline during story shots.

| Marker | East, north (m) | Function |
|---|---|---|
| `tree_rest` | `(-4.4,12.2)` | Clear south root pad; Commander begins lying facing south and later sits/rises. Pad is 3.5×2.5 m. |
| `tris_watch` | `(-1.3,12.6)` | Tristitia faces Commander; both fit shared/two-shot. |
| `woods_edge` | `(-12,17)` | West-side offstage exit and return access. |
| `road_gate` | `(5,22)` | Departure walk/fade, connected to road continuing north to `(5,40)`. |

Woods lane: 2.4 m wide, goes north of the waking trunk via `(-1,18)` and `(-9,18)`. Road link: 3 m wide, southeast/east of tree; north road: 5 m wide. The JSON records control points, object footprints and frame metadata; `build_layout.py` renders the plan directly from it. Navigation checks examine these proposed ground collisions; foliage/alpha occlusion still needs visual engine checks. Pose approach for the optional kneel/hand-kiss branch can use the open gap between the markers, then return to tree_rest.

## Candidate review and unresolved owner choices

**A** gives a brighter sage resting area, broad tree silhouette, more visible masonry and lush peripheral framing. **B** gives a taller/cropped canopy, warmer bark, a quieter earth connection and a less prominent gate. Both preserve the same tree-left / woods-west / road-north topology. Generated edge dressing and silhouette scale differ; neither is a surveyed pixel-exact placement plate. Use the JSON, not painted root locations, when building the scene.

Clean and labelled companions were visually inspected. Trees, west passage, north road and gate are legible; no characters or baked lamp pools are present. The distant gate is still visually compressed for concept readability, so approve its scenic-layer approach separately from any claim about distance. Full gameplay sprite contrast, prone pose contact, canopy cutaway, dialogue UI overlap and close-shot native density have not been tested in Godot.

Owner choice: A versus B (or A palette with B's quieter road); accept the scenic city matte treatment; decide whether the existing tree needs a root/canopy split after pose review. These choices do not block delivery of the requested candidates. No approved folder, live scene, collision map or game code was edited.
