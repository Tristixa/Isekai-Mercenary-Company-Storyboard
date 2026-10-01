# Eurydica: build plan v4 (approved; superseded by v5 on 2026-09-29)

Approved by the owner on 2026-09-28 as the **layout basis for the Godot town** (sprint S4 in `Game Design/FGC_09_Sprint_Plan.md`).

- `eurydica-plan.json`: the **construction source**, in metres, north up, +x east, +z south. It holds districts, routes, terraces, buildings (footprint, facade id, door face, `yaw_deg`), ground zones with blend widths, props, markers and the phase-1 slice. The Godot plan importer reads this file.
- `Eurydica Build Plan.md`: the human plan, with the v2 to v4 change notes and the conformance checklist.
- `eurydica-plan.svg` / `.png`: the to-scale map, rendered from the JSON.
- `check_plan.py`: geometry, access, connectivity, spacing and lock checks (PLAN_CHECK_PASS at approval).
- `review/`: the bird's-eye look views (interpretive candidates; **the JSON governs construction**).

**Key facts:**
- 83 buildings; median wall gap 2.35 m; 48 rotated buildings.
- Guild Edge beside the South Gate: the Guild house is 37 m from the gate, the stables 23 m.
- Arrival Ward has the lodging house east of the spine.
- A 28 m clock tower stands at the centre of the Civic Terrace (x 0, z −70).
- The walk from the gate to the market is 68 s.

**Refinements to make while building the town in M2** (noted at approval):
1. **The market stretch** around the red-tree court should read as green-roofed businesses (provisions, shops, stalls), not plum homes.
2. **Fill the leftover gaps:** the patch between the spine and the Service Lanes (orchard or allotments), and the very large bare Workshop and Quays yards (stacked materials, work areas).
3. **Add the roof kit** (dormers, chimneys, bays) and **market stall clusters** from the JRPG gap analysis (`D:/Codex/IMC/runs/eurydica-plan-v3/review/jrpg-gap-analysis.md`).

Source runs: `D:/Codex/IMC/runs/eurydica-plan-v4/` (plus v1–v3 history).
