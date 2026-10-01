# Frontier Guild Chronicle: UI-HUD Specification

**Version 0.1 (draft, 2026-09-28).** Status: **in review.** P1, P2 and P5–P8 were decided by the owner on 2026-09-28.

This document defines what every screen shows and how it looks. It sits between the GDD, which says what the player must be able to see and do (§15, the screen contracts), and the implementation spec FGC_07, which says how the UI is built (§12 layers and theme, §13 input). Where this document and the GDD disagree, the GDD wins until the owner approves a GDD change; each proposed change is listed in §9.

Sections 1–3 and 5–8 were written by Claude. Section 4, the screen inventory, was drafted by Codex from the GDD and reviewed by Claude.

---

## 1. The reference: one game only

**Visual reference: Fire Emblem: Three Houses.** The owner chose it (2026-09-28) for its homey, nostalgic management hub, which is close to our Guild house: a calendar, officers, rosters with skill levels, quest cards, bonds. The owner's screenshots are in `Research/Fire Emblem Three House UI/`, and each file name carries a note.

**Readability rule: Dragon Quest XI.** It isn't a second visual source. We take only its lesson: simple, clean, readable screens that don't feel like plain vector graphics.

We copy Three Houses' **structure and grammar**, never its assets, emblems or text. Codex never receives its screenshots as image references; the kit is described in words (§7).

## 2. Visual language

### 2.1 The grammar we take from Three Houses

| # | Element | How Three Houses does it | FGC version |
|---|---|---|---|
| G1 | **The world stays visible** | Menus are cards floating over the live 3D scene; the player character stays in the middle | Management screens are cards over the HD-2D diorama. The world behind gets a stronger tilt-shift blur and dims to about 70%. No full-screen takeovers except the title, the region map, minigames and results. |
| G2 | **Screen title ribbon** | A diagonal ribbon in the top-left corner, flat colour with a faint pattern, the screen name in serif | Band-coloured flat ribbon, flat line-art ends, the screen name in Marcellus. The owning officer's small name tag beneath it (GDD 15). |
| G3 | **Paper cards** | Pale ivory cards; corner ornaments are tone-on-tone line art | Surface cards with a 1–2 px Line border and tone-on-tone corner ornaments (§2.2). |
| G4 | **Header bands** | Flat colour bands with a faint diamond lattice and a small medallion | Flat Band colour, lattice ≤15%, a small flat icon, the title in Marcellus. |
| G5 | **List rows** | Face slot, name, dotted leader lines, bars with numbers; the selected row is a glowing highlight band with a quill cursor | The same. Selected row: a Blue glow band. The cursor is a small quill (our own drawing). Dotted leaders in Ink at 40%. |
| G6 | **List + detail** | A list card on the left, a detail card on the right | The default layout for every roster, stock and queue screen. |
| G7 | **Tabs** | Labels across the top, separated by diamond medallions, with shoulder-button hints at each end | The same, with an Accent diamond on the active tab. |
| G8 | **Help ribbon** | A ribbon at the bottom centre with star ends, describing the selected item | The same. It carries the GDD §15 "exact next requirement" text when an action is blocked. |
| G9 | **Button hints** | Angled dark tabs with the key glyph, then a light label plate, bottom right | The same. Glyphs switch between keyboard and gamepad (FGC_07 §13). |
| G10 | **Main menu as a book** | An open book with a list of chapters and a quill | **The Guild ledger:** an open ledger book with the menu entries, the Guild name and the purse on its page. |
| G11 | **Date emblem** | A wreath medallion with a large day number and the month | **The clock medallion:** a wreath medallion with the day number and the time. The ring fills through the day, and it turns orange from 19:00 (GDD 15). |
| G12 | **Objectives** | A short list under the date, top left, with a scroll icon per line | The same: story objectives and pinned projects (up to three, GDD 3). |
| G13 | **Results banner** | A full-width flat band with a large word, then one line per reward | Flat Band colour; the grade word in Band text (Accent only for S). |
| G14 | **Battle cards** | Nameplate banners (blue ally, red enemy), an HP diamond with the number and small stat cards, slightly tilted in 3D | The party's cards stack down the right edge, semi-transparent and slightly tilted (§5.7; P5). |

### 2.2 Visual hierarchy, layers and decoration *(revised again 2026-09-28 from the owner's deep read of Three Houses)*

**History.** v1 (painted, textured) had the right look for navigation pieces but wrong for content. v2 and v3 (flat) read as vector. The owner's analysis, confirmed by zoomed crops of the screenshots, is that Three Houses uses **three tiers of treatment** and **separate overlay layers**, not one finish everywhere.

**Three tiers:**

| Tier | What | Treatment | Three Houses example |
|---|---|---|---|
| **1. Identity and navigation** | Title ribbon, the Guild ledger book, the clock medallion, results banner | **Painted and textured allowed**: brush texture, ornate painted ends, depth. These are few and large, so they can carry the richness. | The Menu book, the "Roster"/"Goals" ribbons |
| **2. Content cards** | Lists, dossiers, request cards, dialogue box, map cards | **Paper with stains** (below), a thin dark outer line and a soft darker edge burn; frame decoration and border strips are **pattern only** (flat line pattern, tone-on-tone). Header bands: flat dark band with a small medallion icon. | Staff Detail, Region Map "Battlefield", Profile |
| **3. Text-heavy and transient** | Notifications, tooltips, help ribbon, objectives, button hints | **No texture, no stains.** Plain surface, an **icon first**, then the text. | The objective list, the help ribbon |

**Overlay layers (never baked into the card):** a card is drawn as stacked pieces, so each can be added, moved or faded in the engine.
1. The base paper (flat colour, or a very soft paper tile).
2. **Stains:** a set of 6–8 soft, cloudy, low-opacity blotch overlays (multiply blend, about 6–12%), placed and rotated per card from a seeded pick so cards don't repeat.
3. **Watermark:** a large, faint emblem behind the content (about 5–8%), one per screen or card: the owner's emblem (§9 P9), in black or Ink.
4. The frame: a thin dark line, the edge burn, corner and border patterns.
5. The content.

**Headings inside cards** (Condition, Attributes, Tracker): either **bold**, or on a **dark band with a faint diagonal lattice that fades to transparent**, with light text (the Profile's "Personal History").

**Components, from the screenshots:**
- **Tabs:** each label sits on a small dark diamond; the active tab gets a larger, glowing diamond (Profile tabs).
- **Face slots:** no frame. A **dark gradient backing** behind the face, and the face may overlap the row edge slightly (Staff Roster).
- **Bars** (HP, stats, progress): the fill sits **inside a dark track with its own thin border**, a contained bar (Staff Roster). The textured stamina segments from v1 stay.
- **Row dividers:** a light line above a dark one (a slight emboss), plus the dotted leader under the name.
- **Values:** a small label, then a large right-aligned number ("Next: 52").
- **Icons everywhere:** dark rounded tiles with a light glyph for skills and categories; badges for rank (a letter inside a badge shape); a coin icon on a dark tile for gold; icons on every notification ("⚠ Operation returned", never "Alert | Operation returned").
- **Selection:** the glowing selected-row band and the quill (v1's, which the owner liked); the ledger menu's brush-stroke highlight (§5.8).

**The test is unchanged:** in content tiers the eye lands on the text first. Richness belongs to tier 1.

### 2.3 Colour *(the owner's palette proposal below was tried in v2/v3 and not adopted: the owner rated v1's parchment-and-navy colouring best. **The GDD 2.5 tokens stay, as used in v5.** This table is kept only for its status colours and as a record.)*

Picked from the owner's palette (`Research/Color Palette.png`): lighter, ivory and white surfaces instead of dark navy and old parchment.

| Token | Hex | Use |
|---|---|---|
| Surface / Surface raised | #F7F3E8 / #FAFAFA | Cards, lists / selected-row base, text fields |
| Surface tone | #F2E8D6 | Section bars, table headers, row stripes |
| Ornament / Line | #D7CCC8 / #BCAAA4 | Tone-on-tone ornaments (at 15–30%), hairlines, leaders |
| Ink / Ink soft | #3E2723 / #6D4C41 | Body text / labels and secondary text |
| Band / Band pattern | #2F5597 / #3F6EC1 | Header bands, ribbons, name plates (pattern at ≤15%) |
| Band text | #FAFAFA | Text on bands |
| Select / Select edge | #A9C7F5 / #3F6EC1 | Selected-row glow, focus |
| Accent | #E5B76A | Sparingly: active tab diamond, clock ring fill, quill tip. Flat, never metallic |
| Success / Warning / Danger / Critical | #43A047 / #F59A4B / #E15A5A / #B63A3A | Status (always with an icon or word) |
| Info / Rare / Disabled | #3F6EC1 / #9575CD / #9E9E9E | Info, rare finds, locked items |
| Battle: Guild / enemy banner | #2F5597 / #B63A3A | Battle cards |

Contrast: Ink on Surface is about 13:1; Band text on Band about 7:1; Ink soft on Surface about 7:1, all above the 4.5:1 rule. HUD plates over the world use Surface at 90% opacity.

### 2.4 Type

Locked by the owner on 2026-09-28 after the v5 font specimen (pairing C), and written into GDD 2.5:
- **Headings, ribbons, names:** Cormorant Garamond SemiBold.
- **Body text and all numbers:** Alegreya (the serif), with **lining figures** (OpenType `lnum`); 0 and o, 8 and S stay distinct.
- **Card header titles:** ALL CAPS ("ADVENTURER DOSSIER"). Section headings and names stay in title case.
- **Battle names:** Pixelify Sans only.

All are OFL. Godot sets `lnum` through a `FontVariation`'s OpenType features.

### 2.5 Readability rules (from Dragon Quest XI)

At the 1920×1080 reference resolution:
1. **Ornament stays on frames, headers and ribbons.** Data regions (rows, tables, text) are plain parchment with Ink text. No texture under numbers.
2. **Minimum sizes:** body 22 px, numbers in tables 24 px, headers 28 px, help ribbon 22 px. The GDD's readable-scale setting (16b) scales everything from these.
3. **Contrast** at least 4.5:1 for text, including disabled text.
4. **One primary action per card,** placed bottom right, labelled with a verb ("Dispatch", "List", "Pay").
5. **At most about 8 rows visible** in a list before scrolling; show the scroll position.
6. **Icons get a label** on first appearance on a screen, and a tooltip everywhere.
7. **Numbers are right-aligned** in columns, with the unit (G, %, h) after the number.

### 2.6 Motion

Short and quiet: cards slide in 8 px and fade over 0.15 s; the selected row's glow eases over 0.1 s; results banners sweep in over 0.3 s. Reduced-motion (GDD 16b) turns slides into fades. Nothing blocks input while it animates.

## 3. Faces and portraits

Owner rules, 2026-09-28:

| Where | What is shown |
|---|---|
| **Dialogue** | **Waist-length portraits**, not face crops. The Commander on the left, the speaker on the right (FGC_07 §12.4). |
| **Small face slots** for adventurers and staff (rosters, allies, reports, results) | Their **idle-left pixel sprite** in a small frame, scaled by a whole number with nearest-neighbour filtering. No painted portraits are needed. |
| **Small face slots** for officers | A face crop of their approved painted portrait. |
| **Important NPC profile** (officers, the buyers) | The **full portrait uncropped on the left** of the profile screen; the details on the right use the space the portrait leaves. |
| **Eurydica NPCs without portraits** | The name only (Scene Script Format). |
| **Monsters** | Their approved battle still, left-facing, in the same small frame. |

**Why sprites:** the adventurer portraits so far looked generic. The officers' portraits work because the owner supplied face references. Painted adventurer portraits would need the portrait skill refined first; this rule removes that dependency. If painted adventurer portraits are wanted later, `$imc-portrait-art-direction` must be improved first (tracked in §9).

**The face frame:** one small frame asset (§7) holds either a sprite or a portrait crop. It is the same size everywhere, so rows line up whether they show a pixel sprite or a painted face.

## 4. Screen inventory

The full inventory is in [`FGC_08 UI screens/screen-inventory.md`](FGC_08%20UI%20screens/screen-inventory.md), with the same data as JSON in `inventory-data.json`. Codex wrote it from the GDD, FGC_07, the scene format, the sprint plan and the owner's screenshots; Claude reviewed it on 2026-09-28.

It contains:
- **A. Navigation map:** how the player reaches each screen, and where Back returns.
- **B. 102 entries** (screens, overlays and HUD elements). Each has the same fields: ID, owner officer, GDD refs, sprint, entry and return, clock behaviour, the data shown with its source, actions with proposed command names, empty/loading/blocked/error states, face and portrait slots, the Three Houses pattern it follows, input, and gaps.
- **C. 69 shared components:** the basis of the asset kit in §7.
- **D. Build order** by sprint, plus the **gap register** (26 items).

**How to read it:** the GDD and FGC_07 remain the authority. Command names and input bindings marked "proposed" are proposals. Where the inventory records a gap, nothing was invented to fill it.

**Review notes (Claude):**
- The entries follow the GDD closely. The review caught one error in this document's first draft (the battle HUD, now fixed in §5.7), not in the inventory.
- **Three gaps are real conflicts between documents** and need a decision; they are listed in §9 (P6–P8).

## 5. Layouts of the key screens

Reference 1920×1080. Wireframes show layout, not art.

### 5.1 World HUD (the town, HQ and interiors)

```
+--------------------------------------------------------------------------------+
| (clock medallion)  [purse 2,500 G | Rep 0 | Morale 60 | Rank F]      (minimap)  |
|   day 3 · 14:20     [ || 1x 2x 4x ]                                             |
| [scroll] Objective: Meet Mae at the tavern                                      |
| [pin] Boarhide Vest for Anselm                                                  |
| [!] Alert: Operation returned                    (world)                        |
|                                                                                 |
|                          [E] Talk   (world-space prompt)                         |
|                                                                                 |
|                                                        [Tab] Ongoing  [Esc] Ledger|
+--------------------------------------------------------------------------------+
```

- **Top left:** the clock medallion (G11), and beside it the plate with the purse, Reputation, Morale and Rank, plus the speed controls and the battle-pace chip. Together they carry every field of GDD 15's "Top bar". This replaces the full-width top bar (P1, approved).
- **Under it:** objectives and pins (G12), then alerts as toasts sliding in from the left (G12; GDD 15 Alerts). A click or `interact` opens the object.
- **Top right:** the minimap (FGC_07 §12.2), hidden during dialogue.
- **Bottom right:** button hints.

### 5.2 Dialogue view

```
+--------------------------------------------------------------------------------+
|                                                                                 |
|  +----------+                                                  +----------+     |
|  |          |                 (diorama, camera eased in)       |          |     |
|  | Commander|                                                  |  Speaker |     |
|  | waist-up |                                                  |  waist-up|     |
|  | (dimmed) |                                                  |          |     |
|  +----------+                                                  +----------+     |
|        [ Mae ]  <- name plate (ornate end)                                      |
|   +------------------------------------------------------------------------+   |
|   | "Fast as usual."                                                   (v)  |   |
|   +------------------------------------------------------------------------+   |
|                                                          [Log]  [Auto]  [Skip]  |
+--------------------------------------------------------------------------------+
```

- The portraits stand at the sides, waist length, and overlap the text box's top edge a little. The non-speaker dims to 55% (FGC_07 §12.4).
- The name plate has one ornate end, like Three Houses. Narration uses a centred box with no name plate; thoughts are italic in parentheses.
- Choices appear as a vertical stack of parchment buttons above the text box, with the quill cursor.

### 5.3 List + detail (Roster, Processing queue, Commerce stock, Recruitment)

```
+--------------------------------------------------------------------------------+
| \ Roster \      (Elsie)                                                          |
|  [ All ][ Hunters ][ Scouts ]  <-tabs->                                          |
|  +------------------------------------+   +-----------------------------------+  |
|  | Name          | HP      | Stamina  |   | [face] Anselm Voigt     Rank C    |  |
|  |[f] Anselm ....| 180/180 | ■■■□     |   | passive, reach, state             |  |
|  |[f] Nell   ....| 120/140 | ■■□□     |   | stats with bars                   |  |
|  |[f] Severa ....|  90/150 | ■□□□  !  |   | equipment / backpack              |  |
|  |  ...          |         |          |   |                                   |  |
|  +------------------------------------+   +-----------------------------------+  |
|        ~~~~~~~~ Rest restores all four stamina bars. ~~~~~~~~   [X] Rest  [B] Back|
+--------------------------------------------------------------------------------+
```

### 5.4 Card pair (Request Board, contract, flashpoint)

Following the owner's "Request" screenshot: the **client card on the left** (the client's portrait or name, status stamp such as ACCEPTED, and the brief), and the **terms card on the right** (title, client, description, a reward table with icons and quantities, the deadline, and the owned/listed/reserved goods). The primary action (Accept, Deliver) sits at the bottom right of the terms card.

### 5.5 Preparation (Elsie)

```
+--------------------------------------------------------------------------------+
| \ Preparation \  (Elsie)             template: [ Hylaea hunt ▾ ]                  |
|  +---------------- formation ----------------+  +----------- forecast --------+  |
|  |  BACK   [f]      [f]      [ + ]           |  | duration, return, cutoff    |  |
|  |  FRONT  [f]      [f]      [f]             |  | stamina before -> after     |  |
|  +-------------------------------------------+  | risk 5% / 25% bands          |  |
|  +------------- selected member --------------+  | consumables                 |  |
|  | stats, reach, passive, backpack grid       |  +-----------------------------+  |
|  +-------------------------------------------+                  [A] Dispatch     |
+--------------------------------------------------------------------------------+
```

Two rows of three slots, at most five people (GDD 15). The face slots show idle-left sprites.

### 5.6 Results banner (minigames, rank, highlights)

The full-width Band (G13): the grade letter or word in large Band-text Marcellus (Accent only for S), one line per result (bond points, gold, items, skill progress), and a small parchment card at the bottom left with the faces involved and their progress bars.

### 5.7 Field view battle HUD

GDD §9 "Battle HUD" as changed on 2026-09-28: the party is a **column of cards on the right**, following the owner's Star Ocean: The Second Story R reference, so five members never cover the fight.

```
+--------------------------------------------------------------------------------+
| (clock + speed)          [Forest Wolf ████░░]  [Dire Boar ██████] RARE          |
| Hylaea · target: Boar                                  +---------------------+   |
| time left 1h 12m                                       |(bust) Anselm  FRONT |   |
| corpses: 2                                             | 180 ████████  SKILL |   |
|                                                        +---------------------+   |
|                     (the fight in the diorama)         |(bust) Nell          |   |
|                                                        | 120 ██████          |   |
|                                                        +---------------------+   |
|  +--------------------+                                |  ... up to 5 cards  |   |
|  | battle log         |                                +---------------------+   |
|  | Anselm hits Boar 16|                                                          |
|  +--------------------+                              [Leave view]  [Recall]     |
+--------------------------------------------------------------------------------+
```

- **Party cards** down the right edge, one per member, semi-transparent (the Band-coloured card at about 70% opacity, text fully opaque). Like Three Houses' battle cards, they may lean a few degrees in perspective. Each card has:
  - a round bust (face and shoulders from the front idle sprite), ringed by the **gold attack timer** (Accent) filling clockwise;
  - the name, a large HP number and HP bar, status effects above the name, and FRONT or BACK;
  - the **orange skill meter** (0–100) along the card's lower edge, glowing with SKILL at full. Never blue: that reads as MP. There is no turn-order bar.
- **The acting member's card** slides out a little and brightens; the target's card flashes on a hit.
- **Enemy HP** at the top centre, one bar per enemy, with a RARE badge where it applies.
- **Top left, under the clock cluster:** the place and target, time left and secured corpses.
- **Bottom left:** the battle log.
- **Buttons:** Leave view and Recall, bottom right. The clock and speed controls stay visible.
- **In the world:** damage numbers pop at body height with stacked hits offset, plus the skill-name banner at the top centre, as in the reference.

### 5.8 The Guild ledger (main menu)

An open ledger book on the right half of the screen, with the world visible on the left (G10). The left page shows the Guild name, the chapter and the purse. The right page lists Ongoing, Roster, Storage, Requests, Bonds, Journal, Save and Settings.

The owner's reference for this screen is mainly **how the list and its selection look**:
- **Rows:** each entry is centred Marcellus text on a ruled line, Ink colour.
- **Hover/focus:** a soft ink-wash stroke (Select at about 35%) sweeps in behind the entry over 0.1 s, like a brush highlight, and the entry text turns Band colour and slightly larger.
- **Selected (pressed):** the stroke becomes solid Select with a Select-edge hairline, the text stays Ink, and the quill cursor touches the entry's left end.
- **News:** a small red-ink exclamation mark in the margin beside entries with news.
- **Disabled:** Disabled grey text; the help ribbon says why.

### 5.9 Region map *(structure decided and look approved by the owner, 2026-09-29)*

**Approved look:** `UI Kit/Approved Region Map v1/` (mockups A/B/C, the painted map, discovery overlays, previews). S5 builds from it. **Owner refinements for the Godot build:**
1. Elsie's corner in Atelier Ryza's style: the portrait in a white semi-transparent circle with a thin border; the dialogue box white and semi-transparent with a thicker border.
2. A thin border on the map and detail cards, or rounded corners.
3. Instead of the flat navy background, a semi-transparent horizontal gradient: low-opacity navy (or white) at the left and right edges, transparent in the middle, so the world shows through. This relaxes G1's full-screen takeover for this screen.
4. The help ribbon gets the header pattern and a thin border, like the key-hint plates.

**Decided:**
- **The Frontier may have several regions.** Regions are **tabs** across the top of the map card, not a zoom from a world map into a region (the owner, after Strange Brigade). In Eurydica the one tab ("Eurydica") acts as the card's title. After the move to the Frontier, Eurydica's areas can't be selected (GDD 16a), so the tabs list Frontier regions only.
- The flow stays **Region map → Area detail → Hunt, Scout or Contract** (the screen inventory's `ui_region_map` and `ui_area_detail`).

**Proposed layout** (built from the references in `Research/Region Map/`; see the owner's notes and Claude's comparison in the chat of 2026-09-29):

```
+--[ Eurydica ]--[ (Frontier regions later) ]------------------------------+
|                                               |  +---------------------+ |
|   PAINTED PARCHMENT MAP (Tier 2 map frame)    |  | ENVIRONMENT PREVIEW | |
|                                               |  | (the area's battle  | |
|   South Gate --- road --->  (o) Hylaea F  42% |  |  backdrop, cropped) | |
|                             (o) Bernmoor E    |  +---------------------+ |
|                             (lock) Erythra D  |  | HYLAEA FOREST       | |
|   landmarks and dens appear on the map as     |  | Rank F  Explored 42%| |
|   ink drawings when discovered (fog = blank   |  | [====------]        | |
|   parchment)                                  |  | Species 2/3  Dens 1 | |
|                                               |  | Rare lead: -        | |
|  (Elsie)  "The boars are thick near the       |  | [Hunt][Scout][Contr]| |
|  portrait  South Gate this week."             |  +---------------------+ |
+--------------------------------------------------------------------------+
```

- **The map card (from Strange Brigade and Atelier Ryza):** a painted, hand-drawn map on parchment, with small painted vignettes for each area (forest, reedbeds, stone ridges) and the city at one edge. Each area has a marker with its name and an **exploration ring**; a locked area shows its rank. **Discovery draws in:** landmarks, dens and paths stay blank parchment until found, then appear as ink drawings. This makes GDD 7.2's exploration visible on the map itself.
- **The detail card on the right (from Strange Brigade's card, with the Hyrule Warriors and Infinity Strash preview):** a Tier 2 paper card with the area's **environment preview** at the top (the area's idle-battle backdrop, so no extra painting is needed). Below it: name, rank, the **exploration % bar** (where Strange Brigade shows the stage progress dots), species identified, dens found, any rare lead, then the Hunt, Scout and Contract buttons.
- **Elsie at the bottom left (from Atelier Ryza, and Metaphor's corner card):** her small portrait with one line of advice drawn from the forecast or the discoveries. It follows the portrait rules in §3.
- **Not taken:** Metaphor's slanted brush-stroke style and red slashes (too loud for the Three Houses tiers); Infinity Strash's modern blue panels and cartoon cutouts; Hyrule Warriors' dark tech frame; Three Houses' political map (it names kingdoms, not a few areas to explore).

## 6. Layer and pause rules

Unchanged from FGC_07 §12.2 and §04: HUD on layer 20, screens on 30, dialogue on 40. Every management screen pauses the clock (GDD 4). The world HUD's clock medallion shows a small pause mark whenever the clock is paused.

## 7. The painted asset kit

**Approved and installed 2026-09-28:** `UI Kit/Approved v1/` (427 pieces, 62 icons, 11 emotes, `kit.json`, six proof mockups). The list below was its brief.

The inventory's 69 components split into what Codex paints and what the engine draws. Codex paints in one finish, described in words from §2 (no Three Houses images), directly as Codex tasks; the owner reviews the results, not prompts.

**Painted (Codex), stretchable frames unless noted:**

| Group | Pieces |
|---|---|
| Frames | Surface card (2 border weights), Band header band with icon slot, title ribbon (G2), help ribbon with star ends (G8), confirm card, tooltip card, toast card |
| Rows and focus | Selected-row glow band, quill cursor (small sprite), dotted leader, tab bar with diamond separators and active diamond |
| Buttons | Primary and secondary buttons in 5 states (idle, hover/focus, pressed, disabled, selected); choice button; button-hint tab with glyph plate |
| HUD | Clock medallion wreath with a fill ring (G11), stat plate, speed buttons, battle-pace chip, minimap ring, objective scroll icon, alert severity icons |
| Portrait frames | Small face frame (sprite or crop), round battle bust frame with the gold timer ring and orange skill meter tracks, waist-length dialogue plate edges, name plate with one ornate end, full-portrait dossier frame |
| Special screens | Guild ledger book (open, two pages), results banner, parchment map frame, request status stamps (ACCEPTED, COMPLETE, EXPIRED) |
| Icons (about 40, one sheet) | Gold, Reputation, Morale, Rank, time, stamina, HP, quality grades, monster tiers, item categories, the five officers' departments, the four Commander skills, status effects, locks, alerts |
| Emotes | The 11 emotes in the scene format |

**Engine-drawn (code):** text, numbers, bars and their fills, the stamina bars, grids (backpack, Fitting), the minigame puzzle surfaces, charts, the battle log text and all layout.

**Everything decorative follows §2.2:** flat, tone-on-tone, no texture, bevel or metallic gold. Ornaments ship as white alpha masks that the engine tints and fades. The first Codex job is the **style test** (the world HUD and the Roster screen, painted in one or two versions of the §2 finish). The full kit follows once the owner picks.

## 8. Implementation notes

- **One Godot `Theme`** (`ui_theme.tres`, FGC_07 §12.1) holds every stretchable frame (as `StyleBoxTexture`), the fonts and the colour tokens. Screens never set colours or fonts directly.
- **Face frames** use a `TextureRect` with nearest-neighbour filtering for sprites and linear filtering for portrait crops, inside the same frame asset.
- **Battle labels** use `Sprite3D`/`Label3D` billboards or a `SubViewport` per label, set to render on top, on layer 10.

## 9. Open items and proposed GDD changes

| # | Item | Status |
|---|---|---|
| P1 | Regroup GDD 15's "Top bar" into the top-left clock-medallion cluster (same fields) | **Approved** by the owner, 2026-09-28; applied to GDD §15 |
| P2 | The Guild ledger as the main menu, with the list and selection styling in §5.8 | **Approved** by the owner, 2026-09-28 |
| P3 | Idle-left sprites in small face slots for adventurers and staff | Owner rule, 2026-09-28 |
| P4 | Refine `$imc-portrait-art-direction` before any painted adventurer portraits | Deferred; not needed while P3 holds |
| P5 | Battle cards: the party as a semi-transparent card column on the right (Star Ocean reference), replacing the bottom row; the battle log moves to the bottom left | **Approved** by the owner, 2026-09-28; applied to GDD §9 and §5.7. The per-action cards in the world were dropped in favour of the column. |
| P6 | **Inventory G10, GDD conflict:** processing quality odds (§12.1, §15) versus the rank-3 ability Trained eye (§5a.2) | **Decided** by the owner: the odds stay visible, and **Trained eye** becomes a passive (no Unsellable from processing; that chance moves to Damaged). Applied to GDD §5a.2 and §5.4. |
| P7 | **Inventory G11, spec conflict:** the field view returned to `world` in FGC_07 §04, but GDD §15 says screens return to their previous context | **Approved** 2026-09-28: follow the GDD; FGC_07 §04 updated |
| P8 | **Inventory G25, sprint-plan conflict:** FGC_09 S8 said every session grades D–S, but Fitting has no D | **Approved** 2026-09-28: follow the GDD; FGC_09 S8 updated |
| P9 | The FGC watermark emblem for tier-2 cards and the ledger | **Decided** by the owner, 2026-09-28: `Research/Watermark.png` (wings, a star and a ring), recoloured black or Ink at low opacity so it shows on parchment |
| P10 | Icon set: gold, Reputation, Morale, a rank badge, time, the alert severities, objective and pin, stamina, HP, quality grades, departments | Required; first icons drawn in the v4 test |
| — | The other 23 gaps in the inventory's gap register are unauthored details (name-entry rules, backlog, settings ranges, minigame tuning), each assigned to the sprint that builds the screen | Tracked in the inventory |
