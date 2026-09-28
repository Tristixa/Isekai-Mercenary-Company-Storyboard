# GDD v2.1 proposals (resolved)

**Resolved 2026-09-27.** Everything here was decided and merged into `IMC GDD.md` v2.1. Later refinements, also merged: Commander skills cap at rank 2 in Eurydica; skills grow through officer working sessions (minigames); hunger is a status; officers get one permanent trade-off perk at Bond 5; romance is Frontier-only. This file is kept as the decision record.

## Owner decisions (2026-09-27)

1. **Name: Frontier Guild Chronicle (FGC).** The organisation is a Guild in player-facing text; the player stays "Commander".
2. **Romance: bond levels with authored scenes and a Bond 4 choice, one romance at a time, but NOT with the officers.** Romanceable characters are NPCs in Eurydica and, later, the Frontier. Officers aren't romanceable (this may change later if players ask for it).
3. **Day and sleep:**
   - **Operations run 07:00–20:00.** The cutoff and Resolution, then the Day Summary, happen at **20:00**.
   - **After 20:00:** officers follow their own free-time routines, and adventurers go to bed and regain **1 stamina bar overnight**.
   - **A rest order during the day** (the adventurer isn't dispatched) restores the **full** stamina bar.
   - **The day ends only by using the bed after 20:00.** At 01:00 the Commander falls asleep automatically. **No Tired penalty.**
   - **No busking.** No daytime nap skip.
4. **The Commander never fights. No "Accompany".** Commander skills are being detailed (see A6) before a decision.

Status of the rest: **proposals, not decided.** Each item gives a recommendation and the reason for it. After the owner decides, the chosen answers move into `IMC GDD.md` and this file is archived. The sources are the owner's requests of 2026-09-27, `D:/Codex/Progression conversation.md`, the story bible and a Codex audit of the GDD (part B).

---

## Part A: the owner's new topics

### A1. The game's name

**Facts:**
- In the story, Eurydica has no adventurer's guild, and the Company fills that gap (bible line 54).
- The Chapter 1 manuscript calls it a guild (the player names it: `<Guild-name>`).
- Later, the organisation becomes the Frontier's verification body, with "Guild Verified" (bible lines 87, 107).
- The Commander keeps the title Commander.
- "Isekai" was a joke and can go. "Chronicle" is wanted as a homage to Steambot Chronicles. The bible already bases the Commander's voice on Vanilla.

**Options:**

| Name | For | Against |
|---|---|---|
| **Guild Chronicle** | Short, says what you do, a direct homage | Generic, hard to search |
| **Frontier Guild Chronicle** | Names the destination of the whole arc (Chapter 6 onward) | The first five chapters happen before the frontier |
| **The Wayfarers' Chronicle** | Warm, adventurous, fits the guild of expeditions | Doesn't say "management" |
| **Chronicle of the Unwritten Frontier** | Ties "chronicle" to the guild's later job: writing trustworthy records of the unknown | Long |

**Recommendation: Frontier Guild Chronicle.**
- "Chronicle" matches what the guild literally becomes: the keeper of verified records.
- "Frontier" is the promise the early chapters build toward.
- "Guild" corrects the Company/guild mismatch.
- The abbreviation **FGC** can replace IMC in new work, while the old folders keep their names.

**Follow-up:** rename "Company" to "Guild" in player-facing text (Company Rank → Guild Rank, and so on). Keep "Commander" as the player's title.

### A2. The Commander's own life (Steambot-style ordinary life)

**What Steambot does:**
- Vanilla has hunger (he can't run while hungry, and a growling stomach makes listeners walk away mid-performance).
- He busks and later plays in a band for tips.
- He rents an apartment and dates.
- He never has to do any of it.

Its charm is that ordinary life is **optional and rewarding**, never a chore.

**Recommendation: a light personal layer that feeds the guild, not a survival sim.**
- **Meals, not a hunger meter:**
  - Eating a meal (at the HQ table with the officers, or at the tavern or a food stall) gives **Well-fed** until the evening: faster walking and one extra dialogue option in some talks.
  - Skipping meals only removes the bonus. No penalties that feel like chores.
- **Energy and sleep (A3)** is the only real need, and it's what ends the day.
- **Personal activities** each pay into something the guild cares about, so they pass the "Tomorrow I want to ___" test:

| Activity | Where | Pays into |
|---|---|---|
| Talk and eat with people | HQ, tavern, market | **Bonds** (A4), rumours that become Information leads |
| Busk music (Steambot homage; a simple timing minigame, instruments bought or crafted by Fulker) | Red-tree plaza, tavern | Personal tips, **Reputation**, and a following that brings customers and recruits |
| Help residents (the existing request cast: Hollis, Beren, Marta and the others) | Around the city | Reputation, lasting customer relationships, cheaper supplies |
| Walk the night city | Eurydica after 23:00 | Night-only NPCs and events (the ladies in the red and green dresses already exist in the dialogue data), rumours, romance dates |
| Gifts and outings | Shops, then with an officer | Bonds |

- **Commander growth, not combat stats.** Four Commander skills rise through activities and story choices:
  - **Leadership:** Morale;
  - **Negotiation:** contract rewards and sale prices;
  - **Insight:** forecast confidence and scout finds;
  - **Craft sense:** workshop results.

  Each has 5 ranks with small, visible effects (for example Negotiation +2% sale price per rank). This is the BattleTech-style commander growth, applied to running a guild.
- **Money:** one guild purse. The Commander's personal spending shows as its own line, "Commander", in the Day Summary. Busking tips go to the purse too.

### A3. Sleep and the day structure

**The confusion:** the day ends at 23:00 with the Resolution and the Day Summary. So what does sleeping do?

**Recommendation: sleep IS the end-of-day button, and the evening after 23:00 is the Commander's free time.**

| Time | What happens |
|---|---|
| 07:00 | The new day starts, paused, in the Commander's room |
| 07:00–23:00 | Guild operations run. The Commander can walk the HQ and the city while time runs; talks and shops pause the clock (as in proof 4) |
| 23:00 | Cutoff, then the Resolution and the Day Summary, as now |
| 23:00–02:00 | **Night:** no operations. The clock keeps running while the Commander walks the night city: tavern, night NPCs, dates, busking, reading reports |
| Any time after the Day Summary | **Go to bed** in the Commander's room: the day ends and the next one starts at 07:00 |
| 02:00 | If he's still awake, he falls asleep where he is and starts the next day **Tired** (walks slower, no Well-fed bonus until he eats) |

- **Napping in the daytime** (optional): sleeping before 23:00 fast-forwards to 23:00. Operations resolve exactly as if you had watched (same simulation), then the Resolution plays. This is simply "skip to tonight", which management games need anyway.
- The Commander never needs to sleep to restore stats beyond Tired. Energy exists only to give the night a natural end.

### A4. Romance

**Model: bonds with the officers**, like Fire Emblem supports or Persona confidants, told through our portrait dialogue view.

**How bonds grow:**
- Bond levels 0–5 per officer.
- Points come from time spent together (meals, evening talks, outings), from choosing gifts they like, and from **working well with their department** (for example Mae's points rise when her processing is used well and she isn't overworked).
- Each level unlocks an authored **bond scene**: a heart event with choices.

**Romance:**
- At Bond 4 a scene offers a choice to become more than colleagues. Declining keeps a close friendship with its own ending.
- **One romance at a time.** Ending it takes a scene.
- Romance scenes and endings unlock at Bond 5.

**Pacing and the story:**
- At most one bond level per officer per in-game week.
- Bond 4 can't happen before that officer's personal story beat (after Chapter 2 for the founding officers, for example).
- The main story stays the same for everyone; only bond scenes and small lines change.

**Gameplay value, kept small:**
- Each bond level gives that officer's department a small perk (for example Mae at Bond 3: processing takes 10% less time).
- A romance partner adds one extra scene per chapter and a special ending epilogue.
- No stat power that the player feels forced to chase.

**Who (owner to confirm):**
- The officers: Tristitia, Elsie, Steady Mae, Liliana, Valerie, and Fulker (Fulker's gender and personality aren't established in the bible yet).
- Adventurers could come later.

**Tone guard:**
- Adult-coded characters; restrained, mature writing.
- Officers keep their professional roles and their own views. The bible's "trust through responsibility" dynamics stay the core of each bond (for example Tristitia tests whether he follows through).

### A5. Should the Commander fight? (BattleTech)

**Recommendation: no, not as a fighter.**
- The bible's premise is that he is "not a lone hero who personally solves every problem through combat" (bible lines 42, 285).
- The management pillar ("The player decides; combat resolves itself") depends on it.
- In BattleTech the commander pilots a mech because that game is about tactics; ours is about running the guild.

**Offered instead:**
- The Commander skills (A2).
- **Optional, later: "Accompany".** The Commander can go along on one expedition per day in the back row. He doesn't attack, but gives one **command** per fight (Focus target, Hold the line, Fall back) and +10% skill-meter fill to the party. It costs his whole day (no HQ or city activities while out), and he can be lightly injured (no personal activities for 2 days).

  It needs Commander battle sprites (stance, command gesture, hurt), so it's parked under "Ideas saved for later" unless the owner wants it now.

### A6. Commander skills and ordinary life, in detail (after the owner's decisions)

**Skills: four, each with ranks 0–5.** Skill points come from ordinary activities and from dialogue choices. Each rank's effect is small and shown on the Commander's page.

| Skill | What it does, per rank | Rank 3 unlock | Grown by |
|---|---|---|---|
| **Leadership** | Morale losses −10% per rank; +1 Morale at the Day Summary per rank on days with no injuries | **Word of encouragement:** once a day, remove Red Fatigue's penalty from one adventurer's next dispatch | Evening talks with adventurers at HQ; briefing a party before dispatch; choices that take responsibility |
| **Negotiation** | Request and contract gold +4% per rank; market buyers pay +2% per rank | **Haggle:** the travelling merchant pays 60% of value instead of 50% | Talking with shopkeepers and clients; delivering requests in person; choices that bargain or persuade |
| **Insight** | Scout find chance +2 points per rank; forecast accuracy +2% per rank | **Sharp ear:** one extra rumour or lead each morning | Reading the day's reports at the Commander's desk; tavern and street conversations; talks with Liliana; choices that ask or observe |
| **Know-how** | Processing and crafting time −3% per rank | **Trained eye:** see the quality odds before starting a processing job | Visiting Mae and Fulker while they work; helping in the Workshop in the evening; choices that offer practical help |

**How points work:**
- Each activity gives 1–2 points to its skill, **once per day per activity**, so skills grow steadily rather than by grinding.
- A dialogue choice tagged with a skill gives +2. The tags follow the bible's intent styles: taking responsibility is Leadership, bargaining Negotiation, asking and observing Insight, offering hands-on help Know-how.
- Rank costs are cumulative: 10 / 25 / 45 / 70 / 100 points.
- An engaged player reaches rank 3 in a favourite skill around Chapter 2, and all ranks 5 near the Eurydica charter.

**Ordinary activities (no minigames):**

| Activity | When and where | Gives |
|---|---|---|
| **Meals** (breakfast at HQ, lunch at the tavern or a stall, supper) | 07:00–09:00 / 11:00–14:00 / 18:00–22:00 | **Well-fed** until the next meal slot: walk +10%, an extra dialogue option in some talks. HQ breakfast with officers or adventurers counts as a talk. Tavern meals give a rumour. |
| **Talks at HQ** | Any time officers and adventurers are around; in the evening they're in their free-time spots | Leadership or Know-how points, officer friendship scenes (see below), adventurer Morale |
| **Reports at the desk** | Commander's room, evening | Insight points; a recap of the day's numbers and trends |
| **Walking the city** | Day and night; different NPCs by time | Requests, rumours, Negotiation, the romance NPCs |
| **Shopping and gifts** | Market by day | Gifts for romance NPCs; personal items |
| **Outings and dates** (romance NPCs) | Evening | Bond levels and scenes (A4) |
| **Help in the Workshop** | Evening, after Fulker joins | Know-how points |

**Money:** one guild purse. The Commander's personal spending is its own line in the Day Summary.

**Officers:** they're not romanceable, but they still have **friendship scenes**: short authored moments unlocked by talking with them over time. These give the same small department perks as A4's bonds, only with no romance (**owner to confirm**).

---

## Part B: open questions, contradictions and gaps (Codex audit)

The full audit is `GDD Audit 2026-09-27 (Codex).md`, with line-cited evidence and numbers. It found:
- **40 unresolved items:** the 10 in section 17, plus 30 more marked "carried over" or "not yet".
- **24 contradictions.**
- **The missing economy spec.**
- **A hook test.**

Claude reviewed it; the notes below say where we differ.

### B1. The hook test: the most important finding

The GDD has plenty of verbs but few **visible prizes**. On day 3, 10 and 25, a player can rarely finish "Tomorrow I want to ___, because that will let us ___" with a lasting change. Four small changes fix this, all reusing existing systems:

| | Change | Visible prize | Competing choice |
|---|---|---|---|
| **H1** | Recipe cards visible before the Workshop opens (at Beren's and Elsie's); inventory items show their uses | Boarhide Vest +30 HP/+8 DEF for Rowan, the Hunter Bow for Mira | Hides for gear, for Beren, for wages, or for the Dorm Annex |
| **H2** | Known hunting grounds shown as sources: target chance, materials, benefits | Boar Nest supplies two customers; paths shorten searches | Exploit boars, push to wolves (Hollis), or chase a rare |
| **H3** | Marta and Beren become **repeat customers** (a weekly order each) after their first request | A dependable buyer for familiar goods | Sell into a forecast peak instead, or craft |
| **H4** | The **Dorm Annex** (600G + 6 boar hides) is shown on the HQ map, with the waiting recruits named: beds 2 → 4 | Hire Aveline and Durgan; hunt and scout at the same time | Strengthen the current pair first, or invest in processing |

Plus **three player-pinned projects** in the Day Summary: one nearly done, one being funded, one beyond reach.

**Recommendation: adopt H1–H4 and pinning.** They also support the Commander layer: busking tips and town help feed the same projects.

### B2. Contradictions that need a decision (Claude's recommendation first)

1. **Company or guild (C01):**
   - Codex suggests keeping "Company", with "guild" as the Commander's analogy.
   - **Claude recommends "Guild" throughout**, tied to the rename (A1). The manuscript already says guild, and the bible's future "Guild Verified" needs it.
2. **When the officers join (C02):** the GDD says Valerie is never recruitable and Liliana arrives in Chapter 2, but the owner's story plan recruits Commerce, Crafting and Information in Chapter 1. **Recommendation:** officers join through the story, never through the recruitment pool. All three join in Chapter 1, in the order the player's interests trigger:
   - first sale or request completed: Valerie;
   - first scouting return: Liliana;
   - boar material seen: Fulker.
3. **The first flashpoint (C03):** the GDD says Blackfang, the story says the chimera. **Recommendation:**
   - the **Chimera is the Chapter 2 flashpoint**;
   - Blackfang becomes an optional Mosswood contract;
   - Ambermaw is Chapter 3 and Crownstone Chapter 4;
   - flashpoints never expire and a loss carries no Reputation penalty.
4. **"Victory" (C05):** Rank C plus the final flashpoint doesn't end the game, because the story continues to the frontier (Chapter 6). **Recommendation:** rename it "Eurydica charter complete". Play continues; Chapter 5 is the transition and Chapter 6 the move (1,500G, 48 hours, everything carries over).
5. **Beds and starters (C06):** the GDD lists four starters, but there are only two beds. **Recommendation:** Rowan and Mira first; Aveline and Durgan stay visible and become hireable when the Annex is built (H4).

The other contradictions are clerical: 25% versus 40% injured HP, "one tank and four behind" versus 3+3 slots, the leftover Pathfinder formula, stale references, and the skill-meter off-by-one. **Recommendation: fix them all as Codex lists** (audit section 2).

### B3. The missing economy and systems spec: adopt Codex's numbers as starting values

The audit proposes complete, mutually consistent starting rules. **Recommendation: adopt them into the GDD as starting values, balanced in the next proof.** They cover:

- **Materials and processing (§3.4):**
  - "Common value" means per unit;
  - a boar yields 2 meat + 1 hide;
  - quality odds by staff rank;
  - one job per processor, no spoilage, and a cutoff returns the job.
- **Equipment (§3.4):** 10 recipes that give every early material a use (Lure, Scout Map, Route Map, Boarhide Vest, weapons, Arrow Case, Reed Ward, Ridge Edge, Refinement). One weapon, armour and accessory upgrade per adventurer; enhancement levels 1–5, with elite parts needed at 4–5.
- **Market (§3.4):** listing slots 3/5/8 by Reputation, hourly shared buyers, demand Low/Normal/High, forecasts at 70/80/90% accuracy by clerk rank.
- **Staff and money (§3.5):**
  - wages taken from the roster;
  - staff ranks 1–3;
  - Morale effects on processing speed only;
  - Reputation is standing, never spent;
  - a debt rule with no game over.
- **HQ (§3.6):** Dorm Annex, Larger Dorm, a second processing table, a second workbench and trading shelves, with costs and effects.
- **Requests (§3.7):**
  - the state machine;
  - rewards for Hollis, Marta and Beren;
  - an exchange for rare slime parts, so a 20% drop can't fail a 2-day order;
  - Marta and Beren repeat orders;
  - eight optional subjugations.
- **Rules and systems (§3.1–3.3, 3.8–3.9):**
  - exact combat and tick rules;
  - Valencia's full kit (400G/120G, Chapter 2, Rank E);
  - Marsh and Redstone find tables and rares;
  - scout risk 1 / 1.5 / 2%;
  - the frontier transition contract;
  - saves (3 profiles, rotating autosaves);
  - Standard and Relaxed difficulty.

**Where Claude differs from the audit:**
- **Sleep.** It treats night as a flat 23:00 → 07:00 jump. With A3, the night is 23:00 → bed (at the latest 02:00), then a jump to 07:00. Recovery still advances the full 8 hours.
- **Its time-of-day NPC schedule** (night 20:00–23:00) should extend past 23:00 for the night city.
- **Its warning against relationship systems** is met by keeping bonds to six authored officer arcs with small department perks (A4), not a grind.

### B4. Section 17: answers (all from the audit, Claude agrees)

1. **Valencia:** confirmed as the first mage (Chapter 2, Rank E), kit in audit §3.2.
2. **The progression screen at Elsie's:** show every milestone and cost before buying; one free rebuild per adventurer, then 100G.
3. **Passives:** fixed, one per adventurer; the old skill points are removed.
4. **Scout risk:** Mosswood 1%, Marsh 1.5%, Redstone 2% per half-hour.
5. **Expedition items:**
   - A Lure gives +10 points of group chance.
   - A Scout Map gives +10 points of find chance.
   - Both take one 1×1 backpack cell and are used up.
   - The Route Map is reusable.
6. **Officers:** use the same combat model as everyone else, with the audit's officer stats.
7. **Marsh and Redstone find tables:** audit §3.3.
8. **Monster sprite order:** Moss Slime and Forest Wolf first, then the chimera and Blackfang.
9. **Rare sightings:** don't expire with time; one hunt uses a sighting up.
10. **Adventurer sprites:** Rowan and Mira first.
