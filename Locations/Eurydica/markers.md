# Eurydica: scene markers

Named positions that scene scripts use in `Staging:` and in cues (`move`, `enter`, `exit`, `pan`). See `Game Design/Scene Script Format.md`. Each location scene in the game places these markers; the script converter reports any marker a scene uses that isn't listed here. Add new markers here when a scene needs them.

## Eurydica Outskirts (Scene 1)

- `tree_rest`: beside the tree where the Commander wakes and later rests; room to lie down and sit.
- `tris_watch`: a few steps from the tree, where Tristitia stands watching him; both in one shared view.
- `woods_edge`: where the path enters the deeper woods; Tristitia leaves and returns here.
- `road_gate`: the start of the road toward Eurydica's South Gate.

## Eurydica South Gate (Scene 1)

- `main_street`: just inside the gate on the main street, heading north toward the tavern.

## Eurydica Tavern (Scene 2)

- `table_west`: the Commander's seat on the west side of the table, facing east.
- `table_north`: Tristitia's seat on the north side, facing south.
- `table_east`: Mae's seat on the east side, facing west.

## Guild house (Tier 1) interior (Scene 3)

- `table_north`: Tristitia's chair on the north side of the main-room table, facing south; the open ledger lies between them.
- `table_south`: the Commander's chair on the south side, with room to stand beside it and sit facing north.
- `courtyard_door`: clear approach to the doorway between the main room and the courtyard.
- `office_door_west`: Tristitia's stop west of the open Commander-room doorway, facing east, leaving the passage clear.
- `office_door_east`: the Commander's stop east of the doorway, facing west, leaving the passage clear.
- `unfinished_west`: camera target on the west part of the unfinished main room, close enough to keep the Commander in frame.
- `table_east`: Elsie's seat on the east side of the meeting table, facing west (Scene 6).
- `table_west`: Mae's seat on the west side of the meeting table, facing east (Scene 6).
- `processing_corner`: Mae's processing corner in the east part of the main room (Scene 4 talks, Scene 6).
- `unfinished_east`: camera target on the east part of the unfinished main room, completing the slow sweep.

## Guild house (Tier 1) courtyard (Scene 3)

- `interior_door`: courtyard-side approach to the main-room doorway.
- `bench_east`: Elsie's position east of the equipment bench, facing west toward the damaged travel pack.
- `bench_south`: Tristitia's stop south of the bench, facing Elsie.
- `bench_west`: the Commander's conversation position west of Elsie, with a clear route around the bench.

Scene 4's talks and ambient lines use `Where:` descriptions instead of markers; each talk happens where that character stands in the world.


## Guild house (Tier 2) interior (Scenes 7 and 8)

The main room after the Tier 2 upgrade; every Tier 1 interior marker above stays valid. `courtyard_door` is the hall's front double door to the yard. Positions are in `Interiors/interiors.json` (`guild_house.markers`).

- `reception`: Tristitia's place behind the reception counter. Scene 7 turns her to face west along the counter.
- `reception_west`: the Commander's place at the counter's west end, beside Tristitia, facing west into the hall.
- `hall_centre`: the open floor west of the reception counter, facing east toward it; where a visitor stops (Scene 7, Fulker).
- `arrival_1`, `arrival_2`, `arrival_3`: where Tristitia and the two new officers stop inside the doors, facing east (Scene 8).
- `wait_1` to `wait_4`: standing places by the meeting table, facing south toward the doors, where the officers wait (Scene 8).
- `greet_1` to `greet_4`: closer places facing west toward the arrivals, for the introductions (Scene 8).

## Guild annex (Tier 2) Workshop (Scene 7)

- `fulker_station`: Fulker's crafting table, facing south (work animations face south).
- `workshop_watch_w1`, `workshop_watch_w2`: watching places west of Fulker's table, facing east.
- `workshop_watch_e1`, `workshop_watch_e2`: watching places east of it, facing west.
- `annex_door`: the annex's door from the yard.

## v5 additions — approved 29 September 2026

Qualified IDs below are exact JSON IDs. Coordinates are (x,z) metres in the stated scene; north is -z. These append to the original marker text above. The two existing interior portal mappings remain unchanged.

## Civic Terrace (Alliance appointment)

- `civic_terrace/leaders_1`: shallow leadership arc; city (-3.6, -65.6), ground y=2 m, facing south.
- `civic_terrace/leaders_2`: shallow leadership arc; city (-1.8, -66), ground y=2 m, facing south.
- `civic_terrace/leaders_3`: shallow leadership arc; city (0, -66.2), ground y=2 m, facing south.
- `civic_terrace/leaders_4`: shallow leadership arc; city (1.8, -66), ground y=2 m, facing south.
- `civic_terrace/leaders_5`: shallow leadership arc; city (3.6, -65.6), ground y=2 m, facing south.
- `civic_terrace/commander`: faces the leadership arc; city (0, -63.8), ground y=2 m, facing north.
- `civic_terrace/officers_1`: behind the Commander; city (-3.6, -61.8), ground y=2 m, facing north.
- `civic_terrace/officers_2`: behind the Commander; city (-1.8, -61.8), ground y=2 m, facing north.
- `civic_terrace/officers_3`: behind the Commander; city (0, -61.8), ground y=2 m, facing north.
- `civic_terrace/officers_4`: behind the Commander; city (1.8, -61.8), ground y=2 m, facing north.
- `civic_terrace/officers_5`: behind the Commander; city (3.6, -61.8), ground y=2 m, facing north.
- `civic_terrace/envoy`: beside the leaders; city (5.4, -65.1), ground y=2 m, facing south.
- `civic_terrace/camera_hint`: suggested nonphysical diorama push-in ground anchor; look toward Commander; city (0, -61.1), ground y=2 m, facing north.

## South Gate (envoy arrival)

- `south_gate/envoy_arrival`: just inside the gate; city (-1.5, 296), ground y=0 m, facing north.

## Guild courtyard (envoy, evening and resting)

- `guild_courtyard/envoy`: courtyard arrival, clear of Elsie's staging; city (-27, 290), ground y=0.6 m, facing west.
- `guild_courtyard/adventurer_evening_1`: adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive; city (-29, 292), ground y=0.6 m.
- `guild_courtyard/adventurer_evening_2`: adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive; city (-25, 292), ground y=0.6 m.
- `guild_courtyard/rest_1`: grass resting patch for resting/injured adventurer; field-sleep sprite permitted; city (-38, 291.5), ground y=0.6 m.
- `guild_courtyard/rest_2`: grass resting patch for resting/injured adventurer; field-sleep sprite permitted; city (-24, 288.5), ground y=0.6 m.

## Guild interior (evening adventurers)

- `guild_interior/adventurer_evening_1`: adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive; guild_interior (-2, 1.5), ground y=0 m.
- `guild_interior/adventurer_evening_2`: adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive; guild_interior (2, 1.5), ground y=0 m.

## Tavern interior (evening adventurers)

- `tavern_interior/adventurer_evening_1`: adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive; tavern_interior (-2.5, -3), ground y=0 m.
- `tavern_interior/adventurer_evening_2`: adventurer evening meeting spot, candidate 18:00 until 21:00 exclusive; tavern_interior (2.5, -3), ground y=0 m.
