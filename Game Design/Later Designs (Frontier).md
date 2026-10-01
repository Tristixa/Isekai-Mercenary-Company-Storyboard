# Later designs (Frontier)

Ideas the owner has asked for, to design fully and **implement after every sprint up to the Frontier is done** (owner, 2026-09-29). Nothing here is in the GDD yet.

## 1. Elsie's session: Ruin Diving (proposal)

**The owner's idea (2026-09-29):** Elsie's working session becomes **Ruin/Dungeon Diving**, available only in the Frontier. It's inspired by *Aliens: Dark Descent*: the player navigates a party through a ruin over long distances, using magic or a device.

### What Aliens: Dark Descent does (research)

- **Real time with a planning pause:** the squad moves as one group in real time. Using an ability slows or pauses time so the player can aim it.
- **Stress:** every fight raises each member's stress. High stress brings debuffs and mistakes, so the game rewards **avoiding** fights rather than seeking them. Pills and rest lower it.
- **The motion tracker:** it shows unseen threats as dots, and the best move is often to steer around them.
- **Scarce resources and safe rooms:** ammunition, health and toolkits are limited. The squad rests and saves by sealing itself in a room, which costs toolkits.
- **Missions** last about 20–60 minutes.

Sources: [Wikipedia](https://en.wikipedia.org/wiki/Aliens:_Dark_Descent), [Shacknews review](https://www.shacknews.com/article/136009/aliens-dark-descent-review), [Steam discussion on stress](https://steamcommunity.com/app/1150440/discussions/0/3810657811753885196/), [Steam discussion on real time with pause](https://steamcommunity.com/app/1150440/discussions/0/3807278817576015978/).

### How it could translate to FGC

- **A top-down ruin map** with rooms and corridors, explored in real time. The Commander guides the party; the clock is paused as in every session (GDD 5a.2).
- **A "resonance compass"** (Liliana's device, or Elsie's magic) plays the motion tracker's role: it shows threats nearby but not exactly what they are.
- **Strain** plays stress's role. Fights and traps raise it; resting in a sealed chamber lowers it and spends supplies. It gives the same push toward careful routing that Expedition Planning rewards today.
- **Rewards:** relics and rare materials, and **verified ruin maps**, which feed Liliana's verification work and the Guild's Frontier standing.
- **Length:** one session, shorter than Dark Descent (for example, 10–20 minutes).

### Combat research: how Dark Descent fights (2026-09-29)

**What happens when enemies appear:**
- **The squad is one unit.** The player moves four marines as a group. The game picks who leads, heals or welds, and **each marine fires automatically** at anything in their sightline. Nobody aims unless the player spends an ability. Running stops them shooting.
- **Command Points (CP) are the player's real input.** The squad shares a pool of 3 (it grows with upgrades), and each ability costs 1 CP. Opening the ability wheel slows time, or pauses it if that's set in the options.
  - **Universal abilities:** Flare (light, +10 accuracy), Suppressive Fire (a cone where the marine's fire rate doubles and aliens move at 70% speed, but the marine can't run), the Deployable Motion Tracker.
  - **Weapon abilities:** Shotgun Blast, the U1 grenade, the Sentry Gun (250 rounds, fires on its own in a cone).
  - CP comes back through rest, waiting, or class skills.
- **Positioning matters more than aiming:** the player fights from a corridor, drops a sentry on the likely approach, welds a door behind them, or simply leaves.
- **The hive's alert level:** gunfire and noise alert the hive, which sends hunts. The longer the squad stays hunted, the more aggressive the hive becomes: bigger patrols, elite enemies, then an onslaught that routinely wipes the squad. The motion tracker (60 m, all around the squad, moving dots only) lets the player avoid fights, and an overloaded tracker lures enemies away for 30 s.
- **Stress is the long-term cost:** every fight raises it. High stress means missed shots, fumbled reloads and double ammo use ("Berserk"), fewer CP, and lasting traumas. Welding into a shelter and resting lowers it.

**What critics disliked:**
- The squad-as-one-unit control is imprecise: marines lag around corners, and the player can't place individuals around a room.
- Enemy spawning and pathing make back-to-back hunts feel unfair.
- Some reviewers read stress as just a difficulty modifier.

Sources: [GameSpew, pausing](https://www.gamespew.com/2023/06/how-to-pause-combat-in-aliens-dark-descent/), [DualShockers, command skills](https://www.dualshockers.com/aliens-dark-descent-command-skills/), [Gamepressure, motion tracker](https://www.gamepressure.com/aliens-dark-descent/how-the-motion-tracker-works/z010cd8), [Game Rant, squad orders](https://gamerant.com/aliens-dark-descent-how-to-issue-squad-skills-marine-orders/), [GameSpot review](https://www.gamespot.com/reviews/aliens-dark-descent-review-theyre-in-the-walls/1900-6418085/), [Shacknews review](https://www.shacknews.com/article/136009/aliens-dark-descent-review), [GodisaGeek review](https://godisageek.com/reviews/aliens-dark-descent-review/), [Steam, auto-fire](https://steamcommunity.com/app/1150440/discussions/0/3807278624252019283/).

> **Owner choice (2026-09-29): option B, "fight where you stand".** It stays a proposal in this file and is **not** part of the GDD until the Frontier design.

### Can FGC do this? Yes, because Dark Descent is already an auto-battle

Dark Descent's fights **are** an auto-battle: marines choose targets and shoot on their own, and the player adds position plus a few paid abilities. FGC's combat engine already does the auto part. Each fighter fills an action meter at their rate, auto-targets by reach and row, and uses their signature skill when the meter is full. What Ruin Diving adds is **where** the party stands and **when** the Commander spends an order.

**Three ways to build it (from most to least ambitious):**

| Option | How a fight plays | Reuses | New work | Art cost |
|---|---|---|---|---|
| **A. Full real-time tactics** (true Dark Descent) | Combat happens on the ruin map itself. Enemies path, flank and use sightlines and cover; fighters fire by line of sight | Stats only | A new spatial combat engine, enemy AI, pathfinding, sightlines | High: every fighter needs walk cycles in 4 directions plus attack and hit animations, and every monster needs them too |
| **B. Hybrid: fight where you stand** (recommended) | Exploring is real time on the map. On contact, time slows and the party **locks into formation where it stands**; enemies enter from the direction they came. The existing engine runs the fight in real time, while the Commander spends Orders and can order a retreat | The whole combat engine, formations, skills, consumables | The facing and row rule (whoever faces the threat is the front row), Orders, the retreat rule, the map, the compass, Strain | Moderate: party walk cycles (4 directions); the battle stills we already have work in the fight |
| **C. Node map** (Darkest Dungeon style) | The player picks rooms on a map; fights are ordinary auto-battles | Everything | Just the map and the choices | Low, but it loses the real-time feel the owner wants |

**Option B in more detail:**
- **Moving:** the party moves as one group (like Dark Descent), shown as a small formation. Clicking a point walks it there.
- **Contact:** when a threat's dot reaches the party, the fight starts in place. **The direction matters:** a threat from the side or the rear puts back-row fighters in front for that fight, so a flanked mage takes the hits. This carries Dark Descent's "position matters" idea without per-fighter micromanagement, and it avoids the imprecise control critics disliked.
- **Commander Orders (the CP):** the party shares **3 Orders** per dive, and each costs 1. Using one slows time. The Orders come from the "delve profile" (question 1a): Vanguard **Hold the Door** (a doorway fight admits one enemy at a time), Ranger **Scout Ahead** (identifies the dots in range), Warden **Overwatch** (fires first at the next enemy to enter), Breaker **Breach** (opens a shortcut but raises alert), mage **Ward Light** (the flare equivalent: +accuracy, reveals). Orders come back only at a sealed chamber.
- **Alert (the hive):** fights and noisy Orders raise the ruin's alert. Higher alert means more wandering groups, then an elite. The pull toward careful routing is the same as in Dark Descent.
- **Strain (stress):** it builds per fight. At high Strain a fighter's meter fills more slowly, and at maximum they refuse Orders. **It resets after the dive**; FGC already has Fatigue and Morale as long-term costs, so Strain doesn't add lasting traumas.
- **Leaving:** "Fall back" disengages at the cost of Strain and leaves the fight's loot behind. The dive ends at an exit or when the party falls.
- **Determinism:** the dive runs on a private copy of the Guild state with its own seeded stream. Each Order is a command stamped with its moment, so a dive can be replayed and tested exactly like the rest of the simulation.

**The main risks:**
1. **Art is the biggest cost.** The ruin needs walking parties, and walk cycles are where our sprite pipeline is least reliable (only idle and the first walk frame are dependable). Option B keeps the fights on stills; option A doesn't.
2. **Balance across two modes:** the same adventurers fight in idle hunts and in dives. Orders and Strain must exist only in dives so hunt balance isn't disturbed.
3. **Session length:** Dark Descent missions last 20–60 minutes. FGC should aim for 10–20, around 6–10 rooms and 3–5 fights.

### Open questions for the owner

1. **Who dives?** The adventurers' skills are built for the idle battle (meters, auto-targeting), not for real-time command. Two options:
   - **(a) The same adventurers, with a "delve profile":** each gets one or two dive abilities from their role. For example: Vanguard holds a doorway, Ranger scouts ahead and reveals, Warden keeps overwatch, Breaker breaks walls, the mage lights and wards. No new characters, and it deepens the existing cast.
   - **(b) A new "Explorator" roster:** specialists made for diving. That means new characters, art and hiring, and a clean separation from the battle roster.

   Leaning (a): it reuses the cast the player already cares about.
2. **Leadership in Eurydica:** Leadership grows only through Elsie's session (GDD 5a.2), and today that's Expedition Planning, which also runs in Eurydica. If Elsie's session becomes Frontier-only, Leadership can't grow before Chapter 3. Options: keep Expedition Planning in Eurydica and add Ruin Diving in the Frontier (Elsie then has two sessions), or accept that Leadership starts growing in the Frontier.
3. **Is it a session or an operation?** A Commander session (paused clock, one per day, grades D–S) keeps it within the existing minigame system. A ruin expedition (the party is away, the clock runs) would make it a new operation type.
