# Eurydica: approved pixel art v1

Owner-approved on 2026-10-01, when the town moved to Proof 1's look: crisp pixel art at **1 art pixel = 4 cm (25 px per metre)**, transparent PNGs, alpha 0 or 255, 64 colours or fewer, shown in the game with nearest filtering. This set **supersedes the painted storybook finish** (Approved Facades v1–v3, Finish v2, the painted ground, trees and red tree) for the town. Those folders stay as history and as design references.

- `trees/`: `tree-broad`, `tree-tall`, `tree-young` (generated with references, then gridded).
- `landmarks/`: the red tree (13 m, same design as Approved Red Tree v1) and its fallen-leaf ring (10 m ground decal).
- `props/`: 49 props: streets and the Guild (lamp post, wall lantern v1b, handcart, barrels, crates, bench, banner, notice board, trough, hay, baskets, planter), the market (three stalls, four pictogram shop signs), work yards, gardens and quays, and the north bank (clock face, bell, mooring post, rowboat, fishing net, water pump, washing line, flower cart).
- `interiors/`: the Guild hall, Tier 2 annex and tavern pieces (owner-approved 2026-10-01): fantasy plants in old-world planters, fire, chandelier, lamps, cloth hangings, Mae's hanging cuts, and iconic oversized small items (tankard, loaf, candle, book, map roll, cleaver, notices, letter, pouch, shelf rows, forge fire, tavern pieces). Made by Codex under the `imc-pixel-props` skill (runs `pixel-guild-organic-v2`, `pixel-guild-small-v1`, `pixel-annex-tavern-v1`). Volume furniture is built in code (FurnitureKit), not stored here. The first interior set (`pixel-interiors-v1`) was rejected and removed.
- `*/meta*.json`: sizes, anchors (`anchor_px` or `trunk_base_px`, zero-based grid pixels), real sizes and provenance. `review/`: the review sheets the owner approved from.

Made by Codex (`D:/Codex/IMC/runs/pixel-trees-v1`, `pixel-red-tree-v1`, `pixel-props-v1`, `pixel-north-bank-v1`; untouched masters and attempts stay there). Buildings, roofs and ground are drawn in code by the game (`presentation/world/pixel_art.gd`), not stored here. No text, letters, logos or emblems anywhere.
