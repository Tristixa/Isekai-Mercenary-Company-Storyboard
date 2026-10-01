# Eurydica: approved ground v1

The owner approved this set on 2026-09-30 for the Godot town (sprint S4). Later dislikes get a **localized change** to the item concerned only.

- `tiles/<material>.png`: seven seamless painted tiles, 1024 × 1024 for **4 × 4 m**:
  - `paved_main`: the 8 m spine and the bridge;
  - `paved_local` and `paving`: the 4–5 m lanes;
  - `earth`: the common base;
  - `dressed_stone`: the civic terrace and plazas;
  - `grass`;
  - `garden_bed`.

  These match the plan's `ground_zones[].material` and `routes[].surface`. There's no light, shadow or water baked in. They're painted art, so they use linear filtering.
- `masks/`: tileable greyscale blend masks for the soft, lobed edges between earth and each material (0.7 m blends per the plan), and `paving-edge-gaps.png` for irregular stones where paving meets earth.
- `cutouts/`: 12 edge pieces (grass tufts, moss, pebbles, weeds, leaves, paving chips) in `edge-pieces.png`, with `atlas.json` rectangles and a labelled sheet.
- `review/`: the 20 × 14 m market-spine composite at the game camera, and a top-down assembly.
- `Codex README.md`: the production record, with 131 checks including 28 seam axes. Source run: `D:/Codex/IMC/runs/fgc-s4-ground/` (prompts and untouched masters).

Known weaker spot, noted at approval: the garden-bed soil reads somewhat flat and blotchy. Revisit it only if it looks wrong in the game.
