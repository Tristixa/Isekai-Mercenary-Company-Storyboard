# Eurydica: approved facades v3 (owner approved 2026-09-30; phase-1 buildings without v2 art)

Seven facade IDs, 28 PNG elevations, eight phase-1 building instances. Prepared from `handoff/task-facades-v3-phase1.md`. No approval or live-game integration is implied. All authored work is inside this run apart from the requested six-line report.

Open **review.html**. `review/assembled-all-seven.png` shows the original plan yaw from the fixed north-facing camera. `review/storefront-all-seven.png` rotates each object to expose its entrance under the same 40-degree-down perspective camera (vertical FOV 30). These are actual textured box/curved-roof Blender renders, not image-generated mockups or live-game captures. Camera distance is 42 m, target height 5.4 m, at 1280x800; that framing fits every building at a common scale. The requested camera pitch/FOV/heading are preserved; follow distance is an isolated-preview framing choice.

## Geometry contract

`facades-spec-v3.json` follows the v2 schema, generated with the unchanged skill `facade_spec.mjs`. All faces are 64 px/m, outside-facing N/E/S/W, bottom-edge ground. The plan supplies no ridge-axis field for these missing facade IDs; the v2 north/south-gable convention (ridge z) is used. For all eight instances, the resulting `min(5, 0.55 * footprint_width)` equals the plan roof height. No plan field is changed. The inverse-yaw test independently confirms every world door position is the centre of its declared local face. Both warm homes share an 8x8 m footprint, 6.2 m walls, 4.4 m roof, east door and +10-degree yaw.

| Facade | Footprint m | Wall / roof m | Door | Roof | Plan instances |
|---|---|---|---|---|---|
| `market_bakery` | 9 x 8 | 6.2 / 4.95 | N | green | street_home_8 |
| `market_provisions` | 5 x 9 | 9.3 / 2.75 | E | green | infill_home_12 |
| `market_small_shop_east` | 6 x 6 | 4.4 / 3.3 | N | green | infill_home_06 |
| `market_small_shop_south` | 10 x 7 | 6.2 / 5 | W | green | infill_home_23 |
| `food_shop` | 10 x 9 | 6.2 / 5 | W | warm_red | food_shop |
| `clinic` | 12 x 10 | 6.2 / 5 | W | warm_red | clinic |
| `house_warm` | 8 x 8 | 6.2 / 4.4 | E | warm_red | service_home_0, service_home_2 |

## Finish, prompts and references

Generation used the built-in image tool, matching the v2 production route. No external API/CLI generation was used. Exact per-call prompts are in `sources/*prompt.txt` and consolidated in `prompts.md`; untouched generated masters and local-correction masters are in `sources/`. The tool's returned PNG bytes were saved directly because its default runtime image directory was not accessible to the workspace shell.

Every initial building call attached its layout guide plus approved `tavern/e.png`, `house_green/n.png` and `provisions/e.png` as **storybook finish A and detail anchors**. They define warm plaster, broad timber, dressed-stone plinth, soft painted edges, selective shutters, flower boxes and restrained wear/ivy. They do not impose another building's dimensions. `references/provenance.json` records source paths and hashes.

- Bakery and cloth shop: Market Spine concept, for shop-house identity. Arrival Ward concept was additionally attached to their localized corrections as context only.
- Provisions and sundries: Market Building Exteriors, for trade identity; original plan concept labels remain in the spec.
- Hilde's food shop, clinic and warm homes: Service Lanes, for named premises and residential identity.
- Concepts never set elevation perspective, text or baked lighting. All rear/unseen facades are conservative new candidates derived from the same materials and structural bands; the plan provides no surveyed opening layouts.
- Kingdoms of Amalur README was read for atmosphere only. No Amalur image was attached or copied.
- Green roof is the unchanged approved v2 seamless correction. Warm-red is a new supporting preview tile, generated against approved Finish B green plus the Service Lanes hue reference, cropped to four complete courses and edge-blended by the v2 method. `sources/roof-processing.json` records this. Roof geometry and ridge cap remain separate.

Production faces contain no lettering or heraldic emblems. Pictograms identify the trades. Lanterns and windows are unlit; paint uses neutral material shading and the approved soft contact occlusion only. Preview lighting is computed during rendering. No pixel grid, palette quantization or pixel-unfake was applied.

## Processing and checks

`process.py` retains exact inspected crops, invokes the unchanged v2 `fit_face.py`, registers door-leaf bounds with piecewise x/y coordinate resampling, aligns eave bands, then invokes unchanged `mask_faces.py`. Gable interiors retain linear vertical fitting; only exterior truss-edge colors are extended where needed before masking to avoid grey background under an opaque gable. This is resampling, not repainting. All transparent RGB is scrubbed. Door registrations describe visible leaves, not frames, at 1.4 x 2.3 m. Pictograms may change aspect slightly during exact-dimension fitting.

`review/check-facades.txt`: **254/254 v2 checks pass**, 28 exact-size faces, zero failures. This is a face-only spec; props and roof-tile checker branches are outside the requested scope. `review/delivery-audit.json` additionally verifies every plan footprint/height/door/palette, inverse-yaw door centres, bottom-edge opacity, registered leaf ground contact, all assemblies and camera metadata. Automated checks verify declared geometry/landmarks, not artistic approval.

Visual review covered all generated masters, corrected storefronts, extracted faces, door overlays, roof repeats and the assembled sheet. The bakery/cloth signs were moved inside their wall boundaries and the missing sundries lantern was added by localized generation. Original masters remain untouched. The owner should judge storefront density and painted awning depth in the isolated assemblies; awnings/counters are facade relief paint in this candidate pass, not extra protruding geometry. Approved roof-kit dormers/chimneys are not mounted by this isolated face-preview rig.

## Files and reproduction

- `<facade_id>/{n,e,s,w}.png`: final faces.
- `facades-spec-v3.json`, `door-registration-v3.json` (also `door-registration.json` for the v2 checker).
- `sources/plan-buildings.json`, `sources/buildings-input.json`, `sources/layouts.json`, `sources/processing-records.json`: geometry and fitting evidence.
- `review/assembled-*.png`, `review/storefront-*.png`, labeled sheets and door overlays.
- `prepare.py`, `process.py`, `render_previews.py`, `finalize.py` and unchanged skill scripts in `scripts/`.
- `manifest.json`: file hashes, excluding the manifest itself.

Use the installed sprite-gen Python environment for preparation/processing/finalization, and Blender 5.2 in background mode for rendering. Re-run `process.py`, `render_previews.py`, then `finalize.py`; `prepare.py` is the initial contract/guide builder. No project or storyboard writes are required.
