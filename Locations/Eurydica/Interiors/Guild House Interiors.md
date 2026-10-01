# Guild house interiors: design proposal (v1)

**Status:** layout approved by the owner on 2026-10-01 (Tier 2 as a separate annex on the reserved plot; the meeting table always present; dorm 4 beds from the start, 8 after the Dorm Expansion). Next: Codex makes the pixel furniture, Claude builds the rooms in Godot (code-drawn pixel walls and floors, like the town), and the plan's interior records and markers are updated.

## Owner decisions this design follows (2026-10-01)

- **Eurydica follows Scene 6, not the GDD's Frontier department layout.** Officers get separate department rooms only in the Frontier.
- **Tier 1:** Mae works in a **processing corner of the main room**. Elsie works from the **courtyard** (her bench, as in Scenes 3–5). Tristitia works at the **main-room table** and in the Commander's office.
- **Tier 2** (Scene 6, objective C1S6-1) adds, in one upgrade:
  - a **second officers' room** (Fulker, Valerie, Liliana sleep there);
  - a **Workshop** for both processing and crafting, with **4 tables**: Mae, Fulker, and one for each staff member (processing staff, craftsman);
  - **one Commerce + Information room** for Valerie and Liliana (separate rooms only in the Frontier);
  - it **unlocks** the dormitory expansion from 4 to 8 beds.
- **Not shown to the player:** dormitory interiors, a kitchen (Frontier content) and the inn.
- **The tavern common room** is needed (Scene 2).

## How interiors look and play

- **The same look and camera as the town:** pixel walls and floors drawn in code at 25 px/m, Codex pixel furniture, the close HD-2D camera, depth blur and bloom. Warm lamps and the hearth are the main light; daylight comes through the windows.
- **The wall nearest the camera (south) is cut away**, as in Octopath interiors, so you look north into the room. Partitions between rooms are low-cut (half height) on the camera side, so the player can see into the neighbouring room.
- **Interiors are bigger than the outside.** This is the usual HD-2D convention. The exterior footprint is 7.5 m, but a 7 × 7 m interior can't hold a meeting table, a processing corner and two bedrooms at our camera distance. The interior is about **12 × 9 m**. The exterior stays as approved.
- **Doors:** walking into the courtyard door or the front door fades to the other scene (the plan's portals).

## Tier 1: the Guild house (ground floor, 12 × 9 m)

North is up; the camera looks north from the south (bottom).

```
 north wall (windows)
+---------------------+----+-----------------------+
| COMMANDER'S ROOM    |stair| OFFICERS' ROOM        |
| = his office        | to  | Tristitia, Mae, Elsie |
| bed, desk with the  |dorm | 3 beds, wardrobe,     |
| objective paper,    |(no  | chest, a small table  |
| chest, window       |entry)                       |
+-----door------------+----+--------door-----------+   <- low partition
| hearth                                            |
|      +-----------+                 PROCESSING     |
|      |  MEETING  |                 CORNER (Mae)   |
|      |   TABLE   |  4 seats        table, hooks,  |
|      |  (N S E W)|                 tub, barrels   |
|      +-----------+                                |
| unfinished bay (west)        unfinished bay (east) |  courtyard door (east wall)
+--------------------  front door  -----------------+
 south wall: cut away for the camera
```

- **The main room** (12 × 5 m, south half):
  - **the big meeting table** with four seats: `table_north` (Tristitia), `table_south` (Commander), plus new `table_east` and `table_west`. Scenes 3, 5 and 6 use it; Scene 6 seats all four.
  - **a hearth** on the west wall, for warmth and evening light. It isn't a kitchen.
  - **Mae's processing corner** in the east part: a heavy processing table, hanging hooks, a wash tub, barrels and crates. This is Scene 4's "Processing corner".
  - **two "unfinished" bays**, west and east (`unfinished_west`, `unfinished_east`): bare plank floor, sheeted furniture, stacked crates and a ladder. Scene 3's camera pan reveals them. They stay as storage after Tier 2, tidier.
  - **the courtyard door** on the east wall, which leads to the courtyard (Elsie's bench, the yard).
- **The Commander's room**, north-west (5 × 4 m): his bed, a desk that is also his office (Scene 3: "This room is yours. It will also serve as your office"), a chest and a window. **The objective paper** is pinned above the desk, where Tristitia writes the objectives (Scene 6). The doorway markers `office_door_west` and `office_door_east` stay outside its door.
- **Stairs to the dormitory** (north centre, 1.5 m): visible, but the player can't use them ("adventurers' quarters"). The dorm itself is never shown.
- **The officers' room**, north-east (5 × 4 m): three beds (Tristitia, Mae, Elsie), a wardrobe, a chest and a small table. The player can walk in, so at night the officers are seen sleeping there.

## Tier 2: the Guild hall annex (new building in the reserved plot)

The Tier 1 house is full. Tier 2 is the **expansion** Scene 6 describes ("we need to do expansion on the guild house"). It's a new building on the **HQ reservation** next to the Guild yard: the hedged plot west of the stables, which the plan has kept clear for this. Its door faces the Guild yard. Inside it's about **14 × 10 m**:

```
+---------------------------------+-----------------------+
| WORKSHOP (processing + crafting)| COMMERCE + INFORMATION|
|                                 | Valerie: trading      |
|  [Mae]  processing table,       | counter + shelves     |
|         hooks, tub, cold store  | (Trading Shelves      |
|  [Fulker] forge + anvil +       |  upgrade adds two)    |
|         workbench, chimney      |                       |
|  [staff] processing table       | Liliana: desk, map    |
|  [staff] crafting bench         | wall, rumour board    |
|  material shelves, racks        | (blank papers)        |
+------------ wide doors ---------+-------door-----------+
|  yard side (corpses come in)       OFFICERS' ROOM II    |
|                                    (rear, 3 beds:       |
|                                    Fulker, Valerie,     |
|                                    Liliana) + stairs to |
|                                    the dorm (8 beds,    |
|                                    not shown)           |
+---------------------------------------------------------+
 south wall: cut away
```

- **The Workshop** (west, about 8 × 6 m) has four tables, as decided:
  1. **Mae's processing table** (she moves here from the main-room corner when Tier 2 is built), with hooks, a tub and a cold store;
  2. **Fulker's forge, anvil and workbench**, with a chimney and the forge glow;
  3. **a processing staff table**;
  4. **a craftsman's bench**.

  It also has shared material shelves and racks, and wide double doors to the yard for bringing corpses in.
- **The Commerce + Information room** (east, about 6 × 6 m):
  - **Valerie:** a trading counter with goods shelves (the *Trading Shelves* upgrade visibly adds two shelves).
  - **Liliana:** a desk, a map wall and a rumour board with pinned blank papers (no writing).
  - Cassia (information clerk) takes a stool at Liliana's desk once she joins (after C1S7-1).
- **Officers' Room II** (rear, about 6 × 4 m): three beds for Fulker, Valerie and Liliana, a wardrobe and a chest. The player can walk in.
- **Stairs to the dormitory** (not shown): the expansion to 8 beds is an option Tier 2 unlocks. It changes capacity only, not anything visible.
- After Tier 2, **Mae's old corner** in the Tier 1 main room becomes a tidy storage corner. The meeting table stays.

## The tavern common room (Scene 2), about 10 × 8 m

A bar counter along the north wall with the innkeeper, a hearth on the west wall, four or five tables, and Mae's table near the hearth (`table_west`, `table_north`, `table_east`, `mae_side`, as Scene 2 stages them). Lanterns hang from the beams, and the stairs to the inn rooms are visible but closed.

## Pieces for Codex (pixel furniture), once the layout is approved

Meeting table and four chairs; hearth; beds (single, three styles); desk; wardrobe; chests; sheeted furniture; ladder; Mae's processing table, hooks, tub and cold store; forge, anvil and workbench; processing staff table; craftsman bench; material shelves and racks; trading counter; goods shelves; Liliana's desk; map wall; rumour board; wall lamps; the bar counter and stools; tavern tables and benches; a stair piece. No text, letters or emblems.

## Plan and GDD changes on approval

- `eurydica-plan.json` interiors: resize `guild_interior` to about 12 × 9 m and add `table_east` and `table_west`. Add `guild_annex_interior` (Tier 2) and its portal in the HQ reservation, and the annex building on the reserved plot.
- GDD §5 and §12.7: Eurydica uses this Tier 1 / Tier 2 plan. The single Tier 2 upgrade replaces *Officers' Quarters II* and the separate Second Workbench and Second Processing Table. The dorm expands from 4 to 8 after Tier 2. Department rooms come in the Frontier. Kitchen meals are Frontier content.
