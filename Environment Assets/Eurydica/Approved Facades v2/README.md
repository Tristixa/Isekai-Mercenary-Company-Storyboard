# Eurydica: approved facades v2

The owner approved these on 2026-09-28 "for now". Anything they dislike later gets a **localized change** to that item only, not a new pass over the whole set.

The finish is storybook walls (A) with detailed-texture roofs (B), as chosen in `Approved Finish v2`. Codex painted them with `$imc-environment-art-direction`. They replace `Approved Facades v1` for all Eurydica buildings; the geometry contract (`facades-spec.json`) is unchanged from v1.

## Contents

- **Building faces:** `<building>/<n|e|s|w>.png` for all 11 buildings. The tavern and house_green are the Approved Finish v2 wall anchors, copied unchanged; the other 9 were repainted (36 faces). 64 px/m, the ground on the bottom edge, gables and gatehouse arches as in v1.
- **`roofs/`:** green, violet, brown and patchwork, 512×512 for 8×8 m. These are the **seamless corrections** from `D:/Codex/IMC/runs/roofs-v2-seamless/`. The first v2 tiles, including the style-test green anchor, had a dark 1-px border, an edge vignette and a repeating top course; the corrections keep the look and fix only the tiling. Seam-profile ratios: 0.992–1.002; course deviation ≤ 1.6%. See `Codex roof seam notes.md` and `review/roofs-tiled-3x3.png`.
- **`roof-kit/` + `roof-kit-spec.json` (new):** small and large dormers, stone and brick chimneys, 1- and 2-storey bays, as orthographic face textures with sizes, attach points and suitable roof colours.
- **`stalls/` + `stalls-spec.json` (new):** three market stall clusters (produce pair, red-tree court, herb row) painted for the gameplay camera, with bottom-centre anchors and canopy tops.
- **`attachments/`, `props/`, `walls/city_wall.png`:** unchanged from v1 after a compatibility review.
- **Records:** `Codex run notes.md` (check results: 514/514), `manifest.json` (hashes of the first v2 delivery; the four roof files were replaced afterwards), `prompts.md`, `door-registration*.json`, `sources/` (untouched generated sheets), `review/`.

**Source runs:** `D:/Codex/IMC/runs/facades-v2/` and `D:/Codex/IMC/runs/roofs-v2-seamless/`.

Not yet done: the Godot builder mounting the roof kit and stalls, and a review at the gameplay camera in the running town.
