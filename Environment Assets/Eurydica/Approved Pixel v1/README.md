# Eurydica: approved pixel art v1

Owner-approved on 2026-10-01, when the town moved to Proof 1's look: crisp pixel art at **1 art pixel = 4 cm (25 px per metre)**, transparent PNGs, alpha 0 or 255, 64 colours or fewer, shown in the game with nearest filtering. This set **supersedes the painted storybook finish** (Approved Facades v1–v3, Finish v2, the painted ground, trees and red tree) for the town. Those folders stay as history and as design references.

- `trees/`: `tree-broad`, `tree-tall`, `tree-young` (generated with references, then gridded).
- `landmarks/`: the red tree (13 m, same design as Approved Red Tree v1) and its fallen-leaf ring (10 m ground decal).
- `props/`: 49 props: streets and the Guild (lamp post, wall lantern v1b, handcart, barrels, crates, bench, banner, notice board, trough, hay, baskets, planter), the market (three stalls, four pictogram shop signs), work yards, gardens and quays, and the north bank (clock face, bell, mooring post, rowboat, fishing net, water pump, washing line, flower cart).
- `interiors/`: **superseded 2026-10-01** (the owner judged them noisy without clear silhouettes; kept only until the annex and the tavern are redone). Volume furniture is now built in code (FurnitureKit) and organic pieces come from Codex under the `imc-pixel-props` skill. 42 interior pieces for the Guild house (Tier 1), the Tier 2 annex (Workshop, Commerce + Information) and the tavern (owner, 2026-10-01; Codex run `pixel-interiors-v1`). Layout: `Locations/Eurydica/Interiors/Guild House Interiors.md`.
- `*/meta*.json`: sizes, anchors (`anchor_px` or `trunk_base_px`, zero-based grid pixels), real sizes and provenance. `review/`: the review sheets the owner approved from.

Made by Codex (`D:/Codex/IMC/runs/pixel-trees-v1`, `pixel-red-tree-v1`, `pixel-props-v1`, `pixel-north-bank-v1`; untouched masters and attempts stay there). Buildings, roofs and ground are drawn in code by the game (`presentation/world/pixel_art.gd`), not stored here. No text, letters, logos or emblems anywhere.
