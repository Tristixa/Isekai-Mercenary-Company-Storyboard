# Eurydica facade candidates / facades-v1

Status: **candidate, not approved**. Prepared 2026-09-27 for the southern Eurydica explorable-town proof, Chapter 1 Scene 3. All production exports are in this run. No storyboard, skill, game, proof code, geometry or live texture was changed.

## Location brief

- Location ID: `eurydica-south`; artwork revision: `facades-v1`; building IDs and exact output paths come from `../../handoff/facades-spec.json`.
- Purpose: painted near-albedo UV elevations for existing 3D building volumes in a playable exterior. This is a layout-preserving texture pass. Curved roof geometry and runtime integration remain with the proof author.
- Buildings: tavern, company_house, repair_supply, provisions, gatehouse, lodging, stables, guard_shelter, store_shed, house_violet, house_green.
- Rendering: approved simplified IMC game appearance with the clean painted Hylaea finish and accepted tavern source as set anchor. Broad matte plaster, substantial structural timber, quiet stone and sparse construction joints. `fit.pixel_unfake: false`; no palette quantization or pixel-grid export.
- Palette: cream/peach plaster, dark brown timber, quiet grey stone; deep green and violet roofs, brown stable roofing and red/brown patchwork shed roofing; localized wine, cream and saffron cloth.
- Lighting: neutral near-albedo and soft recess/joint AO. Windows dark, lamp unlit, trough dry. Runtime owns directional light, cast/contact shadows, emissions and water.
- Facade camera: strictly straight-on orthographic elevation, each face seen from outside, ground at bottom. No roof plane or perspective baked into these UV faces.
- Props camera: approximately 40 degrees downward, looking north and front-facing, mild perspective; exposed tops. The retained courtyard reference supplied camera construction only, not pixel rendering. Generated object perspective remains an art approximation to be reviewed in the proof.
- Runtime camera: perspective follow camera, about 40 degrees down, looking north, no rotation; scrolling area. Viewport, world extent and nearest zoom were not remeasured because this task supplies individual UV faces rather than a city backdrop/master.
- Density: exact facade/tile dimensions at 64 pixels/metre. Props use estimated physical heights and ground depths at 64 pixels/metre with projected vertical/depth components; estimates are recorded in `props/anchors.json`.
- Gameplay: preserve the specified entrances and gate opening; no collision, navigation, UI, actor placement or occlusion changes were made. Roof overhangs/curves, porch, dormer, chimneys and steps require existing/separate geometry or later integration.
- Ground/open-space: no base ground is authored. The roughly 80/20 scene occupancy rule remains a proof-level concern; these separated wall and prop assets do not consume or redefine routes themselves.
- Ownership/history: tavern replacement door plank; provisions selling bay/storage door and broad plaster repair; repair shop reused work-door structure; modest Company house and patched shed; stable half-doors and loft hatch. No additional world lore is proposed.

## Deliverables

- 44 facade PNGs in the eleven building folders, with exact binary silhouette alpha.
- Four 512x512 roof tiles in `roofs/`, seamless in both axes; one 256x218 horizontally repeating city wall in `walls/`.
- Six exact-size attachment PNGs in `attachments/`.
- `props/sheet.png`: chroma-keyed production sheet; twelve extracted transparent cutouts and `props/anchors.json` with dimensions, bottom-centre ground anchors and estimated heights.
- `review/overview.png`: labeled overview of every building and all four faces, tile repeats, attachments and props. `review/assembled-tavern.png` and `review/assembled-company_house.png` compare faces at a shared metric scale and ground line. Additional roof 3x3 and wall 3x1/3x3 previews and prop cutout review are retained.
- `sources/`: untouched generated source bytes and all pre-existing tavern sources. `prompts.md` and individual `prompts/*.txt`: exact submitted prompts and attachment roles. `references/` and `reference-provenance.json`: frozen copies/hashes of referenced art.
- `manifest.json`: file inventory, byte sizes, image dimensions, alpha ranges, hashes and check summary. `check-results.json`: individual automated results.

## References and precedence

The user handoff and RESUME NOTE override older defaults. `sources/tavern-v2.png` is the explicitly accepted source and was not regenerated or overwritten. The older headings in the preserved beginning of `prompts.md` are historical; the RESUME NOTE is the current source-selection authority.

Every new building call attached its layout guide, its approved location concept, clean Hylaea Props, the accepted tavern sheet as "finish and detail level of this set", and the retained runtime environment screenshot. Concept references establish identity, never labels, lighting or camera. The tool accepts at most five paths; the approved identity concept also carried the simplified game appearance role. The initial six-path Company call was rejected before generation and was resubmitted with five explicit references.

Tiles and attachments attached an appropriate approved concept, clean Hylaea Props, accepted tavern and runtime screenshot. Props additionally attached the retained front-facing courtyard camera example. Exact ordered paths and their roles are in `prompts.md` and `reference-provenance.json`.

## Production and extraction notes

Generation used the session's built-in image tool. Sprite-gen's read-only start guide reported that its Codex CLI launcher was unavailable; the built-in tool itself worked, so no alternative provider/API or procedural painting was used. Sprite-gen's canonical `remove_chroma_background_ycbcr` extracted props and attachments. No global settings/defaults were changed.

The built-in returned RGBA source sheets despite the magenta prompts. Those exact returned sources are retained. For canonical extraction, low-alpha outer colour haze was excluded, then the objects were composited onto a pure magenta processing plate and keyed with the canonical extractor. `props/sheet.png` is that chroma production plate; it is not misrepresented as the untouched provider source. Alpha-edge cleanup and all resampling remain reproducible.

Facade RGB comes entirely from generated paint. Source crops are recorded in `source-crops.json`. `extract_facades.py` resamples source landmarks, extends painted edge pixels where necessary, and applies pixel-centre analytic gable/arch masks. Every silhouette interior is alpha255 and exterior alpha0, with transparent RGB scrubbed. Gatehouse north/south use identical paint.

The accepted tavern source has only two rectangular storeys on its north/south gables. Extraction repeats one existing painted upper storey on each gable to obtain three 3.1m storeys matching east/west; this is cut-and-resample assembly of accepted paint, not regeneration. Its source file remains byte-for-byte untouched. All three floor bands and foundation height are aligned in the paper review.

Doors were registered from manually inspected source door-leaf bounds, excluding jamb/lintel, to the required centre/width/height. The provisions source entrance was off-centre; piecewise resampling re-centres it while retaining the adjacent counter. `door-registration.json` records these transforms. Automated door checks verify those registrations; they are not independent semantic image recognition.

Roof crops begin/end at authored course joints; opposing edges receive only a 3px blend. The wall receives the same narrow horizontal edge cleanup. Roof previews use 3x3 repetition; the city wall has both requested review formats. No texture was painted procedurally.

## Designed beyond the concepts

The concepts are oblique exterior views, not cardinal elevations or measured blueprints. All exact cardinal window spacing, structural grids, floor bands and unseen rear/side treatments are reconstructed candidates. In particular: tavern/Company/repair/provisions rear elevations; lodging hidden rear and gable ends; stable east/rear walls and stall-door arrangement; guard booth back and blank-board face; shed back/side boarding; gatehouse narrow end elevations; and all four generic house elevations are newly resolved from the shared concept language. The named frontages preserve identity without claiming pixel-exact reconstruction of unseen sides. The generic houses and stables have no dedicated measured approved elevation.

## Validation and limits

Run with the installed sprite-gen Python environment (Pillow and numpy):

```powershell
& 'C:\Users\Tristixa-\.codex\skills\sprite-gen\.venv\Scripts\python.exe' -B 'D:\Codex\IMC\runs\facades-v1\check_facades.py'
```

The checker validates all fixed dimensions, every facade alpha pixel plus a sampled grid, opaque wall rectangles, edge continuity, identical gate faces, prop chroma residue, margins, anchor bounds and door registration. Read `check-summary.txt` for the actual latest result.

Visual review covered the labeled overview, both paper assemblies, tile repeats and extracted props against the approved reference language. Outputs remain candidates. Perspective calibration of props, anchor behavior, visible seams at actual camera distance, roof overlap and runtime lighting still need proof integration review. No runtime test or approval is claimed. No requested asset category was skipped.
