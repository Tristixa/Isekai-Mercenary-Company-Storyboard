# Guild house redesign v2: proposal

**Status:** approved by the owner on 2026-10-01 and built in the game (Tier 1 hall and exterior first; the annex and tavern follow). Plan v7d carries the bigger hall. It replaces the v1 rooms (`Guild House Interiors.md`, judged cramped, warehouse-like, yellow, with clipping stairs and open bedrooms). Nothing is built until the owner approves this plan.

**Owner direction:** a proper fantasy adventurers' guild where players are comfortable spending most of their days. Tier 1 is a real workplace, not a castle (that's the Frontier HQ). Neutral colours, not yellow; greenery; big windows; closed bedrooms; Mae gets a processing room. The exterior may change as much as needed. References: `Research/Atmosphere - Kingdoms of Amalur/Interiors/` (take the structure and comfort, not the dark brown palette).

## The look

- **Palette:** pale warm-grey plaster walls; dark walnut timber (posts, beams, the gallery rail); grey-blue flagstones in the hall and light oak boards in the private rooms; fabrics in navy, sage and cream; brass and dark iron fittings. Wood is used for structure and furniture, not on every surface, so things stand out.
- **Greenery everywhere:** potted ferns and palms, hanging ivy baskets, flower boxes on the inner window sills.
- **Light:** tall north windows are the main light by day (glass panes that glow, plus a cool daylight fill); a ring chandelier, wall lamps and the hearth are warm accents, and take over in the evening.
- **Furniture:** volume pieces are built in the game as 3D shapes with pixel textures (beds, tables, desks, chairs, counters, shelves, chests, crates, barrels, stairs); Codex makes the organic pieces with the new `imc-pixel-props` skill (plants, fire, chandelier, cloth hangings, food, bottles).

## The exterior (town plan change)

The Tier 1 Guild house grows from 7.5 × 7.5 m to a **two-storey guild hall of about 19 × 14.5 m**, north of the Guild yard (x −41 to −22, z 91 to 105.5). The yard, the gate side and every scene marker stay where they are.

- A **stone ground storey** and a **timber-framed upper storey** with diagonal braces (Amalur's Guild exterior), tall ground-floor windows, a central **arched double door** at the top of **wide stone steps** facing the yard, a **lean-to porch** on posts along the front, a small **dormer tower** over the door, lamps on brackets, flower boxes, and a hanging sign with a plain sword-and-scroll pictogram (no letters, no emblem).
- **Roof: slate blue** (owner, 2026-10-01, from the Amalur reference `631007081851.jpg`): dark blue-grey slate shingles. No other building in Eurydica uses blue, so the Guild hall reads as its own landmark from anywhere in the south bank, and it matches the Guild's navy cloth. The Tier 2 annex shares it. The GDD roof colour rule gets a new line: blue is the Guild's colour.
- **Neighbours:** the stables shift 4 m west (still beside the HQ reserve); the store shed goes (its storage moves into the hall's processing room and later the Tier 2 Workshop). The plan checker is re-run so every door, route and marker stays valid.

## Tier 1 interior: ground floor about 28 × 16 m

The hall is wider than one screen (about 14 m across at the camera's focus), so it feels open as you walk through. The front (south) wall is cut away for the camera as before. **Closed rooms** have four walls and a door; when the Commander is inside one, its front wall fades out (the same cutaway as the town).

```
 north wall: tall windows over the hall
+------------+--------------------------------+------------+
| COMMANDER'S|        MAIN HALL (double        | OFFICERS'  |
| OFFICE     |        height, gallery above    | ROOM       |
| desk, books|        the north side)          | 3 beds,    |
| objective  |   [ long meeting table, 6 ]     | wardrobes, |
| board, bed |   under the big windows         | a window,  |
| alcove     |                                 | plants     |
| (closed)   |   hearth + lounge   chandelier  | (closed)   |
+---door-----+   (armchairs, rug)              +---door-----+
| PROCESSING |                                 |  STAIRS up |
| ROOM (Mae) |   plants, banners   reception   |  to the    |
| table,hooks|                     counter     |  gallery / |
| tub, cold  |                     (Tristitia) |  dorm (no  |
| store;     |                     + request   |  entry)    |
| door to the|                     board       |            |
| yard       |                                 |            |
+------------+------------ front doors --------+------------+
 south: open to the camera; the Guild yard beyond
```

- **The main hall (14 × 16 m, double height):**
  - **the long meeting table for six** under the tall north windows (Scenes 3, 5, 6: `table_north`, `table_south`, `table_east`, `table_west` and two more);
  - **the hearth lounge:** a stone hearth with armchairs, a low table and a big rug, the comfortable heart of the room;
  - **Tristitia's reception counter** by the entrance, with ledgers, and the **request board** beside it (blank pinned papers): her working place for requests and briefings;
  - a **gallery** along the north side above (decorative: it leads to the dorm; no entry), heavy timber posts, a ring chandelier, plain navy and sage cloth hangings, and plants throughout.
- **The Commander's office (west, closed, 7 × 7 m):** desk with the objective board above it, bookshelves, a window, a chest, a rug, plants, and a curtained **bed alcove** (Scene 3: "This room is yours. It will also serve as your office").
- **Mae's processing room (south-west, closed, 7 × 7 m):** her processing table, hooks with hanging cuts and pelts, a wash tub, a cold store, shelves, and its own door out to the yard so carcasses never cross the hall. In Tier 2 she moves to the Workshop; this room becomes the Guild's storeroom.
- **The officers' room (east, closed, 7 × 7 m):** three beds (Tristitia, Mae, Elsie) with their own quilts, wardrobes, a window, a small table, plants.
- **The stairs (south-east):** a proper flight with a landing rising to the gallery, with clearance on all sides so nothing clips. The player can't go up ("adventurers' quarters").

## Tier 2 annex and the tavern

- **The Tier 2 annex** keeps its plan (Workshop with the four tables, Commerce + Information, Officers' Room II) but grows to about **24 × 14 m** with the same palette, tall windows and plants. Officers' Room II is **closed**, and the Workshop has stone floors, the forge glow and big yard doors.
- **The tavern** grows to about **20 × 14 m**: a bar along the back, a hearth, tables on rugs with high-backed chairs, hanging lanterns, a gallery and stairs to the inn rooms (no entry).

## Order of work after approval

1. **Codex** (skill test running now): plants, hearth fire, chandelier, cloth hangings; then the rest of the organic pieces.
2. **Claude:** the 3D furniture kit (tables, chairs, beds, desks, counters, shelves, chests, crates, barrels, stairs, the hearth surround), the room builder with closed rooms and the cutaway, window glass that glows, the new exterior and the plan change with checks.
3. Screenshots of the Tier 1 hall first, for review, before the annex and the tavern.
