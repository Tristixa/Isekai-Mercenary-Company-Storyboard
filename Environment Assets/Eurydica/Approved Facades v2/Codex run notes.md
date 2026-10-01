# Eurydica facades v2 — CANDIDATES, NOT APPROVED

Prepared 2026-09-28 from `handoff/task-facades-v2.md`. Storybook finish A walls and detailed-texture finish B roofs. All authored files are in this run and the requested handoff report; project folders were read-only. Built-in image generation was used, followed by the environment skill's fitting, masking and checks. No live-game installation or approval is implied.

## Delivered

- **44 wall faces for all 11 buildings.** Repainted all four faces of company_house, gatehouse, guard_shelter, house_violet, lodging, provisions, repair_supply, stables and store_shed (36 faces). All eight tavern/house_green faces are byte-identical copies of the approved finish-A anchors.
- **Four 512x512 roof tiles**, covering 8x8 m each. Violet, brown and warm red/brown patchwork were repainted in finish B. Green is an unchanged approved anchor. New tiles use the style-test's 16-pixel opposite-edge blending; exact opposite-edge differences are zero.
- **Six attachments, twelve props, their anchors, and city_wall.png**, copied unchanged after visual comparison. The existing cloth has broad quiet folds and the timber/metal props already have restrained painted detail. They sit well beside the storybook walls. The quieter dressed-stone city wall remains a suitable municipal background. No item in this group required repainting.
- **Six new roof-kit modules, 20 face textures:** small/large dormers, stone/brick chimneys, and one-/two-storey bays. See `roof-kit-spec.json` for metre sizes, 64 px/m sizes, attachment points, roof compatibility and face reuse. Dormers/bays have front and both side returns; hidden rear interfaces meet the host. Chimneys include four elevations. Roof slopes and chimney top caps are builder geometry.
- **Three new stall clusters:** market_produce_pair, red_tree_court and market_herb_row. Complete props painted for a straight-north camera approximately 40 degrees down, including canopy tops; no separate canopy geometry is used. `stalls-spec.json` records sizes, source crops and bottom-centre anchors. Height/depth are art estimates for the builder to inspect in the town.
- `facades-spec.json` is copied from v1 without changing a byte. `prompts.md`, untouched generated sheets, processing records and image hashes are retained.

## Review

- `review/overview.png`: every building and all four labeled faces, at a common scale.
- `review/v1-v2-compare.png`: every building's entrance face before/after.
- `review/roof-kit.png`, `review/stalls.png`: the new kits at labeled sizes.
- `review/materials.png`: roof repeats and unchanged attachments/props.
- `review/assembled-company_house.png`, `review/assembled-tavern.png`: ground-aligned paper assemblies.

Owner review should focus on flower/ivy density, the new dormer/bay proportions, and stall scale/contact at the actual gameplay camera beside 93-pixel characters. These are candidate texture deliveries; the Godot builder still mounts the new assets. No runtime screenshot, collision test or in-town approval was claimed.

## Contract and processing evidence

The v1 openings and structural identity were retained, with local piecewise coordinate registration for **74 glazed window openings and eight repainted contract doors**. Gatehouse arrow slits, stable half-doors, hatch, shed vent and provisions selling hatch were visually checked. North/south gatehouse paint is identical. Existing unseen faces inherit v1 rather than adding new architectural layouts. New kit side returns extrapolate the concept materials and form.

`sources/processing-records.json` records exact source crops and `fit_face.py` calls; `sources/landmark-registration.json` records window source/target bounds. `door-registration.json` describes the delivered paintings, including the original style-test records for the two anchors; `sources/door-registration-v1.json` retains v1 history. `mask_faces.py` applies the analytic silhouette to the 36 repainted faces only, so approved anchor files stay byte-identical.

The lodging generation replaced a lower window with a sign; a local image edit restored it. A generated lamp on the court stall was removed. Source alpha haze was removed before resizing stalls. Roof-kit grey stone was protected with explicit masks after visual review caught background-removal damage. Frames were reviewed again after refining the local registration boundaries. No palette quantization or pixel-unfake was used.

`facade_spec.mjs` independently regenerated all 44 face dimensions, types, wall/gable heights, doors and arches from reconstructed building inputs; every value matched v1. Its verification output stays in `sources/`, separate from the unchanged delivered contract.

Required command:

```text
check_facades.py --spec D:/Codex/IMC/runs/facades-v2/facades-spec.json --run D:/Codex/IMC/runs/facades-v2
```

Result:

```text
PASS: 514/514 checks; 0 failures. 44 faces; 55 exact-size images; 12 props; 0 magenta-like prop pixels. Roof/wall opposite-edge max difference: 0/255.
```

`review/check-facades.txt`, `review/spec-verification.txt` and `review/delivery-audit.json` hold verification evidence. The additional audit checks unchanged-source hashes, 36 distinct repaints, kit texture dimensions, chimney opacity and stall margins/anchors. Automated checks validate the declared contract; door checks use inspected landmarks, not independent image recognition. `manifest.json` lists PNG hashes.

## Reference provenance

Primary roots: `D:/Storyboards/Isekai Mercenary Company/Environment Assets/Eurydica/Approved Facades v1/`, sibling `Approved Finish v2/`, and `D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/concepts/`.

Each generated building attached its v1 assembled face sheet as **layout and identity**, its concept as **identity only**, and approved `walls-A/house_green/e.png` as **rendering only**. Company house, store shed and violet house use Company Edge; lodging, stables, guard shelter and gatehouse use Arrival Ward; provisions and repair supply use Market Building Exteriors. New roof tiles attach their own v1 hue tile and `roof-B/green.png` as finish reference. The roof kit attaches Company Edge, Market Building Exteriors and the same finish-A wall. Stalls attach Market Spine or Company Edge, the finish wall, and the approved handcart as camera reference. The oblique concepts never set facade perspective.

Reproduction scripts are stored in this run. Use the installed sprite-gen Python environment for Pillow/NumPy and the companion environment scripts under `D:/Godot Projects/IMC-Companion-Skill-Environment/scripts/`. Generation itself uses the built-in tool; no external CLI/API fallback was used.
