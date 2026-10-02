# Battle ring and party gauges — v1 candidates

[Battle proof](mockups/battle-ring.png) · [Component sheet](sheets/battle-ring.png) · [Manifest](kit-battle.json)

17 components, each supplied as a transparent 2× PNG and `@1x.png`. These extend the approved v5 Canvas kit; they await owner artwork approval. No game integration was performed. Piece exports have no text or emblems. Sheet labels and proof text are separate.

The manifest preserves the approved entry fields: `piece`, `file`, numeric `tier`, `group`, `size`, source-pixel `margins`, `stretch`, applicable `tint_token`, and `notes`. Additional `file_1x`, `use_size`, `scale` and source-pixel `anchor` fields make resolution explicit. All pieces are fixed-aspect with zero margins and `stretch: false`.

## Assembly

All eight timeline layers are 480×480 source / 240×240 display. Stack their centers at [240,240] source / [120,120] display; retain transparent padding, including the pointer and hub. Angles increase clockwise from twelve o'clock. Enemy track radius is 100px, party track 71px. Each has 24 aligned white ticks, spaced every 15 degrees from the top; twelve longer, brighter ticks fall every 30 degrees. Use a separate navy backing if desired, then bezel, tracks, divider, ACT section, hub and pointer. The opaque ACT section covers 300–360 degrees; rotate around the common center. Portraits sit behind their frames. Hub bust diameter is 60px; its NEXT text area is [106,152,28,12] display pixels.

Marker frames and glow masks are 96×96 source / 48×48 display with a common center [24,24] display. Bust openings are 34px diameter. Tint white acting masks once using their token; place behind the rim. The red flag's attachment point is [20,15] display, text-safe rectangle [5,3,30,9].

Gauge frame and both tracks are 208×208 source / 104×104 display, center [52,52] display, bust opening 70px diameter. HP radius 41px and width 9px; skill radius 49px and width 3px. Start at 225 degrees clockwise from twelve and sweep 270 degrees, ending at 135 degrees. This is the reference HTML's 135-degree start in Canvas's east-origin convention. Draw bust, empty tracks, clipped engine fills, then frame/end caps. Fills are hidden at zero and clipped by angle rather than scaled. HP is green, yellow below 50%; skill is orange, glowing when full. The blank ready tab has [7,4,34,10] text-safe space.

The mockup retains the original 1280×720 layout and fixture imagery. The handoff's explicit 240px ring replaces the reference's 210px placeholder while keeping left 20px / bottom 16px. Party gauges retain 104px size and right 22px / top 84px. Fonts are the approved bundled Heading/Body fonts; the original HTML's font-family alias is mapped to Alegreya. Engine labels appear only in the proof.

## Reproduce and verify

From this run directory, with Node and Chrome installed:

```powershell
node sources/revise-v1c.mjs
node sources/verify.mjs
node sources/verify-delivery.mjs
```

The copied Chrome DevTools helper writes profiles only inside this run. `sources/provenance.json` hashes all preserved inputs; `sources/generated/` holds untouched native Canvas exports, with drawing instructions in `prompts.md`. Verification measures PNG dimensions, alpha, concentric bounds, white tick counts and long-tick counts, portrait openings, white-alpha masks, ACT placement, gauge sweeps, proof placement and retained-source hashes. The asset checker also rejects a deliberately incomplete manifest. Visual review uses the labelled parchment/navy sheet and the actual-size rebuilt proof. Static artwork checks do not prove Godot integration or runtime behavior.

## v1b revision

Reduced only `tl_track_enemy` and `tl_track_party` to 24 ticks (12 long + 12 short), preserving their colours, bevel, size and centre. Original 2? and @1x track PNGs are retained in `history/v1-60-ticks/`. All other component exports are unchanged. The component sheet and battle proof were re-rendered. Revision checks are recorded in `sources/revision-verification.json`.

## v1c revision

Added blank `tl_act_plate` aligned to the ACT zone on the common 480x480 source canvas. Its use-size center is [77.25,45.955], radius 85.5 at 330 degrees, midway across the tracks. The 36x18px plate is rotated -30 degrees; its local text-safe area is [-14,-6,28,12]. The mockup draws ACT at 12px in Cormorant Garamond SemiBold and removes the old bezel-edge label.

Repainted only `tl_hub`: richer gilding, the existing bezel flourish at four diagonal positions, quarter-point studs, deeper navy and an inner bevel. The portrait opening remains 60px at [120,120]. A matching blank 36x16px NEXT plate sits at [120,158]; proof-only NEXT uses 11px Cormorant Garamond SemiBold. Exports contain no lettering or emblems.

Both v1b hub PNGs were copied before replacement to `history/v1b-hub/`; its baseline records all previous component hashes. All 45 non-hub component files, including both 24-tick tracks, remain byte-identical. The sheet now has five rows (2080x2030) for 17 pieces; the proof remains 1280x720. Native Canvas sources supply the finish deterministically. Verification is in `sources/revision-v1c-verification.json`, `sources/verification.json`, and `sources/delivery-verification.json`.
