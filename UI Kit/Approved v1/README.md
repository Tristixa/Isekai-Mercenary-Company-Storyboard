# FGC UI kit, approved v1

The owner approved this kit on 2026-09-28, after two rounds of review fixes. It is the painted UI for the Godot build (sprint S5) and the reference for every screen in `Game Design/FGC_08_UI_HUD_Spec.md`.

**Finish:** Fire Emblem: Three Houses' structure, described in words (no Three Houses assets were used or copied), in FGC's own pieces. It follows FGC_08 §2.2's three tiers:
- **Tier 1:** painted identity pieces: the title ribbon, clock medallion, Guild ledger, results banner, dialogue name plate.
- **Tier 2:** content cards: paper with separate stain and watermark layers, and pattern-only frames.
- **Tier 3:** plain, icon-first transient pieces: notifications, tooltips, help ribbon, button hints.

**Colours:** GDD 2.5 tokens (parchment and navy). **Fonts (GDD 2.5):** Cormorant Garamond SemiBold for headings and Alegreya with lining figures for body and numbers; card headers in all caps. **Watermark:** the owner's emblem (`Research/Watermark.png`) in Ink.

## Contents

- `kit/`: 427 pieces in `tier1/`, `tier2/`, `tier3/`, `controls/` (21 controls in five states), `icons/` (62 icons at 24/32/48 px plus an atlas), `emotes/` (11), `layers/` (stains, watermark, pattern masks).
- `kit.json`: every piece's file, tier, size, nine-slice margins, states, tint token and atlas rectangle. The Godot theme is built from it (FGC_07 §12.1).
- `sheets/`: labelled review sheets per group. `mockups/`: six 1920×1080 proofs built only from kit pieces (world HUD, roster, dialogue, battle, ledger, request). `review.html` links them all.
- `sources/` (untouched generated drawings), `prompts.md`, `Codex run notes.md` (checks: 143 nine-slice corner tests, text contrast ≥ 5.22:1, coverage).

**Source run:** `D:/Codex/IMC/runs/ui-kit-v1/` (with `superseded/` holding the pre-fix pieces). The style tests v1–v5 that led here are in `D:/Codex/IMC/runs/ui-style-test*/`.

**The mockups' character sprites are stand-ins, not approvals.** The approval on 2026-09-28 covers the kit pieces only. The characters in `mockups/` (for example Anselm, Nell, Severa and Otto in `mock-battle.png`) are outdated sprites placed only to show the layout; their designs and proportions do not match the approved sprites. The approved sprites are in `Character Sprites/`.

**Known limits:** the mockups are flat compositions. The battle mockup's depth is only indicative, since the real stage is 3D (FGC_07 §11 has the formation rule). Localized changes later touch only the piece concerned.
