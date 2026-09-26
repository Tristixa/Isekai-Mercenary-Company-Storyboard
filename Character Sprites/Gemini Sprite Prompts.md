# Gemini prompts for IMC character sprites

> **If a sheet still has a mouth or nose:** don't paint over the Gemini image. Painting on the upscaled image creates mixels. Instead, the pipeline snaps the sheet to its true grid at full detail. The mouth and nose are then removed on that grid, where 1 pixel = 1 art pixel. The cleaned sprites are exported back as a clean 8×8-block reference sheet on the key colour, and **that** reference is used as the start image for the videos. If you edit in Krita, edit the 1× snapped PNG with a 1-pixel pencil and anti-aliasing off, never the big image.

Last updated 2026-09-26. Videos: use **Omniflash** (steadiest, crispest and truest to the sprite of the three models tested). In Omniflash, attach the image with the **Start frame** option, not Ingredients. Tested 2026-09-26: Ingredients redesigned the outfit and changed the face, while Start frame kept the sprite. Each character folder has `Start - Walk Down/Left/Right/Up.png` (the walk pose from row 2 of the sheet, for the walk videos) and `Start - Facing Down/Left/Right/Up.png` (the idle pose from row 1, for the work video and the battle-stance images). Each is the cleaned sprite at ×8, centred on a 1920×1080 magenta frame at the right size. These produce source material for the sprite pipeline in `HD-2D Proof/tools/`, which snaps to the grid, cleans, outlines and packs the frames. Replace the `[BRACKETS]` for each character. Attach the character's current portrait every time.

Keep these the same for every character:
- **Size:** about **96 art pixels tall** from the hair to the soles. The game uses sprites at their native size with no downscale (decided 2026-09-26). The six officer sheets came out 91–98 px tall on a 7.5 px grid, so asking for about 96 keeps new characters consistent with them.
- **Pixel block:** every art pixel is an **8 × 8 block** of image pixels. The snapper finds the grid much more reliably when the block size is fixed and large.
- **Background:** use a **key colour** the character does not wear. The default is pure green `#00FF00`. For characters with green clothing, eyes or skills (Valencia, Elsie's jacket), use magenta `#FF00FF`. Use the **same key colour in the sheet and in all four videos** for that character.

---

## 1. Sprite sheet (still image)

```
Pixel-art character sprite sheet of [NAME] for an HD-2D JRPG, in the style of Octopath Traveler and Dragon Quest III HD-2D field sprites. Use the attached portrait for the design.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients.
- Clean dark outline around the silhouette, a darker shade of the colour next to it rather than pure black. Soft light from the upper left.

Size and proportions:
- The character is about 96 art pixels tall from the top of the hair to the soles of the boots (about 770 image pixels), and about 50 art pixels wide.
- Every sprite on the sheet is drawn at exactly the same scale.
- Head about 40% of the height, large eyes, stylised JRPG proportions, a readable [female/male] silhouette.

Face: large eyes with a highlight. NO mouth, NO lips, NO nose.

Outfit: follow the portrait: [ONE-LINE OUTFIT SUMMARY]. Keep only details large enough to read at this size. Belts, buckles, straps and trim can be 1–2 pixel accents. Leave out tiny props.

Layout: a grid of 4 columns × 2 rows.
- Columns, left to right: facing down (front), facing left, facing right, facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same order of directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid [KEY COLOUR, e.g. pure green #00FF00] filling the whole image. No gradient, no floor, no ground shadow, no text, no labels, no frames or panels.
```

---

## Shared rules for all four videos

Start each video from the character's cleaned sprite, in the direction stated. Paste this block into every video prompt:

```
Pixel-art sprite animation of [NAME], matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid [KEY COLOUR] for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: [OUTFIT LOCK, e.g. long black trousers down to the boots, no shorts, no bare thighs]. Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose.
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.
```

## Video 1: walk, one direction per video (all characters)

Make **four separate videos**, one per direction, each using the matching start frame. Batching all directions in one video made the model redesign the character.

| Video | Start frame | Direction line for the prompt |
|---|---|---|
| 1a | `Start - Walk Down.png` | facing down, toward the camera |
| 1b | `Start - Walk Left.png` | facing left, in side view |
| 1c | `Start - Walk Right.png` | facing right, in side view |
| 1d | `Start - Walk Up.png` | facing up, away from the camera |

Facing right gets its own video even though it mirrors facing left, because several designs are asymmetric (Tristitia's hair over one eye, Elsie's hip flap, Fulker's streak). Mirroring would flip them.

```
[SHARED RULES]
Starting exactly from the attached frame, [NAME] walks in place [DIRECTION LINE] for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.
```

## Video 2: work, greet and idle (all characters)

One video in a batch, using `Start - Facing Down.png` as the start frame.

```
[SHARED RULES]
Starting exactly from the attached frame, the character faces down (toward the camera) the whole time. About 10 seconds:
1. Working (0–4 s): [WORK ACTION, see the list below], a small repeating motion that loops.
2. Greeting (4–6.5 s): stops working, looks up and [GREETING, e.g. gives a small wave / a short bow / a nod], then returns to neutral.
3. Idle (6.5–10 s): relaxed standing idle with a gentle breathing motion and one blink, ending in the same pose it started in so it loops.
```

Work actions:
- **Tristitia:** writing in a ledger held in one arm.
- **Elsie:** checking a folded map.
- **Mae:** sorting materials from a pouch.
- **Fulker:** tapping with a small hammer.
- **Liliana:** reading from her report folio.
- **Adventurers:** a role-appropriate action (sharpening a blade, tightening a strap, checking arrows).

## Video 3: battle idle, skill and attack (adventurers, Tristitia, Elsie)

Battle view: the party stands on the right and faces **left** toward the enemies, as in Octopath.

```
[SHARED RULES]
The character faces left the whole time, holding [WEAPON]. About 10 seconds:
1. Battle idle (0–3 s): ready combat stance with a small breathing bounce, looping.
2. Skill (3–6.5 s): [SKILL NAME]: [SKILL POSE, e.g. raises the weapon and plants it to rally allies (buff) / draws back and throws a fast double slash (attack) / kneels and presses a hand to the ground (heal)]. Show only the body motion, with no effects.
3. Attack (6.5–10 s): a basic [WEAPON] attack. Step in toward the left, strike, and recover back to the battle stance.
```

Fill in for each character:
- **Tristitia:** weapon: a **rapier**, held in one hand. Skill: a precise single-target strike that leaves the enemy exposed. Pose: a fast lunging thrust with the rapier and a quick recovery flourish. Game effect (for the battle design, not the prompt): heavy damage to one enemy plus a massive DEF DOWN and SPD DOWN.
- **Elsie:** weapons: a **short sword in one hand and a spear in the other**, dual-wielded like Hildegard von Krone in Soul Calibur VI. Skill: a party-wide rally. Pose: plants the spear, raises the short sword overhead, and calls out to the party. Game effect: a large ATK UP and DEF UP on the whole party.
- Both officers only take the field in a crisis, so their skills are deliberately strong.
- **Adventurers:** weapon and skill come from their archetype (Vanguard, Scout, Medic, Porter).

## Video 4: hurt, guard, victory and defeat (adventurers, Tristitia, Elsie)

```
[SHARED RULES]
The character faces left the whole time, holding [WEAPON]. About 10 seconds, returning to the battle stance between parts:
1. Hurt (0–1.5 s): recoils from a hit, then recovers.
2. Guard (1.5–3.5 s): raises the weapon or arm to block and holds the guard.
3. Victory (3.5–7 s): [VICTORY POSE, e.g. twirls the weapon and rests it on the shoulder], then holds.
4. Defeat (7–10 s): stumbles and drops to one knee, head down, and holds that pose at the end.
```

---

## Ready to paste: Tristitia and Elsie battle videos (Omniflash)

Revised 2026-09-26 from the Soul Calibur VI reference clips in `~/Videos/Screen Recordings/`: Hildegard for Elsie, Amy's rapier style for Tristitia. The clips can't be fed to the video model as-is. The camera cuts and zooms, the characters are 3D, and they face right with heavy effects. The moves below describe their key poses in words, mirrored to face left.

### Step 0: battle-stance start frames (still images, do these first)

The `Start - Facing Left.png` frames have no weapons. Ask Gemini for **one still image each**, using the character's `Start - Facing Left.png` as the reference. I clean it the same way as the sheets and export it as `Start - Battle Left.png`.

```
Pixel-art sprite of [NAME] in a battle stance facing left, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), outfit, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no anti-aliasing, no mixels. [STANCE LINE]. One sprite, centred, on a flat solid magenta #FF00FF background, with no shadow, no effects and no text.
```

- **Tristitia stance:** "Fencer's ready stance: side-on, knees slightly bent, rapier held forward at chest height pointing left, free hand raised gracefully behind her. The rapier is a slim silver blade about as long as her leg, with a brass swept hilt and a black grip."
- **Elsie stance:** "Low guard: legs wide, spear in her front hand held forward and low pointing left, short sword in her back hand raised high behind her. The spear is a dark wooden shaft about her height with a steel leaf-shaped head; the sword is a broad leaf blade about forearm length with a brass guard."

### One move per video

Walks worked best one direction at a time, so each battle move gets **its own short video** too, about 3–5 seconds. It starts and ends in the battle stance so the moves chain. Use `Start - Battle Left.png` with the **Start frame** option.

Shared block (put it at the top of every battle prompt):

```
Pixel-art sprite animation of [NAME], matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose), outfit and weapon, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing.
Fixed side-view camera: no zoom, no cuts, no pan. The character faces left the whole time and stays centred. Forward movement is kept to a short step; the game engine moves the sprite toward the enemy.
Background: flat solid magenta #FF00FF. No floor, shadow, scenery or text. No visual effects: no glow, trails, sparks or flashes; only the body and weapon.
The outfit and weapon stay identical in every frame. Clean, readable poses with a steady rhythm. Start and end in the attached battle stance.
```

#### Tristitia (rapier, graceful and dance-like)

**T1 Attack: "Rose Waltz" (about 5 s).** The hits come from her whole dance. The last pose grants SPD UP.
```
[SHARED BLOCK]
Tristitia performs a graceful fencing dance, each pose flowing into the next like a waltz:
1. a gliding step forward with a low rising slash;
2. a full pirouette with the rapier sweeping in a wide arc, her coat flaring;
3. a crossing slash from high to low, landing in a deep, elegant lunge;
4. she rises, turns side-on and lifts her free hand high above her head, palm open, holding the pose for a beat as if blessing an ally;
5. she lowers the hand and settles back into the ready stance.
```
Game note: after the pose in step 4, a random party member gets a short **SPD UP** (the build's `speed_up`: attack bar fills 30% faster).

**T2 Skill: "Piercing Verdict" (about 4 s).** A feint, then the real hit.
```
[SHARED BLOCK]
1. Feint: a quick, showy flourish: she flicks the rapier upward in a fast vertical arc in front of her without stepping in (a decoy, no contact).
2. She drops low, then launches a long sliding lunge to the left, body almost horizontal, rapier fully extended in one straight thrust. Hold the extended thrust for a beat.
3. She recovers with a spin and a flick of the blade back into the ready stance.
```
Game note: only the lunge hits: heavy single-target damage plus a massive **DEF DOWN** and **SPD DOWN**. The engine slides the sprite forward during the lunge frames.

**T3 Guard (about 3 s).**
```
[SHARED BLOCK]
Tristitia turns side-on and brings the rapier up in front of her body, blade angled diagonally across her chest, knees bent and weight back, free hand braced behind her. She holds this parry guard steadily, with a small breathing motion, then returns to the ready stance.
```

#### Elsie (spear and short sword, Hildegard style)

**E1 Attack: two hits (about 4 s).**
```
[SHARED BLOCK]
1. Hit one: she steps in and cuts a wide horizontal slash with the short sword, sweeping it across in front of her, her ponytail swinging. No spin: her body stays facing left.
2. She draws the spear back and raises it slightly, bringing her weight onto her back foot to wind up.
3. Hit two: she drops into a low forward lunge and drives the spear straight out to the left in a long thrust. Hold the extended thrust for a beat.
4. She pulls the spear back and steps back into the low guard stance.
```

**E2 Skill: "Rallying Standard" (about 3 s), a simple spear raise.**
```
[SHARED BLOCK]
Elsie straightens up, lifts the spear straight overhead with one arm fully extended and the spearhead pointing to the sky, short sword held at her side, and holds the raised spear proudly for a beat as a rallying signal. She then lowers it and returns to the low guard stance.
```
Game note: a large party-wide **ATK UP** and **DEF UP**.

**E3 Guard (about 3 s).**
```
[SHARED BLOCK]
Elsie plants her feet wide and holds the spear diagonally upright in front of her body with both weapons braced, the short sword crossed behind the spear shaft, weight low. She holds this block steadily with a small breathing motion, then returns to the low guard stance.
```

Still to make for both of them (later, same method): battle idle (a looping stance), hurt, victory and defeat.

---

### What the pipeline does with these

- **Sheet:** the pipeline snaps it to its true grid at native size (no downscale) and sets the light-aware outline. This gives the idle frames and the walk key pose for all 4 directions.
- **Videos:**
  1. Take the frames and pick the loop and key frames (about 6–8 for a walk).
  2. Key out the flat background.
  3. Snap every frame on one locked grid.
  4. Recolour every frame to the character's sheet palette, so nothing flickers.
  4b. **Costume lock**: if the video drifts from the outfit (e.g. Elsie's trousers turned into shorts, so bare thighs showed), any skin that appears where the reference sprite has cloth is repainted in that cloth's colours, keeping the shading. The same step catches a returning mouth. Each fix is reviewed by eye. It can fix colour drift but not a changed silhouette (e.g. a coat that gets shorter), so the outfit-lock line in the prompt still matters.
  5. Outline and pack into the atlas at native size.
