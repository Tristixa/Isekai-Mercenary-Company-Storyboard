# FGC UI kit, battle addition v1 (approved)

The owner approved this set on 2026-10-02. It adds the battle HUD pieces to the approved kit (`../Approved v1/`), in the same v5 finish, and follows GDD §9.4 and FGC_08 §5.7 as changed on 2026-10-02.

## What it is

- **Ring timeline** (Grandia 3 style, use size 240 px): `tl_bezel`, `tl_track_enemy` (outer, crimson) and `tl_track_party` (inner, blue), each with 24 white ticks (one every 15°, longer every 30°), `tl_divider`, `tl_act_zone` (the gilded 300–360° ACT section), `tl_act_plate`, `tl_pointer`, `tl_hub` (the NEXT medallion with a 60 px bust opening), `tl_marker_party` (bright blue rim) and `tl_marker_enemy` (bright red rim), their `_glow` masks for the acting highlight, and `tl_flag_skill`.
- **Party gauge** (Kingdom Hearts style, use size 104 px): `gauge_frame` (70 px bust opening), `gauge_hp_track` (270°), `gauge_skill_track` (thin outer arc) and `gauge_skill_ready`.

All pieces are blank: the engine writes ACT, NEXT and SKILL and draws the HP and skill fills (HP green, yellow below 50%; skill orange, glowing when full). The ring layers share one centre; the game rotates `tl_act_zone`, `tl_act_plate` and `tl_pointer` to the ACT angle.

## Files

- `kit/battle/<piece>.png` at 2× and `<piece>@1x.png` (17 pieces, 34 files).
- `kit-battle.json`: the same entry schema as `../Approved v1/kit.json`.
- `sheets/battle-ring.png`: every piece on parchment and on navy, labelled. `mockups/battle-ring.png`: the approved screen built with the pieces (the characters and background are stand-ins).
- `sources/`, `prompts.md`, `Codex run notes.md` (checks and the v1b tick and v1c ACT plate / hub revisions).

**Source run:** `D:/Codex/IMC/runs/ui-battle-ring-v1/` (`history/` holds the 60-tick tracks and the first hub). The layout mockup is `D:/Codex/IMC/runs/battle-ui-mockup-v2/`.
