# Eurydica

The frontier river town where Chapter 1 begins: the Guild's first base before the move to the Frontier. This folder holds only what is **current** for the HD-2D game. Everything from the earlier 3D plan is in `Archive/`.

## What Eurydica is

A walled river town. The **south bank** (from the South Gate up to the river) is the phase-1 play area: the Guild, the arrival courts, the market around the red tree and the service lanes. The **north bank**, across the Old Bridge, rises in terraces to the Civic Terrace and the clock tower, with the old city, the residences and the waterworks. The workshops and quays along the river are phase 2.

**The layout rule** (owner, 2026-10-01; full text in `Research/Eurydica City References/README.md`): "tight" means **clustered, not crowded**.
- Buildings come in clusters of 3–8 that touch or nearly touch (0–2 m apart), and each cluster has one purpose.
- Green space (meadow, groves, gardens) sits **between** clusters, never around each building.
- One winding main road runs from the South Gate to the Old Bridge, with about five branches, plus short door spurs and alleys.
- Wayfinding reads district → cluster → building. The landmarks (the gate, the red tree, the tavern and the clock tower) punctuate it.
- The target feel is the owner's reference `f03 illustrated`.

## Districts and clusters (plan v7c: 86 buildings, 21 clusters, 59 markers)

| District | Bank / phase | Clusters |
|---|---|---|
| Guild Edge | south, 1 | `gate_cluster`, `guild_compound` (with the HQ expansion reserve, hedged), `guild_neighbours` |
| Arrival Ward | south, 1 | `lodging_row`, `arrival_court`, `arrival_west_court`, `arrival_garden_court` |
| Market Spine | south, 1 | `red_tree_court` (the tree in a grass-and-earth bed), `market_row`, `market_homes`, `market_riverside` |
| Service Lanes | south, 1 | `service_lane`, `service_homes`, `service_garden_row` |
| Workshop Quarter | south, 2 | `workshop_yard` |
| Quays & Storeyards | river, 2 | `quay_row` |
| Civic Terrace | north, 2 | `civic_plaza` (the clock tower at (0, −70); the Alliance appointment markers) |
| Old City Streets | north, 2 | `old_city_row` |
| Residential Quarter | north, 2 | `residential_a`, `residential_b` |
| Waterworks & Gardens | north, 2 | `waterworks_group` |

The South Gate's inner face is 130.8 m from the river.

## The folder

| Path | What it is |
|---|---|
| `Build Plan/` | **The current build plan, v7c** (owner-approved 2026-10-01). `eurydica-plan.json` is what the Godot importer builds the town from. Read `Eurydica Build Plan.md` (metrics and the v7 → v7b → v7c record) and see `review/` (cluster map, bird view, v7b-vs-v7c). `checks/` has the checker (`check_plan_v7c.py` prints PLAN_CHECK_PASS), its result and the authoring scripts. |
| `markers.md` | The scene markers that scene scripts use (`Staging:` and cues). Living; add markers here when a scene needs them. |
| `Archive/` | History, not used (and not a style reference): Build Plans v4 and v5, the v0.1 city briefs, the 3D-era diagrams, the south-bank and north-bank layout concepts, and the Steambot Nefroburg references. |

## The approved art (elsewhere)

The art style is the **painted Unicorn Overlord-style storybook finish** (GDD §2.4). The 3D-era "simplified game appearance" district paintings were removed on 2026-10-01 (they remain in git history only); don't use them as references.

- **The finish anchors:** `Environment Assets/Eurydica/Approved Finish v2/` (storybook walls, detailed-texture roofs).
- **Environment pieces:** `Environment Assets/Eurydica/`: Approved Ground v1, Approved Red Tree v1, Approved Facades v3 (current; v1–v2 are earlier) and Approved Fantasy Plants v1.
- **Atmosphere** (Kingdoms of Amalur mood: warm sun, blue haze, red trees, lanterns, smoke): `Research/Atmosphere - Kingdoms of Amalur/`.
- **Layout references:** `Research/Eurydica City References/` (the owner's f01–f04 and six real towns).
- **Next to the town:** `Locations/Eurydica Outskirts/` (Scene 1).
