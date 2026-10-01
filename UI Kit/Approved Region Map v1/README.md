# FGC region map, approved v1

The owner approved this look on 2026-09-29. It's the reference for the region map and area detail screens in sprint S5 (`Game Design/FGC_08_UI_HUD_Spec.md` §5.9), so S5 builds from this package instead of the research screenshots.

## Contents

- `mockups/`: the three 1920×1080 proofs:
  - `A-hylaea.png`: Hylaea selected, 42% explored, with two discoveries drawn in;
  - `B-erythra-locked.png`: a locked area;
  - `C-frontier-structure.png`: the region tabs after the move. Structure only: Frontier names are not authored.
- `sources/map-master.png`: the painted Eurydica region map, untouched, with no text. Its prompt and provenance are alongside it.
  - **The geography is a proposal, not canon:** the city at one edge, the South Gate road to Hylaea, Bernmoor downstream on the river, and the Erythra Highlands farthest.
- `overlays/`: Hylaea's discovery ink drawings (two dens, a landmark, two hidden paths), aligned to the map as transparent PNGs. `sources/placement-manifest.json` has their positions.
- `previews/`: each area's preview, composed from its approved battle-background layers.
- `checks/`: 1280×720 views and the contrast and overflow checks.
- `Codex README.md`: the production record. The full run, including the superseded first draft, is in `D:/Codex/IMC/runs/region-map-v1/`.

## Owner refinements for the Godot build (2026-09-29)

These are to apply when the screen is built. They don't require redoing this proof.

1. **Elsie's corner, in Atelier Ryza's style:**
   - her portrait sits in a **white, semi-transparent circle with a thin border**;
   - the dialogue box is **white and semi-transparent with a thicker border**.
2. **Cards:** add a **thin border** to the map and detail cards, or give them **rounded corners**.
3. **Background:** replace the flat navy with a **semi-transparent horizontal gradient**: low-opacity navy (or white) at the left and right edges, fading to **transparent in the middle**, so the world shows through.
4. **The help ribbon** ("Choose an area, then an operation"): add the header **pattern** and a **thin border**, like the Q/Enter/Esc hint plates.
