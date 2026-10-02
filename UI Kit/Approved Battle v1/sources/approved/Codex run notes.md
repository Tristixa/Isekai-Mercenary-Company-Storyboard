# FGC UI kit v1

**Candidates, not approved.** Complete artwork delivery based on the owner's approved v5 finish and Font C. No game integration. All task outputs are inside this run, apart from `handoff/ui-kit-v1-last.txt`.

Open [review.html](review.html) for the six proof screens and component sheets. Open PNGs at 100% to judge small glyphs.

## Contents

| Folder | Treatment and contents |
|---|---|
| `kit/tier1/` | Short/long painted v5 title ribbons, neutral laurel clock, separate clock ring, open two-page ledger, five brush-highlight states, one-ended dialogue nameplate, results banner, row strip and S/A/B/C/D grade glyphs. |
| `kit/tier2/` | Two frame weights; header and medallion; section band; dialogue, client, terms, map, confirm and log frames; flat status stamps; translucent party card, bust/timer/skill/status/row parts; enemy banner, HP parts and RARE badge. |
| `kit/tier3/` | Five black fading toasts, tooltip, help ribbon, objective/pin rows, stat plate, speed and battle-pace strips, minimap ring, advance/pause cues, keyboard/gamepad hint plates and glyphs. Plain surfaces, no stains. |
| `kit/controls/` | 21 controls, each idle, hover/focus, pressed, disabled and selected: buttons, choice, diamond tab, full-row glow, quill, track/fill pairs, stamina, stepper, checkbox, toggle, slider, scrollbar and face backing. Also dotted leader, embossed row divider and 20 independent slider/scrollbar track/thumb state pieces. |
| `kit/icons/` | 62 crafted v5-style glyphs, individually redrawn at 24, 32 and 48 px. Seven larger-letter rank badges. The transparent 48 px atlas and its rectangles are in `kit.json`. |
| `kit/emotes/` | All 11 scene symbols as 64 px painted bubbles; sheet includes 44 px use over a 93 px sprite. |
| `kit/layers/` | Flat paper, eight reused cloud stains, owner watermark and eight white-alpha ornament/pattern masks. |

There are **427 registered PNG pieces**. The atlas is an additional packed export. The six requested sheets are accompanied by `sheets/layers.png` to make the layering contract reviewable. PNG piece filenames use snake_case; the six requested mockup filenames retain the handoff's hyphens.

## Engine contract

`kit.json` is authoritative. Each entry supplies `piece`, `file`, numeric `tier`, `group`, `size`, `margins: [left, top, right, bottom]`, `stretch` and applicable `tint_token`, state and notes. Margins are source pixels, not normalized UVs. Use nine-slice for `stretch: true`, keeping corners fixed. Do not shrink a destination below the sum of its two opposing margins plus one pixel. Fixed-aspect ornaments, icons, emotes, stamps, ring parts and the ledger have zero margins and `stretch: false`. Keep the book's spine intact; its page content rectangles are recorded in its notes.

Card composition, back to front:

1. `paper` in Parchment 100.
2. Seeded `stain_1`–`stain_8` placements, multiply blend at 12–24% to match v5's doubled stain strength.
3. The owner's `watermark`, Ink at 5% opacity.
4. The chosen transparent frame and any header/section bands.
5. Icons, faces, text and controls.

Stains and watermark are not baked into content frames. Standalone pattern/ornament assets are white-alpha masks, with tint tokens in the manifest. The content frame exports include their subdued perimeter ornament treatment; the separate masks support independently tinted or repositioned decorations.

Authored colours use the GDD §2.5 token table, including alpha and blends. Painted v5 ribbon/quill/laurel pixels retain their approved texture and shading rather than being reduced to a flat palette. White mask channels and the explicitly requested black toast/portrait-dimming overlays are technical exceptions; scene artwork and portraits retain their source colours. The abandoned UI-spec palette is not used for new components.

Use Cormorant Garamond SemiBold for headings, ribbons and names; Alegreya serif for body and all numbers. Enable `lnum=1`, `onum=0`. Card headers are ALL CAPS; names and sections stay title case. The handoff's explicit Font C rule for names is used throughout, including the battle proof. Bundled OFL licenses are under `sources/fonts/`.

State imagery is distinct in all five states. Hover is also keyboard/controller focus. Keep disabled labels fully opaque Ink on parchment; do not multiply down the entire control including its label. For dark active controls use Parchment text. Bars and stepper values remain engine data. Clip fills by progress, hiding them at zero rather than squeezing their endcaps. For full control resizing, move slider/scrollbar thumbs and stepper subparts according to live values; the provided complete states are visual examples, not behavior scripts.

Battle cards use Navy 800 at 70% opacity. Draw text at full opacity. Clip the Gold 400 attack ring clockwise from twelve o'clock; the separate Warning-coloured orange meter maps 0–100 along the lower edge. Show SKILL at 100. Busts and rings remain round. FRONT/BACK, statuses and HP remain separate. Party cards belong on the right; log belongs bottom left. No turn-order strip or blue MP meter.

The black toast fades only after the text-safe region; keep text between the icon and the final 135 px fade cap. Transparent speed controls use a 3 px Navy 950 text keyline. Painted title text uses a 2 px Navy keyline to remain readable over the diagonal edge. Give icons their source label on first appearance and tooltips in the game.

## Proof content and provenance

| Mockup | Source-grounded content |
|---|---|
| `mock-dialogue.png` | Scene 2, Mae (Happy): “Fast as usual.” Commander left at 55% brightness, Mae right; waist-length crops from `Characters/Officers/`. A close crop of the approved tavern concept excludes its annotation labels. |
| `mock-battle.png` | Four named starters and their GDD maximum HP; front-idle bust sources, gold timers, orange meters, ordinary Forest Wolf and Dire Boar on the left, left-facing party on the right and bottom-left log. Clean approved Hylaea layer artwork, not a baked HUD screenshot. |
| `mock-ledger.png` | Book on the right; Your Guild, Chapter 1 / New Beginning, purse; eight entries, selected Roster, hovered Requests, Ongoing news mark and quill. |
| `mock-request.png` | GDD CH1-REQ-003, Rare Slime Order: 2 Slime Cores, any condition; 25 G / 100 Rep; two-day deadline from first appearance. Portraitless original trader uses name only. |
| `roster.png` | V5's four starters, Font C, caps card headings, separate layers, enlarged F badge and full-row selection. |
| `world-hud.png` | V5 world and clock/stat/objective cluster; new rank badge and Font C. |

Transient HP, elapsed time, inventory counts, log events and selection states are **layout fixtures**, not claimed simulation output or new GDD rules. The request's quantity and reward are canonical. Its due Day 5 / 14:20 date assumes first appearance at the proof's Day 3 / 14:20; the timer begins on appearance, including while Offered, never on acceptance. Severa's front-facing source is named `Base Sprite - Native.png`; Nell's front export is reduced to its display grid, while Anselm and Otto already have native front files. Sprite enlargements in face slots use integer scaling and nearest-neighbour sampling. Three Houses screenshots were neither attached nor copied.

`sources/provenance.json` records the original paths, local copies and SHA-256 hashes for 42 image inputs. The v5 Canvas composition/design sources and the relocated v5 DevTools renderer are retained for inspection. The authored extension is `sources/kit.js`; new UI artwork is native Canvas construction using those original masks and textures. No remote generation was needed.

## Reproduction and checks

From `D:/Codex/IMC`:

```powershell
node runs/ui-kit-v1/sources/build.mjs
node runs/ui-kit-v1/sources/verify.mjs
```

Requires Node 22+ and installed Chrome. The builder reads the named source folders and writes only into this run. Chrome profiles are also placed in this run. Fonts, source copies and scripts are bundled; no package installation or online service is needed.

`sources/verification.json` records completeness, all 105 distinct control states, icon dimensions, eleven white-alpha masks (eight ornaments and three request stamps), six 1920×1080 proofs, font loading, actual source hashes and **143 pixel-comparison nine-slice tests**. The verifier rejects a deliberately missing required piece before accepting the complete manifest. Text in proofs is at least 22 px; numbers use Alegreya. Pixel-sampled text backgrounds pass 4.5:1; outlined transparent text uses its explicit dark keyline as the contrast surface. Visual review also covers hierarchy, 24 px rank readability, state sheets, portraits and the right-side battle layout.

No requested piece is omitted. These are artwork candidates for owner review. Static checks do not constitute Godot integration or prove live scaling, navigation, animation, data binding or localization behavior.

## Fixes 2026-09-28

- Battle: party stands on the right facing left, beside the right-hand cards; ordinary Forest Wolf and Dire Boar stand on the left. RARE remains on the tier-2 sheet.
- Ledger: the player-named guild uses the placeholder **Your Guild**; the selected entry has a softer, less saturated ink wash, stronger than hover.
- Icons: stun uses a dazed spiral, leadership a raised banner and ongoing a signpost. All three sizes, the atlas, its manifest rectangles and the icon sheet were regenerated; insight/information and negotiation/commerce are unchanged.
- Request stamps: ACCEPTED and COMPLETE use Ink; EXPIRED uses Danger. PNGs are white-alpha masks with slightly rotated outlines and sparse ink gaps; tint once with the manifest token. The request mockup and tier-2 sheet show tinted examples.
- Verification: coverage, contrast and all 143 corner checks pass; minimum proof text contrast is 5.22:1. The supplementary check compares every atlas cell and checks replacement backups and unchanged assets. Run it with `node runs/ui-kit-v1/sources/verify-review-fixes.mjs`. Original replaced files are retained under `superseded/before-fixes-2026-09-28/`; the intermediate wash revision is under `superseded/fix-pass-1/`.

- Round 2: Roster selection now uses a soft 48% Blue select wash, darker and more saturated than the unchanged hover; FRONT fighters form a top-left to bottom-right diagonal nearest the enemies, with Nell (BACK) behind them to the right. Replaced files are backed up under `superseded/round2/`.
