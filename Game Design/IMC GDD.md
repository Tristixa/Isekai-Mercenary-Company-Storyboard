# Frontier Guild Chronicle: Game Design Document

**Version:** 2.1 (HD-2D), 2026-09-27. It was called Isekai Mercenary Company until 2026-09-27; "IMC" stays in file names. Version 2.0 is archived as `IMC GDD v2.0 (archived).md`.
**Status:** the single source of truth for game design. It replaces the old 2D GDD (`D:\Godot Projects\IMC-godot\IMC_Reworked_GDD_HUD_Aligned_v1.1.md`) and its balance sheet (`data/BALANCE.md`) for every topic it covers. The decisions behind v2.1 are in `GDD v2.1 Proposals.md`, and the audit behind them is `GDD Audit 2026-09-27 (Codex).md`.
**Terminology:** the organisation is the **Guild** in all player-facing text (Guild Rank, Guild purse and so on). The player's title is **Commander**. Internal IDs keep their old names.

## How this document works

- The old GDD and balance sheet were the starting material. Wherever a proof or a decision by the owner changed something, this document wins, and the change is marked **Changed from v1.1** with the reason.
- Each section has a status:
  - **Proven**: built and checked in a playable proof (link given).
  - **Carried over**: taken from v1.1 and still believed right, but not yet proven in HD-2D.
  - **Designed, not yet proven**: decided on paper; built and balanced in a later proof. Section 17 holds only content still to author, never an open design question.
- After every proof, this document is updated in the same pass, so it never falls behind again.
- Numbers live in tables so tuning is a one-line edit. Every number here is a starting value to tune, not a promise.

### Proofs so far

| Proof | What it proves | Link |
|---|---|---|
| 1. Officer sprites | HD-2D courtyard with all officers walking, sprite pipeline | https://claude.ai/artifact/URLz2pzEhY3dNDmczE33a4 |
| 2. Idle battle | Octopath-style auto-battle, Tristitia's full set, impact feel, party HUD | https://claude.ai/artifact/SiASbqjmHgr78oDRkHKjb5 |
| HUD and operations | Top HUD, expeditions, scouting, hunting, groups, rare targets, field view, closeout | https://claude.ai/artifact/7Zs4BDj59ZY9scaJUPMRDr |
| 4. Explorable Eurydica | Grey-box slice played as Chapter 1 Scene 3: follow camera with cutaway, walking and collision, manuscript dialogue with choices, requests noted, merchant buys at 50%, 14:00 return | https://claude.ai/artifact/N7VYKQzNWXJWwfDhYrUtRb |

**Proof 4 (agreed and built 2026-09-27):**
- **Scope:** the first playable slice, played as Chapter 1 Scene 3. It covers South Gate and Arrival Ward (stables, Jeb), Guild Edge, then called Company Edge (HQ exterior and yard) and the southern Market Spine (tavern, red-tree plaza, Repair & Supply with Gerd, the travelling merchant), with a view toward the Old Bridge. The objective is "return to Tristitia by 14:00". Service Lanes (Dr. Emmerich, Hilde) is visible but closed.
- **Camera:** Octopath-style town camera. Perspective, about 35–40° down, following the Commander, no rotation, tilt-shift depth of field.
- **Buildings:** simple 3D volumes wearing painted facade and roof textures, made per building by Codex from the approved concepts. Codex uses the `$imc-environment-art-direction` skill (`D:/Godot Projects/IMC-Companion-Skill-Environment`), the same one that made Hylaea. The proof starts with plain blocks in the district roof colours to settle camera, scale, walking, collisions, talking and the market.
- **Story fixes:** the Hylaea road leaves by the South Gate; the HQ grows (5.1); the story bible's "guild presence" line is dropped.
- **Results:**
  - **Camera:** 40° down at about 28 m, FOV 30. At that distance a 1.68 m sprite is about 93 px on a 1280×800 view, close to its native pixel size.
  - **Cutaway:** buildings between the camera and the Commander (or nearby people) fade to 22%, Octopath-style. This is needed because the camera faces north and the south wall and gate sit between it and the player.
  - **Walking and time:** walking speed is 3.2 m/s. The day clock runs at 120 company seconds per real second and stops in dialogue and the shop.
  - **Dialogue:** lines are verbatim from the manuscript, extracted by Codex with nested choices. A request is noted only on the offer branch (Jeb: Winter Bedding; Gerd: Keep the Old Ones Working; the merchant: Rare Slime Order). `<name>` and `<Guild-name>` are shown as "Commander" and "the Company" until those names are decided.
  - **Placeholders:** townspeople without sprites use grey stand-ins with a "?" portrait card.
  - **Deferred:** evening and night NPCs (the Lady in a Red Dress, the Lady in a Green Dress and others) wait for a time-of-day pass.
- **Painted facades (version 2):** Codex painted orthographic elevation textures at 64 px/m for 11 buildings (44 faces), using the approved Eurydica concepts for design and its tavern sheet as the style anchor. It also painted 4 roof tiles, the city wall, awnings and 12 props. They are UV-mapped onto the 3D volumes under curved, flared roofs, and lighting comes from the engine. The textures and props are candidates awaiting the owner's review.
- **Camera decided (2026-09-27):** straight north. The facades were approved and moved to `Environment Assets/Eurydica/Approved Facades v1/`. The workflow is now part of `$imc-environment-art-direction` (`references/hd2d-buildings.md`).
- **Stopped here by the owner (2026-09-27):** the remaining town work (sprites for Jeb, Gerd and the merchant, the stall) waits for the Godot build.

The proof sources, build tools and check scripts live in `HD-2D Proof/` (`src/`, `tools/`, `GATES-*.md`).

---

## 1. Vision

**Frontier Guild Chronicle** (FGC) is a fantasy guild-management RPG. It was called Isekai Mercenary Company until 2026-09-27, and "IMC" stays in file and folder names.

- **The Commander:** a young man from Earth who wakes near Eurydica. The city has no adventurer's guild, so he founds one, and later leads it into the unknown Frontier. He doesn't fight.
- **Building the Guild:** he hires and prepares adventurers, sends expeditions, processes monster corpses, trades, pays wages and grows the HQ.
- **A life beside it:** hands-on work with his officers, meals, the city at night and, in the Frontier, romance.

**Core fantasy:** run a living guild where information, logistics, preparation, timing and people matter as much as combat.

**Campaign:** Eurydica (Chapters 1–2) is the short opening act. The **Frontier** (Chapter 3 onward) is the main body of the game (16a). Eurydica teaches the routine; the Frontier holds most of the progression, the cast and the romance.

**Pillars**
- **Management first.** The player decides; combat resolves itself. The Commander never fights.
- **Adventurers matter.** They are persistent people with stamina, condition, gear and risk.
- **Character appeal is core.** Officers, adventurers and NPCs must be memorable enough to have favourites (adult-coded, distinct silhouettes, consistent across portrait and sprite).
- **Information creates profit.** Scouting, forecasts, rumours and verified records create an edge. In the Frontier, verified knowledge becomes what the Guild is known for.
- **Parallel simulation.** Many operations run while Guild time moves.
- **Beautiful HD-2D.** Premium, alive and readable, never a rough mockup.
- **Watchable operations.** Every expedition can be watched as it happens, but watching never changes the outcome.
- **"Tomorrow I want to ___"** *(new)*. Every day the player can see concrete prizes (gear, hunting grounds, repeat customers, rooms, recruits) and chooses which to pursue. There is no prescribed chain (3, 11, 12).
- **A life beside the Guild** *(new)*. The Commander grows through hands-on work with the officers (5a). He has meals, evenings and relationships (5.4, 5b), and none of it is a chore.

---

## 2. Visual direction (HD-2D) - Proven (proofs 1 and 2)

**Changed from v1.1:** the game moved from 2D, briefly through 3D, to HD-2D in the style of Octopath Traveler (decided 2026-09-25). All 3D and Blender work is retired.

### 2.1 Look
- Pixel-art sprites standing in a lit 3D scene: real lights and shadows, depth of field with tilt-shift, bloom, and a warm colour grade.
- Warm late-afternoon light from the upper left is the default for Hylaea.
- Locations are layered like Octopath: a 3D floor, near props, and parallax background layers.

### 2.2 Sprites
- **Source:** Gemini sprite sheets, snapped to their true pixel grid and cleaned by hand. Kept at Gemini's native density: about 91–96 art pixels for a 168 cm adult (1 px ≈ 1.8 cm), in 64-pixel-wide cells.
- **No mouths** on sprites. Expression lives in the portraits.
- **Directions:** four (down, up, left, right). The right-facing walk is the mirrored left walk. **Changed from v1.1**, which recommended eight directions; four reads well at this size and halves production.
- **Walk and idle** for every character who moves in the world.
- **Battle sets** only for characters who fight on screen (see 9.4). They are made from Omniflash videos on a key colour and extracted by the pipeline. The key colour is chosen per character to be far from their palette (green for Tristitia, magenta for Elsie). Download at the 1080p upscale option.
- **Monsters** get **one still image per pose**, with no animation videos (owner, 2026-09-28). The engine adds the motion (breathing, wind-up, lunge, flinch, dissolve), as Octopath does.
  - **Ordinary and rare:** Idle, Attack, Skill, Hurt, Defeat (every monster has one skill, 9.3b).
  - **Boss and flashpoint:** Idle, Attack, Skill, Hurt, Second Hurt, Defeat.
  - The roster and prompts are in `Production Assets Requirement/Eurydica Monsters.md`. Regional and rare variants can be palette recolours of a base sprite.
- The full sheet and video workflow is in `Character Sprites/Gemini Sprite Prompts.md`, `Gemini Battle Batch Prompts.md`, `Gemini Monster Prompts.md` and `Animation Sources.md`.

### 2.3 Portraits
- Portraits follow the locked portrait style, with seven expressions per officer (Happy, Serious, Sad, Anger, Fear, Surprise, Laugh) in `Characters/Portrait Expressions/`.
- Officers present their department's screens with a large portrait and a dialogue box.

### 2.4 Environment art
- Battle and field backgrounds are built from Higgsfield images (`Environment Assets/Higgsfield Battleground Prompts.md`): a far panorama, a mid tree line, a ground tile, a prop sheet and a canopy.
- **New:** the panorama, tree line and canopy must **loop horizontally**, because the field view scrolls them while parties walk (section 8.3).
- **Method that works (2026-09-27):** the owner generated Hylaea with Codex from an MD brief. Source art is painted first, then cut into objects (the 8×8 snap from that first pass is superseded by the painted decision below). The approved set is `Environment Assets/Hylaea/Approved Calibration v1/`. The briefs for Bernmoor and Erythra are in `Environment Assets/Region Prompts - Bernmoor and Erythra Highlands.md`.
- **In the scene (proven in the operations proof):**
  - **Layers:** the far strip stands 26 m back and the mid strip 13 m back, each sized to the band the camera sees above the horizon. The mid strip is planted by its lowest tree base.
  - **Objects:** trees, props and the canopy are lit cutouts anchored at their base. The ground tile covers 6.3 m. Everything scrolls in world units, so perspective gives the parallax.
  - **Layout:** the fighting band stays empty; only small grass sits in front of it, and large pieces stay behind or at the far sides. The layout repeats every 48 m.
- **Pixel density:** the environment art has coarser pixels than the characters. At the characters' density a tall tree would be only as tall as a person. Each group is therefore scaled to a believable real size: trees about 0.105 m per art pixel, props 0.036, grass and flowers 0.03. Depth of field softens the difference at distance. Near the camera the coarse pixels turn into large blocks. The region briefs (revision 2) therefore target art-pixel counts by real size (for example a large tree at 400–550 art pixels).
- **Style decided (2026-09-27): painted.** Environments use the painted, Unicorn Overlord-like source art at full resolution, not 8×8 pixel art. Characters stay pixel sprites. The operations proof defaults to painted; its pixel switch remains only for comparison.
- **Density (owner direction, 2026-09-27):** less negative space, as in `Environment Assets/Hylaea/Codex Concept.png`. There is a tree line in front of the mid strip and more trees and props around the clearing. Big near trunks frame the screen edges. They are the closest layer, so they sweep past fastest while walking; when a fight starts they glide to the edges so they never stop in front of the fighters and a near foreground band of ferns, bushes and logs sits just behind the party HUD, softened by depth of field. Only the fighting floor stays open. The briefs add two sheets per region for this: `Foreground.png` and `Near Trunks.png`.

- **Style changed (owner, 2026-10-01): pixel art, Proof 1's look.** This supersedes the painted decision above for towns and battle backgrounds. Environments are crisp pixel art at **25 art pixels per metre** (4 cm), close to the characters' density, shown with nearest filtering and lit by the scene, with a close, low camera, depth blur and a wide bloom (FGC_07 §10). Buildings, roofs and ground are drawn in code; trees, landmarks and props are generated pixel art made from references (`Environment Assets/Eurydica/Approved Pixel v1`). Battle backgrounds: the near and middle objects are redone as pixel art (`Environment Assets/Hylaea/Approved Pixel v1`); far panoramas and skies keep the approved painted art, softened by depth blur.

### 2.5 UI palette (from the v1.1 VDD)

| Token | Hex | Use |
|---|---|---|
| Navy 950 / 900 / 800 / 700 | #07131F / #0B1D2D / #102B45 / #163B5D | Panels, top bar |
| Gold 500 / 400 | #C99435 / #E0B04A | Frames, headings |
| Blue select / glow | #146EC8 / #37A1FF | Active speed, primary buttons |
| Parchment 100 / 200 / 300 | #F1E2BC / #E6CFA0 / #D2B77D | Maps, discovery pop-ups |
| Ink | #2A2117 | Text on parchment |
| Success / Warning / Danger / Critical | #43A65E / #D79A2B / #C9433A / #9F1F22 | Status, alerts |
| Info / Rare / Disabled | #3C8CCB / #8B5CC7 / #6E6C68 | Info, rare finds, locked items |

- **Fonts** *(changed 2026-09-28, owner, after the UI style tests)*: **Cormorant Garamond SemiBold** for headings, **Alegreya** (the serif) for text and **all numbers** with lining figures, Pixelify Sans for in-battle names. Card header titles are set in **all caps**. (Previously Marcellus and Alegreya Sans.) **Changed:** Pixelify digits misread (an 8 looks like an S), so numbers never use it.
- **Numbers use lining figures.** Old-style figures made "0" read as "o".


### 2.6 Dialogue staging *(new; approved by the owner 2026-09-28; not yet proven)*

HD-2D staging inside the diorama, as in Octopath Traveler II. Not Steambot-style eye-level cuts: our characters are flat, mouthless pixel sprites. Not a zoomed-out view either.

- **Everyday talks:**
  - The camera keeps the straight-north heading and eases in, closer and lower (about 28–30° down), to frame the speakers.
  - The sprites turn to face each other and play small emotes.
  - The portrait dialogue view carries the facial expression.
- **Key story beats only:** authored shots such as letterboxing, a slow pan, a push-in, or a modest turned angle.
- **Writing scenes:** the manuscript uses `Game Design/Scene Script Format.md`: speaker expressions, a fixed cue vocabulary (camera, shake, emote, pose, move), choice tags and flags, readable by the engine.

---

## 3. Core loop — Proven (operations); Designed, not yet proven (economy and pacing)

1. Review the Guild purse, payroll reserve, roster and three pinned projects at HQ.
2. Prepare hunts, scouts or contracts; assign a rest day to people who need full stamina.
3. Let Guild time run while expeditions, processing, crafting and construction proceed. Watch any expedition without changing its outcome.
4. Receive secured corpses, discoveries, experience and request progress.
5. Process materials; choose between customers, gear, expansion and sales. Forecasts help choose when to sell.
6. At 20:00, finish due events, close operations, show Resolution, then Day Summary. Settle payroll on its weekly dates.
7. Advance the night to 07:00. Start the next operating day paused.

**Visible projects.** Show recipe cards before the Workshop opens, material sources on known hunting grounds, Hilde and Gerd's repeat orders after their first deliveries, and Guild House Tier 2 once the first Guild meeting sets it. The player can pin up to three projects; the Day Summary shows progress, remaining goods/gold, source and next action. Suggest one nearly done, one being funded and one beyond current reach; never replace the player's pins automatically.

**Pacing examples are goals for a proof, not day-locked promises.**

| Checkpoint | Intended choice and lasting prize | Stamina and progression check |
|---|---|---|
| Day 3 | Finish slime orders or scout toward boars; preview the Vest and Bow | One dispatch per day can be sustained by overnight sleep. Starting at 4, two dispatches leave 2, sleep gives 3; another two leave 1 and the second is fatigued. A rest day restores 4 at 20:00. |
| Day 10 | Turn boars into Hilde/Gerd deliveries, first gear or beds; pursue wolves for Jeb | With four hires, stagger rest and use a three-person hunt plus one scout. A 100-XP hunt takes 14 successful hunts to fund one level-5 track; calendar timing depends on outcomes and scouting. |
| Day 25 | Aim at the charter and Frontier readiness, or already be in the Frontier; retain useful Eurydica customers while preparing | Eurydica targets a strongest track around level 5–6, Rank C and initial Boarhide/Reed/Ridge gear. It must not require maxing every track or waiting until a fixed day. Night sleep and optional rest days govern readiness throughout. |

**Frontier scaling:** Chapter 3 onward is the main game: larger roster and facilities, higher tracks, gear and Guild ranks, using the same material-to-project loop.

## 4. Time — Proven (clock); Designed, not yet proven (revised day and event contract)

| Rule | Value |
|---|---|
| Operating day | 07:00–20:00; 13 game hours |
| Clock speed at 1× | 1 real second = 120 Guild seconds; 1 game hour = 30 real seconds |
| Unwatched operating day at 1× | 390 real seconds |
| Controls | Pause / 1× / 2× / 4× |
| Simulation tick | 12 Guild seconds; elapsed event durations round up to whole ticks |
| Watched battle pace | ¼ of selected speed; optional setting; global clock slows, not just that fight |
| Entire operating day at battle pace 1× | 1,560 real seconds; a timing bound, not a typical day |
| Market buyer checks | Whole hours 08:00 through 20:00 inclusive: 13 checks per category |
| Night accounting | 20:00→07:00, 11 calendar hours |
| New day | Starts paused at 07:00 |

One authoritative clock drives all operations. Each operation has a saved, stable random stream. Watching, hit-stop, camera movement and rendering never consume gameplay randomness or change game-time action lengths. World walking runs time; dialogue, shops and management pause it and restore the previous chosen speed when closed. Watch preserves Pause if already paused, otherwise uses the battle-pace setting. Use one foreground modal, not stacked pause toggles.

### 4.1 The 20:00 cutoff — Designed, not yet proven

At each tick, resolve completed combat actions first; then due timed events; then cutoff. Within timed events use this stable order: scout intervals and completed production/construction; operation duration/return; market buyers; request/debt deadlines; queued story flags. Stable operation ID breaks ties. A completed contract kill at the deadline or cutoff succeeds before expiry. A completed scout interval earns its rewards before that interval's injury check. A processing job finishing at 20:00 supplies the final buyer check.

At 20:00, no new dispatch, search, combat action or production job starts. Hunts/scouts return with secured results; unfinished accepted contract attempts fail. Cancel in-flight actions without damage; completed kills remain secured. Abort unfinished processing, crafting and Reworking and return their inputs and fees. Retain queue recipes and corpse identities, without overnight work; resuming tomorrow starts the unfinished job from zero. Listings persist. Construction, injury, request and debt timers continue through the night; buyers and production do not.

Resolution lists party, target, start/finish, rewards and status: completed, returned, returned at 20:00, returned (recalled), returned (injured), or failed. Explain secured yields, path/den effects, injury cause, consumed potions and XP, alongside the original prep estimate. It also lists continuing injuries, construction, listings and unused rare sightings. Apply rest-day recovery and daily accounting, then show Day Summary; weekly payroll is an explicit step in that closeout. If dialogue is open, freeze at the cutoff and show closeout after its safe end. Never simulate operations beyond it.

Process the 11-hour night in chronological timer order, including injury expiry and request/debt deadlines. Credit sleep once at the new-day boundary. Personal evening presentation must not advance any part of those same 11 hours twice. The Commander's own evening and sleep are in 4.2.

**Frontier scaling:** retain this clock and closeout contract. The relocation's 48-hour transfer is calendar time with suspended local operations (16a), not extra operating days.

### 4.2 Night and sleep *(new; designed, not yet proven)*

- **After the 20:00 Day Summary:** operations are closed. Adventurers go to bed (+1 stamina overnight, 6.3), and officers follow their evening routines.
- **The Commander's free time:** talks, meals, the night city, the reports at his desk, and dates in the Frontier (5a.3).
- **The day ends only when he sleeps in his bed after 20:00.** At 01:00 he falls asleep automatically. No penalty either way.
- **The night jump** from sleep to 07:00 follows 4.1's 11-hour accounting. Time he spends awake at night is part of those 11 hours, never counted twice.

### 4.3 The city bell *(new, owner 2026-09-28; designed, not yet proven)*

- **Eurydica's clock tower** stands at the centre of the Civic Terrace, the landmark of the north bank. It rings at **09:00, 12:00, 15:00 and 18:00**: a peal that repeats for a while (about 8–10 seconds).
- **Where it's heard:** only outdoors in Eurydica, not in interiors or the field view. It's louder on the north bank and softer near the South Gate.
- **It's a runtime sound cue, keyed to the Guild clock.** It never pauses the clock and changes no rules. It gives the day an audible rhythm; the Intelligent Girl's line about the bell sounding different by the bridge hints at it.
- **Frontier scaling:** each Frontier base can have its own time sound (a camp bell, a horn), or none.

---

## 5. Guild, HQ and officers - Carried over (Adventurer Office proven)

### 5.1 HQ
- **The HQ grows with the story** (decided 2026-09-27; Eurydica rooms per Scene 6, owner 2026-10-01). Chapter 1 uses the small Tier 1 Guild house on **Guild Edge**, beside the South Gate:
  - **Tier 1:** a main room with the big meeting table (Tristitia's working place) and **Mae's processing corner**; the Commander's room, which is also his office; **one shared officers' room** (Tristitia, Mae and Elsie); a small courtyard where **Elsie** works from her bench; and a **dormitory for 4 staff** from the start.
  - **Tier 2** (objective C1S6-1, set at the first Guild meeting in Scene 6): an annex on the reserved plot beside the Guild yard with a **second officers' room** (Fulker, Valerie, Liliana), **one Workshop for processing and crafting** with four tables (Mae, Fulker, one processing staff, one craftsman; Mae moves here) and **one Commerce + Information room** (Valerie and Liliana). It unlocks the dormitory expansion to 8.
  - **"Staff"** means recruitables (adventurers and workers); they all sleep in the dormitory. **Officers** are Tristitia, Mae and the other chiefs. The player never sees the dormitory interior.
  - Design: `Locations/Eurydica/Interiors/Guild House Interiors.md`. The courtyard has no training targets.
- **Separate department rooms per officer, and the HQ kitchen, are Frontier content.** In Eurydica the officers share the rooms above; the Commander still walks to each officer's spot.
- Proof 4 proved walking through Eurydica (grey-box); the HQ interior follows the same method.

### 5.2 Officers

| Officer | Department | Role in play | Fights? |
|---|---|---|---|
| Tristitia | Commander's Office | Briefings, requests admin, Day Summary, payroll, flashpoints | Yes, in crises. Full battle set done. |
| Elsie | Adventurer Office | Roster, rest, backpack, expedition setup and monitoring | Rarely. Longsword and martial arts (9.6); battle stance, attack and skill made, batch 2 pending. |
| Steady Mae | Processing Room | Corpse storage, processing | No |
| Fulker | Workshop | Crafting, Reworking | No |
| Liliana | Information Office | Forecasts, rumours | No |
| Valerie | Commerce / Trading Post | Market, listings, potion counter | No. Always wears glasses. |

- **Full names** (nameplates in brackets): Tristitia Fidei (Tristitia), Elsie Rodger (Elsie), Mae Tanner (Mae, "Steady Mae"), Sigrid Fulker (**Fulker**, since she prefers her surname), Liliana Kessel (Liliana), Valerie Kaufmann (Valerie). See `Naming Guide.md`.
- Officers join through the story, never through the recruitment pool. Valerie, Fulker and Liliana all join during Chapter 1 (14). Never invent a filler officer.
- **Officers fight only at big story moments**, so their battles must look strong (section 9.4).

### 5.3 Guild stats (top bar)
Day, time, Gold, Reputation, Morale, Guild Rank. A new Guild starts at 07:00 with 2,500G, 0 Reputation, 60 Morale and Rank F.


### 5.4 Officer bonds and perks *(new; designed, not yet proven)*

Officers aren't romanceable (owner decision, 2026-09-27; may be revisited if players ask). Each officer has a **bond** from 0 to 5 that grows through time spent with them. It unlocks authored **friendship scenes**, one per level, and a **perk choice** at Bond 5.

**Perk arithmetic (applies to every "faster/slower" and "relative" perk):**
- "X% faster" means duration × (1 − X%), and "X% slower" means duration × (1 + X%). For example, Quick Hands gives a processing duration ×0.75.
- A "relative" change to the Pristine chance multiplies it (Careful Cuts: Pristine × 1.25). The probability added or removed is taken from, or returned to, **Standard**. Damaged and Unsellable chances never change, except through the Commander's Know-how rank-3 **Trained eye** (5a.2), which moves the Unsellable chance to Damaged. It applies after perks and session bonuses, which don't touch those two rows.

**Bond points (starting values, owner may retune):**

| Source | Points |
|---|---|
| Evening talk (once a day per officer) | +1 |
| Shared meal (counts as that day's talk; never both) | +1 |
| Working session with that officer | C +1, B +2, A +2, S +3 (D +0) |
| A dialogue choice tagged `{bond: X +n}` | as written |

**Bond levels** need 5 / 12 / 20 / 30 / 42 cumulative points for Bonds 1–5. The weekly one-level limit and Bond 5's story beat still apply.

**Growth:**
- Bond points come from:
  - working sessions with that officer (the Commander's minigames, 5a.2);
  - one evening talk per day;
  - sharing a meal;
  - dialogue choices they respond to.
- At most one bond level per officer per in-game week.
- Bond 5 also needs that officer's personal story beat, so most perks arrive in the Frontier.
- **In Eurydica, bonds are capped at level 1** (owner, 2026-09-29). Points keep accumulating past 12, but the level stays at 1 until the Guild reaches the Frontier. There the one-level-per-week limit still applies, so banked points never skip levels. Bonds 2–5, their scenes and every perk belong to the Frontier.

**Perk, FNV-style:**
- At **Bond 5** the Commander picks **one of two** perks for that officer, **once and permanently**.
- A perk changes the department's **direction**; it never simply adds power. Each has a clear benefit and a matching cost.

| Officer | Bond 5 perk (pick one, permanent) |
|---|---|
| **Tristitia** (Commander's Office) | **Tight Ship:** weekly payroll −10%; Morale −1 each week. **Open Door:** +1 Morale at each Day Summary with no injuries; weekly payroll +5%. |
| **Elsie** (Adventurer Office) | **Hard Drills:** fight experience +15%; a rest order restores 2 bars instead of full. **Easy Pace:** a rest order also shortens an injury by one day; fight experience −10%. |
| **Steady Mae** (Processing) | **Quick Hands:** processing 25% faster; Pristine chance −25% (relative). **Careful Cuts:** Pristine chance +25% (relative); processing 25% slower. |
| **Fulker** (Workshop) | **Rough Patch:** Reworking jobs (12.8) take half the time, but can only raise material to Standard. **Master's Salvage:** Reworking can turn 3 Damaged units into 1 Pristine in 6 hours. |
| **Liliana** (Information) | **Wide Net:** one extra lead or rumour each morning; forecast accuracy −10 points. **Deep Analysis:** forecast accuracy +10 points and one more day ahead; no morning rumours. |
| **Valerie** (Commerce) | **Volume Trader:** +2 listing slots; listings of 10 or more units sell for +10%; every listing must be at least 10 units. **Premium Seller:** buyers pay +25% for Pristine goods; Damaged goods can't be sold at all (market, trader or negotiation). |

**Perks are visible from the start.** Each officer's profile (opened from their department) shows their bond level, a hint toward the next scene, and **both Bond 5 perks** with a "Bond 5" lock. The player can see what they're working toward and plan around it.

**Perks combine into strategies:**
- *Rough Patch* (fast Reworking to Standard), *Quick Hands* (fast processing) and *Volume Trader* (big stacks) make a **volume** Guild.
- *Master's Salvage* (Damaged into Pristine), *Careful Cuts* (more Pristine) and *Premium Seller* (+25% for Pristine) make a **quality** Guild.

The choices are permanent, so the player commits to one identity per department.

Perk numbers are starting values, balanced in a proof like the rest of the economy.

---

## 5a. The Commander *(new; designed, not yet proven)*

The Commander never fights and never joins an expedition (owner decision, 2026-09-27). His play is running the Guild, his own growth through **hands-on work with the officers**, and an ordinary life around it, in the spirit of Vanilla in Steambot Chronicles.

### 5a.1 Moving and hunger
- He walks at 3.2 m/s and **runs** at 5.6 m/s.
- **Hunger is a status, as in Steambot.**
  - Eating any meal makes him **Fed** for 8 Guild hours.
  - After that he's **Hungry**: he can't run until he eats. There is no other penalty.
- **Meals:**
  - the HQ kitchen is Frontier content (owner, 2026-10-01); in Eurydica the Commander eats at the tavern or food stalls;
  - the tavern costs 8G;
  - food stalls cost 5G;
  - in the Frontier, settlement cookhouses.
- Meals have no fixed hours. Eating with an officer also counts as a bond talk.

### 5a.2 Commander skills and officer working sessions

**Skills:** four skills, each ranked 0–5. They grow from **working sessions**: hands-on minigames with an officer, during operating hours. Each session also teaches the Frontier's practical craft. In Eurydica the sessions use old Frontier reports and local work; in the Frontier they use real Frontier material.

| Skill | Officer and session | What the session produces | Effect per rank | Rank 3 unlock |
|---|---|---|---|---|
| **Leadership** | **Elsie: Expedition Planning.** Plot a party's route across a Frontier-style map grid: terrain costs, rest points, water, threats, within a stamina and time budget. | The next party dispatched today is **Briefed**: it starts each fight with 10 meter | Morale losses −10% | **Word of encouragement:** once a day, cancel one adventurer's Red Fatigue penalty for the next dispatch |
| **Negotiation** | **Valerie: Counter-offer.** Haggle with one buyer over 3–5 rounds; the buyer has a hidden price ceiling and patience that you read from their reactions. | A real sale of one stack from storage at the agreed price, which can beat the market | Request and contract gold +4% (the total is rounded down); market buyers pay +2% | **Standing offer:** once a week, a repeat customer or trader orders a material you hold at +20%, at any base |
| **Insight** | **Liliana: Cross-check.** Compare field reports, sketch maps and witness notes, and mark the discrepancies (distances, landmarks, counts, dates). | A **verified record**. In Eurydica it confirms one rumour or reveals one lead. In the Frontier it builds the verified routes the Guild becomes known for (Guild Verified, from the Frontier chapter that grants that authority). | Scout find chance +2 points; forecast accuracy +2% | **Sharp ear:** one extra lead each morning |
| **Know-how** | **Mae: Cutting Chart** (trace cut lines on a carcass diagram with precision) or **Fulker: Fitting** (fit parts into a frame, a grid assembly puzzle). | Mae: the current processing job's Pristine chance +5 to +15 points by grade. Fulker: the current crafting job takes 10–25% less time by grade. | Processing and crafting time −3% | **Trained eye** *(passive; changed 2026-09-28)*: processing never produces Unsellable. That chance is added to Damaged instead (rank-1 processor: Damaged 20%, Unsellable 0%; rank 2: Damaged 10%, Unsellable 0%). Quality odds are always shown (§12.1) |

**Session rules:**
- A session takes **1 Guild hour**. The clock pauses while you play, and the hour passes when you finish; operations run as normal.
- Once per officer per day, during 07:00–20:00, with an officer who is present and has something to work on.
- **Points by grade:** D (failed) 1, C 2, B 3, A 4, S 5. They also give that officer bond points (5.4).
- A dialogue choice that matches a skill gives +2. The tags follow the bible's intent styles: taking responsibility is Leadership, bargaining Negotiation, asking and observing Insight, hands-on help Know-how.
- Rank costs are cumulative: 10 / 25 / 45 / 70 / 100 points.

**Frontier scaling:**
- Eurydica material can only take a skill to **rank 2**. Ranks 3–5, including every rank-3 unlock, need the Frontier's harder sessions: longer routes, unfamiliar traders, contradictory expedition logs, strange carcasses and parts.
- A session's difficulty rises with the skill's rank.

### 5a.2a The working sessions in detail

**Shared rules:**
- A session lasts 2–4 real minutes; the Guild clock is paused while you play.
- It's played with the mouse, or with a controller stick and buttons.
- Grades run D (failed) / C / B / A / S. Each minigame computes a fair best result for its own puzzle, so S means "near the best possible", never luck.
- The officer comments in the portrait dialogue view before and after. One free hint is available, and taking it caps the grade at A.
- Content comes from authored templates with randomised details, so sessions stay fresh without hand-writing each one.

**Tuning numbers:** the exact tuning of each session is set by its playable prototype in M3 and recorded here then. That covers the negotiation's starting acceptance, tactic changes and tell thresholds, the cut scoring weights and speed band, and the Fitting par. The rules below are fixed.

#### Expedition Planning (Elsie, Leadership)

- **Board:**
  - A map grid of a Frontier-style area: 9×7 tiles in Eurydica, up to 15×11 in the Frontier.
  - It shows a start camp, a goal (a survey point) and terrain with a cost in hours: road 1, grass 2, forest 3, marsh 4, cliff and deep water impassable.
  - There are water sources, possible rest spots, and **threat zones** (monster territory, drawn as a shaded radius).
- **The party** has a **time budget** (12 hours) and **stamina** (10 points). Each tile costs its hours, and each tile inside a threat zone costs 1 stamina.
- **Rest spots:** you may place up to **2**. Each costs 2 hours and restores 3 stamina, but only on a rest spot or beside water.
- **Play:** draw the route tile by tile (undo is free), place the rests, then press **Dispatch**. The party walks it as an animation.
- **Failure:** running out of time or stamina before the goal is **D**.
- **Grading:** against the solver's best route, by hours left + stamina left − threat tiles crossed:
  - S: within 5% of best;
  - A: within 15%;
  - B: within 30%;
  - C: reached the goal.
- **Frontier scaling:**
  - fog: tiles are unknown until a report reveals them, so you plan with partial information;
  - one **mid-route event** (a flood or rockfall closes a tile) that makes you re-plan once from where the party stands;
  - night tiles that cost double.
- **Produces:** the next party dispatched today is **Briefed**. It starts each fight with 10 meter; an S grade gives 15.

#### Counter-offer (Valerie, Negotiation)

- **Setup: the daily negotiation order.**
  - Each morning Valerie posts **one negotiation order**, shown like a request on her counter.
  - A buyer from the roster (`Characters/Negotiation Buyers Roster.md`) wants one item and quantity, **picked at random from what's in storage** (never reserved goods, never more than you hold).
  - The item follows the buyer's taste. For example, the Collector prefers rare and Pristine goods.
  - If storage has nothing sellable that fits, there's no order that day.
  - The order lasts until 20:00. Playing it is the day's session with Valerie.
- **The buyer card:** the buyer's persona, the item's market value, a **hidden ceiling** (80–140% of value, depending on persona and quality) and **patience** (3–5 rounds).
- **The buyers:**
  - Eurydica has one, the Travelling Merchant, with honest tells.
  - The Frontier has four traders from rival merchant factions:
    - Dietrich Vogt of the Frontier Exchange (a gambler who bluffs once and rewards nerve);
    - Reinhold Eisenmann of the Iron Ledger Consortium (a poker face);
    - Lady Isabeau de Chamerolles of House Chamerolles (over-eager warmth that misleads);
    - Captain Josie Harlan of the Meridian Charter Company (barter, slow tells).
- **Each round:**
  1. Set a price on a slider.
  2. Play one **tactic**: *Hold firm*, *Show quality* (only helps with Standard or Pristine goods), *Add a unit* (bundle), *Mention another buyer*, or *Give ground*.
  3. The buyer answers in a portrait line.
- **Reading the buyer:**
  - The tone is the **tell**: warm means you're under the ceiling with room, neutral means close, irritated means over. It is persona-dependent: a quartermaster hides warmth.
  - A tactic that suits the persona raises their acceptance toward the ceiling; a wrong one costs a round of patience.
- **The deal:**
  - A deal happens when your price is at or under what the buyer currently accepts.
  - If patience runs out, the buyer walks: **D**, no sale.
- **Grading:** by final price against the hidden ceiling: S at least 95%, A at least 85%, B at least 70%, C any deal below that.
- **Frontier scaling:**
  - personas whose tells mislead;
  - **barter**: settlements pay in supplies or goods instead of gold, so you weigh what each is worth to the Guild;
  - multi-item bundles.
- **Produces:** a **real sale** of the ordered goods at the agreed price (or the bartered goods), with no listing fee.

#### Cross-check (Liliana, Insight)

In the spirit of *Papers, Please*: spot what doesn't add up across documents. The differences: there's no queue of applicants, facts are linked **across several documents**, you judge **which source to trust**, and the output is a verified record rather than a stamp.


- **Board:**
  - A desk with **2–4 documents** about the same route or event: a field report, a sketch map, a witness note, a ledger entry.
  - Each holds facts: distances, directions, landmarks, counts, dates, times of day. **3–6 of them conflict.**
- **Play:**
  1. Link two conflicting facts across documents to mark a **discrepancy**.
  2. Then **resolve** it by choosing which source to trust, from clues: first-hand or hearsay, the writer's date and position, the weather that day.
  - A false link costs points.
- **Timer:** a soft timer of about 3 minutes, visible as Liliana's candle burning down. Running over lowers the grade by one step; it never fails the session.
- **Grading:** by discrepancies found and resolved correctly, minus false links:
  - S: all found and resolved, no false links;
  - A: all found;
  - B: at least 70% found;
  - C: at least one found;
  - D: none.
- **Frontier scaling:**
  - subtler conflicts: mixed units, a map drawn upside down, day-count errors across months;
  - a **forged document** to expose;
  - records from rival sources.
- **Produces:** a **verified record**.
  - In Eurydica it turns one rumour into an exact lead, or reveals one find in a known area.
  - In the Frontier it builds verified route segments. The Alliance of Nations grants the Guild its verification authority at the Civic Terrace appointment (14, 16a), so from the first Frontier day these are **Guild Verified**, the Guild's recognised product.

#### Cutting Chart (Mae, Know-how)

- **Needs:** a corpse in processing or queued.
- **Board:** Mae unrolls a line drawing of **that species**' carcass, with **3–6 cut lines** (dotted guides) and **no-cut zones** (glands, bladders, stomach) shaded red.
- **Play:** trace each line in one stroke at a steady pace. The score counts **accuracy** (distance from the guide) and **steadiness** (speed kept within a band; too fast tears, too slow drags). Crossing a no-cut zone ruins that cut.
- **Grading:** by the average cut score: S at least 90, A at least 75, B at least 55, C at least 30, below that D.
- **Frontier scaling:** curved and branching cuts, unfamiliar anatomy (Frontier monsters) where the no-cut zones are learned by trial, and cuts done in a set order.
- **Produces:** that job's **Pristine chance +5 / +8 / +11 / +15 points** at C / B / A / S, taken from its Standard share. A D gives no change and never makes the job worse.

#### Fitting (Fulker, Know-how)

- **Needs:** a crafting job in progress or queued.
- **Board:**
  - A **jig frame** on a grid, with fixed pegs.
  - A tray of **parts**: grid shapes with notches, in the same visual language as the backpack.
  - Every cell must be filled, and every peg must sit in a notch.
- **Play:** drag, rotate and drop parts; undo is free but counts as a move. Fulker names one "key part" that must go in first.
- **Grading:** by moves and time against par: S at or under par, A +25%, B +50%, C completed. There is no D: Fulker finishes it for you, for C.
- **Frontier scaling:**
  - bigger frames;
  - **adjacency rules** (the metal part must touch the strap);
  - **unstable materials** that shift one cell after placement.
- **Produces:** that job takes **10 / 15 / 20 / 25% less time** at C / B / A / S.

### 5a.3 The Commander's day and night
- **07:00–20:00, operating hours:**
  - He walks the HQ and the city while Guild time runs, and runs working sessions and errands.
  - Dialogue, shops and sessions pause the clock.
- **20:00:** the cutoff, the Resolution and the Day Summary.
- **After 20:00, night:**
  - Operations are closed.
  - Adventurers go to bed (they can be talked to until 21:00), and officers follow their own routines in their free-time spots.
  - The Commander can talk to them (bond), eat, walk the night city (different people are out), read the day's reports at his desk, or, in the Frontier, meet romance characters.
- **The day ends only when he sleeps in his bed after 20:00.** At 01:00 he falls asleep automatically. No penalty either way.

**Other ordinary activities, none of them grinding:**
- meals;
- evening talks;
- reports at the desk (a recap of trends, and no points);
- city and settlement walks with requests and rumours;
- shopping for gifts;
- dates (5b).

---

## 5b. Romance *(new; designed, not yet proven; Frontier)*

- **Who:** romance belongs to the **Frontier**, the main body of the game. The romanceable characters are Frontier NPCs, **not officers** and not Eurydica residents. The cast will be written with the Frontier (target: 3–4 characters).
- **Bond:** each romance character has a bond of 0–5, with an authored scene at each level. Points come from evening talks and dates (outings to specific Frontier places), gifts they like (a gift they dislike costs points), and dialogue choices.
- **Bond 4:** a scene offers to become more than friends. Declining keeps a friendship with its own closing scene.
- **One romance at a time.** Ending one takes a scene.
- **No stat perks.** The consequences are story: extra scenes, the partner's presence in the Commander's life at the base, and an epilogue.
- **Pacing:** at most one bond level per week; Bond 4 follows that character's personal story beat.
- **Tone:** adult-coded characters and restrained, mature writing, consistent with the bible.

---

## 6. Adventurers - Proven in part (operations proof)

### 6.1 Starting adventurers (sprites not made yet)

| Name | Specialty | HP | ATK | DEF | Rate | Traits | Passive |
|---|---|---|---|---|---|---|---|
| Anselm Voigt | Vanguard | 180 | 18 | 10 | 1.0 | Steadfast, Shield-trained | **Shieldbearer** |
| Nell Larkin | Ranger | 150 | 16 | 8 | 1.0 | Keen-eyed, Trailwise | **Tracker** |
| Severa Kaltenbach | Warden | 175 | 17 | 16 | 1.0 | Disciplined, Watchful | **Big Game Hunter** |
| Otto Grimbald | Breaker | 205 | 18 | 8 | 1.0 | Unshakable, Heavy-handed | **Ironclad** |

Otto is redesigned (owner, 2026-09-28): **full plate armour with a closed helmet and a heavy two-handed warhammer, no shield**. His passive changes from Shieldbearer to **Ironclad**, and his skill keeps its effect under a new name, **Hammerfall**. Severa uses a **greatsword** (decided 2026-09-27): a blade clearly shorter than her body (about chest height when planted), because full-length greatswords caused most of the video failures. Her specialty is renamed Warden (her old catalog id) so it no longer shares a name with the Shieldbearer passive. Reach: Anselm, Severa and Otto are **melee**; Nell is **ranged** (bow). Their looks, personalities and asset lists are in `Characters/Adventurers and Staff Roster.md`. In the operations proof the starters use officer sprites as stand-ins (Anselm = Fulker, Nell = Liliana, Severa = Steady Mae, Otto = Valerie) until their own sheets exist. Chloris is planned as a future adventurer.

### 6.2 Passives *(new)*
Passives are named abilities an adventurer brings to an expedition. They are shown on the roster and the prep screen.

| Passive | Effect | Owner |
|---|---|---|
| Tracker | +10% chance of a group of the hunt target; +10% find chance when scouting | Nell |
| Shieldbearer | +25% DEF while in the front row | Anselm |
| Ironclad | +20% DEF while in the front row, and immune to stun | Otto |
| Big Game Hunter | +20% ATK and +20% attack rate against Elite monsters (rare, variant and boss) | Severa |

The percentages are starting values to tune. Items may later give similar bonuses (lures, maps).

**Monster tiers** *(new)*: every monster is either **Ordinary** or **Elite**.

| Tier | What it is | Examples |
|---|---|---|
| Ordinary | The three regular monsters of each area | Moss Slime, Dire Boar, Forest Wolf |
| Elite: Rare | Found by a scout's sighting; hunted as a special target (8.4) | Mossback Elder, Silvermane |
| Elite: Variant | A stronger version of an ordinary monster that turns up now and then in normal hunts (10.4) | Variant Dire Boar (bigger, recoloured) |
| Elite: Boss | Contract and flashpoint targets | Blackfang Direwolf, Ambermaw Matriarch, Crownstone Wyrm |

Anything that says "Elite" (like Big Game Hunter) applies to all three kinds.

### 6.2a Support adventurers (mages) — Designed, not yet proven

Chloris is the first recruitable mage. Preview her in Chapter 1; recruiting requires Chapter 2, Guild Rank E and a free bed. Mages are ranged; healing, buffs, debuffs and offensive spells are supported action types, but only Chloris's authored kit enters the opening roster. Formation remains three slots per row, five people total: a lone front tank supports at most three back-row allies.

| Chloris | Starting value |
|---|---|
| HP / ATK / DEF / rate | 150 / 14 / 9 / 0.9 |
| Hire / weekly wage | 400G / 120G |
| Basic action | Arcane bolt, normal damage formula, ranged |
| Fixed passive | Measured Casting: mage meter gain ×1.10 |
| Signature | Verdant Blessing: living front-row allies gain +25% ATK and DEF for their next 3 individual actions |
| Empty front row | Bless living back-row allies instead |

No overheal. Blessing modifiers use the same selection limits as every other adventurer.

| Track | Rank 1 at level 5 | Rank 2 at level 8, Frontier only |
|---|---|---|
| Power | Blessing ATK bonus becomes +35% | Blessed recipients deal +15% damage to Elites |
| Toughness | Also heals recipients for 10% max HP | Blessing DEF bonus becomes +40% |
| Speed | Also gives +15% attack rate | Targets every living ally |
| Focus | Lasts 5 recipient actions | Retains 25 meter after casting |

**Frontier scaling:** opens Chloris's rank-2 choices and additional authored support kits; no generic random mage pool.

### 6.2b Signature skills — Proven (base skills); Designed, not yet proven (interaction details)

Each adventurer has one signature, used as their next action once their meter is full. Skills target the front living enemy unless modified. Durations count the affected fighter's completed actions, including stunned lost actions; a newly applied effect never loses duration on its application action.

| Adventurer | Meter role | Signature | Base effect |
|---|---|---|---|
| Severa | Attacker | Diving Splitter | 2.5× normal-hit damage to one enemy |
| Anselm | Defender | Phalanx | +50% DEF for his next 3 actions |
| Nell | Attacker | Frost Arrow | Normal hit; target's attack interval ×1.5 for its next 3 actions |
| Otto | Defender | Hammerfall | Normal hit; target skips its next action |
| Chloris | Mage | Verdant Blessing | Section 6.2a |

**Frontier scaling:** rank-2 modifiers expand these same signatures; they do not add a second skill tree.

### 6.2c Progression: four tracks — Proven (earning); Designed, not yet proven (spending)

Every track starts at level 1 with no bonus. Level n supplies n−1 increments. Adventurer track level, modifier rank, staff rank and Guild Rank are different labels; there is no fifth, separately purchased character level. “Adventurer level 5–6” in the campaign target means the strongest developed track is around that range, not four maxed tracks.

| Track | Increment per level above 1 |
|---|---|
| Power | +4% base ATK |
| Toughness | +5% base max HP; +3% base DEF |
| Speed | +3% attack rate |
| Focus | +5% meter gain for every role |

| Spending rule | Value |
|---|---|
| Destination level n | 100n XP; sequential purchases only |
| Total cost 1→5 / 1→6 / 1→8 / 1→10 | 1,400 / 2,000 / 3,500 / 5,400 XP |
| Eurydica limit | Track level 6; 3,000 lifetime earned XP per adventurer |
| Frontier limit | Track level 10; 12,000 lifetime earned XP per adventurer |
| Selected modifiers | At most 2 rank-1 choices and 1 rank-2 choice |
| Rank-2 prerequisite | Same track's rank-1 choice selected, track level 8 |
| Rebuild at Elsie's | One free per adventurer, then 100G; available at HQ only |

The lower opening cap replaces the audit's unrestricted opening progression so a long Eurydica stay cannot consume Frontier growth. At the current campaign cap, stop new awards; retain existing spendable XP. On Frontier arrival, raise the cap without a free XP grant. A rebuild refunds spent XP to that person's pool, resets purchased track levels and modifier choices, and preserves lifetime earned XP. Commit the complete build atomically after showing stats, interval ticks, milestones and price. Locked Frontier levels remain previewable. All purchased track stats apply whether or not their modifier is selected.

| XP source | Award |
|---|---|
| Hunt/scout deployment | +10 to each member still standing at the first completed fight, or to the scout at its first completed interval; once per operation, never on departure |
| Fight won | +5 per standing member |
| Monster killed | Listed base XP to each member standing at that kill; Ordinary ×1, Variant ×2, Rare ×3, Boss ×5; apply one tier only |
| Scout interval | +4 per completed half-hour to that scout |
| Find | +10 for a newly acquired landmark, path or rare sighting; hints/empty leads give none |

Forced milestone reveals count as actual finds once and credit the scout whose interval crossed the threshold; concurrent scouts process in stable ID order. Injury after an interval does not erase its XP. Downed people retain earlier XP but gain none for subsequent kills while down. A 100-XP hunt is only an illustrative rate: 14 such hunts buy one first milestone, 20 buy level 6; do not promise a milestone on a particular day.

| Adventurer / track | Rank 1 at level 5 | Rank 2 at level 8, Frontier only |
|---|---|---|
| Nell / Power | Frost Arrow coefficient becomes 1.5× normal hit | Its slowed targets take +20% damage from all allies |
| Nell / Toughness | Nell gains +25% DEF for 2 actions after firing | Frost Arrow also lowers target ATK by 20% while its slow lasts |
| Nell / Speed | Hits 2 enemies | Hits all enemies |
| Nell / Focus | Slow lasts 5 actions | Slow interval multiplier becomes ×2 |
| Severa / Power | Coefficient becomes 3× instead of 2.5× | A signature kill refills 50 meter, once per cast |
| Severa / Toughness | Takes 30% less damage for 2 actions | Heals for 20% of total signature damage dealt |
| Severa / Speed | Second target takes half damage | Primary target full damage, every other enemy half |
| Severa / Focus | Signature damage to Elites ×1.5, after its coefficient | Applies −30% DEF for 3 target actions |
| Anselm / Power | During Phalanx, retaliates using 50% of Anselm's ATK | Retaliation uses 100% ATK |
| Anselm / Toughness | Phalanx DEF bonus becomes +75% | Casting heals 15% max HP |
| Anselm / Speed | Phalanx lasts 5 actions | Starts each fight at 50 meter |
| Anselm / Focus | Other living front allies gain +25% DEF for their next 3 actions | Provokes all enemies while Anselm's Phalanx remains active |
| Otto / Power | Signature coefficient becomes 2× | Stun skips 2 actions |
| Otto / Toughness | Gains +30% DEF for 2 actions | Casting heals 10% max HP |
| Otto / Speed | Hits and stuns 2 enemies | Hits and stuns all enemies |
| Otto / Focus | His stunned targets take +25% damage from allies | Against a slowed target, stun skips 2 actions |

Multi-target choices hit the primary front enemy, then the next living enemy in stable slot order. Anselm retaliates inside the incoming action against its attacker, using the normal formula with the listed ATK coefficient; retaliation generates no meter or recursive counter. Otto's two longer-stun effects give at most two skips, not four. Severa's Elite bonus stacks with her fixed Big Game Hunter passive. Healing caps at max HP and never revives.

Innate passives are fixed, one per authored adventurer. Remove the old learned skill-point system and Pathfinder levels; Route Map supplies the search bonus. Otto's plate-and-warhammer design is his only outfit; there is no later shield variant.

**Frontier scaling:** levels 7–10, rank-2 modifiers and the raised lifetime cap open on arrival; the opening limits do not reset purchased stats or charge for them again.

### 6.3 Stamina, fatigue and rest — Designed, not yet proven

| Rule | Value |
|---|---|
| Stamina | 4 bars maximum |
| Deployment | Spend 1 immediately; recall does not refund it; cannot depart from 0 |
| Red Fatigue | At 1 or 0 bars after debit: ATK, DEF and attack rate ×0.5; scout injury chance ×2 |
| Overnight sleep | Restore 1 bar, capped at 4, once per night |
| Rest order for the day | No dispatch that day; restore to 4 at 20:00 |

These are the only stamina recovery rules. Idle hours, hiring, rehire, rebuild and injury expiry grant no extra stamina. Full stamina is an initial condition for a never-hired recruit, not a repeatable rehire reward. An injured adventurer can sleep or receive a rest order, but stamina recovery never removes the injury.

Assign rest at 07:00 or later only if the person has not dispatched that day. No retroactive rest after an expedition. A rest order locks dispatch for the rest of that day; cancelling before 20:00 removes its full-recovery entitlement. Overnight sleep may follow a rest day, but the cap prevents extra bars. Show stamina before and after debit: the third dispatch from 4 begins fatigued at 1.

**Frontier scaling:** preserve the four-bar rules; a larger roster makes rotating rest practical rather than adding a new recovery currency.

### 6.4 Health and injury — Carried over; Designed, not yet proven (timing clarification)

| Condition | Rule |
|---|---|
| Healthy and idle at HQ, including rest and sleep | Recover 10% max HP per calendar hour, capped at max; calculate proportionally to elapsed ticks |
| Downed hunter/contract member | Return at 25% max HP; injured for 48 calendar hours |
| Injured scout | Immediate return at 40% max HP; injured for 48 calendar hours |
| During injury | No passive HP recovery or dispatch; HP stays at return value |
| Injury expiry | Become Available unless another valid restriction applies; ordinary idle HP recovery resumes; no stamina award |

An 11-hour night heals an otherwise healthy idle person fully, even from very low HP. If injury expires partway through it, only the remaining healthy hours heal. A downed fighter stays down through that operation; surviving allies can continue. On return each downed member receives the injury state; a wipe returns everyone immediately. Never restore HP by repeatedly equipping max-HP gear.

**Frontier scaling:** retains injury rather than death; later hazards must use explicit prep warnings. No additional serious-injury tier is part of this design.

### 6.4a Nobody is lost for good — Carried over

Defeat means injury, never permanent loss. Unpaid employees temporarily leave after returning crafted gear and backpack items to storage. Former staff stay visible indefinitely, retaining stats, XP, stamina and outstanding injury timers. Rehire costs unpaid wages plus the original hire cost and requires a free bed or station. Time may expire an injury while absent; absence grants no Guild sleep/rest recovery. Dismissal also preserves the person and does not erase accrued wages. Officers never enter the employee recruitment pool or leave over payroll. The rescue loan in 13.4 keeps recovery possible.

**Frontier scaling:** carry every authored person and former-staff record across relocation; no replacement by anonymous rolls.

### 6.5 States — Designed, not yet proven

One primary state: Available, Hunting, Scouting, On contract, Resting, Injured, Event-locked, or Left. Red Fatigue is a condition overlay, not a second primary state. Preserve injury end-time separately while Left or Event-locked. A rest-day order may apply during injury without changing the displayed Injured state. After release, derive the state from active restrictions; do not blindly set Available. All dispatches recheck employment, HP above zero, injury, stamina, state and reservations.

**Frontier scaling:** the same states cover larger rosters and the relocation lock; no Dead state.

### 6.6 Backpack — Carried over; Designed, not yet proven (item contract)

| Rule | Value |
|---|---|
| Grid | F/E: 4×4; D/C: 5×4; B/A/S: 5×5 |
| Equipment bonuses | One active weapon upgrade, one armour upgrade, one accessory per adventurer |
| Potion | 20G; 1×1; restores 30% max HP |
| Potion trigger | After an enemy damage action, if alive and HP ≤40%; first potion in row-major order, at most one per action |
| Bow / Arrow Case adjacency | Share an orthogonal edge: +15% attack rate once |
| Item rotation | 90° steps; no overlap or out-of-grid placement |

Starter weapon/clothes are bound and included in base stats, occupy no cells and cannot be sold. Nell can place a zero-bonus 1×3 starter-bow token to activate Arrow Case adjacency; Hunter Bow replaces the token. Crafted footprints and effects are in 12.2. No backpack stacking: each consumable is a separate physical item. Reserve lures and maps for an expedition and consume them at dispatch; a reusable active Route Map stays packed. Equipment carried but not selected in its category gives no bonus. Materials and corpses use shared storage, not these grids.

After enemy damage, determine downing first; a potion cannot revive or trigger between cosmetic combo hits. Equipment edits require Available at HQ, and prep edits remain a draft until dispatch. Removing max-HP gear clamps current HP; adding it does not heal. Invalid placements keep the original item intact. Respecs, grid changes and rehires must never delete inventory.

**Frontier scaling:** 5×5 packs at higher Guild ranks, more gear choices and stronger tiers; keep category limits so carrying duplicates is not unlimited power.

### 6.6a Consumables — tier 1 in Eurydica *(owner decisions 2026-09-29; designed, not yet proven)*

Consumables are a **heavy requirement, never a mandatory one** (Monster Hunter World is the reference). They sit in the backpack, one 1×1 cell each, so they compete with gear for space, and the risk forecast includes them. Eurydica has **tier 1 only, bought, not crafted**: Elsie's counter before Commerce, then also Valerie's Trading Post, at any base. Tiers 1–5 come from the Frontier's **Research Department** (16a; `Consumables and Research Proposal.md`).

| Tier-1 item | Price | Trigger | Effect |
|---|---|---|---|
| Potion | 20G | In combat: after an enemy damage action, if alive and HP ≤40% (6.6) | Restores 30% max HP |
| Demondrug | 30G *(starting value)* | Whole expedition, from departure | +8% ATK for the carrier |
| Armorskin | 30G *(starting value)* | Whole expedition, from departure | +8% DEF for the carrier |
| Hunting Lure | 25G | Consumed at hunt departure | +10 points to the target's group chance (9.2) |
| Scout Map | 20G, once scouting opens | Consumed at scout departure | +10 points to find chance (8.2) |

- One Demondrug and one Armorskin effect per fighter; a second copy doesn't stack. A recall never refunds a consumed item; unused items come home.
- Dr. Wendt's clinic request keeps its weekly allotment of four potions at 18G (11.1).
- **Tuning target (owner):** a normal party without consumables still succeeds, but often comes home with its front line near 50% HP. A **solo hunt without potions and a Demondrug or Armorskin should fail**. Balance monsters and prices to this in the M3 playtest.
- Purchased consumables resell for at most half their actual purchase price, so there is no buy-sell loop.

## 7. Regions and discovery — Proven (structure); Designed, not yet proven (completion rules)

### 7.1 Map — Carried over

| Eurydica area | Required Guild Rank | Theme |
|---|---|---|
| Hylaea Forest | F | Old oak forest, South Gate road; beasts and forest-habitat fantasy monsters |
| Bernmoor | E | Reedbeds and slow water |
| Erythra Highlands | D | Cold stone stairways and ridges |

Locked areas show rank and story context. Each area contains three ordinary species, three landmarks (including two dens) and two hidden paths. Rare monsters and bosses are separate from that ordinary count. No extra regional boar species are implied by proof recolours.

### 7.2 Discovery — Designed, not yet proven

| Milestone | Effect |
|---|---|
| Each completed scout half-hour | +2 percentage points, capped at 100%; incomplete intervals give nothing |
| Full 3-hour scout | +12 points, unless charting ends the trip early |
| 25% / 50% | Identify second / third ordinary species |
| 75% | Reveal first missing den in table order: second-species den, then third-species den |
| 100% | Reveal all remaining fixed landmarks/paths; return active discovery scouts after resolving that interval |

Add progress before evaluating identification and eligible finds. Multiple scouts contribute separately in stable operation order. Den discovery never bypasses species identification. If an interval charts the area, other simultaneous scouts still receive their due interval rewards and injury roll, but cannot duplicate unique finds or add progress beyond 100%. After charting, offer repeat surveys for rare leads with the same duration, stamina, find and injury rules; they add no exploration. Hunts and discovered benefits remain available.

At the current rate, boars require 13 intervals (6.5 scout hours, 26%), wolves 25 (12.5 hours, 50%), and full charting 50 (25 hours). That is 3, 5 and 9 trips of up to 3 hours, respectively. Two full trips reach only 24%. The old 30-points-per-trip rule would need four trips, not five; it is historical, not active. Scouting opens by events in 14, not by an assumed Day 1 sandbox schedule.

### 7.3 Region Knowledge — Proven (panel); Designed, not yet proven (source links)

Show known species out of three, landmarks out of three, paths out of two, current search time, effective target probabilities, active benefits and rare sightings. Finds clear local fog on the parchment field map. Each known hunting-ground card links outputs to recipes, requests and pinned projects; bonuses to group size also show added danger.

**Frontier scaling:** new areas reuse this schema with independent exploration and source data. Their places and species require content authoring; section 16a defines route verification without inventing them.

## 8. Scouting — Proven (field view); Designed, not yet proven (complete tables and risk)

### 8.1 Rules — Carried over

| Rule | Value |
|---|---|
| Party / stamina | Exactly 1 adventurer / 1 bar at departure |
| Duration | 30-minute increments, up to 3 hours; return at 20:00 if earlier |
| Fighting | None |
| Reputation | +2 once if at least one interval completes, including injured/recall returns |
| Recall | Immediate; keep completed findings and progress |

### 8.2 Finds — Designed, not yet proven

Each completed interval adds exploration, resolves threshold reveals, then rolls once for an eligible weighted find. Chance is 45%, plus 10 percentage points for Tracker and 10 for one consumed Scout Map, capped at 80%. Remove discovered fixed entries and active/reserved sightings from the pool. A hint may appear once per still-unidentified species within 20 points of its threshold; it gives no find XP. Empty pools show “No new lead,” never fabricate a reward. Discoveries awarded by milestone guarantees do not also remain available for the same interval's random roll.

| Hylaea find | Kind | Eligible at | Weight | Effect |
|---|---|---|---|---|
| Charcoal Burners' Trail | Path | 10% | 3 | Search −5 min |
| Dire Boar Nest | Den | 15% | 3 | Boar encounter weight ×1.5; target group +15 points when known |
| Mossy Spring | Landmark | 30% | 2 | Living hunters heal 10% max HP after a won fight |
| Old Poachers' Track | Path | 40% | 2 | Search −5 min |
| Howling Ridge | Den | 55%, wolf known | 2 | Wolf weight ×1.5; target group +15 points; area variant chance +4 points |
| Fresh tracks | Hint | Within 20 points of next identification | 2 | Hint only |
| Mossback Elder | Rare sighting | Boar known | 1.5 | One available sighting |
| Silvermane | Rare sighting | Wolf known | 1 | One available sighting |

| Bernmoor find | Kind | Eligible at | Weight | Effect |
|---|---|---|---|---|
| Reedcutters' Causeway | Path | 10% | 3 | Search −5 min |
| Serpent Reedbed | Den | 15% | 3 | Serpent weight ×1.5; target group +15 points when known |
| Dry Islet | Landmark | 30% | 2 | Area scout injury chance ×0.75 |
| Raised Towpath | Path | 40% | 2 | Search −5 min |
| Stalker Hollow | Den | 55%, Stalker known | 2 | Stalker weight ×1.5; target group +15 points |
| Fresh marsh tracks | Hint | Within 20 points of next identification | 2 | Hint only |
| Reedcoil Elder | Rare sighting | Serpent known | 1.5 | One available sighting |
| Pale Marsh Stalker | Rare sighting | Stalker known | 1 | One available sighting |

| Erythra find | Kind | Eligible at | Weight | Effect |
|---|---|---|---|---|
| Quarry Steps | Path | 10% | 3 | Search −5 min |
| Highland Wolf Lair | Den | 15% | 3 | Wolf weight ×1.5; target group +15 points when known |
| Sheltered Cairn | Landmark | 30% | 2 | Area scout injury chance ×0.75 |
| Miners' Traverse | Path | 40% | 2 | Search −5 min |
| Drake Roost | Den | 55%, Drake known | 2 | Drake weight ×1.5; target group +15 points |
| Fresh ridge tracks | Hint | Within 20 points of next identification | 2 | Hint only |
| Redmane Alpha | Rare sighting | Highland Wolf known | 1.5 | One available sighting |
| Old Ridge Drake | Rare sighting | Ridge Drake known | 1 | One available sighting |

Find chances and forecast presentation use the stated baseline (Commander skills and officer perks can modify this; see section 5 and the Commander section).

### 8.3 The field view — Proven

Follow shows the scout walking while the painted world scrolls, with exploration, field map, information list, log and parchment discovery pop-ups. Leaving or reopening it never changes progress, RNG or risk. Watching scouting does not invoke battle pace.

### 8.4 Rare targets — Designed, not yet proven

A sighting adds one purple RARE target and does not expire with time. Dispatch reserves it exclusively for one hunt. Each completed search has a 70% chance to meet that rare until it appears. It is solo, can appear at most once and produces at most one corpse per reservation. After its defeat, remaining searches use ordinary species only. Ending the hunt consumes the sighting whether successful, recalled, injured or cut off. A later scout can find it again, including after 100% charting. Rare stats, raw values and processing are in section 10.

### 8.5 Scout risk — Designed, not yet proven

| Area | Base injury per completed half-hour | Full six-interval trip, no modifiers |
|---|---|---|
| Hylaea | 1% | 5.85% injury; 94.15% no incident |
| Bernmoor | 1.5% | 8.67% injury; 91.33% no incident |
| Erythra | 2% | 11.42% injury; 88.58% no incident |

Use `1 − (1 − p)^n`, where n is the number of intervals that can complete before the selected return/cutoff. Apply area landmarks, flashpoint aftermath and Red Fatigue before calculating p. For changing p, use `1 − product(1 − p_i)`. Six fatigued Hylaea checks at 2% give 11.42%, not 12%. Progress/finds/XP resolve before each injury roll. Injury ends the scout immediately at 40% HP for 48 hours, with earned results and the +2 Reputation. No death or serious-injury lottery.

**Frontier scaling:** initial base risk is 2% per half-hour, with the same forecast contract and safe-route benefits; new content supplies the area-specific data.

## 9. Hunting and combat

### 9.1 Hunt rules — Proven (loop); Designed, not yet proven (precise contract)

| Rule | Value |
|---|---|
| Party / cost | 1–5 adventurers; 1 stamina each at departure |
| Duration | 1, 2 or 3 hours, including searches and combat; shortened by cutoff |
| Return | Immediate at selected duration, recall, wipe or 20:00; no extra return travel |
| Loot | One corpse per completed kill, secured immediately |
| Reputation | +1 per secured hunt/contract corpse returned, once |
| After victory | Resume search if time remains |

Search minutes are `max(10, (30 × (1 − 0.25e) − 5p) × m)`, where e is exploration/100, p is found paths and m is 0.95 with one active Route Map, otherwise 1. Round the result up to a 12-second tick. At 0%/no paths it is 30 minutes; at 100%/two paths it is 12.5 minutes before rounding, 12.6 after. Multiple Route Maps never stack.

For an ordinary target, assign weight 0.70 to it and divide 0.30 equally among other known ordinary species. With only one known species its chance is 1. Multiply each den species' weight by 1.5 and normalise. Flashpoint aftermath replaces the target's pre-den share with 0.85 and the others' total with 0.15. For a reserved rare, preserve its 0.70 chance; distribute only the ordinary 0.30 equally among known species, den-weighting and normalising inside that share. After the rare encounter, use equal known-ordinary weights modified by dens for remaining searches.

Interrupted, unfinished actions yield no kill or damage; every earlier completed kill remains secured even if a later action wipes the party. No “final exchange” exclusion. Dispatch preview shows the actual shortened finish time and rejects departure at/after cutoff.

**Frontier scaling:** retain local expeditions of at most three hours initially; routes modify existing search rules within the same floor.

### 9.1a Formation: front and back rows — Proven

| Rule | Value |
|---|---|
| Slots | 3 front + 3 back; at most 5 people total; at least 1 front at dispatch |
| Valid examples | 2 front + 3 back; 3 front + 2 back; 1 front + 3 back |
| Enemy target | Enemy slot index wraps over living front members in slot order; if none, use living back members |
| Party target | Front living enemy unless skill says otherwise |
| Melee in back | Damage ×0.5 |
| Ranged in either row | Full damage |

Prep has row labels, reach icons, swap/remove and melee warnings. Every battle HUD member is tagged FRONT or BACK. Provoke is the only opening-act exception to enemy row targeting. Re-evaluate targets at action start; a dead queued target retargets to the next valid living one. No back-row bypass enemy type is included here.

**Frontier scaling:** future authored reach attacks must declare their targeting and warning; they do not silently change the baseline row rule.

### 9.2 Groups — Proven (groups); Designed, not yet proven (probability semantics)

| Ordinary species | Base group chance |
|---|---|
| Moss Slime / Dire Boar / Forest Wolf | 60% / 45% / 70% |
| Marsh Slime / Marsh Serpent / Marsh Stalker | 60% / 40% / 50% |
| Stone Crawler / Highland Wolf / Ridge Drake | 40% / 70% / 30% |
| Rares and bosses | 0%; solo |

For the selected ordinary hunt target, `c = min(0.95, base + den 0.15 + Tracker 0.10 + lure 0.10)`, adding only present bonuses. Tracker never stacks. Other ordinary encounters use base c. Roll a second monster at c; only if it joins, roll a third at c/2. All members share the selected species, with independent variant rolls. Expected group size is `1 + c + c²/2`; a boar target with all bonuses has c=0.80 and expectation 2.12. Fixed optional-contract encounters do not add hunt group rolls.

**Frontier scaling:** content can add species/group data while preserving the probability cap, three-enemy limit and disclosed risk.

### 9.3 Combat rules — Proven (queue); Designed, not yet proven (edge cases and officer kit)

| Rule | Value |
|---|---|
| Attack interval | `ceil((120 / effective rate) / 12) × 12` Guild seconds; apply interval slow before final tick rounding |
| Normal base damage | `max(1, floor(effective ATK × 100 / (100 + effective DEF)))` |
| Final damage | Apply skill coefficient, row penalty and damage-taken/dealt multipliers to base damage; floor once, minimum 1 |
| Normal / skill / stunned lost action | 24 / 72 / 12 Guild seconds |
| Queue | Readiness time, then front slots, back slots, enemy slots; stable slot order |
| Stage | One action at a time per encounter; independent encounters run concurrently |

Build stats from listed base × (1 + track percentages), then flat equipment, then applicable passives, fatigue, whole-expedition consumables (Demondrug, Armorskin; 6.6a) and temporary multipliers. Keep fractional stats until the damage or tick rounding point. Snapshot permanent build, equipment, row and post-debit fatigue at fight start. Apply temporary status and target-specific Big Game Hunter dynamically; mixed ordinary/variant groups do not grant its Elite bonuses against ordinary targets.

Attack gauges start empty. They fill while another fighter acts, then queue once and stop; an actor's gauge restarts after its action ends. Retain fractional gauge progress if a dynamic rate/slow changes. At each tick finish the active action, remove downed actors, update surviving gauges and mage meters for elapsed time, and queue new ready actors. Only after the timed-event/cutoff phases in section 4 may a still-active operation start its next action; never start one at its return time or at 20:00. Tied readiness uses the table order. Big Game Hunter uses the current valid intended target while charging and is re-evaluated at action start; display interval changes when that target changes tier. A stunned ready fighter loses one queued action for 12 seconds, consumes one skip, restarts its gauge, and spends no skill meter.

Resolve damage at action end. Multi-target results belong to one atomic action in target order. Resolve damage/downing, nonrecursive retaliation from a surviving defender, potion trigger for a surviving recipient, meter awards and status application; then age pre-existing affected-actor status counters. Discard invalid targets rather than hit corpses. Stop the operation only after completed-action rewards are secured. Recall/duration/cutoff cancels the unfinished action and discards that encounter's remaining queue.

Same-stat buffs use strongest magnitude and longest remaining duration without adding duplicates. Debuffs follow the same rule; up and down multiply. Incoming-damage vulnerability uses the strongest overlapping value. Provoke uses newest living valid source; when it ends, return to ordinary row targeting. Stun refreshes to the greater remaining skip count rather than adding. Effect durations run on the affected fighter's actions; a skill granting its caster a buff does not immediately shorten that buff. Combat-only buffs, meters and queues reset between encounters except explicit starting-meter modifiers.

| Story guest | HP / ATK / DEF / rate | Role and moves |
|---|---|---|
| Tristitia | 360 / 38 / 24 / 1.2 | Melee attacker. Rose Waltz: one normal action's damage shown as two hits; +20% attack rate for 3 recipient actions to one seeded-random living ally. Piercing Verdict: 2.5× normal hit; target DEF −25% and interval ×1.5 for 3 target actions. |
| Elsie | 420 / 30 / 36 / 1.0 | Melee defender, longsword and martial arts. Hateful Slash: normal hit to front enemy; provokes all living enemies for each enemy's next 2 actions. |

Story guests occupy normal party slots, use the same queue and meters, and receive no persistent adventurer XP. Their presence is explicit in the story formation preview. Tristitia's visual two-hit combo is one meter event. No every-third-action override. These numbers describe officer combat kits, not department perks.

Prep risk is approximate Low/Moderate/High advice from 100 complete fixed-seed simulations separate from gameplay RNG: under 5% / 5% to under 25% / at least 25% with any downed member. Use the selected duration, formation, equipment, fatigue, groups and variants; display main causes, never a promised survival probability. Cache by prep inputs; recalculating does not reroll gameplay.

At watched 1×, a normal action takes 0.8 real seconds and a skill 2.4. A 23-game-minute queued fight takes 46 watched seconds. The older 19-minute batch sample is historical; neither sample establishes the safety of later regions or two-person boar teams. Presentation references remain in 9.4–9.6, but this simulation contract governs them.

**Frontier scaling:** new kits and enemies use this same deterministic contract; more content does not create a separate officer combat engine.

### 9.3a Skill meter — Proven (meter); Designed, not yet proven (exact timing)

| Role | Gain |
|---|---|
| Attacker | 25 per completed normal damage action; not per cosmetic hit or target |
| Defender | 20 per enemy damage action received while surviving; not per cosmetic hit |
| Mage | Continuous in-combat gain `100 / (4 × current rounded attack interval)` per Guild second |

Focus multiplies these gains; Chloris's passive multiplies mage gain again. Meter is clamped to 0–100; there is no charge out of combat. At action start, use a signature if meter is 100 and consume 100; a completed skill generates no normal-action meter from its own damage. Explicit retain/refill modifiers apply after completion. Starting at zero with no modifiers, an attacker completes four normal actions and uses the skill as action five. Defender meter can fill during another actor's action; skills still wait for readiness and queue order. Mage gain continues while queued or acting, capped normally. Interrupted skills do not refund consumed meter, and ending the encounter resets it.

The orange meter glows with SKILL at full; the gold ring remains the attack timer. Never use blue MP styling for either.

**Frontier scaling:** rank-2 retention and starting-meter modifiers use these explicit exceptions; no automatic meter-system replacement.

### 9.3a2 Standing orders: when to use the signature *(owner decision 2026-10-01; designed, not yet built)*

Hunts stay automatic and watching never changes the outcome. The player plans instead: each adventurer has **one standing order for their signature skill**, saying when to use it once the meter is full. Much simpler than Unicorn Overlord or Pillars of Eternity by design.

| Order | The skill fires when the meter is full and... |
|---|---|
| **As soon as ready** (default) | always (today's behaviour) |
| **Save for an Elite** | a rare, variant or boss enemy is in the fight |
| **When I'm hurt** | the adventurer is below 50% HP |
| **When a front ally is hurt** | a living front-row ally is below 50% HP (suits Anselm's Phalanx with its Focus upgrade) |
| **Before an enemy skill** | any enemy's skill meter is at 80% or more (9.3b), so a defensive skill is up for the big hit |

- **The trade-off:** while the skill is held, the meter stays full and gains nothing, so holding too long means fewer skills. A held skill is used at the first action where its condition is true.
- **Unlocks:** *As soon as ready* from the start; the others unlock through Elsie's training (5.4, the Adventurer Office) so the system arrives gradually.
- **Later, optional:** a targeting rule for attack skills (front, weakest, the enemy that hit an ally) and an adjustable potion threshold (25 / 40 / 60%).
- Deterministic: orders read only fight state, never randomness or watching.

### 9.3b Monster skills *(new, owner decision 2026-09-28; designed, not yet proven)*

Every monster has **one skill**: ordinary monsters, their variants, rares, bosses and flashpoints.

**When it fires:**
- Monsters use the **attacker meter** (9.3a): +25 per completed attack. When it's full, the monster's next action is its skill, and the meter resets to 0.
- So a monster's skill comes every **fifth action**. The ordinary action order and the watch/unwatch equivalence are unchanged.

**How strong it is:**

| Tier | Skill budget (pick one form) |
|---|---|
| Ordinary (and its variants) | A single hit at **×1.5** damage, **or** a normal hit plus **one light status** lasting 2 of the target's actions (ATK DOWN −15%, DEF DOWN −15%, or SPD DOWN: interval ×1.25) |
| Rare | A single hit at **×2.0**, **or** ×1.25 plus one status lasting 3 actions (−25%, or interval ×1.4) |
| Boss and flashpoint | Their authored kit (10.x): up to ×2.5, or a status on the whole front row, or a stun of 1 action |

**Rules:**
- A skill targets like a normal attack (front row first, provoke respected).
- Statuses follow the stacking rules in 9.3.
- A variant keeps its parent's skill; its ATK bonus applies as normal.
- Skill names, effects and still poses are listed per monster in `Production Assets Requirement/Eurydica Monsters.md`, **approved by the owner on 2026-09-28**.
- The hunt risk estimate (9.1) includes monster skills.

**Frontier scaling:** Frontier monsters may carry authored multi-target or two-skill kits at boss tier; ordinary monsters stay at one skill.

### 9.4 Battle presentation - Proven (proof 2 and operations proof)
**Changed from v1.1:** presentation is now Octopath-style HD-2D.

**Layout**
- Party on the right facing left, enemies on the left. Up to three enemies: one in front, two behind.
- Attackers step forward to strike. Officers with battle sets play their full moves.
- A clearing in the area's battle background, with depth of field.

**Impact feel**
- **Hit-stop**: 0.13 s for normal hits, 0.26 s for big ones.
- **Flash**: the target sprite only (never the whole screen), 1–2 frames, light grey so it never blooms.
- **Spark**: a small hit spark at the point of contact.
- **Shake**: smooth, directional and decaying. Never random jitter.
- **Damage numbers**: pop at body height; stacked hits are offset.
- **Skills**: a camera push-in and vignette that hold for the whole skill.
- The proofs' VFX are placeholders. Godot gets real slash and thrust effects matching the Soulcalibur VI references. Full-screen tints only for skills and breaks.

**Battle HUD**
- **Enemy HP**: top centre, one bar per enemy (RARE badge where it applies).
- **Party gauges** *(changed 2026-10-02, owner; replaces the 2026-09-28 card column)*: a slim column of round gauges down the right edge, in the style of Kingdom Hearts.
  - A round bust (face and shoulders from the front idle sprite) in each gauge.
  - **HP is the thick arc** round the bust (green, yellow below half). There is no HP number: the arc shows it.
  - **The skill meter is a thin orange arc** outside it, glowing with a SKILL tab when full. Never blue: that reads as MP.
  - The name sits under the gauge as plain text with a shadow, no box. No FRONT/BACK label: the formation is visible on the field.
  - The acting member's gauge glows.
- **Timeline ring** *(new 2026-10-02, owner; in the style of Grandia 3)*: bottom left, a round timeline. **Party markers ride the inner (blue) track and enemy markers the outer (red) track**, with blue and red rims. Each marker moves clockwise at its fighter's attack speed; whoever reaches the gilded **ACT** section acts.
  - The centre hub shows **NEXT**, the bust of whoever acts next.
  - The acting fighter's marker glows. Markers ease forward, and jump back a little when their fighter takes a hard hit.
  - An enemy whose skill is due gets a red **SKILL** flag that pulses gently.
  - Hunts are automatic, so the ring has only Wait and ACT. A command section, where time stops for orders, is for the hand-played flashpoints (`Game Design/To-Do (Later).md`).
- **Left side**: place and target, time left, secured corpses.
- **Battle log** *(changed 2026-10-02, owner)*: a small button at the top left showing the latest line. Pressing it opens a semi-transparent black log window in the centre of the screen, with white text and names, numbers and skills in bold. **Game time pauses while the log is open** and resumes when it closes, as on the management screens.
- **Buttons**: Leave view and Recall. The HUD cluster with the speed controls stays visible.
- **Closing the view never stops the fight**, and reopening it shows the live state.

### 9.5 The search walk *(new)*
While a hunting party searches, the field view shows them walking in formation as the world scrolls past. When an encounter starts, the scroll eases to a stop and the monsters slide in from the left. After a win the party walks on. The environment layers must loop horizontally (2.4).

### 9.6 Officer battle moves
Officers fight only at story moments, so their battles are showpieces. They use the same combat model as adventurers (9.3). This table covers presentation.

| Officer | Weapon | Attack | Skill | Guard |
|---|---|---|---|---|
| Tristitia | Rapier (right-handed) | **Rose Waltz**: a dance-like combo. Hit 1 lands after the pass-through cut, when she has turned her back (samurai draw); hit 2 is a low cut. The final raised hand gives a random ally SPD UP. | **Piercing Verdict** (when her skill meter is full, 9.3a; numbers in 9.3): a flourish and charge at her own spot, then a high-speed lunge that ends *behind* the target. Heavy damage plus DEF DOWN and SPD DOWN for 3 turns. | Rapier parry |
| Elsie | **Longsword and martial arts** (decided 2026-09-27), in the spirit of Yoshimitsu (Tekken): sword cuts flowing into punches and kicks. Front row. | A mixed sword, kick and punch combo (`Elsie/Attack.mp4`) | **Hateful Slash**: a slash that provokes. Every enemy must attack Elsie for its next 2 actions, protecting the rest of the party (`Elsie/Skill, Hateful slash(provoke enemy).mp4`) | Sword crosswise against her forearm, front knee raised (batch 2, prompt in Revision 5) |

- **Elsie:** the greatsword is dropped (every attempt failed), and so is the spear and short sword. She now fights with a longsword plus kicks and punches. Her stance, attack and skill are made; batch 2 (idle, hurt, guard, victory, defeat) uses `Gemini Battle Batch Prompts.md` Revision 5. Her skill changed from the party buff to a provoke, which fits her role of keeping adventurers safe.
- **Provoke:** a provoked enemy ignores the front-row rule and attacks the provoker until the effect ends.
- Status effects in use: ATK UP, DEF UP, SPD UP, DEF DOWN, SPD DOWN, PROVOKE.

---

## 10. Monsters and materials — Proven (Hylaea proof); Designed, not yet proven (complete rewards and later balance)

### 10.0 Variants — Proven (appearance and encounters); Designed, not yet proven (parts)

| Rule | Value |
|---|---|
| Appearance | 15% larger, distinct palette, VARIANT badge; alert even when unwatched |
| Stats | Parent HP ×1.5; ATK and DEF ×1.25; parent rate |
| Chance | 8% independently per ordinary hunt member; Howling Ridge adds 4 points in Hylaea; total cap 20% |
| Tier / XP | Elite: Variant; parent base XP ×2 exactly once |
| Processing | Parent time, ordinary outputs and rare roll, plus one guaranteed elite unit |

Rare, Variant and Boss are mutually exclusive Elite subtypes. Fixed contract encounters use the listed ordinary/boss identity without random variant upgrades. The exact number of variants per hunt depends on completed encounters; no fixed “one every two hunts” promise. Nine ordinary species mean nine elite material IDs. All early elite parts are saleable, with their stronger uses in higher-tier Frontier recipes (gear and consumables) previewed for the Frontier.

### 10.1 Hylaea Forest — Proven (ordinary proof values); Designed, not yet proven (bosses and rares)

| Monster | HP | ATK | DEF | Rate | Hunt knowledge | Base processing | Common unit value | Base XP |
|---|---|---|---|---|---|---|---|---|
| Moss Slime | 180 | 4 | 0 | 0.7 | 0% | 30 min | 8G | 6 |
| Dire Boar | 330 | 6 | 8 | 0.8 | 25% | 45 min | 12G | 11 |
| Forest Wolf | 420 | 8 | 10 | 1.0 | 50% | 60 min | 16G | 14 |
| Blackfang Direwolf | 1,950 | 15 | 25 | 1.0 | Optional contract | 90 min | 30G | 65 |
| Hylaea Chimera | 2,400 | 17 | 25 | 1.0 | Chapter 2 flashpoint | 120 min | 30G | 80 |

These retain the beefier ordinary monster values already used in the operations proof. Historical batch and queued timing measurements belong to their specific test parties; they are not fresh v2.1 balance evidence.

### 10.2 Bernmoor — Carried over (ordinary/boss stats); Designed, not yet proven (complete data)

| Monster | HP | ATK | DEF | Rate | Hunt knowledge | Base processing | Common unit value | Base XP |
|---|---|---|---|---|---|---|---|---|
| Marsh Slime | 510 | 10 | 15 | 0.8 | 0% | 45 min | 18G | 18 |
| Marsh Serpent | 660 | 13 | 20 | 1.0 | 25% | 60 min | 22G | 24 |
| Marsh Stalker | 840 | 15 | 25 | 1.1 | 50% | 75 min | 28G | 30 |
| Ambermaw Matriarch | 3,300 | 21 | 35 | 1.0 | Chapter 2 flashpoint (second) | 120 min | 45G | 110 |

### 10.3 Erythra Highlands — Carried over (ordinary/boss stats); Designed, not yet proven (complete data)

| Monster | HP | ATK | DEF | Rate | Hunt knowledge | Base processing | Common unit value | Base XP |
|---|---|---|---|---|---|---|---|---|
| Stone Crawler | 900 | 17 | 35 | 0.8 | 0% | 60 min | 30G | 32 |
| Highland Wolf | 1,140 | 20 | 30 | 1.1 | 25% | 75 min | 36G | 38 |
| Ridge Drake | 1,500 | 24 | 45 | 0.9 | 50% | 90 min | 45G | 48 |
| Crownstone Wyrm | 5,400 | 28 | 50 | 1.0 | Chapter 2 flashpoint (third) | 150 min | 65G | 180 |

### 10.4 Rare monsters — Designed, not yet proven

| Rare / parent | HP | ATK | DEF | Rate | Processing | Raw-corpse reference value | Base XP before ×3 |
|---|---|---|---|---|---|---|---|
| Mossback Elder / Dire Boar | 800 | 11 | 18 | 0.8 | 60 min | 60G | 32 |
| Silvermane / Forest Wolf | 950 | 13 | 16 | 1.1 | 75 min | 75G | 38 |
| Reedcoil Elder / Marsh Serpent | 1,320 | 17 | 25 | 1.0 | 90 min | 110G | 55 |
| Pale Marsh Stalker / Marsh Stalker | 1,680 | 20 | 30 | 1.1 | 105 min | 140G | 65 |
| Redmane Alpha / Highland Wolf | 2,280 | 26 | 36 | 1.1 | 105 min | 180G | 80 |
| Old Ridge Drake / Ridge Drake | 3,000 | 30 | 50 | 0.9 | 120 min | 225G | 95 |

Rares yield their parent's three common units and one guaranteed parent rare unit; Mossback retains the boar split of two meat and one hide. These values are raw-corpse references, not the price of each processed part. Rares do not also roll an extra rare output or elite-variant part.

### 10.5 Material outputs — Designed, not yet proven

All values below are **per unit at Standard quality**. Ordinary corpses give three total common units plus one 20% roll for a single rare unit. One persistent quality roll applies to all outputs. “Rare part” means the processing output, not a rare-monster corpse and not an elite-variant part.

| Species | Three common units | Rare unit / value | Elite-variant unit / value |
|---|---|---|---|
| Moss Slime | 3 Slime Gel, 8G each | Slime Core / 40G | Elite Slime Core / 80G |
| Dire Boar | 2 Boar Meat + 1 Boar Hide, 12G each | Boar Tusk / 60G | Elite Boar Tusk / 120G |
| Forest Wolf | 3 Wolf Pelts, 16G each | Wolf Fang / 80G | Elite Wolf Fang / 160G |
| Marsh Slime | 3 Marsh Gel, 18G each | Marsh Core / 90G | Elite Marsh Core / 180G |
| Marsh Serpent | 3 Serpent Scales, 22G each | Venom Gland / 110G | Elite Venom Gland / 220G |
| Marsh Stalker | 3 Stalker Hides, 28G each | Stalker Claw / 140G | Elite Stalker Claw / 280G |
| Stone Crawler | 3 Crawler Plates, 30G each | Crawler Core / 150G | Elite Crawler Core / 300G |
| Highland Wolf | 3 Highland Pelts, 36G each | Highland Fang / 180G | Elite Highland Fang / 360G |
| Ridge Drake | 3 Drake Scales, 45G each | Drake Heart / 225G | Elite Drake Heart / 450G |

Preserve existing item IDs; “common slime part” and “rare slime part” are aliases for Slime Gel and Slime Core, not additional items. Bosses give five common units plus one guaranteed boss rare: Blackfang Pelt/Fang (30G/150G), Chimera Hide/Heart (30G/150G), Ambermaw Hide/Core (45G/225G), Crownstone Scale/Heart (65G/325G). These are tradable trophies; no baseline recovery or gear requires a unique defeated boss's material.

Ordinary raw-corpse reference value is three common-unit values; boss raw value is five common-unit values; neither includes an expected rare premium. Variants use their parent's raw reference value so processing is how their extra elite part is realised. Corpses themselves have no rolled market quality until processed.

**Frontier scaling:** author new species/material uses and higher gear recipes there; preserve the per-unit, identity and mutually exclusive tier contracts. Do not add Frontier monster names in this opening-act draft.

## 11. Contracts, requests and flashpoints — Designed, not yet proven

### 11.1 Request lifecycle — Designed, not yet proven

States are Hidden → Offered → Accepted → Completed, Expired or Failed. Offer-branch dialogue reveals an ID once; seeing it is not accepting it. Refusing before the offer branch leaves it Hidden, so a later conversation can reveal it. Timers begin on first appearance, including while Offered, and use calendar hours through nights. Show absolute deadline and remaining time before acceptance. A due delivery may complete at its deadline before expiry.

An ignored offer expires without penalty. Accepted timed expiry, voluntary abandonment, or failed optional subjugation costs 10 Reputation once; no Morale penalty. A failed no-deadline delivery does not arise merely from waiting. Main flashpoints use 11.4 instead. City offers CH1-REQ-003 through CH1-REQ-007 disappear at Chapter 1 end if still unaccepted; show a warning before concluding the chapter. CH1-REQ-001/002 use their own timers. Accepted requests survive chapter changes and relocation, subject to their remaining deadlines.

Reserve partial quantities, but complete the entire order atomically for its full reward. Show owned/listed/reserved/available counts and exact consumed units; choose lowest acceptable quality first. Never consume equipped or bound items. Before Jeb's courier benefit, HQ may reserve/escrow the goods but payment/completion requires a client visit. After the benefit, the board completes any eligible Eurydica delivery immediately. A client is always available through a request interaction while an accepted order is active, regardless of ambient NPC schedule. This access belongs to the request, not to a trader's visit schedule.

### 11.2 Seven Chapter 1 requests — Designed, not yet proven

These seven IDs replace the unindexed ten-delivery claim. Reward rules and clients are complete; final dialogue is content work.

| ID / display request / client | Quantity and quality | Gold / Rep | Deadline from appearance | Persistent result |
|---|---|---|---|---|
| CH1-REQ-001 / Bathroom / inn owner (`eur_inn_owner`) | 5 Slime Gel, any condition | 50 / 50 | 5 days | Bathroom aftermath flag; offer introduced at M02 |
| CH1-REQ-002 / Garden / noble household's garden steward (`eur_garden_steward`) | 2 Slime Cores, any condition | 100 / 50 | 4 days | Garden aftermath flag; offer introduced at M02; garden client, not inn owner |
| CH1-REQ-003 / Rare Slime Order / original trader client | 2 Slime Cores, any condition | 25 / 100 | 2 days | Order aftermath flag; request-owned exchange below |
| CH1-REQ-004 / Clinic / Dr. Emmerich | 10 Slime Gel, any condition | 100 / 20 | 6 days | Four potions per Guild week may be bought for 18G each; normal price after allotment |
| CH1-REQ-005 / Winter Bedding / Jeb | 3 Standard+ Wolf Pelts | 75 / 25 | None | Permanent free board courier for Eurydica clients |
| CH1-REQ-006 / Hilde's supply / Hilde | 4 Standard+ Boar Meat | 60 / 20 | None | Roast aftermath; enables EUR-WO-001 |
| CH1-REQ-007 / Keep the Old Ones Working / Gerd | 2 Standard+ Boar Hides | 40 / 20 | None | Repair aftermath; enables EUR-WO-002; shows Vest recipe |

Clinic allotments reset at the start of each Guild week (days 1, 8, 15…), never accumulate, and remain claimable from the potion counter at any base through the completed-request flag. Jeb's own first completion requires visiting him; later deliveries may use the board. No core mechanic waits for the original Rare Slime Order trader to revisit.

**Rare-core safeguards.** Accepting CH1-REQ-003 exposes a one-time alternative in that request's panel: 15 Slime Gel of any condition satisfy its two cores directly. No physical tradeable cores are issued. CH1-REQ-002 gains the same alternative when its final 24 hours begin and fewer than two cores have been obtained/reserved for it; acceptance during that window enables it immediately. Choosing the full gel alternative releases any core reservation. Each alternative consumes 15 gel once, is exclusive with ordinary core delivery, grants only the request's stated reward, and earns no sales Reputation. The request panel remains accessible at every base. Explain the alternative before acceptance; it removes rare-drop dependence, not the need to gather common goods.

Two Standard boar corpses yield four meat and two hides: enough for Hilde and Gerd together, paying 100G and 40 Rep initially. That competes with 36G generic walk-up value for the same six Standard common units, with gear and with the HQ upgrades. Rare parts/quality are extra, not assumed in that comparison.

| Repeat customer ID | Goods / reward | Availability |
|---|---|---|
| EUR-WO-001 / Hilde | 4 Standard+ Boar Meat / 60G + 5 Rep | First offer 7 calendar days after CH1-REQ-006 completion; then 7 days after each repeat completion |
| EUR-WO-002 / Gerd | 2 Standard+ Boar Hides / 40G + 5 Rep | First offer 7 calendar days after CH1-REQ-007 completion; then 7 days after each repeat completion |

One outstanding instance per customer, no countdown and no accumulated missed orders. A completed repeat returns 7 calendar days after completion; an **abandoned or failed** one returns 2 calendar days after it ends (owner, 2026-09-29). Show next appearance and quantities. Offers already accepted carry across relocation; pause future recurrence while Eurydica is not the operating base and resume its remaining wait only on resuming that base. Existing unaccepted Eurydica repeat offers are suspended there. Contacts and aftermath remain in the journal; they are not a separate relationship-XP ladder.

### 11.3 Optional subjugations — Designed, not yet proven

These eight specified encounters replace an unsupported “eight authored stories” claim. Their final scenes remain content work. Offers require M08 and the listed conditions. Each uses a 30-minute approach, then the same combat, with no hunt search/group/variant lottery. Approach is included in prep's estimated finish time; battle time is outcome-dependent. An accepted operation may run until victory, recall, wipe, its absolute deadline or 20:00.

Offers last 72 calendar hours from appearance; acceptance does not restart the clock. Ignore freely. Accepted failure costs 10 Rep once. Reoffer an unsuccessful contract 7 calendar days after expiry/failure; successful contracts never recur. Rewards, completion flag, normal corpse Reputation and kill/fight XP occur once, with no duplicated boss corpse or repeat reward. Corpse rewards already secured before failure remain.

| ID / client / problem | Eligibility | Fixed encounter | Gold / Rep | Ending flag premise |
|---|---|---|---|---|
| EUR-SUB-01 / inn owner / slime nuisance | F; first hunt returned | 2 Moss Slimes | 90 / 15 | Inn supply access cleared |
| EUR-SUB-02 / Gerd / damaged deliveries | F; boar known | 2 Dire Boars | 140 / 20 | Repair supplies delivered |
| EUR-SUB-03 / Jeb / stable road danger | F; wolf known | 2 Forest Wolves | 200 / 25 | Road warning removed |
| EUR-SUB-04 / South Gate guard / Blackfang attacks | E; wolf known; Chapter 2 or later | Blackfang Direwolf | 450 / 100 | Blackfang case closed, not the Chimera story flag |
| EUR-SUB-05 / Dr. Emmerich / marsh supplies blocked | E; Marsh Slime known | 2 Marsh Slimes | 260 / 30 | Clinic supply report resolved |
| EUR-SUB-06 / trade contact / pickup blocked | E; Serpent known | 2 Marsh Serpents | 320 / 35 | Pickup report resolved |
| EUR-SUB-07 / Gerd / unsafe quarry access | D; Crawler known | 2 Stone Crawlers | 420 / 40 | Quarry report resolved |
| EUR-SUB-08 / trade contact / high-road danger | D; Highland Wolf known | 2 Highland Wolves | 500 / 45 | Shipment route cleared |

Trade-contact roles retain their source client IDs but dispatch, turn-in and retries belong to the board, never an itinerant NPC's presence. Ending flags grant no unlisted economic bonus. Rewards use the stated baseline (Commander skills and officer perks can modify this; see section 5 and the Commander section).

### 11.4 Flashpoints — Designed, not yet proven

| Flashpoint | All required gates | Reward | Lasting aftermath |
|---|---|---|---|
| Hylaea Chimera — Chapter 2, first | Chapter 2 entered; E; 300 Rep | 900G + 250 Rep | Hylaea base scout injury becomes 0.5%; ordinary target share becomes 85% before den weighting |
| Ambermaw Blockade — Chapter 2, second | Chimera cleared; E; 800 Rep | 1,400G + 350 Rep | Marsh ordinary target share becomes 85% before den weighting |
| Crownstone Reckoning — Chapter 2, third | Ambermaw cleared; D; 1,400 Rep | 2,000G + 450 Rep | Erythra ordinary target share becomes 85% before den weighting |

Each target is a solo Elite boss with section 10 stats, a 30-minute approach and the standard combat model. Display named threats early with every unmet condition. Main-story offers never expire. Losing, recalling or reaching cutoff fails the attempt but costs no Reputation and leaves the offer available; retry when a party is ready. Reward and aftermath apply only on first victory. No respawn-farming reward, timed offer lockout, invented boss phase or hidden officer rescue. Story guests enter only through the explicit authored formation.

**Frontier scaling:** new contracts, residents and chapters use this lifecycle and request-owned safeguards. Crownstone's success brings the Alliance envoy (14), not the end of the campaign.

## 12. Economy — Designed, not yet proven

All money belongs to the Guild purse. Inventory reservations are authoritative and exclusive across listings, requests, recipes, equipment and building jobs. Preview spending against the next payroll bill. Base values below may be affected where applicable (Commander skills and officer perks can modify this; see section 5 and the Commander section).

### 12.1 Processing — Designed, not yet proven

**Work order (owner decision, 2026-09-28).**
- The Commander gives Mae one **processing work order**: an ordered list of corpses (up to 30).
- **Mae assigns the jobs herself.** Whenever a table and a processor are free, she hands the next corpse in the order to the **highest-rated free processor** (staff rank, then total productive hours).
- **No processor sits idle** while the work order still has corpses and a table is free. Mae covers a vacant table herself at fallback speed (12.6).
- One processor works one corpse at a time.
- The Commander can reorder, add or remove waiting corpses at any time. Removing the active job cancels it and returns the whole corpse.
- The screen shows each processor's current corpse and finish time, the order's estimated completion time, possible yields and quality chances. Eurydica storage is unlimited for materials/corpses; no spoilage or hidden overflow.

| Processing quality | Sale-value multiplier | Staff rank 1 chance | Rank 2 chance | Rank 3 chance |
|---|---|---|---|---|
| Pristine | 1.25 | 10% | 20% | 30% |
| Standard | 1.00 | 70% | 70% | 65% |
| Damaged | 0.50 | 15% | 8% | 5% |
| Unsellable | 0 | 5% | 2% | 0% |

One quality roll applies to the entire job. **How later modifiers meet the fixed roll:** the job stores one random number `u` when the corpse is first queued. The outcome is read from `u` against the job's **final odds table** at completion: the base odds of the first committed processor's rank, then any perk, then any Cutting Chart session bonus (Pristine taken from Standard). Modifiers change the table, never the draw, so reloading or reassigning can't reroll. Recipes and food requests require Standard or Pristine; explicit “any condition” requests can consume Unsellable. Guaranteed elite parts count at any quality for recipes that use them; quality affects their sale price, not that eligibility. No second gear-quality roll.

Persist quality and rare-roll results against the corpse ID when first queued, using its first committed processor rank. Cancellation, a new worker, cutoff or reload never rerolls the corpse. Refund reservations on cancellation/cutoff while retaining that identity. Other waiting jobs remain queued. At 07:00 valid queues resume automatically after checking assignments and inputs; held reservations cannot be sold in the meantime, while released inputs must be reacquired before restarting.

Duration = monster base time × staff duration factor × Morale factor, rounded up to ticks; snapshot factors at job start. The active job aborts at cutoff if incomplete, returning the whole corpse. A queued tomorrow job has no secretly banked overnight progress.

### 12.2 Equipment and recipes — Designed, not yet proven

Crafted gear adds flat stats to an adventurer's existing starter kit. Recipe cards are visible before the Workshop opens at Gerd's and Elsie's, with exact inputs, source links, fee, duration, footprint and result. One active weapon, armour and accessory; craft choices need no separate appearance per equipment piece in the first release. One craftsman/workbench processes one crafting or Reworking job at a time, up to 20 queued jobs. “Production focus” is a recipe-category filter, not free daily output.

| Output | Standard+ inputs and fee | Base time | Footprint / benefit |
|---|---|---|---|
| Route Map | 2 Wolf Pelts + 30G | 1 hour | 1×2 accessory; party search ×0.95; strongest only |
| Boarhide Vest | 4 Boar Hides + 40G | 2 hours | 2×2 armour; +30 max HP, +8 DEF |
| Balanced Blade/Hammer | 4 Slime Gel + 2 Boar Tusks + 50G | 2 hours | 1×3 weapon; +5 ATK for the matching melee kit |
| Hunter Bow | 3 Boar Hides + 1 Wolf Fang + 40G | 2 hours | 1×3 weapon; +4 ATK for Nell |
| Arrow Case | 2 Boar Hides + 15G | 1 hour | 1×2 accessory; adjacent bow gains +15% attack rate |
| Reed Ward | 4 Serpent Scales + 1 Marsh Core + 80G | 3 hours | 2×2 armour; +45 HP, +12 DEF |
| Ridge Edge | 4 Drake Scales + 1 Crawler Core + 120G | 3 hours | 1×3 weapon; +10 ATK; melee, bow or caster-focus form |

Each recipe yields one item. Blade/Hammer and Ridge forms are choices within one recipe, not multiplied outputs. Ridge bow counts as a bow for Arrow Case. If one person carries Arrow Case, they cannot also activate Route Map; another party member may carry the map. Crafting reserves inputs and fee at job start (12.2a; queued jobs are intentions without a material claim), supplies output on completion, and refunds both on cancellation/cutoff. A job never takes goods already reserved by a request, listing or another job. Output and completion flag commit together.

The Workshop crafts **gear only**; consumables are bought in Eurydica and researched in the Frontier (6.6a). Crafted gear is a sellable good with its own market demand (12.4).

### 12.2a Workshop work order — Designed, not yet proven

The Workshop uses the same model as Processing. The Commander gives Fulker one **workshop work order** that mixes crafting and Reworking jobs (12.8). Fulker assigns each job to the highest-rated free craftsman, covers a vacant bench herself at fallback speed, and never leaves a craftsman idle while jobs wait. Inputs are reserved when a job starts, not when it's queued.

### 12.3 Enhancement — Removed (owner, 2026-09-29)

The permanent-stat enhancement system and its Refinement material are removed. Adventurer power comes from the four tracks (6.2c), skills, equipment (12.2) and consumables for one expedition (6.6a). Refinement's role becomes the Demondrug line (6.6a). Elite parts keep their sale value and gain uses in higher-tier Frontier recipes. See `Consumables and Research Proposal.md`.

### 12.4 Commerce — Designed, not yet proven

| Rule | Starting value |
|---|---|
| Listing capacity by Reputation | 3 at 0; 5 at 200; 8 at 700; shelves add 2 |
| Listing stack | 1–99 units, positive whole-Gold unit price |
| Demand state probability | Low 25% / Normal 50% / High 25% |
| Demand price factor | 0.75 / 1 / 1.25 |
| Hourly buy probability | 25% / 50% / 75% |
| Hourly maximum units bought | 1 / 2 / 3 |
| Fee per executed sale | `max(1, ceil(gross × 0.05))` |

At 07:00 extend a persistent demand schedule covering today and the next three days (four with Deep Analysis), so every forecast reads generated demand (owner, 2026-09-29); never reroll already generated days. A market category is a sellable processed-material item ID, shared across qualities and listings; base ID also keys the independent local demand pool. Corpses use the generic walk-up channel, not hourly material demand. **Crafted gear is a market category too**, one per crafted item, with its own demand like a material; its base value is `floor((the recipe inputs' Standard base value + the craft fee) × 1.25)` (owner, 2026-09-29). Example: Boarhide Vest `(4 × 12 + 40) × 1.25 = 110G`, against 48G for its hides sold raw. Each category has one potential buyer at each whole hour 08:00–20:00. On a successful buy roll, consume up to that state's quota from cheapest eligible listings, then oldest, splitting stacks as needed. Willingness to pay is `base unit value × quality multiplier × demand factor`; overpricing gets no sale. Each filled listing is one executed sale for fees. Repricing/splitting/cancelling never creates another buyer or quota.

Reserve listed stock; unsold listings persist overnight. Unsellable quality cannot be listed. If capacity falls below current listings after a Reputation penalty, leave existing listings intact but block new listings until below capacity. Example: three Standard Boar Hides at 12G each produce 36G gross, 2G fee and 34G net. Standard category expected unit capacity, before prices/stock, is 3.25 / 13 / 29.25 units per day at Low/Normal/High; these are expectations from 13 checks, not guaranteed sales.

**Any-trader fallback:** available at every base with no visit schedule or volume limit. A processed unit pays `floor(0.5 × base × quality)`, no listing fee; Unsellable is not bought. Raw corpses pay half their section 10 reference value, floored. Crafted gear pays `floor(0.5 × its crafted base value)`. Purchased consumables resell for at most half their actual purchase price. Track origin/cost so refunds, clinic discounts and recipe choices cannot create a buy-sell loop.

Reputation from sales is one per 100G cumulative net market/walk-up receipts, with remainder retained; request cash and loans do not count. Net means after sale fees but before debt sweeps. Refunds are not new receipts. Reservations prevent accidental sale of a project, request or equipped item.

### 12.5 Information — Designed, not yet proven

| Clerk rank | Forecast horizon | Chance forecast is correct |
|---|---|---|
| 1 | 1 day ahead | 70% |
| 2 | 2 days ahead | 80% |
| 3 | 3 days ahead | 90% |

Forecast Low/Normal/High from the saved true demand; on an incorrect prediction choose one of the other two states uniformly. Save each category/day prediction on first delivery with its confidence; reopening, reassigning or promoting never rerolls it. Later dates can use the new rank. Show actual outcomes afterward. Before a named clerk, Liliana's vacant-station service gives one day ahead at 60% confidence.

Each morning show one uncompleted opportunity from discovered-region data: material use, customer or eligible landmark. Rumours are labelled unverified, reveal no exploration and create no random quests. Recipe sources are visible even before Liliana joins; her service improves timing and leads rather than withholding basic knowledge.

### 12.6 Employees and staff ranks — Designed, not yet proven

| Employee | Hire | Weekly base wage | Eligibility |
|---|---|---|---|
| Anselm | 250G | 90G | M02; first pair; free adventurer bed |
| Nell | 250G | 90G | M02; first pair; free adventurer bed |
| Severa | 300G | 105G | Visible at M02; free bed |
| Otto | 325G | 110G | Visible at M02; free bed |
| Chloris | 400G | 120G | Chapter 2, E, free bed |
| Konrad, processor | 150G | 60G | Preview at M02; free processing staff station (Tier 2) and free bed |
| Cassia, clerk | 150G | 60G | Liliana joined (after C1S7-1); free bed |
| Ulrich, craftsman | 200G | 75G | M05; free craftsman station (Tier 2) and free bed |

Authored candidates never vanish for being unaffordable; no random duplicates. Officers join through story for no hiring charge and have no separate payroll in this baseline. Routine staff are distinct from those officers; they use stations and sleep in the dormitory like the adventurers.

| Staff rank | Promotion condition and cost | Processing/crafting duration factor | Weekly wage factor |
|---|---|---|---|
| 1 | Starting rank | 1.00 | 1.00 |
| 2 | 40 total productive operating hours + 200G | 0.85 | 1.25 |
| 3 | Frontier reached; 100 total productive hours + 400G | 0.70 | 1.50 |

Productive hours credit completed processing, crafting and Reworking work only, using actual operating duration; cancellations/aborted work earn none. Cassia earns one productive hour per morning forecast service delivered, not per category or screen opening. Retain fractional hours, total across promotions, and round the displayed weekly rank wage up to whole gold. Rank-3 staff advancement is held for the Frontier to leave service growth after the opening. Traits without explicit mechanics remain descriptive.

Mae/Fulker/Liliana cover one vacant baseline station at twice base production time or the stated fallback forecast. This is the department's base recovery service, not a bond perk. Officers never double-work a station occupied by its employee. With a second table/bench, Konrad/Ulrich can run one and Mae/Fulker the other at fallback speed. No new anonymous worker is implied.

### 12.8 Reworking (Fulker's Workshop) *(new, owner decision 2026-09-28; designed, not yet proven)*

Fulker opens **Reworking** when she joins in Chapter 1. A craftsman combines lower-grade units of **one material** into a better one.

| Rework | Input | Output | Time |
|---|---|---|---|
| Mend | 2 Damaged | 1 Standard | 4 hours |
| Refine grade | 2 Standard | 1 Pristine | 4 hours |
| *Master's Salvage perk only* | 3 Damaged | 1 Pristine | 6 hours |

- Unsellable units can't be reworked.
- Jobs queue in the Workshop work order (12.2a). Their duration uses staff rank like other Workshop jobs; Morale does not apply (Morale affects processing only, 13.2). A cutoff returns their inputs.
- The perk *Rough Patch* halves the time but allows Mend only (up to Standard).

**Why it's worth doing:** in gold, Reworking breaks even at best (2 Damaged are worth 1 Standard) or loses value (2 Standard are worth more than 1 Pristine). Its value is **access**:
- Damaged stock becomes usable in recipes that need Standard or better.
- Pristine units supply **Pristine-only needs**: fine-goods requests, and the higher Frontier recipe tiers (16a).
- With Valerie's *Premium Seller*, Pristine sells for 1.56× base value.

This is the quality strategy's engine (5.4).

### 12.7 HQ capacity and construction — Designed, not yet proven

Start with **four dormitory beds** (owner, 2026-10-01) and service corners opened free by their story introductions. Every recruitable (adventurer or worker) needs a free bed; workers also need a free station. All Chapter 1 departments work from their corners immediately; Tier 2 moves processing and crafting into the Workshop and adds the second staff stations.

| Upgrade | Preview / prerequisite | Cost / calendar duration | Effect |
|---|---|---|---|
| Guild House Tier 2 | Objective C1S6-1 (Scene 6, the first Guild meeting) | 500G + 6 Standard+ Boar Hides / 48 hours | The annex: second officers' room (Fulker, Valerie, Liliana), the Workshop with 4 tables (2 processing: Mae + a staff station; 2 crafting: Fulker + a craftsman station), the Commerce + Information room; unlocks Dorm Expansion |
| Dorm Expansion | Guild House Tier 2 complete; objective C1S7-1 (Scene 7) | 300G + 8 Standard+ Wolf Pelts / 48 hours | Beds 4→8: room for the starter workers (processing, craftsman, information) and Chloris |
| Trading Shelves | Valerie joined | 300G + 4 Standard+ Boar Hides / 24 hours | +2 listing slots |

*(2026-10-01: Tier 2 and Dorm Expansion replace the Dorm Annex, Larger Dorm, Second Processing Table, Second Workbench and Officers' Quarters II. The sim's HQ upgrade data follows in a later sprint.)* Eight beds hold the five authored adventurers and the three starter workers; more belong to the Frontier. No implicit sixth adventurer. Four people can run a three-person hunt plus one scout, or two modest two-person hunts; two safe boar teams are not promised. Simultaneous operations have no extra slot currency.

One construction job at a time; consume quoted inputs at start, complete through calendar time including night, and refund fully on cancellation before completion. No duplicate upgrade or recurring upkeep. Apply capacity at the completion tick; update room visuals at the next safe transition. Optional HQ spending is blocked while debt is overdue, not ordinary income-producing dispatch/material processing.

**Frontier scaling:** higher gear tiers beyond Boarhide/Reed/Ridge, consumable tiers 2–5 from the Research Department, staff rank 3, more beds/workstations and a larger authored roster. Purchased capacities carry over; no second payment for the same beds. Retain honest local demand and request-owned benefits rather than a travelling-merchant dependency.

## 13. Closeout, payroll and Guild progression — Proven (screens); Designed, not yet proven (accounting)

### 13.1 Day Summary — Proven (layout); Designed, not yet proven (accounting)

At 20:00 after Resolution show revenue, expenses, operations, Reputation by source, Morale by cause, stamina before/after rest orders, injuries/readiness, notable finds and project completions. Show up to three player-pinned projects with quantities, gold shortfall, source and next action. Include accrued wages/reserve, debt principal/due date, and the next overnight recovery preview. The player may set an advisory Gold reserve; purchases warn if they cross it but are blocked only by actual funds or another explicit eligibility rule. Personal spending is a separate Commander accounting line supplied by the Commander section; no personal activity mechanics are defined here.

### 13.2 Weekly closeout and Morale — Designed, not yet proven

Payday is 20:00 on days 7, 14, 21 and every seventh day thereafter. Accrue wages per employed calendar day; employment before that day's cutoff counts once. Wages for partial weeks are not a whole week's charge. Each day contributes its applicable weekly rate/7, with difficulty applied to that day's accrual; round the final sum up to whole Gold once per employee at settlement. A staff promotion affects future accrual, not previously accrued days. Show the projected bill before any hire/promotion. During transfer, accrue/pay on the same calendar boundaries without also charging the day again at arrival.

If gold is short, pause for allocation of full employee balances. Unpaid people leave after returning gear; record their accrued unpaid wages once. No wages accrue while Left. Rehire pays arrears plus original hiring cost, preserving progress. Voluntary dismissal settles accrued wages; if unaffordable, retain that liability as arrears instead of erasing it. Payroll cash is not automatically spent on debt; the debt sweep applies to later positive receipts only. Weekly recruitment refresh only highlights newly story-eligible authored people; it never removes former staff.

| Guild Morale rule | Value |
|---|---|
| Start / range | 60 / 0–100 |
| Processing duration at Morale 0–29 / 30–49 / 50–79 / 80–100 | ×1.15 / ×1.05 / ×1.00 / ×0.90 |
| Successful operations day, no newly injured people | +1 once |
| Newly injured adventurers | −2 each, at most −6 per day |
| Unpaid employees at payroll | −5 each, at most −15 per payday |
| Fully paid nonzero weekly payroll | +3 |
| Idle recovery day, Morale below 60 | +1 |

A successful day requires at least one won hunt/contract fight or completed scout interval. Idle recovery means no expeditions and at least one employed adventurer resting or injured; it cannot also earn the successful-day bonus. Sum daily causes then clamp once. Morale changes only processing duration in this baseline, not quality, combat or wages. (Commander skills and officer perks can modify this; see section 5 and the Commander section).

Rest orders are daily decisions under 6.3; payroll cadence does not govern recovery. End each day with a preview of who can dispatch after sleep.

### 13.3 Guild Rank and Reputation — Carried over (F–C); Designed, not yet proven (full contract)

Start at 07:00 with 2,500G, 0 Reputation, 60 Morale and Guild Rank F. Reputation is standing, never a spendable currency and never below zero. Promotion charges gold only; a later Reputation loss does not demote the Guild or re-lock its areas.

| Promotion | Required Reputation | Gold charge | Unlock |
|---|---|---|---|
| F→E | 200 | 300G | Bernmoor; Chloris's rank gate |
| E→D | 700 | 700G | Erythra; 5×4 packs |
| D→C | 1,500 | 1,500G | The opening act's rank target (no longer a move condition; 16a) |
| C→B | 3,000 | 3,000G | Frontier only; 5×5 packs; higher facility/gear tier access |
| B→A | 6,000 | 6,000G | Frontier only; next facility/gear tier access |
| A→S | 12,000 | 12,000G | Frontier only; highest Guild standing/tier access |

B/A/S thresholds and fees continue the opening curve as unproven starting values; their specific content is authored in the Frontier, not available early. All promotions require the preceding rank and no overdue debt. Do not spend Reputation on promotion or silently grant gear/people just for a rank label. Listing slots and contract gates use current standing as specified; no universal Reputation price multiplier.

Gold/XP/Rep rewards are committed once with their event ID. Sources are hunt/contract corpses, successful scouts, completed requests/contracts/flashpoints, and cumulative net sales. An accepted optional failure debits 10 once; story failures do not. Refunds, exchanges and borrowing do not manufacture sales Reputation.

Starting-cash example: Anselm + Nell + Konrad cost 650G, leaving 1,850G. Four initial adventurers fill the four starting beds (1,125G). Workers need Tier 2 stations and the Dorm Expansion, so they come later. This is a warning to stage investment, not a claim that hiring everyone immediately is viable.

### 13.4 Debt and the Eurydica charter — Designed, not yet proven

**The Eurydica charter** is now the Alliance appointment (14, 16a; owner, 2026-09-29): it follows the Crownstone flashpoint, with no rank or debt condition. Debt still blocks the **departure** until it is repaid. There are no credits, forced stop or fixed day limit here.

| Recovery rule | Value |
|---|---|
| Emergency loan | 2,500G, no interest, due 7 calendar days after acceptance |
| Outstanding ordinary loan | At most one |
| On overdue principal | Block rank promotion and optional HQ purchases; sweep 25% of subsequent positive receipts after sale fees toward principal |
| Sweep rounding | Accumulate fractional Gold remainder; transfer whole Gold, capped at outstanding principal |

Offer the loan only when no employed adventurer can return to work without hiring/rehiring and no eligible candidate is affordable with existing accommodation. Resting/Injured people alone never satisfy that trigger. Cancel/refund outstanding optional purchase reservations before calculating the shortfall. Voluntary repayments are available at any time, capped at principal; repaying early has no fee. Sweep eligible receipts include market, generic trader and cash rewards, but exclude loans, rescue credit and refunds. Clear overdue restrictions when principal reaches zero.

If all adventurers are Left and debt is already outstanding, offer a disclosed rescue advance equal to the cheapest eligible adventurer's rehire shortfall. Apply it directly to that rehire, add it to principal, and give no cash windfall. Repeat only after a later unpaid payroll, not through voluntary dismissal or repeated clicks. Departures release beds. Mae's vacant-station processing and the any-trader fallback keep a route to income. No interest escalation, permanent character loss or default game over.

**Frontier scaling:** B/A/S, more capacity and a longer economy follow C; the purse, Reputation, Morale, payroll liabilities, customer flags and debt persist across bases.

## 14. Story gating — Designed, not yet proven

Services open through once-only event predicates, not fixed days or mandatory numeric milestone order. Preserve M02/M03/M05/M06/M08 IDs. Any new event key below describes a predicate for integration, not a rename of an existing saved ID. Record earned predicates immediately and play introductions at the next safe paused story interaction.

| Milestone / event | Predicate | Result |
|---|---|---|
| M02 | Chapter 1 arrival walk complete; returned to Tristitia for the 14:00 meeting; recruitment scene acknowledged | Anselm/Nell hiring, Severa/Otto preview; CH1-REQ-001/002 offers |
| M03 | M02; at least one hire; Elsie's dispatch explanation acknowledged | Hunting; Mae's baseline Processing opens alongside it |
| M06 | Opens with M03 (owner, 2026-09-30: Elsie suggests hunting and scouting together in Scene 5) | Scouting, from the first expedition; Scout Map fallback |
| First Guild meeting (Scene 6) | M02; the Guild reaches **400 Reputation** (owner, 2026-09-30); plays at 07:00 the next day | Objective C1S6-1: **Guild House Tier 2** can be bought (12.7) |
| M05 / Fulker joins (Scene 7) | Guild House Tier 2 built; plays at 07:00 the next day | Crafting officer joins; the Workshop works; objectives C1S7-1 (Dorm Expansion, talk to Fulker) and C1S7-2 (recruit a processor and a craftsman) |
| Valerie and Liliana join (Scene 8) | Fulker joined and C1S7-2 complete; plays at 07:00 the next day | Commerce and Information officers join together; the information staff member can be recruited; objectives C1S8-1 and C1S8-2 |
| M08 | First ordinary hunt fight won; Tristitia's contract explanation acknowledged | Optional contracts subject to individual gates |
| Service Lanes access | M02 completed; next free city exploration | Hilde/clinic request conversations accessible during Chapter 1 |
| Chapter 1 completion | Commerce, Crafting and Information officers joined; player elects chapter conclusion | Enter Chapter 2; review unaccepted local offers first |
| Ambermaw offer | Chimera cleared (Chapter 2); its scene acknowledged | Ambermaw flashpoint, subject to its rank/Rep gates |
| Crownstone offer | Ambermaw cleared (Chapter 2); its scene acknowledged | Crownstone flashpoint, subject to its rank/Rep gates |
| The envoy (end of Chapter 2) | 3 calendar days after the Crownstone flashpoint is cleared *(starting value)*; envoy scene acknowledged. No rank or debt condition | An Alliance envoy summons the Commander to the Civic Terrace |
| The Alliance appointment | Envoy scene complete; Civic Terrace meeting with the leaders of the nations acknowledged | The Alliance of Nations, impressed by the Guild, appoints it the **sole institution that verifies information** and charges it to open the Frontier. Verification authority starts now. The move unlocks |
| Chapter 3 departure | Appointment complete; move conditions in 16a met; player elects the day | Transfer to the Frontier; Chapter 3 begins on arrival |

*(Changed 2026-10-02 to follow the finished Chapter 1 manuscript, Scenes 6–8: the officers now join in a fixed order, Fulker first, then Valerie and Liliana together. This replaces the earlier boar-material, 400-Reputation and first-scout predicates.)* None of the three is drawn from recruitment, and none requires a bespoke request. Each Chapter 1 scene from 6 on plays at 07:00 on the day after its predicate first holds. The morning-only proof does not establish that all services operate on campaign Day 1. Chapter 1 previews Frontier reports lightly; verification authority is not granted early. The Alliance grants it at the Civic Terrace appointment at the end of Chapter 2 (owner, 2026-09-29); the physical relocation stays at the start of Chapter 3.

**Frontier scaling:** later chapters bind new content to persistent predicates, using the same once-only event/reward contract. Scenes and cast are content to author, not unspecified service logic.

## 15. Screens (HUD flow) — Proven (operations views); Designed, not yet proven (full build contracts)

Management screens pause, show the owning officer and return to their previous navigation context. HQ walking and shortcuts open the same screens. Preview does not mutate state; a labelled commit action revalidates money, inventory, person state and capacity atomically. Cancel returns uncommitted edits; committed-job refunds follow the corresponding system. Blocking conditions explain the exact next requirement, never a generic disabled button.

| Screen / owner | Minimum data and behaviour | Status |
|---|---|---|
| HUD cluster (top left) | Day, time, Guild purse, Reputation, Morale, Rank; orange from 19:00; speed controls and Battle pace chip. Grouped around a clock medallion in the top-left corner (FGC_08 §5.1; owner 2026-09-28), replacing the full-width top bar | Designed, not yet proven |
| Adventurer Office / Elsie | Event dialogue, New Expedition, Ongoing, Roster, Progression, Rest; show readiness and payroll exposure | Proven shell; new actions designed |
| Roster / Elsie | Name, portrait, fixed passive, reach, HP, four stamina bars, primary state and fatigue overlay; inspect/hire route/rest order | Proven shell; state details designed |
| Progression / Elsie | All four tracks, available/lifetime XP and campaign cap, every milestone, selected slots, interval ticks, stat deltas; batch Buy/Rebuild/Cancel | Designed, not yet proven |
| Region Map and Area Detail | Rank locks, field fog, counts, milestones, benefits, rare reservations, target odds, material-use links; Hunt/Scout/Contracts | Proven shell; source links designed |
| Hunt target cards | Stats, groups, Elite badges, processing output and raw-value labels; rare availability and relevant project links | Proven shell; reward labels designed |
| Preparation / Elsie | Two rows of three, at most five people, reach and passives, equipment grid, duration, return/cutoff, stamina before→after, risk/forecast, consumables; Dispatch/Cancel | Proven shell; validation designed |
| Ongoing Expeditions | Party, phase, times, progress/finds or corpses; Watch/View/Follow and immediate Recall; returned-today history | Proven |
| Field view | Live search/scout/battle state, log and notices; Leave/Recall; FRONT/BACK on every member; speed stays visible | Proven shell; labels corrected |
| Alerts | Info/success/warning/critical/rare, source event and timestamp; click opens the relevant object; deduplicate by event ID | Proven shell; persistence designed |
| HQ / Building Map | Current rooms, beds/stations, named waiting recruits, full quote, prerequisite and completion time; Preview/Build/Cancel | Designed, not yet proven |
| Request Board / Tristitia | Hidden excluded; Offered/Accepted/history, client, deadline, exact goods, owned/listed/reserved, full reward/benefit, exchange and courier access; Accept/Reserve/Deliver/Decline | Designed, not yet proven |
| Processing / Mae | Corpse ID, output/quality odds, worker, queue, finish time and cutoff warning; Queue/Reorder/Cancel | Designed, not yet proven |
| Workshop / Fulker | All recipe previews, sources, footprints, stats, queue, inputs/fee and finish; Reserve/Craft/Rework/Cancel | Designed, not yet proven |
| Information / Liliana | Dated forecasts/confidence, prior actual demand, known source links and unverified leads; inspect without reroll | Designed, not yet proven |
| Commerce / Valerie | Available/reserved stock, slots, price, demand, fee/net and debt-sweep preview, shared buyer explanation; List/Reprice/Withdraw/Walk-up sale | Designed, not yet proven |
| Recruitment / Elsie; staff department | Eligible named candidates and former staff, original hire/arrears, bed/station, coming bill; Hire/Rehire, no random refresh purchase | Designed, not yet proven |
| Payroll / Tristitia | Accrued amount by employee, purse/reserve, consequences; full Pay per employee and confirm unpaid departures | Designed, not yet proven |
| Rank / Tristitia | Exact standing, fee, previous rank, campaign/debt gate, unlock; Promote/Cancel | Designed, not yet proven |
| Flashpoint / Tristitia | Chapter/rank/Rep conditions, story formation, unique rewards/aftermath, retry rule; Prepare/Dispatch | Designed, not yet proven |
| 20:00 Resolution / Tristitia | All operation results and persistent jobs/injuries/targets, no missing interrupted actions; Continue to Summary | Proven layout; cutoff revised |
| Day Summary / Tristitia | Cash/Rep/Morale sources, payroll/rescue state, stamina/rest/sleep preview, events, three player pins; inspect/pin/unpin and proceed to night boundary | Proven layout; accounting/pins designed |
| Frontier transfer / Tristitia | 1,500G quote, capacities/persons/items transferred, payroll schedule, suspended request clocks and arrival time; Confirm/Cancel before transfer | Designed, not yet proven |
| Save/load/settings | Profile/slot/version/time, backup recovery, difficulty's next-day effect, readable scale and VFX controls; Save/Load/Cancel | Designed, not yet proven |

Elsie's preparation screen can save two named formation/loadout templates. Applying one shows absent people, missing items and fatigue; it never substitutes a person automatically and still requires dispatch confirmation. All command commits and repeated UI clicks are idempotent by action/event ID. Display arithmetic uses the same rules as the authoritative model. Reduced shake/flash and optional cinematic zoom affect presentation only. Commander's personal activities, bonds and minigames are outside these screen contracts.

**Frontier scaling:** region/base IDs, larger rosters, rank/gear previews and saved projects extend these screens; do not build a second incompatible UI or silently simulate remote trade.

## 16. Production notes

- **Proof pipeline:** a three.js page per proof, published as a private artifact. Each proof has a check ledger (`GATES-*.md`) with automated checks in headless Chrome.
- **Godot target:** a **new HD-2D Godot project and repository, started from a clean state** (owner decision, 2026-09-27). The owner creates them.
  - `D:\Godot Projects\imc-playground` (shared with Haris Munandar and Reza Chrisna) stays as the reference to port from, per Codex's audit (`D:/Codex/IMC/runs/playground-audit/report.md`).
  - **Port:** the verified dialogue text and IDs, the request definitions, the save envelope (checksums, atomic writes, backups), the testing techniques, and the actor collision and spawn-marker conventions.
  - **Don't port:** the 3D models and pose code, the old city scene, the old post-processing, or `game.gd` as a whole.
- **Codex helper:** heavy batch jobs and drafts run on Codex in `D:\Codex\IMC`; only checked results are copied into the project.
- **Next proof (5): a Chapter 1 economy slice.** It proves the "tomorrow I want to" hooks and balances this document's starting values:
  - two recruits, the seven requests and the two repeat customers;
  - recipes, processing and Guild House Tier 2;
  - the 07:00–20:00 day and the night;
  - one working session of each kind.

---

## 16a. Campaign structure and the Frontier — Designed, not yet proven

Eurydica, Chapters 1–2, is the short opening act (owner decision, 2026-09-28: Chapter 1 recruits the officers; Chapter 2 holds all three flashpoints: Chimera, then Ambermaw, then Crownstone). Its target is the first complete Guild routine: adventurers' strongest tracks around 5–6, Guild Rank C, and a first crafted set from Boarhide, Reed and Ridge tiers. The Frontier, Chapter 3 onward, is the main body. Advancing the story never requires exhausting all opening side requests, charting every area or reaching an XP cap.

**The move is story-driven** (owner, 2026-09-29). A few days after the Crownstone flashpoint (3 calendar days, a starting value), an Alliance envoy summons the Commander to Eurydica's Civic Terrace. There the leaders of the nations, impressed by the Guild, appoint it the sole institution that verifies information and charge it with opening the Frontier. Rank C stays the opening act's target, not a gate. Chapter 2 ends with that appointment, not a fourth flashpoint. After it, the player chooses the day to leave; there is no calendar deadline.

| Transfer rule | Contract |
|---|---|
| Price / duration | Paid by the Alliance (no fee) / 48 calendar hours; arrival time is departure time plus 48 hours |
| Preconditions | Alliance appointment complete, no current debt; no active expedition or construction job |
| Before confirmation | Finish/recall expeditions; finish/cancel construction; settle/cancel production and refund unfinished inputs/fees; cancel listings and return stock; show payroll dates/amounts during travel |
| Payroll | Calendar days and payroll boundaries advance; pause transfer for ordinary payroll allocation if necessary; no guaranteed paid wages hidden in the fee |
| Request timers | Accepted timed deliveries freeze with their exact remaining hours for transfer only; resume at arrival; no automatic success or extra reward |
| Other clocks | Injury and debt advance; two crossed nights give one sleep bar each to employed adventurers, capped at four; no automatic rest-day order or transfer rest bonus |
| Local operations | No hunts, scout intervals, production, buyers or new local recurring offers during transfer |
| Carryover | Purse after expenses, Reputation, Morale, rank, employees/former staff, accrued wages/arrears, XP/builds, gear, consumables, inventory, requests/contacts and story/discovery flags |
| HQ at arrival | Carry purchased bed/station/listing capacity; same operational services; never sell the same capacity again |

Expeditions must resolve before departure; accepted optional combat contracts not attempted keep their deadlines and can expire normally. Unaccepted timed offers also continue to expire. The confirmation identifies them separately from protected accepted deliveries. Accepted Eurydica deliveries remain fulfillable through a relocation courier in their request panel, even without Jeb's local unlock; it is transfer protection, not a new remote market. Pause local recurring-customer timers as specified in 11.2. During transfer, heal healthy people by elapsed idle hours and process injury expiry exactly; no simulated successful-operation or idle-rest Morale bonuses. Actual payroll effects still apply. Show any transfer ledger changes on arrival. Resume paused at the arrival clock time; no second night credit.

The first Frontier area opens at 0% exploration with the same three ordinary species, three landmarks and two paths, plus one initial rare lead available to discover. Its names, monsters and scenes are content to author, not placeholders promoted to canon. Initial scouting risk is 2% per half-hour, no death; local hunts/scouts remain at most three hours. Once a path is discovered and one hunt successfully returns from its selected route, set its surveyed-route flag. The path's −5-minute search benefit applies once, never again for verification; use the existing search floor. The new-area route data can distinguish resource-rich and safer paths. The Guild already holds verification authority on arrival, so a surveyed route can be recorded as **Guild Verified**.

Each base has its own demand pool. Eurydica exploration, discoveries, characters and contacts stay in the save/journal, but the inactive base produces nothing and makes no automatic sales. This is not a second autonomous HQ or caravan simulation. Transfer consumes no one and resets no progression. Ordinary manual saves remain available during transfer checkpoints, including payroll.

**Frontier scaling list:**

| System | Opening limit | Frontier extension |
|---|---|---|
| Adventurer progression | Track ≤6; lifetime XP ≤3,000 | Track ≤10; lifetime XP ≤12,000; rank-2 milestones at 8 |
| Guild Rank | F–C | B/A/S thresholds and fees in 13.3 |
| Equipment and consumables | First Boarhide/Reed/Ridge set; tier-1 consumables (bought) | Higher authored gear tiers; consumable tiers 1–5 from the Research Department; elite-part recipes |
| Capacity and people | 2→4→5 beds; five authored adventurers | Additional beds, larger authored roster and new kits; purchased beds persist |
| Staff | Ranks 1–2 | Rank 3, retained productive hours and promotions |
| Backpack | Up to 5×4 | 5×5 at B/A/S |
| Regions and information | Three Eurydica areas, local forecasts | New independent areas/routes, material sources, demand pools and authored leads |
| Requests and story | Seven Chapter 1 deliveries, two customers, eight optional encounters, three flashpoints | New local clients, contracts, chapter scenes and later goals under the same state machine |
| Saves and accounting | Single active base, persistent identity | Relocation and later content migrations without resetting people, projects or liabilities |

Exact higher-tier gear recipes, additional bed packages and later rank reward content belong in Frontier content tables; the gates and persistence rules above are settled design. No Frontier place, monster or cast is invented here.

### 16a.1 Region tags *(owner decision 2026-09-28)*

**Tagging:** every monster, material, recipe, request, repeat order, customer, rumour source, forecast category and negotiation item carries a **region tag**: `eurydica`, or its Frontier area.

**After the move to the Frontier, generators use only content tagged for the active base.** That covers:
- new requests and repeat orders;
- rumours and leads;
- market forecasts;
- negotiation orders and Standing offers;
- the day's hints.

No new content refers to Eurydica monsters or materials again.

**What the tag doesn't touch:**
- Eurydica stock already in storage can still be sold to the any-trader fallback, used in any recipe that accepts it, or delivered on orders **accepted before the move** (the transfer contract above).
- It never appears in a Frontier market listing or forecast.
- The journal keeps the Eurydica record.

## 16b. Saves and difficulty — Designed, not yet proven

| Save rule | Contract |
|---|---|
| Profiles | 3 campaign profiles |
| Manual saves | Unlimited named saves within each profile |
| Autosaves | 3 rotating slots per profile |
| Autosave triggers | New day, before payroll, before flashpoint dispatch, before/after chapter transition and relocation |
| File integrity | Schema version + content revision; atomic replace; last-good backup |
| Resume | Paused; no real-world offline progression |

Persist clock/day and night-credit flags, difficulty/pending changes, per-operation seeds/streams, gauges/queue/in-flight action end, meters/status counters, corpse identity/rolls, exploration/finds/rare reservations, inventory/reservations, listing/demand/forecast state, construction and queues, wages/arrears/debt, lifetime/spendable XP, rest orders/dispatch history, requests/appearance/deadlines/exchanges/recurrence, and once-only story/reward/project flags. Include transfer phase and protected deadline remainders. Saving is allowed in management, world and combat; authored cutscenes save their current safe scene checkpoint. Reload never rerolls rewards or replays a committed payout. Migrations preserve internal IDs; invalid reservations return inputs safely with a notice rather than deleting stock. Keep legacy text tokens as internal data where necessary while rendering Guild terminology.

| Mode | Combat, loot and market | Injury duration | Employee wage accrual | Timed request/optional-offer duration |
|---|---|---|---|---|
| Standard | Baseline | 48 hours | ×1.00 | Baseline |
| Relaxed | Same stats, RNG and drops | 24 hours | ×0.75 | ×2 when created |

Difficulty changes take effect at the next 07:00 boundary. Apply to new injury timers, newly appearing deadlines and future wage accrual only. Never repeatedly extend existing deadlines or alter an existing injury by toggling modes. Quest safeguards trigger by remaining calendar hours. Recurrence intervals, construction, payroll dates, transfer time, debt due dates, stamina and no-deadline orders do not change. Round final wage bills once per employee as in 13.2. No permadeath mode. Font/UI scale, reduced VFX, battle pace and speed controls are independent settings, with the same danger explanations in either mode.

**Frontier scaling:** retain profiles and state contracts through all chapters and content revisions; modes remain consistent across bases.

## 17. Open questions — Designed, not yet proven (content-authoring backlog only)

1. Author the Frontier's named areas, route descriptions, landmarks and material-source text using the settled area schema.
2. Author Frontier ordinary monsters, rares, bosses, higher gear recipes and later capacity rewards within the settled progression gates.
3. Author the additional Frontier adventurers, residents and supporting cast, their identities, kits, portraits, sprites and dialogue.
4. Write the Chapter 1 officer introductions and request aftermath, the eight optional contract scenes, Chapter 2's three flashpoint arcs and transition beat, and Chapter 3 onward's arrival, authority and later campaign scenes.
5. Complete the remaining Eurydica character and monster visual content for the fixed roster and kit: Anselm/Nell first, then Severa/Otto; Moss Slime/Forest Wolf, then Chimera/Blackfang and later-area creatures. These are production assets, not unresolved recruitment, weapon, camera or progression decisions.

No unresolved numeric system rule is parked here. Balance values throughout remain starting values for an integrated proof; that validation status is not an unanswered design question.

### Ideas saved for later
- **Recolourable recruits:** a few simple adventurer sprite bodies, each with 1–5 colour templates the player picks when recruiting. This would allow more recruits without drawing each one. It is more work, so it is parked for now; hand-designed adventurers stay the rule.

---

## 18. Change log

| Date | Change |
|---|---|
| 2026-09-29 | **The move to the Frontier is story-driven** (14, 16a): 3 days after Crownstone an Alliance envoy summons the Commander to the Civic Terrace; the Alliance of Nations appoints the Guild the sole institution that verifies information and pays for the move (no 1,500G fee). Verification authority starts at the appointment. Rank C is no longer a gate; the player still picks the departure day and must have no debt. |
| 2026-09-29 | **Bonds are capped at level 1 in Eurydica** (5.4); banked points carry over to the Frontier under the weekly limit. |
| 2026-10-01 | **Standing orders** (9.3a2): one rule per adventurer for when the signature skill fires; hunts stay automatic. Flashpoints played by hand (Grandia 3-style timeline with movement) and a reusable weather system are agreed for later (`Game Design/To-Do (Later).md`). |
| 2026-10-01 | **Eurydica HQ per Scene 6** (owner): Tier 1 (main room with meeting table and Mae's processing corner, Commander's room = office, shared officers' room, Elsie in the courtyard, **dormitory for 4 staff from the start**) and **Guild House Tier 2** (C1S6-1; 1,000G + 6 Standard+ Boar Hides / 48 h: officers' room II, a 4-table Workshop for processing and crafting, one Commerce + Information room), then **Dorm Expansion 4→8**. Staff (recruitables) sleep in the dorm. Per-officer department rooms and the HQ kitchen are Frontier content. Replaces Dorm Annex, Larger Dorm, Second Processing Table, Second Workbench and Officers' Quarters II. **Environment style:** pixel art (Proof 1), §2.4. |
| 2026-10-02 | **Battle HUD** (§9.4, owner): Kingdom Hearts-style round party gauges (thick HP arc, thin skill arc, name under the gauge, no HP number or FRONT/BACK) replace the card column; a Grandia 3-style timeline ring (party inner, enemies outer, ACT section, NEXT hub) replaces "no turn-order bar"; the battle log becomes a top-left button whose centred window pauses game time. Art: `UI Kit/Approved Battle v1/`. |
| 2026-10-02 | **HQ upgrade costs lowered** (§12.7, owner, Scene 8 note): the Trading Post isn't open yet when they come due, so Guild House Tier 2 drops from 1,000G to **500G** (+ 6 Standard+ Boar Hides) and the Dorm Expansion from 1,000G to **300G** (+ 8 Standard+ Wolf Pelts). The Dorm Expansion is objective C1S7-1 (Scene 7). |
| 2026-10-02 | **Story gating follows the finished manuscript** (§14): 400 Reputation now starts the first Guild meeting (Scene 6, Tier 2 objective). Fulker joins after Tier 2 is built (Scene 7). Valerie and Liliana join together after Fulker's staff objective (Scene 8). Each scene plays at 07:00 the next day. |
| 2026-09-29 | Owner decisions after S2: **enhancement removed** (12.3; Refinement becomes the Demondrug line); **consumables** made a heavy expedition requirement, tier 1 bought in Eurydica (new 6.6a: Potion, Demondrug, Armorskin, Lure, Map), tiers 1–5 from a Frontier Research Department; the Workshop crafts gear only; **crafted gear** gets market demand per item at (inputs + fee) × 1.25; abandoned or failed repeats return after 2 days; the demand schedule covers today + 3 days; the Negotiation gold bonus rounds down. |
| 2026-09-28 | UI finish locked from style test v5 (owner): fonts Cormorant Garamond SemiBold + Alegreya with lining figures, all-caps card headers; the 2.5 colour tokens stay (parchment and navy); the FGC_08 §2.2 tier and layer model; the owner's watermark emblem. |
| 2026-09-28 | UI decisions from FGC_08 (owner): the top bar becomes a top-left HUD cluster around a clock medallion (§15); the battle HUD party row becomes a semi-transparent card column on the right, and the battle log moves to the bottom left (§9). Processing odds stay visible as §12.1/§15 say, so the rank-3 Know-how ability **Trained eye** becomes a passive: processing never produces Unsellable, and that chance moves to Damaged (§5a.2, §5.4 perk arithmetic). |
| 2026-09-28 | Officers' full names recorded: Tristitia Fidei, Elsie Rodger, Mae Tanner, Sigrid Fulker (nameplate Fulker), Liliana Kessel, Valerie Kaufmann. The buyer Florian Zell is renamed **Dietrich Vogt**. |
| 2026-09-28 | The **clock tower** moves to the centre of the Civic Terrace as the north-bank landmark. It rings at 09:00, 12:00, 15:00 and 18:00 outdoors in Eurydica (4.3). |
| 2026-09-28 | **Names replaced** (owner-approved; see `Naming Guide.md`). Older change-log rows were renamed too.
- **Adventurers:** Anselm Voigt, Nell Larkin, Severa Kaltenbach, Otto Grimbald.
- **Staff:** Konrad Metzler, Cassia Susurra, Ulrich Esser. **First mage:** Chloris Linde.
- **NPCs:** Jeb (stables), Hilde (food shop), Gerd (Repair & Supply), Dr. Emmerich (clinic).
- **Buyers:** Dietrich Vogt, Reinhold Eisenmann, Lady Isabeau de Chamerolles (House Chamerolles), Captain Josie Harlan.
- **Regions:** Hylaea Forest, Bernmoor, Erythra Highlands.

Internal IDs are unchanged. |
| 2026-09-28 | **Otto redesign:**
- Full plate armour, a closed helmet and a two-handed warhammer, with no shield and no later shield outfit.
- His passive **Ironclad** (+20% DEF in the front row, immune to stun) replaces Shieldbearer.
- His traits are now Unshakable and Heavy-handed.
- His skill is renamed **Hammerfall**, with the same effect.
- **Facade finish decided:** storybook walls (style-test A) with detailed-texture roofs (B). |
| 2026-09-28 | **District swap:**
- The Guild house district moves beside the South Gate and is renamed **Guild Edge** (was Company Edge).
- The lodging house and cart yard move to the old spot between the gate and the Market Spine, keeping the name Arrival Ward.
- Jeb's stables and the guard shelter stay at the gate.
- The arrival route is now Outskirts → South Gate → Guild Edge → Arrival Ward → Market Spine.

**Rooms:** the Tier 1 Guild house has one shared officers' room (Tristitia, Mae, Elsie) from the start. *(Superseded 2026-10-01: the second officers' room comes with Guild House Tier 2, §5.1 and §12.7.)* Roof colours are a guide by building group: green for businesses and public buildings, plum for homes, brown for work buildings, warm red for Service Lanes and old homes, and **slate blue for the Guild only** (the Guild hall and its Tier 2 annex; owner 2026-10-01, so the Guild reads as its own landmark). |
| 2026-09-28 | Fixes from the implementation-spec review:
- **Workshop inputs** are reserved when a job starts (12.2 matches 12.2a).
- **Reworking** ignores Morale (Morale is processing only).
- **Perk arithmetic** is defined (faster means duration × (1 − X); relative Pristine is taken from Standard).
- **Bond points** have starting values: talk or meal +1, sessions by grade, levels at 5/12/20/30/42.
- **The fixed quality roll** is read against the final odds table at completion.
- **Minigame tuning numbers** come from the M3 prototypes. |
| 2026-09-28 | **Eurydica is 2 chapters.** Chapter 1 recruits the officers. Chapter 2 holds all three flashpoints in order (Chimera, Ambermaw, Crownstone) and ends with the transition beat. The Frontier starts at Chapter 3 (the move). Guild Verified authority comes in a later Frontier chapter. Scene scripts follow `Game Design/Scene Script Format.md`. |
| 2026-09-28 | Every monster has **one skill**, fired through the attacker meter on every fifth action, with a skill budget by tier (9.3b). Ordinary monsters get a Skill still. Monster candidates are made in `D:/Codex/IMC/<Monster>/`, and only approved stills go to `Enemy Sprites/`. |
| 2026-09-28 | **v2.1.1.** Processing and the Workshop use **work orders**: Mae and Fulker assign jobs to the highest-rated free worker, with no idle workers (12.1, 12.2a). New **Reworking** mechanic at Fulker's Workshop (12.8). Bond 5 perks revised (Valerie, Elsie, Fulker's Rough Patch / Master's Salvage) and visible in officer profiles from the start (5.4). Valerie's session is a daily **negotiation order** drawn from storage, with the buyer roster in `Characters/Negotiation Buyers Roster.md`. Cross-check credits Papers, Please. **Region tags** (16a.1). Dialogue staging approved (2.6). Fulker is a woman. |
| 2026-09-27 | **v2.1.** Renamed Frontier Guild Chronicle; "Guild" in player-facing text. Operations run 07:00–20:00, then night and sleep (4.2). Stamina: +1 overnight, a rest order restores it fully. The Commander has skills grown through officer working sessions (5a) and hunger as a status. Officer bonds end in one permanent trade-off perk at Bond 5 (5.4). Romance lives in the Frontier and excludes officers (5b). The chimera is the Chapter 2 flashpoint; all three officers join in Chapter 1; Rank C is the "Eurydica charter", not victory. The Codex audit's economy is adopted as starting values: materials, recipes, market, staff, HQ, requests, saves and difficulty. The "Tomorrow I want to" hooks are added. The Frontier is the main body (16a). Dialogue staging decided (2.6). The Godot target is a new clean project (16). |
| 2026-09-27 | Proof 4 version 3: facades approved, camera locked straight north, HD-2D building workflow added to the environment skill. |
| 2026-09-27 | Proof 4 version 2: Codex-painted facades, curved roofs, arched gatehouse, painted props; camera heading left open for the owner. |
| 2026-09-27 | Proof 4 built and published: explorable Eurydica grey-box (Chapter 1 Scene 3). The town camera and cutaway are decided. Town dialogue follows the manuscript, and requests unlock only on the offer branch. |
| 2026-09-27 | v2.0 created from the v1.1 GDD and the balance sheet. Added: HD-2D direction, four-direction sprites, battle presentation and party HUD, battle pace, 1–3 monster groups, scouting finds, landmarks, hidden paths, rare targets, scout risk, field view and search walk, region knowledge and field map. Scouting slowed from 5% to 2% per half-hour. |
| 2026-09-27 | Elsie decided: longsword with Yoshimitsu-like kicks and punches; her skill becomes Hateful Slash (provoke). Severa takes the greatsword (shorter than full body length) and her specialty becomes Warden. |
| 2026-09-27 | Elsie's greatsword dropped; her weapon is either the spear and short sword or a longsword with Yoshimitsu-like mixed fighting (recommended). |
| 2026-09-27 | Turns: one fighter acts at a time through a readiness queue; attacks take 24 company seconds and skills 72, with a push-in cinematic and a banner for skills. |
| 2026-09-27 | Environment style decided: painted (briefs updated to skip the 8×8 snap). Near trunks scroll with the walk and frame each fight. Proof 4 plan agreed (scope, camera, building method, story fixes). Roster of the starting adventurers and staff written: `Characters/Adventurers and Staff Roster.md`. |
| 2026-09-27 | Denser Hylaea assembly after the owner's concept (tree line, framing trunks, near foreground band); a pixel-art / painted switch in the proof; the region briefs revised for pixel density, density and two new sheets. |
| 2026-09-27 | The approved Hylaea environment set replaces the placeholder clearing in the field view (hunt search walk, battles, scout walk). |
| 2026-09-27 | Balance: group chances raised (slime 60%, boar 45%, wolf 70%); monster HP ×3 and ATK ×0.7 in every area, chosen by simulation (fights about 3× longer, 3× more skills, no wipes for a normal party); kill experience is a fixed value per monster. |
| 2026-09-27 | The operations proof now has the skill meter, the four signature skills, variants (8%, the rust boar recolour for the Dire Boar) and experience earning. Drafted milestone modifiers for Severa, Anselm and Otto, the experience numbers (100 × level costs, 12,000 cap), and Chloris as the proposed first mage (Verdant Blessing). |
| 2026-09-27 | Signature skills: Diving Splitter (Severa), Phalanx (Anselm), Frost Arrow (Nell), Shield Slam (Otto). Progression: four tracks (Power, Toughness, Speed, Focus) bought with experience at rising cost, BattleTech style; level 5 and 8 milestones modify the signature skill, with at most two rank 1 and one rank 2 modifiers per adventurer. Replaces v1.1's skill points. |
| 2026-09-27 | Skill meter under the HP bar, filled by role (attackers by hitting, defenders by being hit, mages over time). Variants: bigger and recoloured, HP ×1.5, ATK/DEF ×1.25, 8% per monster, better experience, variant corpses with a small elite-part library. |
| 2026-09-27 | Monster tiers: Ordinary, or Elite (rare, variant, boss); Big Game Hunter applies to all Elites. Support adventurers are mage types in the back row with heal, buff, debuff or attack skills. |
| 2026-09-27 | Otto keeps Shieldbearer (future shield and one-handed hammer build). Unpaid wages: the staff member leaves but can always be rehired as Former staff for unpaid wages + original hiring cost; the emergency loan trigger is reworded. |
| 2026-09-27 | Front and back rows (3 + 3 slots, up to 5, at least 1 in front), enemies spread over the front row, melee in the back −50%; the operations proof now uses the real starters and their passives. |
| 2026-09-27 | Nobody is permanently lost: no death, no quitting over wages (6.4a). Passives: Shieldbearer (Anselm, Otto), Big Game Hunter (Severa); monster tiers added. Scout risk tuning deferred until Hylaea is complete; its death column removed. Recolourable recruits saved as a later idea. |
