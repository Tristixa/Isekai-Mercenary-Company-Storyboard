# Eurydica Monsters: roster and still-pose prompts

**Status:** move names and skill effects **approved by the owner on 2026-09-28**. Drafted by Codex, reviewed by Claude. It replaces the video workflow in `Gemini Monster Prompts.md`: monsters get **one still per pose**, with no animation videos. Monster designs are still made and approved one by one as art.

Frontier Guild Chronicle · Chapters 1–5 · prepared 2026-09-28 for Claude review. Documentation only; no art approval, generation or integration implied.

## Draft acceptance review

Scope: only `runs/monster-list/Eurydica Monsters v2.md` and `handoff/monster-skills-last.txt`; the source project is read-only. This revision follows `handoff/task-monster-skills.md`. Manual review gates assess source fidelity and art-brief completeness.

- [x] G1: Preserve the 19-monster roster, canonical stats, access, palettes and identity blocks; leave the source unchanged.
  EVIDENCE: Node assertions compared all 19 stat rows, roster identity/tier/access/size/key fields, all 10 identity blocks, original pose blocks and palette maps to the source. Source SHA256 remained cedd1c82f9ed058fced927d84ca59ba436f642baa8f697ddbf666cd7f8a2aa41.
- [x] G2: All 9 ordinary, 6 rare and 4 boss/flashpoint skills have proposed names and exact effects within §9.3b budgets; ordinary variants inherit skills.
  EVIDENCE: Read GDD §9.3b and §9.3 stacking rules. Checked 19 proposed effects; all 9 ordinary and 6 rare effects match their exact tier alternatives. Manually reviewed the four boss effects: ×2.5 single hit, row-wide ATK DOWN, one-action stun, row-wide SPD DOWN. Every name/effect is proposed; variant inheritance and fifth-action timing are explicit.
- [x] G3: Six new ordinary Skill prompts, consistent recolour inheritance, pose inventory and independently counted production totals.
  EVIDENCE: Counted 54 pose prompt bullets, including 6 ordinary Skill prompts; preserved all original pose blocks. Inventory has 15 five-pose sets and 4 six-pose sets = 99 required named-monster stills. Eight five-pose recolour sets and nine five-pose variant recipes yield 40 and 45 derivatives; total including variants is 144. Reviewed every parent chain; no separate rare-source prompt remains.
- [x] G4: Candidate/approved paths and boar approval provenance are current; only the two requested deliverables are written, including a five-line report.
  EVIDENCE: Read local Boar Approval.json: five approved stills, staging archive under D:/Codex/IMC/Boar/Battle Stills v1/, finals directly under Enemy Sprites/Boar/. Updated candidate and approved delivery paths. Only this copy and the five-line handoff report were written; no images generated, no source-project edits or integration.

## Sources and interpretation

Unless absolute, source paths below are relative to `D:/Storyboards/Isekai Mercenary Company/`:

- `Game Design/IMC GDD.md`, including the 2026-09-28 §9.3b decision: §§2.2, 7.1, 8.4, 9–10, 11.3–11.4, 13.3, 14 and 17. Authoritative for species, stats, access and combat.
- `D:/Codex/IMC/Boar/Battle Stills v1/Production.md`, `Prompts.json`, `GATES.md` and `Approval.json`: staged boar production records. Five battle stills (Hurt, Second Hurt, Defeat, Tusk Gore, Wild Charge) were approved via `Approve Battle Stills.ps1`; approved PNGs are directly in `Enemy Sprites/Boar/`. `Enemy Sprites/Boar/Start - Idle.png` was visually inspected for the prior draft; no new visual inspection is claimed here.
- `Production Assets Requirement/Region Prompts - Bernmoor and Erythra Highlands.md` and `Production Assets Requirement/Higgsfield Battleground Prompts.md`: regional colour/mood only. Their painted scenery workflow does not replace pixel-art monster rendering.
- `AGENTS.md`: untouched masters and internal cast comparison. This handoff limits monster comparison to scale sanity and excludes cleanup/transparency conversion.

The latest handoff replaces the GDD's older one-still coverage and the retired monster-video workflow with individually generated still poses. No animation clips, sheets, sprite atlases or game changes are requested.

**Combat authority:** GDD §9.3b gives every monster one skill, including ordinary variants. Monsters use the attacker meter: +25 per completed attack; after four attacks the next (fifth) action is the skill, then the meter resets to 0. Normal targeting applies: front row first, provoke respected. All move names and exact effects below are *proposed* assignments, not approved or playtested kits. Tusk Gore and Wild Charge retain their existing production names; their move-label assignments and Wild Charge's ×1.5 effect remain *proposed* here.

Ordinary skills choose one ×1.5 hit, or a normal ×1.0 hit plus one status for 2 target actions: ATK DOWN −15%, DEF DOWN −15%, or SPD DOWN (action interval ×1.25). Rares choose one ×2.0 hit, or ×1.25 plus one status for 3 target actions: −25% ATK/DEF or interval ×1.4. Bosses/flashpoints choose a hit up to ×2.5, a whole-front-row status, or a 1-action stun. Multipliers refer to normal-hit damage. Under §9.3, same-stat debuffs use the strongest magnitude and longest remaining duration without adding duplicates; up and down multiply. Stun refreshes to the greater remaining skip count. Durations count the affected fighter's actions. Variants inherit the parent's skill and apply their ATK bonus normally. Each boss has **one skill**; Second Hurt is a reaction alternative, never a second phase.

## Roster

19 named monsters: 9 Ordinary, 6 Rare, 1 optional Boss and 3 Flashpoints. Flashpoint is a production tier; in combat these are Elite bosses. Eurydica is Chapters 1–2 (owner, 2026-09-28): Chapter 2 holds all three flashpoints in order, Chimera, Ambermaw, Crownstone, and no other species or flashpoint.

**Chapter first met:** `1+ / E` and `1+ / D` mean no explicit chapter floor is stated for ordinary region access: the rank and discovery gates govern it, potentially during Chapter 1 or later. Bernmoor and Erythra are both needed in Chapter 2 (their flashpoints come second and third), but those are production groupings, not invented locks. Rares additionally require a scout sighting (§8.4). Ordinary discovery thresholds within each region are 0%, 25%, 50% in table order. Hylaea is Rank F. Boss chapter numbers are explicit gates, not estimates.

**Art dimensions:** proposed idle silhouette height × horizontal length, in native art pixels, excluding padding; characters stand about 93 px tall. These are brief targets, not GDD stats or measured exports. Keep pixel density and body mass constant through poses; expand the canvas for action, never stretch a pose to its idle bounding box. Bosses are visibly taller and longer than ordinary relatives. Boar target is provisional: retain the existing drawing and verify native scale before any placement. M = magenta `#FF00FF`; G = green `#00FF00`. All future palettes/design details are proposed unless explicitly sourced.

### Hylaea Forest

| Name | Region | Tier | Chapter first met | New art or recolour of X | Key colour | Size, art px H × L | Status |
|---|---|---|---|---|---|---|---|
| Moss Slime | Hylaea Forest | Ordinary | 1; F | New art | M | 42 × 62 | To make |
| Dire Boar | Hylaea Forest | Ordinary | 1; F | Existing boar art, labelled Hylaea Boar in production | M | ~108 × 160 | Existing Idle; five battle stills approved, including Wild Charge; Second Hurt is extra |
| Forest Wolf | Hylaea Forest | Ordinary | 1; F | New art | M | 82 × 145 | To make |
| Mossback Elder | Hylaea Forest | Rare | 1+; F, sighting | Recolour of Dire Boar | M | ~108 × 160 | To make, pipeline recolour |
| Silvermane | Hylaea Forest | Rare | 1+; F, sighting | Recolour of Forest Wolf | M | 82 × 145 | To make, pipeline recolour including Skill |
| Blackfang Direwolf | Hylaea Forest | Boss | 2+; E, wolf known, M08, EUR-SUB-04 | New art | M | 145 × 230 | To make |
| Hylaea Chimera | Hylaea Forest | Flashpoint | 2; E, 300 Rep, Chapter 1 complete | New art | M | 180 × 265 | To make |

### Bernmoor

| Name | Region | Tier | Chapter first met | New art or recolour of X | Key colour | Size, art px H × L | Status |
|---|---|---|---|---|---|---|---|
| Marsh Slime | Bernmoor | Ordinary | 1+ / E; Chapter 2 (second flashpoint region) | Recolour of Moss Slime (proposed regional reuse) | M | 42 × 62 | To make, pipeline recolour |
| Marsh Serpent | Bernmoor | Ordinary | 1+ / E; Chapter 2 (second flashpoint region) | New art | M | 88 × 160 | To make |
| Marsh Stalker | Bernmoor | Ordinary | 1+ / E; Chapter 2 (second flashpoint region) | New art | M | 95 × 165 | To make |
| Reedcoil Elder | Bernmoor | Rare | 1+ / E, sighting; Chapter 2 (second flashpoint region) | Recolour of Marsh Serpent | M | 88 × 160 | To make, pipeline recolour including Skill |
| Pale Marsh Stalker | Bernmoor | Rare | 1+ / E, sighting; Chapter 2 (second flashpoint region) | Recolour of Marsh Stalker | M | 95 × 165 | To make, pipeline recolour including Skill |
| Ambermaw Matriarch | Bernmoor | Flashpoint | 3; E, 800 Rep, Chimera cleared | New art | M | 165 × 270 | To make |

### Erythra Highlands

| Name | Region | Tier | Chapter first met | New art or recolour of X | Key colour | Size, art px H × L | Status |
|---|---|---|---|---|---|---|---|
| Stone Crawler | Erythra Highlands | Ordinary | 1+ / D; Chapter 2 (third flashpoint region) | New art | G | 75 × 140 | To make |
| Highland Wolf | Erythra Highlands | Ordinary | 1+ / D; Chapter 2 (third flashpoint region) | Recolour of Forest Wolf (proposed regional reuse) | G | 82 × 145 | To make, pipeline recolour |
| Ridge Drake | Erythra Highlands | Ordinary | 1+ / D; Chapter 2 (third flashpoint region) | New art | G | 115 × 195 | To make |
| Redmane Alpha | Erythra Highlands | Rare | 1+ / D, sighting; Chapter 2 (third flashpoint region) | Recolour of Highland Wolf | G | 82 × 145 | To make, pipeline recolour including Skill |
| Old Ridge Drake | Erythra Highlands | Rare | 1+ / D, sighting; Chapter 2 (third flashpoint region) | Recolour of Ridge Drake | G | 115 × 195 | To make, pipeline recolour including Skill |
| Crownstone Wyrm | Erythra Highlands | Flashpoint | 4; D, 1,400 Rep, Ambermaw cleared | New art | G | 215 × 360 | To make |

### Canonical stat check

Transcribed from GDD §§10.1–10.4. Rate is the source attack-rate value. Rare XP is shown as base before the rare ×3 award; do not multiply any other row by that rare factor. No combat stats are inferred from proposed sprite size.

| Monster | HP | ATK | DEF | Rate | Base XP |
|---|---:|---:|---:|---:|---:|
| Moss Slime | 180 | 4 | 0 | 0.7 | 6 |
| Dire Boar | 330 | 6 | 8 | 0.8 | 11 |
| Forest Wolf | 420 | 8 | 10 | 1.0 | 14 |
| Mossback Elder | 800 | 11 | 18 | 0.8 | 32 |
| Silvermane | 950 | 13 | 16 | 1.1 | 38 |
| Blackfang Direwolf | 1,950 | 15 | 25 | 1.0 | 65 |
| Hylaea Chimera | 2,400 | 17 | 25 | 1.0 | 80 |
| Marsh Slime | 510 | 10 | 15 | 0.8 | 18 |
| Marsh Serpent | 660 | 13 | 20 | 1.0 | 24 |
| Marsh Stalker | 840 | 15 | 25 | 1.1 | 30 |
| Reedcoil Elder | 1,320 | 17 | 25 | 1.0 | 55 |
| Pale Marsh Stalker | 1,680 | 20 | 30 | 1.1 | 65 |
| Ambermaw Matriarch | 3,300 | 21 | 35 | 1.0 | 110 |
| Stone Crawler | 900 | 17 | 35 | 0.8 | 32 |
| Highland Wolf | 1,140 | 20 | 30 | 1.1 | 38 |
| Ridge Drake | 1,500 | 24 | 45 | 0.9 | 48 |
| Redmane Alpha | 2,280 | 26 | 36 | 1.1 | 80 |
| Old Ridge Drake | 3,000 | 30 | 50 | 0.9 | 95 |
| Crownstone Wyrm | 5,400 | 28 | 50 | 1.0 | 180 |

Materials in §10.5 support visible gel/core, boar meat/hide/tusks, wolf pelts/fangs, serpent scales/venom gland, stalker hides/claws, crawler plates/core and drake scales/heart. Internal hearts, glands and cores need not be exposed; do not invent equipment or extra species to illustrate a loot item. Rare material inheritance does not authorize adding horns, armour or limbs.

### Regional and rare recolour recipes

The GDD permits regional/rare palette reuse (§2.2) and names all six rare parents (§10.4). Reuse those exact silhouettes and every required pose, including Hurt/Defeat. These proposed palette maps preserve each material's ordered light/mid/dark values and outlines; they are not newly approved identities. Rare enlargement is not mandated; the 15% rule belongs only to ordinary variants.

| Target ← parent | Proposed palette mapping | Set key | Pose handling |
|---|---|---|---|
| Marsh Slime ← Moss Slime | Leaf greens → honey `#C59B43`, amber `#98742C`, peat `#4B4530`; cool teal-grey underside `#435C58` | M | Recolour all five poses, including Skill |
| Highland Wolf ← Forest Wolf | Brown-grey coat → slate `#69747C`, pale grey `#C7CBC5`; tan ruff → muted rust `#985C43`; ivory fangs retained | G | Recolour all five poses, including Skill; change only flat exterior key from M to G consistently |
| Mossback Elder ← Dire Boar | Brown fur → charcoal umber `#403B2E`; olive moss → deep pine `#344B2B` with pale sage `#93A477`; tusks → aged ivory `#C9B78B` | M | All five parent poses; Wild Charge recoloured as Elder Charge (*proposed*) |
| Silvermane ← Forest Wolf | Coat → silver `#B8C5CB`, cool grey `#697D87`; ruff → off-white `#E1E4D9`; eyes → pale gold | M | All five parent poses, including the same howl Skill still |
| Reedcoil Elder ← Marsh Serpent | Scales → dark reed olive `#58663C`; bands → ochre `#B39B54`; belly → cream `#D4C7A1` | M | All five parent poses, including the same coil Skill still |
| Pale Marsh Stalker ← Marsh Stalker | Hide → pale bone `#D4D3B8`, sage-grey `#8A9B8D`, teal-grey `#526B66`; claws retain ivory | M | All five parent poses, including the same pounce Skill still |
| Redmane Alpha ← Highland Wolf | Slate coat → charcoal `#434C55`; ruff → brick red `#A34E3E`, ember ochre highlights `#CC8852`; fangs ivory | G | All five parent poses, including the same howl Skill still |
| Old Ridge Drake ← Ridge Drake | Terracotta scales → weathered stone `#999487`; ridge → dark iron `#555D65`; retain restrained old rust `#825741` in scales | G | All five parent poses, including the same brace Skill still |

### Ordinary variants — pipeline only, no new art

Exactly nine variant identities, derived from their ordinary parent's entire five-pose set, including Skill. Each inherits its parent's skill name and effect; its ATK bonus applies normally (§9.3b). GDD §10.0: 8% independently per ordinary hunt member; Howling Ridge adds 4 percentage points in Hylaea; total cap 20%. Appearance is 15% larger with distinct palette; stats HP ×1.5, ATK/DEF ×1.25, unchanged Rate, parent base XP ×2 once. Pipeline/engine placement must preserve source pixels; do not destructively resize masters. Fixed optional-contract encounters receive no random variants. Do not apply these rules to rares or bosses.

| Ordinary parent | Variant palette (proposed unless noted) | Variant key |
|---|---|---|
| Moss Slime | Teal gel `#4E9992`, pale mint `#AACBB1`, dark blue-green `#315B60` | M |
| Dire Boar | Rust fur `#934D35`, burnt-ochre mane `#BC7741`, dry ochre moss `#9A904D`; rust identity recorded in GDD changelog, exact map proposed | G |
| Forest Wolf | Tawny ochre `#A48D5C`, cream `#D1C5A0`, deep brown `#4C463A` | M |
| Marsh Slime | Deep olive `#5B6939`, pale straw `#C5BB73`, peat `#3A4430` | M |
| Marsh Serpent | Copper `#A16643`, sand `#D1B476`, charcoal `#3F4848` | G |
| Marsh Stalker | Dusk teal `#426F73`, silver sage `#A4B9A8`, deep peat `#303F3D` | M |
| Stone Crawler | Dark slate `#444F61`, cold silver `#A0ADB9`, ochre seams `#AA9362` | G, retain parent key |
| Highland Wolf | Deep umber `#5B483B`, buff `#BAA078`, dark rust ruff `#8F4C39` | G |
| Ridge Drake | Iron blue `#536E86`, steel `#A0B2B9`, charcoal ridge `#303C4B` | G, retain parent key |

If a recolour introduces red-like hues, its derived set uses green consistently, including internal silhouette gaps. This is a planned pipeline key substitution, never a mix of keys within one monster set. No palette recipe uses its own exact key colour inside the creature.

## Pose inventory and move names

Every pose faces RIGHT: enemies stand on the left. Defeat retains the head at the right. Ordinary and Rare = Idle, Attack, Skill, Hurt, Defeat. Boss/Flashpoint = Idle, Attack, Skill 1, Hurt, Second Hurt, Defeat; **one skill**, no Skill 2. Boar Second Hurt remains an extra approved still; Wild Charge fills its required Skill slot.

All move names and effects are *proposed*, including retained production labels. Species names remain canonical. Repeated move names in prose and recolour mappings carry the same *proposed* status. Each move uses one apex still, not a multi-frame sequence.

| Monster | Attack | Skill | Full required set |
|---|---|---|---|
| Moss Slime | Gel Bump — *proposed* | Sticky Press — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Dire Boar | Tusk Gore — *proposed*; existing boar production name | Wild Charge — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Forest Wolf | Snapping Bite — *proposed* | Dread Howl — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Mossback Elder | Tusk Gore — *proposed*; inherited production label | Elder Charge — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Silvermane | Snapping Bite — *proposed* | Silver Howl — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Blackfang Direwolf | Blackfang Bite — *proposed* | Ravaging Lunge — *proposed*; **one skill** | Idle, Attack, Skill 1, Hurt, Second Hurt, Defeat |
| Hylaea Chimera | Raking Claw — *proposed* | Threefold Threat — *proposed*; **one skill** | Idle, Attack, Skill 1, Hurt, Second Hurt, Defeat |
| Marsh Slime | Gel Bump — *proposed* | Clinging Mire — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Marsh Serpent | Reed Fang — *proposed* | Venom Coil — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Marsh Stalker | Hooking Claw — *proposed* | Ambush Pounce — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Reedcoil Elder | Reed Fang — *proposed* | Crushing Coil — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Pale Marsh Stalker | Hooking Claw — *proposed* | Silent Pounce — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Ambermaw Matriarch | Marsh Crush — *proposed* | Matriarch Surge — *proposed*; **one skill** | Idle, Attack, Skill 1, Hurt, Second Hurt, Defeat |
| Stone Crawler | Plate Ram — *proposed* | Plate Crack — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Highland Wolf | Snapping Bite — *proposed* | Ridge Challenge — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Ridge Drake | Ridge Bite — *proposed* | Ridge Crush — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Redmane Alpha | Snapping Bite — *proposed* | Ridge Howl — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Old Ridge Drake | Ridge Bite — *proposed* | Ancient Brace — *proposed* | Idle, Attack, Skill, Hurt, Defeat |
| Crownstone Wyrm | Crownfang Strike — *proposed* | Crownstone Sweep — *proposed*; **one skill** | Idle, Attack, Skill 1, Hurt, Second Hurt, Defeat |

### Proposed skill effects and visuals

Every name and effect below is *proposed*. Row-wide boss statuses use the whole-front-row budget form without a damaging hit. Single-target hits and the stun obey normal row/provoke targeting.

| Monster | Skill name | Exact effect | One-line visual |
|---|---|---|---|
| Moss Slime | Sticky Press — *proposed* | *Proposed:* One ×1.0 hit + SPD DOWN (action interval ×1.25) for 2 target actions. | Gel spreads into a broad rightward pressing lobe, its sticky base low. |
| Dire Boar | Wild Charge — *proposed* | *Proposed:* One ×1.5 hit. | Existing approved low rightward gallop with tusks leading. |
| Forest Wolf | Dread Howl — *proposed* | *Proposed:* One ×1.0 hit + ATK DOWN −15% for 2 target actions. | Planted howl-and-bite action, shown at the howl apex with chest lifted and jaws up-right. |
| Mossback Elder | Elder Charge — *proposed* | *Proposed:* One ×2.0 hit. | Recolour Dire Boar Wild Charge. |
| Silvermane | Silver Howl — *proposed* | *Proposed:* One ×1.25 hit + ATK DOWN −25% for 3 target actions. | Recolour Forest Wolf Dread Howl. |
| Blackfang Direwolf | Ravaging Lunge — *proposed* | *Proposed:* One ×2.5 hit. | Long rightward pounce, both forepaws reaching and jaws forward. |
| Hylaea Chimera | Threefold Threat — *proposed* | *Proposed:* ATK DOWN −25% to every living front-row opponent for 3 actions of each affected target; no damage. | Lion jaws, goat horns and snake-tail head threaten right together. |
| Marsh Slime | Clinging Mire — *proposed* | *Proposed:* One ×1.0 hit + SPD DOWN (action interval ×1.25) for 2 target actions. | Recolour Moss Slime Sticky Press. |
| Marsh Serpent | Venom Coil — *proposed* | *Proposed:* One ×1.0 hit + ATK DOWN −15% for 2 target actions. | Tight coil and exposed right-facing fangs at the braced venom-bite apex. |
| Marsh Stalker | Ambush Pounce — *proposed* | *Proposed:* One ×1.5 hit. | Extended rightward pounce, foreclaws reaching and tail trailing. |
| Reedcoil Elder | Crushing Coil — *proposed* | *Proposed:* One ×1.25 hit + DEF DOWN −25% for 3 target actions. | Recolour Marsh Serpent Venom Coil. |
| Pale Marsh Stalker | Silent Pounce — *proposed* | *Proposed:* One ×2.0 hit. | Recolour Marsh Stalker Ambush Pounce. |
| Ambermaw Matriarch | Matriarch Surge — *proposed* | *Proposed:* Stun one normally selected target for exactly 1 action (one skipped action); no damage. | Heavy body surges right, chest lifted and forelegs reaching. |
| Stone Crawler | Plate Crack — *proposed* | *Proposed:* One ×1.0 hit + DEF DOWN −15% for 2 target actions. | Front plate tilts into a forceful downward-right press; its own shell stays intact. |
| Highland Wolf | Ridge Challenge — *proposed* | *Proposed:* One ×1.0 hit + DEF DOWN −15% for 2 target actions. | Recolour Forest Wolf Dread Howl, preserving its howl-and-bite silhouette. |
| Ridge Drake | Ridge Crush — *proposed* | *Proposed:* One ×1.5 hit. | Low four-legged brace at peak tension before a crushing forward drive. |
| Redmane Alpha | Ridge Howl — *proposed* | *Proposed:* One ×1.25 hit + DEF DOWN −25% for 3 target actions. | Recolour Highland Wolf Ridge Challenge, retaining the original Forest Wolf Skill silhouette. |
| Old Ridge Drake | Ancient Brace — *proposed* | *Proposed:* One ×2.0 hit. | Recolour Ridge Drake Ridge Crush; the brace anticipates a crushing drive, not a defensive buff. |
| Crownstone Wyrm | Crownstone Sweep — *proposed* | *Proposed:* SPD DOWN (action interval ×1.4) to every living front-row opponent for 3 actions of each affected target; no damage. | Continuous thick tail sweeps lower-right, crowned neck still aimed right. |

## Still prompts

**Assembly rule:** each request is exactly the following shared block + that monster's identity block + ONE pose block. This factoring keeps prompts concise; never send only the pose sentence. Generate/select Idle first; every later pose attaches that exact selected Idle as identity, proportions, palette, pixel-density and camera reference. Do not attach an unrelated monster as its identity. Recolour-only sets use the parent poses; do not regenerate them.

**Shared block, required on every call:**

```text
Create ONE standalone HD-2D pixel-art enemy sprite in the Octopath style, one still image, not a sheet or animation. Face RIGHT, enemies stand on the left. Light the material from the upper left. Crisp square pixel clusters, stepped material-coloured outlines, restrained shades; no smoothing, blur or painted gradients. Show one complete coherent creature with generous margins, all limbs, tails, horns and fang tips intact. Keep the identity block's flat opaque key background throughout all empty space and silhouette gaps. No transparency, effects, hit flashes, dust, motion lines, particles, shadows, ground, scenery, opponent, text or UI. The engine supplies effects and shadows. Match the stated native art-pixel scale relative to a roughly 93-pixel-tall character; canvas padding is not body size. For non-Idle poses, preserve the exact creature in the attached selected Idle, its palette, anatomy, body scale and pixel density; change only the requested pose at its peak moment. Do not reproduce Idle instead of the requested action.
```

The anatomy of unmade monsters is **proposed visual design**, not additional lore: the GDD supplies names/materials but does not specify all limbs or head arrangements. Keep natural creature mouths, fangs and snouts; human mouthless-sprite rules do not apply. Regional mood comes from the creature's palette, not painted scenery or haze.

### Moss Slime — new art

**Identity block:** Low, asymmetrical domed gel body, broad flattened base, two small dark eyes directed right, moss-like green colour islands inside the gel, no limbs or accessories. Leaf green `#73934E`, pale sage `#B0C785`, dark olive `#3D5231`; opaque-looking pixel shading, no background showing through gel. Target 42 × 62 art px. Flat MAGENTA `#FF00FF`. Warm Hylaea highlights, subdued green-brown lower-right shading.

- **Idle:** One calm right-facing gel dome, eyes alert, base broadly settled; complete silhouette, no drips detached from the body. Establish the identity for the other poses.
- **Attack — Gel Bump (*proposed*):** Attached Idle is the exact identity. At impact apex, stretch the whole gel mass forward RIGHT into a blunt rounded shoulder, rear compressed and eyes intent; preserve volume, no projectile.
- **Skill — Sticky Press (*proposed*):** Attached Idle is the exact identity. At the peak of a sticky press, spread the gel into a broad flattened lobe reaching RIGHT, rear mass low and base stretched close underneath; eyes intent, volume preserved, no detached gel or target.
- **Hurt:** Attached Idle is the exact identity. Compress the struck right edge sharply inward while the mass recoils LEFT and bulges unevenly upward; involuntary squash, no fragments.
- **Defeat:** Attached Idle is the exact identity. Collapse into a low, intact flattened gel mass, eyes shut, front still at right; no evaporating or dissolving pixels.

### Forest Wolf — new art

**Identity block:** Lean long-legged quadruped wolf with a deep chest, pointed ears, a modest shaggy neck ruff and long bushy tail. Brown-grey coat `#716E5D`, tan highlights `#AA9A78`, dark umber `#383B33`, ivory fangs and amber eyes; no red markings or equipment. Target 82 × 145 art px. Flat MAGENTA `#FF00FF`. Hylaea warmth and quiet earthy values.

- **Idle:** Alert right-facing side stance, four legs naturally spaced, head level and tail low, weight balanced; establish the lean body and ruff.
- **Attack — Snapping Bite (*proposed*):** Attached Idle is the exact identity. Short forward-right bite at full neck extension, jaws open around empty space, one forepaw lifted and hind legs driving; keep tail and all paws complete.
- **Skill — Dread Howl (*proposed*):** Attached Idle is the exact identity. One peak howl still: body planted facing RIGHT, forelegs straight, chest lifted, neck stretched up-right and jaws open; bushy tail lowered. This is the howl apex of the howl-and-bite action; no sound rings or glow.
- **Hurt:** Attached Idle is the exact identity. Chest recoils LEFT, head jerks up-right, forelegs bend and hind paws brace; a hit reaction, not a leap.
- **Defeat:** Attached Idle is the exact identity. Fully side-lying wolf, legs slack and folded naturally, head resting to the right, eye closed and tail settled; no wound or blood.

### Blackfang Direwolf — new art

**Identity block:** Oversized heavy quadruped direwolf, much broader shoulders and deeper chest than Forest Wolf, thick angular ruff, long full tail, prominent dark fangs edged with bone highlights. Near-black umber `#252A27`, charcoal `#414B46`, muted brown highlights `#726A53`, amber eye. No extra limbs or armour. Target 145 × 230 art px, clearly larger than a character. Flat MAGENTA `#FF00FF`.

- **Idle:** Menacing right-facing planted stance, shoulders high, neck low, fangs visible in a restrained snarl; show the complete massive silhouette.
- **Attack — Blackfang Bite (*proposed*):** Attached Idle is the exact identity. Heavy short bite forward RIGHT at maximum jaw opening, neck thrust out, forelegs firm beneath the shoulders; keep it distinct from the airborne skill.
- **Skill 1 — Ravaging Lunge (*proposed*, one skill):** Attached Idle is the exact identity. Peak long forward-right pounce, body stretched horizontally, both forepaws reaching and hind legs extended back, jaws aimed ahead; no streaks or target.
- **Hurt:** Attached Idle is the exact identity. Powerful backward-LEFT recoil, chest lifted, front paws pulled inward, head jerked up-right with open jaws.
- **Second Hurt:** Attached Idle is the exact identity. Small grounded flinch, all paws near their support positions, neck contracts and head angles slightly away from the right; torso remains right-facing.
- **Defeat:** Attached Idle is the exact identity. Heavy body fully on its side, head low at right, folded forelegs and slack hind legs, ruff and tail settled, eye shut.

### Hylaea Chimera — new art

**Identity block:** Proposed coherent chimera anatomy: one four-legged tawny lion body, lion head at the front, one goat head rising from the shoulders, one long snake-headed tail curving forward behind them; no wings. Three heads remain anatomically distinct and readable. Umber/tawny fur `#806748`, dark mane `#403B2D`, olive serpent scales `#647344`, ivory horns `#D0C19C`, amber eyes. Target 180 × 265 art px. Flat MAGENTA `#FF00FF`. Warm woodland material highlights; no supernatural glow.

- **Idle:** Four paws planted facing RIGHT, lion head watchful, goat head upright, attached snake tail arcing behind with its head looking right; all three heads visible without tangling.
- **Attack — Raking Claw (*proposed*):** Attached Idle is the exact identity. Lion forequarter drives right at the apex of a single extended near-forepaw rake; other limbs support the body, goat head balances above and attached snake tail counterbalances.
- **Skill 1 — Threefold Threat (*proposed*, one skill):** Attached Idle is the exact identity. Coiled threatening apex: lion jaws thrust right, goat horns lowered right, snake-tail head raised and extended right beside the body; a single braced pose, no breath, venom or extra attacks drawn.
- **Hurt:** Attached Idle is the exact identity. Shared torso jolts LEFT, forelegs buckle inward, lion head jerks up-right, goat head tilts back and snake tail contracts; preserve the exact head count and attachments.
- **Second Hurt:** Attached Idle is the exact identity. Restrained grounded flinch, lion head turns slightly away, goat neck dips and snake tail tightens; keep body right-facing and all four legs coherent.
- **Defeat:** Attached Idle is the exact identity. Lion body fully side-lying, paws slack, lion head rests at right, goat neck folded naturally above the shoulder and snake tail limp along the body; all heads intact, no severing.

### Marsh Serpent — new art

**Identity block:** Single long limbless serpent, low horizontal rear coils and a raised S-shaped neck, narrow scaled head, small pale fangs, no cobra hood or horns. Olive scales `#7B8050`, peat-dark bands `#424C3D`, ochre belly `#BAA467`, amber eyes, cool teal-grey shade. Target 88 × 160 art px in coiled Idle; retain body length through every pose. Flat MAGENTA `#FF00FF`. Humid amber-marsh palette, no water or haze.

- **Idle:** Rear body in one readable low coil, neck raised in an S and head facing RIGHT; show a continuous body ending in one complete tail tip.
- **Attack — Reed Fang (*proposed*):** Attached Idle is the exact identity. Head and neck shoot forward RIGHT at maximum extension, fanged jaws open, rear coil compressed for leverage; continuous unbroken body, no venom spray.
- **Skill — Venom Coil (*proposed*):** Attached Idle is the exact identity. One tightly braced coil apex, thickest body loop contracting around empty space, raised neck aimed RIGHT, fangs showing in preparation for the venom bite; continuous body and clear tail tip, no captured creature or venom spray.
- **Hurt:** Attached Idle is the exact identity. Neck kinks back LEFT from a blow at the right, head lifted abruptly, rear coil bunches inward; no detached segments.
- **Defeat:** Attached Idle is the exact identity. Entire serpent lies slack in a shallow horizontal S, head resting at right and eyes shut, tail fully visible; no upright striking coil.

### Marsh Stalker — new art

**Identity block:** Proposed low, long-bodied reptilian quadruped with lean shoulders, four splayed clawed feet, a narrow wedge-shaped snout, low dorsal ridge and long tapered tail; hide rather than heavy armour. Dark peat `#4D5546`, muted sage `#86977B`, ochre throat `#B8A16A`, ivory claws, dull gold eye; teal-grey shading. Target 95 × 165 art px. Flat MAGENTA `#FF00FF`. Marsh camouflage in broad readable patches, no attached reeds.

- **Idle:** Crouched alert side stance facing RIGHT, four feet planted apart, wedge snout level, long tail stretched behind; silhouette clear of the body.
- **Attack — Hooking Claw (*proposed*):** Attached Idle is the exact identity. Torso drives forward RIGHT, near foreleg reaches at full claw-hook extension, other three legs support the low body; no slash graphic.
- **Skill — Ambush Pounce (*proposed*):** Attached Idle is the exact identity. One extended forward-RIGHT pounce apex, near foreclaws reaching ahead, both hind legs thrust back, narrow head low and long tail stretched behind; coherent four limbs, no trails.
- **Hurt:** Attached Idle is the exact identity. Shoulder jerks back LEFT, struck foreleg folds, snout lifts up-right and tail bends for balance; recoil rather than attack.
- **Defeat:** Attached Idle is the exact identity. Reptile fully on its side, all four limbs loose, head at right, tail low and uncurled, eye shut; no crouched ambush stance.

### Ambermaw Matriarch — new art

**Identity block:** Proposed massive low-slung four-legged marsh reptile, broad heavy jaw, thick neck, swollen shoulder mass, long muscular tail and blunt low back scutes; visibly distinct from the lean Stalker. Deep peat hide `#4F5037`, olive scutes `#73764B`, amber-gold jaw/throat `#BF963F`, cream teeth `#D7C99B`; cool teal-grey shade. Target 165 × 270 art px. Flat MAGENTA `#FF00FF`. No brood, eggs, ornaments or extra species.

- **Idle:** Broad four-footed right-facing stance, belly low, huge amber jaw slightly open, heavy tail curved left; retain clear separation of the near and far legs.
- **Attack — Marsh Crush (*proposed*):** Attached Idle is the exact identity. Short heavy downward-forward bite at its apex to the RIGHT, head lowered and jaws spread, forefeet planted wide; no victim or debris.
- **Skill 1 — Matriarch Surge (*proposed*, one skill):** Attached Idle is the exact identity. Whole body surges forward RIGHT at full driving stride, chest lifted, forelegs reaching, hindquarters pushing and heavy tail extended behind; distinct from the planted bite, no water splash.
- **Hurt:** Attached Idle is the exact identity. Massive shoulders recoil LEFT, foreknees fold unevenly, jaw jerks up-right and tail curls inward; one clear involuntary hit reaction.
- **Second Hurt:** Attached Idle is the exact identity. Smaller braced flinch with low body, one forefoot drawn inward, head angled slightly away from the right and jaw tightened; no flip.
- **Defeat:** Attached Idle is the exact identity. Huge torso collapsed onto its side, forelegs folded slack, jaw resting at right, tail settled low, eye shut; preserve full mass and scutes.

### Stone Crawler — new art

**Identity block:** Proposed squat six-legged crawling creature with a broad segmented stone-plated back, small forward head under the front plate and stubby jointed legs; no humanoid shape. Terracotta plates `#A5664B`, rust-dark joints `#643F34`, slate underside `#4F5C66`, pale stone highlights `#B7A894`, small amber eyes. Target 75 × 140 art px. Flat GREEN `#00FF00` because of red-like stone. Crisp cold-highland slate shading, no loose floating rocks.

- **Idle:** Low planted stance facing RIGHT, six legs coherently attached with far legs partly occluded, stone plates overlapping along the back, small head visible at front.
- **Attack — Plate Ram (*proposed*):** Attached Idle is the exact identity. Front plate and head thrust forward RIGHT at the apex of a low ram, front legs bracing wide and rear legs pushing; intact shell, no debris.
- **Skill — Plate Crack (*proposed*):** Attached Idle is the exact identity. Raise the front body and tilt its leading plate into a forceful downward-RIGHT press, front legs bent beneath it while middle and rear pairs brace wide; distinct from the low horizontal ram, all six legs coherent, shell intact, no target or debris.
- **Hurt:** Attached Idle is the exact identity. Front body tips back LEFT, front leg pair draws inward, rear legs brace and head retracts slightly beneath the plate; no broken stones.
- **Defeat:** Attached Idle is the exact identity. Shell lies tilted onto its side, all six legs folded slack with natural overlap, head low at right; no disintegration or exposed core.

### Ridge Drake — new art

**Identity block:** Proposed sturdy wingless four-legged drake, long neck, angular hornless snout, continuous low jagged dorsal ridge and tapering tail. Terracotta scales `#9B5D45`, dark rust `#653F36`, slate belly `#65717A`, pale gold ridge tips `#C2A16A`, ivory teeth. Target 115 × 195 art px. Flat GREEN `#00FF00`. Cold Erythra palette with crisp upper-left highlights, no flame or glow.

- **Idle:** Four-footed alert stance facing RIGHT, neck lifted slightly, jaws closed, jagged ridge clear against the key and tail trailing left; establish the complete wingless anatomy.
- **Attack — Ridge Bite (*proposed*):** Attached Idle is the exact identity. Neck drives forward RIGHT into a full-open bite, body low, front legs brace and hind legs push; no fire or target.
- **Skill — Ridge Crush (*proposed*):** Attached Idle is the exact identity. One powerful low brace at peak tension before a crushing forward drive, four legs spread and bent, neck pulled back with snout still RIGHT, jagged back ridge high and tail curled close; no magical barrier or debris.
- **Hurt:** Attached Idle is the exact identity. Neck and chest recoil LEFT, snout tilts up-right, one foreleg buckles while hind legs brace; dorsal ridge and tail remain attached.
- **Defeat:** Attached Idle is the exact identity. Whole drake side-lying, legs loose, long neck curved down to head at right, tail settled and eye closed; intact ridge and teeth.

### Crownstone Wyrm — new art

**Identity block:** Proposed immense limbless stone-scaled wyrm with a thick serpentine body, tall raised neck, broad reptilian head and a crown-shaped cluster of five blunt stone spurs fixed to its skull. No wings, arms or detached stones. Rust/terracotta scales `#995B45`, iron-slate plates `#53616D`, pale crown edges `#C4B798`, dark seams `#343E44`, amber eye. Target 215 × 360 art px in Idle; preserve full body length across poses. Flat GREEN `#00FF00`. Crown is natural stone growth, not metal regalia.

- **Idle:** Enormous low rear coil with tall front neck rising at right, head aimed RIGHT, all five crown spurs readable and tail tip visible left; body one continuous mass.
- **Attack — Crownfang Strike (*proposed*):** Attached Idle is the exact identity. Heavy neck thrusts forward RIGHT and slightly down at maximum bite reach, jaws open, rear coil compressed for leverage; keep complete crown and body.
- **Skill 1 — Crownstone Sweep (*proposed*, one skill):** Attached Idle is the exact identity. Peak powerful body sweep: neck held toward RIGHT while the thick continuous tail arcs forward along the lower-right side, broad opposing body curves imply force; no rock projectiles or impact effects.
- **Hurt:** Attached Idle is the exact identity. Raised neck snaps back LEFT, head tilts up-right, lower body bunches under it and tail contracts; preserve all crown spurs, no shattered plates.
- **Second Hurt:** Attached Idle is the exact identity. Modest neck contraction with head angled slightly away from the incoming right-side blow, heavy rear coil still planted; keep right-facing silhouette and intact crown.
- **Defeat:** Attached Idle is the exact identity. Entire wyrm lies slack in a long low curve, crowned head resting at right, no upright neck, tail laid left and eye closed; full intact stone-scaled body.

## Recolour pose completion

Recolours reuse all five parent stills, including Skill; no separate parent-source Skill generation is needed. Former rare-only howl, coil, pounce and brace sources are now covered by the ordinary Skill blocks. Redmane Alpha also reuses Forest Wolf's howl through Highland Wolf; the former proud howl description is consolidated into this shared pose. No genuinely different rare pose remains required. Preserve recoloured masters separately and record the exact parent pose and palette chain.

| Derived monster / proposed Skill name | Parent Skill still | Final treatment |
|---|---|---|
| Marsh Slime / Clinging Mire (*proposed*) | Moss Slime / Sticky Press (*proposed*) | Marsh palette; M key |
| Highland Wolf / Ridge Challenge (*proposed*) | Forest Wolf / Dread Howl (*proposed*) | Highland palette; exterior key M → G |
| Mossback Elder / Elder Charge (*proposed*) | Dire Boar / approved Wild Charge (*proposed* skill assignment) | Mossback palette; M key |
| Silvermane / Silver Howl (*proposed*) | Forest Wolf / Dread Howl (*proposed*) | Silvermane palette; M key |
| Reedcoil Elder / Crushing Coil (*proposed*) | Marsh Serpent / Venom Coil (*proposed*) | Reedcoil palette; M key |
| Pale Marsh Stalker / Silent Pounce (*proposed*) | Marsh Stalker / Ambush Pounce (*proposed*) | Pale Stalker palette; M key |
| Redmane Alpha / Ridge Howl (*proposed*) | Highland Wolf / Ridge Challenge (*proposed*), originally Forest Wolf | Redmane palette; G key |
| Old Ridge Drake / Ancient Brace (*proposed*) | Ridge Drake / Ridge Crush (*proposed*) | Old Ridge palette; G key |

## Production order

1. **Moss Slime and Forest Wolf first** (GDD §17). Select each Idle, then make Attack, Skill, Hurt and Defeat separately. Reuse the existing boar; check its file/pose provenance without rerendering it.
2. **Hylaea Chimera and Blackfang Direwolf next** (§17), each Idle followed by its five non-Idle poses. These are separate Chapter 2 flashpoint and optional-contract targets, not alternate names for one boss.
3. Complete Hylaea rare recolours: Mossback from boar and Silvermane from wolf; reuse each parent's Skill still. Prepare the three Hylaea ordinary-variant palettes in the pipeline.
4. **Bernmoor:** recolour Marsh Slime; make Marsh Serpent and Marsh Stalker, then Ambermaw Matriarch. Complete Reedcoil Elder and Pale Marsh Stalker, reusing their parents' Skill stills, and three ordinary variants.
5. **Erythra Highlands:** make Stone Crawler and Ridge Drake; recolour Highland Wolf. Make Crownstone Wyrm, then Redmane Alpha and Old Ridge Drake by recolouring their parents' Skill stills; prepare three ordinary variants.
6. Chapter 2's closing transition beat reuses Eurydica's roster; no extra monster or flashpoint is introduced. Source reference, silhouette/scale checks and review precede any eventual game integration.

This plan has **10 new identities / 54 still prompts**: 6 new-art ordinary monsters × 5 poses = 30, plus 4 bosses/flashpoints × 6 poses = 24. The six ordinary Skill prompts are included in 54; there are **0 additional parent Skill-source prompts**. There are **8 named recolour sets** (2 regional + 6 rare), each with 5 derived poses = 40, and **9 ordinary-variant palette recipes**, each covering 5 inherited poses = 45. Dire Boar supplies 5 existing required poses. The 19 named monsters require **99 stills** (54 new + 40 recoloured + 5 existing); variants add 45 derived stills for **144 required stills** including variants. Boar Second Hurt is one preserved extra outside these totals. Counts describe the production plan, not images created or newly approved by this draft.

## How to deliver

Make all candidates under `D:/Codex/IMC/<Monster>/Battle Stills v1/`, with GDD names as folders for new work. Keep the existing Dire Boar alias `Boar`: its staging folder is `D:/Codex/IMC/Boar/Battle Stills v1/`. Five boar battle stills were approved via `Approve Battle Stills.ps1` and recorded in `Approval.json`; do not move or regenerate that approved set. Suggested candidate layout:

```text
D:/Codex/IMC/<Monster>/Battle Stills v1/
  Idle.png
  Attack - <Name>.png
  Skill - <Name>.png         [ordinary/rare]
  Skill 1 - <Name>.png       [bosses/flashpoints; one skill]
  Hurt.png
  Second Hurt.png           [bosses/flashpoints; existing Boar extra retained]
  Defeat.png
  masters/                  [untouched generation/download originals]
  recolours/                [separate derived candidates when applicable]
  Production.md
  Prompts.json
  GATES.md
```

Only after explicit owner approval, copy selected final PNGs to `D:/Storyboards/Isekai Mercenary Company/Enemy Sprites/<Monster>/`. Dire Boar keeps the `Enemy Sprites/Boar/` alias. Keep masters, prompts, QA, working files and unapproved derivatives in staging. Preserve existing approved filenames, including `Wild Charge.png`, and map them to pose slots in the production record.

This is a future delivery layout, not artwork created by this draft. Keep untouched masters including source dimensions, provider/source path and exact prompt. Record the chosen Idle and each image's parent provenance, including ordinary Skill sources for regional and rare derivatives. For every recolour record palette map, source pose, key and intended scale, keeping the parent master unchanged. Candidate review and selection must not be represented as owner approval.

Deliver separate still images on their consistent **opaque flat key**. No transparency conversion, pixel cleanup, resampling, atlas packing or animation-video production belongs to this delivery. Never overwrite approved art with an unreviewed derivative. Human face restrictions do not erase creature mouths or legitimate detail.

Before future art delivery, internally compare monster scale against `HD-2D Proof/out/atlas-wtris.png`, `atlas-welsie.png` and `atlas-wcmd.png`, checking atlas metadata and using matching battle orientation where available. Compare at native art-pixel scale and the same integer nearest-neighbour enlargement with a common foot baseline; never normalize individual heights. For monsters this is **scale sanity against characters only**, not a demand for human proportions. Keep the comparison internal unless requested. Record the observed monster H × L and reference scale in its production record; bosses must read clearly larger. Do not claim that this documentation task performed those future art checks.

Review each still's identity, distinct peak pose, right-facing orientation, complete anatomy, consistent body scale, upper-left light and flat key. Preserve intentional thin fangs, horn tips, claws, tails and eye clusters. Grid checks alone never prove faithful drawing. Keep the boar's approved Second Hurt as an extra source still; its approved Wild Charge fills the ordinary Skill requirement.
