# Eurydica ground candidates — FGC_09 S4

Candidate assets for the owner, generated 2026-09-29. Start with [review.html](review.html). Nothing is installed in the game or published to the storyboard. The preview is a material mock, not an engine capture or an approved town-layout change.

## Deliverables

| Output | Specification |
| --- | --- |
| `tiles/earth.png` | Common warm compacted earth |
| `tiles/paving.png` | Court paving, irregular medium limestone flags |
| `tiles/paved_local.png` | Local-lane paving, smaller varied flags |
| `tiles/paved_main.png` | Main-spine / bridge paving, larger running-bond slabs |
| `tiles/dressed_stone.png` | Civic terrace / plaza, cleaner pale dressed limestone |
| `tiles/grass.png` | Continuous grouped olive-green lawn |
| `tiles/garden_bed.png` | Dark cultivated loam; plants remain separate |
| `tiles/<material>/repeat-3x3.png` | Actual 3072 × 3072 repeat, covering 12 × 12 m |
| `masks/earth-to-<material>.png` | Six 1024 × 1024, 8-bit greyscale painted edge-modulation masks |
| `masks/paving-edge-gaps.png` | 1024 × 1024 greyscale main-paving joint coverage, white = stone |
| `cutouts/edge-pieces.png` | 1536 × 1024 transparent atlas, 12 pieces in four columns and three rows |
| `cutouts/labelled-sheet.png` | Labelled 1536 × 1160 review companion |
| `cutouts/atlas.json` | Source rectangles, content bounds, ground anchors, suggested metre widths and heights |
| `composite-preview.png` | 2048 × 1200 unlabelled perspective assembly from these assets |
| `composite-preview-labelled.png` | Same assembly with review annotations |
| `market-patch-topdown.png` | Native 5120 × 3584 material-only ground assembly, 20 × 14 m |

All seven material exports are opaque RGB PNGs, **1024 × 1024 covering 4 × 4 metres**, or 256 texels/m. The three paving names are separate candidates, not missing aliases. Use linear filtering and mipmaps, repeat in both axes, and colour-space conversion for albedo. No pixel-grid processing, palette quantization, runtime lighting, cast shadows or water surfaces were added. Some painted stone edge and plant form accents remain part of the illustration; engine sun and cast shadows remain separate.

## Mask usage

These are tileable **edge modulation fields**, not complete polygon masks. Repeat them in world-space UVs at 4 m per repeat. The six fields are phase/rotation variants of one generated painted lobe master, maintaining the same edge vocabulary. Load them as linear data, not sRGB. UV origin and rotation can be chosen per zone; use the same world scale throughout a zone.

For positive-inside signed distance `d` in metres, and that edge's `blend_width_per_edge_m` value `w`, the preview uses:

```text
t = clamp((d + w/2) / w, 0, 1)
t = clamp(t + (painted_mask - 0.5) * 1.5 * 4*t*(1-t), 0, 1)
coverage = t*t*(3-2*t)
colour = mix(earth, target_material, coverage)
```

The entire transition stays inside the total `w`-metre band; white lobes advance the target material and black lobes recess it. The mock uses `w=0.7 m`. At 256 texels/m that band is about 179 texels. An edge with `w=0` uses a hard distance test, avoiding division by zero. Respect the plan's zero-width quay edges instead of applying the typical value everywhere.

For the main paving, sample `paving-edge-gaps.png` at exactly the same UV origin and scale as `paved_main.png`. White preserves stone and dark gaps reveal earth. Apply it only near the outer boundary, then fade it out within the positive half of the blend band so interior paving remains solid:

```text
edge_band = 1 - smoothstep(0, w/2, max(d,0))
coverage *= 1 - edge_band * (1 - stone_gap_mask) * 0.9
```

The gap mask follows the main paving tile; it is not UV-registered to the other two paving arrangements. Material switching at lane junctions is shown in the mock; exact junction geometry belongs to integration.

## Cutouts and scale

Reading order: two grass tufts, two moss patches, two pebble scatters, creeping clover, a low rosette, two leaf scatters, and two paving-chip scatters. The master has generous separation; the production atlas retains it. Atlas rectangles allow each cluster to be corrected or placed independently. Suggested widths range from 0.50 to 0.85 m, and height metadata stays at or below 0.25 m. These are explicit candidate placement choices, not measurements extracted from an approved game object.

The sheet was requested at the fixed north-facing camera looking approximately 40° down. Preserve the painted viewing angle when placing low billboards or decals. Use the recorded content bounds and anchors instead of sizing from transparent cell margins. `preview-scene.json` records the mock's placements. Cast/contact shadows are absent and remain engine-owned.

The first transparent generation contained blurry surrounding halos and was rejected for export. ImageGen replaced only its background with magenta; the installed sprite-gen `cutout --key magenta` route then performed canonical extraction and despill. Both generated masters are untouched in `sources/`. Cyan, magenta and yellow QA composites are retained beside the production sheet. The labelled sheet's checkerboard is presentation-only and is not in the production alpha atlas.

## Preview and camera

The 20 × 14 m mock contains an 8 m north/south main spine, a 4 m local lane, earth shoulders, grass, a garden bed, a small dressed-stone sample and 18 placements using all twelve cutout types. It is an illustrative material arrangement, not a claim to reproduce a particular polygon from the approved city plan. Most of the patch remains broad unobstructed ground.

The preview is a perspective ray/ground-plane projection using camera offset `(0,18.4,21.8) m`, straight north, 30° vertical FOV and pitch 40.16°. This follows the HD-2D proof camera contract. The wider output canvas contains the whole patch. Ground is bilinearly sampled; the cutouts are composited at their perspective-scaled metre widths. There are no people or unverified sprite-comparison claims. This does not validate Godot imports, terrain shaders, occlusion or runtime lighting.

## Sources and exact prompts

Generation used the **built-in GPT ImageGen tool**, with local reference images attached. Exact initial prompts and reference paths are in `brief-and-prompts.json`; the four targeted paving-repair prompts are in `repair-prompts.json`. No external API-key fallback or provider switch was used. The standalone sprite-gen workflow probe could not find its generation CLI in this environment; its local processing tools were available.

Reference copies and SHA-256 provenance are in `references/` and `reference-provenance.json`:

- Approved north-bank concept: ground colour, grass/earth boundaries and civic paving.
- Approved market-spine concept / retained v0.3: broad slab patterns and game readability.
- Approved arrival-ward concept: earth yards and local-lane palette.
- `HD-2D Proof/out/town/02-market.png`: camera and scale only; UI, characters and lighting excluded.
- Approved Facades v2 tavern south elevation and green roof: compatible painted finish. Tavern was attached to generation; roof was inspected as a supporting finish check.
- Approved Hylaea Calibration v1 `clean/Props.png`: plant rendering and grouped organic forms, attached to cutout generation.
- Retained actual-runtime appearance image: inspected for environment complexity; its portrait and UI are excluded.

The first five listed generation roles were attached to all seven material calls. Cutouts received north-bank, market, proof, Hylaea and tavern. The mask received north-bank and market. Repair calls received their exact affected candidate as edit target. `plan-ground-extract.json` preserves the read-only plan's ground zones/routes and source hash.

There are fourteen untouched generated PNG masters: seven material masters, one lobe mask, two cutout passes and four paving repairs. Generated square masters are 1254 × 1254; cutout masters are 1536 × 1024. Export sizes are separate from generation sizes. Source bytes and dimensions are independently recorded in `qa/validation.json` and `qa/source-hashes.json`.

## Processing and seam checks

1. `process_tiles.py` uses the installed sprite-gen `make_tile` implementation on both axes with a 1024 px period and 200 px overlap. Source material RGB is exported opaque; incidental generated alpha on two material masters is not interpreted as ground coverage. Originals remain unchanged.
2. Visual inspection found hard diagonal quilt joins in paving, despite some wrap-edge scores passing. Four targeted ImageGen repairs corrected the internal stone arrangement. `finalize_seams.py` fits the repair masters to 1024 px, retains a 4 px original border with a 12 px transition, and makes a 6 px wrap-colour correction. This is explicitly recorded processing, not a claim that raw generation was automatically seamless.
3. For the greyscale control field, the rejected hard quilt is replaced by a 230 px cosine overlap crossfade in each axis, then phase/rotation variants. This preserves broad lobes without hard internal cuts. The paving-gap control texture is derived from the final main tile's dark joints, denoised and thresholded with soft transitions.
4. `qa/seam-checks.json` contains final two-axis measurements: **14 images × 2 axes = 28 passing wrap checks**. Checks compare edge discontinuity against ordinary interior pixel variation. Original quilt reports and pre-repair images remain in `qa/` as history and can contain `needs-review`; they are not the final verdict.
5. Every material has a true full-size 3 × 3 repeat sheet. The review includes final repeat overviews, mask overviews, alpha checks and the assembled patch. Numeric seam scores do not establish owner approval or eliminate recognizable repetition on very large surfaces.

`build_review.py` rebuilds the preview, atlas metadata, overview sheets and offline HTML. To reproduce, run `process_tiles.py`, `finalize_seams.py`, then `build_review.py` with the installed sprite-gen Python environment and its package root on `PYTHONPATH`. Chroma extraction uses the installed `run-sprite-gen.cmd cutout` command documented above. Run `verify.py` last. All authored files stay in this run; the only external authored file is the requested six-line handoff report.

Remaining owner work: review these candidates, choose or revise the appearance, then authorize integration separately. No asset here is marked approved.
