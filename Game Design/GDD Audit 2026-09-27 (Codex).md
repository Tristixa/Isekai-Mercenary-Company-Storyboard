# IMC GDD v2.0 finalisation audit

Read-only audit, 27 September 2026. Design source: all 785 lines of the current GDD. Only this report and `handoff/gdd-audit-last.txt` were written; design and game sources were not edited.

## Verdict and reading key

**The GDD is ready to guide another operational proof, but not a complete campaign implementation.** Combat, scouting and presentation have substantial rules. The main missing design is what the resulting materials, money, relationships and company growth let the player do next. Finalise that connection before expanding the monster roster.

The highest-priority corrections are: reconcile the officer recruitment and chimera chapter plan; specify equipment, processing outputs, hiring and HQ capacity together; connect existing resident requests to lasting benefits; close combat/progression edge cases; and separate an Eurydica completion milestone from the Chapter 6 frontier transition. Section 17 alone is not the full decision backlog.

**Evidence labels:** “Read” means explicitly present in the cited source, not independently proven in the game. “Derived” is arithmetic from those rules. “Inference” is an interpretation or hypothetical playthrough. **Every recommendation and every new number below is a proposed starting design, not approved canon or a measured balance result.** Asset production and implementation tests are recommended future work, not work performed in this audit.

### Source register

Line numbers are 1-based physical lines as read on this date. `GDD Lx-y` identifies the design source. Supporting abbreviations below use the same notation. Links open the source file; the numeric ranges in prose identify the evidence.

| Key | Source and coverage |
|---|---|
| GDD | [Game Design/IMC GDD.md](<D:/Storyboards/Isekai Mercenary Company/Game Design/IMC GDD.md>), L1-785, read completely; SHA256 `32F483BB29BA3D222A28254D7ED7DC32348B447C07FEB6BBC09363E2060A2E2A` |
| Bible | [IMC_STORY_AGENT_BIBLE.md](<D:/Storyboards/Isekai Mercenary Company/IMC_STORY_AGENT_BIBLE.md>), L1-672, read completely |
| Chapter | [Chapter 1 - New Beginning.md](<D:/Storyboards/Isekai Mercenary Company/Game Design/Chapters/Chapter 1 - New Beginning.md>), L1-264; the only chapter implementation document found in that directory |
| S1 | [Scene 1 - Opening.md](<D:/Storyboards/Isekai Mercenary Company/Manuscript/Chapter 1 - New Beginning/Scene 1 - Opening.md>), L1-203 |
| S2 | [Scene 2 - Tavern Talk.md](<D:/Storyboards/Isekai Mercenary Company/Manuscript/Chapter 1 - New Beginning/Scene 2 - Tavern Talk.md>), L1-265 |
| S3 | [Scene 3 - Day 1.md](<D:/Storyboards/Isekai Mercenary Company/Manuscript/Chapter 1 - New Beginning/Scene 3 - Day 1.md>), L1-334 |
| S4 | [Scene 4 Day 2-5.md](<D:/Storyboards/Isekai Mercenary Company/Manuscript/Chapter 1 - New Beginning/Scene 4 Day 2-5.md>), L1-384; side dialogue, not a finished next milestone |
| R1 | [Requests/Chapter 1.md](<D:/Storyboards/Isekai Mercenary Company/Requests/Chapter 1.md>), L1-63 |
| RND | [Requests/No Deadline Requests.md](<D:/Storyboards/Isekai Mercenary Company/Requests/No Deadline Requests.md>), L1-54 |
| RR | [Requests/README.md](<D:/Storyboards/Isekai Mercenary Company/Requests/README.md>), L1-25 |
| RRE | [Requests/Recurring/Eurydica.md](<D:/Storyboards/Isekai Mercenary Company/Requests/Recurring/Eurydica.md>), L1-22 |
| Roster | [Adventurers and Staff Roster.md](<D:/Storyboards/Isekai Mercenary Company/Characters/Adventurers and Staff Roster.md>), L1-175 |
| Owner | [Progression conversation.md](<D:/Codex/Progression conversation.md>), L1-211; the owner's chapter correction is L118; the hook test is L109 |
| Legacy pointer | [imc-playground/docs/GDD.md](<D:/Godot Projects/imc-playground/docs/GDD.md>), L1-7, redirects to v2.0; no old balance values were silently imported |

All four Chapter 1 manuscript files and all four request files were read completely. No external proof URL was evaluated and no game simulation was executed: “Proven” below is the GDD's status, not a fresh audit result. The chapter folder does not supply Chapters 2-6; their planned structure comes from the owner and task handoff. The Bible's referenced world-canon handoff and external creative references were not needed to adjudicate these mechanical questions.

## 1. Open questions and recommended answers

### 1.1 All ten questions in section 17

| ID | Open item and evidence | Recommended answer | Reason |
|---|---|---|---|
| O01 | Valencia and eight modifiers; GDD L210-230, L748 | Confirm the proposed support mage for Chapter 2 at Rank E; use the complete kit and modifier table in §3.2 below. Preview her during Chapter 1. | A visible support recruit gives Rank E a specific party-building payoff. |
| O02 | Experience spending screen unproven; GDD L244-280, L749 | Keep four tracks, `100 × destination level` costs and 12,000 lifetime cap. At Elsie's, show all milestones, stat deltas, balance and total cost; commit purchases together. Select modifiers explicitly; permit one free rebuild per adventurer, then 100G. | A wrong early click should not permanently ruin a hand-designed character. |
| O03 | Learned vs fixed passives; GDD L313, L750 | Keep one fixed innate passive per authored adventurer. Remove old skill points and Pathfinder levels. Progression modifies the signature skill only; a Route Map can give the old search benefit. | Avoid two competing progression systems and obsolete references. |
| O04 | Deferred scouting risk; GDD L432-445, L751 | Initial half-hour injury chances: Mosswood 1%, Marsh 1.5%, Redstone 2%; Red Fatigue doubles them. All are 48-hour injuries and 40% return HP. No serious-injury tier in Eurydica. | Modest, legible risk is enough until the full economy can absorb injury downtime. |
| O05 | Lures, maps and backpack; GDD L197, L495, L752 | Both occupy 1×1. Consume one assigned lure at hunt departure for +10 percentage points to target group chance; consume one Scout Map for +10 points to find chance. Route Map is reusable, 1×2, −5% search time, strongest only. See §3.4 for costs and stacking. | Existing preparation can support a clear yield-versus-safety choice. |
| O06 | Officer vs adventurer combat; GDD L531-536, L577-580, L753 | Use the same attack timer, action queue, meter and status rules for everyone. Tristitia gains 25 meter per completed normal attack, even if visually a two-hit combo; Piercing Verdict is the next action after four normal attacks. Elsie uses defender meter. Proposed officer numbers appear in §3.1. | Watching a cinematic must not switch the simulation model. |
| O07 | Marsh/Redstone finds and rares; GDD L414, L754 | Adopt the two complete proposed tables in §3.3: three landmarks, two paths, one hint and two rare sightings each. | Reuse the proven discovery structure without introducing a separate system. |
| O08 | Monster sprites missing; GDD L606-611, L625-643, L755 | Production order: Moss Slime and Forest Wolf, Mossback recolour and Silvermane, chimera and Blackfang, then each next region's ordinary three, boss and two rares. One engine-animated still per monster; nine ordinary-variant palettes. | Fix the first playable economy and story climax before broad asset production. |
| O09 | Sighting expiry; GDD L421-425, L756 | No passive time expiry. A sighting reserves one hunt, permits at most one rare encounter/corpse, and is consumed when that hunt ends. If missed or defeated, scout it again. Allow scouting after 100% for sightings. | Prevent rare-farming ambiguity and avoid pressure competing with an already busy tutorial. |
| O10 | Four adventurer sheets absent; GDD L177-186, L757 | Produce Rowan and Mira first, then Aveline and Durgan. Each needs four-direction idle/walk, battle idle/attack/signature/hurt/guard/victory/defeat and portrait expressions per Roster L26-40. Keep stand-ins only in labelled proofs. | The initial recruitment pair must be identifiable before later roster growth. |

### 1.2 Unresolved, deferred or incomplete carried-over items elsewhere

This inventory includes production deferrals because the handoff asks for every unresolved item. “Keep out of scope” is a concrete recommendation where a feature is optional; it is not an assertion that the feature is implemented.

| ID | Evidence | Recommended answer | Reason |
|---|---|---|---|
| O11 | Player/company names are placeholders; GDD L34 | Player name at the S1 prompt; company name at founding, default “the Company”; 1-24 displayed characters, editable at HQ. Replace both legacy tokens from saved state. | Resolves manuscript substitution without inventing a canonical name. |
| O12 | Grey NPCs, merchant stall, night NPC pass; GDD L35-39 | Give the three proof request-givers their own sprites and portraits and finish the stall first. Morning 07:00-12:00, day 12:00-18:00, evening 18:00-20:00, night 20:00-23:00. Schedule S4's ambient NPCs accordingly; no rewards or required order. | Closes the time-of-day deferral while preserving optional town life. |
| O13 | Facades awaiting review then approved; GDD L37-38 | Mark the 11 building facades approved; retain “candidate” specifically for roofs/props not explicitly covered by approval. Camera north is settled. | Do not reopen a settled camera choice or infer approval of every asset. |
| O14 | HQ interior and expanding departments; GDD L149-154 | Use the capacity/cost table in §3.6; start with two beds and separate officer work corners, add department rooms with their Chapter 1 arrivals. | A physical house needs a matching staffing rule. |
| O15 | Elsie batch 2 pending; GDD L161, L580 | Finish idle, hurt, guard, victory and defeat using the already decided longsword/martial-arts kit. | No weapon decision remains. |
| O16 | Durgan's future shield/hammer; GDD L186; Roster L98 | Change outfit at the start of Chapter 3 as a story presentation change; retain current passive/skill and statistics. | Prevent a cosmetic plan from silently changing balance. |
| O17 | Support caster kinds described but not built; GDD L210-230 | Implement Valencia's buff kit only for first Eurydica release; no generic healer/debuffer/offensive-mage recruitment without authored characters. Her Toughness milestone offers limited healing. | Defines an implementable support scope without filler characters. |
| O18 | Progression effects lack some magnitudes and interactions; GDD L247-313 | §3.2 defines base-level treatment, all missing Mira magnitudes, modifier choice/prerequisites, stacking, respec and XP abuse protections. | Numeric tables do not yet resolve execution semantics. |
| O19 | Rest, injuries and leaving carried over; GDD L315-335, L685-699 | Daily rest assignment, real calendar hours through the 8-hour night, post-debit fatigue, one payroll liability per employee, equipment return and non-compounding arrears; see §3.5. | Avoid lost operating days and recovery softlocks caused by timing ambiguity. |
| O20 | Backpack carried over with only one synergy; GDD L337-338 | Specify footprints, active equipment limits, rotation, adjacency and potion timing in §3.4; keep only 4×4 and 5×4 Eurydica packs. | The old system cannot be rebuilt from one example. |
| O21 | Find eligibility, main den and repeatability implicit; GDD L355-414 | Threshold checks after adding exploration; 75% reveals the first missing den in table order; 100% reveals remaining fixed finds. Found unique entries leave the pool. Repeat surveys add no exploration but can find rares. | Resolves empty-table and fully-charted-area failures. |
| O22 | Rare corpse processing/value/encounter behaviour; GDD L423-430, L610-611 | Mossback 60 min and Silvermane 75 min; rare carcasses yield three common parts and one guaranteed rare part; define listed 60G/75G as raw-carcass reference value. Rare encounters once per reservation. | Rare hunting must have a complete loot and income route. |
| O23 | Pathfinder in active formula, probability notation and group roll ambiguity; GDD L458-459, L494-495 | Use exploration as `e = percent/100`; normalise den weights; third monster only rolls if second joined; clamp group chance to 95%; remove Pathfinder levels. §3.1 supplies exact formulas. | Different reasonable readings produce different encounters. |
| O24 | Future reach attacks; GDD L482 | No back-row bypass attacks in the first Eurydica release, except existing provoke redirection. Add future reach enemies only with a visible prep warning and authored target rule. | The tank/support promise needs a stable first implementation. |
| O25 | Placeholder combat VFX; GDD L548-554 | Retain specified hit-stop and skill push-in; provide slash, thrust, blunt and spell effect families; effects never drive simulation timing. Include reduced shake/flash and disable cinematic zoom options. | Production polish should preserve the watch/unwatch invariant. |
| O26 | Variant chance boosts and elite-part library absent; GDD L588-600 | Keep 8% baseline; give Mosswood's Howling Ridge a clearly listed +4 percentage-point area bonus as a proposal, cap all boosts at 20%; nine elite IDs map to ordinary species. Values and uses in §3.4. | The exciting drop needs a visible destination; avoid an unbounded item catalogue. |
| O27 | Variant experience still called open; GDD L597 vs L256-266 | Use the existing ×2 variant, ×3 rare and ×5 boss multipliers once only; remove obsolete “once experience exists.” | This question is already answered elsewhere. |
| O28 | Marsh/Redstone stats untested; GDD L625-641 | Retain current stats as provisional, add XP/group values in §3.3, and validate equipped parties before calling either area proven. | Mosswood's three-person sample cannot establish later-area safety. |
| O29 | Regional boar recolours optional; GDD L643 | Keep them as art experiments, not extra canonical species in the initial nine-ordinary roster. | Avoid expanding the item and find tables for an available asset. |
| O30 | Eight subjugations, ten deliveries and repeatable slots carried over without content links; GDD L647-659 | Adopt seven actual current request IDs, add the two proposed recurring work orders in §3.7, and use the explicit optional contract roster below. Retire the unexplained “ten” and “eight authored” claims until indexed. | Counts without traceable content are not build specifications. |
| O31 | Processing carried over; GDD L143, L665 | Fix yields, qualities, times, queue ownership, no spoilage and cutoff refunds as §3.4. | Processing is the dependency for requests, crafting and cash flow. |
| O32 | Forecasts and rumours carried over; GDD L164, L666 | Use one-day forecasts at clerk rank 1, two/three at ranks 2/3; calibrated coarse demand signals plus material-use links; rumours reveal opportunities, never grant verified discoveries. §3.4. | Information needs actionable value without secretly creating demand. |
| O33 | Commerce carried over; GDD L667 | Define shared daily demand, willingness-to-pay, hourly quantity, fee rounding, listing reservations and cumulative sales reputation in §3.4. Retain the 50% walk-up fallback. | A listing interface alone cannot simulate a market. |
| O34 | Production focus and enhancement carried over; GDD L668 | One explicit queued job per workbench; focus filters recipes, not free daily output. Ten recipes, enhancement levels 1-5, deterministic costs/effects below. | Make “craft” mean a specific useful output. |
| O35 | Staff rank/hiring/wages unspecified; GDD L665-669, L686 | Import the three named staff's hire/wage numbers from Roster explicitly; three staff ranks with service-earned promotion and bounded bonuses, §3.5. | Preserves existing characters and closes recurring expense math. |
| O36 | Rank, loans and victory carried over; GDD L689-699 | Reputation is a non-spent standing; promotions charge gold only. Rank C plus Chapter 4 flashpoint is Eurydica completion, not campaign end. No-interest rescue loan has a recoverable default rule, §3.5/3.8. | Avoid both premature credits and unrecoverable insolvency. |
| O37 | Story service milestones carried over without events; GDD L703-715 | Keep IDs, define event predicates and independent officer branches in §3.7. Add Processing, Commerce and Information, which are missing from the table. | Story gating must not become an accidental fixed tutorial chain. |
| O38 | Carried-over screens and unimplemented HQ walking; GDD L734 | Give each screen an owner, data, commit/cancel behaviour and pause policy (§3.9); HQ walk opens the same screens as optional shortcuts. | Navigation names are not interaction contracts. |
| O39 | Recolourable recruits parked; GDD L760 | Exclude generated/recoloured recruits from the authored Eurydica roster; no palette-picker feature in this scope. | Matches the permanent, individually designed character rule. |
| O40 | Open camera/weapon/departure wording in historical entries; GDD L768-785 | Preserve history labelled “superseded”; north camera, longsword Elsie, temporary wage departure and current four-track progression are the active decisions. | An old log entry is not a second active rule. |

The GDD contains no literal “TBD,” but its omitted economy parameters are just as unresolved. The supporting requests do contain explicit TBDs; §3.7 resolves their client identities, rewards, items, deadlines, delivery and relocation behaviour. Fixed, numeric carried-over rules such as 30-minute contract approach and the 23:00 ordering are retained unless a conflict below requires clarification.

## 2. Contradictions, stale statements and scope tensions

“Conflict” means incompatible active instructions. “Ambiguity” or “gap” means multiple readings or missing detail; it should not be represented as a proven contradiction.

| ID / kind | Evidence and consequence | Recommended resolution |
|---|---|---|
| C01 — terminology drift | GDD L47-49 establishes a mercenary/adventurer company. S2 L128-172 has the outsider propose a guild; S4 L61, L119, L147-159, L174-181 calls the actual institution a guild. Bible L54 correctly says no pre-existing adventurer guild. | Keep “guild” as the outsider's proposed analogy in S2; use “Company” for its current institutional name and saved company-name token. This is inconsistent naming, not evidence of a rival existing guild. |
| C02 — direct story conflict | GDD L167 says Valerie is never recruitable; Owner L118 says Chapter 1 recruits the Commerce officer. GDD L152 delays Liliana's office to Chapter 2, while the owner puts Information in Chapter 1. | “Officers join through story, never through the employee recruitment pool.” All three join in Chapter 1; Liliana can get a larger dedicated room in Chapter 2, but her service works before then. |
| C03 — campaign conflict | GDD L655-657 names Blackfang as first flashpoint; Owner L118 specifies the Mosswood chimera in Chapter 2. S2 L75-80 and S4 L129-132 establish the chimera already affecting the region. | Chimera is the Chapter 2 flashpoint. Reclassify Blackfang as an optional Mosswood boss contract. Retain Ambermaw/Crownstone for Chapters 3/4 as a proposed mapping. |
| C04 — missing gate conditions, not numerical impossibility | GDD L693-695 grants Marsh at 200 Rep and Redstone at 700, but flashpoints start at 300/800/1,400 (L655-657). Rep gates alone allow a Rank F company to see the Marsh boss offer without paying promotion or visiting Marsh. | Keep early region previews and access; require the target area's rank, chapter and preceding flashpoint explicitly. Do not claim that region-before-boss access itself is an error. |
| C05 — campaign endpoint conflict | GDD L698 calls Rank C + final flashpoint + no debt “Victory,” while Owner L118 continues to Chapter 6 frontier; Bible L105-123 continues around Chapters 6/7. | Rename it “Eurydica charter complete.” Set relocation to Chapter 6 per the owner; Chapter 7 verification authority can remain a distinct later event. |
| C06 — capacity ambiguity | GDD L152 and S3 L272-280 have two adventurer beds. GDD L181-186 names four starters; Roster L44 says they are hired at M02, whereas S3 L330 offers Mira and one male swordsman. | Four is the starter pool, not simultaneous starting employment. Rowan/Mira available first; others remain visible and hireable after capacity expansion. Identify Rowan explicitly; his current art is a sword/coat, not the shield user wording in S3. |
| C07 — direct combat geometry conflict | GDD L467 promises one tank with four behind; L471 limits each row to three slots. | Retain 3+3 slots/up to five total; correct the example to two front + three back, or one front + at most three back. |
| C08 — direct health conflict | GDD L323 returns injured scouts at 25% HP; L439 says 40%. | Hunters return at 25%, scouts at 40%; both 48 hours. |
| C09 — removed mechanic survives | GDD L313 replaces skill points and treats Pathfinder as possible item/passive; L458 still subtracts Pathfinder skill levels, and L750 asks about restoring the old tree. | Fixed innate passives, four-track spending, one Route Map bonus; delete Pathfinder-level arithmetic. |
| C10 — officer skill timing conflict | GDD L531-536 uses attacker meters but retains “today every third action”; L577 and L753 specify/offer every third. | One meter rule with explicit combo semantics; treat proof-2 every-third behaviour as historical. |
| C11 — off-by-one skill description | GDD L525 says the next action after full meter is the skill; L531 adds 25 per hit but says about every fourth attack. | With an empty 100-point meter: normal actions 1-4 fill it, action 5 is the skill. Skills do not refill themselves. |
| C12 — outdated progression status | GDD L597 calls XP not yet existent; L256 and L779 say earning is built. | Mark earning implemented-in-proof; spending/milestone selection unproven. |
| C13 — stale Day 1 assumption | GDD L369 suggests Day 1 slimes plus scouting/two scouts; L709-713 puts scouting at M06, later than Workshop M05; Chapter L183 stops the current slice before the first recruitment event. | Distinguish proof sandbox from campaign. Bring basic scouting after first hunt independently of Workshop; never promise it in the current morning-only build. |
| C14 — asset pipeline conflict | GDD L64 says all 3D work retired but L28, L67-69 and L741 require 3D environments/project. L87 mandates 8×8 snapping while L93 selects painted full-resolution art. | Retire 3D *character* production and the old fully 3D visual direction; retain 3D scene volumes. Full-resolution painted environment is current; snapping text belongs to history. |
| C15 — status contradiction already resolved later | GDD L37 says facades await review, L38 approves them. L769 keeps a historical open camera. | Mark each asset's latest status; do not ask for north-camera confirmation again. |
| C16 — content count mismatch | GDD L649-650 claims eight authored subjugations, ten deliveries and repeatable slots. Current Requests has seven CH1-REQ IDs; RRE L3 explicitly says none recurring designed. | The listed source set does not substantiate those counts. Index imported legacy content before calling it current; do not assert the old content never existed elsewhere. |
| C17 — request-client contradiction | R1 L25 says inn owner; L31 refers to a noble and L33 flags the inconsistency. GDD L650 supplies no current client list. | Make CH1-REQ-002 a noble household's garden steward; keep unnamed until narrative naming, with a fixed client ID and garden delivery destination. |
| C18 — rest cadence ambiguity | GDD L319 assigns 24-hour rest at closeout; L685-687 nests rest assignment under “Weekly closeout.” | Daily 23:00 rest assignment, weekly payroll only. Otherwise four bars cannot support ordinary weekly operations. |
| C19 — loot ordering conflict at wipe | GDD L461 secures a corpse as soon as a monster falls, but L464 excludes the “final exchange”; L510-518 has replaced simultaneous exchanges with serial actions. | Every completed kill grants its corpse immediately, even if a later enemy action wipes the party. Interrupted, uncompleted attacks grant nothing. |
| C20 — stats snapshot ambiguity | GDD L508 fixes fight stats at fight start, but L238-240 and L577-582 apply buffs, slows and provoke during the fight; Big Game Hunter (L195) depends on target tier. | Snapshot gear, fatigue and base progression at fight start; evaluate temporary effects per action. Resolve Big Game Hunter against the queued target, not as a permanent whole-fight buff from one variant. |
| C21 — historical measurements mixed | GDD L520 reports queued fights about 23 company minutes; L621-623 still presents 19 minutes and about 40 watched seconds as current. | Label the 19-minute batch result historical. At the stated clock, 23 minutes is 46 watched seconds; neither sample establishes all-party safety. |
| C22 — arithmetic typo | GDD L369 says old 30%-per-trip scouting charted an area in five scouts. | It takes four full trips from 0, not five; current 12%-per-trip takes nine. |
| C23 — rest of “nobody lost” history | GDD L785 says no quitting over wages; active L328-331 permits leaving and unlimited rehire. | Say no *permanent* departure; retain temporary unpaid-wage leave. |
| C24 — stale references/UI copy | GDD L205 points to nonexistent 10.4 instead of 10.0; L414 points to question 6 instead of 7; L520 points to nonexistent 4.4; L562 labels only slot 1 FRONT despite multiple front slots. | Correct references to 10.0, question 7 and section 4; tag every front member per L480. |

Already reconciled or not contradictions: Bible L54 has already removed the old “guild presence” claim (GDD L29); bandits in S1/S2 do not violate GDD L349's restriction on *monster species*; scene-specific camera cuts do not necessarily violate the fixed gameplay camera; the proof's closed Service Lanes (GDD L26) is a slice boundary, not proof that Marta can never appear; the Chapter handoff's deferred list (L249-264) is not a ban on designing the rest of Chapter 1.

## 3. Build gaps and proposed starting specifications

These are recommendations for finalising the document, not changes to source files. Proposed numbers close design decisions; balance still needs an integrated proof. A value already read from the GDD or Roster is identified as retained/imported.

### 3.1 Combat, clock and expedition semantics

**Gap:** GDD L132-143, L458-536 and L577-582 have most individual rules but not one complete deterministic resolution contract.

- One global company clock and stable per-operation random stream. Watching changes clock speed only. Hit-stop, camera and animations cannot change RNG calls, damage, elapsed company time or rewards. At 1× a 16-hour unwatched day is 480 real seconds; a fully battle-paced day would be 1,920 seconds, so cinematic pacing must be optional.
- Resolve a tick in the retained order: completed action/damage, timers and operation completions, cutoff. At equal readiness, front slots 1-3, back slots 1-3, then enemy slots. Downed queued actors are removed. Resolve damage at action end; an action interrupted by recall/duration/cutoff does not deal damage, while prior completed kills remain secured. A contract killed exactly at 23:00 succeeds. Recall immediately ends the operation; a hunt reaching its selected duration returns immediately, including during battle.
- Hunt duration choices 1, 2 or 3 hours; scouts 30-minute increments to 3 hours. The displayed finish time includes the 30-minute approach for contracts. No separate hunt return-travel charge in Eurydica. New actions at 23:00 are forbidden, including attempts to exploit the cutoff boundary.
- Search minutes: `max(10, (30 × (1 - 0.25 × e) - 5 × paths) × routeMapMultiplier)`, `e` in [0,1], map multiplier 0.95 or 1. Round elapsed timers up to the 12-second tick. At 0%/0 paths = 30 minutes; at 100%/2 paths = 12.5 minutes before tick rounding (12.6 after). A den multiplies that species' encounter weight by 1.5, then all weights normalise. If only one ordinary species is known it gets probability 1. If targeting a reserved rare, allocate 0.7 to it and 0.3 among known ordinary species before den weighting of the ordinary share; the rare probability stays 0.7.
- Let `c = min(0.95, base + target-den 0.15 + Tracker 0.10 + lure 0.10)`, including each bonus only when its prerequisite is present. Roll second at c, third at c/2 **only after second succeeds**; encounter members are the selected species. Non-target ordinary encounters use base c only. Expected group size is `1 + c + c²/2`. Multiple Trackers never stack. An encountered rare is solo and may appear once; continue ordinary encounters for remaining hunt time after it dies. If it has not appeared, each completed search gets another 70% opportunity until hunt end.
- Skill meter 0-100; reset between fights unless a modifier explicitly sets a starting value. Skills consume 100 at action start and generate no meter from their own damage; basic attacks give 25 once per completed action, defender meter gains 20 per enemy damage action received, mage meter accrues continuously in combat at `100/(4 × current attack interval)` per second. No out-of-combat charge. A stun consumes readiness, lasts 12 seconds, restarts the attack gauge and counts as that fighter's lost action.
- Same-stat buffs use the strongest magnitude and longest remaining duration, never add duplicates. Up and down effects multiply; damage-taken modifiers apply after the GDD damage formula with a minimum of 1. New effects do not lose one duration immediately on the action that applied them. Slow is an interval multiplier, not a rate penalty. Provoke uses newest valid source; when it ends, target assignment returns to the row rule. Stun refreshes remaining skips to the greater value; two overlapping two-action stuns do not become four.
- Proposed officer encounter kit: Tristitia HP 360, ATK 38, DEF 24, rate 1.2, melee attacker; Elsie HP 420, ATK 30, DEF 36, rate 1.0, melee defender. These are story guest values, not hireable units. Rose Waltz deals one normal attack's total damage in two visual hits; SPD UP +20% for three recipient actions to one seeded-random living ally. Piercing Verdict deals 2.5× normal damage and DEF −25%, interval ×1.5 for three target actions. Hateful Slash deals a normal hit to the front enemy and provokes all living enemies for two of each enemy's actions. Officers occupy normal party slots and grant no permanent XP; a story formation containing them must still be previewed.
- Hunt risk remains qualitative, not a fake precise survival percentage (GDD L433, L522). Use a fixed-seed ensemble separate from gameplay RNG: 100 complete simulated hunts using the proposed party and configured duration; Low if under 5% have any downed member, Moderate 5%-under 25%, High otherwise. Show main causes and mark advice approximate. Scout probabilities use `1-(1-p)^n`, not `n×p`; findings and progress resolve before injury on each interval so the return retains that interval's rewards.

**Verification needed, not performed:** same-seed watched/unwatched equivalence; simultaneous-tick kill/cutoff; recall during skill; downed queued actor; multiple provoke sources; partial scout interval; three-enemy and mixed-variant target transitions. An ensemble rating is a recommended implementation, not a promise the existing proof computes it.

### 3.2 Experience, modifiers and Valencia

**Gap:** GDD L247-311 specifies costs and most examples but leaves base treatment, build locking, several effect values and modifier interactions unstated.

Keep level 1 as baseline: level n provides `(n-1)` increments. Compute ATK/HP/DEF from the listed base, additive track percentages, flat equipment, then multiplicative encounter/status effects; round damage only at the existing damage formula. Speed modifies rate, then interval rounds to a tick. Focus multiplies every role's meter gain, including mage time gain. These are separate from company rank and staff rank.

Cumulative cost 1→5 is 1,400; 1→8 is 3,500; 1→10 is 5,400. Two rank-1 modifiers and one rank-2 modifier are **chosen**, not silently assigned by which button the player clicked first. A rank-2 choice requires that same track's rank-1 choice. All track stats apply regardless of modifier slots. Display effective attack-interval ticks as well as percentage gains: a small Speed increase may not change the rounded interval immediately. Respec refunds spent XP into the same person's spendable pool without changing lifetime XP; no stat gains from unspent XP. At the 12,000 cap, stop new awards, not the ability to spend old XP. At departure do not grant XP immediately: award the +10 deployment bonus once on a completed fight or completed scout interval, to prevent instantaneous recall farming. This deliberately changes GDD L260. Scouting's +4 per interval/+10 per find belongs to its sole scout. Ignore cosmetic repeat hints for find XP. Downed adventurers retain previously earned XP, and get none for subsequent kills while down.

Complete missing examples: Mira Toughness rank 1 gives +25% DEF for two actions; rank 2 applies −20% target ATK while Frost Arrow's slow lasts. Her rank-1 Power means 1.5× a normal hit, not an additional multiplier on other modifiers. Aveline's Focus elite bonus multiplies signature damage by 1.5 after her 2.5×/3× coefficient. Rowan counterattacks resolve as immediate retaliation inside the incoming action, use normal damage against the attacker with 0.5×/1× Rowan ATK, and trigger no meter or further counter. Rowan Focus rank 2 taunts for Phalanx's remaining duration. Durgan Power rank 2 and Focus rank 2 both produce a maximum two skipped actions, never four. Multi-target modifiers use the front target plus the next living enemy; “all” hits each once.

**Proposed Valencia kit:** HP 150, ATK 14, DEF 9, rate 0.9; ranged mage, basic arcane bolt uses the same damage formula. Hire 400G, wage 120G/week; available at Chapter 2 and Rank E, previewed earlier. Fixed passive **Measured Casting:** +10% mage meter fill; no extra skill tree. Verdant Blessing retains +25% ATK/DEF for the front row's next three individual actions (GDD L227). No overheal; an empty/dead front row makes it target living back-row members instead.

| Track | Rank 1, level 5 | Rank 2, level 8 |
|---|---|---|
| Power | Blessing ATK bonus becomes +35% | While blessed, each recipient deals +15% damage to Elites |
| Toughness | Blessing also heals its recipients for 10% max HP | Its DEF bonus becomes +40% |
| Speed | Blessing also gives +15% attack rate | Blessing targets all living allies |
| Focus | Blessing lasts five recipient actions | After casting, Valencia retains 25 meter |

Her modifiers preserve the same two-rank-1/one-rank-2 limit. Preview actual recipient statistics in preparation. Roster L173-175 explicitly leaves her identity confirmation open; this recommendation does not canonise a new appearance or biography.

### 3.3 Scouting, find tables and later-area completeness

**Gap:** GDD L373, L401-414 promises three landmarks and two paths per area, but only Mosswood is authored; later groups, rares and XP are missing (GDD L625-641).

All tables below are **proposed working names/content**, not read canon. Use the same 45% find roll, +10 percentage points from Tracker, plus selected Scout Map, cap 80%. Add exploration before checking eligibility; remove discovered unique finds from the weighted pool. A hint is eligible only if an unidentified ordinary monster is within 20 percentage points of its threshold; it can display once per unidentified species and grants no find XP. If nothing is eligible, show “No new lead” and award no find XP. A sighting already active/reserved cannot be duplicated. At 100%, current scouts return; the UI then offers a clearly labelled repeat survey for rare leads, with unchanged stamina, injury and XP rules but no exploration progress. Do not remove the ordinary hunt option or land benefits at 100%.

| Amber Marsh find | Kind | Eligible | Weight | Lasting effect |
|---|---|---:|---:|---|
| Reedcutters' Causeway | Path | 10% | 3 | Search −5 min |
| Serpent Reedbed | Den | 15% | 3 | Serpent encounter weight ×1.5; target group chance +15 points once known |
| Dry Islet | Landmark | 30% | 2 | Scout injury chance ×0.75 in this area |
| Raised Towpath | Path | 40% | 2 | Search −5 min |
| Stalker Hollow | Den | 55%, Stalker known | 2 | Stalker weight ×1.5; target group +15 points |
| Fresh marsh tracks | Hint | Within 20 points of next identification | 2 | Hint only |
| Reedcoil Elder | Rare | Serpent known | 1.5 | One sighting |
| Pale Marsh Stalker | Rare | Stalker known | 1 | One sighting |

| Redstone find | Kind | Eligible | Weight | Lasting effect |
|---|---|---:|---:|---|
| Quarry Steps | Path | 10% | 3 | Search −5 min |
| Highland Wolf Lair | Den | 15% | 3 | Wolf weight ×1.5; target group +15 points once known |
| Sheltered Cairn | Landmark | 30% | 2 | Scout injury chance ×0.75 in this area |
| Miners' Traverse | Path | 40% | 2 | Search −5 min |
| Drake Roost | Den | 55%, Drake known | 2 | Drake weight ×1.5; target group +15 points |
| Fresh ridge tracks | Hint | Within 20 points of next identification | 2 | Hint only |
| Redmane Alpha | Rare | Highland Wolf known | 1.5 | One sighting |
| Old Ridge Drake | Rare | Ridge Drake known | 1 | One sighting |

Retain Mosswood's existing table; 75% reveals Dire Boar Nest if missing, otherwise Howling Ridge if missing. Equivalent second-species den, then third-species den order in other areas. Den discovery does not bypass the 25%/50% monster-identification gates. 100% reveals fixed landmarks/paths, not rares. O26's proposed +4-point variant benefit belongs to Howling Ridge in addition to its current effect; present it explicitly, not as an assumed existing effect.

| New rare | HP / ATK / DEF / rate | Processing | Raw value | Base XP before ×3 |
|---|---|---:|---:|---:|
| Reedcoil Elder | 1,320 / 17 / 25 / 1.0 | 90 min | 110G | 55 |
| Pale Marsh Stalker | 1,680 / 20 / 30 / 1.1 | 105 min | 140G | 65 |
| Redmane Alpha | 2,280 / 26 / 36 / 1.1 | 105 min | 180G | 80 |
| Old Ridge Drake | 3,000 / 30 / 50 / 0.9 | 120 min | 225G | 95 |

Retain normal/boss stats in GDD L629-641. Proposed ordinary group chances: Marsh Slime 60%, Serpent 40%, Stalker 50%; Stone Crawler 40%, Highland Wolf 70%, Ridge Drake 30%. Bosses and rares are solo. Proposed base XP: Marsh Slime 18, Serpent 24, Stalker 30, Ambermaw 110; Crawler 32, Highland Wolf 38, Drake 48, Crownstone 180. Apply tier XP multipliers once, not to already-multiplied values. No cross-area rare-spawn lottery or additional regional boars.

### 3.4 Processing, equipment, backpack, information and commerce

**Gap:** GDD L338, L600 and L663-669 cannot currently connect a corpse to a specific piece of equipment or a predictable customer transaction.

#### Material and processing contract

Treat “Common value” in GDD L604-641 as **per common unit**, not per corpse; add that heading explicitly. Material quality value multipliers: Pristine 1.25, Standard 1, Damaged 0.5, Unsellable 0; requests marked “any condition” may consume even Unsellable units, but crafting/food require Standard or better. One quality roll applies to every output in that processing job. Proposed staff-rank probabilities (Pristine/Standard/Damaged/Unsellable): rank 1 = 10/70/15/5%, rank 2 = 20/70/8/2%, rank 3 = 30/65/5/0%. No Morale effect on quality, only processing speed, to avoid compound randomness.

Keep three total common units per ordinary carcass and one 20% rare roll. In particular **boar yields 2 meat + 1 hide, not three of each**. Two boars can therefore supply Marta's four meat and Beren's two hides. Other ordinary species give three of the listed common unit. Rares give three parent-species common units plus a guaranteed parent rare; bosses give five common plus one boss rare. Variants give their ordinary outputs/rare roll plus one guaranteed elite unit. Recipe inputs accept Standard/Pristine equally; no extra “quality gear” roll. Roll quality and rare output from the persistent corpse identity so cancel/reload cannot reroll it.

| Species | Common unit(s) | Rare unit, base value | Elite variant unit, base value |
|---|---|---|---|
| Moss Slime | Slime Gel (alias “common slime part”), 8G | Slime Core (alias “rare slime part”), 40G | Elite Slime Core, 80G |
| Dire Boar | Boar Meat / Boar Hide, each 12G | Boar Tusk, 60G | Elite Boar Tusk, 120G |
| Forest Wolf | Wolf Pelt, 16G | Wolf Fang, 80G | Elite Wolf Fang, 160G |
| Marsh Slime | Marsh Gel, 18G | Marsh Core, 90G | Elite Marsh Core, 180G |
| Marsh Serpent | Serpent Scale, 22G | Venom Gland, 110G | Elite Venom Gland, 220G |
| Marsh Stalker | Stalker Hide, 28G | Stalker Claw, 140G | Elite Stalker Claw, 280G |
| Stone Crawler | Crawler Plate, 30G | Crawler Core, 150G | Elite Crawler Core, 300G |
| Highland Wolf | Highland Pelt, 36G | Highland Fang, 180G | Elite Highland Fang, 360G |
| Ridge Drake | Drake Scale, 45G | Drake Heart, 225G | Elite Drake Heart, 450G |

Rare and elite values here are proposed multiples (5×/10× common unit), not read values. Boss common parts retain 30G/45G/65G for Blackfang/Ambermaw/Crownstone, with boss rare parts at 150G/225G/325G. Chimera uses five Chimera Hide at 30G and one Chimera Heart at 150G. These are tradable trophies; no mandatory unique-boss material is required to recover from failure or build baseline gear.

One processor, one active corpse, up to 20 queued jobs; no staff multi-assignment. Storage holds unlimited materials/corpses for Eurydica; no decay or hidden overflow. Queue output respects input reservations and FIFO unless reordered. Base times are GDD monster times, multiplied by staff speed and Morale duration factors, rounded up to the tick. Ordinary variants use their parent's time. Rare times are O22/§3.3. Cosmetic quality never prevents the guaranteed elite unit from satisfying enhancement; no additional elite-only special requests are required in this first specification. Cutoff aborts the active job, returns inputs and requeues it for next morning, retains its rolled outcome, with a warning before starting something that cannot finish. No overnight processing. Automatic sales never touch recipe/request reservations.

#### Equipment, recipes and enhancement

Displayed adventurer base stats already include their personal starter weapon/clothes. Those bound starter pieces occupy no backpack cells and cannot be sold; crafted equipment contributes the listed **additional** stats. One active weapon upgrade, one active armour upgrade and one active accessory per adventurer; duplicate category items may be carried but grant no stats. Equipment does not require a new appearance per item in this release. A recipe card can be inspected before the officer joins; it shows materials, source, time, cost and exact stat effect.

One workbench and one craftsman perform one queued crafting or enhancement job at a time. A new recipe job reserves materials/fee at start, delivers at completion, and returns both on cancellation/cutoff. No free daily production. “Focus” is the selected recipe category/filter. The following ten recipes give every early material a visible use:

| Output (one unless stated) | Standard-or-better inputs + fee | Base time | Footprint / benefit |
|---|---|---:|---|
| Hunting Lure | 1 Boar Meat + 5G | 30 min | 1×1; consumed at departure, +10 target group points for one hunt |
| Scout Map | 1 Slime Gel + 8G | 30 min | 1×1; consumed at departure, +10 find points for one scout |
| Route Map | 2 Wolf Pelts + 30G | 1 hour | 1×2; reusable accessory, party search ×0.95, strongest only |
| Boarhide Vest | 4 Boar Hides + 40G | 2 hours | 2×2 armour; +30 max HP, +8 DEF |
| Balanced Blade/Hammer (same recipe, matching owner's kit) | 4 Slime Gel + 2 Boar Tusks + 50G | 2 hours | 1×3 weapon upgrade; +5 ATK to a melee adventurer |
| Hunter Bow | 3 Boar Hides + 1 Wolf Fang + 40G | 2 hours | 1×3 weapon upgrade; +4 ATK for Mira |
| Arrow Case | 2 Boar Hides + 15G | 1 hour | 1×2 accessory; bow adjacency gives retained +15% attack rate |
| Reed Ward | 4 Serpent Scales + 1 Marsh Core + 80G | 3 hours | 2×2 armour; +45 HP, +12 DEF |
| Ridge Edge (melee/bow/focus variants) | 4 Drake Scales + 1 Crawler Core + 120G | 3 hours | 1×3 weapon upgrade; +10 ATK; “focus” for caster |
| Refinement | 3 Slime Gel + 10G | 1 hour | Storage material; consumed in enhancement |

Potions remain bought for 20G each; do not make an immediately cheaper infinite-profit potion recipe. Scouting unlock sells Scout Maps for 20G, and Elsie sells lures for 25G before Commerce; these are access fallbacks, not a new shop department. Bound starter bow counts as a bow only after placing its zero-bonus 1×3 kit token in the backpack; Hunter Bow replaces that token. This makes the existing adjacency rule usable without double-counting starter ATK.

Enhancement applies to the adventurer's training profile at Fulker's, matching “5% of base stats per level” in GDD L668; it is not an unspecified item-upgrade system. Levels 1-5: each adds 5% of base ATK/DEF/max HP, additive to track percentages, no rate increase. Level n requires `2n` Standard common units from one species, `n` Refinements and `25n G`; levels 4/5 also require one elite part, of any ordinary species. Duration `30n` minutes. Adventure and enhancement are mutually exclusive. This gives elite parts a firm use while allowing sale instead. Show the permanent result before payment.

**Backpack rules:** retain 4×4 at company F/E, 5×4 at D/C (GDD L338); B/A grids are outside Eurydica, not current ranks. Each potion/lure/map is a physical item, no stacks inside a backpack, rotations in 90° steps allowed, invalid placements never auto-delete. Adjacency means at least one shared orthogonal edge between bow and case, no diagonals, +15% once. Potions: resolve enemy damage, down if HP reaches zero, otherwise consume the first potion in row-major cell order when HP ≤40%; restore 30% max, cap at max, at most one per enemy action. No resurrection or between-hit trigger within a cosmetic combo. Unequipped gear lives in shared storage; roster departure returns crafted gear as well as consumables. HP on gear removal clamps to new max; equipping max-HP gear does not heal current HP. Equipment changes allowed only while Available at HQ; prep changes remain draft until dispatch. Materials and corpses are not packed, and do not reduce combat capacity.

#### Market and information

Commerce starts with three listing slots, then five at 200 Reputation and eight at 700; each listing remains 1-99 units (retained GDD L667). Shared stock is reserved per listing; changing price/cancelling is free and cannot create more buyers. At 07:00 generate a persistent next-three-day demand schedule per material category: Low/Normal/High, probability 25/50/25%, factor 0.75/1/1.25. At each whole hour 08:00-23:00 each category has one shared potential buyer: buy probability 25/50/75% by demand state, at most 1/2/3 units respectively, with willingness-to-pay `base value × quality × demand factor`. Buy cheapest eligible listing first, then oldest; split listing stacks to fulfil this shared quota. Too-high price yields no sale. The same category's demand is shared across all listings, so splitting stacks does not multiply demand.

Fee per executed sale `max(1, ceil(gross × 0.05))`; reject a zero/negative-price listing. Sales Reputation is awarded from **cumulative net market and walk-up receipts**, one per 100G with remainder saved, never rounding away every small sale; request cash rewards are excluded. Base-priced Standard Boar Hide, three units sold: gross 36G, fee 2G, net 34G. Walk-up merchant pays `floor(0.5 × base × quality)` per unit with no listing fee and no volume cap; does not buy Unsellable. Raw corpses may be sold at 50% of their stated/reference raw value, no extra Reputation loophole beyond actual net receipts; ordinary raw value is three common-unit values, with no expected rare premium. Crafted equipment walk-up resale is 25% of consumed material base value, fees excluded; no buy-sell or craft-sell profit loop.

Information staff rank 1/2/3 sees 1/2/3 days ahead; predicted Low/Normal/High is correct with probability 70/80/90%, otherwise selects one of the two incorrect states uniformly. Sample the prediction once per category/day and persist it; opening the screen repeatedly cannot reroll. Always show confidence and subsequent actual result. Rumours show one uncompleted opportunity from discovered-region data each morning: material use, customer or eligible landmark; no new random quest generator, no automatic exploration. Before Liliana arrives, known material sources remain visible on recipe cards. Her advantage is timing and additional leads, never withholding basic recipe information.

### 3.5 Staff, recruitment, Morale, Reputation and recovery

**Gap:** GDD L171, L328-332, L665-669 and L685-699 omit hire/wage tables, staff ranks, Morale effects, payroll allocation and default consequences. The Roster already supplies several costs and should be imported by reference rather than reinvented.

| Named employee | Hire / weekly wage | Source and availability recommendation |
|---|---:|---|
| Rowan | 250G / 90G | Read: Roster L51; first M02 pair |
| Mira | 250G / 90G | Read: Roster L66; first M02 pair |
| Aveline | 300G / 105G | Read: Roster L81; visible from M02, hire when a bed exists |
| Durgan | 325G / 110G | Read: Roster L97; visible from M02, hire when a bed exists |
| Oren | 150G / 60G | Read: Roster L115; available M02, optional until processing opens |
| Nessa | 150G / 60G | Read: Roster L128; available when Liliana joins |
| Bastian | 200G / 75G | Read: Roster L141; available M05 |
| Valencia | 400G / 120G | Proposed, not in Roster's numeric table; Chapter 2 + E |

No random weekly replacements, no duplicates and no disappearance of unaffordable authored recruits. Weekly refresh checks story eligibility and highlights newly eligible people; Former staff remains separately visible indefinitely (retains GDD L328-331). Officer story recruitment costs 0G and officers have no separate payroll in this initial specification; named workers/adventurers are paid. Routine staff are not the officers who introduce departments. Their employment requires an unlocked department and an available workstation, not an adventurer bed.

Staff start at rank 1, which is separate from Company Rank F/E/D/C. Promotion to staff rank 2 requires 40 productive operating hours plus 200G; rank 3 requires 100 total hours plus 400G. Processing/crafting duration multipliers 1/0.85/0.70, wage multipliers 1/1.25/1.50 rounded up to whole gold. Processing quality probabilities and information confidence are in §3.4. Clerk gains one productive hour per morning forecast delivered. Personality traits remain descriptive unless an explicit mechanical passive is authored; no hidden stat bonuses for “Methodical” or “Patient.”

To prevent a locked department from blocking the tutorial or recovery, Mae/Fulker/Liliana each cover one **vacant** baseline station at twice base processing/crafting duration or 60% one-day forecast confidence. An officer cannot also run an extra job while the worker occupies that station. Additional workbench capacity can therefore have a use without inventing a fourth staff member: Bastian runs the first bench, Fulker covers the second at half speed. This is a proposed fallback, not a claim officers currently process in code.

**Payroll and rest:** Day 7, 14, 21 etc. after the 23:00 Resolution. Accrue pro-rata wages for employed calendar days, rounded once per employee at payday; hiring before that day's cutoff counts that day. Show the coming bill before hiring. If gold is insufficient, pause and let the player allocate full employee payments; unpaid employees leave after returning equipment, owing only accrued unpaid wages. No additional wages accrue while Left; rehire is arrears + original hire cost, retained from GDD L329. Dismissal settles accrued wages and returns gear; it must not erase payroll liability. Officers never enter Left.

Stamina starts at four; debit one before applying Red Fatigue, so the third dispatch from full starts at one and suffers the penalty. Display before/after prominently. Retain 24-hour rest, assignable at **every daily** closeout, not only payroll. At Day 2 23:00, rest ends Day 3 23:00, ready Day 4 07:00. The overnight 23:00→07:00 jump advances recovery, injuries, request deadlines and debt clocks eight hours, but not buyers or production. Healthy idle HP recovery applies through that night; injured HP remains at return value until injury ends, then idle recovery resumes. Injury recovery also restores stamina to four. No extra 24-hour rest after a 48-hour injury. Available/Resting/Injured/Left are mutually exclusive states; Red Fatigue is a condition overlay.

**Morale:** retain start 60; range 0-100. Processing duration multiplier 1.15 at 0-29, 1.05 at 30-49, 1.00 at 50-79, 0.90 at 80-100. No direct combat or wage modifier. At daily closeout: +1 if at least one operation succeeded and none injured, −2 per newly injured adventurer capped at −6/day, −5 per unpaid employee capped at −15/payday, +3 for fully paid weekly payroll. An idle recovery day grants +1 if Morale is below 60. Clamp once after totals and display each cause. This makes Morale visible without worsening injury, combat damage, pay and processing simultaneously.

**Reputation:** retain hunt/scout/request/sales sources and promotion thresholds; start at 0 explicitly. It is standing, never spent on promotion and never below 0. Promotion charges only 300/700/1,500G and never demotes an already unlocked region after a −10 contract failure. Beyond rank it provides listing slots (3/5/8 at 0/200/700), access to optional higher-trust contracts and the flashpoint offers; customer benefits also use the customer's own completion flag, not a second general relationship currency. No universal price multiplier: it would stack economy acceleration and make local relationships redundant.

**Debt and insolvency:** retain 2,500G principal/no interest/seven-day due date. Loan offered if no hired adventurer can ever return without rehire, and no affordable candidate can be hired with available accommodation; merely Resting/Injured does not trigger it. One outstanding loan. At the due date, unpaid balance becomes overdue, blocks rank promotion and optional HQ purchases, and sweeps 25% of positive receipts after sale fees toward principal; it adds no interest or permanent loss. Payroll retains priority for existing cash. Cancel outstanding purchase reservations before declaring insolvency. If everyone is Left while that loan is already outstanding, Tristitia offers one explicitly disclosed rescue advance equal to the cheapest available adventurer's rehire shortfall, added to principal, no cash windfall; existing beds are released by departed adventurers. Repeat only after a subsequent unpaid payroll and only for the actual shortfall. Mae's vacant-station fallback and the walk-up buyer leave a route back to income. No hard game-over in the default mode.

**Derived starting-cash sanity check:** Rowan + Mira + Oren cost 650G, leaving 1,850 of the GDD's 2,500G. All four adventurers + three rank-1 workers cost 1,625G, wages total 590G/week. Buying a 600G dorm too leaves 275G before earnings, less than a full week's 590G bill. Therefore staff/HQ must be staged and payroll reserve displayed; “hire everyone immediately” cannot be the tutorial. This check is arithmetic, not a simulated solvency claim.

### 3.6 HQ expansion costs, effects and a second operating group

**Gap:** GDD L152-154 promises expansion without numbers, staffing limits or a benefit beyond doors. S3 L272-280 gives the two-bed constraint.

| Upgrade | Visibility / prerequisite | Proposed cost / duration | Concrete effect |
|---|---|---|---|
| Dorm Annex | Preview from founding; first returned hunt permits construction | 600G + 6 Standard Boar Hides; 24 calendar hours | Beds 2→4; can hire Aveline and Durgan and split people across simultaneous operations |
| Larger Dorm | Preview at first promotion; requires Annex + E | 1,000G + 8 Standard Wolf Pelts; 48 hours | Beds 4→6; Valencia can join, with one future authored place left empty |
| Second Processing Table | Preview when Processing opens; first 10 corpses processed | 350G + 2 Standard Boar Hides; 24 hours | Two jobs at once, Oren plus Mae covering the spare table at twice base time |
| Second Workbench | Preview at Fulker's introduction; requires E | 600G + 4 Standard Crawler Plates; 24 hours | Two craft/enhance jobs at once, Bastian plus Fulker's slower spare-station work |
| Trading Shelves | Preview with Valerie | 300G + 4 Standard Boar Hides; 24 hours | Two additional listing slots, additive to Reputation's cap |

The first Processing area, Workshop, Information corner and Commerce counter open at their officer/service introduction **without separate construction tolls**. Paid expansions add capacity rather than blocking the newly taught feature. Construction starts while paused with an explicit quote; one site job at a time, persists overnight, consumes inputs at start, cancellable for full refund before completion, cannot be duplicated. Visual room changes happen at a safe transition, mechanical effect at completion. No recurring building upkeep for this first release.

Keep simultaneous operations possible from the beginning; people and beds are the limit, not a new arbitrary expedition-slot currency. The Annex makes a **three-person hunt plus one scout**, or **two two-person slime hunts**, possible with four employees. It does **not** prove that two two-person boar teams are safe. With only five authored adventurers including Valencia, two independent three-person hunting teams are impossible; the UI must not promise them. A sixth adventurer needs a separate authored character and kit if that later goal becomes required.

### 3.7 Requests, contracts, chapter gates and persistent customers

**Gap:** GDD L649-659 and L703-715 omit the actual board state machine and service introductions; RR L11-25 defines some timing, while RND rewards and RRE content are unfinished.

Use states Hidden → Offered → Accepted → Completed, Expired or Failed. Showing an offer is not acceptance. Offer-branch dialogue reveals the ID once; refusal does not reveal it; returning later permits the offer while chapter availability remains valid. Timer starts on **appearance**, retained from RR L11; the board shows absolute deadline and remaining hours before acceptance. Durations mean calendar time including nights. Timed offer expiry with no acceptance has no penalty; failure/expiry after acceptance costs 10 Reputation once (proposed extension of the contract rule to deliveries), no Morale penalty. No-deadline requests remain until complete once accepted. City CH1-REQ-003–007 unaccepted offers disappear at Chapter 1 end, retained from RR L13. CH1-REQ-001/002 use their time deadline without an extra chapter removal rule.

Completion takes the full quantity atomically at Tristitia or the named client; partial reservations allowed, partial cashouts not allowed. Standard/Pristine preferred, lowest acceptable quality consumed first; display the exact units. Bound or equipped items cannot be consumed. Inventory counts distinguish owned, listed, reserved and available. Delivering once sets the NPC's existing aftermath dialogue flag and any separate relationship benefit. Accepted requests persist across chapter changes and relocation.

| Request | Read requirements/reward | Recommended completion of unresolved details / consequence |
|---|---|---|
| CH1-REQ-001 Bathroom | 5 Slime Gel any condition; 50G/50 Rep; 5 days, R1 L7-16 | Client ID `eur_inn_owner`, the existing tavern/inn, deliver there or at HQ. Introduced at M02. |
| CH1-REQ-002 Garden | 2 Slime Cores any condition; 100G/50 Rep; 4 days, R1 L22-33 | Client ID `eur_garden_steward`, noble household's steward at water/garden district; no invented personal name. Introduced at M02. |
| CH1-REQ-003 Merchant | 2 Slime Cores any condition; 25G/100 Rep; 2 days, R1 L39-48 | Keep low-cash/high-standing choice, add an on-accept one-time “three gel lots” exchange: turn in 15 Slime Gel to the merchant for exactly 2 requested cores, locked to this order, no resale. State this alternative before accepting. |
| CH1-REQ-004 Clinic | 10 Slime Gel any condition; 100G/20 Rep; 6 days, R1 L54-63 | Completion gives a permanent four-potions-per-week allotment at 18G each; normal potion price remains 20G beyond that. |
| CH1-REQ-005 Hollis | 3 Wolf Pelts, no deadline, reward TBD; RND L9-20 | Standard+, 75G/25 Rep. Permanent free delivery from the board to Eurydica clients through the stable's local courier contact; no travel timer for turn-ins. |
| CH1-REQ-006 Marta | 4 Boar Meat, no deadline, reward TBD; RND L26-37 | Standard+, 60G/20 Rep. Enables the distinct recurring supply order below and existing roast dialogue. |
| CH1-REQ-007 Beren | 2 Boar Hides, no deadline, reward TBD; RND L43-54 | Standard+, 40G/20 Rep. Enables his recurring supply order and previews Boarhide Vest recipe via Repair & Supply. |

Before Hollis's benefit, Tristitia can reserve and receive the goods, but the delivery stays Accepted until the Commander visits the client for payment; after it, HQ/board delivery and payment are immediate. This does not consume company simulation hours while the board is open. The Garden/merchant rare parts are **processing rare outputs**, not elite variant parts, not a rare-monster corpse. Add the same 15-gel-to-two-core quest exchange for the Garden request if its first two cores have not dropped by the start of its last day; this is an explicit proposed RNG safeguard, not a current rule. Exchanges are one-time quest transactions, supply the named request directly and grant no sales Reputation.

**The two recurring orders are new designs, not reinterpretations of the one-time requests.**

| ID / client / appearance | Required goods / reward | Repeat, time and delivery rules |
|---|---|---|
| EUR-WO-001, Marta, Service Lanes; after CH1-REQ-006 completion | 4 Standard+ Boar Meat / 60G + 5 Rep. Description: replenish the roast supply. Tristitia: “Marta knows what she can use each week.” | One offer every 7 calendar days after completion; no countdown, one instance maximum; deliver to Marta or via Hollis's unlocked courier. Source: Dire Boar hunts/processing, Mosswood. |
| EUR-WO-002, Beren, Market Spine; after CH1-REQ-007 completion | 2 Standard+ Boar Hides / 40G + 5 Rep. Description: keep repair leather stocked. Tristitia: “Beren has another small batch of repairs waiting.” | Same recurrence/no-deadline/one-instance rules. Deliver to Beren or courier. Source: same boar hunts. |

Use completion flags, no new relationship XP ladder. Show the next replenishment date and next order's quantities. After Chapter 6 relocation, new Eurydica recurring offers stop; accepted orders remain deliverable by courier, and the next-offer timer resumes only if Eurydica base operations resume. This resolves RR L25/RRE L20 without inventing remote infinite income. Trusted contacts still exist in the journal.

**Optional subjugation replacement index:** GDD's “eight authored” content is not substantiated here. To close the mechanical gap, these eight **proposed** contracts reuse existing targets; their narrative presentation still must be written before being labelled authored. All have one fixed encounter, 30-minute approach, 72-hour offer life from appearance, no charge to accept, −10 Rep on accepted failure, no penalty to ignore, repeat offer after 7 days if unsuccessful, and no repeat cash/XP farming after success. Completion pays reward plus normal secured corpses and XP; no boss loot duplication.

| Proposed ID / client / problem | Required rank and knowledge | Target | Gold / Rep | Persistent completion flag / ending premise |
|---|---|---|---:|---|
| EUR-SUB-01 / inn owner / slime nuisance | F, first hunt returned | 2 Moss Slimes | 90 / 15 | Inn's supply access is clear; client acknowledges the work |
| EUR-SUB-02 / Beren / boars damage deliveries | F, boar known | 2 Dire Boars | 140 / 20 | Beren receives the delayed repair supplies |
| EUR-SUB-03 / Hollis / wolves threaten stable road | F, wolf known | 2 Forest Wolves | 200 / 25 | Stable road warning is removed |
| EUR-SUB-04 / South Gate guard / Blackfang attacks road | E, wolf known, Chapter 2 | Blackfang | 450 / 100 | Blackfang case closed; **not** the chimera flashpoint |
| EUR-SUB-05 / Dr. Ginger / marsh supplies inaccessible | E, Marsh Slime known | 2 Marsh Slimes | 260 / 30 | Clinic's marsh-supply report is resolved |
| EUR-SUB-06 / travelling merchant / serpents block pickup | E, Serpent known | 2 Marsh Serpents | 320 / 35 | Merchant's pickup report is resolved |
| EUR-SUB-07 / Beren / stone plates needed safely | D, Crawler known | 2 Stone Crawlers | 420 / 40 | Beren receives a completed quarry-route report |
| EUR-SUB-08 / travelling merchant / wolves bar high road | D, Highland Wolf known | 2 Highland Wolves | 500 / 45 | Highland shipment route is cleared |

These ending premises are proposed flags/dialogue subjects, not automatic new economic bonuses or canon motives. They use existing residents; no filler officers. The exact textual mission scenes are production work after accepting the design.

**Story milestone predicates:** retain named M02/M03/M05/M06/M08 identifiers but remove any requirement that their numeric order is a mandatory feature chain. At M02, the 14:00 return presents Rowan/Mira and the two intro requests. M03 follows one completed hire and Elsie's dispatch explanation; Processing opens alongside it under Mae. On the first hunt return, Elsie can introduce basic scouting (M06) independently of Crafting. Discovering or receiving a boar material previews Fulker's equipment; talking to him can open M05 in Chapter 1. First request completion **or** first sale introduces Valerie's joining scene; first scouting return introduces Liliana's joining scene. These are proposed event triggers, not approved scene dialogue. Allow Commerce/Crafting/Information introductions in whichever eligible order the player pursues. None requires completing another officer's bespoke tutorial quest. M08 opens optional contracts after the first ordinary hunt win and Tristitia's explanation. Chapter 1 ends when all three officers have joined and the player chooses to conclude the chapter; no fixed day or mandatory side-order completion.

**Reconciled flashpoint table:** retain existing gold/Rep reward scale but change boss identity and explicit story gates.

| Flashpoint | Gate | Proposed starting encounter | Reward and persistent aftermath |
|---|---|---|---|
| Mosswood Chimera, Chapter 2 | Chapter 1 complete, E, 300 Rep | Solo Elite boss: HP 2,400, ATK 17, DEF 25, rate 1.0; base XP 80 before ×5; corpse processing 120 min | 900G/250 Rep; Mosswood scout injury chance becomes 0.5% baseline and all known Mosswood target encounter probability becomes 85% before den weighting |
| Ambermaw Blockade, Chapter 3 | Chimera cleared, E, 800 Rep | Retain GDD L632 stats | 1,400G/350 Rep; Amber Marsh target encounter probability 85% before den weighting |
| Crownstone Reckoning, Chapter 4 | Ambermaw cleared, D, 1,400 Rep | Retain GDD L641 stats | 2,000G/450 Rep; Redstone target encounter probability 85% before den weighting |

Show these named threats before eligibility with explicit gate labels. Main-story offers **do not expire**; remove the 72-hour/10-day lockout for flashpoints, keep it only where explicitly defined for optional work. Retry after injured people recover, with no additional countdown. No 10-Rep penalty for a story-boss loss. Clear rewards and aftermath apply once. Officers join a fight only when its authored story scene says so; routine parties can be tested against these values without relying on an invisible officer rescue. No new poison, three-head targeting or boss-phase system is required for the first chimera design.

### 3.8 Frontier and scope of “final”

**Gap:** GDD's region list ends at three Eurydica areas (L345-351) and its victory condition ends at Rank C (L698); it contains no frontier operating model. Owner L118 is explicit about Chapter 6 relocation. Bible L87 and L105-123 separates later verification authority from early company life.

Recommended scope decision: finalise this as the **Eurydica systems specification plus a persistent campaign transition contract**. Do not label the whole six-plus-chapter campaign content-complete. The following is the minimum frontier model proposal that the core systems must support:

- Chapter 4/Rank C/no debt grants the Eurydica completion milestone. Continue play; no forced credits or save termination. Chapter 5 is a readiness/transition chapter using existing jobs and company development, not an invented fourth flashpoint. Unlock the Chapter 6 move when its story introduction completes and the Commander elects to move; no forced calendar deadline or undisclosed resource cost.
- Move cost 1,500G, 48 calendar hours; confirmation shows accrued wages and all accepted request deadlines. Finish/recall active expeditions, settle or cancel unfinished production and return reserved inputs, cancel listings and retain stock. No employee is deleted. Pause the player's timed accepted deliveries during the transfer to prevent surprise failure; resume with the same remaining hours at arrival. Normal payroll and debt clocks advance and their settlement preview is mandatory. Injury/rest recovery advances normally.
- Transfer Gold, Reputation, Morale, rank, employees, skills, gear, inventory, debt and request/contact flags unchanged. Start Frontier HQ with the number of beds and workstations purchased in Eurydica; do not sell the same capacity again. Introduce one initial frontier area at 0% exploration, with the existing three ordinary monsters/three landmarks/two paths schema and one rare lead to start. Those species and story identities require separate authored content; do not turn placeholder names into world canon.
- Use the same ≤3-hour local expeditions initially, no new survival meter. A discovered route plus one successful hunt there sets an internal “surveyed route” flag and grants −5-minute search time as an existing path effect, within the current floor; one route flag per path. The player chooses resource-rich versus safer paths using the same map and prep systems. Do not call it “Guild Verified” until Chapter 7's authority transition. Frontier scouting base injury rate starts at 2% per half-hour, no death.
- Reuse material/equipment/customer rules with a new base/location ID and separate demand pool. No global automatic sales between bases. The map can remember Eurydica; do not simulate a second autonomous HQ or a caravan logistics game without an explicit later design. Chapter 1 only lightly previews unknown frontier reports and Elsie's concern; no early verification institution.

This is sufficient to preserve saves and avoid hard-coding “Rank C means game over.” It is deliberately not a fabricated frontier monster catalogue or chapter manuscript. To call a full-campaign GDD final, the frontier's named areas, enemies, officer scenes and later goals must be authored; that is a **content-scope gap**, not an unanswered recommendation in this audit.

### 3.9 Save, difficulty, screens and implementation boundaries

**Gap:** save/load, difficulty and most carried-over screen behaviour are absent from GDD L719-741. A Godot target and proof links are not a persistence or user-interaction specification.

Recommended saves: three campaign profiles, unlimited named manual saves within a profile, three rotating autosaves; autosave at new day, before payroll, before flashpoint dispatch and before/after chapter transition. Save schema version plus content revision; atomic replacement and last-good backup. Persist seed/stream state per operation, action queue and in-flight action end tick, meter/status counters, corpse roll identity, exploration/finds/reserved rare, request appearance/deadline/branch flags, listings, material reservations, construction, employee arrears and lifetime/spendable XP. Manual save allowed in all management/world states and fights; during authored cutscenes save at the current safe scene checkpoint. Reload must not reroll outcomes or re-award rewards. No real-world offline progression; resume paused. Migration must preserve identities and return invalid reservations safely rather than delete items.

Difficulty: **Standard** uses proposed baseline. **Relaxed** keeps combat/statistics/drop rates but halves injury duration, multiplies staff/adventurer wages by 0.75 (round final bill per employee), and doubles request deadlines. Change only at next new-day boundary; effects apply to newly created injuries/deadlines and subsequent wage accrual, never repeatedly extend existing timers. No permadeath mode. Difficulty, font/UI scale, reduced VFX and clock-speed choices are separate settings. Keep numeric danger explanations visible in both modes.

Pause policy: world walking uses the company clock; dialogue/shop/management screens open paused and restore the prior chosen speed only on close. Opening Watch does not pause unless the player already paused. A single foreground modal prevents stacking dialogs to change time. At 23:00 queue closeout until the current dialogue safely ends; no new simulation events beyond the cutoff. HQ shortcuts open the same officer screen and show their portrait, preserving room identity while avoiding repeated walking for routine tasks.

| Screen gap at GDD L734 | Minimum build contract |
|---|---|
| HQ / Building Map | Current rooms, capacity, build quote, completion time and current job; Preview/Build/Cancel |
| Commander's Office / Request Board | Offer vs accepted vs completed, source/client, deadline, reserved stock, full reward and benefit; Accept/Reserve/Deliver/Decline |
| Processing | Corpse ID/species/possible outputs, worker, quality chances, finish time, cutoff warning; Queue/Reorder/Cancel |
| Information | Dated forecasts with calibrated confidence, actual previous results, material-use leads and unverified rumour labels |
| Commerce | Available vs reserved stock, price, demand signal, fee/net preview, shared listing slots; List/Reprice/Withdraw |
| Workshop | All recipe previews, active category, exact inputs/time/effect, target person for enhancement; Reserve/Craft/Cancel |
| Recruitment / Payroll | Pool, former staff, hire + next bill, bed/station requirement; Hire/Rehire/Pay by employee |
| Rank / Flashpoint | Exact unmet conditions, gold charge or party preview, unique reward, consequence and retry rule |
| Summary | Today's cash flows, accrued wage reserve, injuries/rest readiness, completed projects, and up to three player-pinned future goals |

The GDD's three.js proofs remain references; no new engine or rendering architecture is recommended by this audit. Do not equate a UI screenshot or existing prototype label with a verified economy/save implementation.

## 4. The hook test: days 3, 10 and 25

### 4.1 What the current GDD can actually support

These are **inferred, conditional playthroughs, not playtest results**. The manuscript implementation handoff stops before the Day 1 14:00 event (Chapter L7, L183); the GDD has no event predicates for M02-M08 and no housing expansion rule. Thus it cannot guarantee any exact day-3/10/25 state. To test its intended loop, assume the first two hires/hunts have opened, treat rest as daily and nights as advancing recovery, and permit later story introductions when relevant. Those timing interpretations are disclosed gaps, not hidden imports of §3's proposals. Exact cash, quality and wages cannot be simulated from GDD alone; Roster costs are supporting evidence, not yet integrated GDD rules.

| Day and plausible current state | Today's play and an honest “tomorrow” sentence | Soon / building / beyond reach | Where the hook succeeds or fails |
|---|---|---|---|
| **Day 3: two hires, slimes and introductory orders.** Rowan/Mira hunted on Days 1 and 2, then were assigned rest at Day 2 closeout, so they are unavailable until Day 3 23:00 under the 24-hour rule. | Process stored slime corpses, examine requests, visit the merchant. **“Tomorrow I want to hunt more slimes, because that will let us finish the bathroom order and earn our first standing.”** If that order is already done, try Garden/merchant rare cores. | Soon: processing results today and rested staff tomorrow. Building: an accepted request or 200-Rep promotion. Beyond reach: Hollis's pelts and Beren's hides can already be requested, but the proof only exposes the latter shops (GDD L26, L34). | The initial request is a concrete hook. It becomes weak when it is a repeated 20% rare-part roll, or when the next material depends on an unspecified scouting story trigger. No equipment prize or paid capacity upgrade is defined. An entire rest day can be only administration before the officers arrive. Sources: GDD L315-323, L665, L709-713; R1 L9-28; RND L3. |
| **Day 10: basic scouting introduced; two-hire conservative branch.** Three completed 3-hour scouts have reached 36%, enough for boars; one or two additional scouts would reach wolves. Exact calendar requires alternating rest and hunts. | Scout with Mira for the den/path while Rowan recovers; resume paired hunting later. **“Tomorrow I want to hunt the boars we found, because that will supply both Marta and Beren.”** Alternative: finish two more scouts and pursue Hollis's wolf pelts. | Soon: scout discovery or processed boar. Building: two residents' orders or the first skill milestone. Beyond reach: wolves at 50%, Rank E/Valencia and Marsh. | This is the strongest existing seed: place→two needs. But RND L13, L30, L47 has no rewards; boar meat/hide output is not mapped in GDD L665; repeat business does not exist (RRE L3). A den's +15 points currently means more danger, not proven dependable supply. The player cannot price the choice to sell vs craft, or recruit a third person, because those rules are absent. |
| **Day 25: Mosswood may be charted and Rank E may be reached.** Nine full scouts can reach 100%; request completion and hunts can plausibly cross 200 Rep, but exact promotion day is not derivable. Continue with two employees unless a missing housing rule is supplied. | Consider Marsh scouting, a rare hunt, or saving toward Blackfang's 300-Rep offer. **“Tomorrow I want to scout the Marsh, because that will reveal more valuable monsters.”** If near 300: **“Tomorrow I want to prepare for Blackfang, because its reward helps reach the next company rank.”** | Soon: a return, sale or rare target. Building: a known milestone modifier or promotion cash. Beyond reach: Redstone at D and the later bosses. | Existing milestones can sustain a favoured adventurer build, and bosses give clear large rewards. But new areas mainly advertise stronger enemies and higher prices; their find tables, XP, equipment requirements and material uses are missing. Charting Mosswood returns every scout, with no stated way to acquire another rare sighting. “Prepare” has no complete gear prescription. The company's physical future is still undefined, and the chimera story has disappeared from the reward chain. Sources: GDD L265-311, L367, L423-425, L625-669, L693-698. |

A more generous Day 10/25 branch can assume a legacy housing expansion allows all four starters. It then offers a three-person hunt plus scout and more staggered rest. **That is a missing-rule assumption**, not something the current GDD establishes. The measured three-person boar party (GDD L615) should not silently replace the manuscript's two starting recruits in a “typical early game” example.

### 4.2 Pacing calculations that change these scenarios

- **Rest and safe work:** four bars with immediate debit and Red Fatigue at ≤1 means only two deployments from full before fatigue penalties. A third and fourth are possible (the fourth departs from 1 to 0), but unsafe; no departure from 0. A daily-closeout 24-hour rest consumes the whole following operating day. If “closeout” meant weekly only, the first week would be much worse. This interpretation should be explicit (GDD L316-319, L687).
- **Scouting milestones:** 2 points per half-hour means boars at the 13th interval = 26% = 6.5 cumulative scout hours; wolves at 25 intervals = 50% = 12.5 hours; charted at 50 intervals = 25 scout hours. Full-trip counts are 3, 5 and 9 respectively. The first two full trips reach only 24%, so “two or three scouts” in GDD L369 needs a partial-third-trip qualification. Multiple scouts reduce calendar delay, not total scout work.
- **Rare request lottery:** with independent 20% rare rolls (GDD L665), collecting two rare parts needs 10 processed corpses **on average**, not a guarantee. After five corpses, probability of at least two is 26.27%; after ten it is 62.42%. The Garden plus merchant need four cores, expected 20 slime corpses. This ignores quality restrictions because their requests explicitly accept any condition. A two-day clock beginning during the pre-recruitment city walk (R1 L41-45) can punish a player for merely offering help early. This motivates a quest-limited alternative, not inflating rare drop rates for the entire economy.
- **XP pace:** a proposed 100-XP hunt needs 14 hunts for the 1,400-XP first milestone, not exactly twelve. Two non-fatigued hunts then a full rest day average roughly one hunt/calendar day for that team, making a second-week milestone plausible only with regular successful hunting. At the same rate, the 12,000 cap would take 120 hunts, not a Day 25 automatic max. A first milestone is not all four tracks mastered (GDD L267).
- **Scout risk:** six 1% checks give 5.85% injury, matching “about 6%” in GDD L442; Red Fatigue's six 2% checks give 11.42%, not exactly 12%. Proposed Marsh 1.5% gives 8.67% per trip before modifiers.
- **Prizes versus gold:** an ordinary boar's three common parts have 36G gross reference value if “Common value” means a unit, or only 12G if it means the entire corpse. That factor-of-three ambiguity prevents a defensible expansion-payback estimate. With the proposed unit reading and 50% fallback, two boar carcasses' six common parts yield 36G walk-up cash before rare outputs/quality; Marta+Beren proposed first deliveries pay 100G and 40 Rep for the same Standard goods. An incentive to choose customers is explicit rather than assumed.

### 4.3 Smallest set of changes that produces branching goals

The full audit above closes many implementation gaps. **Only four connected design changes are needed to test the hook hypothesis**; do not wait for the frontier, all optional contracts or a larger roster.

| Minimal change | Reused system | Chapter 1 visible prize and lasting consequence | Competing choice |
|---|---|---|---|
| **H1. Preview gear and material uses before manufacture.** Add locked recipe cards at Beren/Elsie and source links on inventory items. | Workshop, backpack, known-monster cards | Boarhide Vest's +30 HP/+8 DEF and Mira's bow/case bonus can be seen before Fulker joins; materials become a specific party improvement. | Spend hides on gear now, sell for wages, fulfil Beren, or reserve them for beds. |
| **H2. Show known hunting grounds as useful sources.** Use existing den/path discoveries; show target probability, group bonus, materials and active benefits before dispatch. | Scouting, Region Knowledge, hunt target selection | Boar Nest helps supply two customers; paths shorten searches; Mossy Spring sustains repeated fights. The chimera aftermath makes the area more reliable. | Explore toward wolves for Hollis, exploit known boars, or pursue an active rare for elite enhancement. |
| **H3. Make the two existing customer arcs leave repeat opportunities.** After their one-offs, enable separate weekly Marta/Beren orders with previewed quantities and next appearance. | Request board, completion flags, existing aftermath dialogue | A dependable destination for familiar output and a reason to maintain an established route. | Sell into a forecast peak instead, craft personal gear, or keep a payroll reserve. Neither customer is mandatory for an officer. |
| **H4. Put the Dorm Annex quote and the actual waiting recruits on the HQ map.** Tie beds to employment and leave simultaneous operations otherwise unrestricted. | HQ growth, recruitment, existing four starters | Four beds permit a three-person hunt plus a scout or two modest groups; the player can picture whom they will hire. | Make the current pair stronger first, increase processing throughput, or invest in people. |

Two enabling corrections are prerequisites, not additional management systems: basic scouting must be introduced independently of Workshop, and the game's material IDs/yields must be explicit. Opening Service Lanes during Chapter 1 is needed for Marta to participate; its closure in the current proof need not be changed within that proof's scoped release. Show requests/recipes before they are fulfilable, but keep requirements and availability honest.

Each activity should display a short causal path, for example:

| Visible place/resource | Player-selected use | New capability | Why another place becomes interesting |
|---|---|---|---|
| Dire Boar Nest → hides | Vest for Rowan | More HP/DEF for the existing party | Wolf hunts and their pelts/fangs become a more credible target |
| Dire Boar Nest → meat + hides | Marta/Beren supply | Regular orders and income | Funds a new employee to scout Marsh while others earn locally |
| Mosswood hides → Annex | Hire Aveline/Durgan | Hunt and scout concurrently | A rare sighting need not consume the company's entire work day |
| Wolves → fang/pelts | Bow, Route Map or Hollis delivery | Better ranged damage, faster searches or easier delivery | The player chooses preparation, throughput or convenience |

These links are opportunities, not a required quest chain. The “new capability” rows are proposed benefits, not claims of measured combat safety. Avoid requiring the vest to unlock wolves or requiring Marta before Beren. Money provides an alternative route to several needs, and customer flags preserve a human consequence without a new relationship grind.

With those changes, plausible **target experiences** become:

- **End of Day 3:** “Tomorrow I want Mira to scout for boars, because their hides can become Rowan's vest or room for Aveline.” Soon: returning people/processing; building: vest or Annex reserve; beyond reach: wolves and their visible uses. This requires basic scouting to have opened; it is a playtest target, not a fixed-day unlock.
- **End of Day 10:** “Tomorrow I want one boar run for Marta and Beren, because that will pay toward the Annex while Mira looks for wolves.” A different player: “I want the bow first, because Mira is in every hunt.” Both are legitimate; H3 must not make customer supply universally superior to every forecast sale.
- **End of Day 25:** “Tomorrow I want to try Valencia with Rowan in the Marsh, because local earnings now cover the other group's work and Marsh parts make Reed Ward.” Another player may still prefer the chimera, a rare target or a workshop upgrade. A 6-bed house is room to grow, not a claim that six authored recruits already exist.

The daily summary can show **three optional pinned projects chosen by the player**: one near completion, one being funded, one visible beyond reach. Pinning follows existing item/request/room cards; it awards no extra quest currency and never forces a recommended order. Success criterion for the next integrated proof: at each of these checkpoints, a player can name two materially different next projects, their source/cost and what changes after completion, without reading the campaign victory screen.

## 5. A few other mechanic improvements, ranked by value versus cost

These are additional to the four hook changes and required rule corrections. Cost is an **inferred relative implementation effort**, not a schedule estimate.

| Rank | Improvement | Value / cost | Concrete scope and why it is worth doing |
|---|---|---|---|
| 1 | Payroll reserve and spend preview | Very high / low | Every hire, promotion and HQ quote shows cash after purchase and next accrued payroll; allow a player-set reserved amount. No mandatory spend block except actual insufficient cash. Prevents the 275G-before-wages trap without making the economy forgiving by accident. |
| 2 | Reusable expedition preparation | High / low-medium | Save two named formation/loadout templates, substitute nobody automatically, show missing items/fatigue and confirm each dispatch. Reuses Elsie's prep screen; no auto-hunt loop. Reduces repetitive administration while preserving decisions. |
| 3 | Post-operation explanations | High / medium | Resolution lists material yield, effect of discovered paths/den, injury cause, consumed potion and XP gained; compare selected prep estimate with actual outcome. Explain why a project advanced without exposing debug logs. |

Do not add weapon durability, hunger, permanent death, a second skill tree, random infinite recruits or a large relationship-level system to repair missing hooks. The current systems have enough decisions once their rewards and dependencies are visible.

## 6. Finalisation order, evidence and acceptance ledger

### Recommended sequence after this audit

1. Adopt one canonical terminology and chapter/flashpoint/rank table; resolve the active contradictions in §2.
2. Put the numeric employee, material, recipe, HQ, board and market contracts into the GDD's tables or linked data with explicit authority. An old document being “carried over” is insufficient.
3. Implement one complete Chapter 1 economy slice using the four hook changes, with the two actual initial recruits, realistic rest and wages, and the seven existing requests. Preview unbuilt prizes honestly.
4. Validate it with short seeded scenarios, then balance later areas and the chimera. Do not extrapolate 24 Mosswood hunts to all formations and regions.
5. Keep the frontier transition contract in saves now; author Chapter 5/6 content separately before claiming a complete campaign design.

No owner approval, source edit, art generation or engine change was attempted. Recommendations are concrete enough to review without requiring this audit to stop for design decisions.

### Acceptance ledger

The ledger was established before the audit work, inside the authorised report instead of an extra GATES.md. These are manual design-review gates; shell checks below support factual claims but are not presented as an independently approved automated gate suite.

- [x] G1: Read the complete GDD and named supporting sources; separate read facts, arithmetic, inference and proposals.
  EVIDENCE: All 785 GDD lines read in bounded sections; all named supporting text files read; source register distinguishes the optional legacy pointer. Fourteen input-file SHA256 snapshots, including the task handoff, matched on recheck.
- [x] G2: Account for all ten section 17 questions and unresolved/deferred items elsewhere with a recommendation and reason.
  EVIDENCE: O01-O10 map one-to-one to section 17; O11-O40 cover the full-text open/not-yet/carried-over/deferred/later/pending/placeholder/proposal sweep. Duplicate and already-settled items are identified, not reopened.
- [x] G3: Cite and classify disagreements, distinguishing conflicts from gaps and historical/scope differences.
  EVIDENCE: C01-C24 reviewed against cited GDD and supporting lines. Rank-before-flashpoint access, the morning proof boundary, guild analogy and old change-log entries are explicitly distinguished from active contradictions.
- [x] G4: Cover the requested build gaps with concrete, mutually compatible starting rules.
  EVIDENCE: Reviewed equipment effects and inputs, nine elite IDs, staffing/wages, request state/timing, Morale, Reputation, HQ capacity, repeat business, frontier persistence, save/difficulty and simulation edge cases. All new quantities are labelled proposals; no new production or code work is claimed.
- [x] G5: Analyse days 3/10/25 under current rules and propose minimal branching hooks plus few ranked improvements.
  EVIDENCE: Days 3, 10 and 25 each state assumptions, a tomorrow goal and the failure point. Four minimal changes reuse existing systems; three additional improvements are ranked by value/cost. No hypothetical later roster or housing capacity is claimed as established.
- [x] G6: Verify calculations, report completeness, exactly twelve summary lines and the two-file write scope.
  EVIDENCE: PowerShell checks passed: unique O01-O40 and C01-C24, 101 explicit GDD citation starts within source bounds, consistent Markdown table widths, no replacement characters and exactly 12 nonempty summary lines. Arithmetic rechecked independently for XP, payroll, scout risk, rare-part probability and group size. Tool-write review shows only the two authorised report files.

Final gate result: **6 met, 0 unmet, 0 abandoned.** Design recommendations remain proposals; adopting them and proving balance are subsequent work, not unfinished audit deliverables.

