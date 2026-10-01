# Frontier Guild Chronicle: Document Register

**Living index. Read this first.**
**Last updated:** 28 September 2026

This register answers one question: "which document is current?". Every topic has exactly **one** owning document. Files, folders and tools still carry the old name "IMC" (Isekai Mercenary Company); that's history, not a second project. Archived documents are kept for history only and must never be used as a source.

---

## 1. Current document set

| # | Current file | Version | Owns (authority for) |
|---|---|---|---|
| 00 | `Game Design/FGC_00_Document_Register.md` | living | Which file is current, authority order, standing rules |
| 01 | `Game Design/IMC GDD.md` | v2.1.x | **All game design:** rules, numbers, systems, campaign structure, screens, the "what". Summary docs never override it. |
| 02 | `Game Design/Scene Script Format.md` | v1 | The script syntax: speakers and expressions, narration, thoughts, cues, choices and tags, talks, barks, ambient lines |
| 03 | `Manuscript/<Chapter>/<Scene>.md` | per scene | Every spoken line, choice, narration line and scene's staging. Written in format 02. |
| 04 | `IMC_STORY_AGENT_BIBLE.md` | living | Story canon: world, institutions, characters' identities and voices, the chapter arc |
| 05 | `Game Design/Chapters/<Chapter>.md` | per chapter | Chapter implementation notes (beats, milestones, handoffs) |
| 06 | `Requests/` (`README.md`, `Chapter 1.md`, `No Deadline Requests.md`, `Recurring/`) | per file | Request records: clients, requirements, rewards, deadlines, lifecycle notes. Values must match GDD 11. |
| 07 | `Game Design/FGC_07_Implementation_Spec.md` | v0.1 | **Godot architecture:** runtime contracts, data formats, save, RNG, rendering stack, script runtime, tests: the "how". Its JSON schemas and examples are in `Game Design/FGC_07 schemas/`. |
| 08 | `Game Design/FGC_08_UI_HUD_Spec.md` | v0.1 draft | **UI and HUD:** the Three Houses visual language, face and portrait rules, key-screen wireframes, the painted asset kit and proposed changes. Its screen inventory (102 entries, 69 components, gap register) is in `Game Design/FGC_08 UI screens/`. |
| 09 | `Game Design/FGC_09_Sprint_Plan.md` | v0.1 | **Order of work only**, never rules: milestones M1–M3, sprints S0–S9, exit gates, the art and writing track |
| 10 | `Characters/Adventurers and Staff Roster.md` | living | Looks, personalities and asset lists of hired characters |
| 11a | `Game Design/Naming Guide.md` | living | Name roots, method, avoid-list, and every current name with its meaning |
| 11 | `Characters/Negotiation Buyers Roster.md` | living | The negotiation buyers: factions, looks, personas and expression list |
| 12 | `Characters/Officers/<Name>/` | per officer | Officer profiles and approved portrait expressions |
| 13 | `IMC_Portrait_Maker_Agent.md` + `Notes/Portrait_Approvals.md` | living | The locked portrait style and portrait QA; which portraits are approved |
| 14 | `Production Assets Requirement/` | per file | Asset briefs and generation prompts: sprites, battle batches, monsters (`Eurydica Monsters.md`), buyer portraits, region and battleground prompts |
| 15 | `Locations/Eurydica/` (`README.md`, `Build Plan/`, `markers.md`) | living | The current city plan (v7c) and the scene markers used by scripts; `Archive/` holds the 3D-era plans and studies (history only) |
| 16 | `Environment Assets/<Region>/` (approved sets) | per set | **Approved** environment art: Hylaea calibration set, Eurydica facades v1. Only approved assets live here. |
| 16a | `UI Kit/Approved v1/` | v1 | **Approved UI kit:** every painted UI piece by tier, icons, emotes, stain and watermark layers, `kit.json` (nine-slice margins, tints) and proof mockups. Defined by FGC_08. |
| 17 | `D:/Godot Projects/IMC-Companion-Skill-Environment` (`$imc-environment-art-direction`) | git | The environment art workflow, including HD-2D building facades (`references/hd2d-buildings.md`) |
| 18 | `D:/Godot Projects/IMC-Companion-Skill` (`$imc-art-direction`) | git | Character and monster sprite art direction |
| 19 | `HD-2D Proof/` (`src/`, `tools/`, `GATES-*.md`) | frozen | **Reference implementations** of rules and presentation: battle, operations, town. They demonstrate intent; the GDD and spec win on any difference. |

**The game:** `D:/Godot Projects/frontier-guild-chronicle` (Godot 4.7, repo `Tristixa/frontier-guild-chronicle`).
**Reference only:** `D:/Godot Projects/imc-playground` (legacy 3D, shared with Haris Munandar and Reza Chrisna). Port from it per spec §18; never merge back.
**Candidates** (unapproved art and drafts) live in `D:/Codex/IMC/`, never in the project folders.

---

## 2. Authority order

When two documents disagree, resolve by **topic**, not by date:

| Topic | Winner → fallback |
|---|---|
| A game rule or number (combat, economy, time, progression) | 01 GDD → 07 spec → 19 proofs |
| Request values (reward, deadline, quantity) | 01 GDD §11 → 06 Requests |
| What a character says, and a scene's staging | 03 Manuscript → 04 bible (voice) |
| Script syntax | 02 Scene Script Format → 07 spec §09 (runtime) |
| Story canon, identities, chapter arc | 04 bible → 05 chapters → 01 GDD (only for gameplay-facing structure such as flashpoint order) |
| Character looks and asset lists | 10/11/12 rosters → 13 portrait guide → 14 production docs |
| Environment look and camera | 16 approved sets → 17 environment skill → 15 location concepts |
| Engine, code architecture, data format, tests | 07 spec |
| Order of work | 09 sprint plan (when written) |

**Standing rules:**
1. **Documents beat images.** A concept or generated image that shows a different value, label or layout is wrong where it differs; images are authoritative only for the look they were approved for.
2. **A summary never restates a value differently.** If a summary and its source differ, the source wins and the summary is corrected.
3. **Change the owning document first.** Change a rule in its owning document first (with a change-log line), then update the summaries. The GDD's change log is §18.
4. **Nothing archived is a source:** `IMC GDD v2.0 (archived).md`, `GDD v2.1 Proposals.md` (decision record), `GDD Audit 2026-09-27 (Codex).md` (evidence), `Production Assets Requirement/Gemini Monster Prompts.md` (superseded), and anything in an `Archived` folder.
5. **Candidates never live in the project.** Art and drafts stay in `D:/Codex/IMC/` until the owner approves them.

---

## 3. Cross-document decisions log

| Date | Decision | Owning doc updated |
|---|---|---|
| 2026-09-27 | Renamed to Frontier Guild Chronicle; the organisation is the Guild | 01 GDD |
| 2026-09-28 | Eurydica is Chapters 1–2; the Frontier starts at Chapter 3 | 01 GDD, 04 bible, 14 monsters |
| 2026-09-28 | Manuscript uses the HD-2D script format; Chapter 1 Scenes 1–4 converted | 02, 03 |
| 2026-09-28 | Eurydica NPCs have no portraits yet (name only), except the Travelling Merchant's negotiation set | 02, 11 |
| 2026-09-28 | New clean Godot project; `imc-playground` is reference only | 01 GDD §16, 07 spec |
