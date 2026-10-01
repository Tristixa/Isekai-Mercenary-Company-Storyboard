# Eurydica: build plan v5 (approved)

The owner approved this plan on 2026-09-29. It's a **localized update of the approved v4** and **replaces v4 as the construction source for the Godot town** (sprint S4, `Game Design/FGC_09_Sprint_Plan.md`). v4 stays next to it as history.

- `eurydica-plan.json`: the **construction source** (metres, north up, +x east, +z south). The Godot plan importer reads this file. SHA-256 starts `5bfc52f9e40090aa`.
- `Eurydica Build Plan.md`: the human plan. The v5 changes are at the top; v4's text follows.
- `eurydica-plan.svg` / `.png`: the to-scale map, rendered from the JSON.
- `review/`: measured top-down diagrams of the four changed areas.
- `roof-kit-schedule.md`: dormers, chimneys and bays per building.
- `checks/`: the plan checker (PLAN_CHECK_PASS at approval), its results, and the byte-diff proof that nothing outside the change list moved.
- New markers are in `../markers.md` under "v5 additions".

## What changed from v4

1. **The market by the red-tree court:** four buildings became green-roofed businesses (provisions, sundries, bakery, cloth). Three stall clusters of three awnings each, with crates, baskets and a barrow.
2. **Filled gaps:** about 20 props each in the Quays and Workshop yards (a hand hoist, a lean-to, carts, stacks, work benches, a drying rack, a tool shed). A fenced 30 × 42 m allotment garden between the spine and the Service Lanes, with ten beds, a shed, a water butt, compost and fruit trees.
3. **Roof kit** on all 83 buildings. Footprints and the roof colour rule are unchanged.
4. **Civic Terrace stage for the Alliance appointment** (GDD 14): five leaders facing south with the envoy beside them, the Commander facing them, five officers behind, and a camera hint. The plaza is unchanged, with at least 1.3 m between figures.
5. **The envoy's arrival:** spots just inside the South Gate and in the Guild courtyard.
6. **The adventurer dormitory is closed to the player:** the attic dorm, Dorm Annex and Larger Dorm are marked `player_access: false` ("adventurers' quarters"). There are six evening spots (Guild hall, courtyard, tavern) where adventurers can be found until 21:00, and two courtyard resting spots where the field-sleep sprites may be used.

**Unchanged:** every v4 building position and footprint, route, junction, district, terrain level, existing marker and portal. The gate-to-market walk is still 68.065 s, and the phase-1 area and HQ expansion reservation are unchanged.

**Still to do when building in S4:** the NPC schedules and door-lock behaviour are runtime work. v5 only records them in the plan.

Source run: `D:/Codex/IMC/runs/eurydica-plan-v5/` (including the superseded first density pass).
