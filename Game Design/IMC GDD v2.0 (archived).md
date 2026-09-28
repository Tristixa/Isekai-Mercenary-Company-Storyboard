# Isekai Mercenary Company: Game Design Document

**Version:** 2.0 (HD-2D), started 2026-09-27
**Status:** the single source of truth for game design. It replaces the old 2D GDD (`D:\Godot Projects\IMC-godot\IMC_Reworked_GDD_HUD_Aligned_v1.1.md`) and its balance sheet (`data/BALANCE.md`) for every topic it covers.

## How this document works

- The old GDD and balance sheet were the starting material. Wherever a proof or a decision by the owner changed something, this document wins, and the change is marked **Changed from v1.1** with the reason.
- Each section has a status:
  - **Proven**: built and checked in a playable proof (link given).
  - **Carried over**: taken from v1.1 and still believed right, but not yet proven in HD-2D.
  - **Open**: a decision still to make (collected in section 17).
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
- **Scope:** the first playable slice, played as Chapter 1 Scene 3. It covers South Gate and Arrival Ward (stables, Hollis), Company Edge (HQ exterior and yard) and the southern Market Spine (tavern, red-tree plaza, Repair & Supply with Beren, the travelling merchant), with a view toward the Old Bridge. The objective is "return to Tristitia by 14:00". Service Lanes (Dr. Ginger, Marta) is visible but closed.
- **Camera:** Octopath-style town camera. Perspective, about 35–40° down, following the Commander, no rotation, tilt-shift depth of field.
- **Buildings:** simple 3D volumes wearing painted facade and roof textures, made per building by Codex from the approved concepts. Codex uses the `$imc-environment-art-direction` skill (`D:/Godot Projects/IMC-Companion-Skill-Environment`), the same one that made Mosswood. The proof starts with plain blocks in the district roof colours to settle camera, scale, walking, collisions, talking and the market.
- **Story fixes:** the Mosswood road leaves by the South Gate; the HQ grows (5.1); the story bible's "guild presence" line is dropped.
- **Results:**
  - **Camera:** 40° down at about 28 m, FOV 30. At that distance a 1.68 m sprite is about 93 px on a 1280×800 view, close to its native pixel size.
  - **Cutaway:** buildings between the camera and the Commander (or nearby people) fade to 22%, Octopath-style. This is needed because the camera faces north and the south wall and gate sit between it and the player.
  - **Walking and time:** walking speed is 3.2 m/s. The day clock runs at 120 company seconds per real second and stops in dialogue and the shop.
  - **Dialogue:** lines are verbatim from the manuscript, extracted by Codex with nested choices. A request is noted only on the offer branch (Hollis: Winter Bedding; Beren: Keep the Old Ones Working; the merchant: Rare Slime Order). `<name>` and `<Guild-name>` are shown as "Commander" and "the Company" until those names are decided.
  - **Placeholders:** townspeople without sprites use grey stand-ins with a "?" portrait card.
  - **Deferred:** evening and night NPCs (the Lady in a Red Dress, the Lady in a Green Dress and others) wait for a time-of-day pass.
- **Painted facades (version 2):** Codex painted orthographic elevation textures at 64 px/m for 11 buildings (44 faces), using the approved Eurydica concepts for design and its tavern sheet as the style anchor. It also painted 4 roof tiles, the city wall, awnings and 12 props. They are UV-mapped onto the 3D volumes under curved, flared roofs, and lighting comes from the engine. The textures and props are candidates awaiting the owner's review.
- **Camera decided (2026-09-27):** straight north. The facades were approved and moved to `Environment Assets/Eurydica/Approved Facades v1/`. The workflow is now part of `$imc-environment-art-direction` (`references/hd2d-buildings.md`).
- **Next:** sprites for Hollis, Beren and the merchant; the merchant stall as a painted prop.

The proof sources, build tools and check scripts live in `HD-2D Proof/` (`src/`, `tools/`, `GATES-*.md`).

---

## 1. Vision

IMC is a fantasy company-management RPG. The player is the **Company Commander**, not the hero in the fight. They build a mercenary company by hiring and preparing adventurers, sending expeditions, processing monster corpses, selling materials, paying wages, upgrading facilities and surviving long-term pressure.

**Core fantasy:** run a living adventurer company where information, logistics, preparation, timing and people matter as much as combat.

**Pillars**
- **Management first.** The player decides; combat resolves itself.
- **Adventurers matter.** They are persistent people with stamina, condition, gear and risk.
- **Character appeal is core.** Officers, adventurers and NPCs must be memorable enough to have favourites (adult-coded, distinct silhouettes, consistent across portrait and sprite).
- **Information creates profit.** Scouting, forecasts and rumours create an edge.
- **Parallel simulation.** Many operations run while company time moves.
- **Beautiful HD-2D.** Premium, alive and readable, never a rough mockup.
- **Watchable operations** *(new)*. Every expedition can be watched as it happens, but watching never changes the outcome.

---

## 2. Visual direction (HD-2D) - Proven (proofs 1 and 2)

**Changed from v1.1:** the game moved from 2D, briefly through 3D, to HD-2D in the style of Octopath Traveler (decided 2026-09-25). All 3D and Blender work is retired.

### 2.1 Look
- Pixel-art sprites standing in a lit 3D scene: real lights and shadows, depth of field with tilt-shift, bloom, and a warm colour grade.
- Warm late-afternoon light from the upper left is the default for Mosswood.
- Locations are layered like Octopath: a 3D floor, near props, and parallax background layers.

### 2.2 Sprites
- **Source:** Gemini sprite sheets, snapped to their true pixel grid and cleaned by hand. Kept at Gemini's native density: about 91–96 art pixels for a 168 cm adult (1 px ≈ 1.8 cm), in 64-pixel-wide cells.
- **No mouths** on sprites. Expression lives in the portraits.
- **Directions:** four (down, up, left, right). The right-facing walk is the mirrored left walk. **Changed from v1.1**, which recommended eight directions; four reads well at this size and halves production.
- **Walk and idle** for every character who moves in the world.
- **Battle sets** only for characters who fight on screen (see 9.4). They are made from Omniflash videos on a key colour and extracted by the pipeline. The key colour is chosen per character to be far from their palette (green for Tristitia, magenta for Elsie). Download at the 1080p upscale option.
- **Monsters** are one detailed still each, moved by the engine (breathing, wind-up, lunge, flinch, dissolve), as Octopath does. Regional and rare variants can be palette recolours of a base sprite.
- The full sheet and video workflow is in `Character Sprites/Gemini Sprite Prompts.md`, `Gemini Battle Batch Prompts.md`, `Gemini Monster Prompts.md` and `Animation Sources.md`.

### 2.3 Portraits
- Portraits follow the locked portrait style, with seven expressions per officer (Happy, Serious, Sad, Anger, Fear, Surprise, Laugh) in `Characters/Portrait Expressions/`.
- Officers present their department's screens with a large portrait and a dialogue box.

### 2.4 Environment art
- Battle and field backgrounds are built from Higgsfield images (`Environment Assets/Higgsfield Battleground Prompts.md`): a far panorama, a mid tree line, a ground tile, a prop sheet and a canopy.
- **New:** the panorama, tree line and canopy must **loop horizontally**, because the field view scrolls them while parties walk (section 8.3).
- **Method that works (2026-09-27):** the owner generated Mosswood with Codex from an MD brief. Source art is painted first; the pipeline then snaps it to exact 8×8 blocks and cuts the objects out. The approved set is `Environment Assets/Mosswood/Approved Calibration v1/`. The briefs for Amber Marsh and Redstone are in `Environment Assets/Region Prompts - Amber Marsh and Redstone Highlands.md`.
- **In the scene (proven in the operations proof):**
  - **Layers:** the far strip stands 26 m back and the mid strip 13 m back, each sized to the band the camera sees above the horizon. The mid strip is planted by its lowest tree base.
  - **Objects:** trees, props and the canopy are lit cutouts anchored at their base. The ground tile covers 6.3 m. Everything scrolls in world units, so perspective gives the parallax.
  - **Layout:** the fighting band stays empty; only small grass sits in front of it, and large pieces stay behind or at the far sides. The layout repeats every 48 m.
- **Pixel density:** the environment art has coarser pixels than the characters. At the characters' density a tall tree would be only as tall as a person. Each group is therefore scaled to a believable real size: trees about 0.105 m per art pixel, props 0.036, grass and flowers 0.03. Depth of field softens the difference at distance. Near the camera the coarse pixels turn into large blocks. The region briefs (revision 2) therefore target art-pixel counts by real size (for example a large tree at 400–550 art pixels).
- **Style decided (2026-09-27): painted.** Environments use the painted, Unicorn Overlord-like source art at full resolution, not 8×8 pixel art. Characters stay pixel sprites. The operations proof defaults to painted; its pixel switch remains only for comparison.
- **Density (owner direction, 2026-09-27):** less negative space, as in `Environment Assets/Mosswood/Codex Concept.png`. There is a tree line in front of the mid strip and more trees and props around the clearing. Big near trunks frame the screen edges. They are the closest layer, so they sweep past fastest while walking; when a fight starts they glide to the edges so they never stop in front of the fighters and a near foreground band of ferns, bushes and logs sits just behind the party HUD, softened by depth of field. Only the fighting floor stays open. The briefs add two sheets per region for this: `Foreground.png` and `Near Trunks.png`.

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

- **Fonts:** Marcellus for headings, Alegreya Sans for text and **all numbers**, Pixelify Sans for in-battle names. **Changed:** Pixelify digits misread (an 8 looks like an S), so numbers never use it.
- **Numbers use lining figures.** Old-style figures made "0" read as "o".

---

## 3. Core loop - Proven (operations proof), economy part carried over

1. Review the company at HQ.
2. Prepare adventurers and send expeditions: hunts, scouts and later contracts.
3. Let company time run while several operations proceed. Watch any of them if you like.
4. Receive corpses, discoveries, alerts and rewards.
5. Process, forecast, sell and craft *(carried over)*.
6. At 23:00, operations close; review the Resolution and the Day Summary; payroll and recruitment happen at weekly closeout.
7. Next day.

---

## 4. Time - Proven (operations proof)

| Rule | Value |
|---|---|
| Operating day | 07:00–23:00 |
| Clock speed at 1× | 1 real second = 120 company seconds (1 game hour = 30 real seconds) |
| Speed controls | Pause / 1× / 2× / 4× in the top bar |
| Combat tick | 12 company seconds; all combat and timed events resolve on a tick |
| **Battle pace** *(new)* | While the player watches a fight, the clock runs at ¼ of the chosen speed. A "Battle pace ¼" chip shows in the top bar. |
| New day | Starts paused at 07:00 |

**Changed from v1.1: battle pace.** At the old clock rate, fights lasted 2–8 real seconds, too fast to follow Octopath-style presentation. Slowing the clock only while a fight is on screen gives each fighter about one action every 4 real seconds at 1×. Outcomes are identical whether or not the player watches, because the simulation is the same; only its speed changes.

**Order within a tick** (from v1.1): combat damage, then timed events (scout intervals, searches, durations), then the cutoff. An event that completes exactly at 23:00 succeeds.

### 4.1 The 23:00 cutoff
- No new operation can start after 23:00.
- Hunts and scouts come home (status "returned at 23:00"). Contracts in progress fail.
- *(Carried over)* Unfinished processing aborts and returns the whole corpse. Unfinished enhancement aborts and returns its inputs. Rest and injuries continue. Listings persist.
- The **Resolution** screen lists every operation of the day with party, times, result and status (completed / returned / returned at 23:00 / returned (recalled) / returned (injured) / failed), plus anything that persists (injuries, rare targets still on the list).
- Then the **Day Summary** (section 13).

---

## 5. Company, HQ and officers - Carried over (Adventurer Office proven)

### 5.1 HQ
- **The HQ grows with the story** (decided 2026-09-27). Chapter 1 uses the small Tier 1 Company house on Company Edge: main room, Commander room, small courtyard and two-bed dormitory, with the expansion yard beside it. Departments are added as officers join and the yard is built up (Liliana's Information Office from Chapter 2, and so on). The courtyard has no training targets.
- HQ is room-based. Each officer owns a department, and the Commander walks to them. Never gather every officer in one room.
- Proof 4 proved walking through Eurydica (grey-box); the HQ interior follows the same method.

### 5.2 Officers

| Officer | Department | Role in play | Fights? |
|---|---|---|---|
| Tristitia | Commander's Office | Briefings, requests admin, Day Summary, payroll, flashpoints | Yes, in crises. Full battle set done. |
| Elsie | Adventurer Office | Roster, rest, backpack, expedition setup and monitoring | Rarely. Longsword and martial arts (9.6); battle stance, attack and skill made, batch 2 pending. |
| Steady Mae | Processing Room | Corpse storage, processing | No |
| Fulker | Workshop | Crafting, enhancement | No |
| Liliana | Information Office | Forecasts, rumours | No |
| Valerie | Commerce / Trading Post | Market, listings, potion counter | No. Always wears glasses. |

- Tristitia and Valerie are never recruitable. Never invent a filler officer.
- **Officers fight only at big story moments**, so their battles must look strong (section 9.4).

### 5.3 Company stats (top bar)
Day, time, Gold, Reputation, Morale, Company Rank. A new company starts at 07:00 with 2,500G, 60 Morale and Rank F.

---

## 6. Adventurers - Proven in part (operations proof)

### 6.1 Starting adventurers (sprites not made yet)

| Name | Specialty | HP | ATK | DEF | Rate | Traits | Passive |
|---|---|---|---|---|---|---|---|
| Rowan Vale | Vanguard | 180 | 18 | 10 | 1.0 | Steadfast, Shield-trained | **Shieldbearer** |
| Mira Ashford | Ranger | 150 | 16 | 8 | 1.0 | Keen-eyed, Trailwise | **Tracker** |
| Aveline Frost | Warden | 175 | 17 | 16 | 1.0 | Disciplined, Watchful | **Big Game Hunter** |
| Durgan Brass | Breaker | 205 | 18 | 8 | 1.0 | Resolute, Heavy-handed | **Shieldbearer** |

Durgan keeps Shieldbearer because he later becomes a shield and one-handed hammer fighter. Aveline uses a **greatsword** (decided 2026-09-27): a blade clearly shorter than her body (about chest height when planted), because full-length greatswords caused most of the video failures. Her specialty is renamed Warden (her old catalog id) so it no longer shares a name with the Shieldbearer passive. Reach: Rowan, Aveline and Durgan are **melee**; Mira is **ranged** (bow). Their looks, personalities and asset lists are in `Characters/Adventurers and Staff Roster.md`. In the operations proof the starters use officer sprites as stand-ins (Rowan = Fulker, Mira = Liliana, Aveline = Steady Mae, Durgan = Valerie) until their own sheets exist. Valencia is planned as a future adventurer.

### 6.2 Passives *(new)*
Passives are named abilities an adventurer brings to an expedition. They are shown on the roster and the prep screen.

| Passive | Effect | Owner |
|---|---|---|
| Tracker | +10% chance of a group of the hunt target; +10% find chance when scouting | Mira |
| Shieldbearer | +25% DEF while in the front row | Rowan, Durgan |
| Big Game Hunter | +20% ATK and +20% attack rate against Elite monsters (rare, variant and boss) | Aveline |

The percentages are starting values to tune. Items may later give similar bonuses (lures, maps).

**Monster tiers** *(new)*: every monster is either **Ordinary** or **Elite**.

| Tier | What it is | Examples |
|---|---|---|
| Ordinary | The three regular monsters of each area | Moss Slime, Dire Boar, Forest Wolf |
| Elite: Rare | Found by a scout's sighting; hunted as a special target (8.4) | Mossback Elder, Silvermane |
| Elite: Variant | A stronger version of an ordinary monster that turns up now and then in normal hunts (10.4) | Variant Dire Boar (bigger, recoloured) |
| Elite: Boss | Contract and flashpoint targets | Blackfang Direwolf, Ambermaw Matriarch, Crownstone Wyrm |

Anything that says "Elite" (like Big Game Hunter) applies to all three kinds.

### 6.2a Support adventurers (mages) *(new, not yet built)*
The back row's full value comes from mage-type adventurers, who usually stand in the back row. Their skills fall into four kinds:

| Kind | What it does | Example use |
|---|---|---|
| Heal | Restores an ally's HP | Keeps a lone front-row tank standing |
| Buff | Raises an ally's stats (ATK UP, DEF UP, SPD UP) | Hardens the tank, speeds up the damage dealers |
| Debuff | Lowers an enemy's stats (DEF DOWN, SPD DOWN) | Softens an Elite for the rest of the party |
| Attack | An offensive spell | The heavy damage dealer of the party |

This is the Unicorn Overlord build the rows are for: one tank in front, supported and healed from behind while an offensive mage does the heavy damage. Mages are ranged, so they lose nothing in the back row. Their skill meter fills over time (9.3a).

**The first mage (proposal): Valencia.** She already has a Gemini sprite sheet and a "Battle to Buff to Attack" clip in `Character Sprites/Valencia/`, and her look (glasses, scholar's cloak, green gem) fits a support caster.

| | |
|---|---|
| Role | Support mage (Buff), back row, ranged |
| Skill | **Verdant Blessing**: the front row gains ATK UP and DEF UP (+25%) for their next 3 actions |
| Joins | Recruitable after the first promotion (Rank E), so the rows' support payoff arrives with the second area |

Her milestone modifiers will be written once she is confirmed.

### 6.2b Signature skills *(new)* - Proven (operations proof)
Each adventurer has **one** signature skill (Dota 2 style), fired when their skill meter fills (9.3a). It gets stronger through progression milestones (6.2c) instead of a skill tree.

| Adventurer | Role (meter) | Skill | Effect (starting values) |
|---|---|---|---|
| Aveline | Attacker | **Diving Splitter** | Heavy damage to one enemy: 2.5× a normal hit |
| Rowan | Defender | **Phalanx** | DEF +50% for his next 3 actions |
| Mira | Attacker (ranged) | **Frost Arrow** | A normal hit that also slows one enemy: its attack interval ×1.5 for its next 3 actions |
| Durgan | Defender | **Shield Slam** | A normal hit that stuns one enemy: it skips its next action |

Durations count the affected fighter's own actions, so they work the same at any clock speed. Skills target the front enemy unless a milestone says otherwise.

### 6.2c Progression: four tracks *(new, not yet built; inspired by BattleTech)*
**Reference.** In BattleTech (HBS, 2018) each pilot has four skills: Gunnery, Piloting, Guts and Tactics. Experience earned on missions is spent to raise them one level at a time, and each level costs more than the last. Every level adds stats. Level 5 and level 8 unlock abilities, but a pilot can learn only two level-5 abilities and one level-8 ability. That limit forces a pilot to specialise. IMC keeps that structure, but milestones **modify the adventurer's one signature skill** instead of adding new abilities, so there is no skill tree to author per character.

**Tracks.** Every adventurer has the same four tracks, each from level 1 to 10:

| Track | Each level gives (starting values) |
|---|---|
| Power | +4% ATK |
| Toughness | +5% HP, +3% DEF |
| Speed | +3% attack rate |
| Focus | +5% skill meter fill |

**Experience** (earning is built in the operations proof; spending is not yet):

| Source | Experience |
|---|---|
| Each deployment (hunt or scout) | +10 to each member |
| Each fight won | +5 to each member still standing |
| Each monster killed | The monster's experience value (10.1; for example Dire Boar 11, Forest Wolf 14) to each member still standing; variants ×2, rares ×3, bosses ×5 |
| Scouting | +4 per completed half-hour, +10 per find |

- **Spending:** in the Adventurer Office with Elsie. Raising a track to level *n* costs 100 × *n* (level 2 costs 200, level 5 costs 500).
- **Cap:** 12,000 lifetime experience per adventurer. A single track from 1 to 10 costs 5,400, so a veteran maxes about two tracks and part of a third, and specialisation stays meaningful.
- **Pace:** a three-person Mosswood boar hunt earns each member about 100 experience. The first milestone (level 5 on one track, 1,400 in total) comes after roughly a dozen hunts, around the second in-game week.

**Milestones.** Reaching level 5 on a track unlocks that track's **rank 1** modifier for the adventurer's skill; level 8 unlocks **rank 2**.
- **Limit:** like BattleTech, an adventurer keeps only **two rank 1 modifiers and one rank 2 modifier**. Which tracks the player pushes first decides the adventurer's build; later tracks still give their stats.
- **Authoring:** each adventurer has eight modifiers (four tracks × two ranks).

**Example: Mira's Frost Arrow**

| Track | Rank 1 (level 5) | Rank 2 (level 8) |
|---|---|---|
| Power | The arrow hits 1.5× harder | Slowed enemies take +20% damage from everyone |
| Toughness | Mira gains DEF UP for 2 actions after firing | The slow also lowers the target's ATK |
| Speed | **Multi-shot**: hits 2 enemies | Hits every enemy |
| Focus | The slow lasts 2 more actions | The slow becomes ×2 instead of ×1.5 |

So one Mira might become a multi-shot crowd slower (Speed, Focus), and another a single-target killer (Power).

**Aveline: Diving Splitter**

| Track | Rank 1 (level 5) | Rank 2 (level 8) |
|---|---|---|
| Power | 3× damage instead of 2.5× | A kill with it refills half her meter |
| Toughness | She takes −30% damage for her next 2 actions after it | It heals her for 20% of the damage dealt |
| Speed | **Cleave**: also hits a second enemy for half damage | Hits every enemy (full on the target, half on the rest) |
| Focus | +50% damage against Elites (stacks with Big Game Hunter) | The target also gets DEF DOWN (−30%) for 3 actions |

**Rowan: Phalanx**

| Track | Rank 1 (level 5) | Rank 2 (level 8) |
|---|---|---|
| Power | While it holds, every hit he takes strikes back for 50% of his ATK | The counter hits for his full ATK |
| Toughness | DEF +75% instead of +50% | Raising it also heals him 15% HP |
| Speed | Lasts 5 actions instead of 3 | His meter starts each fight half full |
| Focus | The rest of the front row gains +25% DEF too | **Taunt**: while it holds, every enemy attacks Rowan |

**Durgan: Shield Slam**

| Track | Rank 1 (level 5) | Rank 2 (level 8) |
|---|---|---|
| Power | 2× damage | The stun lasts 2 actions |
| Toughness | DEF UP (+30%) for his next 2 actions after it | It heals him 10% HP |
| Speed | Hits 2 enemies and stuns both | Hits and stuns every enemy |
| Focus | A stunned enemy takes +25% damage from everyone | Against a slowed enemy (Frost Arrow), the stun lasts 2 actions: a Mira and Durgan combo |

These give real build choices: a counter-punching Rowan (Power) against a taunting wall (Focus), or a crowd-control Durgan (Speed) against one who locks down a single Elite (Power and Focus).

- **Replaces:** this takes over from v1.1's skill points (one per five deployments; Conditioning, Arms Training, Guard Training, Pathfinder). Pathfinder's search-time bonus can become a passive or an item.

### 6.3 Stamina, fatigue and rest (from v1.1)
- Four stamina bars. Each deployment spends one immediately. Recall never refunds it.
- **Red Fatigue** at 1 or 0 bars: attack, defense and attack rate at 50%. Scouts in Red Fatigue have double injury risk *(new)*.
- An adventurer at 0 bars cannot deploy.
- Rest takes exactly 24 hours and restores all four bars. It is assigned at closeout and continues through the cutoff.

### 6.4 Health and injury
- Healthy idle adventurers recover 10% of max HP per hour.
- A downed hunter, or a scout hurt in the field, becomes **Injured** for 48 hours and cannot deploy. They come home at 25% HP.

### 6.4a Nobody is lost for good *(new)*
**Changed from v1.1:** v1.1 had permanent death (a 10% roll for every downed hunter), permanent departure when wages went unpaid, and rehiring within 7 days. That assumed recruits were randomly generated. In the HD-2D game every adventurer and staff member is designed one by one, with their own sprite and portrait, so **no one is ever permanently removed**.
- **Defeat** means injury, never death. A wipe sends the whole party home injured.
- **Unpaid wages → Left (not permanent):** a staff member whose weekly wage can't be paid **leaves the company**. They are not gone for good: they appear in the Recruitment list as **Former staff**, with no time limit.
  - **Rehire cost** = their unpaid wages + their original hiring cost (the same amount paid when they were first recruited).
  - On leaving, their backpack items return to storage. They come back with their stats, passive and progress intact.
  - *Changed from v1.1*, which let people rehire only within 7 days, after which they were gone for good.
- **Emergency loan** (kept from v1.1): offered when no adventurer is left working and no one, new recruit or former staff, is affordable to hire or rehire.

### 6.5 States
Available, Hunting, Scouting, On contract, Resting, Injured, Event-locked, and Left (former staff who can be rehired). There is no Dead state.

### 6.6 Backpack - Carried over
The spatial backpack grid from v1.1 is unchanged: items have footprints and cannot overlap; Bow next to Arrow Case gives +15% attack rate; F/E packs 4×4, D/C 5×4, B/A 5×5. Potions (20G, 1×1) automatically restore 30% max HP when a hit leaves the carrier at or below 40%, at most one per damage batch.

---

## 7. Regions and discovery - Proven (operations proof)

### 7.1 Map
Parent region **Eurydica** (the city and company HQ), with three child areas:

| Area | Required rank | Theme |
|---|---|---|
| Mosswood Forest | F | Old oak forest outside the city, reached by the road from the South Gate (decided 2026-09-27; the district map is right). **Beasts and forest-habitat fantasy monsters only.** |
| Amber Marsh | E | Reedbeds and slow water |
| Redstone Highlands | D | Cold stone stairways and ridges |

The Region Map is parchment-styled. Locked areas show the rank they need.

### 7.2 Discovery
Each area has an exploration percentage that only scouting raises.

| Rule | Value |
|---|---|
| Progress per full 30 minutes of scouting | **+2%** |
| Progress for a full 3-hour scout | **12%** |
| Partial half-hours | Nothing |
| Trips to chart an area alone | About 9 |
| Several scouts in one area | Each adds its own progress |
| 25% and 50% | Identify the next ordinary monster (it becomes huntable, with an alert) |
| 75% | The area's main den is found if scouting hasn't found it yet |
| 100% | Area charted: every remaining landmark and path is revealed, and every scout there comes home |

**Changed from v1.1:** v1.1 gave 5% per half-hour (30% per trip), which charted an area in five scouts. It is now 2% per half-hour so scouting stays meaningful for longer. Consequence: the second monster (25%) takes two or three scouts, so Day 1 is slimes plus scouting, or two scouts at once.

### 7.3 Region knowledge *(new)*
Area Detail shows:
- a **Region Knowledge** panel: known monsters (x of 3), landmarks (x of 3), hidden paths (x of 2), current search time, and every active benefit and rare sighting;
- a **field map**, a small parchment map of the area whose fog clears as discovery rises. Finds are pinned on it and clear the fog around them.

---

## 8. Scouting - Proven (operations proof)

**Changed from v1.1:** scouting was a silent progress bar. It now has finds, risk and a view. This restores ideas from the legacy storyboard ("Storyboard 04 – Hunt / Scout Expeditions"), without its old success-chance mechanics for hunting.

### 8.1 Rules

| Rule | Value |
|---|---|
| Party | Exactly 1 adventurer |
| Cost | 1 stamina |
| Duration | Up to 3 hours, cut short by 23:00 |
| Fighting | Never |
| Reputation | +2 if at least one half-hour completed |
| Recall | Any time; keeps everything found |

### 8.2 Finds
Every completed half-hour adds 2% and then rolls for a find.

| Rule | Value |
|---|---|
| Find chance per half-hour | 45% (+10% with Tracker) |
| What can be found | Anything eligible on the area's find table, picked by weight |

**Mosswood find table**

| Find | Kind | Eligible from | Weight | Effect |
|---|---|---|---|---|
| Charcoal Burners' Trail | Hidden path | 10% | 3 | Hunts search 5 minutes less |
| Dire Boar Nest | Landmark (den) | 15% | 3 | Dire Boars appear 1.5× as often; +15% chance of a boar group when they are the target |
| Mossy Spring | Landmark | 30% | 2 | Hunting parties recover 10% HP after every won fight |
| Old Poachers' Track | Hidden path | 40% | 2 | Hunts search 5 minutes less |
| Howling Ridge | Landmark (den) | 55%, once Forest Wolves are known | 2 | Forest Wolves appear 1.5× as often; +15% chance of a pack when they are the target |
| Fresh tracks | Hint | An unidentified monster within 20% of its threshold | 2 | Flavour: hints at the next monster before it is identified |
| Mossback Elder | Rare sighting | Dire Boar known | 1.5 | Adds a rare hunt target (8.4) |
| Silvermane | Rare sighting | Forest Wolf known | 1 | Adds a rare hunt target |

Each landmark and path is found once. Amber Marsh and Redstone need their own tables (open question 6).

### 8.3 The field view *(new)*
- Choosing **Follow** on a scout opens the field view. The scout walks in place while the forest scrolls past (Octopath style: the world moves, the character stays).
- It shows the exploration bar with its milestones, the field map, an "Information revealed" list, a field log, and a parchment pop-up for each find ("Landmark found!", "Rare sighting!").
- Watching never changes the outcome.

### 8.4 Rare targets *(new)*
- A rare sighting adds a special target to the hunt list with a purple RARE badge.
- It stays until a hunt that targets it ends, whether or not the party kills it. Only one party can track it at a time.
- It is always alone (no groups) and appears 70% of the time on its hunt.
- A new sighting can put it back on the list.

| Rare | Based on | HP | ATK | DEF | Rate | Corpse value |
|---|---|---|---|---|---|---|
| Mossback Elder | Dire Boar (recolour) | 800 | 11 | 18 | 0.8 | ~60G |
| Silvermane | Forest Wolf | 950 | 13 | 16 | 1.1 | ~75G |

### 8.5 Scout risk *(new; scouting only)*
Only scouting shows a probability forecast. Hunting outcomes come from real fights.

| Rule | Value |
|---|---|
| Injury chance per half-hour (Mosswood) | 1% |
| Red Fatigue | Doubles it |
| Injured scout | Comes home at once with 40% HP and a 48-hour injury, keeping everything found and the +2 Reputation |
| Forecast on the prep screen | No incident / Injury percentages for the whole trip, plus the find chance |

For a rested scout on a full trip in Mosswood, the forecast is about 94% no incident and 6% injury.

- **No death.** Nobody dies (6.4a). The proof's "death" column goes. Harder areas can instead have a "serious injury" outcome with a longer recovery.
- **Deferred:** the owner decided to tune scout risk later, once Mosswood's whole core loop is playable and the mechanics can be judged together. The numbers above are placeholders until then.

---

## 9. Hunting and combat

### 9.1 Hunt rules - Proven (operations proof)

| Rule | Value |
|---|---|
| Party | 1–5 adventurers in a front row and a back row (9.1a) |
| Cost | 1 stamina each |
| Duration | Up to 3 hours, cut short by 23:00 |
| Search time | 30 min × (1 − 0.25 × discovery%) − 5 min per hidden path, never below 10 min (Pathfinder skill: −5% per level, strongest in party) |
| Encounter odds | Target 70%; other known ordinary monsters share 30%; a den multiplies its monster by 1.5 |
| After a won fight | Search again until time runs out |
| Loot | Whole corpses only. Each monster killed is one corpse, secured the moment it falls. |
| Reputation | +1 per corpse brought home |
| Recall | Any time; keeps every secured corpse; no stamina refund |
| Wipe | The party comes home injured; corpses secured earlier are kept; nothing from the final exchange |

### 9.1a Formation: front and back rows *(new)* - Proven (operations proof)
**Changed from v1.1:** v1.1 used a single ordered list where the enemy always hit slot 1. The party now has two rows, in the spirit of Unicorn Overlord, so the player can build around them: one armoured tank in front with four behind, or three fighters in front and two ranged behind.

| Rule | Value |
|---|---|
| Slots | 3 in the front row, 3 in the back row |
| Party size | Up to 5, with at least 1 in front |
| Enemy targeting | Enemies spread their attacks over the living front row: enemy N hits front member N (wrapping round when there are fewer front members) |
| Back row | Only attacked when the whole front row is down |
| Melee in the back row | −50% damage (they can't reach) |
| Ranged | Full damage from either row |
| Party targeting | Everyone hits the front living enemy |

- **Prep screen:** two labelled rows of three slots. Each adventurer has Front and Back buttons, a filled slot has ⇅ (swap rows) and ✕ (remove), and a melee fighter in the back shows a "melee: −50% damage" warning. Reach is shown by a sword or bow icon.
- **Battle:** the front row stands nearest the enemies, the back row further behind, and the columns are staggered in depth so nobody hides behind a row-mate. The party HUD tags each member FRONT or BACK.
- **Support roles:** the real payoff of the rows comes from mage-type adventurers in the back row who heal, buff, debuff or attack (6.2a). None of the four starters is a mage yet.
- **Later:** some enemies could get reach attacks that hit the back row.

### 9.2 Groups *(new)*
**Changed from v1.1:** v1.1 had exactly one monster per encounter. Encounters now hold 1–3 monsters.

| Monster | Base chance of 2 or more |
|---|---|
| Moss Slime | 60% |
| Dire Boar | 45% |
| Forest Wolf | 70% (packs) |
| Rare monsters | 0% (always alone) |

- A second monster joins at the group chance *c*; a third joins with chance *c*/2.
- **Bonuses apply only to the hunt target:** +15% if its den is found, +10% with Tracker in the party. Items may add more later.
- More monsters mean more corpses and more danger. Every monster attacks, so a group of three hits three times as hard; the front row spreads that load. The prep screen's risk estimate includes groups and the formation.

### 9.3 Combat rules - Proven (operations proof)
Combat is automatic. The player's control is preparation: party, order, stamina, gear, target.

| Rule | Value |
|---|---|
| Attack interval | 120 ÷ attack rate company seconds, rounded up to the next 12-second tick |
| Damage | max(1, floor(attack × 100 ÷ (100 + defense))) |
| Party targets | The front living enemy |
| Enemy targets | Spread over the living front row, then the back row (9.1a) |
| Turns | **One fighter acts at a time** (see below) |
| Fight stats | Fixed when each fight starts: Red Fatigue, the row (melee in back −50%) and passives (Shieldbearer, Big Game Hunter) |

**Turns (changed 2026-09-27).** v1.1 resolved everyone whose timer was due in one simultaneous batch. Now one fighter acts at a time, so every attack and skill can be animated in full and skills get their cinematic:

| Rule | Value |
|---|---|
| Attack gauge | Fills over the fighter's attack interval (the gold ring); when full, the fighter is ready |
| Queue | Ready fighters wait in the order they became ready; ties go to the front row, then the back row, then enemies |
| Stage | The first fighter in the queue acts as soon as the previous action ends; the gauge refills after acting |
| Action length | Normal attack 24 company seconds; skill 72 (the cinematic); a stunned enemy's lost turn 12 |
| State | Every action sees the fight as it is at that moment (HP, who is down, the front target) |

At battle pace (4.4) a normal attack takes 0.8 real seconds at 1× and a skill 2.4 seconds, during which the camera pushes in with a vignette and a skill banner, as in proof 2. Measured over 24 simulated hunts, fights now last about 23 company minutes (was 19) with no change to safety.

The prep screen shows a Low / Moderate / High risk estimate with an icon and text, based on expected fights over three hours (groups included).

### 9.3a Skill meter *(new)* - Proven (operations proof)
Every fighter has a **skill meter**: a second, thinner bar under the HP bar in the party row. When it is full, the fighter's next action is their skill, and the meter empties.

How it fills depends on the fighter's role, so each role plays differently:

| Role | Fills from | Starting value | Result |
|---|---|---|---|
| Attacker (Tristitia, Aveline, Mira) | Landing attacks | +25 per hit dealt | A skill about every 4th attack |
| Defender (Rowan, Durgan) | Being hit | +20 per hit taken | A skill after about 5 hits taken, so a busy tank gets it sooner |
| Mage | Time, like the attack timer | Full over 4 attack intervals | Steady, predictable skills from the back row |

- **Colour:** the meter is orange with a glow and a "SKILL" tag when full. It must not be blue, which reads as MP, or gold, which is the attack-timer ring.
- **Tristitia:** today Piercing Verdict comes every third action. Under the meter she is an attacker, so it comes when her meter fills from her hits.
- The starters' skills are in 6.2b.

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
- **Party row**: along the bottom with no container box, Star Ocean 2 style.
  - A round bust (face and shoulders from the front idle sprite) instead of a name plate.
  - Name above a large HP number and HP bar.
  - The attack timer is a **gold ring filling clockwise** around the bust. Not a blue bar: that reads as MP.
  - Status effects sit above the name. Slot 1 shows FRONT.
- **Left side**: place and target, time left, secured corpses.
- **Right side**: battle log.
- **Buttons**: Leave view and Recall. The top bar with the speed controls stays visible.
- There is **no turn-order bar**; the rings make it redundant.
- **Closing the view never stops the fight**, and reopening it shows the live state.

### 9.5 The search walk *(new)*
While a hunting party searches, the field view shows them walking in formation as the world scrolls past. When an encounter starts, the scroll eases to a stop and the monsters slide in from the left. After a win the party walks on. The environment layers must loop horizontally (2.4).

### 9.6 Officer battle moves
Officers fight only at story moments, so their battles are showpieces.

| Officer | Weapon | Attack | Skill | Guard |
|---|---|---|---|---|
| Tristitia | Rapier (right-handed) | **Rose Waltz**: a dance-like combo. Hit 1 lands after the pass-through cut, when she has turned her back (samurai draw); hit 2 is a low cut. The final raised hand gives a random ally SPD UP. | **Piercing Verdict** (every third action): a flourish and charge at her own spot, then a high-speed lunge that ends *behind* the target. Heavy damage plus DEF DOWN and SPD DOWN for 3 turns. | Rapier parry |
| Elsie | **Longsword and martial arts** (decided 2026-09-27), in the spirit of Yoshimitsu (Tekken): sword cuts flowing into punches and kicks. Front row. | A mixed sword, kick and punch combo (`Elsie/Attack.mp4`) | **Hateful Slash**: a slash that provokes. Every enemy must attack Elsie for its next 2 actions, protecting the rest of the party (`Elsie/Skill, Hateful slash(provoke enemy).mp4`) | Sword crosswise against her forearm, front knee raised (batch 2, prompt in Revision 5) |

- **Elsie:** the greatsword is dropped (every attempt failed), and so is the spear and short sword. She now fights with a longsword plus kicks and punches. Her stance, attack and skill are made; batch 2 (idle, hurt, guard, victory, defeat) uses `Gemini Battle Batch Prompts.md` Revision 5. Her skill changed from the party buff to a provoke, which fits her role of keeping adventurers safe.
- **Provoke:** a provoked enemy ignores the front-row rule and attacks the provoker until the effect ends.
- Status effects in use: ATK UP, DEF UP, SPD UP, DEF DOWN, SPD DOWN, PROVOKE.

---

## 10. Monsters - Proven in part

### 10.0 Variants *(new)* - Proven in the operations proof, except the chance boosts and the elite-part library
A **variant** is a stronger version of an ordinary monster. It counts as Elite (6.2), so Big Game Hunter works against it.

| Rule | Starting value |
|---|---|
| Looks | 15% bigger and a distinct palette, with a VARIANT badge on its HP bar |
| Stats | HP ×1.5, ATK and DEF ×1.25 |
| Chance | 8% for each ordinary monster in an encounter, rolled separately. A 3-hour hunt has about 3–4 fights of 1–3 monsters, so roughly one variant every two hunts: often enough to meet, rare enough to cheer. |
| Boosts | Some landmarks, items and traits raise the chance (for example a Mosswood landmark that adds +4% there) |
| Reward | Better experience for the party, once adventurer experience exists (open question), and its own corpse |
| Alert | A "Variant!" pop-up and log line when one appears, so the moment registers even when the player isn't watching |

**Variant corpses.** A variant brings home a **variant corpse**. Processing it gives the usual parts plus one elite part from a small library: one elite part per ordinary monster, for example Slime Core → Elite Slime Core. That is nine elite parts across the three areas. Elite parts are worth more and feed later uses (stronger enhancement, special requests). It is kept small on purpose, so it marks the moment without bloating the item list.

### 10.1 Mosswood Forest

| Monster | HP | ATK | DEF | Rate | Known at | Process time | Common value | Sprite |
|---|---|---|---|---|---|---|---|---|
| Moss Slime | 180 | 4 | 0 | 0.7 | 0% | 30 min | 8G | Placeholder |
| Dire Boar | 330 | 6 | 8 | 0.8 | 25% | 45 min | 12G | Done |
| Forest Wolf | 420 | 8 | 10 | 1.0 | 50% | 60 min | 16G | Placeholder |
| Blackfang Direwolf | 1,950 | 15 | 25 | 1.0 | Contract only | 90 min | 30G | Needed |
| Mossback Elder (rare) | 800 | 11 | 18 | 0.8 | Sighting | – | ~60G | Boar recolour |
| Silvermane (rare) | 950 | 13 | 16 | 1.1 | Sighting | – | ~75G | Needed |

Experience per kill: Moss Slime 6, Dire Boar 11, Forest Wolf 14, Blackfang 65, Mossback Elder 32, Silvermane 38 (before the variant, rare and boss multipliers).

**Changed 2026-09-27: beefier monsters.** HP ×3 and ATK ×0.7 against v1.1, together with the higher group chances (9.2). Fights were over before slows, stuns and buffs mattered. Measured over 24 simulated 3-hour boar hunts (Rowan and Aveline in front, Mira behind):

| Setting | Fight length | Skills per fight (party) | Front row HP left | Wipes |
|---|---|---|---|---|
| v1.1 numbers | 6.5 min | 1.5 | 65% | 0% |
| Groups up, HP ×2 | 13 min | 3.4 | 31% | 0% |
| **Groups up, HP ×3, ATK ×0.7 (chosen)** | **19 min** | **4.7** | **43%** | **0%** |

A fight now lasts about 40 real seconds when watched at 1× battle pace. A lone adventurer hunting boars wipes about 60% of the time, which makes solo hunting a real risk. The experiment tool is `HD-2D Proof/tools/tune-ops.mjs`.

### 10.2 Amber Marsh (Rank E) - Carried over (HP ×3, ATK ×0.7 applied like Mosswood; not yet tested)

| Monster | HP | ATK | DEF | Rate | Known at | Process time | Common value |
|---|---|---|---|---|---|---|---|
| Marsh Slime | 510 | 10 | 15 | 0.8 | 0% | 45 min | 18G |
| Marsh Serpent | 660 | 13 | 20 | 1.0 | 25% | 60 min | 22G |
| Marsh Stalker | 840 | 15 | 25 | 1.1 | 50% | 75 min | 28G |
| Ambermaw Matriarch | 3,300 | 21 | 35 | 1.0 | Contract only | 120 min | 45G |

### 10.3 Redstone Highlands (Rank D) - Carried over (HP ×3, ATK ×0.7 applied like Mosswood; not yet tested)

| Monster | HP | ATK | DEF | Rate | Known at | Process time | Common value |
|---|---|---|---|---|---|---|---|
| Stone Crawler | 900 | 17 | 35 | 0.8 | 0% | 60 min | 30G |
| Highland Wolf | 1,140 | 20 | 30 | 1.1 | 25% | 75 min | 36G |
| Ridge Drake | 1,500 | 24 | 45 | 0.9 | 50% | 90 min | 45G |
| Crownstone Wyrm | 5,400 | 28 | 50 | 1.0 | Contract only | 150 min | 65G |

The Marsh and Redstone boars made for proof 2 are palette variants of the Dire Boar and can become regional monsters if wanted.

---

## 11. Contracts, requests and flashpoints - Carried over

- **Subjugations:** accepted contracts take a 30-minute approach, then use the same combat as hunts. A failed accepted contract costs 10 Reputation; ignoring an offer costs nothing. There are eight authored subjugations, each with a resident, a problem, a target, a reward and an ending.
- **Resident requests:** ten authored one-off deliveries (road lanterns, children's soles, hospice blankets and so on) plus repeatable supply slots.
- **Flashpoints** (presented by Tristitia):

| Flashpoint | Target | Unlocks at | Reward |
|---|---|---|---|
| Blackfang Direwolf Menace | Blackfang Direwolf | 300 Rep | 900G, 250 Rep |
| The Ambermaw Blockade | Ambermaw Matriarch | 800 Rep, after Blackfang | 1,400G, 350 Rep |
| The Crownstone Reckoning | Crownstone Wyrm | 1,400 Rep, after Ambermaw | 2,000G, 450 Rep |

  Offers last 72 hours. A failure or expiry returns after 10 days.

---

## 12. Economy - Carried over (not yet proven in HD-2D)

- **Processing (Steady Mae):** one processor works one corpse. Duration depends on the monster, the staff rank and Morale. One quality roll gives Pristine, Standard, Damaged or Unsellable parts. Ordinary corpses give 3 common parts and a 20% chance of a rare part; bosses give 5 common parts and one guaranteed rare.
- **Information (Liliana):** forecasts of future demand, with confidence based on staff rank. They never change the real market.
- **Commerce (Valerie):** listings of 1–99 units at a unit price; buyers check hourly and may buy part of a stack. The fee is 5% of each purchase (minimum 1G). Net sales earn 1 Reputation per 100G.
- **Workshop (Fulker):** daily production chosen by focus; enhancement adds 5% of base stats per level using common parts and refinements.
- **Staff:** processor, information officer and craftsman are hired roles with weekly wages.

---

## 13. Closeout, payroll and progression - Proven (closeout), rest carried over

### 13.1 Day Summary (presented by Tristitia)
Groups:
- Revenue
- Expenses
- Operations (hunts and fights won, scouts and finds, exploration change, corpses in storage)
- Reputation (with its sources)
- Morale
- Stamina
- Notable events (finds, identifications, injuries)

### 13.2 Weekly closeout
- Payroll is paid weekly, then recruitment refreshes.
- Rest is assigned at closeout.

### 13.3 Company rank

| Promotion | Reputation | Gold | Unlocks |
|---|---|---|---|
| F → E | 200 | 300G | Amber Marsh |
| E → D | 700 | 700G | Redstone Highlands |
| D → C | 1,500 | 1,500G | Final rank |

### 13.4 Victory and loans
- **Victory:** Rank C, the final Flashpoint cleared, and no debt. There is no fixed day limit.
- **Emergency loan:** 2,500G, repaid within 7 days, no interest. Offered when no adventurer is working and no one, recruit or former staff, is affordable (6.4a).

---

## 14. Story gating - Carried over

Services open when the story introduces them, not on fixed days:

| Milestone | Service |
|---|---|
| M02 | Recruitment |
| M03 | Hunting |
| M05 | Workshop |
| M06 | Scouting |
| M08 | Contracts |

The campaign and its chapters live in `Manuscript/`, `Game Design/Chapters/` and `IMC_STORY_AGENT_BIBLE.md`.

---

## 15. Screens (HUD flow)

| Screen | Status |
|---|---|
| **Top bar**: Day, Time (turns orange in the last hour), Gold, Reputation, Morale, Rank, Battle pace chip, Pause/1×/2×/4× | Proven |
| **Adventurer Office**: Elsie's portrait and dialogue (changes with events); menu of New Expedition, Ongoing Expeditions, Roster | Proven |
| **Roster**: bust, name, passive, role, HP, stamina bars, status (Available, On expedition, Injured, Red Fatigue) | Proven |
| **Eurydica Region Map** (parchment) | Proven |
| **Area Detail**: exploration bar with milestones, known monsters (silhouette + "?" when unknown), Region Knowledge, field map, Hunt / Scout / Contracts | Proven |
| **Hunt target selection**: large cards with art, stats, tactics, group chance, corpse value; rare cards in purple | Proven |
| **Preparation**: front and back rows of three slots, roster picker with Front/Back buttons, reach icons and passives, duration and return time, cutoff warning, stamina before → after, Red Fatigue warning, risk (hunt) or forecast (scout) | Proven |
| **Ongoing Expeditions list** (right side): each operation with party, phase, time bar, discovery bar for scouts, corpses for hunts; buttons Watch battle / View / Follow and Recall; "Returned today" below | Proven |
| **Field view**: hunt battle, search walk, scout walk (section 8.3 and 9.4) | Proven |
| **Alerts**: right-side cards (left side in the field view), colour-coded info / success / warning / critical / rare | Proven |
| **23:00 Resolution** and **Day Summary** | Proven |
| HQ walking, Building Map, Commander's Office, Processing, Information, Commerce, Workshop, Request Board, Payroll, Recruitment, Rank promotion, Flashpoint screens | Carried over |

---

## 16. Production notes

- **Proof pipeline:** a three.js page per proof, published as a private artifact. Each proof has a check ledger (`GATES-*.md`) with automated checks in headless Chrome.
- **Godot target:** the 3D project (`D:\Godot Projects\imc-playground`) becomes the HD-2D game. Proofs are the reference for its implementation.
- **Codex helper:** heavy batch jobs (for example sprite extraction) can run on Codex in `D:\Codex\IMC`; only checked results are copied into the project.

---

## 17. Open questions

1. **Confirm Valencia as the first mage** (6.2a), then write her milestone modifiers.
2. **Progression screen.** Spending experience at Elsie's office (the four tracks, costs, milestones) is designed but not yet proven.
3. **Passive growth.** Are passives fixed per adventurer, or learned too (v1.1's skill points: Conditioning, Arms Training, Guard Training, Pathfinder)?
4. **Scout risk by area** (deferred until Mosswood's core loop is complete).
5. **Items for expeditions.** Lures (group chance), maps (find chance), and whether the backpack holds them.
6. **Officer battles vs. the adventurer combat model.** Proof 2 used a speed-based turn gauge for Tristitia's showcase fight; hunts use the attack-rate model. Unify them: for example, Tristitia's skill replaces every third attack under the attack-rate model.
7. **Find tables for Amber Marsh and Redstone**, including their rare monsters.
8. **Monster sprites needed:** Moss Slime, Forest Wolf, Silvermane, Blackfang, and the Marsh and Redstone rosters.
9. **Rare target expiry.** Should a sighting expire after some days if nobody hunts it?
10. **Adventurer sprites:** Rowan, Mira, Aveline and Durgan need sheets before they can replace the stand-ins.

### Ideas saved for later
- **Recolourable recruits:** a few simple adventurer sprite bodies, each with 1–5 colour templates the player picks when recruiting. This would allow more recruits without drawing each one. It is more work, so it is parked for now; hand-designed adventurers stay the rule.

---

## 18. Change log

| Date | Change |
|---|---|
| 2026-09-27 | Proof 4 version 3: facades approved, camera locked straight north, HD-2D building workflow added to the environment skill. |
| 2026-09-27 | Proof 4 version 2: Codex-painted facades, curved roofs, arched gatehouse, painted props; camera heading left open for the owner. |
| 2026-09-27 | Proof 4 built and published: explorable Eurydica grey-box (Chapter 1 Scene 3). The town camera and cutaway are decided. Town dialogue follows the manuscript, and requests unlock only on the offer branch. |
| 2026-09-27 | v2.0 created from the v1.1 GDD and the balance sheet. Added: HD-2D direction, four-direction sprites, battle presentation and party HUD, battle pace, 1–3 monster groups, scouting finds, landmarks, hidden paths, rare targets, scout risk, field view and search walk, region knowledge and field map. Scouting slowed from 5% to 2% per half-hour. |
| 2026-09-27 | Elsie decided: longsword with Yoshimitsu-like kicks and punches; her skill becomes Hateful Slash (provoke). Aveline takes the greatsword (shorter than full body length) and her specialty becomes Warden. |
| 2026-09-27 | Elsie's greatsword dropped; her weapon is either the spear and short sword or a longsword with Yoshimitsu-like mixed fighting (recommended). |
| 2026-09-27 | Turns: one fighter acts at a time through a readiness queue; attacks take 24 company seconds and skills 72, with a push-in cinematic and a banner for skills. |
| 2026-09-27 | Environment style decided: painted (briefs updated to skip the 8×8 snap). Near trunks scroll with the walk and frame each fight. Proof 4 plan agreed (scope, camera, building method, story fixes). Roster of the starting adventurers and staff written: `Characters/Adventurers and Staff Roster.md`. |
| 2026-09-27 | Denser Mosswood assembly after the owner's concept (tree line, framing trunks, near foreground band); a pixel-art / painted switch in the proof; the region briefs revised for pixel density, density and two new sheets. |
| 2026-09-27 | The approved Mosswood environment set replaces the placeholder clearing in the field view (hunt search walk, battles, scout walk). |
| 2026-09-27 | Balance: group chances raised (slime 60%, boar 45%, wolf 70%); monster HP ×3 and ATK ×0.7 in every area, chosen by simulation (fights about 3× longer, 3× more skills, no wipes for a normal party); kill experience is a fixed value per monster. |
| 2026-09-27 | The operations proof now has the skill meter, the four signature skills, variants (8%, the rust boar recolour for the Dire Boar) and experience earning. Drafted milestone modifiers for Aveline, Rowan and Durgan, the experience numbers (100 × level costs, 12,000 cap), and Valencia as the proposed first mage (Verdant Blessing). |
| 2026-09-27 | Signature skills: Diving Splitter (Aveline), Phalanx (Rowan), Frost Arrow (Mira), Shield Slam (Durgan). Progression: four tracks (Power, Toughness, Speed, Focus) bought with experience at rising cost, BattleTech style; level 5 and 8 milestones modify the signature skill, with at most two rank 1 and one rank 2 modifiers per adventurer. Replaces v1.1's skill points. |
| 2026-09-27 | Skill meter under the HP bar, filled by role (attackers by hitting, defenders by being hit, mages over time). Variants: bigger and recoloured, HP ×1.5, ATK/DEF ×1.25, 8% per monster, better experience, variant corpses with a small elite-part library. |
| 2026-09-27 | Monster tiers: Ordinary, or Elite (rare, variant, boss); Big Game Hunter applies to all Elites. Support adventurers are mage types in the back row with heal, buff, debuff or attack skills. |
| 2026-09-27 | Durgan keeps Shieldbearer (future shield and one-handed hammer build). Unpaid wages: the staff member leaves but can always be rehired as Former staff for unpaid wages + original hiring cost; the emergency loan trigger is reworded. |
| 2026-09-27 | Front and back rows (3 + 3 slots, up to 5, at least 1 in front), enemies spread over the front row, melee in the back −50%; the operations proof now uses the real starters and their passives. |
| 2026-09-27 | Nobody is permanently lost: no death, no quitting over wages (6.4a). Passives: Shieldbearer (Rowan, Durgan), Big Game Hunter (Aveline); monster tiers added. Scout risk tuning deferred until Mosswood is complete; its death column removed. Recolourable recruits saved as a later idea. |
