# Frontier Guild Chronicle: Sprint Plan

**Chapter 1 build plan: milestones M1–M3**

| **Version** | v0.1 · 28 September 2026 |
|---|---|
| **Status** | CURRENT, **approved by the owner on 2026-09-28**. See `FGC_00_Document_Register.md` |
| **Scope** | Order of work, deliverables and exit gates for building Chapter 1 in Godot. This plan owns **sequencing only**. Every rule comes from the GDD, and every "how" from `FGC_07_Implementation_Spec.md`. |

---

# 00. Planning assumptions

- **The team:**
  - **The owner:** design decisions, story writing (the manuscript), character and portrait art (Gemini, Omniflash), and every approval.
  - **Claude, the driver:** architecture, presentation, integration, merging and reviews. Claude decides the order of work within a sprint.
  - **Codex, the helper** (CLI, sandboxed, writing only to `D:/Codex/IMC`): simulation modules and their tests from the spec, content conversion, tools, and environment art through the environment skill. Claude reviews all of it and copies it in.
- **Sprint length:** about one week. A sprint ends at its exit gate, not on a date. If a gate fails the sprint extends; the next sprint never starts on a failed foundation.
- **The project:** `D:/Godot Projects/frontier-guild-chronicle`, Godot 4.7, typed GDScript. Each sprint keeps an unlazy gate ledger in `.unlazy/fgc-sN/` (as SMC does).
- **Placeholder art is expected until its approved version exists.** Missing art never blocks gameplay work, because everything binds through IDs (spec §06, §10.8).
- **Design documents are frozen during a sprint,** except for fixes to genuine gaps, which go to the owning document first (register, rule 3).
- **Definition of done (every task):**
  - the behaviour matches the GDD and spec;
  - `godot --headless --path . --script res://tests/run_all.gd` exits 0;
  - the content validator reports 0 errors;
  - the scene-script lint reports 0 errors;
  - no invented content, text or rules.

---

# 01. Overview

| Milestone | Sprint | Goal | Result you can see | Depends on |
|---|---|---|---|---|
| **M1: headless core** | S0 | Foundation | None (tests only) | this plan approved |
| | S1 | Clock, operations, combat | A hunt and a scout resolve headless, deterministic and golden-tested | S0 |
| | S2 | Economy and requests | A week of processing, crafting, selling, requests and payroll resolves headless | S1 |
| | S3 | Saves, story, Commander, transfer | A scripted Chapter 1 week runs headless, saves and reloads identically | S2 |
| **M2: HD-2D presentation** | S4 | The world | Walk all of Eurydica in the approved pixel look (Proof 1) | S3, build plan approved |
| | S5 | Dialogue and UI | Scenes play from the manuscript; the core management screens work on the real sim | S4 |
| | S6 | Field and battle view | Watch a hunt from dispatch to the Resolution | S5 |
| **M3: Chapter 1 slice** | S7 | Chapter 1 content | Scene 1 to the chapter's end, with days 2–5 play, the night and sleep | S6 + owner's scenes |
| | S8 | Working sessions | The five minigames playable; tuning written into GDD 5a.2a | S7 |
| | S9 | Playtest, balance, build | A Chapter 1 Windows build that passes the "tomorrow I want to" test | S8 |

**The parallel art and writing track** runs alongside S0–S6 and must finish before the sprint that needs it (§05).

---

# 02. M1: headless core

**Goal:** every GDD rule runs in `sim/` with no graphics, and is tested.

## S0: foundation
- The project settings, folders and autoload skeletons (spec §02); a `docs/README.md` pointing to the design documents.
- A typed content loader and **content validator** (spec §06.5). The JSON schemas are copied from `Game Design/FGC_07 schemas/` into `content/_schemas/`.
- **The RNG** (spec §08, D22) and the **command and event bus** (spec §07.1, D09).
- **The test runner** (spec §16), plus a one-line build script.
- **The asset-sync tool** skeleton (spec §10.8), with an empty manifest.
- **Codex:** the validator and schema loading, the RNG and its tests.
- **Claude:** the project skeleton, the bus, `SimHost`, the runner, review.
- **Exit gate:** the runner passes the RNG, bus and validator tests; a malformed content fixture fails with the right error code.

## S1: clock, operations, combat
- The tick pipeline (spec §07.3), the clock, night and sleep (GDD 4, 4.1, 4.2).
- Stamina, injury and rest (GDD 6.3–6.5, with the +1 overnight and full rest-order rules).
- Hunts, groups, scouting and finds, rare sightings, scout risk (GDD 7–9).
- The combat engine: formation, the action queue, damage, statuses, the skill meter, signature skills, **monster skills** (9.3b), variants, experience.
- The risk estimate (100 fixed-seed simulations).
- **Golden tests:** port the numbers the operations proof already demonstrates (`ops.html`) and check them against the GDD.
- **Codex:** the combat engine and scouting modules with their tests.
- **Claude:** the tick pipeline, operations and clock, review.
- **Exit gate:**
  - the same seed gives the same event history twice;
  - watched equals unwatched;
  - every numeric rule in GDD 4 and 6–10 has a passing golden test.

## S2: economy and requests
- Inventory, reservations and the backpack.
- **The processing work order** and **the Workshop work order**, with recipes, enhancement and **Reworking** (GDD 12.1–12.3, 12.8).
- The market and the any-trader fallback, information, and **negotiation-order generation** (5a.2a; the minigame itself comes in S8).
- Requests, repeat orders, contracts and flashpoints (GDD 11).
- Payroll, Morale, Reputation, Guild rank, debt (GDD 13), and HQ construction (GDD 12.7).
- **Codex:** processing, workshop, market and requests with their tests.
- **Claude:** accounting and payroll, construction, review.
- **Exit gate:** a scripted week (hire two, hunt boars, process, craft a vest, sell, deliver Gerd's request, pay wages) produces exactly the numbers the GDD predicts.

## S3: saves, story, Commander, transfer
- **Saves:** profiles, slots, autosave triggers, migration and corruption tests (spec §08, GDD 16b).
- Story flags and predicates (GDD 14), the request unlock tags used by scripts, and the conditions list for the script lint (spec §09.2).
- The Commander: hunger, skills and ranks, and working sessions as data (the grade in, the effects out).
- Bonds and the Bond 5 perks (GDD 5.4), region tags and the region transfer (16a), difficulty.
- **A 30-day headless soak test:** a scripted "reasonable player" runs 30 days. It's a smoke test for balance, not the balance itself.
- **Codex:** saves and migration, the soak script.
- **Claude:** story and Commander, transfer, review.
- **M1 exit gate:**
  - every GDD numeric rule has a golden test that passes;
  - a scripted Chapter 1 week runs, saves mid-fight, reloads, and finishes identically;
  - the soak test finishes 30 days with no invariant violations.

---

# 03. M2: HD-2D presentation

**Goal:** the M1 simulation, seen and played.

## S4: the world
- The asset sync, run against the approved sources.
- **The HD-2D stack:**
  - `SpriteActor`: billboards, directions, poses, emotes;
  - `CameraRig`: exploration and dialogue shots;
  - the post stack: tilt-shift, bloom, grade LUT;
  - `Building3D`: facades, curved roofs, generic rotation;
  - the cutaway;
  - time of day.
- **The ground material:** painted tile materials blended by a painted mask with soft, broken edges, plus edge cutouts (tufts, moss, pebbles), as in the north-bank concept.
- **A plan importer:** it builds the town from `Locations/Eurydica/Build Plan/eurydica-plan.json` (the approved build plan: v7c, the clustered city, since 2026-10-01; v5 is archived), including terraces, walls, stairs, the river, props and markers.
- **Look test first:**
  1. Rebuild the proof-4 slice in Godot and compare screenshots with the proof.
  2. Then build phase 1 of the plan (the Chapter 1 area).
- **Codex:** paints the ground tiles, blend masks, edge props and any new facades from the build plan's asset list, all through the environment skill, as candidates for the owner.
- **Claude:** the whole stack and the importer.
- **Exit gate:** walk phase 1 with collisions, camera, cutaway and time of day. Screenshots are reviewed against the concepts' conformance checklist; the owner approves the look.

## S5: dialogue and UI
- The scene converter and lint (spec §09): all four Chapter 1 scenes lint clean.
- `ScenePlayer`, the dialogue view, talks, barks and ambient lines.
- **UI:** the theme, top bar, alerts, minimap, objective.
- **The core screens:** Adventurer Office (prep, Ongoing list, roster), Processing (work order), Workshop, Commerce, Request Board, Resolution and Day Summary, recruitment and payroll.
- **Screen acceptance states (FGC_08)** are written during this sprint, as in SMC_08.
- **Codex:** the converter, lint and the screen acceptance-state test captures.
- **Claude:** the runtime, dialogue view, screens.
- **Exit gate:** Scenes 1–4 play (on placeholder locations where needed); every core screen reaches its acceptance states on the real simulation.

## S6: field and battle view
- The field stage with the Hylaea set, the search walk, battle presentation (hit-stop, flash, spark, shake, numbers), the skill cinematic, the party HUD, monster pose stills.
- Watch, View and Follow from the Ongoing list; battle pace.
- **Codex:** monster still integration and the pose-switch tests.
- **Claude:** the stage and battle presentation.
- **M2 exit gate:**
  - walk phase-1 Eurydica;
  - dispatch a hunt at Elsie's;
  - watch it through the search and the fight;
  - see the Resolution and the Day Summary;
  - all driven by the M1 simulation, with no presentation-owned rules.

---

# 04. M3: Chapter 1 slice

**Goal:** Chapter 1, playable from New Game to the chapter's end.

## S7: Chapter 1 content
- **Locations:**
  - the Outskirts (Scene 1);
  - the tavern interior (Scene 2; the approved tavern interior concept exists);
  - the Guild house interior and courtyard (Scene 3);
  - the Service Lanes (Hilde, Dr. Emmerich).
- **Scenes:** 1–4, the **14:00 return** (recruitment and the first requests), the **three officer introductions** (Valerie, Fulker, Liliana), and the **Chapter 1 conclusion**, all written by the owner in the script format.
- **Life in the city:** the night city, sleep, ambient townspeople by time band.
- **Exit gate:** a new game plays through Chapter 1's story beats with no lint errors and no dead ends.

## S8: working sessions
- The minigame framework (spec §14) and the five sessions: Expedition Planning, Counter-offer, Cross-check, Cutting Chart, Fitting.
- Their tuning numbers are written into GDD 5a.2a.
- Bond points and friendship-scene triggers (the scenes are written by the owner as they come).
- **Codex:** the Fitting and Cross-check puzzle generators and their solvers.
- **Claude:** the framework, Planning, Counter-offer, Cutting Chart.
- **Exit gate:** each session gives its GDD grades reproducibly (D–S; Fitting has no D and completes at C with assistance, FGC_08 P8) from fixed seeds, and its outputs change the simulation as the GDD says.

## S9: playtest, balance, build
- The owner plays Chapter 1. Balance the GDD's starting values against the hook test ("Tomorrow I want to ___" at days 3, 10 and 25) and the audit's pacing checks.
- Record every retuned number in the GDD, with a change-log line.
- Build the Windows release candidate.
- **M3 exit gate:** the owner signs off the Chapter 1 playtest; tests are green; the build runs on a clean machine.

---

# 05. Parallel art and writing track

| Needed by | Item | Who |
|---|---|---|
| S4 | **Eurydica build plan**: done: v5 approved 2026-09-29, replaced by v7c (clustered) approved 2026-10-01 (`Locations/Eurydica/Build Plan/`); the Godot town was rebuilt from v7c on 2026-10-01 and moved to the pixel look the owner approved the same day (S4 done) | Codex draft, Claude review, owner approval |
| S4 | Pixel art: trees, the red tree, 49 props, the Hylaea battle objects (`Approved Pixel v1`); buildings, roofs and ground drawn in code | Codex (generated pixel art), Claude (code); owner approval 2026-10-01 |
| S5 | **Eurydica region map** painting, drawn from a reference image: the parchment base and a painted vignette per area (hand-drawn, not vector), plus the ink layers for landmarks, dens and paths revealed by discovery (FGC_08 §5.9) | Codex; owner approval |
| S5 | Emote icons (11, format §5) | Codex or owner |
| S5 | Special sprite poses from the scene headers (sit, kneel, salute, point, nod, think, raise mug, stand up from a chair…) | Owner (Gemini) |
| S5 | The Travelling Merchant's negotiation portraits | Owner |
| S6 | Monster stills: Moss Slime and Forest Wolf first (the boar exists), then Chimera and Blackfang | Owner |
| S6 | Anselm and Nell sprites (walk and battle), replacing the stand-ins | Owner |
| S7 | **Outskirts:** concept B approved 2026-09-28 (`Locations/Eurydica Outskirts/`); assets (the backdrop strip and road-edge tile) still to paint | Codex |
| S7 | Tavern interior and Guild house interior and courtyard assets | Codex (environment skill); owner approval |
| S7 | **Scenes to write:** the 14:00 return, the three officer introductions, the Chapter 1 conclusion | Owner |
| S8 | Friendship scenes for Bond 1 (the Eurydica cap; GDD 5.4) | Owner |

---

# 06. Risks and mitigations

| Risk | Mitigation |
|---|---|
| The tilt-shift post shader is slow at 1280×800 | Measure in S4; fall back to half-resolution blur, or to CameraAttributes DoF plus a tilt mask |
| The blended ground doesn't read like the concept | The S4 look test comes before building the district; the owner approves the look, not just the code |
| Writing throughput for Chapter 1 scenes | S7 lists the scenes early; locations and systems don't wait on them (placeholder scenes keep flow testable) |
| Many special sprite poses | A missing pose falls back to idle (spec §10.4); the owner prioritises by scene |
| The Codex CLI sandbox fails (as after the power cut) | Test with a one-line run before long jobs; Claude takes the work back if Codex is unavailable |
| Balance drift across 13 systems | Golden tests per rule (M1), the 30-day soak (S3), and the hook-test playtest (S9) |

---

## Changelog
| Date | Change |
|---|---|
| 2026-09-28 | v0.1: first plan (M1–M3, S0–S9, art and writing track). |
