# Gemini prompts: adventurer and staff sprites, v2 (officer proportions)

Written 2026-09-28. **Why v2:** the approved adventurer sprites don't match the officers. They stand about 12% taller (102–106 px vs 93–95), with smaller heads (a quarter of their height instead of a third), longer legs and smaller eyes (evidence: `D:/Codex/IMC/Cast Comparison 2026-09-28/`). The owner is regenerating them in Gemini at the officers' proportions. The officers' sheets were made the same way, so they are the reference.

Everything in `Gemini Sprite Prompts.md` still applies (8×8 blocks, flat key colour, the cleaning pipeline, Omniflash with **Start frame**). This file only replaces the sheet prompt and adds the new poses and videos.

## Attach every time (references are mandatory)

| Role | File |
|---|---|
| **Style and proportion** (head size, eyes, outline, pixel size, height) | `Character Sprites/Officers/Elsie/Reference Sheet.png` for women, `Character Sprites/Officers/Commander/Reference Sheet.png` for men. Add `Tristitia/Reference Sheet.png` as a second style reference if Gemini accepts three images. |
| **Design** (costume, palette, equipment, hair only) | Adventurers: their approved `Idle Front.png` from `Character Sprites/Recruitable Staff/Adventurers/<Name>/`, plus their portrait if they have one (`Characters/Staff/<Name>/Portrait.png`). Staff: no approved art yet, so the design is described in words (below). |

Say in the prompt which image plays which role. Gemini must take the **proportions and face style from the officer sheet** and **only the costume and colours** from the design image.

## Target heights

The game scale is 93 art px for 168 cm (Tristitia). Keep height differences deliberate:

| Character | Height | Target sprite height |
|---|---|---|
| Anselm Voigt | about 180 cm (young, armoured) | about 98 px |
| Nell Larkin | 165 cm | about 91 px |
| Severa Kaltenbach | 176 cm | about 97 px |
| Otto Grimbald | stocky, full plate | about 96 px, the widest of the cast |
| Konrad Metzler | 185 cm, slightly stooped | about 99 px |
| Cassia Susurra | 158 cm, petite | about 87 px |
| Ulrich Esser | 183 cm, broad | about 100 px |

## 1. Base sheet (still image)

```
Pixel-art character sprite sheet of [NAME] for an HD-2D JRPG.

References:
- Image 1 ([Elsie / Commander] reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. [NAME] must look like a member of the same cast as that character.
- Image 2 is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height or face drawing.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about [HEIGHT] art pixels tall from the top of the hair (or helmet) to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: [DESIGN LINE]. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid [KEY COLOUR] filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**Facing right** is the left sprite mirrored in the engine (owner, 2026-09-28, to save cost and effort). Mirroring flips asymmetric details (Anselm's shield arm, Severa's one-sided cape); that is accepted.

## 2. Sleeping pose (adventurers; still image)

Attach the approved base sheet from step 1 as the reference.

```
Pixel-art sprite of [NAME] asleep, matching the attached sprite sheet exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: [SLEEP LINE]. Seen from the same three-quarter game camera as the sheet. Eyes closed. One sprite, centred, on a flat solid [KEY COLOUR] background. No bed, pillow, blanket, floor, shadow, "Z" letters, effects or text.
```

## 3. Battle stance (adventurers; the start frame for the battle video)

```
Pixel-art sprite of [NAME] in a battle stance facing left, matching the attached sprite sheet exactly: same design, colours, face (NO mouth, NO nose), pixel size and proportions. True pixel grid, no anti-aliasing, no mixels. [STANCE LINE]. One sprite, centred, on a flat solid [KEY COLOUR] background, with no shadow, no effects and no text.
```

## 4. Battle reaction stills (adventurers): Getting Hit, Guard, Victory, Defeat

Still images, not video (owner, 2026-09-28, to save cost and effort). Attach the approved battle stance from step 3 as the reference. **All four face screen LEFT**, including Guard: check the head and gaze, torso, feet, and the side the weapon or shield protects. A raised shield on a front-facing body does not count.

```
Pixel-art sprite of [NAME] facing left in a battle pose, matching the attached battle-stance sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: [POSE LINE]. One sprite, centred, on a flat solid [KEY COLOUR] background, with no shadow, no effects, no impact marks and no text.
```

Make the four as separate images.

| Pose | Shared pose line (add the character's line below) |
|---|---|
| **Getting Hit** | recoiling from a blow from the left: upper body knocked back to the right, head turned aside, eyes squeezed shut, weapon arm thrown out of guard, feet still on the ground |
| **Guard** | braced facing left, weight on the back foot, blocking with [GUARD LINE] |
| **Victory** | [VICTORY LINE], relaxed and proud, still turned toward the left |
| **Defeat** | dropped to one knee, head down, one hand on the ground, [DEFEAT LINE] |

| Character | Guard line | Victory line | Defeat line |
|---|---|---|---|
| Anselm | the kite shield held up in front, covering his body, sword ready behind it | sword raised high in his right hand, shield lowered at his side | shield lying flat beside him, sword still gripped |
| Nell | the bow held horizontally across her body, leaning back | bow raised overhead in one hand, the other hand on her hip | bow resting on the ground under her hand |
| Severa | the greatsword held flat and horizontal in front, both hands, blade across her body | greatsword planted point-down in front, both hands on the pommel | greatsword planted beside her, holding it to stay up |
| Otto | the warhammer shaft held horizontally in front with both hands | warhammer resting on his shoulder, free fist on his hip | warhammer head on the ground, both hands on the shaft |

## 5. Videos (Omniflash, one at a time, Start frame)

Use the **Shared rules** block from `Gemini Sprite Prompts.md` at the top of every video prompt, with the character's key colour and outfit lock.

**Walk (everyone): three videos, front, side and back,** with the matching row-2 frame as the start frame, and the walk prompt from `Gemini Sprite Prompts.md` Video 1.

**Battle (adventurers): one 10-second video** from the battle-stance frame:

```
[SHARED RULES]
Starting exactly from the attached frame, the character faces left the whole time, holding [WEAPON]. About 10 seconds:
1. Battle idle (0–3 s): ready stance with a small breathing bounce, looping.
2. Attack (3–6 s): a basic [WEAPON] attack: step in toward the left, strike, recover to the stance.
3. Skill (6–10 s): [SKILL NAME]: [SKILL POSE]. Show only the body motion, with no effects. End back in the battle stance.
```

**Work (HQ staff): one 4-second video each** from the row-1 facing-down frame:

```
[SHARED RULES]
Starting exactly from the attached frame, the character faces down (toward the camera) the whole time. About 4 seconds of [WORK LOOP], a small repeating motion that ends in the same pose it started in, so it loops. Mime the workstation: no table, anvil, board or bench appears; the station is placed in the game.
```

## Fill-ins

### Anselm Voigt (man; key magenta #FF00FF)
- **Design line:** young and enthusiastic; warm golden-blond short messy hair; brown eyes; silver-steel plate armour over a deep-teal surcoat; a medium teal kite shield with a steel rim on his LEFT arm (viewer's right in the front view); an arming sword on his right side. No emblems.
- **Sleep line:** lying on his back, armour on, shield set down beside him, one arm behind his head.
- **Stance line:** shield raised in front at chest height, sword held back and ready, feet planted.
- **Weapon:** arming sword and kite shield. **Skill:** Phalanx: plants his feet and raises the sword crosswise in a guard behind the shield.

### Nell Larkin (woman; key magenta #FF00FF)
- **Design line:** warm brown skin, freckles; very dark brown hair in one long braid over her shoulder; amber eyes; a green hooded capelet (hood down), cream shirt, fitted green tunic and legwear, brown leather jerkin, a bracer on her bow arm, fingerless gloves, light brown boots; a wooden recurve bow on her back and a hip arrow case.
- **Sleep line:** curled on her side, hood up over her head, bow set beside her.
- **Stance line:** bow held forward at the ready, an arrow nocked, half drawn, back straight.
- **Weapon:** recurve bow. **Skill:** Frost Arrow: a longer, deeper draw, a held aim, then the release.

### Severa Kaltenbach (woman; key green #00FF00)
- **Design line:** fair skin; navy-black hair in a neat low bun with a few loose strands; ice-blue eyes; steel half-plate (breastplate, pauldrons, gauntlets) over a dark-blue gambeson; a white and steel-blue tabard with the same pattern as the design image; a short dark-blue cape on one shoulder only; grey trousers, steel-capped boots; a broad plain greatsword shorter than her full height (the blade reaches her chest when planted), carried over her shoulder.
- **Sleep line:** sitting against an unseen wall, knees drawn up, greatsword leaning across her shoulder, head bowed.
- **Stance line:** two-handed greatsword held diagonally in front, point up and slightly forward, feet apart.
- **Weapon:** greatsword. **Skill:** Diving Splitter: a short run-up and leap, then a two-handed downward cleave. Keep the whole blade in frame; never raise it straight overhead.

### Otto Grimbald (man; key green #00FF00)
- **Design line:** full plate armour from head to toe in gunmetal steel with darkened-silver trim and small ochre padding at the joints; a closed German sallet helmet (rounded crown, lowered visor, narrow sight slit, swept neck guard) with a bevor covering the face; a heavy two-handed warhammer with a long wooden shaft and a rectangular iron head; no shield; a wide, planted stance.
- **Sleep line:** sitting on the ground against an unseen wall, helmet and armour still on, the warhammer across his lap.
- **Stance line:** warhammer held diagonally across the body in both hands, head low and forward, feet wide.
- **Weapon:** two-handed warhammer. **Skill:** Hammerfall: raises the hammer high to one side and brings it down in a heavy overhead blow, with a short stagger of follow-through.

*(Confirmed by the owner, 2026-09-28: heavy armour and a two-handed warhammer, no shield.)*

### Konrad Metzler, processor (man; key magenta #FF00FF, since he wears dark green)
- **Design line:** late fifties, very tall, big-framed and slightly stooped; deep brown skin; bald with a neat grey beard and bushy grey eyebrows; a kind, heavy-browed face with a squint; a long off-white butcher's apron with a few old stains over a dark-green work shirt with rolled sleeves; leather forearm guards; a belt of wrapped knives and a cleaver; wooden clogs.
- **Work loop:** sharpening a knife on a hand-held whetstone, then holding a hide up to inspect it.

### Cassia Susurra, information clerk (woman; key green #00FF00)
- **Design line:** early thirties, petite; olive skin; a short deep-plum bob with a straight fringe (clearly purple, not pink); grey eyes; a knowing look; a long mustard-yellow travelling coat with many pockets over a black high-necked blouse, a brown skirt over leggings, ankle boots; a leather satchel stuffed with notebooks; a pencil behind one ear.
- **Work loop:** flipping through a notebook held in one hand, then reaching out to pin a note to an unseen board.

### Ulrich Esser, craftsman (man; key green #00FF00)
- **Design line:** late thirties, broad chest and shoulders, strong arms; light skin reddened by forge heat; salt-and-pepper hair tied in a short tail; short dark stubble; steel-grey eyes; goggles pushed up on his head; a heavy brown leather smith's apron over a charcoal undershirt with bare arms; thick gloves tucked in the belt; leather trousers, work boots; a hammer and tongs on his belt.
- **Work loop:** hammering on an unseen anvil at waist height with a hand hammer, holding tongs in the other hand, in a steady rhythm. (No glow or sparks; those are engine effects.)

## 6. Asset checklist

| | Stills | Videos |
|---|---|---|
| Adventurers | base sheet (3×2), sleeping, battle stance, Getting Hit, Guard, Victory, Defeat | walk front / side / back; battle idle → attack → skill (10 s) |
| HQ staff | base sheet (3×2) | walk front / side / back; work loop (4 s) |

Facing right is mirrored in the engine for every still and video.

## Review before approval

Compare each result with Tristitia, Elsie and the Commander at native size and the same whole-number zoom on one foot line (the standing rule): head size, eye style, outline weight and pixel size must match, and heights must follow the table above.

## 7. Ready to paste, per character

Every prompt below is complete: nothing to fill in. Work top to bottom for each character; each step's result is the next step's reference. "Clean" means the usual snap-and-clean pass from `Gemini Sprite Prompts.md`, which produces the start frames. Facing right is mirrored in the engine.

### Anselm Voigt (adventurer; key magenta #FF00FF; about 98 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Commander/Reference Sheet.png` (style and proportion), `Character Sprites/Recruitable Staff/Adventurers/Anselm Voigt/Idle Front.png` (design).

```
Pixel-art character sprite sheet of Anselm Voigt for an HD-2D JRPG.

References:
- Image 1 (Commander reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Anselm Voigt must look like a member of the same cast as that character.
- Image 2 is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height or face drawing.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 98 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: young and enthusiastic; warm golden-blond short messy hair; brown eyes; silver-steel plate armour over a deep-teal surcoat; a medium teal kite shield with a steel rim on his LEFT arm (viewer's right in the front view); an arming sword on his right side. No emblems. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure magenta #FF00FF filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Sleeping.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Anselm Voigt asleep, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: lying on his back, armour on, shield set down beside him, one arm behind his head. Seen from the same three-quarter game camera as the sheet. Eyes closed. No bed, pillow, blanket, floor, "Z" letters. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects and no text.
```

**3. Battle stance.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Anselm Voigt in a battle stance facing left, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: shield raised in front at chest height, sword held back and ready, feet planted. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects and no text.
```

**4. Getting Hit.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Anselm Voigt facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: recoiling from a blow from the left: upper body knocked back to the right, head turned aside, eyes squeezed shut, weapon arm thrown out of guard, feet still on the ground. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**5. Guard.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Anselm Voigt facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: braced facing left, weight on the back foot, blocking with the kite shield held up in front, covering his body, sword ready behind it. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**6. Victory.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Anselm Voigt facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: sword raised high in his right hand, shield lowered at his side, relaxed and proud, still turned toward the left. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**7. Defeat.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Anselm Voigt facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: dropped to one knee, head down, one hand on the ground, shield lying flat beside him, sword still gripped. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**8. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Anselm Voigt, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 98 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: silver-steel plate armour over a deep-teal surcoat, the teal kite shield on his left arm, the arming sword, short golden-blond hair; no emblems. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Anselm Voigt walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**9. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Anselm Voigt, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 98 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: silver-steel plate armour over a deep-teal surcoat, the teal kite shield on his left arm, the arming sword, short golden-blond hair; no emblems. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Anselm Voigt walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**10. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Anselm Voigt, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 98 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: silver-steel plate armour over a deep-teal surcoat, the teal kite shield on his left arm, the arming sword, short golden-blond hair; no emblems. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Anselm Voigt walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**11. Battle idle → attack → skill (video, 10 s, Omniflash, Start frame).** Start frame: the cleaned battle stance from step 3.

```
Pixel-art sprite animation of Anselm Voigt, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 98 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: silver-steel plate armour over a deep-teal surcoat, the teal kite shield on his left arm, the arming sword, short golden-blond hair; no emblems. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces left the whole time, holding an arming sword and a teal kite shield. About 10 seconds:
1. Battle idle (0–3 s): ready stance with a small breathing bounce, looping.
2. Attack (3–6 s): a basic attack with the arming sword and a teal kite shield: step in toward the left, strike, recover to the stance.
3. Skill (6–10 s): Phalanx: he plants his feet and raises the sword crosswise in a guard behind the shield, holds it, then relaxes back to the stance. Show only the body motion, with no effects. End back in the battle stance.
```

### Nell Larkin (adventurer; key magenta #FF00FF; about 91 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Elsie/Reference Sheet.png` (style and proportion), `Character Sprites/Recruitable Staff/Adventurers/Nell Larkin/Idle Front.png` (design).

```
Pixel-art character sprite sheet of Nell Larkin for an HD-2D JRPG.

References:
- Image 1 (Elsie reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Nell Larkin must look like a member of the same cast as that character.
- Image 2 is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height or face drawing.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 91 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: warm brown skin, freckles; very dark brown hair in one long braid over her shoulder; amber eyes; a green hooded capelet (hood down), cream shirt, fitted green tunic and legwear, brown leather jerkin, a bracer on her bow arm, fingerless gloves, light brown boots; a wooden recurve bow on her back and a hip arrow case. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure magenta #FF00FF filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Sleeping.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Nell Larkin asleep, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: curled on her side, hood up over her head, bow set beside her. Seen from the same three-quarter game camera as the sheet. Eyes closed. No bed, pillow, blanket, floor, "Z" letters. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects and no text.
```

**3. Battle stance.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Nell Larkin in a battle stance facing left, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: bow held forward at the ready, an arrow nocked and half drawn, back straight. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects and no text.
```

**4. Getting Hit.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Nell Larkin facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: recoiling from a blow from the left: upper body knocked back to the right, head turned aside, eyes squeezed shut, weapon arm thrown out of guard, feet still on the ground. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**5. Guard.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Nell Larkin facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: braced facing left, weight on the back foot, blocking with the bow held horizontally across her body, leaning back. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**6. Victory.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Nell Larkin facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: bow raised overhead in one hand, the other hand on her hip, relaxed and proud, still turned toward the left. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**7. Defeat.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Nell Larkin facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: dropped to one knee, head down, one hand on the ground, bow resting on the ground under her hand. One sprite, centred, on a flat solid pure magenta #FF00FF background, with no shadow, no effects, no impact marks and no text.
```

**8. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Nell Larkin, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 91 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the green hooded capelet with the hood down, fitted green tunic and legwear, brown leather jerkin, the single long braid, the bow and hip arrow case. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Nell Larkin walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**9. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Nell Larkin, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 91 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the green hooded capelet with the hood down, fitted green tunic and legwear, brown leather jerkin, the single long braid, the bow and hip arrow case. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Nell Larkin walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**10. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Nell Larkin, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 91 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the green hooded capelet with the hood down, fitted green tunic and legwear, brown leather jerkin, the single long braid, the bow and hip arrow case. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Nell Larkin walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**11. Battle idle → attack → skill (video, 10 s, Omniflash, Start frame).** Start frame: the cleaned battle stance from step 3.

```
Pixel-art sprite animation of Nell Larkin, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 91 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the green hooded capelet with the hood down, fitted green tunic and legwear, brown leather jerkin, the single long braid, the bow and hip arrow case. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces left the whole time, holding a wooden recurve bow. About 10 seconds:
1. Battle idle (0–3 s): ready stance with a small breathing bounce, looping.
2. Attack (3–6 s): a basic attack with the wooden recurve bow: step in toward the left, strike, recover to the stance.
3. Skill (6–10 s): Frost Arrow: a longer, deeper draw, a held aim, then the release, and back to the stance. Show only the body motion, with no effects. End back in the battle stance.
```

### Severa Kaltenbach (adventurer; key green #00FF00; about 97 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Elsie/Reference Sheet.png` (style and proportion), `Character Sprites/Recruitable Staff/Adventurers/Severa Kaltenbach/Idle Front.png` (design).

```
Pixel-art character sprite sheet of Severa Kaltenbach for an HD-2D JRPG.

References:
- Image 1 (Elsie reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Severa Kaltenbach must look like a member of the same cast as that character.
- Image 2 is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height or face drawing.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 97 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: fair skin; navy-black hair in a neat low bun with a few loose strands; ice-blue eyes; steel half-plate (breastplate, pauldrons, gauntlets) over a dark-blue gambeson; a white and steel-blue tabard with the same pattern as the design image; a short dark-blue cape on one shoulder only; grey trousers, steel-capped boots; a broad plain greatsword shorter than her full height (the blade reaches her chest when planted), carried over her shoulder. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure green #00FF00 filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Sleeping.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Severa Kaltenbach asleep, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: sitting against an unseen wall, knees drawn up, greatsword leaning across her shoulder, head bowed. Seen from the same three-quarter game camera as the sheet. Eyes closed. No bed, pillow, blanket, floor, "Z" letters. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects and no text.
```

**3. Battle stance.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Severa Kaltenbach in a battle stance facing left, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: two-handed greatsword held diagonally in front, point up and slightly forward, feet apart. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects and no text.
```

**4. Getting Hit.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Severa Kaltenbach facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: recoiling from a blow from the left: upper body knocked back to the right, head turned aside, eyes squeezed shut, weapon arm thrown out of guard, feet still on the ground. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**5. Guard.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Severa Kaltenbach facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: braced facing left, weight on the back foot, blocking with the greatsword held flat and horizontal in front with both hands, blade across her body. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**6. Victory.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Severa Kaltenbach facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: greatsword planted point-down in front, both hands on the pommel, relaxed and proud, still turned toward the left. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**7. Defeat.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Severa Kaltenbach facing left in a battle pose, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: dropped to one knee, head down, one hand on the ground, greatsword planted beside her, holding it to stay up. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**8. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Severa Kaltenbach, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 97 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: steel half-plate over a dark-blue gambeson, the white and steel-blue tabard, the short dark-blue cape on one shoulder only, grey trousers, navy-black hair in a low bun, the greatsword shorter than her height. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Severa Kaltenbach walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**9. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Severa Kaltenbach, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 97 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: steel half-plate over a dark-blue gambeson, the white and steel-blue tabard, the short dark-blue cape on one shoulder only, grey trousers, navy-black hair in a low bun, the greatsword shorter than her height. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Severa Kaltenbach walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**10. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Severa Kaltenbach, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 97 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: steel half-plate over a dark-blue gambeson, the white and steel-blue tabard, the short dark-blue cape on one shoulder only, grey trousers, navy-black hair in a low bun, the greatsword shorter than her height. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Severa Kaltenbach walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**11. Battle idle → attack → skill (video, 10 s, Omniflash, Start frame).** Start frame: the cleaned battle stance from step 3.

```
Pixel-art sprite animation of Severa Kaltenbach, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 97 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: steel half-plate over a dark-blue gambeson, the white and steel-blue tabard, the short dark-blue cape on one shoulder only, grey trousers, navy-black hair in a low bun, the greatsword shorter than her height. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces left the whole time, holding a two-handed greatsword. About 10 seconds:
1. Battle idle (0–3 s): ready stance with a small breathing bounce, looping.
2. Attack (3–6 s): a basic attack with the two-handed greatsword: step in toward the left, strike, recover to the stance.
3. Skill (6–10 s): Diving Splitter: a short run-up and leap, then a two-handed downward cleave, and back to the stance. Keep the whole blade in frame; never raise it straight overhead. Show only the body motion, with no effects. End back in the battle stance.
```

### Otto Grimbald (adventurer; key green #00FF00; about 96 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Commander/Reference Sheet.png` (style and proportion), `Character Sprites/Recruitable Staff/Adventurers/Otto Grimbald/Idle Front.png` (design).

```
Pixel-art character sprite sheet of Otto Grimbald for an HD-2D JRPG.

References:
- Image 1 (Commander reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Otto Grimbald must look like a member of the same cast as that character.
- Image 2 is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height or face drawing.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 96 art pixels tall from the top of the helmet to the soles, every sprite on the sheet at the same scale.

Face: none visible. The sallet visor is closed in every sprite; only the dark sight slit shows.

Design: full plate armour from head to toe in gunmetal steel with darkened-silver trim and small ochre padding at the joints; a closed German sallet helmet (rounded crown, lowered visor, narrow sight slit, swept neck guard) with a bevor covering the face; a heavy two-handed warhammer with a long wooden shaft and a rectangular iron head; no shield; a wide, planted stance. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure green #00FF00 filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Sleeping.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Otto Grimbald asleep, matching the attached sprite exactly: same design, colours, closed helmet (no face shows), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: sitting on the ground against an unseen wall, helmet and armour still on, the warhammer across his lap. Seen from the same three-quarter game camera as the sheet. Eyes closed. No bed, pillow, blanket, floor, "Z" letters. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects and no text.
```

**3. Battle stance.** Attach: the approved base sheet from step 1.

```
Pixel-art sprite of Otto Grimbald in a battle stance facing left, matching the attached sprite exactly: same design, colours, closed helmet (no face shows), pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: warhammer held diagonally across the body in both hands, head low and forward, feet wide. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects and no text.
```

**4. Getting Hit.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Otto Grimbald facing left in a battle pose, matching the attached sprite exactly: same design, colours, closed helmet (no face shows), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: recoiling from a blow from the left: upper body knocked back to the right, head turned aside, eyes squeezed shut, weapon arm thrown out of guard, feet still on the ground. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**5. Guard.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Otto Grimbald facing left in a battle pose, matching the attached sprite exactly: same design, colours, closed helmet (no face shows), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: braced facing left, weight on the back foot, blocking with the warhammer shaft held horizontally in front with both hands. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**6. Victory.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Otto Grimbald facing left in a battle pose, matching the attached sprite exactly: same design, colours, closed helmet (no face shows), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: warhammer resting on his shoulder, free fist on his hip, relaxed and proud, still turned toward the left. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**7. Defeat.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).

```
Pixel-art sprite of Otto Grimbald facing left in a battle pose, matching the attached sprite exactly: same design, colours, closed helmet (no face shows), weapon, pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
Pose: dropped to one knee, head down, one hand on the ground, warhammer head on the ground, both hands on the shaft. One sprite, centred, on a flat solid pure green #00FF00 background, with no shadow, no effects, no impact marks and no text.
```

**8. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Otto Grimbald, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: full plate armour head to toe with the closed sallet helmet and visor down at all times, the two-handed warhammer; no shield. Keep the helmet visor closed in every frame; no face shows.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Otto Grimbald walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**9. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Otto Grimbald, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: full plate armour head to toe with the closed sallet helmet and visor down at all times, the two-handed warhammer; no shield. Keep the helmet visor closed in every frame; no face shows.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Otto Grimbald walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**10. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Otto Grimbald, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: full plate armour head to toe with the closed sallet helmet and visor down at all times, the two-handed warhammer; no shield. Keep the helmet visor closed in every frame; no face shows.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Otto Grimbald walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**11. Battle idle → attack → skill (video, 10 s, Omniflash, Start frame).** Start frame: the cleaned battle stance from step 3.

```
Pixel-art sprite animation of Otto Grimbald, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: full plate armour head to toe with the closed sallet helmet and visor down at all times, the two-handed warhammer; no shield. Keep the helmet visor closed in every frame; no face shows.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces left the whole time, holding a heavy two-handed warhammer. About 10 seconds:
1. Battle idle (0–3 s): ready stance with a small breathing bounce, looping.
2. Attack (3–6 s): a basic attack with the heavy two-handed warhammer: step in toward the left, strike, recover to the stance.
3. Skill (6–10 s): Hammerfall: he raises the hammer high to one side and brings it down in a heavy overhead blow with a short stagger of follow-through, then back to the stance. Show only the body motion, with no effects. End back in the battle stance.
```

### Konrad Metzler (HQ staff; key magenta #FF00FF; about 99 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Commander/Reference Sheet.png` (style and proportion).

```
Pixel-art character sprite sheet of Konrad Metzler for an HD-2D JRPG.

References:
- Image 1 (Commander reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Konrad Metzler must look like a member of the same cast as that character.
- There is no design image for this character: follow the design description below exactly.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 99 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: late fifties, very tall, big-framed and slightly stooped; deep brown skin; bald with a neat grey beard and bushy grey eyebrows; a kind, heavy-browed face with a squint; a long off-white butcher's apron with a few old stains over a dark-green work shirt with rolled sleeves; leather forearm guards; a belt of wrapped knives and a cleaver; wooden clogs. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure magenta #FF00FF filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Konrad Metzler, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 99 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long off-white butcher's apron over the dark-green shirt with rolled sleeves, leather forearm guards, the knife belt, clogs, bald head and neat grey beard. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Konrad Metzler walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**3. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Konrad Metzler, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 99 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long off-white butcher's apron over the dark-green shirt with rolled sleeves, leather forearm guards, the knife belt, clogs, bald head and neat grey beard. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Konrad Metzler walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**4. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Konrad Metzler, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 99 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long off-white butcher's apron over the dark-green shirt with rolled sleeves, leather forearm guards, the knife belt, clogs, bald head and neat grey beard. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Konrad Metzler walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**5. Work loop (video, 4 s, Omniflash, Start frame).** Start frame: `Start - Facing Down.png` (row 1, front) from the cleaned sheet.

```
Pixel-art sprite animation of Konrad Metzler, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 99 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long off-white butcher's apron over the dark-green shirt with rolled sleeves, leather forearm guards, the knife belt, clogs, bald head and neat grey beard. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces down (toward the camera) the whole time. About 4 seconds of sharpening a knife on a hand-held whetstone, then holding a hide up to inspect it, a small repeating motion that ends in the same pose it started in, so it loops. Mime the workstation: no table, anvil, board or bench appears; the station is placed in the game.
```

### Cassia Susurra (HQ staff; key green #00FF00; about 87 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Elsie/Reference Sheet.png` (style and proportion).

```
Pixel-art character sprite sheet of Cassia Susurra for an HD-2D JRPG.

References:
- Image 1 (Elsie reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Cassia Susurra must look like a member of the same cast as that character.
- There is no design image for this character: follow the design description below exactly.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 87 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: early thirties, petite; olive skin; a short deep-plum bob with a straight fringe (clearly purple, not pink); grey eyes; a knowing look; a long mustard-yellow travelling coat with many pockets over a black high-necked blouse, a brown skirt over leggings, ankle boots; a leather satchel stuffed with notebooks; a pencil behind one ear. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure green #00FF00 filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Cassia Susurra, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 87 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long mustard-yellow coat, black high-necked blouse, brown skirt over leggings, ankle boots, the satchel, the short deep-plum bob. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Cassia Susurra walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**3. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Cassia Susurra, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 87 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long mustard-yellow coat, black high-necked blouse, brown skirt over leggings, ankle boots, the satchel, the short deep-plum bob. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Cassia Susurra walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**4. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Cassia Susurra, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 87 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long mustard-yellow coat, black high-necked blouse, brown skirt over leggings, ankle boots, the satchel, the short deep-plum bob. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Cassia Susurra walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**5. Work loop (video, 4 s, Omniflash, Start frame).** Start frame: `Start - Facing Down.png` (row 1, front) from the cleaned sheet.

```
Pixel-art sprite animation of Cassia Susurra, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 87 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the long mustard-yellow coat, black high-necked blouse, brown skirt over leggings, ankle boots, the satchel, the short deep-plum bob. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces down (toward the camera) the whole time. About 4 seconds of flipping through a notebook held in one hand, then reaching out to pin a note to an unseen board, a small repeating motion that ends in the same pose it started in, so it loops. Mime the workstation: no table, anvil, board or bench appears; the station is placed in the game.
```

### Ulrich Esser (HQ staff; key green #00FF00; about 100 px)

**1. Base sheet.** Attach: `Character Sprites/Officers/Commander/Reference Sheet.png` (style and proportion).

```
Pixel-art character sprite sheet of Ulrich Esser for an HD-2D JRPG.

References:
- Image 1 (Commander reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Ulrich Esser must look like a member of the same cast as that character.
- There is no design image for this character: follow the design description below exactly.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 100 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale.

Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: late thirties, broad chest and shoulders, strong arms; light skin reddened by forge heat; salt-and-pepper hair tied in a short tail; short dark stubble; steel-grey eyes; goggles pushed up on his head; a heavy brown leather smith's apron over a charcoal undershirt with bare arms; thick gloves tucked in the belt; leather trousers, work boots; a hammer and tongs on his belt. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure green #00FF00 filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**2. Walk front (video, Omniflash, Start frame).** Start frame: `Start - Walk Down.png` from the cleaned sheet.

```
Pixel-art sprite animation of Ulrich Esser, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 100 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the heavy brown leather apron over the charcoal undershirt, bare arms, goggles pushed up on his head, salt-and-pepper hair in a short tail. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Ulrich Esser walks in place facing down, toward the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**3. Walk side (video, Omniflash, Start frame).** Start frame: `Start - Walk Left.png` from the cleaned sheet.

```
Pixel-art sprite animation of Ulrich Esser, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 100 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the heavy brown leather apron over the charcoal undershirt, bare arms, goggles pushed up on his head, salt-and-pepper hair in a short tail. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Ulrich Esser walks in place facing left, in side view for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**4. Walk back (video, Omniflash, Start frame).** Start frame: `Start - Walk Up.png` from the cleaned sheet.

```
Pixel-art sprite animation of Ulrich Esser, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 100 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the heavy brown leather apron over the charcoal undershirt, bare arms, goggles pushed up on his head, salt-and-pepper hair in a short tail. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, Ulrich Esser walks in place facing up, away from the camera for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

**5. Work loop (video, 4 s, Omniflash, Start frame).** Start frame: `Start - Facing Down.png` (row 1, front) from the cleaned sheet.

```
Pixel-art sprite animation of Ulrich Esser, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 100 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid pure green #00FF00 for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: the heavy brown leather apron over the charcoal undershirt, bare arms, goggles pushed up on his head, salt-and-pepper hair in a short tail. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
Starting exactly from the attached frame, the character faces down (toward the camera) the whole time. About 4 seconds of hammering on an unseen anvil at waist height with a hand hammer, holding tongs in the other hand, in a steady rhythm, a small repeating motion that ends in the same pose it started in, so it loops. Mime the workstation: no table, anvil, board or bench appears; the station is placed in the game.
```

