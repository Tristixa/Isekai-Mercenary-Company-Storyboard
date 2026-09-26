# Gemini battle batch prompts (Omniflash)

Written 2026-09-26. Each character gets two batched videos of about 10 seconds:

- **Batch 1:** battle idle → attack → skill.
- **Batch 2:** battle idle → hurt → guard → victory → defeat.

Attach every start image with Omniflash's **Start frame** option, not Ingredients.

| Character | Faces | Weapon hand | Batch 1 start frame | Batch 2 start frame |
|---|---|---|---|---|
| Tristitia | left | rapier in her **right** hand | `Start - Battle Left.png` (step 0) | screenshot of her battle idle from batch 1 |
| Elsie | left | spear in the front hand, short sword in the back hand | `Start - Battle Left.png` (step 0) | screenshot of her battle idle from batch 1 |

For batch 2, take the screenshot from a frame in the first 2 seconds of batch 1, where she is standing in her battle idle. Save it in her folder as `Start - Battle Idle.png`. Pick a clean frame with no motion blur.

---

## Step 0: battle-stance still (Gemini image, once per character)

Attach the character's `Cropped/Start - Facing Left.png` as the reference. Send me the result so I can clean it into the start frame.

**Tristitia:**
```
Pixel-art sprite of Tristitia in a battle stance facing LEFT, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose; long white hair over one eye, violet eyes, beauty mark and freckles), black officer long coat with oxblood lining and brass trim, white shirt with oxblood tie, black gloves, full-length black trousers and tall black boots. Pixel size 8×8 image pixels per art pixel, about 96 art pixels tall. True pixel grid, no anti-aliasing, no mixels.
A fencer's ready stance side-on, knees slightly bent, the rapier in her RIGHT hand held forward at chest height pointing left, her left hand raised gracefully behind her. The rapier: a slim silver blade about as long as her leg, a brass swept hilt with a small cup guard and a black grip.
One sprite, centred, on a flat solid magenta #FF00FF background, with no shadow, no effects and no text.
```

**Elsie:**
```
Pixel-art sprite of Elsie in a battle stance facing LEFT, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose; high blonde ponytail, blue eyes), olive cropped jacket with gold trim and grey rolled cuffs, black fitted top, brown belts and pouch, brown gloves, FULL-LENGTH black trousers down to the boots (no shorts, no bare thighs) and brown boots. Pixel size 8×8 image pixels per art pixel, about 96 art pixels tall. True pixel grid, no anti-aliasing, no mixels.
Low guard stance: legs wide, the spear in her front hand held forward and low pointing left, the short sword in her back hand raised high behind her. The spear: a dark wooden shaft about her height with a steel leaf-shaped head. The short sword: a broad leaf blade about forearm length with a brass guard.
One sprite, centred, on a flat solid magenta #FF00FF background, with no shadow, no effects and no text.
```

---

## Shared block (top of every video prompt)

Both characters face **left**, toward the enemies.

```
Pixel-art sprite animation, matching the attached start frame exactly: same character, design, colours, face (NO mouth, NO nose), outfit and weapons, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing.
Fixed side-view camera: no zoom, no cuts, no pan, no camera shake. The character faces left the whole time and stays centred. Forward movement is kept to a short step, because the game engine moves the sprite toward the enemy.
Background: flat solid magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text, no captions. No visual effects: no glow, trails, sparks, magic or impact flashes; only the body and the weapons.
The outfit and weapons stay identical in every frame. Clear, readable poses with a steady rhythm and no stumbles. Each part returns to the battle idle stance before the next part begins.
```

---

## Tristitia: rapier, graceful and dance-like, facing left

### Batch 1: battle idle → attack → skill (about 10 s)
```
[SHARED BLOCK]
Tristitia holds the rapier in her RIGHT hand throughout.
0–2 s, battle idle: fencer's ready stance facing left, rapier forward at chest height pointing left, left hand raised gracefully behind her, coat hem swaying, a gentle breathing bounce. It loops.
2–6 s, attack "Rose Waltz", a graceful fencing dance where each pose flows into the next like a waltz:
  (a) a gliding step forward with a low rising slash;
  (b) a full pirouette with the rapier sweeping in a wide arc, her coat flaring;
  (c) a crossing slash from high to low, landing in a deep, elegant lunge;
  (d) she rises, turns side-on and lifts her free left hand high above her head, palm open, holding it for a beat as if blessing an ally;
  (e) she lowers the hand and settles back into the ready stance.
6–10 s, skill "Piercing Verdict":
  (a) feint: a quick, showy upward flick of the rapier in a vertical arc in front of her, without stepping in;
  (b) she drops low and launches a long sliding lunge to the left, body almost horizontal, rapier fully extended in one straight thrust, and holds it for a beat;
  (c) she recovers with a turn and a flick of the blade, back into the ready stance.
```

### Batch 2: battle idle → hurt → guard → victory → defeat (about 10 s)
Start frame: `Start - Battle Idle.png` (the screenshot from batch 1).
```
[SHARED BLOCK]
Tristitia holds the rapier in her RIGHT hand throughout.
0–1.5 s, battle idle: the fencer's ready stance with a gentle breathing bounce.
1.5–3 s, hurt: she recoils backward from a hit (body jolts to the right, away from the enemy, head dips), then recovers to the ready stance.
3–5 s, guard: she turns side-on and brings the rapier up in front of her body, blade angled diagonally across her chest, knees bent and weight back, left hand braced behind her. She holds the parry steadily, then returns to the ready stance.
5–7.5 s, victory: she lowers the blade, raises the rapier vertically before her face in a fencer's salute, then sweeps it down to her side and stands tall, holding the pose.
7.5–10 s, defeat: she staggers, drops to one knee and leans on the rapier with its point on the ground, head bowed, and holds that pose to the end.
```

Game notes (not part of the prompt):
- Rose Waltz: the hand raise gives a random ally a short **SPD UP** (`speed_up`).
- Piercing Verdict: the feint does not hit. The lunge is the real hit: heavy damage plus a massive **DEF DOWN** and **SPD DOWN**.

---

## Elsie: spear and short sword (Hildegard style), facing left, never spins

### Batch 1: battle idle → attack → skill (about 10 s)
```
[SHARED BLOCK]
Elsie holds the spear in her front hand and the short sword in her back hand throughout. She never spins; her body always faces left.
0–2.5 s, battle idle: low guard stance facing left, spear forward and low pointing at the enemy, short sword raised high behind her, knees bent, ponytail swaying, a small breathing bounce. It loops.
2.5–6.5 s, attack (two hits):
  (a) hit one: she steps in and cuts a wide horizontal slash with the short sword, sweeping it across in front of her;
  (b) she draws the spear back and raises it slightly, her weight on her back foot, winding up;
  (c) hit two: she drops into a low forward lunge and drives the spear straight out to the left in a long thrust, holding it for a beat;
  (d) she pulls the spear back and steps into the low guard stance.
6.5–10 s, skill "Rallying Standard": she straightens up and lifts the spear straight overhead with one arm fully extended, the spearhead pointing at the sky, the short sword held at her side, and holds it proudly for a beat as a rallying signal. Then she lowers it and returns to the low guard stance.
```

### Batch 2: battle idle → hurt → guard → victory → defeat (about 10 s)
Start frame: `Start - Battle Idle.png` (the screenshot from batch 1).
```
[SHARED BLOCK]
Elsie holds the spear in her front hand and the short sword in her back hand throughout. She never spins.
0–1.5 s, battle idle: the low guard stance with a small breathing bounce.
1.5–3 s, hurt: she recoils backward from a hit (body jolts to the right, away from the enemy, ponytail whips), then recovers to the guard stance.
3–5 s, guard: she plants her feet wide and holds the spear diagonally upright in front of her body, the short sword crossed behind the spear shaft, weight low. She holds the block steadily, then returns to the guard stance.
5–7.5 s, victory: she plants the spear upright beside her, rests the short sword on her shoulder and stands tall, holding the pose.
7.5–10 s, defeat: she stumbles, drops to one knee and leans on the planted spear, head bowed and ponytail falling forward, and holds that pose to the end.
```

Game notes: the attack hits twice (sword, then spear). Rallying Standard gives a large party-wide **ATK UP** and **DEF UP**.

---

---

# Revision 2 (2026-09-26): stronger officer moves

Review of the first results:
- **Tristitia:** batch 1's attack and all of batch 2 are good. Her skill came out static. She raised the blade, spread her arms and never really lunged.
- **Elsie:** all of her clips are clean but lack force. Her victory pose grew a third hand holding the spear, and her spear is too plain for an officer.

**How to get force.** A video model tends to move everything at one even speed. A strike feels strong from contrast: a slow wind-up, a held pause, a very fast strike, a freeze at full extension, then an overshoot and settle. The prompts below spell out that timing. On top of it:
- **Sprite pipeline (me):** I cut frames. Key poses get held longer (the wind-up and the impact freeze), and in-between frames are dropped so the strike itself takes only 1–2 frames. This is where most of the snap comes from.
- **Godot:** hit-stop on impact (a 3–6 frame freeze), screen shake, a camera push-in, an impact flash, afterimages, the dash toward the enemy, and the skill VFX. Octopath gets much of its weight from these, not from the sprite.

## Tristitia: new skill clip only (about 5 s)

Start frame: `Start - Battle Idle.png`, the screenshot of her idle from batch 1. This replaces the skill section of batch 1. Her attack, idle and batch 2 stay.

```
[SHARED BLOCK]
Tristitia holds the rapier in her RIGHT hand throughout. Contrast is essential: slow, elegant build-up, then explosive speed.
0–0.5 s: ready stance.
0.5–1.5 s, flourish (a feint, no contact): she spins a full graceful turn on the spot, coat and hair flaring outward, whipping the rapier around her in a wide circle. The spin ends facing left with the rapier sweeping up into a high vertical arc above her head.
1.5–2.5 s, charge: she sinks very low into a deep crouch, rapier drawn back beside her hip with the point aimed at the enemy, her free left hand stretched forward to aim. She HOLDS completely still in this coiled pose for most of a second, as if gathering power.
2.5–3 s, lunge: she explodes forward in one extremely fast sliding lunge, back leg fully straight, body almost horizontal, rapier arm fully extended in a straight thrust with her whole weight behind it. The lunge happens in just a few frames.
3–3.5 s: she FREEZES at full extension for a beat, coat tails still flying forward from the momentum.
3.5–5 s: she pulls back with a smooth half-turn and a flick of the blade, and settles into the ready stance.
```

## Elsie: officer spear, then remake both batches

### New stance still (Gemini image)

Attach `Battle Stance.jpg` as the reference. It keeps the pose and changes only the spear.

```
Pixel-art sprite of Elsie, identical to the attached sprite in pose, design, colours, face (NO mouth, NO nose), outfit, short sword, pixel size and scale, on a flat solid magenta #FF00FF background with no shadow, no effects and no text. Change ONLY the spear into an officer's winged spear: a long steel leaf-shaped blade with two short gold-edged wings at its base, a polished gold collar with a small olive-green tassel below it, a dark lacquered shaft with two thin gold bands, and a gold butt cap. It keeps the same length and the same grip as before. True pixel grid, no anti-aliasing, no mixels.
```

Save it as `Battle Stance 2.jpg`. Start batch 1 from it, and take batch 2's start from batch 1's idle as before. The spear change means all of her battle clips get remade, so the victory clip with the extra hand is simply replaced.

### Batch 1: battle idle → attack → skill (about 10 s)
```
[SHARED BLOCK]
Elsie holds the winged spear in her front hand and the short sword in her back hand throughout. She never spins; her body always faces left. Contrast is essential: a clear wind-up, then very fast strikes that freeze on impact.
0–2 s, battle idle: low guard stance, spear forward and low toward the enemy, short sword raised high behind her, knees bent, ponytail swaying, a small breathing bounce.
2–6.5 s, attack (two hits):
  (a) wind-up: she twists her shoulders back, the short sword drawn far back, and holds for a split second;
  (b) hit one: a very fast, wide horizontal slash across in front of her, following through hard so the ponytail whips; freeze briefly at the end of the swing;
  (c) wind-up: she draws the spear back and slightly up, weight rocking onto her back foot, and holds;
  (d) hit two: she explodes into a deep low lunge and drives the spear straight out in a long, powerful thrust in just a few frames; FREEZE at full extension for a beat;
  (e) she pulls the spear back and settles into the low guard stance.
6.5–10 s, skill "Rallying Standard": she plants her feet, sweeps the spear up and thrusts it straight overhead with one arm fully extended, the spearhead and tassel pointing at the sky, short sword held out at her side, and holds the pose proudly as a rallying signal. Then she lowers it and returns to the low guard stance.
```

### Batch 2: battle idle → hurt → guard → victory → defeat (about 10 s)
Use the same batch 2 prompt as before, with these two changes:
- Add this line after the shared block: "She has exactly two hands: the spear is in one hand and the short sword in the other at all times."
- Replace the victory line with: "5–7.5 s, victory: she stands tall and plants the spear upright beside her, gripping it with her front hand, and rests the short sword on her shoulder with her back hand. She holds the pose calmly with a slight confident lift of the chin."
