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

---

# Revision 3 (2026-09-26): Elsie switches to a greatsword

She drops the spear and short sword: dual-wielding made the video model duplicate hands and weapons. Her new weapon is **one two-handed greatsword**.
- **Attack:** a destructive "home-run" swing.
- **Skill:** the rally raise, giving the whole party ATK UP and DEF UP.
- **Background:** keep **magenta #FF00FF** for Elsie. Her jacket is olive green, so a green key would eat her colours.

## Step 0: the greatsword stance still (Gemini image)

Attach `Cropped/Start - Facing Left.png` as the reference.

```
Pixel-art sprite of Elsie in a battle stance facing LEFT, matching the attached sprite exactly: same design, colours, face (NO mouth, NO nose; high blonde ponytail, blue eyes), olive cropped jacket with gold trim and grey rolled cuffs, black fitted top, brown belts and pouch, brown gloves, full-length black trousers and brown boots. Pixel size 8×8 image pixels per art pixel, about 96 art pixels tall. True pixel grid, no anti-aliasing, no mixels.
She holds ONE two-handed greatsword with BOTH hands on the long grip: a broad, heavy steel blade with a simple bevel line, the blade alone about as long as she is tall, a plain steel cross-guard with small gold caps, and a grip wrapped in brown leather. Stance: feet wide and knees bent, the greatsword held low and angled back over her rear shoulder, ready to swing, with her weight on the back foot.
Exactly two arms and two hands, both on the grip. One sprite, centred, on a flat solid magenta #FF00FF background, with no shadow, no effects and no text.
```

Save it as `Battle Stance GS.jpg`. I clean it into `Start - Battle GS.png`.

## Batch 1: battle idle → attack → skill (Omniflash, about 10 s, start frame = `Start - Battle GS.png`)

```
Pixel-art sprite animation of Elsie, matching the attached start frame exactly: same design, colours, face (NO mouth, NO nose), outfit and greatsword, pixel size (8×8 image pixels per art pixel) and scale (about 96 art pixels tall). True pixel grid, no blur, no anti-aliasing.
Fixed side-view camera: no zoom, no cuts, no pan, no camera shake. She faces LEFT the whole time and stays centred; forward movement is only a short step, because the game engine moves the sprite toward the enemy.
Background: flat solid magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text. No visual effects: no glow, trails, sparks, dust or impact flashes; only her body and the sword.
She holds ONE greatsword with BOTH hands at all times; exactly two arms and two hands. The blade stays the same length (as long as she is tall) and the same design in every frame.
Contrast is essential: slow, heavy wind-ups, then explosive swings that freeze at the end.

0–2.5 s, battle idle: feet wide, the greatsword resting back over her shoulder with both hands on the grip, ponytail swaying, a slow heavy breathing bounce. It loops.
2.5–6.5 s, attack "Home-Run Cleave": she plants her lead foot, twists her hips and shoulders far back and HOLDS the loaded pose for a moment, blade cocked behind her like a batter; then she uncoils in one explosive horizontal swing through the enemy line in just a few frames; she FREEZES at the end of the follow-through with the blade extended high over the opposite shoulder and her body fully twisted; then she lets the sword's weight carry it down and settles back into the idle.
6.5–10 s, skill "Rallying Standard": she plants the greatsword's tip in the ground in front of her, grips the pommel with both hands, then heaves the sword up and thrusts it straight overhead with both arms extended, the blade pointing at the sky, and holds the rally pose proudly for a beat. Then she brings it back down to the idle.
```

## Batch 2: battle idle → hurt → guard → victory → defeat (about 10 s, start frame = a clean idle frame from batch 1)

```
[Same first five lines as batch 1: pixel rules, camera, background and no effects, one greatsword with two hands, contrast.]

0–1.5 s, battle idle: the greatsword resting over her shoulder, breathing.
1.5–3 s, hurt: she is STRUCK by an enemy hit: her body jolts backward to the right, away from the enemy, her head snaps back and her ponytail whips; she staggers one step and recovers into the idle. She does not attack.
3–5 s, guard: she brings the greatsword down in front of her body, holding the flat of the blade upright as a shield with one hand on the grip and the other braced against the flat, knees bent, weight low. She holds the block steadily, then returns to the idle.
5–7.5 s, victory: she swings the greatsword up and rests it across her shoulders behind her neck, both wrists draped over it, and stands tall with a confident lift of the chin. She holds the pose.
7.5–10 s, defeat: she staggers, drives the greatsword tip into the ground and sinks to one knee, both hands on the grip, head bowed and ponytail falling forward. She holds that pose to the end.
```

Game notes: Home-Run Cleave is one massive hit (a big hit-stop, screen shake and launch knockback in Godot). Rallying Standard gives a large ATK UP and DEF UP to the whole party.

---

# Revision 4 (2026-09-26): Elsie's own greatsword moves (replaces Revision 3's batches)

Her stance is `Elsie/Battle Stance GS.jpg`: Siegfried's reverse side hold. One hand is on the grip with the blade trailing low behind her to the right, and her free fist is forward. The sword is inspired by Caladbolg. The moves are **our own** and don't follow any reference choreography. The goal of the attack is the **feeling of a devastating impact**, not a particular motion.

**Keep the whole sword in frame.** Every prompt keeps the blade inside the frame and away from "overhead" poses: pointing the greatsword at the sky cropped it last time. Her skill now raises her **free hand**, not the sword.

Start frame: `Battle Stance GS.jpg` itself, attached with the Start frame option. It already has the right size, framing and headroom.

## Shared block (top of both Elsie prompts)

```
Pixel-art sprite animation of Elsie, matching the attached start frame exactly: same design, colours, face (NO mouth, NO nose), outfit and greatsword, pixel size (8×8 image pixels per art pixel) and scale. True pixel grid, no blur, no anti-aliasing.
Fixed side-view camera: no zoom, no cuts, no pan, no camera shake. She faces LEFT the whole time and stays in the same spot; forward movement is only a short step, because the game engine moves the sprite toward the enemy.
The ENTIRE greatsword stays inside the frame in every frame: it never goes above her head and is never cut off by the edge of the image.
The greatsword keeps exactly the same size and design in every frame: a broad, heavy steel blade with a gold-edged triangular guard and a leather-wrapped grip. She has exactly two arms and two hands.
Background: flat solid magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text. No visual effects: no glow, trails, sparks, dust, shockwaves or impact flashes; only her body and the sword.
Each part ends back in the attached stance before the next part begins.
```

## Batch 1: battle idle → attack → skill (about 10 s)

```
[SHARED BLOCK]
0–2.5 s, battle idle: the reverse side hold from the start frame. The blade trails low behind her, one hand on the grip, free fist forward, knees bent. The sword's weight makes her shoulders rise and fall slowly with her breathing; the ponytail sways. It loops.

2.5–7 s, attack "Ruinous Cleave". The whole point is WEIGHT and FORCE:
  (a) she sinks lower and grips the sword with both hands, dragging the heavy blade further back behind her; her whole body coils and strains against its weight, and she holds that coiled pose for a moment;
  (b) she drives her body forward and the blade sweeps up from low behind her, through the front, in one massive rising diagonal cut that ends at chest height in front of her. It happens in just a few frames, and her body leans hard into it as if the sword is pulling her;
  (c) she FREEZES at the end of the cut for a beat, arms fully extended, blade level in front of her, her back foot lifting slightly from the momentum;
  (d) the blade's weight carries it back down, she lets it drag behind her again and plants her feet, returning to the reverse side hold.

7–10 s, skill "Rallying Standard": she keeps the greatsword low behind her in the reverse hold, straightens up, and thrusts her FREE hand high into the air with a clenched fist, chin raised, as if calling the charge. She holds that pose for a beat, then lowers the fist back into the stance. The sword stays low and inside the frame the whole time.
```

## Batch 2: battle idle → hurt → guard → victory → defeat (about 10 s)

Start frame: a clean battle-idle frame from batch 1 (saved as `Start - Battle Idle.png`).

```
[SHARED BLOCK]
0–1.5 s, battle idle: the reverse side hold, slow breathing.
1.5–3 s, hurt: she is STRUCK by an enemy hit. She does not attack. Her body jolts backward to the right, away from the enemy, her head snaps back and her ponytail whips; the sword drags on the ground for a moment as she staggers one step, then she recovers into the stance.
3–5 s, guard: she swings the greatsword around in front of her body and plants it upright with the tip on the ground, holding the flat of the blade toward the enemy like a shield, both hands on the grip, crouching behind it. She holds the block steadily, then returns to the stance.
5–7.5 s, victory: she plants the greatsword tip-down in the ground beside her, rests one hand on the pommel, puts the other hand on her hip and stands tall with a confident lift of the chin. She holds the pose.
7.5–10 s, defeat: she staggers, drives the sword tip into the ground and sinks to one knee, both hands on the grip, head bowed, ponytail falling forward. She holds that pose to the end.
```

Game notes: Ruinous Cleave is one massive hit (a long hit-stop, the target knocked back, a strong but smooth shake). Rallying Standard gives a large ATK UP and DEF UP to the whole party.

# Revision 5 (2026-09-27): Elsie with a longsword and martial arts (replaces Revisions 3 and 4)

The greatsword is dropped: every greatsword attempt failed in a different way. Elsie now fights with a **longsword plus punches and kicks**, in the spirit of Yoshimitsu (Tekken): sword strikes flow into kicks and punches with her free hand and feet. One weapon avoids the duplicated-hands problem of the spear-and-sword version.

Her stance is `Elsie/Battle Stance.jpg`: a wide, low martial-arts stance facing left, the longsword held low in her back hand with the point angled up behind her, her free fist raised in front. Batch 1 is already made (`Attack.mp4`, and `Skill, Hateful slash(provoke enemy).mp4`). Only batch 2 remains.

**Key colour:** keep **magenta #FF00FF** (her jacket is olive green).

## Shared block (top of the Elsie batch 2 prompt)

```
Pixel-art sprite animation of Elsie, matching the attached start frame exactly: same design, colours, face (NO mouth, NO nose), outfit and longsword, pixel size (8×8 image pixels per art pixel) and scale. True pixel grid, no blur, no anti-aliasing.
Fixed side-view camera: no zoom, no cuts, no pan, no camera shake. She faces LEFT the whole time and stays in the same spot; any step is short, because the game engine moves the sprite.
She holds ONE longsword in her back hand the whole time: a straight steel blade with a simple silver cross-guard and a brown leather grip. The sword keeps exactly the same size and design in every frame and never leaves the frame. Her other hand is a free fist. She has exactly two arms, two hands and two legs. She never spins.
Background: flat solid magenta #FF00FF for the whole video. No floor, no shadow, no scenery, no text. No visual effects: no glow, trails, sparks, dust or flashes; only her body and the sword.
Each part ends back in the attached stance before the next part begins.
```

## Batch 2: battle idle → hurt → guard → victory → defeat (about 10 s)

Start frame: `Battle Stance.jpg`, attached with the Start frame option (or a clean battle-idle frame from `Attack.mp4`, saved as `Start - Battle Idle.png`, if it matches better).

```
[SHARED BLOCK]
0–1.5 s, battle idle: the wide martial-arts stance from the start frame. She bounces lightly on the balls of her feet like a fighter waiting for an opening, fist up, sword low behind her; the ponytail sways. It loops.
1.5–3 s, hurt: she is STRUCK by an enemy hit. She does not attack. Her body jolts backward to the right, away from the enemy, her head snaps back and her ponytail whips; she skids half a step on her back foot, then snaps back into the stance.
3–5 s, guard: she turns side-on and raises the longsword crosswise in front of her body, the flat of the blade braced against her free forearm, and lifts her front knee to protect her body, like a martial-arts block. She holds the block steadily, then returns to the stance.
5–7.5 s, victory: she flicks the sword down to her side, point to the ground, rolls her shoulder, and raises her free fist beside her face, chin up, standing tall and confident. She holds the pose.
7.5–10 s, defeat: she staggers, drops to one knee, the sword point on the ground and her free hand on the ground for support, head bowed, ponytail falling forward. She holds that pose to the end.
```

Game notes: Elsie is a front-row fighter. Her attack mixes sword cuts with kicks and punches (as in `Attack.mp4`). Her skill **Hateful Slash** provokes: after the slash, every enemy must attack her for their next 2 actions (see GDD 9.6).
