# Frontier Guild Chronicle: Implementation Specification

| **Version** | v0.1 · 28 September 2026 |
|---|---|
| **Status** | CURRENT. See `FGC_00_Document_Register.md` |
| **Scope** | How FGC is built in Godot: architecture, runtime contracts, data formats, saves, RNG, rendering, the script runtime and tests. **It never changes a game rule**: rules and numbers come from the GDD (`IMC GDD.md`). Where the GDD is silent on an implementation detail, this spec decides it, marked **[spec decision]**. |
| **Authors** | Claude (§00–05, §09–15, §17, merge); Codex (§06–08, §16, §18), reviewed by Claude |

---

# 00. Source authority and implementation policy

## 00.1 Source authority
- **Rules, numbers, systems:** GDD v2.1.x. Reference implementations: the proofs in `HD-2D Proof/src/` (`ops.html` operations/combat/clock, `battle.html` battle presentation, `town.html` town/camera/buildings/dialogue). A proof demonstrates intent; if it differs from the GDD, the GDD wins.
- **Script syntax:** `Scene Script Format.md`. **Scene content:** `Manuscript/`.
- **Everything else:** the register's authority order.

## 00.2 What this specification decides
Engine settings, project layout, autoloads, the simulation/presentation split, the command and event bus, content file formats, the save format, RNG ownership, the script converter and runtime, the HD-2D rendering stack, UI architecture, input mapping, the minigame framework, tests, and repository conventions.

## 00.3 Engine lock
- **Godot 4.7**, **Forward+** renderer (`d3d12` on Windows), **Jolt** physics, **typed GDScript** only (no C#, no GDExtension in M1–M3). [spec decision]
- Project: `D:/Godot Projects/frontier-guild-chronicle`, repo `Tristixa/frontier-guild-chronicle`, branch `main`.
- Target: Windows desktop, 1280×800 reference resolution, scaling with `canvas_items` / `expand` (already set in `project.godot`).

## 00.4 HD-2D asset lock (hard rules)
**Required:**
- **Characters are pixel sprites:** four-direction idle and walk atlases (64×108 cells, anchor 32,105), billboarded in the 3D world at **1 art pixel = 1.68/93 m**.
- **Monsters** are one still per pose (GDD 2.2).
- **Buildings** are box volumes wearing painted orthographic facade textures under generated curved roofs (GDD proof 4; `$imc-environment-art-direction` `hd2d-buildings.md`).
- **Field backdrops** are painted layers and cutouts (GDD 2.4).
- **Portraits** are 2D (768×1024 RGBA).

**Forbidden:**
- skeletal 3D character models, rigs or pose layering;
- eye-level character close-ups;
- 3D-modelled monsters;
- baking lights, glows or water into painted art (the engine owns them);
- nearest-neighbour filtering on painted art (only pixel sprites use nearest).

## 00.5 Notation
`code` = file, node, field or ID. **MUST / MUST NOT** = hard requirements. "Command" = presentation-to-simulation message; "event" = simulation-to-presentation message.

---

# 01. Runtime scope (M1–M3)

The first playable target is **Chapter 1 in Eurydica**: the opening (Scene 1), the tavern (Scene 2), Day 1 (Scene 3) with the 14:00 return, and Days 2–5 play (Scene 4 talks and requests) on top of the full daily loop: hunts, scouts, processing, market, requests, closeout, night and sleep.

Everything region-specific is **data** (content JSON with region tags; GDD 16a.1). Chapter 2 and the Frontier are added as content, not code.

**Out of scope for M1–M3:** the Frontier content, romance (Frontier-only), Chloris, gamepad polish, audio mixing beyond basic buses, and platform builds other than Windows.

---

# 02. Godot project organization

```
res://
  app/            autoloads and the app state machine
    game.gd            Game: the app state machine (§04)
    content.gd         Content: loads and validates content/ at boot (§06)
    sim_host.gd        SimHost: owns GuildState, real-time to tick bridge (§05)
    saves.gd           Saves: profiles, slots, autosave (§08)
    audio.gd           Audio: music and sfx by ID (§15)
    settings.gd        Settings: speed, accessibility, video (GDD 16b)
  sim/            pure simulation: RefCounted and Resource classes only; MUST NOT reference Node, SceneTree, Input or rendering (§03, §07)
  content/        JSON data (§06); content/scenes/ holds converter output (§09)
  presentation/
    world/             town, HQ, interiors: buildings, props, markers, cutaway
    camera/            CameraRig and shot solver (§10.2)
    post/              tilt-shift DoF, grade (§10.3)
    actors/            SpriteActor billboards (§10.4)
    field/             operations field view: search walk, battle stage (§11)
    dialogue/          ScenePlayer, dialogue view, talk menus, barks (§09)
    ui/                screens, HUD, theme (§12)
    minigames/         the five working sessions (§14)
  scenes/         .tscn (main.tscn, worlds/, field/, ui/)
  assets/         imported art and audio (synced from approved sources only, §10.8)
  tools/          headless tools: scene converter, content validator, asset sync, facade builder
  tests/          run_all.gd and test suites (§16)
```

**Autoloads, in order:** `Settings`, `Content`, `SimHost`, `Saves`, `Audio`, `Game`. `Game` is last, because it starts the state machine once the others are ready.

**Naming:**
- files `snake_case.gd`; classes `PascalCase` via `class_name`; signals past tense (`day_closed`);
- content IDs are lower `snake_case` (§06);
- scene markers use the names in `Locations/Eurydica/markers.md`.

---

# 03. Architecture: simulation and presentation

```
 Input ──> Presentation (scenes, UI, camera, ScenePlayer)
               │ commands                ▲ events + read-only state
               ▼                         │
          SimHost (autoload) ── advances ──> GuildState (sim/)
               ▲                              │
            Saves  <── serialize / restore ───┘
```

## 03.1 The headless rule
- `sim/` holds **all** game rules and state. It runs under `godot --headless` with no scene tree. Every GDD rule is testable there (§16).
- `GuildState` is the single root of simulation state: clock, guild stats, roster, operations, inventory, work orders, market, requests, flags, the Commander and the bonds.
- Presentation **reads** state through read-only accessors, and **changes** it only by sending commands. It never writes fields directly.

## 03.2 Commands and events [spec decision]
- **The command and event envelopes are defined in §07.1:** `SimCommand` / `CommandResult` / `SimEvent`, with revision checks, stable error codes and receipts. A failed command changes nothing, including RNG state (the no-mutation-on-failure rule).
- Presentation calls `SimHost.submit(command)`. Each module lists its command kinds (§07.2).
- **Events:** `SimHost` re-emits committed `SimEvent`s as the signal `sim_event(ev)`. Presentation subscribes; alerts, field view and HUD react only to events and state.
- **Watch equivalence:** events are produced identically whether or not anything is watching. Watching changes only the real-time rate (§05), never the command or RNG sequence.

## 03.3 Determinism
- All randomness comes from `sim/rng.gd` streams (§08).
- No `randf()`, `Time` or frame-rate-dependent code in `sim/`. The simulation advances in whole ticks of **12 company seconds**.

---

# 04. Application state machine (`Game`)

| State | Enters when | What runs | Leaves to |
|---|---|---|---|
| `boot` | Launch | Settings, content load and validation (a failure shows the validator report and stops) | `title` |
| `title` | Boot done | Title screen: continue, new game, load, settings | `profile`, `scene` (new game), `world` (load) |
| `scene` | A script scene starts (new game, story trigger) | `ScenePlayer` plays a converted scene (§09); control locked unless the script unlocks it | the state the scene hands off to (`world`, next `scene`) |
| `world` | Exploration (town, HQ, interiors) | Commander movement, talks, barks, ambient lines; the clock runs (07:00–20:00 day, night after) | `overlay`, `field`, `closeout`, `scene`, `sleep` |
| `overlay` | A management screen, dialogue, shop or minigame opens | The UI screen; **the clock pauses** (GDD 4) | the previous state |
| `field` | Watch battle / View / Follow from the Ongoing list | The field view (§11); battle pace ¼ while a fight is on screen | the state it was opened from (`world` or `overlay`), restored with its screen and selection (GDD 15; FGC_08 P7) |
| `closeout` | 20:00 cutoff | Resolution, then the Day Summary (with weekly payroll when due), sim paused | `world` (night) |
| `sleep` | Bed used after 20:00, or the 01:00 auto-sleep | The night jump to 07:00, autosave, the morning screen | `world` (day) |

- **Overlays stack**, but only one is interactive. The clock is paused while any overlay is open (one foreground-modal rule, GDD 4).
- Story triggers such as the 14:00 return or flashpoint scenes are **sim events** (`story_trigger`). `Game` turns them into a `scene` state at the next safe moment, never in the middle of an overlay.

---

# 05. Clock integration (`SimHost`)

- **Real time to company time:** `company_seconds += delta × speed × 120`, where speed is 0 (paused), 1, 2 or 4. While a fight is on screen in the field view, the rate is × ¼ (battle pace; GDD 4).
- **Fixed ticks:** accumulated company time is consumed in **12 s ticks**. Each tick runs `tick_pipeline.gd` through `advance_ticks(1)` in the phase order of §07.3 (GDD 4.1): completed combat actions, then timed events, then the cutoff, then new starts. It returns events. Time is stored as absolute ticks (7,200 per day; 07:00 = tick 2,100; 20:00 = tick 6,000).
- **A frame's cap:** at most 120 ticks per frame (24 company minutes). Any excess carries to the next frame, so 4× on a slow frame never skips logic. [spec decision]
- **Pausing:** `SimHost.pause_reasons: Dictionary` holds a reason per source (`"overlay"`, `"scene"`, `"closeout"`, `"user"`). The clock runs only when it is empty.
- **Cutoff (20:00):** the sim emits `day_cutoff`. `Game` enters `closeout`. After the summary, the sim is in **night mode**: no operations, and the clock runs at 1× for walking until sleep (GDD 4.2).
- **Sleep:** the command `sleep` performs the night jump to 07:00 (GDD 4.1's 11-hour accounting, never counting awake night time twice), then emits `day_started`.
- **Testing:** headless tests call `advance_ticks(n)` directly and never touch real time.

---

# 06. Content data formats


## 06.1 Layout, serialization and identity

**[spec decision]** D01 Use UTF-8 JSON, one record per file, schema dialect JSON Schema 2020-12. Authoring and runtime use the same strict schemas; a separate semantic validator handles references and rule relationships. Decode into immutable typed `RefCounted` definitions; JSON dictionaries never escape `Content` as mutable shared objects. Numbers are finite; whole counts are JSON integers. Durations are whole Guild/calendar seconds, never real seconds. Percentages use fractions unless named `_pct` (0–100) or `_points` (percentage points); seconds are converted to ticks with `ceil(seconds / 12)`. No arbitrary GDScript, resource constructors or expressions may appear in data.

```text
content/
  manifest.json                       # content revision, file list and hashes
  schemas/{shared,<record_type>}.schema.json
  common/{rework_rules,commander_skills,officers,minigame_templates,rules}/
  eurydica/{regions,areas,monsters,materials,recipes,processing_yields,finds}/
  eurydica/{requests,repeat_orders,contracts,flashpoints,adventurers,staff}/
  eurydica/{buyers,hq_upgrades,minigame_templates,rumour_sources}/
  frontier/<area_id>/<same record families>/
  scenes/                             # generated scene JSON; contract owned by §09
  aliases.json                        # explicit source/legacy ID mappings
  visual_bindings.json                # pose/palette IDs -> presentation assets
```

`manifest.json = {"id":"fgc_content","region":"common","rev":1,"schema_version":1,"content_revision":"<sha256>","files":[{"path":"eurydica/materials/boar_hide.json","sha256":"<sha256>"}]}`. Paths are relative to `content/`, sorted bytewise, with no `..` or absolute paths. The revision hashes the canonical ordered `files` list; it excludes itself. **[spec decision]** D02 Stable identity is `(record_type,id)`; foreign-key fields have one declared target type. Cross-type equal IDs such as `eurydica` are legal, duplicates within a type are fatal. All records have `id`, `region`, `rev`; IDs match `^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$`. `rev` is a positive authoring revision, not a save schema version. Display text is independent of IDs.

Preserve existing material IDs: **`common_slime_part` = Slime Gel**, **`rare_slime_part` = Slime Core**. `slime_gel`/`slime_core` are aliases, never duplicate stock categories. Legacy `campaign_catalog.gd:6–17` confirms those IDs; the town proof's `slime_gel` is an alias. Preserve `boar_hide`, `boar_meat`, `wolf_pelt`. Do not resurrect obsolete `redstone_boar_corpse` as a new GDD species.

**[spec decision]** D03 Canonical request IDs are `ch1_req_001`…`ch1_req_007`, repeat IDs `eur_wo_001/002`, contract IDs `eur_sub_01`…`eur_sub_08`. Keep `source_id` exactly as GDD (`CH1-REQ-003`, etc.), with explicit aliases from legacy `ch1.request.03` and authored display IDs. Story milestone lookup accepts preserved `M02/M03/M05/M06/M08` tokens and resolves them to `m02/m03/m05/m06/m08`; retain original tokens in source provenance and migration data. Existing dialogue line/choice IDs are opaque authored anchors, preserved verbatim inside scene records; new **record** IDs obey snake_case. Never mass-replace manuscript IDs or `<Guild-name>` tokens.

## 06.2 Schemas and representative records

The companion `schemas/` folder contains **one actual JSON Schema per required record type**, plus `shared.schema.json`; `examples/` contains one GDD-derived JSON record for each. These files are part of this draft and should be copied with it for merge review. All top-level schemas are closed objects (`additionalProperties:false`), with all enumerated fields required; nullable fields are explicitly nullable. Common fields are `id`, `region`, `rev`, `name`, `gdd: string[]`, `authoring_status: specified|incomplete`, `missing_fields: string[]`.

| Record / schema and example | Exact fields after common fields | GDD example and governing section |
|---|---|---|
| [monster](schemas/monster.schema.json), [example](examples/monster.json) | `area_id,tier,parent_id,stats,base_xp,knowledge_pct,processing_yield_id,skill,poses,variant_palette_ref,group_chance` | Moss Slime: HP 180, ATK 4, DEF 0, rate .7, XP 6, group .60; §§2.2, 9.3b, 10.1. Skill null explicitly pending approved species assignment. |
| [material](schemas/material.schema.json), [example](examples/material.json) | `base_value_g,qualities,quality_multipliers,part_kind,source_monster_ids,aliases` | Boar Hide 12G Standard; quality values 0/.5/1/1.25; §§10.5, 12.1. Runtime quality belongs to a stock lot, never to a material definition. |
| [recipe](schemas/recipe.schema.json), [example](examples/recipe.json) | `inputs,fee_g,duration_seconds,output_item_id,output_count,output_forms,category,footprint,effects,gate` | Vest: 4 Standard+ hides +40G, 7,200 s, 2×2, +30 HP/+8 DEF; §12.2. Output forms are alternatives for one output, never multiple rewards. |
| [rework_rule](schemas/rework_rule.schema.json), [example](examples/rework_rule.json) | `input_quality,input_count,output_quality,output_count,duration_seconds,requires_perk,forbidden_perks,same_material` | Mend 2 Damaged→1 Standard, 14,400 s. Also author Refine grade 2 Standard→1 Pristine/14,400 s and Master's Salvage 3 Damaged→1 Pristine/21,600 s with perk; §12.8. |
| [processing_yield](schemas/processing_yield.schema.json), [example](examples/processing_yield.json) | `monster_id,duration_seconds,common,rare,guaranteed,quality_roll_scope,raw_reference_g` | Boar 2 meat+1 hide, 20% one tusk, 2,700 s, raw reference 36G; §§10.1, 10.5. Variant adds exactly one elite part; rare guarantees parent rare and has no extra rare/elite roll. |
| [region](schemas/region.schema.json), [example](examples/region.json) | `area_ids,chapter_start,operating_base,track_cap,lifetime_xp_cap,enhancement_cap,staff_rank_cap,commander_skill_cap,rank_ceiling,local_generators` | Eurydica caps 6/3,000/2/2/2/C, Chapters 1–2; §16a. `region` here describes campaign/base configuration, `area` a hunting ground. |
| [area](schemas/area.schema.json), [example](examples/area.json) | `base_id,rank_required,ordinary_ids,landmark_ids,path_ids,rare_ids,boss_ids,scout_injury_chance,initial_exploration_pct,route_rules` | Hylaea F, three ordinary species, three landmarks (two dens), two paths, 1% risk; §§7–8. `redstone` preserves legacy area identity; display is Erythra Highlands. |
| [find](schemas/find.schema.json), [example](examples/find.json) | `area_id,kind,weight,gate,unique_scope,monster_id,effects` | Charcoal Burners' Trail: ≥10%, weight 3, −300 s search; §8.2. Den eligibility additionally checks species identification before applying benefits. |
| [request](schemas/request.schema.json), [example](examples/request.json) | `source_id,client_id,offer_event,inputs,reward,deadline_seconds,deadline_origin,accepted_failure_rep,chapter_end_withdrawal,completion_access,alternatives,transitions` | Rare Slime Order: 2 cores any condition, 25G/100 Rep, 172,800 s from offer; accepted 15-gel substitution; §§11.1–11.2. |
| [repeat_order](schemas/repeat_order.schema.json), [example](examples/repeat_order.json) | `source_id,client_id,unlock_request_id,inputs,reward,wait_seconds,wait_origin,max_outstanding,deadline_seconds,inactive_policy` | Hilde: 4 Standard+ meat, 60G/5 Rep, 604,800 s after first/repeat completion, no deadline or backlog; §11.2. |
| [contract](schemas/contract.schema.json), [example](examples/contract.json) | `source_id,client_id,gate,encounter,approach_seconds,offer_duration_seconds,reoffer_wait_seconds,reward,completion_flag,accepted_failure_rep,random_groups,random_variants` | EUR-SUB-02: M08, F, boar known; two boars, 1,800 s approach, 72 h offer, 140G/20 Rep; §11.3. |
| [flashpoint](schemas/flashpoint.schema.json), [example](examples/flashpoint.json) | `gate,boss_id,approach_seconds,reward,completion_flag,aftermath,offer_duration_seconds,failure_rep,repeat_reward,guest_ids` | Chimera: Chapter 2/E/300 Rep, 900G/250 Rep, Hylaea risk .005 and target share .85; §11.4. Guests require explicit authored formation; example assumes none. |
| [adventurer](schemas/adventurer.schema.json), [example](examples/adventurer.json) | `specialty,stats,reach,meter_role,traits,passive_id,signature,modifier_choices,hire_g,weekly_wage_g,gate,initial_tracks` | Anselm 180/18/10/1, Shieldbearer, Phalanx, all eight modifier choices, 250G/90G; §§6, 12.6. |
| [staff](schemas/staff.schema.json), [example](examples/staff.json) | `role,hire_g,weekly_wage_g,station_kind,gate,ranks` | Konrad 150G/60G, ranks at 0/40/100 productive hours, cost 0/200/400G; §12.6. |
| [officer](schemas/officer.schema.json), [example](examples/officer.json) | `department,join_event,payroll_g,romanceable,bond_cap,max_levels_per_week,bond_thresholds,bond_awards,bond_five_story_flag,friendship_scene_ids,perks,fallback_service` | Fulker, no wages, no romance, Rough Patch/Master's Salvage; §§5.4, 12.6, 12.8. Unknown bond quantities are null, not invented. |
| [buyer](schemas/buyer.schema.json), [example](examples/buyer.json) | `persona,faction,taste_tags,ceiling_factor_range,patience_range,sampling_profile,initial_acceptance_rule,tactics,tell_mapping,allow_barter,allow_multi_item` | Travelling Merchant, honest tells; legal ceiling envelope .8–1.4, patience 3–5; §5a.2a. Envelope is not an asserted uniform sampling distribution. |
| [commander_skill](schemas/commander_skill.schema.json), [example](examples/commander_skill.json) | `officer_ids,template_kinds,rank_thresholds,rank_cap,eurydica_cap,points_by_grade,dialogue_points,per_rank_effects,rank_three_unlock,session_seconds,session_effects` | Leadership, cumulative 10/25/45/70/100, D–S 1–5, rank-3 Encouragement, Briefed 10/S 15; §5a.2. |
| [hq_upgrade](schemas/hq_upgrade.schema.json), [example](examples/hq_upgrade.json) | `preview_gate,purchase_gate,inputs,fee_g,duration_seconds,effects,unique,refund_before_completion` | Annex 600G+6 Standard+ hides, 86,400 s, beds 2→4; §12.7. |
| [minigame_template](schemas/minigame_template.schema.json), [example](examples/minigame_template.json) | `kind,officer_id,skill_id,rank_min,rank_max,fields,generator_id,solver_id,grading_rule_id,hint_grade_cap,session_seconds` | Expedition Planning field contract only; §5a.2a. No puzzle artwork, UI or generated template implementation in this draft. |

`shared.schema.json` defines `stats={hp,atk,def,rate}`, input `{item_id,quantity,min_quality}`, reward `{gold,reputation,effects}`, effect `{op,target,value,duration_actions}`, and predicate nodes `{all:[…]}`, `{any:[…]}` or `{fact,cmp,value}`. Empty `all` is true. Supported comparisons are `eq,gte,lte,contains,not_contains`; ordered enums compare by declared domain order (F<E<D<C<B<A<S; Unsellable<Damaged<Standard<Pristine), not lexical order. Predicates only read registered facts. Effects execute through the owning module, not arbitrary field writes. **[spec decision]** D04 The validator maintains typed fact/effect registries in `sim/rules/fact_registry.gd` and `sim/rules/effect_registry.gd`; unknown op/target pairs fail. Effect ordering is array order; all effects of a reward are one transaction. Tactics distinguish `eligible` (can play) from `effective_when` (can help): Show quality only helps Standard/Pristine, without inventing a prohibition on selecting it for Damaged stock. `accepted_failure_rep` checks the transition's penalty magnitude; it does not add a second debit alongside that transition effect.

Monster `poses` requires idle/attack/skill/hurt/defeat and second_hurt for bosses. Binding IDs are implementation identifiers, not a claim that assets already exist. Variants inherit parent's skill and pose bindings with palette reference and 1.15 visual scale; HP×1.5/ATK×1.25/DEF×1.25/rate unchanged. Their skill is not a second independently authored skill. Tier multipliers apply once. Raw corpse identity stores species/tier and has no processed quality until its sticky roll.

Officer perk data must contain these **two choices each**, at Bond 5 after personal beat, immutable after selection (GDD §5.4):

| Officer | First choice | Second choice |
|---|---|---|
| Tristitia | `tight_ship`: payroll×.90; Morale−1/week | `open_door`: +1 Morale at injury-free Day Summary; payroll×1.05 |
| Elsie | `hard_drills`: fight XP×1.15; rest restores 2 bars instead of full | `easy_pace`: rest shortens injury 24 h; fight XP×.90 |
| Mae | `quick_hands`: processing 25% faster; Pristine probability×.75 | `careful_cuts`: Pristine probability×1.25; processing 25% slower |
| Fulker | `rough_patch`: Rework duration×.5; Mend only | `masters_salvage`: unlock 3 Damaged→1 Pristine, 6 h |
| Liliana | `wide_net`: +1 morning lead/rumour; accuracy−10 points | `deep_analysis`: accuracy+10 points, horizon+1 day; no morning rumours |
| Valerie | `volume_trader`: +2 slots; ≥10-unit listings pay +10%; minimum listing 10 | `premium_seller`: Pristine buyer payment×1.25; prohibit Damaged market/trader/negotiation sales |

Store positive and negative effects together. No default perk, no officer romance, no off-screen auto-choice. Duration interpretation and probability redistribution questions are recorded in §06.7 rather than silently tuned here.

Other template kinds have the following field contracts (only fields, as requested):

| `kind` | Required generated payload fields and GDD constraints |
|---|---|
| `expedition_planning` | `grid,start,goal,water,rest_spots,threat_zones,time_budget_hours,stamina_budget,rest_limit,optimal_score`; 9×7 Eurydica/up to 15×11 Frontier; 12 h/10 stamina, two rests costing 2 h/restoring 3; optional authored `fog,mid_route_event,night_tiles`; solver must prove reachable goal and fair grade reference. |
| `counter_offer` | `order_id,buyer_id,stock_lot_ids,item_id,quality,quantity,market_value_g,ceiling_g,patience,initial_acceptance_g,tactic_table,tell_table`; Frontier-capable `barter_options,bundle_entries`; secrets stay in session state, never ordinary view-models. |
| `cross_check` | `documents,facts,conflicts,evidence_links,correct_resolutions,soft_timer_seconds`; 2–4 documents, 3–6 conflicts, about 180 real seconds; authored `forgery,unit_conversions,orientation` when applicable. |
| `cutting_chart` | `species_id,corpse_id,job_id,cut_lines,no_cut_zones,speed_band,score_weights,required_order`; 3–6 guides; actual geometry/weights require authored content. |
| `fitting` | `job_id,frame_cells,pegs,parts,notches,key_part_id,par_moves,par_time_seconds`; authored `adjacency_rules,shift_rules`; solver validates exact fill, peg/notch matching and key-part-first. |

**[spec decision]** D05 `generator_id`, `solver_id`, `grading_rule_id` are registered built-in strategies. Data can supply new boards/personas/species using existing mechanics; arbitrary new mechanics require code. Generator results and input snapshots persist on session start; reopening does not reroll.

## 06.3 Request state machine data and instances

Every request definition supplies its transition table; the engine rejects tables outside GDD §11.1:

| From / trigger | To / atomic outcome |
|---|---|
| Hidden / actual offer branch | Offered; store first appearance and absolute deadline once; merely seeing NPC or declining earlier is no offer. |
| Offered / accept | Accepted; preserve deadline; reserve selected partial quantities explicitly. |
| Offered / deadline | Expired; no penalty. |
| Offered / Chapter 1 end, IDs 003–007 only | Expired with reason `chapter_withdrawn`; warning before chapter commit; no penalty. |
| Accepted / eligible delivery at client or authorised courier | Completed; consume full quantity lowest acceptable quality first, release reservations, award once. At the exact deadline this wins over expiry. |
| Accepted / eligible gel alternative | Completed; consume 15 gel once, release core reservation, grant same reward, no tradable cores or sales Rep. |
| Accepted / timed expiry | Expired; −10 Rep once, no Morale loss. |
| Accepted / abandon or failed optional attempt | Failed; −10 Rep once. No-deadline deliveries never fail for waiting. |
| Terminal / repeated command | No new payout, consumption or penalty. |

**[spec decision]** D06 Request instances use `{instance_id,definition_id,state,offered_at_tick,accepted_at_tick,deadline_tick,deadline_remaining_transfer_ticks,reservation_ids,alternative_enabled,alternative_used,completion_event_id,failure_event_id,terminal_reason}`. Repeat instances additionally have `{next_offer_tick,paused_wait_ticks,suspended,sequence}`; contracts have `{attempt_operation_id,reoffer_tick,succeeded_once}`. Flashpoint offer availability is distinct from attempt status: failure closes that attempt, retains the offer and charges no Rep. `offered_at_tick` is immutable; `deadline_tick=null` means no deadline, not zero. Alternative access for Garden begins with ≤24 h remaining and <2 cores obtained/reserved for that request, including acceptance inside the window. Rare Slime Order gets its alternative on acceptance. Accepted deliveries survive chapter/base changes; only their timers freeze during transfer.

All seven deliveries must be transcribed exactly:

| ID suffix | Client | Inputs | Gold / Rep | Appearance deadline | Persistent result |
|---|---|---|---|---|---|
| 001 | `eur_inn_owner` | 5 gel any | 50 / 50 | 5 days | Bathroom flag, M02 offer |
| 002 | `eur_garden_steward` | 2 cores any | 100 / 50 | 4 days | Garden flag, M02 offer, final-24h gel safeguard |
| 003 | original trader client | 2 cores any | 25 / 100 | 2 days | Order flag, gel safeguard |
| 004 | Dr. Emmerich | 10 gel any | 100 / 20 | 6 days | 4 potions/week at 18G, reset days 1/8/15…; any-base counter |
| 005 | Jeb | 3 Standard+ wolf pelts | 75 / 25 | none | Free Eurydica board courier after visiting Jeb for this first completion |
| 006 | Hilde | 4 Standard+ boar meat | 60 / 20 | none | Roast flag; Hilde repeat after 7 days |
| 007 | Gerd | 2 Standard+ boar hides | 40 / 20 | none | Repair flag; Vest preview; Gerd repeat after 7 days |

Client IDs in examples (`travelling_merchant`, etc.) are provisional binding keys, not renamed legacy identities: migration/conversion must preserve the exact client source ID through `aliases.json` after scene conversion. Clients remain accessible through accepted-request interaction regardless of ambient schedules. Delivery escrow at HQ before courier is not completion.

## 06.4 Region tag rule

GDD §16a.1 governs **generation**, not inventory deletion. All local generation is `record.region == GuildState.active_base_id`, including every referenced local material, customer, forecast category and negotiation line item. `common` is allowed for reusable mechanics, officers and templates, but is **not** a wildcard to draw Eurydica goods into Frontier orders. A common template must bind only active-base local references. Bindings are validated after generation as well as at content load.

Eurydica's three hunting areas have `region:"eurydica"`; Frontier area's authored base/region ID will be its tag. After transfer: no new Eurydica requests/repeats/rumours/forecasts/listings/negotiation/Standing offers/hints. Held Eurydica stock remains tradable through any-trader, usable in recipes that explicitly accept it, and deliverable on previously accepted orders. Journal and dormant base state persist. Repeat wait/offer suspension is stored, never simulated as a second HQ. Purchased global capacities are not charged again.

## 06.5 Content validator

**[spec decision]** D07 `tools/validate_content.gd` exposes `validate(root: String, release: bool) -> Array[ContentIssue]` and CLI `--root=… --mode=draft|release --report=…`. `Content` runs identical validation before publishing the registry. Schema structure plus semantic checks are mandatory; schema success alone cannot launch a campaign.

Checks: parse errors and duplicate JSON keys; exact field/type/enum/range checking; duplicate typed IDs; aliases acyclic/unambiguous; all typed references resolve; positive/sensible durations and finite numbers; region/base matching and generator closure; stat/skill/variant constraints; mandatory pose bindings and release asset existence; exactly three ordinary species/three landmarks (two dens)/two paths per opening area; unique find ownership; bounded probability distributions and quality sums; tier-exclusive XP/yields; inputs and outputs resolve; no Unsellable Reworking; recipe quality and footprint compatibility; monotonic progression/skill/rank thresholds; perk pairs and opposing effects; prerequisites and scene dependencies acyclic; permanent flags/rewards not duplicated; request transition legality, deadlines, alternatives and courier access; repeat single-instance rules; no random groups/variants in fixed contracts; no flashpoint expiry/penalty/repeat payout; no invented Frontier definitions; minigame registered solver and valid generated puzzle; release rejects incomplete records and unresolved design conflict dependencies. Relations like `ordinary_ids` exactly 3 and `perks` exactly 2 are semantic checks even where a JSON array schema only sets a minimum.

Release rejects null required-to-run skill/persona/bond values. Draft permits explicitly incomplete examples, reports warnings, and does not claim a shippable database. Structural defects remain errors in draft. All `missing_fields` entries must identify a null, omitted authored collection, or documented external authoring dependency; `specified` records must have an empty list. Unknown fields do not receive silent defaults.

Error format, JSON Lines sorted by `(file,pointer,code)`:

```json
{"severity":"error","code":"FGC_CONTENT_REF","file":"content/eurydica/recipes/boarhide_vest.json","pointer":"/inputs/0/item_id","record_type":"recipe","record_id":"boarhide_vest_recipe","gdd":"12.2","message":"Unknown material id: boar_hdie","related":["content/eurydica/materials/boar_hide.json"]}
```

Stable codes include `FGC_CONTENT_PARSE,TYPE,FIELD,ID,REF,REGION,RANGE,RULE,AUTHORING,ASSET` with the same prefix. Exit 0 = no errors; 1 = content errors; 2 = invocation/I/O failure. Registry activation is all-or-nothing. No errors hidden behind a default value or a partial successful load.

## 06.6 Shared rule data

**[spec decision]** D08 Fixed tuning tables are versioned JSON under `content/common/rules/`, checked by dedicated typed loaders and golden cases, not repeated constants in unrelated modules. Required tables: `clock`, `progression`, `stamina_injury`, `quality_by_staff_rank`, `staff_ranks`, `market`, `guild_ranks`, `morale`, `debt`, `difficulty`, `enhancement`, `backpack`, `commander_sessions`. These are support tables, not additional authored monsters/quests. Each has `id,region:"common",rev` and explicit named fields, including GDD provenance per rule. The nineteen schemas here cover the requested record families; full support-table schemas are a subsequent implementation task, not claimed as delivered launch data.

## 06.7 Source gaps and conflicts — do not convert these into game rules

**Review status (Claude, 2026-09-28):**
- **Resolved in the GDD:** items 2 (bond point values, GDD 5.4), 4 (Workshop reservation at job start, 12.2), 5 (Reworking ignores Morale, 12.8) and 6 (perk arithmetic and the fixed-roll odds table, 5.4 and 12.1).
- **Item 1 resolved:** the owner approved the monster skills on 2026-09-28 (`Eurydica Monsters.md`).
- **Still open:** item 3's tuning numbers are set by the M3 minigame prototypes (GDD 5a.2a).


1. `Production Assets Requirement/Eurydica Monsters.md` explicitly labels species skill names/effects as **proposed**; some production chapter labels also lag GDD. GDD §9.3b budgets/timing and §§11.4/16a Chapter 2 placement win. Release needs approved skill assignments; the example skill is null rather than an invented Slime move.
2. GDD §5.4 specifies bond sources and weekly gating, but not numeric point thresholds/awards. Do not equate session skill points with bond points without authored data. Romance cast, gift values, and scenes remain authoring work; romance has no stat perks.
3. GDD §5a.2a gives negotiation ceiling/patience bounds and qualitative tactics, not complete persona-specific distributions, starting acceptance, numerical tactic changes or exact tell thresholds. `Characters/Negotiation Buyers Roster.md` supplies proposed narrower values (e.g. Merchant 80–105%/5 rounds) but labels its designs/personas proposals and retains superseded chapter numbers. Do not silently promote those proposals into approved GDD rules. Buyer fields reserve the contracts; null is not zero or uniform. Cutting Chart scoring weights/speed band, Fitting par generation and edge-case grade normalization likewise require approved authored parameters. Do not invent rewards for failed Planning/Cross-check beyond explicitly stated GDD consequences.
4. GDD §12.2 says queued ingredients are reserved explicitly; newer §12.2a expressly says Workshop inputs are reserved **when a job starts, not when queued**. This draft follows the specific newer work-order rule: waiting recipes are intents without a material claim; start revalidates availability, and a player reservation owned by another system is never stolen. Note this wording reconciliation at merge.
5. GDD §13.2 says Morale changes processing only, while §12.8 explicitly says Reworking uses staff rank and Morale “like other Workshop jobs.” Preserve an explicit `morale_applies` rule dependency for Reworking and flag the broader Workshop wording for GDD reconciliation. Do not silently broaden Morale to ordinary crafting/enhancement. Until reconciled, the affected release rule table fails `FGC_CONTENT_RULE`.
6. GDD §5.4's processing “25% faster/slower” does not unambiguously say throughput or duration, nor where relative Pristine-probability changes take/return probability mass. GDD §12.1 fixes a roll when first queued, while a later Cutting Chart session can change that job's odds (§5a.2a). Persist underlying random variates and modifier provenance (§07.4), but require the final approved odds/redistribution contract before release. No independent new roll is allowed.

These are visible source-authoring/wording issues, not permission requests and not delegated design changes. Drafting proceeds with strict interfaces; a full implementation must resolve them in the GDD.

**Frontier readiness:** local data uses active-base tags and typed references; new authored records plug into existing systems without hard-coded Eurydica branches. Unknown new mechanics still require an explicit extension; missing Frontier content is never fabricated.

---

# 07. Simulation modules


## 07.1 State and bus contract

All `sim/` classes are typed GDScript `RefCounted`, with no Node, SceneTree, FileAccess, rendering, audio, autoload lookup or wall-clock dependency. `SimHost` owns exactly one `GuildState`; `Game` owns screen/modal flow; `Content` supplies immutable definitions; `Saves` performs I/O. `Audio` and `Settings` are presentation/application services. Commands enter through `SimHost`, never by editing returned dictionaries.

**[spec decision]** D09 `sim/command_bus.gd` and `sim/event.gd` define:

```gdscript
# Contract fields; explicit typed classes implement these records.
SimCommand { id: String, kind: StringName, expected_revision: int,
             issued_at_tick: int, payload: Dictionary }
CommandResult { ok: bool, command_id: String, code: StringName,
                message_key: String, revision: int, events: Array[SimEvent] }
SimEvent { id: String, tick: int, phase: int, sequence: int,
           kind: StringName, entity_id: String, payload: Dictionary }
submit(command: SimCommand) -> CommandResult
advance_ticks(count: int) -> Array[SimEvent]
snapshot() -> GuildSnapshot
events_after(sequence: int) -> Array[SimEvent]
```

Commands validate expected revision, IDs/types, eligibility, resources and reservations before modifying anything. Failure returns a stable code (`stale_revision,invalid_argument,not_available,insufficient_gold,reserved,locked,cutoff`) with unchanged simulation and RNG. Successful commands stage writes on a transaction, commit once, bump revision and publish immutable events after commit. Reusing a committed command ID with identical payload returns its saved receipt; different payload returns `command_id_conflict`. No event subscriber can trigger an immediate reentrant mutation. Effects requesting another system's change route through the transaction coordinator, not observer signal ordering.

Input commands are ordered by accepted command serial. They execute at the current settled tick boundary, including while paused, before advancing to a later tick; already resolved historical events cannot be retroactively undone. Event ID is `event_<monotonic serial>`, operation ID `op_<monotonic serial>`; compare numeric serials for ties, not lexicographic `op_10` versus `op_2`. Persist serial counters, command receipts and once-only effect receipts. Client retry IDs are saved when a safe checkpoint contains the transaction. Rendering events may be dropped/rebuilt; the authoritative receipts cannot.

**[spec decision]** D10 `sim/guild_state.gd` stores these named aggregates:

```text
revision, serials, rng, command_receipts, effect_receipts,
clock, difficulty, active_base_id, guild, roster, former_staff, prep_templates,
inventory, reservations, operations, combat, discoveries,
processing, workshop, construction, markets, information,
negotiation, requests, repeat_orders, contracts, flashpoints,
commander, bonds, romance, story, projects, transfer, journal
```

Substate has one write owner, listed below. Read models are copies. Instance IDs never reuse deleted serials; content IDs never depend on translated names. Inventory owns `{lot_id,item_id,quality,quantity,origin,actual_purchase_g}` and unique equipment/corpse instances; reservations own claims by owner ID. Gold transaction ledger owns gross/fee/net/debt-sweep classification. Values requiring fractions (HP regeneration, XP modifiers, wage accrual) retain fractional precision until the GDD's stated rounding point; whole item counts and tick times never use floats. No implementation may round each day's wage independently.

## 07.2 System ownership map

The table names **proposed exact files**, public command payloads, emitted event kinds and owned state. `internal` entries are deterministic coordinator calls, not UI-accessible commands.

| Module (`res://sim/…`) / GDD | Commands or internal inputs | Events | Owned state |
|---|---|---|---|
| `clock.gd`, `tick_pipeline.gd` / §§4, 4.1–4.2, 16b | `advance_ticks(count)`, `sleep`, `set_pending_difficulty(mode)` | `tick_completed,cutoff_reached,new_day,difficulty_applied` | `clock{absolute_tick,day,phase,last_sleep_credit_day,last_closeout_day}`, `difficulty{active,pending}` |
| `operations.gd` / §§8.1, 9.1, 11.3–11.4 | `dispatch_hunt(area_id,target_id,duration_ticks,formation,loadout)`, `dispatch_scout(area_id,duration_ticks,person_id,loadout,repeat_survey)`, `dispatch_contract(contract_instance_id,formation,loadout)`, `dispatch_flashpoint(flashpoint_id,formation,loadout)`, `recall(operation_id)` | `operation_dispatched,search_completed,encounter_started,operation_returned,resolution_ready` | `operations{party,kind,phase,start_tick,end_tick,target,sighting_reservation,secured_corpses,xp_ledger,settlement_receipt}` |
| `combat_engine.gd`, `combat_effects.gd` / §§6.2a–c, 9.1a–9.3b | internal `start_encounter(op_id,encounter)`, `finish_actions(tick)`, `charge(tick)`, `start_ready_actions(tick)`, `cancel_inflight(op_id)` | `action_started,action_completed,damage_applied,status_applied,actor_downed,kill_secured,fight_won` | `combat[op_id]{fighters,build_snapshots,gauges,ready_queue,inflight,meters,statuses,target_ids}` |
| `scouting.gd`, `discovery.gd` / §§7–8, 16a | internal `complete_interval(op_id)`, `grant_verified_record(record)`, `mark_surveyed_route(path_id,op_id)` | `exploration_changed,species_identified,find_acquired,rare_sighting_created,route_surveyed,scout_injured` | `discoveries[area_id]{progress,known_species,fixed_finds,hints,sightings,route_flags}` |
| `progression.gd` / §6.2c, §12.3 | `commit_build(person_id,tracks,modifier_ids)`, `rebuild(person_id,build)`; internal `award_xp(person_id,source_id,amount)` | `xp_awarded,build_committed,modifier_unlocked` | roster-owned progression partition `{tracks,selected_modifiers,xp_spendable,xp_lifetime,rebuild_used}` |
| `roster.gd`, `recovery.gd` / §§6.3–6.5, 12.6 | `hire(person_id)`, `dismiss(person_id)`, `rehire(person_id)`, `order_rest(person_id)`, `cancel_rest(person_id)`, `promote_staff(person_id)`; internal elapsed calendar segments | `employee_hired,employee_left,injury_started,injury_expired,rest_resolved,hp_recovered,staff_promoted` | roster employment/HP/stamina/injury/rest/dispatch history, former staff; staff rank/productive ticks |
| `inventory.gd`, `backpack.gd`, `reservations.gd` / §§6.6, 12, 15 | `commit_backpack(person_id,placements,active_categories)`, `save_prep_template(slot,name,formation,loadout)`, `delete_prep_template(slot)`, `reserve(owner_id,claims)`, `release(owner_id)` | `inventory_changed,reservation_changed,backpack_committed,prep_template_saved,potion_consumed` | `inventory,reservations,prep_templates`, roster backpack partition; bound equipment/origin/quality identity |
| `processing.gd` / §§10.5, 12.1, 12.6 | `set_processing_order(corpse_ids)`, `remove_processing_job(job_id)`; internal assign/finish/abort/resume | `processing_started,processing_completed,processing_cancelled,quality_committed` | `processing{order,stations,jobs}`, corpse roll/provenance partition in inventory via transaction |
| `workshop.gd` / §§12.2–12.3, 12.8 | `queue_craft(recipe_id,form_id)`, `queue_enhancement(person_id,next_level,input_species_id)`, `queue_rework(rule_id,item_id)`, `reorder_workshop(job_ids)`, `cancel_workshop(job_id)` | `workshop_started,gear_crafted,enhancement_completed,rework_completed,workshop_cancelled` | `workshop{order,stations,jobs,input_escrow,fee_escrow,duration_snapshot}` |
| `market.gd` / §12.4, §16a.1 | `list_stock(lot_claims,unit_price_g)`, `reprice(listing_id,price_g)`, `cancel_listing(listing_id)`, `sell_to_trader(claims)`, `buy_consumable(item_id,quantity)` | `listing_created,sale_completed,purchase_completed,demand_generated` | `markets[base_id]{demand_days,listings,hour_checks,category_quota}`; inventory/gold changes through coordinator |
| `information.gd` / §§7.3, 12.5, 5a.2 | internal `deliver_morning_service(day)`, `deliver_forecast(category_id,target_day)`, `verify_record(record_id)` | `forecast_delivered,rumour_delivered,lead_revealed,record_verified` | `information{saved_predictions,confidence,service_days,rumours,verified_records}` |
| `negotiation_orders.gd` / §5a.2a, §16a.1 | internal `generate_daily_order(day)`; `begin_negotiation(order_id)`, `submit_negotiation_round(session_id,price_g,tactic_id,extra_claims)` | `negotiation_order_posted,order_unavailable,negotiation_round_resolved,negotiation_closed` | `negotiation{daily_order,session,buyer_secrets,patience,rounds,stock_claims,sale_receipt}` |
| `requests.gd` / §§11.1–11.2 | `reveal_request(id,offer_anchor)`, `accept_request(instance_id)`, `reserve_delivery(instance_id,claims)`, `deliver_request(instance_id,channel,alternative_id)`, `abandon_request(instance_id)` | `request_offered,request_accepted,delivery_reserved,request_completed,request_expired,request_failed` | `requests`, once-only exchange and persistent client benefits |
| `repeat_orders.gd`, `contracts.gd`, `flashpoints.gd` / §§11.2–11.4 | internal eligibility/deadline/completion; `accept_contract(id)`, `abandon_contract(id)`; dispatch through operations | `repeat_offered,repeat_suspended,contract_offered,contract_completed,contract_failed,flashpoint_available,flashpoint_cleared` | corresponding instances, reoffer timers, first-clear receipts, aftermath |
| `accounting.gd`, `payroll.gd`, `guild_progression.gd`, `debt.gd` / §13 | `set_gold_reserve(amount)`, `allocate_payroll(employee_ids)`, `promote_guild`, `accept_loan`, `repay_debt(amount)`, `accept_rescue(person_id)`; internal receipt/accrual/closeout | `ledger_posted,payroll_due,wages_paid,morale_changed,reputation_changed,rank_promoted,debt_changed,charter_recorded` | `guild{gold,rep,morale,rank,ledger,wage_accrual,arrears,debt,sales_rep_remainder,reserve}` |
| `construction.gd` / §12.7 | `start_upgrade(upgrade_id)`, `cancel_construction` | `construction_started,construction_completed,construction_cancelled,capacity_changed` | `construction{active_job,purchased_ids,capacities}` |
| `commander.gd`, `sessions.gd` / §5a | `eat_meal(source_id,officer_id?)`, `begin_session(officer_id,template_id,job_id?)`, `finish_session(session_id,evidence)`, `encourage(person_id)`, `standing_offer` | `meal_eaten,hunger_changed,session_started,session_graded,commander_rank_changed,briefing_granted` | `commander{fed_until,skill_points,ranks,session_days,encouragement_day,standing_offer_week,briefed_today}`, active session evidence/targets |
| `bonds.gd`, `romance.gd` / §§5.4, 5b | `evening_talk(person_id)`, `choose_perk(officer_id,perk_id)`, `give_gift(person_id,item_id)`, `complete_date(date_id)`, `choose_relationship(person_id,choice)`; approved dialogue effects | `bond_points_awarded,bond_level_changed,friendship_scene_due,perk_chosen,relationship_changed` | `bonds{points,level,last_level_week,talk_day,scene_flags,perk}`, `romance{active_partner,personal_beats}` |
| `story_flags.gd` / §§14, 2.6 | `acknowledge_scene(scene_id,checkpoint_id)`, `commit_dialogue_choice(scene_id,choice_id)`, `elect_chapter_conclusion`, internal predicate evaluation | `predicate_earned,story_scene_queued,service_unlocked,chapter_changed` | `story{flags,earned_predicates,acknowledged_scenes,safe_checkpoint,pending_introductions}` |
| `projects.gd`, `journal.gd` / §§3, 7.3, 13.1, 15 | `pin_project(project_id)`, `unpin_project(project_id)`; internal event projections | `project_pin_changed,project_progress_changed,day_summary_ready` | `projects{pinned_ids}`, journal summaries/contact/history; derived counts cached only |
| `region_transfer.gd` / §16a | `prepare_transfer(destination_id)`, `commit_transfer(quote_revision)`, internal `advance_transfer`, payroll-resume | `transfer_prepared,transfer_started,transfer_checkpoint,transfer_arrived` | `transfer{phase,origin,destination,departure_tick,arrival_tick,protected_deadlines,ledger,calendar_cursor}` |
| `risk_forecast.gd` / §§8.5, 9.3 | read-only `assess(prep_snapshot)` | result only; no gameplay event | cache outside GuildState keyed by canonical prep/content hash; 100 independent fixed-seed simulations |

The Commander never enters the expedition roster. Presentation animation, minigame controls, puzzle drawing, field following and portrait staging stay outside `sim/`; only validated gameplay inputs/evidence enter it. Negotiation presentation shows the minigame, while the simulation owns actual goods, acceptance evaluation and payout; an arbitrary UI `sale_success=true` is not accepted. Visual movement sends interaction commands and supplies real elapsed time via SimHost; it does not award XP. Elsie's two named preparation templates persist formation/loadout intentions only; applying one creates a preview that reports absent people, missing items and fatigue, never substitutes someone, and still requires dispatch confirmation (GDD §15).

## 07.3 Authoritative tick and calendar pipeline

**[spec decision]** D11 Represent time as absolute 12-second ticks from day 1 00:00: 7,200 ticks/calendar day; 07:00 = tick 2,100, 20:00 = 6,000. A new operating day has 3,900 ticks. Real elapsed seconds accumulate only in SimHost at `120 * chosen_speed * battle_pace`; process whole ticks and retain the fractional remainder in app memory. Remainder is presentation pacing, not simulated progress. Load resets it and pauses.

Each tick has these immutable phases, implementing GDD §4.1:

1. **Completed combat actions.** In stable operation serial order resolve all actions whose `end_tick <= now`; secure kills, items and XP; finish atomic multi-target actions and victory before any deadline.
2. **Continuous calendar accrual for the elapsed interval.** Integrate healthy HQ HP recovery and employed-time accounting against the preceding interval's restrictions, split on timer boundaries; advance living fighter gauges/mage meter and queue newly ready actors. An injury expiring at this boundary grants no healing for the preceding injured interval. It may heal in subsequent healthy time. No new action starts yet.
3. **Timed events group A.** Due scout intervals and production/construction completions; stable entity serial within a type. For scouts: exploration, threshold guarantees, eligible find roll, XP, then injury roll. Snapshot the due scout set so a charting return cannot suppress another scout's simultaneous earned interval/injury check. **[spec decision]** D12 Where §4.1 groups different entity types together without a total order, use scouts, processing, Workshop, construction, then same-type serial. Do not start new jobs between these completions.
4. **Timed events group B.** Due operation duration/return, including immediate wounded/wiped returns. Secure all previous rewards; cancel unfinished actions. Completed final contract kill at the same tick has already succeeded.
5. **Timed events group C.** Hourly market buyers, including 20:00; processing outputs from phase 3 are available to previously authorised sales where inventory rules allow. No fabricated auto-listing command.
6. **Timed events group D.** Request/contract/debt deadlines, then queued story predicate flags. Command deliveries committed at this current boundary before a later tick retain their completion; a due auto-authorised eligible delivery resolves before expiry, never silently completes a client visit requirement.
7. **Cutoff.** If 20:00, close operations; abort unfinished production/enhancement/Reworking with full input/fee return; retain queue intent and corpse roll identity; resolve rest and daily causes, open Resolution then Day Summary, with explicit payroll step on day 7 multiples. Do not begin work/action/search/dispatch at this boundary. Mark closeout once.
8. **Starts only while operating and before cutoff/return.** Queue starts, search completions starting encounters, next searches and ready combat actions. Revalidate state after all earlier phases. **[spec decision]** D13 A search which completes at the operation's end cannot begin a fight; no damage can be manufactured at expiry. Record newly started search/job/action endpoints rounded upward to ticks.

Tick phases are functions called by `tick_pipeline.gd`, never Godot signal connection order. Most phases are no-ops at night/transfer. Clock speed (Pause/1×/2×/4×) and one foreground modal token belong to SimHost/Game; dialogues, shops and management save/restore chosen speed, watching preserves Pause, scouting watch never applies battle pace. Watching battle optionally multiplies global wall-to-Guild-time rate by ¼. Running the same tick sequence with different rendering cannot alter event history.

Night elapsed time uses the same calendar scheduler and cursor, from 20:00 through 07:00; personal evening walking and the sleep jump divide, rather than duplicate, those 11 hours. Sleep allowed after 20:00, automatic at 01:00 with no penalty; award employed adventurer +1 stamina only at the next 07:00 boundary. Process injuries, construction, request/debt deadlines and payroll boundaries in chronological order; no buyers, expedition intervals or production. Day starts paused. Pending difficulty applies at 07:00 to future injuries/deadlines/wages only. Relaxed sets new injury duration to 24 h, future wages×.75 and newly created timed request/optional deadlines×2; unchanged existing timers, loot, combat and demand.

## 07.4 System-specific transaction invariants

**Operations, combat and scouting.** Dispatch rechecks employment, HP>0, stamina>0, injury, rest/enhancement/event locks, formation, gear and reservations; debit stamina and consume chosen lure/map atomically. Red Fatigue is evaluated **after** debit (≤1), never an extra primary state. A rare sighting is exclusively reserved; hunt ending consumes it regardless of result. Each completed rare search rolls .70 until encounter; after encounter no second rare or variant conversion. Hunt/search/group/variant probabilities and progression follow GDD §§7–10. No deployment XP on departure; grant 10 once at first completed hunt fight/scout interval. Contract kill/win XP applies, but the GDD's deployment award is hunt/scout only. Return reputation is +1 per secured hunt/contract corpse or +2 once for any completed scout interval. Receipt keys prevent repeated settlement.

Combat snapshots permanent stats, equipment, row and post-debit fatigue per **fight**, while temporary statuses/target-specific Elite bonuses remain dynamic. Gauge progress persists through dynamic interval changes. Readiness tie order: front slots, back slots, enemies; one active action per encounter. Start decides skill consumption and valid targets; completion applies damage/downing, surviving retaliation, surviving potion, meter/status application, then aging of pre-existing recipient effects. No meter per cosmetic hit; no recursive retaliation. Stun consumes 12 s, no meter spending; normal/skill 24/72 s. Monster skills use attacker meter; fourth completed normal attack fills it, next eligible action uses skill. Interrupted actions have no damage and refund no already-consumed skill meter. Completed kills survive recall/wipe/cutoff. Midfight saves resume, not restart.

Scouting threshold guarantees precede random finds, and rewards precede risk; den benefits never bypass species identification. At 100%, other already-due intervals still finish, unique finds remain unique. Hints have no XP. Repeat surveys add no exploration but retain interval/find/injury rules. Risk preview uses `1-product(1-p_i)`, not summed percentages. Prep combat risk runs 100 complete fixed-seed simulations with the exact prospective duration/loadout/formation/skills and classifies <5% / [5%,25%) / ≥25% any-down as Low/Moderate/High. These seeds and cache never advance campaign RNG.

**Production.** Processing order ≤30 corpses; Workshop order ≤20 mixed craft/enhance/Rework jobs. Choose highest rank, then productive hours, then **[spec decision]** D14 stable worker ID as final tie. A worker serves one station/job; Mae/Fulker each cover at most one vacant baseline service at fallback×2; they never double-work an occupied station. Keep valid work moving; an unavailable waiting job stays visibly blocked and does not consume another job's materials. **[spec decision]** D15 Scan order for the first runnable job when the head lacks inputs/eligible worker; preserve relative order of remaining jobs and explain the blocker. This realizes the no-idle requirement without creating stock.

Processing queue commit binds a corpse ID and first committed processor-rank snapshot used for its sticky roll, distinct from actual duration worker snapshot. **[spec decision]** D16 Persist `{quality_u,rare_u,first_rank,quality_outcome,rare_outcome,modifier_provenance}` once for that corpse; later worker reassignment/cancel/reload/cutoff never draws again. Queue preview makes the first rank binding visible before commit. The later Cutting Chart bonus must use the same `quality_u` under the approved odds contract (source conflict §06.7), never another draw. This permits a traceable modifier without pretending the source has already resolved reclassification. An existing better result must not be silently discarded by reopening a session. Release is blocked on the exact approved interaction, not allowed to pick a random interpretation.

Workshop waiting jobs hold intentions only per §12.2a; on start reserve actual available Standard+ lots and fee, then atomic completion consumes escrow and creates exactly one result. Reworking uses one material ID at exact input qualities; no Unsellable, no mixing identities, no output quality roll. Enhance targets the **person**, sequentially, with rest/dispatch exclusion and any-quality elite input at levels 4–5. Cancel/cutoff returns every input and fee, zero partial output; preserve recipe intent, no banked time overnight. Productive hours credit only completed jobs, actual operating ticks; forecast service credits one hour/day, not category count. 07:00 resume revalidates all claims. Processing/crafting timing modifiers and session bonuses use start snapshot or the specifically authorised targeted session adjustment, not live incidental morale/promotions.

**Commerce/information.** One persisted three-day demand schedule per base/category, extended at 07:00. One buyer per category per whole hour 08–20; cheapest eligible listing, then oldest/serial, at most quota 1/2/3. Fees per filled listing `max(1,ceil(gross*.05))`; no extra quota by splitting. Willingness uses material base×quality×demand plus explicit applicable Commander/perk modifiers. Sold lots cannot also satisfy requests. Any-trader accepts old-region stock with the GDD half-reference/material-only/actual-cost rules and Premium Seller prohibition; no visit window or stock limit. Sales Rep retains net-receipt remainder, excludes requests/loans/refunds; debt sweeps occur after the sale fee. Save actual consumable purchase cost. Forecast once delivered is fixed per category/day, even after promotions/reassignment; prediction errors choose another state uniformly. Never reroll hidden truth on reopening. A morning order samples only compatible unreserved active-base storage, ≤owned quantity; no eligible stock means no order. It expires at 20:00, no listing fee. Starting a session locks explicit stock claims; additional-unit tactics cannot consume reserved or nonexistent goods. Before session start, changed stock revalidates the existing order without a new random buyer/order roll.

**Payroll, Morale, debt.** Wages accrue applicable rate/7 once for every employed calendar day whose cutoff includes employment, with future-only rank/difficulty/perk changes; retain exact fractional accrual and ceil once per employee at payday. Payroll allocation pays full employee balances; unpaid staff return crafted gear/backpack, retain arrears/stats/XP/stamina/injury and become Left. No absence stamina recovery, no officer wages/departure. Rehire = original hire+arrears plus capacity check. Daily Morale sums causes then clamps once; payroll separate explicit causes. Reputation floor zero, promotions spend Gold only and never demote after losses. Emergency loan eligibility distinguishes unrecoverable staffing from merely resting/injured workers; cancel optional purchase reservations before shortfall. Rescue advance pays rehire directly, adds principal, once per later unpaid-payroll incident. Overdue sweep stores fractional remainder, takes 25% positive eligible receipts capped by principal; no interest or game over. Charter flag is once-only C+Crownstone+zero debt and persists after later debt.

**Commander/bonds/story.** Meal makes Fed for 8 h; Hungry only disables running (walk 3.2/run 5.6 m/s), no expedition modifier. HQ kitchen free; tavern 8G/stall 5G. Session once/officer/day during operations with work available; validated completion awards the stated grade points and advances exactly one Guild hour through the ordinary pipeline. **[spec decision]** D17 Require one operating hour remaining before session start (latest 19:00) so completion cannot extend operations past 20:00 or invent a shortened session; a target job finishing within that hour must receive any earned targeted modifier before its completion is resolved. Presentation sends evidence; registered solver/grade evaluator recomputes grade, caps hint use at A and commits exactly once. Skill caps obey content origin (Eurydica ≤2); difficulty cannot substitute for Frontier sessions. Working-session progress and its pause checkpoint persist. Meals with officers count as a bond talk; don't double-credit the same meal and talk event. Weekly one-level gate, personal-beat Bond-5 gate, permanent one-of-two perks, no invented numeric bond gains. Romance is authored Frontier NPC-only, one active romance, Bond-4 personal-beat gate, no stats. Story predicates are earned immediately but introductions play at safe paused interactions; chapter transition is elected, not automatic at a date.

**Transfer.** Readiness quote identifies all cleanup/refunds and payroll dates; commit requires same revision and GDD §16a conditions (transition beat, charter, no debt, 1,500G, no active expedition/construction). Refund unfinished production and cancel listings atomically before departure. Advance exactly 48 calendar hours, retain arrival clock time and paused state. Freeze **accepted timed deliveries only** with exact remaining ticks; optional combat contracts and unaccepted offers continue deadlines, injury/debt/construction calendar rules persist as applicable. No local operations/production/buyers/new local repeats. Pay/accrue crossed payroll days exactly once, pause travel for allocation as needed; credit two crossed sleep boundaries to employed adventurers, no rest-day bonus or synthetic daily-success Morale. Preserve all staff/former staff, progress, stock, requests, contacts, flags and purchased capacity. Restore protected deadlines on arrival, suspend origin repeat waits. Surveyed route flag requires discovered path and successful hunt return on selected route; verification never doubles the path's −5-minute effect.

**Frontier readiness:** every module reads definitions and region-scoped state, not hard-coded chapter content. Existing commands, transactions, timers and effects support the specified Frontier extensions, with inactive-base history retained and no autonomous second HQ.

---

# 08. Saves, RNG and migration


## 08.1 Save envelope and exact payload

GDD §16b requires three profiles, unlimited named manual saves and three rotating autosaves/profile. **[spec decision]** D18 Use a distinct namespace, never the playground's save directory:

```text
user://fgc/profiles/profile_1/          # also profile_2, profile_3
  index.json                           # rebuildable display-name/slot index
  manual/<slot_id>.json                 # monotonic save_<serial>, display name inside
  auto/auto_0.json, auto_1.json, auto_2.json
  *.json.tmp, *.json.bak                # sibling temporary and last-good backup
```

User names never become paths. `slot_id` is validated with a fixed safe pattern; names can be Unicode. Saves are not limited by the legacy 48-character user label/path rule or a legacy fixed slot count. No active campaign is overwritten merely by selecting a profile. Index corruption is repairable by scanning verified slot headers. Autosave next-slot cursor advances only after successful replacement; use saved sequence numbers to reconstruct it if the index update crashes.

```json
{
  "format":"fgc_guild_save",
  "version":1,
  "content_revision":"<manifest SHA-256>",
  "checksum":"<SHA-256 of canonical payload>",
  "payload":{
    "version":1,
    "content_revision":"<same manifest SHA-256>",
    "profile_id":"profile_1",
    "slot_id":"save_1",
    "display_name":"Before the Chimera",
    "save_sequence":1,
    "rng_algorithm":"sha256_counter_v1",
    "campaign_seed":"<64 lowercase hex digits>",
    "state":{},
    "scene_checkpoint":{"scene_id":null,"checkpoint_id":null},
    "content_bindings":[]
  }
}
```

This is an envelope illustration, **not a valid empty GuildState**. `state` serializes every aggregate in §07.1. `content_bindings` lists `{record_type,id,rev}` for referenced definitions; active operations/jobs also store exact dispatch/start rule snapshots required to continue under that revision. Header version/revision must equal payload version/revision so checksum covers compatibility metadata. Save sequence is monotonic per profile; wall-clock display timestamps, if added, are metadata only and never advance simulation.

Persist clock/night/closeout credits and pending difficulty; operation streams, search endpoints, fighters/gauges/queue/inflight/target/meter/status and snapshot stats; sticky corpse quality/rare results and variates; discovery and rare ownership; all lot/item identities and exclusive reservations; production intentions, active escrows, fees and duration factors; listings/demand/check cursors/forecasts; construction; wages and per-day accrual receipts, arrears, debt/remainder; lifetime/spendable XP, rest and dispatch days; request first appearances, deadlines, gel alternatives, recurrence waits; scene checkpoint and once-only rewards/flags/pins; Commander hunger/session state; bond and perk choices; transfer phase/cursor/protected remainders. Save only between complete transactions; never halfway through a multi-target action or payout.

Saving is allowed in combat, world and management, and at transfer payroll checkpoints. Authored cutscenes save the current **safe scene checkpoint** per §09; never serialize arbitrary tween time as story progress. Resume paused with zero offline progression and preserved in-flight action endpoint. Do not copy SMC's unfinished-duel reset policy.

## 08.2 Canonical JSON and write/recovery protocol

Port the **pattern** from `company_state.gd:713–852`, not schema-5 validation. **[spec decision]** D19 Canonicalization version `godot_json_roundtrip_v1` is:

```gdscript
var normalized: Variant = JSON.parse_string(JSON.stringify(payload, "", true, true))
var canonical: String = JSON.stringify(normalized, "", true, true)
var checksum: String = canonical.sha256_text()
```

Recursively sorted object keys, unchanged array order, UTF-8, no insignificant whitespace, finite valid JSON only. Use the same locked Godot serializer on write/read; golden bytes cover Unicode and integer/float round trips. Integers that may exceed JSON's exact 53-bit range (RNG counters/seeds) serialize as validated decimal/hex **strings**. The SHA-256 is corruption detection, not authenticity or encryption. Reject duplicate keys before dictionary conversion. Version the canonicalizer if engine serialization changes; do not “fix” old checksums using new formatting before verification.

`app/saves.gd` serializes saves on one writer queue. `sim/save_codec.gd` (pure encode/decode/validation) returns a detached payload; the I/O service never shares a live mutable state dictionary.

1. Snapshot a settled transaction boundary; validate full payload/reference/escrow invariants before writing.
2. Serialize to sibling `.tmp`; flush and close; check write error. Reopen, parse, verify checksum/header/schema and semantic state using the same loader. Failure leaves current slot and backup unchanged.
3. If existing slot validates, copy it to `.bak.tmp`, flush/close/read-verify, then atomically replace `.bak`. Never replace a good backup with corrupt main bytes. If backup preservation fails, abort the new save without replacing main.
4. Atomically replace final with verified `.tmp` **on the same filesystem**. Test the target platform's overwrite semantics. Do not remove the only good main first. **[spec decision]** D20 Hide replacement behind `AtomicFileStore.replace_verified`; use Godot rename only where it demonstrably provides atomic replacement, otherwise a platform adapter implementing replace semantics is required. An unsupported atomic replace returns an error and retains the previous slot; no delete-then-rename fallback masquerades as atomic.
5. Report success, then update the rebuildable index/cursor by the same protocol. Keep `.bak` as previous validated save. On disk-full/readback/rename failure report the actual failed stage; no successful-save toast.

Load checks main without mutating memory. If missing/corrupt, verify `.bak` and offer/load recovery with a clear notice; do not silently save recovered state over evidence. `.tmp` is never automatically promoted. Future-version or incompatible-content main is an incompatibility result, not corruption: do not silently fall back to older gameplay to hide it. If neither main nor backup is usable, retain current session and show diagnostics. A failure loading one profile never loads another. Memory swaps only after checksum, migration and semantic validation succeed. Resource limits for parser depth/size are implementation guards, configurable/tested for expected long campaigns; the old 8 MB cap is not a game rule.

## 08.3 Autosave barriers

Save at: **new day**, **before payroll**, **before flashpoint dispatch**, **before and after chapter transition**, **before and after relocation** (GDD §16b). Store a transaction marker with the before checkpoint so loading it does not replay already committed after-state. **[spec decision]** D21 Barrier-triggered actions wait for the pre-save result; on failure retain the pre-action state and report a retryable save error. A post-save failure leaves the already committed in-memory outcome intact and visibly unsaved; retry saving, never reapply effects. Manual save remains available. Transfer has before-departure and after-arrival barriers, plus ordinary payroll checkpoint saving. Transition triggers coalesce only when they refer to the same exact pre/post state; no lost before/after checkpoint due to event ordering.

## 08.4 Stable RNG streams

**[spec decision]** D22 Use a project-owned deterministic counter generator in `sim/seeded_rng.gd`, algorithm `sha256_counter_v1`, avoiding engine-dependent `String.hash()`, wall time and global `randf()`. This is an implementation choice; GDD specifies stable ownership, not a generator algorithm.

```text
LP(s) = ASCII decimal UTF-8 byte length of s + ':' + UTF-8(s)
stream_seed_bytes = SHA256( LP('fgc_rng_v1') || LP(campaign_seed_hex)
                           || LP(domain) || LP(owner_id) || LP(purpose) )
block(k) = SHA256( stream_seed_bytes || uint64_big_endian(k) )
u32 = first four bytes of block(k), unsigned big-endian; increment k
uniform01 = u32 / 4294967296.0
```

Counter starts zero; persist as an unsigned decimal string. Reject overflow rather than wrap/reseed. Integer uniform `[0,n)` uses rejection: `limit=floor(2^32/n)*n`; discard values `>=limit`, then `%n`. Bernoulli consumes one uniform draw (`u<p`); weighted choices use integer weights, normalized exactly from authored decimals (e.g. 1.5→3 when scale=2), rejection-sampled into cumulative intervals in stable content ID order. Do not depend on dictionary iteration order. No test or presentation access can mutate a gameplay counter.

| Domain / owner / purpose | Consumption and persistence |
|---|---|
| `operation / op_<serial> / encounter` | Search target, group rolls and member variants in stable slot order; reserved rare rule uses this stream. Persist seed and counter with operation. |
| `operation / op_<serial> / combat` | Only authored randomness such as Tristitia's living-ally buff; no random damage added to the GDD formula. |
| `operation / op_<serial> / scout_find`, `scout_risk` | Independent find and risk streams; per completed interval, not rendered frame. Preserve progress/draw cursor mid-operation. |
| `corpse / corpse_<serial> / yield` | First queue commit's quality and rare variates once; persist results even after cancel/cutoff. Deterministic guaranteed outputs do not make extra rare rolls. |
| `day / <base_id>:<day>:<category_id> / demand` | Three-day demand truth generated only for missing days/categories; persisted values remain authoritative. |
| `day / <base_id>:<day>:<category_id>:<hour> / buyer` | One hourly buyer check with persisted processed key; changing listing count doesn't add draws. |
| `generator / <base_id>:<day>:<generator_id>:<instance_serial> / generate` | Negotiation orders, rumours/leads, session templates and Standing offers use distinct generator IDs and stable persisted outputs. |
| `generator / <base_id>:<target_day>:<category_id> / forecast` | First delivered forecast plus recorded confidence; promotion/reopening never creates another draw. |
| `preview / <prep_hash>:<trial_index> / risk` | Separate fixed root seed and copied state; 100 simulations; never serialize preview counters into campaign RNG. |

Fresh campaign entropy is obtained once by the app and saved as `campaign_seed`; it is the only nondeterministic gameplay initialization. Operation serial allocation is monotonic, unaffected by watching. Retries/new operations get their own committed serials; rejected commands do not allocate or consume streams. Saves store algorithm version, root seed, stream owner/seed/counter and already-generated outputs; seed alone is insufficient for mid-operation resume. Cosmetic randomness stays outside `sim/` and is excluded from state hashes.

## 08.5 Versioning and migration

**[spec decision]** D23 Start new format at schema 1; migration modules `sim/migrations/v001_to_v002.gd`, etc. implement `migrate(source: Dictionary) -> MigrationResult` on a deep copy. Each step declares source/target schema, content compatibility and exact ID aliases, and returns notices/changed paths. Check old checksum **before** migration, validate old shape, run contiguous steps, then validate the new state and references. Missing migration or unsupported future version rejects load without changing disk or memory.

Content revision differs from schema. Equal schema is not automatically compatible: changed/deleted IDs or mechanics require a declared content migration; harmless text/art changes can explicitly declare compatibility. Active-operation rule snapshots and frozen generated outcomes survive compatible content updates; no retroactive new rewards, progress, offers, free XP or time advancement on load. Maintain immutable old save and backup until a separately successful new save. Migration is idempotent under retry and never repeatedly applies an alias, grant or refund.

Reservation repair (GDD §16b): compare authoritative owned/escrowed quantities and owner existence. Orphaned claims release held owned goods; escrowed goods/fees are returned **once** with a receipt and notice. Never mint claimed stock that never existed; unreconcilable quantities reject recovery rather than delete or fabricate assets. Missing definition IDs require explicit aliases or recovery policy, not guessed substitutes. Preserve original IDs/provenance where necessary, including legacy dialogue tokens.

The old `imc-playground` format/schema 1–5 is **not** this format. Port checksum/transaction/error-test techniques but do not promise legacy campaigns load. An explicit legacy importer would need separate approved mappings for obsolete combat, inventory, wages and story; absent that importer, detect format mismatch and retain the file unchanged. This prevents “migration” from importing retired game rules.

**Frontier readiness:** the payload stores bases, people, region content revisions and clocks by stable ID; transfers and future content migrations preserve identity, claims, liabilities and RNG positions. No save reset is tied to entering Chapter 3.

---

# 09. Scene script runtime

## 09.1 The converter (`tools/scene_convert.gd`)
- **Input:** `Manuscript/<Chapter>/*.md`, read from the storyboard repo path set in `tools/paths.json`.
- **Output:** `content/scenes/<chapter_id>/<scene_id>.json`.
- **Run:** `godot --headless --path . --script res://tools/scene_convert.gd -- <chapter>`. The converter is deterministic: the same input gives the same output bytes.
- **Grammar** (from `Scene Script Format.md`):

| Source | Node type | Fields |
|---|---|---|
| `Speaker (Expr):` + `"text"` | `line` | `speaker`, `expr` (inherited if omitted), `text` |
| `{text}` under a speaker | `thought` | `speaker`, `text` |
| `> text` | `narration` | `text` |
| `[cue: args]` | `cue` | `cue`, `args[]` |
| `N. **[Label]** {tags}` + nested nodes | `choice` | `options[{label, tags[], nodes[]}]` |
| `[if: cond]` … `[else]` … `[end if]` | `branch` | `cond`, `then[]`, `else[]` |
| `## Talk: Name` / `## Bark: Name` / `## Ambient: Name` | `talk` / `bark` / `ambient` | `where`, `when`, `trigger`, `nodes[]` |
| `\|note\|` | dropped | Kept in `notes[]` for the report only |

- A scene file's header (`Location`, `Time`, `Actors`, `Music`, `Staging`, `Special poses`) becomes the scene record's `setup`.

## 09.2 Lint rules (the converter fails on any)
1. An expression not in that speaker's portrait set (officers and the Commander: 8 incl. Base; buyers: 8 negotiation + Dietrich's Bluff). Characters without a portrait set may carry expressions, which are ignored, and produce a **warning**.
2. An unknown cue or wrong argument count (the cue table in the format doc is the whitelist).
3. A marker in `Staging:`, `move`, `enter`, `exit` or `pan` that isn't in `markers.md` for the scene's location.
4. A `pose` not listed in the header's `Special poses` (except `idle`).
5. An unknown tag, request ID, skill name, flag name or game-state condition. Flags are declared in `content/common/flags.json`; conditions are a fixed list defined in §07.
6. A quoted line with no speaker in scope; a narration line (`>`) with a speaker; a `{thought}` outside a speaker block.
7. `{after: X}` naming a topic that doesn't exist in the same talk.
8. The report lists every writer note, so staging notes that still need a cue are visible.

## 09.3 The runtime (`presentation/dialogue/scene_player.gd`)
- `ScenePlayer.play(scene_id)` walks the node list:
  - **`line`, `thought`, `narration`** show the dialogue view (§12.4) and wait for advance input. The typewriter reveal is skippable.
  - **`cue`** nodes in a row start together; each returns when done or immediately.
  - Camera cues go to `CameraRig` (§10.2); sprite cues go to the actor (§10.4); `shake` and `fade` go to the post and UI layers; `sfx` and `music` go to `Audio`.
  - **`choice`** shows the options, runs the chosen option's nodes, and sends its tags as sim commands: `grant_skill_points`, `add_bond`, `set_flag`, `unlock_request`.
  - **`branch`** evaluates conditions through `SimHost.query_condition(name)`.
- **Talks:**
  - Opening an NPC runs its talk node.
  - `{topic}` options loop back to the menu, with an automatic **[Leave]**.
  - `{after:}` hides locked topics.
  - Heard topics are stored in the sim as flags `heard:<talk>:<label>`, so they survive saves.
- **Barks:** proximity areas on the NPC play a bark once per day, as a world-space speech bubble (no portrait, no pause).
- **Ambient lines:** the NPC is spawned only when its `when:` matches the time band (Morning 07–11, Day 11–17, Evening 17–20, Night 20–01) [spec decision]. Its `[if: done: …]` variant is chosen at interaction.
- **Placeholders:** `<name>` and `<Guild-name>` are filled in from the sim at display time.
- **Portraits:** the Commander is on the left and the current speaker on the right. A speaker with no portrait set shows the name plate only (GDD, owner 2026-09-28).
- **Saving mid-scene:** scenes checkpoint at scene start and at each choice. A save restores to the last checkpoint (GDD 16b).

---

# 10. HD-2D presentation

Each number below comes from proof 4 (`town.html`) and GDD 2 / proof 4 results unless marked.

## 10.1 World scenes
- `scenes/worlds/eurydica_town.tscn` is the Chapter 1 slice first, then the full south bank per `Locations/Eurydica/` (layout corrections from the GDD audit apply: lodging east of the spine, the clinic and food shop placed per the plan).
- The HQ (`hq_tier1.tscn`) and interiors are separate scenes, linked by door markers.
- **Coordinates:** 1 unit = 1 m; +x east, +z south. The camera looks north.
- **Markers:** `Marker3D` nodes named exactly as in `markers.md`, grouped under `Markers/`.

## 10.2 CameraRig (`presentation/camera/camera_rig.gd`)
- **Exploration:** perspective, **FOV 30°**, offset **(0, 18.4, 21.8)** from the followed actor (about 40° down), straight-north heading, eased follow (lerp 0.12 per 60 Hz frame, made frame-rate independent). Near 0.5, far 200.
- **Dialogue shots (GDD 2.6):**

| Shot | Behaviour |
|---|---|
| `shared` | Frames all scene actors: target = actor centroid; the distance is solved so every actor fits within 70% of the frame height; pitch eases from 40° to **30°** |
| `push-in X` | Target X at 30° pitch, at 55% of the exploration distance |
| `two-shot A B` | Frames both at 30° pitch, with 15% side padding |
| `gaze X` | Pans to a point 4 m along X's facing, at X's eye height |
| `pan M` | Pans to marker M |
| `turn a` | Yaw by `a` (±30° max); sprites and props re-face (10.4) |
| `return` | Back to `shared` |

- Every shot eases over 0.6 s (sine in-out). `hold t` waits. Letterbox is a UI overlay (§12).
- **Field view:** the camera is set by the field stage (§11).

## 10.3 Post stack (`presentation/post/`)
- **Tilt-shift depth of field:** a full-screen post shader on a camera-attached quad (`tilt_shift.gdshader`, `hint_screen_texture` + `hint_depth_texture`), ported from the proof's DoF shader:
  - focus distance = the camera-to-target distance;
  - range 16 m;
  - maximum blur radius 4 px;
  - tilt band from `smoothstep(0.30, 0.55, |uv.y − 0.47|)`.

  [spec decision] The engine's `CameraAttributesPractical` DoF stays off.
- **Bloom:** `Environment` glow, intensity 0.25, bloom threshold 0.9 (proof 4: UnrealBloom strength 0.25, threshold 0.9).
- **Grade:** ACES tone mapping at exposure 1.08, plus a colour-correction LUT built from the proof's grade (shadows toward cool, highlights toward warm, vignette 0.9). The LUT is generated once by `tools/make_grade_lut.gd`.
- **Sun:** a DirectionalLight3D from the upper left of the screen (north-west), soft shadows, shadow distance 60 m, following the camera.

## 10.4 SpriteActor (`presentation/actors/sprite_actor.gd`)
- **The node:** a `Sprite3D` (not billboarded by the engine). `pixel_size = 1.68/93`, texture filter **nearest**, `alpha_cut = discard` (so it casts shadows), shaded, with a 0.12 emissive lift like the proof.
- **Orientation:** yaw = the camera heading; tilt = −0.6 × the camera pitch, so the sprite leans toward the camera.
- **The atlas:**
  - rows are down, left, right, up; idle is columns 0–3 and walk columns 4–13; frame rate from the atlas JSON;
  - a direction comes from screen-relative movement;
  - the right-facing walk is the mirrored left walk where the atlas lacks it.
- **Other parts:**
  - a contact shadow blob: a circle of radius 0.36, 28% black, flattened to half height;
  - special poses: separate textures keyed `<actor>_<pose>`; a missing pose falls back to idle and logs a warning;
  - emotes: a small billboard above the head (the 11 icons, GDD format §5).
- **Movement:** walk 3.2 m/s, run 5.6 m/s (disabled while Hungry). Collision is a CharacterBody3D capsule (radius 0.3) on the world's static colliders.

## 10.5 Buildings (`presentation/world/building_3d.gd`, a `@tool` node)
- **Exported:** `facade_id` (for example `tavern`, `house_green`), a footprint (x0, z0, x1, z1), `door_face`, an optional wall height `H`, `awning`, `chimney`.
- **Generation**, in the editor and at runtime (the hd2d-buildings reference):
  - a core box and four facade quads, 2 cm proud, with alpha scissor plus a matching shadow material;
  - generic facades rotate with the door face, and the ridge swaps on a 90° turn;
  - the gable height is `G = min(5, 0.55 × span)`, using the curve `y = H + G(1−u)^1.4`;
  - the roof is a generated ArrayMesh: two curved slopes, 0.45 m overhang, flared eaves (+0.2 m), UVs in 8 m units, and a ridge cap;
  - the gatehouse has piers, a lintel and a vault, leaving an open passage.
- **Collision:** a StaticBody3D box per footprint (the gatehouse piers only).
- **Textures:** from `assets/facades/<id>/<face>.webp` (§10.8). A missing face uses a flat plaster colour and logs a warning.

## 10.6 Cutaway
Every 0.1 s, rays run from the camera to the Commander and to every actor within 9 m, at four heights (0.3, 1.0 ±0.3 m, 1.6 m). Every mesh of a building hit by a ray fades as a group to **22%** opacity, using an alpha material override with a depth pre-pass. It is restored when no longer hit. The fade eases over 0.25 s. [spec decision]

## 10.7 Time of day
The sun colour and intensity follow four bands (Morning / Day / Evening / Night) keyed to the clock. The night uses a cool moonlight and lamp OmniLights on the painted lamp posts, which are unlit in the paint. NPC schedules use the same bands (§09.3).

## 10.8 Assets and sync
- `tools/sync_assets.gd` copies **approved sources only**, listed in `tools/asset_manifest.json`, from the storyboard repo into `res://assets/`:
  - sprite atlases;
  - portraits;
  - monster stills;
  - facades, roof and wall tiles, attachments, props;
  - the Hylaea set;
  - fonts.
- Painted art is converted to lossless WebP with alpha. Pixel sprites stay PNG.
- The manifest records each file's source path and SHA-256. The sync refuses a source under `D:/Codex/IMC` (candidates never ship).

---

# 11. Field and battle view (`presentation/field/`)

- **The stage:** the painted Hylaea layers (GDD 2.4), set up as in the operations proof:
  - far strip 26 m back, mid strip 13 m;
  - ground tile 6.3 m;
  - a 48 m repeating layout;
  - near trunks scrolling at parallax factor 24, gliding to the edges when a fight starts;
  - the fighting band z −2.8…2.8 kept empty.

  Other regions use the same stage with their own set, chosen by `region.field_set` (§06).
- **The search walk:** the party walks right while the layers scroll. Walk speed is tied to the operation's search progress from events, never its own timer.
- **Battle presentation (proof 2):**
  - monsters stand on the left facing right; the party is on the right, facing left;
  - **party formation layout** *(owner correction, 2026-09-28)*: the front row stands nearer the enemies, the back row behind it to the right. Within each row, members further up the screen (further from the camera) are shifted **left**, so each row runs diagonally from bottom-right to top-left. Then no fighter is hidden behind the one below it, and the two rows never interleave. Proof 3 had it the other way (`ops.html`: `COLZ = [.1, -1.5, 1.7]`, `COLX = [0, .9, -.5]`, rows at x 2.0 and 3.7), which made five-member parties look disorderly. Use `COLX = [0, -.9, .5]` with the same `COLZ` and row x, or equivalent spacing: each step up the screen moves about one sprite width sideways. Enemy groups mirror the rule (further up = shifted right);
  - an action plays as wind-up, move, impact, return;
  - hit-stop is **0.13 s** normal and **0.26 s** big;
  - a white flash on the target sprite only (1–2 frames), a hit spark, a decaying directional shake, a damage-number pop;
  - skills play the push-in, vignette and banner for the whole skill.

  Monster poses switch between still sprites (GDD 2.2); the engine adds breathing, lunge, flinch and dissolve.
- **Timing:** presentation timing never feeds back into the sim. The field view **plays events** at the battle-pace rate (§05), and if it falls behind it compresses animations; it never delays sim ticks. [spec decision]
- **The HUD:** the party card column on the right (GDD 9.4 as changed 2026-09-28; FGC_08 §5.7): bust with the gold attack-readiness ring, HP, the orange skill meter, statuses; enemy HP bars at the top centre; the battle log bottom left.

---

# 12. UI architecture (`presentation/ui/`)

## 12.1 Theme
- A single `ui_theme.tres` built from GDD 2.5 tokens (the navy, gold, parchment, ink and status colours).
- Fonts: Marcellus for headings, Alegreya Sans for text and **all numbers** (lining figures), Pixelify Sans only for in-battle names.
- Colours are referenced by token name in code (`UiTokens.GOLD_500`), never as hex. [spec decision]

## 12.2 Layers (CanvasLayers)
| Layer | Contents |
|---|---|
| 0 | World (3D) |
| 10 | World-space labels: name tags, the talk prompt, barks, emotes |
| 20 | HUD: top bar (GDD 15), objective, alerts, minimap |
| 30 | Screens and overlays (management screens, shop, minigames) |
| 40 | Dialogue view |
| 50 | Letterbox and fades |
| 90 | Debug (dev builds only) |

## 12.3 Screens
One scene per GDD 15 screen, in `scenes/ui/`. Each screen binds to read-only sim state and sends commands. Screens own **no** rules: a button that can't act shows the sim's refusal message.

## 12.4 Dialogue view
Ported from proof 4:
- the Commander portrait on the left, the speaker on the right; a non-speaker is dimmed to 55% brightness;
- the name plate and a 140 px text box;
- options as buttons;
- narration in a centred box with no name plate; thoughts in italics in parentheses;
- speakers with no portrait set get the name plate only.

The text box never covers the minimap: the minimap hides while the dialogue view is open.

---

# 13. Input

| Action (`InputMap`) | Keyboard / mouse | Gamepad (mapped, polished later) |
|---|---|---|
| `move` | WASD / arrows; click the ground to walk | Left stick |
| `run` | Hold Shift | Hold B |
| `interact` / `advance` | E, Space, Enter; left click | A |
| `cancel` | Esc; right click | B |
| `speed_pause` / `speed_1` / `speed_2` / `speed_4` | P / 1 / 2 / 4 | D-pad |
| `open_ongoing` | Tab | Y |

- Movement is **screen-relative** and rotated by the camera heading.
- Input never reaches `sim/`. Presentation turns it into commands.

---

# 14. Minigame framework (`presentation/minigames/`)

- **The contract:** `MinigameSession.start(template: Dictionary, context: Dictionary) -> void`, signalling `finished(result: Dictionary)`.
  - `result = {grade: "D|C|B|A|S", hint_used: bool, outputs: {...}}`.
  - `SimHost` receives `session_result` and applies the GDD 5a rules: skill points by grade, 1 Guild hour, bond points, outputs.
- **Session rules:**
  - The clock is paused while a session is open (overlay state).
  - Once per officer per day, enforced by the sim.
  - A hint caps the grade at A.
- **Content:** templates in `content/minigames/<kind>/*.json` (§06), with randomised details seeded from the day's session stream (§08).
- **Grading:** each minigame computes its own best result for the S threshold (GDD 5a.2a), such as the solver route or the maximum ceiling.
- **The five sessions:** `expedition_planning`, `counter_offer`, `cross_check`, `cutting_chart`, `fitting`. They are built in M3 or later; M1–M2 only need the framework and one stub.

---

# 15. Audio

- **Buses:** Master, Music, SFX, UI, Voice (unused for now).
- `Audio.play_music(id)` crossfades over 1.5 s; `Audio.sfx(id)`. IDs map to files in `content/common/audio.json`.
- Script cues `[music:]` and `[sfx:]` call these. A missing ID logs a warning and plays nothing.
- Location music is set from the location record and the time band.

---

# 16. Testing


## 16.1 Runner and fixtures

**[spec decision]** D24 `tests/run_all.gd extends SceneTree` discovers `test_*.gd` recursively under `tests/{unit,sim,content,saves,integration}` in sorted path order, instantiates typed test suites, invokes sorted `test_*` methods, awaits declared async tests and reports every failure. A parse/load error, missing expected suite, uncaught script error, timeout, or zero discovered tests is failure, not a skipped pass. No test addon required. Emit `PASS/FAIL <path>::<method>` and a machine-readable JSON summary; exit 0 only when all required cases pass, otherwise 1 (2 for runner invocation error). A suite manifest records required families so accidentally deleting a suite cannot turn CI green.

Fixtures in `tests/fixtures/`: `guild_new`, `two_hunters`, `scout_thresholds`, `cutoff_collisions`, `market_three_listings`, `payroll_partial_week`, `transfer_payday`, `request_safeguards`, `corpse_rolls`, `active_combat`, `legacy_bad_envelopes`, `incomplete_content`. Fixtures construct state using validated builders; malformed-save/content fixtures intentionally bypass builders. Each fixture records `content_revision,seed,commands,expected_events,expected_state`. Golden outputs are independently calculated from GDD, never regenerated from the implementation under test as part of ordinary tests. Test names use `test_<system>_<boundary>_<expected_behavior>`.

Save tests use an injected FileStore and isolated `user://test_saves/<run_id>/`; never campaign/profile paths. Enumerate and verify cleanup targets inside that test root. Sim tests need no scenes and no GPU. Import/presentation checks are separate from rules. Numerical comparisons use exact integers/ticks and explicitly stated epsilon only for unavoidable floating point HP/gauge calculations; event/state canonical hashes cover exact persisted representation.

## 16.2 Required families

| Family | Required evidence |
|---|---|
| Determinism | Same content, seed, starting state and command stream produce equal per-tick state hashes, RNG counters and ordered gameplay events. Repeat with watched/unwatched, headless, different real-frame chunk sizes, all clock speeds, camera/modal changes and save/resume at every action phase. Compare at equal Guild ticks; optional battle pace changes elapsed real duration only. Adding an unrelated concurrent operation must not consume another operation's RNG, while shared discoveries/resources still legitimately interact. Preview simulations never touch campaign counters. |
| Tick order | One collision fixture puts final boss kill, scout threshold/injury, processing/crafting/construction completion, operation return, buyer check, delivery/debt deadline, story flag and cutoff at one tick. Assert exact ordered effects and no new action/start. Parameterize one tick before/at/after 20:00 and operation deadline. Concurrent charting scouts both earn due rewards/risk. |
| Numeric rule goldens | Coverage ledger below: one independent expected case for **every normative numeric rule/table cell/formula**, plus boundaries and stacking combinations. Statistical expectations are checked algebraically and deterministic draw fixtures, not flaky random acceptance. |
| Save integrity | Round-trip every aggregate; mid-action/gauge/meter/status equality; difficulty pending; rare reservation; sticky rolls; transfer/payroll interruption; exactly-once rewards. Fail-inject open/write/flush/readback/backup/replace/index stages, process interruption at each step, truncated JSON, duplicate keys, wrong checksum/header, NaN/overflow, path traversal, corrupt main/good backup, corrupt backup, stale tmp, future schema and unknown content refs. Assert last-good recoverable and live state unchanged on failed load. |
| Migrations | One golden fixture per schema/content migration edge; preserved IDs, inventory conservation, no extra time/XP/grants, idempotent repairs/refunds, preserved operation RNG, rejected unsupported gaps/legacy format. |
| Content validation | Positive full registry plus mutated one-defect fixtures for every validator code and semantic rule. Include bad region closures, missing skill bindings, multiple perk choices, illegal transitions, invalid quality distributions and incomplete-authoring release rejection. Validate actual launch database, not only tiny examples. |
| Commands/reservations | Fingerprint before/after rejected input; no state/RNG/receipt mutation. Same command replay returns same receipt. Cross-system claim races, insufficient quantity, stale quotes, rehire inventory return, capacity shrink and equipment HP-clamp anti-heal cases. |
| Scene-script lint | Invoke §09's linter exactly as below; validate generated content and malicious/invalid scene fixtures. Include manuscript parity and offer-branch-only request unlocks. Do not invent §09 lint semantics here. |

## 16.3 Numeric coverage ledger

**[spec decision]** D25 `tests/fixtures/gdd_numeric_rules.json` holds rows `{rule_id,gdd_section,source_table,source_row,field,source_value,test_path,test_method,case_id,status}`. The implementation must enumerate every normative number, including all monster/material/recipe tables, each progression modifier and each officer perk. `tools/check_numeric_coverage.gd` cross-checks that every row points to an executed passing test case and that source revision/hash matches the approved GDD extraction. Document-only samples/proof timings/pacing goals get `status:"non_normative"` plus rationale; they are not silently omitted or enforced as gameplay. A changed GDD invalidates coverage until reviewed. The following is the mandatory family map and representative independently calculable goldens, not a false claim that this draft implements those tests.

| GDD | Required suite / representative golden and full parameterization scope |
|---|---|
| §§3–4.2 | `test_clock.gd`: 07→20 = 46,800 s = 3,900 ticks = 390 real s at 1×, 1,560 s at battle pace; duration 13 s→24 s; exactly 13 hourly buyer checks. Night 39,600 s once, auto-sleep 01:00, max 3 project pins, new day paused. Pacing day 3/10/25 goals are non-normative. |
| §§5.3–5.4 | `test_bonds_perks.gd`: starting 2,500G/0 Rep/60 Morale/F; bond 0–5, ≤1 level/officer/week, story gate and one permanent choice. Parameterize all 12 perks and their costs, relative probability versus points, payroll/week and injury-free-day conditions. Unresolved §06.7 values are explicit failing authoring gates, never guessed expectations. |
| §§5a–5b | `test_commander.gd`, `test_session_grades.gd`: 8 h Fed, 3.2/5.6 movement policy, meals 0/8/5G, 1 h session, rank costs 10/25/45/70/100, D–S points 1–5/+2 tagged dialogue, cap 2/5, per-rank effects and rank-3 cooldowns. All Planning tile/rest/budget/score thresholds; negotiation .95/.85/.70 grade thresholds; Cross-check counts/timer/hint cap; Cutting scores 90/75/55/30 and bonuses 15/11/8/5; Fitting par/+25/+50 and 25/20/15/10% reductions. Romance one partner, five bonds, Bond-4 gate, no stat effects. |
| §§6.1–6.2c | `test_progression.gd`: all starter/Chloris stats, passives, signatures and eight choices/person; 1→5 costs 1,400 XP, 1→6 2,000, 1→8 3,500, 1→10 5,400. Caps 6/3,000 vs 10/12,000; sequential 100n; 2 rank-1 +1 rank-2; rebuild free then 100G; preserve lifetime. Every XP source, standing-at-kill and one tier multiplier, deployment once, hints zero, guests zero persistent XP. |
| §§6.3–6.5 | `test_recovery.gd`: from stamina 4 three dispatches yield 3/2/1 and only third is red; recall no refund; 0 cannot depart; sleep +1; rest full; no idle/rehire/rebuild/expiry stamina. Injury Standard 48 h / Relaxed 24 h, return .25/.40 max HP; idle +.10 max HP/hour, expiry mid-night splits elapsed healing; all state-priority combinations. |
| §6.6 | `test_backpack.gd`: 4×4/5×4/5×5 rank grids; 90° placement; one active category; potion 20G/30% heal at ≤40% alive, row-major one/action, no revive; bow orthogonal adjacency +15% once; starter token 1×3; gear HP increase no heal and removal clamp; consumable origin resale. |
| §§7–8.5 | `test_scouting.gd`: each 1,800 s +2%; 13/25/50 intervals→26/50/100%; 75% guaranteed first missing den; 100% flush unique fixed finds. All three area find tables, weights and gates; chance .45+Tracker .10+map .10 with .80 cap and Insight; base risks .01/.015/.02, fatigue×2, landmark×.75, Chimera .005. Six .01 checks = .058519850599; six .02 = .114157619136. Rare reservation .70, no expiry, consumed on return; +2 Rep once. |
| §§9.1–9.3b | `test_combat.gd`: search max(10,(30*(1-.25e)-5p)*m), 100%/2 paths→12.6 min after rounding; .95 Route Map once. Formation ≤5 with 3 slots/row, ≥1 front; melee-back×.5. All base group chances; c=.80 expected size 2.12; conditional third c/2; group cap .95. ATK18 vs DEF8 base damage floor(1800/108)=16; rate .7 interval 180 s; actions 24/72/12; queue ties and dynamic gauge fractions. Attacker25/defender20/mage formula; every monster skill budget, status strength/duration, provoke, stun, retaliation, overheal cap and multi-target atomicity. Preview 100 trials and 5/25% boundaries. |
| §§2,9.4–9.6,15 | `test_presentation_contracts.gd`, `test_prep_templates.gd`: authored visual numeric defaults are validated separately from sim (including .13/.26s hit-stop and 1–2-frame target flash); presentation cannot change action time/RNG. Exactly two saved named prep templates; apply reports missing actors/items, substitutes nobody and never dispatches. Top bar late-state begins19:00. Palette/camera/art-density defaults belong to presentation acceptance fixtures; approximate proof measurements are marked non-normative where the GDD describes them as results, not rules. |
| §§10–10.5 | `test_monster_yields.gd`: all 19 named stats, 9 ordinary group/variant definitions, 6 rares, 4 bosses, every raw/unit value/output. Variant HP×1.5, ATK/DEF×1.25, base chance .08/+ .04/cap .20, XP×2; rares×3/boss×5. Boar common2+1 and one .20 rare; rare boar guaranteed tusk no elite; variant guaranteed elite plus parent's rare roll; boss five common+one rare; one whole-job quality. Visual 1.15 scale/pose counts belong to content/presentation checks. |
| §§11.1–11.4 | `test_requests.gd`: parameterize seven exact quantities/qualities/rewards/deadlines, 15-gel exclusivity, Garden final24h, −10 once accepted failure, ignored free, at-deadline delivery wins. Clinic 4/week at18G reset1/8/15 no carry; courier first Jeb client; repeats7 days one pending. All eight fixed optional encounters/rewards, 30min approach,72h offer/7day reoffer; all three Chapter2 flashpoint gates/rewards/aftermath and no loss penalty/farming. |
| §§12.1–12.3,12.8 | `test_production.gd`: quality distributions (10/70/15/5),(20/70/8/2),(30/65/5/0) percent; value1.25/1/.5/0; all recipes, forms, footprints, input qualities, fees/durations; 30/20 queue limits; every enhancement level 1–5, +5% base/level, no speed, opening≤2. Staff factors1/.85/.70, fallback2, no work idle; sticky roll under cancellation/reload/cutoff. Rework2:1/4h and3:1/6h, no Unsellable, Rough Patch half+Standard-only. |
| §§12.4–12.5 | `test_market.gd`: demand probabilities .25/.50/.25; factors .75/1/1.25; buy .25/.50/.75, quotas1/2/3, capacity3/5/8 at0/200/700 (+2 shelves). Three Standard hides at12G→gross36 fee2 net34; expected category capacity3.25/13/29.25 over13 checks. Trader floor(.5*base*quality), equipment .25 material-only; Rep one/100 net with remainder. Forecast horizons1/2/3 and .70/.80/.90, fallback1/.60, wrong states equiprobable, persist after promotion. |
| §§12.6–12.7 | `test_staff_hq.gd`: every hire/wage/gate (including Chloris400/120), promotions40h+200G and100h+400G Frontier, wages×1/1.25/1.5 ceil displayed weekly; completed productive hours only. All five HQ input/cost/duration/capacity rows; one construction, full refund, overnight finish, debt lock, capacities carry. |
| §§13.1–13.4 | `test_accounting.gd`: payday20:00 days7n; partial week accrual/7, one employee-level ceil, no double-transfer day; morale thresholds29/30/49/50/79/80, all daily/payroll deltas/caps and clamp once. All six promotion thresholds/costs, no demotion. Loan2500/7days/one ordinary loan, sweep.25 accumulated; receipt1G four times gives1G swept, cap principal. Rescue shortfall direct/once per later unpaid payroll, no dismissal loop. Charter C+Crownstone+zero debt once. |
| §§14–16a.1 | `test_story_transfer.gd`: all event predicates (M06 independent of M05), no fixed day gates; Chapter1 offer warning; Chapter2 three ordered flashpoints. Transfer1500G/48h, arbitrary departure clock preserved, exact two sleep boundaries, payroll pause, accepted delivery-only freeze, no duplicate path −5min at verification, first Frontier risk .02, zero initial exploration, strict local generators with old-stock exceptions. |
| §16b | `test_saves_difficulty.gd`: exactly3 profiles/3 autoslots, many named saves, every trigger, paused resume/no offline time, all persisted state; difficulty next07:00, injury24vs48, wages .75vs1, new timed offers×2, no repeated extension or altered recurrence/debt/transfer/stamina. |

## 16.4 Scene-script lint integration and CI commands

**[spec decision]** D26 Proposed integration seam for Claude's §09: `tools/lint_scenes.gd` exposes `lint(root: String) -> Array[ContentIssue]` and CLI `--root=… --report=…`, with 0/1/2 exit semantics as §06. `tests/content/test_scene_scripts.gd` calls this same function against `res://content/scenes` and fixtures for each §09 rule code. An independent CLI subprocess test asserts exit code/report parity. If §09 chooses another filename/signature, change this adapter and commands together; the rule semantics remain exclusively §09's. Missing linter is a failure, not an optional skip. Scene JSON/manuscript parity tests prove line/choice IDs, nesting, safe checkpoints and offer anchors survive conversion.

Run from the **future FGC project root**; these are specified commands, not commands executed for this draft:

```powershell
godot --headless --path . --editor --import
godot --headless --path . --script res://tools/validate_content.gd -- --root=res://content --mode=release --report=user://validation/content.jsonl
godot --headless --path . --script res://tools/lint_scenes.gd -- --root=res://content/scenes --report=user://validation/scenes.jsonl
godot --headless --path . --script res://tests/run_all.gd -- --report=user://validation/tests.json
godot --headless --path . --script res://tools/check_numeric_coverage.gd -- --report=user://validation/numeric.json
```

The CI wrapper must capture each exit status immediately, enforce a timeout, and fail on nonzero, engine script/parse errors or absent reports; do not let a later successful command mask a failure. Record Godot version/build, OS, content revision, fixture seed and test list. No runtime pass is claimed from documentation review. The audit's stored legacy baseline was red (missing suites plus viewport failures); it cannot certify this project.

**Frontier readiness:** fixtures parameterize base/content IDs and source-rule coverage; adding Frontier tables adds golden cases and cross-base/transfer tests through the same headless runner, with no new testing framework.

---

# 17. Build and repository conventions

- **Branches:** `main` is always green (tests pass). Work happens on short `feature/<topic>` branches merged back through pull requests.
- **Commits:** the imperative mood, one topic each, with Claude-authored commits carrying the co-author line.
- **Never commit** `.godot/`, exports or `assets/` sources larger than needed. Use Git LFS for `assets/**/*.webp|png|ogg` larger than 1 MB. [spec decision]
- **Export:** one Windows preset (`export_presets.cfg`), built by `tools/build.cmd` after `tests/run_all.gd` passes.
- **Documents:** design documents stay in the storyboard repo (the register). The game repo holds only a `docs/README.md` that points to them.

---

# 18. Port list from imc-playground


Paths below are relative to **`D:/Godot Projects/imc-playground/`**. Audit reference: `D:/Codex/IMC/runs/playground-audit/report.md` §§2 (rules/state), 4 (dialogue), 6 (GDD conflicts), 7 “What to port into B”, Appendices A–B. The audit's commit was `b40ee81`; exact function names below were rechecked in the current local files. **[spec decision]** D27 Each later port records actual source commit + file hash + original function, destination, retained invariant, replaced rule and new tests in `docs/ports.json`; do not claim the current working files necessarily equal that historical commit.

## 18.1 Port/adapt specific boundaries

| Exact source file / functions | Proposed destination | Port/adapt and reason |
|---|---|---|
| `Scripts/IMC/company_state.gd`: `save_game` (713), `_read_save_file` (787), `has_save`, `has_backup`, `load_backup`, `load_game`, `_valid_slot` | `app/saves.gd`, `sim/save_codec.gd`, platform `AtomicFileStore` | Adapt canonical round-trip checksum, prewrite validation, temporary verification, validated backup and failure messages. Replace old directory/format/mode/slot/schema assumptions; add tested true atomic replacement and backup staging. Audit §2 calls these the strongest reusable save pattern. |
| Same: `_integer` (854), `_json_safe` (1000), `_validate_data`, `_validate_items`, `_validate_battle` | save/content/state validators | Port defensive technique only: reject malformed scalars, depth/overflow, invalid nested references before changing live state. Rewrite ranges/required fields for GuildState; old schema5/battle data is incompatible. |
| Same: `_migrate` (813) | `sim/migrations/` | Adapt deep-copy sequential metadata-only migration and no-grant-on-load discipline. Do **not** paste old v1–5 defaults into FGC or enable implicit legacy import. |
| Same: `_next_id`, `_ok`, `_fail`, `_commit`, `_can_add_items`, `_take_items`, `_add_items` | command results, receipts, inventory transaction helpers | Adapt monotonically allocated identity, explicit failure/commit boundaries, validation before debit. Replace old inventory stack caps and direct dictionary item removal with quality lots and exclusive reservations. |
| `Scripts/IMC/campaign_operations.gd`: `apply` (147), `_apply`, `action_reason` (710), `_loadout_snapshot` (608), `_same_value`, `_validate_loadout_snapshot`, `validate` | `sim/command_bus.gd`, prep validation and snapshots | Adapt transactional dispatch/unchanged-on-rejection, snapshot isolation and structured guard explanations; rewrite rule dispatch and snapshot shape. Do not port precomputed expedition battle replay. Audit §§2,6,7. |
| Same: `_scene_request_definitions` (705), `chapter_transition` (680), `_validate_request` (1269) | converter, `requests.gd`, `story_flags.gd` | Adapt source mapping, explicit deadlines/state checks and accepted-request carryover structure. Replace every old reward/condition/deadline/transition with current GDD §§11/14/16a; no gameplay constants copied unchecked. |
| `Scripts/IMC/scene_four_data.gd`: `catalog` (1427), `requests` (1432), `resolve_text`, `_safe_name`, `validate`, `_validate_lines`, `_validate_line`, `_index_lines`, `_validate_dependencies`, `_visit`, `_validate_requests` | scene converter, §09 validator, UI token resolver | Preserve verbatim dialogue/choice IDs, nested offer branches, dependency checks, client source anchors and provenance. Replace development request overrides: legacy Gerd is any-condition 90G/30Rep, current GDD is Standard+ 40G/20Rep. Keep legacy tokens internally; render Guild terminology. Audit §§4,6,7. |
| `Scripts/IMC/story_data.gd`: `validate`, `validate_scenes`, `_check_id`, `_check_text`, `_check_line`, `_check_choice`; literal scene/choice records | converter and §09 lint | Adapt ID/text/choice integrity, preserve manuscript parity. Separate every 3D shot/actor pose command from semantic story effects; do not assume old staging is a compatible scene script. |
| `Scripts/IMC/campaign_journeys.gd`: `reason`, `apply`, `record_victory` (72), `settle` (80), `next_event` (90), `validate` | contracts/flashpoint/timer modules | Adapt exactly-once settlement and stable next-event scanning. Replace authored old journeys, ration costs, timing and gates; GDD fixed contracts use30min approach and current combat. |
| `Scripts/IMC/campaign_management.gd`: `roster`, `equipment_comparison`, `inventory`, `departments`, `community` | view-model builders outside authoritative state | Adapt filtered read-only rows and comparison APIs. Recompute from current stats/backpack/quality/service definitions; do not keep old combat-stat formula. |
| `Scripts/IMC/campaign_advice.gd`: `assess`, `_add`, `_safe_tree`, `_time_advice`, `_payroll_due` | prep/advice view models + `risk_forecast.gd` | Adapt structured cause/remedy records and safe inspection. Replace numeric risk heuristics with GDD 100 fixed-seed simulations and exact calendar payroll projection. |
| `Scripts/IMC/battle_session.gd`: `snapshot` (51), `_emit` (254), `record` (261), seeded `setup` (25) | combat snapshot/events/test adapters | Adapt event/snapshot/deterministic-test **interfaces only**. Its turn/skill/element resolution is retired; FGC uses live 12-second concurrent encounter queue. |
| `Scripts/IMC/location_loader.gd`: `build_location` (15), `describe_location` (52) | future presentation location adapter | Adapt marker/destination/arrival conventions, not world instances or renderer state. This is a reference for Claude's presentation sections, not a simulation dependency. Audit §7 item5. |
| `Scripts/IMC/actor.gd`: collision setup within `configure` (58), movement/collision portion of `_physics_process` (135) | future `presentation/world/commander_actor.gd` | Adapt CharacterBody3D collision shape and move-and-slide shell only; use straight-north sprite direction mapping, GDD3.2/5.6 speeds and hunger run gate. Remove rig loading, mesh normalization, skeletal animation and visual rotation dependencies. Audit §7 item5 and GDD§16 explicitly preserve collision/spawn conventions. |
| `tests/company_test.gd`: `_fingerprint`, `_unchanged_failure`, `_new_slot`, `_write_fixture`, `_envelope`, `_test_saves`, `_cleanup` | `tests/{sim,saves}/` | Port fault fixtures, isolation and unchanged-on-failure assertions. Replace values/slot namespace and use bounded safe cleanup. |
| `tools/checks/operations_state_test.gd`: `fingerprint`, `reject`, `bad_save`, `_save_integrity`, `_multi_seed`, `_legacy_migration` | command/save/determinism tests | Adapt negative controls, corrupted-state loading and multi-seed coverage; old migration expectations are source evidence, not compatibility promises. |
| `tools/checks/regional_operations_state_test.gd`: `canonical`, `reject`, `roundtrip`, `bad_save`, `_regional_seeds_and_equipment`, `_new_deadline_boundaries`, `_malformed_saves` | regional/save/transfer tests | Keep regional isolation, round-trip and malformed-state techniques; replace old regional rules, deadlines and equipment assumptions. |
| `tools/checks/scene_four_data_test.gd`: `_source_parity`, `_flatten`, `_anchors`, `_structure`, `_requests`, `_resolution`, `_negative_controls`, `_malformed_scalar_controls` | scene conversion parity tests | Adapt source-line/ID/nested-choice and negative-control checks; rebind to current manuscript and GDD economics. |
| `tests/battle_test.gd`: `_fixture`, `_test_scheduler`, `_test_validated_actions`, `_test_status_lifecycle`, `_verify_ledger` | `tests/sim/test_combat.gd` | Port fixture/assertion/event-ledger patterns, rewrite all turn-order/status/numeric goldens for current GDD. `_test_elements` is not a design authority for FGC. |
| `tools/test.mjs` runner structure | new CI wrapper | Adapt subprocess fail-on-error and report capture only. Discover actual required suites and fail if absent; do not import its stale list or stored green claims (audit §1). |

## 18.2 Explicitly leave behind

| Source boundary | Reason |
|---|---|
| `Scripts/IMC/company_state.gd`: `_initial_state`, `_advance_simulation`, `_resolve_expedition`, `_close_day`, `_gain_experience`, `_person_power`; `campaign_operations.gd`: `_start`, `_advance`, `_payroll`, `_gain_experience`, `_market_price`, `_wear_equipment` | Old balances, start grants, minute/day accounting, payroll, progression, durability and market rules differ. Reimplement from GDD with no silent carryover. |
| `Scripts/IMC/battle_rules.gd`, `battle_model.gd`, `battle_session.gd` resolution (`prepare_turn`, `choose_auto`, `act`, `_resists`, `_apply_status`, `_end_turn`) | Old combat/element/turn engine is not the live GDD action-end queue, meter and row model. Retain only isolated invariant/test ideas listed above. |
| `Scripts/IMC/campaign_catalog.gd` old `routes`, `research`, `region_facts`, equipment/item prices and authored development encounters | Old Pathfinder/rations/research/extra regional boar assumptions are retired. Reuse stable compatible IDs via explicit aliases, not records wholesale. |
| `Scripts/IMC/world_builder.gd`, `tools/author_eurydica.gd`, `tools/bake_worlds.gd`, `tools/expand_outskirts.gd`, `Scenes/Worlds/*.tscn`, `Scenes/DemoForest.tscn` | Procedural city/forest, terrain, scene geometry and forced-bake workflow do not implement the approved HD-2D layout. Never run these against the clean project. Audit §§3,7. |
| `Scripts/IMC/actor_pose.gd`, `atlas_face.gd`, `cinematic_director.gd`, `cinematic_stage.gd`, `cinematic_shot.gd`, `cinematic_sequence.gd`, `dialogue_camera.gd`, `staging_commands.gd`; `Scenes/Cinematics/OpeningStage.tscn` | Retired skeletal/3D facial/shot staging. Preserve semantic dialogue anchors elsewhere; rebuild sprite/portrait staging under §09/presentation. |
| `Scripts/IMC/actor.gd` visual children and rig bindings, `creature.gd`, `battle_view.gd`, `battle_effects.gd`, `Scripts/forest_player.gd`, old shaders/compositor/render options | Wrong camera/rig/scene assumptions. Movement/collision concepts may inform presentation but are not directly ported systems or art approval. |
| `Scripts/IMC/game.gd` as a root monolith and existing panel scenes/layouts | Replace mixed controller with agreed six autoloads, command bus and read models. Do not bring UI dependencies into pure sim. |
| `.godot/`, imported caches, baked resources, saved validation reports, old executable/build outputs | Generated/historical evidence, not source or current acceptance. No blanket asset copy; approved portraits/audio bindings can be reviewed independently for presentation. |
| Old `company_state.gd` 8 MB file limit, mode sandbox/campaign coupling, schema5 header and old save directory | Not FGC profile/slot/content/migration contracts. Avoid collision with legacy user data. |

## 18.3 Proof references are algorithm references, not ports

`D:/Storyboards/Isekai Mercenary Company/HD-2D Proof/src/ops.html`: inspect `interval`, `eligibleFinds`, `scoutTick`, `settle`, `tick`, `resolveTurn` and queue ordering for tested ideas. The read source has `CUTOFF=23*HOUR` (line472), damage applied inside turn-start functions, hint XP and charting ordering differing from current GDD. **Do not translate it verbatim.** `town.html` proves 3.2m/s/120 Guild seconds and offer-branch request behavior, but its 10:00 arrival slice is not the campaign's universal day start and its small shop inventory is not the full economy. Source authority stays with the GDD. Port fixtures only after updating expected values to it.

**Frontier readiness:** port small invariants and identity/provenance boundaries, then feed all regions through the new schemas/modules. Retired Eurydica-specific assumptions cannot leak into the main campaign by copying whole controllers.

---

---

## Appendix A: GDD coverage

| GDD section | Implemented by |
|---|---|
| 1 Vision, 3 Core loop | §01, §03, §04 |
| 2 Visual direction (incl. 2.6 staging) | §00.4, §10, §11, §12 |
| 4 Time, 4.1 Cutoff, 4.2 Night | §05, §07 |
| 5 Guild, HQ, officers, 5.4 bonds, 5a Commander, 5b romance | §07, §14 (romance: Frontier, out of M1–M3 scope) |
| 6 Adventurers | §06, §07 |
| 7 Regions, 8 Scouting | §06, §07, §11 |
| 9 Hunting and combat (incl. 9.3b monster skills) | §07, §11 |
| 10 Monsters and materials | §06, §07 |
| 11 Requests, contracts, flashpoints | §06, §07, §09 |
| 12 Economy (processing, workshop, Reworking, market, information, staff, HQ) | §06, §07 |
| 13 Closeout, payroll, progression | §04, §07 |
| 14 Story gating | §07, §09 |
| 15 Screens | §12 |
| 16 Production notes, 16a Campaign and region tags, 16b Saves and difficulty | §06, §08, §17 |
| 17 Content backlog | Content, not code |
| 18 Change log | History, not code |

## Appendix B: Codex-section spec decisions (D01–D27)

Every **[spec decision]** in these sections is listed below. Decisions select representation, ordering, persistence or validation mechanics, never replacement game balance. D17's session-start eligibility is an implementation interpretation of the one-hour/operating-hours rules and is explicitly visible for merge review.

| Decision | Scope |
|---|---|
| D01 | JSON dialect, one-record files, units, strict immutable typed loading |
| D02 | Typed identity namespaces and manifest content revision |
| D03 | Canonical snake_case IDs plus explicit source/legacy aliases and preserved scene anchors |
| D04 | Typed predicate/effect registries and atomic reward execution |
| D05 | Registered template generators/solvers and frozen session inputs |
| D06 | Request/repeat/contract instance fields and terminal reason representation |
| D07 | Validator API, issue shape/codes, draft/release modes and exit status |
| D08 | Central versioned support rule tables, rather than duplicated constants |
| D09 | Command/event envelopes, transactional receipts, serial/tie and retry semantics |
| D10 | GuildState aggregate names and single write ownership |
| D11 | Absolute tick representation and app-only fractional pacing accumulator |
| D12 | Stable order within the GDD's grouped timed completion phase |
| D13 | Search completion starts only after expiry/cutoff eligibility check |
| D14 | Worker ID as final equal-rank/equal-hours tie-breaker |
| D15 | First runnable queued job, stable remainder and visible blocked jobs |
| D16 | Persist original processing variates and rank/modifier provenance; unresolved odds interaction remains authoring gate |
| D17 | Latest session start 19:00 and evidence-before-hour-advance transaction sequencing |
| D18 | Profile/slot paths, separate namespace and rebuildable index |
| D19 | Versioned Godot round-trip canonicalizer and large integer string representation |
| D20 | Verified atomic replacement abstraction, platform tests and failure behavior |
| D21 | Autosave barriers, cursor advancement and pre/post failure handling |
| D22 | SHA-256 counter RNG, length-prefixed seed derivation and stream ownership |
| D23 | Explicit schema/content migration chain and no implicit legacy import |
| D24 | Test runner discovery/failure semantics, isolated fixtures and reports |
| D25 | GDD numeric coverage ledger and normative/non-normative classification |
| D26 | Proposed §09 linter integration seam and shared CLI/library verification |
| D27 | Per-port commit/hash/provenance record and selective adaptation boundary |

JSON Schemas and example records for §06 are in `Game Design/FGC_07 schemas/` (`schemas/`, `examples/`). They move into the game repo's `content/_schemas/` when M1 starts.

## Changelog
| Date | Change |
|---|---|
| 2026-09-28 | v0.1: first version. Claude's sections written; Codex's §06–08, §16 and §18 merged after review. |
