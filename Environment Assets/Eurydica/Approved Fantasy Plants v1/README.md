# Eurydica: approved fantasy plants v1 (owner approved 2026-09-30)

Open `review.html` for the local review. These are owner-review candidates, not approved or installed game assets.

## Deliverables

- `plants/`: 14 transparent RGBA PNGs, two independently generated specimens per species; eight matching grayscale emission PNGs.
- `atlas.json`: species, variant, dimensions in metres, pixel dimensions, bottom-centre anchor, mask association, source crop and candidate status.
- `labelled-sheet.png`: all specimens, labelled with height and mask availability; thumbnails are fitted for inspection rather than displayed at uniform world scale.
- `preview-day.png`, `preview-dusk.png`, `day-dusk-comparison.png`: all fourteen plants on the approved ground patch, with identical placements. Dusk lights the mask regions to illustrate emission intent.
- `mask-review.png`: each emissive cutout beside its aligned mask.
- `sources/`: untouched generated PNG masters and lossless base64 copies of the original tool payloads.
- `generation.json`: generation prompts and reference paths; `emberseed-a-prompt.txt` preserves the full first prompt.
- `references/`: unchanged local copies of the four attached art references and the approved ground used for compositing.
- `preview-placements.json`, `build.ps1`, `mask-review.ps1`: reproducible export and preview records.
- `qa.json`: file, alpha, alignment, dimensions, source-integrity and local-link checks.

## Design and camera

The design source is the **Fantasy plants** table in `D:/Storyboards/Isekai Mercenary Company/Research/Atmosphere - Kingdoms of Amalur/README.md`. Its seven FGC designs govern the output: matte orange Emberseed pods, blue-violet Stormfern tips, pale-gold Lantern caps, upright silver-white Silverleaf herbs, deep-red Crimson creepers, tall Skybells with small sky-blue bells, and teal Glassreeds with dew-bead tips. No Amalur screenshots were attached, and no Amalur plant artwork or names were used as asset designs.

The requested fixed game camera, approximately 40 degrees down and straight north, was stated in every generation prompt. This is painted camera matching, not a measured 3D projection. Both variants are independent specimens, not mirrored copies. Skybell retains its specifically requested small blossoms; the collection is plant set dressing rather than a flower bed.

Heights: Emberseed 0.7 m; Stormfern 0.8 m; Lantern cap 0.35 m; Silverleaf herb 0.6 m; Crimson creeper 1.0 m high by 1.2 m wide; Skybell 1.1 m; Glassreed 1.0 m. Unspecified widths are provisional estimates from each painted aspect ratio, recorded explicitly in the atlas. Preview vertical scale uses 160 pixels/metre times cos(40 degrees); this is a review scale, not a verified runtime binding.

## References and roles

Every generation attached these four files:

1. `D:/Storyboards/Isekai Mercenary Company/Environment Assets/Hylaea/Approved Calibration v1/objects/fern-wide.png` — fern shape language, grouped values, selective contours and painted finish.
2. `D:/Storyboards/Isekai Mercenary Company/Environment Assets/Hylaea/Approved Calibration v1/objects/bush-round.png` — clustered foliage and restrained painterly detail.
3. `D:/Storyboards/Isekai Mercenary Company/Environment Assets/Hylaea/Approved Calibration v1/objects/grass-tall.png` — long-leaf construction and matching paint treatment.
4. `D:/Storyboards/Isekai Mercenary Company/Environment Assets/Eurydica/Approved Red Tree v1/red-tree.png` — town palette harmony, especially Crimson creeper red; not plant anatomy.

`D:/Storyboards/Isekai Mercenary Company/Environment Assets/Eurydica/Approved Ground v1/review/composite-preview.png` supplies the approved preview ground. It was inspected and copied unchanged, then used for offline day/dusk assembly; it was not an image-generation attachment. The reference crops themselves and the explicit prompt supplied the plant camera guidance.

## Production and emission

The built-in image generator produced each master with transparency. Its automatic service cache is outside the deliverable; the returned PNG bytes were saved unchanged under `sources/`. No project or storyboard files were edited. The sprite-gen read-only workflow probe found its local generation CLI unavailable; the available built-in generator handled image production without API billing or a CLI fallback.

Exports crop transparent margins, keep native painted resolution, add eight pixels at the left, right and top, and align the silhouette to the cell's bottom edge. `anchor.normalized` is `[0.5, 1.0]`; pixel anchors describe canvas edges from the top-left. The images retain their generated alpha, with no palette quantization or pixel-unfake pass.

Emission maps share the exact cutout canvas and alignment. They are 8-bit grayscale-palette PNGs: black is non-emissive, white is emissive, and edge values retain alpha coverage. Color selection isolates each intended accent, followed by component cleanup and hole filling. Glassreed additionally uses manually reviewed bead regions to exclude leaf highlights. The editable selection rules are in `build.ps1`. Silverleaf, Crimson creeper and Skybell have no emission map.

The cutouts contain no added halo, bloom, ground lighting or cast shadow. Dusk is an offline illustration: the scene and plant albedo are dimmed and the mask regions receive emission colors. Godot should own intensity, tint and any eventual bloom or local lights. This preview does not claim engine integration. The simple fence supports behind creepers exist only in the review composition and are not part of the plant PNGs.

## Review and verification

Inspected all fourteen masters in a contact sheet, the labelled export sheet, emission masks beside their cutouts, and the ground composition. Corrected false-positive leaf/stem emission regions before delivery. Machine checks in `qa.json` cover counts, unique variants, required heights and creeper widths, transparent alpha, bottom-edge occupancy, mask canvas/alpha containment, grayscale palettes, untouched source hashes and existing local HTML links.

Owner approval and actual game import remain pending. The approximate camera match, provisional unspecified widths and final engine emission strength should be judged in the target game before approval.
