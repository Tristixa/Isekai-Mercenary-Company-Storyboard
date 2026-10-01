# Outskirts generation prompts and reference roles

Status: concepts only; no owner approval. Generated 2026-09-28 using the built-in image_gen tool. No API fallback, quantization, pixel-unfake, character generation or runtime edits. A and B were generated independently from the same five references, not from one another. The tool accepts at most five attachments, so two source pairs were placed on reference boards; originals are retained unchanged with hashes in references/provenance.json.

## Exact attachment order for A and B

1. `D:/Codex/IMC/runs/outskirts/references/mosswood-style-board.png`
2. `D:/Codex/IMC/runs/outskirts/references/arrival-ward.png`
3. `D:/Codex/IMC/runs/outskirts/references/gatehouse-south.png`
4. `D:/Codex/IMC/runs/outskirts/references/game-readability-board.png`
5. `D:/Codex/IMC/runs/outskirts/references/gameplay-camera-guide.png`

The exact roles are in each prompt below. The camera guide is computed from the metric JSON; the layout PNG is a north-up plan and is not used as a camera reference. Clean Hylaea paint supersedes the older simplified-game finish where they differ; the older pair only constrains complexity/readability. Arrival Ward includes the approved South Gate; there is no separate south-gate concept file in that flat folder.

## Candidate A: exact prompt

```text
Create one clean, unlabelled environment concept candidate A: EURYDICA OUTSKIRTS, Chapter 1 opening, NIGHT. Landscape 16:10, target 1280x800. Empty environment: no people, no characters, no UI, no lettering, no diagrams. This is an assembled art review candidate, not modular production artwork.
ATTACHED REFERENCE ROLES, in supplied order:
1 mosswood-style-board.png: left clean Tree Variants PRIMARY painted tree shapes and broad waking tree; right clean Props painted rocks and ferns. Full-resolution painted finish, never pixel8. Ignore board labels.
2 arrival-ward.png: distant wall and low green curved-roof South Gate design ONLY; ignore diagonal camera, daytime, labels and district layout.
3 gatehouse-south.png: approved pale large-block arch construction ONLY, not camera.
4 game-readability-board.png: left approved IMC broad simplified forms, right actual runtime world readability. Ignore people, portraits, UI, labels, lighting, city layout and rivers. Hylaea painted finish takes priority.
5 gameplay-camera-guide.png: PRIMARY PROJECTION, layout and scale lock. Replace schematic proxies with finished scenery, ignore grid, labels and outlined scale rulers. Straight north with zero diagonal rotation; perspective offset (0,18.4,21.8)m, 40 degrees down, vertical FOV30. Adult scale 93px at 1280x800, but OMIT figures.
LAYOUT LOCK: Same 30m east-west by 40m north-south site as guide, cropped at gameplay distance (do not zoom out to fit the whole plot). Waking tree ground anchor (-5,15), south root resting pad (-4.4,12.2), watching spot (-1.3,12.6). Broad waking tree left of centre, approximately 6.8m tall, natural roots frame a flat empty patch clearly visible on its south/right side. No root crossing the resting pad. Woods at WEST/left with a clear side lane towards (-12,17), leaving a visible break between trees. A broad 5m worn earthen road lies to the RIGHT of the tree, centered east=5, running STRAIGHT NORTH/up the screen. A quiet 3m ground link joins clearing to road. Open traversable centre, about 80% usable ground in metric footprint; foliage clusters at edges, no shrubs closing these routes.
Distant Eurydica wall and tiny recognizable low green-roof gate at the upper end of the road, behind the clearing: low contrast independent scenic matte in a thin uppermost band, conveys a ten-minute onward journey, never a giant castle immediately behind tree. At the locked down-facing camera there is no real sky horizon; do not tilt up or invent a broad cinematic sky. Gate is symbolic distant layer, separated by compressed quiet distance. No nearby city houses, no bridge, no water.
TAKE A: sheltered silver-sage clearing. Deep forest green and ink-blue shadows, muted sage foliage with broad cool moonlit plane changes, slate-violet distance, readable muted earth road. Natural shelter comes from the existing broad waking-tree silhouette; sparse moss and one fern cluster. Gentle quiet mood, crisp readable painted assets matched to Hylaea. No glossy 3D, pixel grids, individual leaf micro-detail, dramatic volumetric fog, blur, visible light beams, glowing windows, lantern glow, baked light pools, spotlit ground, lens effects or character shadows. Guild/engine owns all local lighting; only broad ambient night mood. Keep upper tree foliage from swallowing the woods passage or road. No annotations in this clean version.
```

## Candidate B: exact prompt

```text
Create one clean, unlabelled environment concept candidate B: EURYDICA OUTSKIRTS, Chapter 1 opening, NIGHT. Landscape 16:10, target 1280x800. Empty environment: no people, no characters, no UI, no lettering, no diagrams. This is an assembled art review candidate, not modular production artwork.
ATTACHED REFERENCE ROLES, in supplied order:
1 mosswood-style-board.png: left clean Tree Variants PRIMARY painted tree shapes and broad waking tree; right clean Props painted rocks and ferns. Full-resolution painted finish, never pixel8. Ignore board labels.
2 arrival-ward.png: distant wall and low green curved-roof South Gate design ONLY; ignore diagonal camera, daytime, labels and district layout.
3 gatehouse-south.png: approved pale large-block arch construction ONLY, not camera.
4 game-readability-board.png: left approved IMC broad simplified forms, right actual runtime world readability. Ignore people, portraits, UI, labels, lighting, city layout and rivers. Hylaea painted finish takes priority.
5 gameplay-camera-guide.png: PRIMARY PROJECTION, layout and scale lock. Replace schematic proxies with finished scenery, ignore grid, labels and outlined scale rulers. Straight north with zero diagonal rotation; perspective offset (0,18.4,21.8)m, 40 degrees down, vertical FOV30. Adult scale 93px at 1280x800, but OMIT figures.
LAYOUT LOCK: Same 30m east-west by 40m north-south site as guide, cropped at gameplay distance (do not zoom out to fit the whole plot). Waking tree ground anchor (-5,15), south root resting pad (-4.4,12.2), watching spot (-1.3,12.6). Broad waking tree left of centre, approximately 6.8m tall, natural roots frame a flat empty patch clearly visible on its south/right side. No root crossing the resting pad. Woods at WEST/left with a clear side lane towards (-12,17), leaving a visible break between trees. A broad 5m worn earthen road lies to the RIGHT of the tree, centered east=5, running STRAIGHT NORTH/up the screen. A quiet 3m ground link joins clearing to road. Open traversable centre, about 80% usable ground in metric footprint; foliage clusters at edges, no shrubs closing these routes.
Distant Eurydica wall and tiny recognizable low green-roof gate at the upper end of the road, behind the clearing: low contrast independent scenic matte in a thin uppermost band, conveys a ten-minute onward journey, never a giant castle immediately behind tree. At the locked down-facing camera there is no real sky horizon; do not tilt up or invent a broad cinematic sky. Gate is symbolic distant layer, separated by compressed quiet distance. No nearby city houses, no bridge, no water.
TAKE B: weathered indigo-and-olive verge. Same waking tree and placement, west woods exit and north road as the guide. Make the south-facing root hollow slightly more sheltered through broad moss shapes, with less leafy foreground intrusion and a broader quiet swath of earth. Matte indigo night shadows, muted olive foliage retaining local green, warm grey soil under broad cool ambient moonlight. Restrained earthy bark, cooler violet-grey distant wall. More sober and exposed feeling than the silver-sage take, without changing geometry or moving objects. Sparse rock-medium and fern-wide near outer boundaries only. The distant wall and green-roof gate should be low-contrast and substantially smaller than the waking tree, kept at the uppermost edge like a separate scenic strip; do not make this the city forecourt. Crop some upper waking-tree canopy naturally at top-left as a gameplay-distance camera would. Keep tree-root anchor near x=435,y=370 and road near x=970,y=450 at 1280x800; the usable rest patch lies southeast of the roots near x=455,y=460. No people. No labels. Painterly grouped foliage exactly as clean Hylaea reference; no pixel grid, no elaborate leaf noise, no glossy PBR, no cinematic fog, no visible rays, no pools of moonlight, no emissive windows, no lantern glow. Local Guild lighting belongs to engine. No invented furniture, fire, camp, bandits, tents, castle towers or river. Keep road wide, straight north; its convergence remains modest, never an eye-level vanishing-point landscape.
```

## A labelled companion: exact prompt

Sole attachment: `review/outskirts-concept-A.png`, role: locked art/source for annotation.

```text
Make a labelled ART REVIEW companion of the attached concept A. The attached image is the sole locked environment/source reference: preserve its composition, painted trees, road, terrain, night colours and gate. Do not redesign, move or add environmental content. Preserve landscape aspect ratio and full view. Add only clean readable cream review labels on small dark navy panels with thin cream leader lines and small terminal dots. Labels are presentation overlays, never in-world signs. Place panels around margins so the empty waking/resting area and central route remain legible. Add upper-left title panel reading exactly "EURYDICA OUTSKIRTS — A" and small subtitle "NIGHT / CONCEPT CANDIDATE — NOT APPROVED". Add four callouts exactly:
"01  WAKING TREE" leader to the large trunk left of centre.
"02  WOODS EDGE" leader to the open western passage behind/left of the waking tree.
"03  NORTH ROAD" leader to the broad road on the right half.
"04  DISTANT SOUTH GATE" leader to the green-roof arch at the upper end of the road.
Small footer: "SCENIC CITY LAYER / TEN-MINUTE JOURNEY CONTINUES OFF MAP".
Keep text correctly spelled, legible, and labels clear of their subjects. No characters, portraits, extra map graphics or fake UI.
```

## B labelled companion: exact prompt

Sole attachment: `review/outskirts-concept-B.png`, role: locked art/source for annotation.

```text
Make a labelled ART REVIEW companion of the attached concept B. The attached image is the sole locked environment/source reference: preserve its composition, painted trees, road, terrain, night colours and gate. Do not redesign, move or add environmental content. Preserve landscape aspect ratio and full view. Add only clean readable cream review labels on small dark navy panels with thin cream leader lines and small terminal dots. Labels are presentation overlays, never in-world signs. Place panels around margins so the empty waking/resting area and central route remain legible. Add upper-left title panel reading exactly "EURYDICA OUTSKIRTS — B" and small subtitle "NIGHT / CONCEPT CANDIDATE — NOT APPROVED". Add four callouts exactly:
"01  WAKING TREE" leader to the large trunk left of centre.
"02  WOODS EDGE" leader to the open western passage behind/left of the waking tree.
"03  NORTH ROAD" leader to the broad road on the right half.
"04  DISTANT SOUTH GATE" leader to the green-roof arch at the upper end of the road.
Small footer: "SCENIC CITY LAYER / TEN-MINUTE JOURNEY CONTINUES OFF MAP".
Keep text correctly spelled, legible, and labels clear of their subjects. No characters, portraits, extra map graphics or fake UI.
```

## Transport notes

An initial seven-reference call was rejected before generation by the tool's five-reference limit. The final five-reference prompts above are the successful generation calls. The local sprite-gen workflow probe could not access Codex CLI or Grok credentials; generation used the available native image tool under its built-in workflow. Generated bytes were copied into this run without resizing. The image tool also creates its own runtime-managed originals outside the run; all agent-authored project artifacts are confined to the requested run and report. Labelled companions are AI annotation edits; clean images remain the authoritative art candidates. No label pixels are intended for runtime.

