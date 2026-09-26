# Gemini monster prompts: the boar for the idle-battle proof

Written 2026-09-26. The same rules apply as for the characters: Omniflash, **Start frame** option, flat magenta #FF00FF background, 8×8 image pixels per art pixel, no effects (hit flashes, dust and death dissolve are done in the engine), no text.

## What the proof needs

- **One base boar with full animation.** Enemies stand on the left and **face right** toward the party, as in Octopath. Enemies only need one direction, so no walk cycles.
- **Two regional variants as palette swaps.** I recolour the base boar's frames in the pipeline, which costs no credits. Octopath reuses enemies with recolours all the time. If a variant later needs a different shape (armour plates, a bigger tusk), it gets its own still and videos.
  - **Mosswood Boar** (base): dark brown bristles, mossy green on the back, pale tusks.
  - **Marsh Tusker**: muddy olive-grey, dried mud on the legs, yellowed tusks (Amber Marsh).
  - **Redstone Boar**: rust-red hide, ash-grey mane, dark tusks (Redstone).
- **Size:** a large wild boar. It stands roughly as tall as a character's waist to chest and is clearly heavier and wider than a human, so it reads as a threat: about **70 art px tall and 120 art px long**. Octopath draws its enemies bigger than the party for readability.

## Step 1: the idle still (Gemini image)

```
Pixel-art sprite of a large wild boar monster for an HD-2D JRPG battle, in the style of Octopath Traveler enemy sprites. Side view, FACING RIGHT, standing in a tense battle-ready idle: head low, tusks forward, shoulders hunched, bristly mane raised.
Design: a massive boar with dark brown coarse bristles, a patch of mossy green growth along its back, a thick mane from head to shoulders, two curved pale tusks, small fierce amber eyes, scarred snout, sturdy hooves.
Pixel rules: true pixel grid, every art pixel is an exact 8×8 block of image pixels, no anti-aliasing, no blur, no mixels. Clean dark outline in a darker shade of the neighbouring colour, soft light from the upper left.
Size: about 70 art pixels tall and 120 art pixels long.
One sprite, centred, on a flat solid magenta #FF00FF background, with no shadow, no ground, no effects and no text.
```

Save it as `Character Sprites/Boar/Idle.png` and send it to me first. I'll clean it (grid snap, key colour, outline) and export the start frame, just as with Tristitia's and Elsie's battle stances.

## Step 2: two videos (Omniflash, about 10 s each, start frame = the cleaned idle)

Shared block:
```
Pixel-art sprite animation of the wild boar, matching the attached start frame exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale. True pixel grid, no blur. Fixed side-view camera with no zoom, pan or cuts. The boar faces RIGHT the whole time and stays centred; forward movement is kept to a short lunge, because the game engine moves the sprite. Flat solid magenta #FF00FF background with no ground, shadow, dust, effects or text. Every part returns to the battle idle before the next begins.
```

**Batch 1: idle → attack → skill**
```
[SHARED BLOCK]
0–3 s, battle idle: heavy breathing, flanks rising and falling, snorting, head bobbing slightly, one front hoof pawing the ground. It loops.
3–6 s, attack "Tusk Gore": it lowers its head and holds still for a moment, then lunges forward very fast with a violent upward toss of the tusks, freezes at the top of the toss for a beat, and backs off into the idle.
6–10 s, skill "Wild Charge": it rears back and scrapes the ground twice with a front hoof, crouches low and trembling as it builds up, then bursts forward in a short explosive charge with its head down, stops hard and shakes its head, returning to the idle.
```

**Batch 2: idle → hurt → defeat**
```
[SHARED BLOCK]
0–2 s, battle idle (same as batch 1).
2–4 s, hurt: it recoils from a hit, its body jolting backward to the left, head jerking up with a squeal, then it stumbles and recovers to the idle.
4–6 s, second hurt: a smaller flinch with the head turning away, then back to the idle.
6–10 s, defeat: it staggers, its front legs buckle, and it collapses onto its side, lying still to the end.
```

In the game, the boar's attack hits one party member, and **Wild Charge** is a stronger single hit. The regional variants can get different skills later, for example Redstone's charge could cause a stun.
