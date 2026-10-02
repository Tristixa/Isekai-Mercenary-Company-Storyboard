# Special pose prompts: Chapter 1 (Scenes 1–8)

Written 2026-09-30; recounted 2026-10-02 for the finished Chapter 1 manuscript (Scenes 1–8), after the kneel, hand-kiss and salute options were removed. These are paste-ready prompts for **every special pose in the Chapter 1 scene headers**: a sprite pose beyond idle and walk (`Game Design/Scene Script Format.md` §1). Each pose is a **still image**, not a video.

- **Only the facings the scene staging uses are listed.** Facing right is the left pose **mirrored** in the engine.
- **A missing pose falls back to idle** (FGC_07 §10.4), so none of these blocks development. Poses marked **optional** can be skipped: the portrait and the emotes carry the moment.

## How to make each one

- **Tool:** Gemini, still image. **Attach, in order:**
  1. the character's `Reference Sheet.png`: style, proportion and design;
  2. the matching `Cropped/Start - Facing <Down|Left|Up>.png`: the scale and the facing.
- **One image per pose.** When a pose needs two facings, put both on one image, side by side, as on the base sheet.
- **Background:** pure magenta `#FF00FF` for everyone, the same as their sheets.
- **Clean** it with the usual snap-and-clean pass (true 8×8 grid, mouth and nose removed). Save the cleaned result as `Character Sprites/Officers/<Character>/Poses/<pose>.png` (and `<pose> - Left.png` or `<pose> - Up.png` when there's more than one facing). The engine loads it as `<actor>_<pose>`.
- **Props:** a tavern mug is drawn in the hand. **Chairs, tables and benches are never drawn** (the scene places them), so seated poses mime the seat.
- **Review:** compare it with the character's sheet at the same zoom on one foot line. Same head size, pixel size, outfit and palette; no mouth, no nose.

## Prompt template (every pose)

```
Pixel-art sprite of [NAME] in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about [HEIGHT] art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: [OUTFIT LOCK].

Pose: [POSE]. Direction: [FACING].

Show only the character (and a hand-held prop if the pose names one). No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

## Summary

| Character | Required (Gemini) | Optional (Gemini) | Puppet script (no Gemini) |
|---|---|---|---|
| Commander | lie (down); sit_ground (down); sit (left, up); raise_mug (left) | think_seated, look_down_seated, stand_from_chair | nod (standing down; seated left) |
| Tristitia | sit (down); raise_mug (down); point (down, left) | stand_from_chair | nod (standing down; seated down) |
| Elsie | look_down (left); sit (left) | — | nod (seated left) |
| Mae | sit (left); raise_mug (left) | — | nod (seated left) |
| Fulker | — (her craft loop is in the work animation prompts) | — | nod (standing down) |
| Valerie, Liliana | — (Scene 8 needs only idles and turns) | — | — |

**11 required Gemini images and 4 optional**, counted per pose (some poses have two facings on one image), **plus 5 puppet nods** (7 facings) made by script, and Fulker's existing work loop.

**Removed 2026-10-02 (owner):** the Commander's kneel, kneel_reach, stand_from_kneel, salute and salute_seated, and Elsie's withdraw_hand and salute, with the kneel, hand-kiss and salute options in Scenes 1–3.

**Proposed manuscript tweak:** in Scene 1 the Commander sits **on the ground** under the tree, which is a different pose from sitting on a chair. This file names it `sit_ground`. I'll update Scene 1's header and cues to match when you confirm.

## Commander (about 93 px; key magenta)

### lie

*Used in Scene 1 (under the tree).* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Down.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: lying on his back on the grass, asleep, arms loose at his sides, legs straight, head toward the top of the image; the body is seen from above at the game's 40° camera, so it reads as a short lying figure. Direction: facing down, toward the camera (front view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### sit_ground

*Used in Scene 1 (under the tree; the header currently calls this `sit`).* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Down.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: sitting on the ground with his knees drawn up and one forearm resting on a knee, relaxed. Direction: facing down, toward the camera (front view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### think_seated (optional)

*Used in Scene 1.* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Down.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: sitting on the ground as in sit_ground, one hand raised to his chin, head tilted slightly, thinking. Direction: facing down, toward the camera (front view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### sit

*Used in Scene 2 (facing east = mirrored left); Scenes 3 and 6 (facing north = up).* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Left.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Up.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: seated upright on an unseen chair at a table: thighs level, knees bent at a right angle, feet flat on the floor, hands resting on his thighs. Mime the chair: no chair or table appears. Direction: facing left, in side view; and on the right of the same image, facing up, away from the camera (back view). Leave at least 60 image pixels of empty background between the two sprites.

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### nod (puppet)

*Used in Scene 1 (standing, down) and Scene 2 (seated, facing east = mirrored left).* **Not a Gemini image.** Made by the puppet script (`D:/Codex/IMC/runs/puppet-pilot-v1/puppet.py`, owner-approved 2026-10-02) from the Commander's matching idle or seated pose: the head drops 1 then 2 pixels with the eyes closed at the bottom. It needs only that pose's eye boxes and chin line measured.

### look_down_seated (optional)

*Used in Scene 3.* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Up.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: seated on an unseen chair, head bowed, looking down at his hands. Direction: facing up, away from the camera (back view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### stand_from_chair (optional)

*Used in Scene 3.* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Up.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: halfway up from an unseen chair: knees still bent, hands pushing off his thighs, torso leaning forward. Direction: facing up, away from the camera (back view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### raise_mug

*Used in Scene 2 (facing east = mirrored left).* Attach `Character Sprites/Officers/Commander/Reference Sheet.png` + `Character Sprites/Officers/Commander/Cropped/Start - Facing Left.png`.

```
Pixel-art sprite of Commander in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: messy black hair, the long black coat worn open over a white shirt, dark blue jeans (he is from Earth), dark boots.

Pose: seated on an unseen chair, raising a wooden tavern mug in a toast at head height. Direction: facing left, in side view.

Show only the character and the mug. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

## Tristitia (about 93 px; key magenta)

### sit

*Used in Scenes 2, 3 and 6 (table_north, facing south = down).* Attach `Character Sprites/Officers/Tristitia/Reference Sheet.png` + `Character Sprites/Officers/Tristitia/Cropped/Start - Facing Down.png`.

```
Pixel-art sprite of Tristitia in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: long silver hair falling over one eye, the long black coat with gold trim and red lining, the white shirt with the red cravat, black gloves, black trousers, black boots.

Pose: seated upright on an unseen chair at a table: thighs level, knees bent at a right angle, feet on the floor, hands folded on her lap. Composed and poised. Direction: facing down, toward the camera (front view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### raise_mug

*Used in Scene 2.* Attach `Character Sprites/Officers/Tristitia/Reference Sheet.png` + `Character Sprites/Officers/Tristitia/Cropped/Start - Facing Down.png`.

```
Pixel-art sprite of Tristitia in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: long silver hair falling over one eye, the long black coat with gold trim and red lining, the white shirt with the red cravat, black gloves, black trousers, black boots.

Pose: seated as in sit, raising a wooden tavern mug in a restrained toast at shoulder height. Direction: facing down, toward the camera (front view).

Show only the character and the mug. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### point

*Used in Scene 1 (the way to Eurydica).* Attach `Character Sprites/Officers/Tristitia/Reference Sheet.png` + `Character Sprites/Officers/Tristitia/Cropped/Start - Facing Down.png` + `Character Sprites/Officers/Tristitia/Cropped/Start - Facing Left.png`.

```
Pixel-art sprite of Tristitia in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: long silver hair falling over one eye, the long black coat with gold trim and red lining, the white shirt with the red cravat, black gloves, black trousers, black boots.

Pose: standing, one arm extended, pointing ahead with her index finger, as if showing the way. Direction: facing down, toward the camera (front view); and on the right of the same image, facing left, in side view. Leave at least 60 image pixels of empty background between the two sprites.

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### stand_from_chair (optional)

*Used in Scene 3.* Attach `Character Sprites/Officers/Tristitia/Reference Sheet.png` + `Character Sprites/Officers/Tristitia/Cropped/Start - Facing Down.png`.

```
Pixel-art sprite of Tristitia in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: long silver hair falling over one eye, the long black coat with gold trim and red lining, the white shirt with the red cravat, black gloves, black trousers, black boots.

Pose: halfway up from an unseen chair: knees still bent, one hand on the table's edge (mimed, no table). Direction: facing down, toward the camera (front view).

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### nod (puppet)

*Used in Scene 5 (standing, down) and Scene 6 (seated, down).* **Not a Gemini image.** Made by the puppet script (`D:/Codex/IMC/runs/puppet-pilot-v1/puppet.py`, owner-approved 2026-10-02) from Tristitia's matching idle or seated pose: the head drops 1 then 2 pixels with the eyes closed at the bottom. It needs only that pose's eye boxes and chin line measured.

## Elsie (about 93 px; key magenta)

### look_down

*Used in Scene 3 (bench_east, facing west = left). The puppet script's look-down (lowered lids, head 1 pixel lower) is a stand-in until this is made.* Attach `Character Sprites/Officers/Elsie/Reference Sheet.png` + `Character Sprites/Officers/Elsie/Cropped/Start - Facing Left.png`.

```
Pixel-art sprite of Elsie in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: the blonde high ponytail, the olive-green military jacket, black fitted trousers, brown gloves, the equipment belts, brown boots.

Pose: standing, head bowed, looking down at something on the bench in front of her, hands at her sides. Direction: facing left, in side view.

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### sit

*Used in Scene 6 (table_east, facing west = left).* Attach `Character Sprites/Officers/Elsie/Reference Sheet.png` + `Character Sprites/Officers/Elsie/Cropped/Start - Facing Left.png`.

```
Pixel-art sprite of Elsie in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: the blonde high ponytail, the olive-green military jacket, black fitted trousers, brown gloves, the equipment belts, brown boots.

Pose: seated upright on an unseen chair at a table: thighs level, knees bent at a right angle, feet flat on the floor, forearms resting on her thighs, relaxed but alert. Mime the chair: no chair or table appears. Direction: facing left, in side view.

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### nod (puppet)

*Used in Scene 6 (seated, facing west = left).* **Not a Gemini image.** Made by the puppet script (`D:/Codex/IMC/runs/puppet-pilot-v1/puppet.py`, owner-approved 2026-10-02) from Elsie's matching idle or seated pose: the head drops 1 then 2 pixels with the eyes closed at the bottom. It needs only that pose's eye boxes and chin line measured.

## Mae (Steady Mae; about 93 px; key magenta)

### sit

*Used in Scene 2 (table_east, facing west = left); Scene 6 (table_west, facing east = mirrored left).* Attach `Character Sprites/Officers/Steady Mae/Reference Sheet.png` + `Character Sprites/Officers/Steady Mae/Cropped/Start - Facing Left.png`.

```
Pixel-art sprite of Mae Tanner (Steady Mae) in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: long wavy brown hair, the white blouse with rolled sleeves, the brown leather vest, the belts and pouches, brown gloves, dark trousers, brown boots.

Pose: seated relaxed on an unseen chair, leaning back slightly, one arm resting on the table's edge (mimed). Direction: facing left, in side view.

Show only the character. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### raise_mug

*Used in Scene 2.* Attach `Character Sprites/Officers/Steady Mae/Reference Sheet.png` + `Character Sprites/Officers/Steady Mae/Cropped/Start - Facing Left.png`.

```
Pixel-art sprite of Mae Tanner (Steady Mae) in a special pose, for an HD-2D JRPG. Match the attached sprite sheet exactly: same design, colours, head size (about one third of the total height), large eyes with a single highlight, outline weight, pixel size and shading.

Pixel rules: true pixel grid; every art pixel is an exact 8×8 block of image pixels on one grid. No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.

Scale: the same scale as the attached start frame (about 93 art pixels tall when standing). Seated, kneeling and lying poses are shorter because of the pose, never because the character is smaller.

Face: large eyes with a highlight, NO mouth, NO lips, NO nose.

Outfit, exactly as in the sheet: long wavy brown hair, the white blouse with rolled sleeves, the brown leather vest, the belts and pouches, brown gloves, dark trousers, brown boots.

Pose: seated as in sit, raising a wooden tavern mug high in a cheerful toast. Direction: facing left, in side view.

Show only the character and the mug. No chair, table, bench, floor, shadow, effects or text. Background: one flat solid pure magenta #FF00FF filling the whole image.
```

### nod (puppet)

*Used in Scene 6 (seated, facing east = mirrored left).* **Not a Gemini image.** Made by the puppet script (`D:/Codex/IMC/runs/puppet-pilot-v1/puppet.py`, owner-approved 2026-10-02) from Mae's matching idle or seated pose: the head drops 1 then 2 pixels with the eyes closed at the bottom. It needs only that pose's eye boxes and chin line measured.

## Fulker (about 93 px; key magenta)

### craft

*Used in Scene 7 (fulker_station, facing south = down).* **Not a still.** This is Fulker's Workshop work loop, already written in `Production Assets Requirement/Officer Work Animation Prompts.md` (Sigrid Fulker — Workshop); the scene plays it twice.

### nod (puppet)

*Used in Scene 7 (standing, down).* **Not a Gemini image.** Made by the puppet script (`D:/Codex/IMC/runs/puppet-pilot-v1/puppet.py`, owner-approved 2026-10-02) from Fulker's matching idle or seated pose: the head drops 1 then 2 pixels with the eyes closed at the bottom. It needs only that pose's eye boxes and chin line measured.
