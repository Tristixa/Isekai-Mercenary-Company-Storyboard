# Environment prompts: Bernmoor and Erythra Highlands

Written 2026-09-27 for generation with Codex, following the method that produced the approved **Hylaea Approved Calibration v1**. **Revision 2 (same day)** adds what placing Hylaea in the game taught us: pixel density, a denser composition, and two new sheets for the near foreground. See "Revision 2" below; it overrides anything older in this file.

## Decision (2026-09-27): the painted style

The owner chose the **painted, Unicorn Overlord-like style** for environments. For every set from now on:
- Keep the cleaned painted art at full resolution: `sources/`, `clean/` and `objects/` (cutouts with anchors) plus the manifest.
- **Skip the 8×8 grid snap** and the `pixel8/` and `logical/` exports. The "exact 8×8 blocks" wording in the older prompts below no longer applies. The pixel-density table in Revision 2 is kept only for reference.
- Everything else still applies: magenta key, loops, light direction, density, no pink or violet, and the two new sheets.

## Revision 2: lessons from placing Hylaea in the game

Hylaea was placed in the operations proof (hunt search walk, battles, scout walk), in both the 8×8 pixel style and the painted source style. See `Hylaea/Codex Concept.png` for the target density.

1. **Pixel density (pixel style only).**
   - **The problem:** at a fixed 8×8 block, every object ends up about 50–90 art pixels tall, whatever its real size. Our characters are about 93 art pixels for 168 cm (1 art pixel ≈ 1.8 cm), so a Hylaea tree at the characters' density is only as tall as a person. In the game, trees had to be drawn with pixels about five times coarser than the characters', and near-camera plants turned into giant blocks.
   - **The fix:** target art-pixel counts by real size, and let the pipeline choose each object's block size (source height ÷ target art pixels) instead of 8 for everything.

   | Object | Real size | Target art pixels (height) |
   |---|---|---|
   | Character (reference) | 1.68 m | 93 |
   | Large tree | 8–10 m | 400–550 (crowns may be cropped by the camera; still paint them whole) |
   | Mid-distance tree | 5–6 m | 150–200 (it is far away, so it can be coarser) |
   | Boulder / bush / stump | 1–1.8 m | 55–100 |
   | Grass tuft / flowers / mushrooms | 0.3–0.6 m | 18–35 |
   | Near-camera foreground piece | 0.8–1.5 m | 60–90, blurred by depth of field |

   If the **painted style** is chosen instead (the proof has a switch to compare), skip the grid snap entirely and keep the cleaned painted art at full resolution. Everything else in this file still applies.
2. **Denser composition.**
   - **Far background:** about **a third** quiet, not half. Keep one calmer depth opening, but fill the rest with layered trunks and foliage (or ridges and willows). The game blurs this layer, so busy-but-soft is fine.
   - **Mid layer:** more trees or rock pillars, closer together. Gaps show the far layer, not empty space.
   - **Assembly:** the game adds full trees at the sides, a dense edge of props around the clearing and a near foreground band. Only the fighting floor itself stays open.
3. **Two new sheets per region** (7 and 8 below), for the near foreground just behind the party HUD and for the big trunks that frame the screen edges. They are shown large and blurred, so they need bold shapes more than fine detail.
4. **Colour hygiene:** no stray saturated pixels (Hylaea's mid trees had 11 near-pure-yellow ones).

### Hylaea addendum (the same two sheets for the approved set)

```text
M7 → Hylaea/Foreground.png. Create a Hylaea cutout sheet, painted in the approved Hylaea style (attached), of exactly six LOW, WIDE near-foreground pieces in three columns and two rows: a mossy exposed-root arch, a tangle of thick mossy roots, a broad fern clump, a long low bush mass, a fallen mossy branch with leaves, and a wide clump of tall grass with a few ferns. They sit just in front of the camera at the bottom of the screen, so each is wider than tall (about 2.5:1), with bold shapes, grouped values and modest detail; the game blurs them. Seen from slightly above, at about human eye height. Upper-left warm late-afternoon light. Complete silhouettes with bases, generous gutters, flat solid magenta #FF00FF everywhere else; no floor, soil islands, cast shadows, pink or violet. Painted source art, no pixel mosaic. No characters, animals, text or UI.
```

```text
M8 → Hylaea/Near Trunks.png. Create a Hylaea cutout sheet, painted in the approved Hylaea style (attached), of exactly two massive old hardwood trunk bases side by side: one leaning slightly left, one leaning slightly right. Each shows a huge buttressed base, thick exposed roots spreading onto the ground and the trunk rising past the TOP edge of the cell (the crown is out of frame). They frame the left and right screen edges near the camera. Bold bark planes and moss, modest detail (the game blurs them). Slight three-quarter side view at about human eye height; upper-left light. Flat solid magenta #FF00FF in all empty space; no floor, cast shadows, pink or violet. Painted source art, no pixel mosaic. No characters, animals, text or UI.
``` Give Codex this file together with the Hylaea references listed below. Each prompt is self-contained, so it can be pasted on its own.

## What to attach as references

| Reference | File | Use it for |
|---|---|---|
| Approved Hylaea sources | `Hylaea/Approved Calibration v1/sources/*.png` | Painted style, level of detail, edge quality, light direction |
| Approved Hylaea exports | `Hylaea/Approved Calibration v1/pixel8/*.png` | What the final 8×8 result must match in density and scale |
| Approved Hylaea far background | `Hylaea/Far Background - Approved Source.png` | How quiet and low in contrast a far layer must be |
| Hylaea pipeline record | `Hylaea/Approved Calibration v1/manifest.json` and `README.md` | Extraction, grid snap and checks to repeat |

**Style transfer only.** The Hylaea art sets the painted style, detail budget, value structure and camera. It must NOT set the subject: no oaks, no moss-forest content in the new regions.

## Method (the same as Hylaea)

Tell Codex to use the **`$imc-environment-art-direction`** skill (source `D:/Godot Projects/IMC-Companion-Skill-Environment`, already installed for Codex). It is the skill that made Hylaea and supplies the Unicorn Overlord rendering rules.

1. **Source art first.** Generate each item as hand-painted source art in the approved Hylaea manner (Unicorn Overlord-like broad matte planes, grouped light/midtone/shadow values, selective contours). Do **not** ask the image model for pixel mosaic or dithering; the exact 8×8 grid is made afterwards by the pipeline.
2. **Same pipeline:** canonical chroma extraction, component grouping, grid-snap downscale, `background.make_tile` for tiles and loops. Produce `sources/`, `clean/`, `objects/`, `logical/`, `pixel8/` (every block exactly 8×8) and a `manifest.json` with the same checks.
3. **Review before approval:** the user approves each set. Unapproved candidates, tools and previews stay in `D:/Codex/IMC`. Only the approved set is copied to:
   - `Environment Assets/Bernmoor/Approved Calibration v1/`
   - `Environment Assets/Erythra Highlands/Approved Calibration v1/`
4. **File names** are the same six as Hylaea (`Far Background.png`, `Mid Layer.png`, `Ground Tile.png`, `Props.png`, `Canopy.png`, `Tree Variants.png`), plus the two new sheets `Foreground.png` and `Near Trunks.png`. The mid layer is renamed from "Mid Trees" because the Erythra one is mostly rock.

## Shared rules (both regions)

- **Negative space (revised).** The far background keeps about a third quiet, with one calm depth opening; the rest is layered, soft detail. The mid layer is dense. Only the fighting floor stays open. The lower region of the far background stays calm so fighters read clearly.
- **Horizontal loop.** Far background, mid layer and canopy must join seamlessly at the left and right edges (same heights, colours and forms), with no prominent object touching either edge and no left-to-right brightness ramp. The game scrolls them while parties walk.
- **Camera.** Standing props, trees and the mid layer use the battle's slight three-quarter side view at about human eye height. The ground tile is straight overhead. The canopy is seen from below.
- **Light.** Upper-left key light, the same direction as Hylaea, so all regions share one lighting rig. Each region has its own time of day and colour (below). No baked sunbeams, fog overlays, bloom, vignette, light pools or depth-of-field blur; the game adds those.
- **Key colour.** Every cutout sheet (mid layer, props, canopy, tree variants) uses **flat solid magenta #FF00FF** in all empty areas and internal gaps. Because of that, **no pink, magenta or violet** in any object: no heather, no pink flowers, no violet shadows.
- **Clean colours.** No isolated saturated sparkle pixels (the Hylaea mid-tree layer came back with 11 near-pure-yellow pixels on its crowns; avoid this).
- **Isolation.** Props and trees: complete silhouettes, usable ground-contact bases, generous gutters, nothing touching another object or a cell edge. No soil islands, platforms or cast shadows on the background.
- **Nothing else.** No characters, monsters, animals, text, labels, UI, borders, grid lines or watermark.
- **Scale.** Match the Hylaea objects' pixel density, so a boulder here is the same pixel size as a Hylaea boulder beside a 168 cm character.

---

## Bernmoor (Rank E)

**Identity.** Wide reedbeds and slow, shallow water tinted amber by peat and tannin, broken by groves of weeping willows and silver dead snags. Humid, still and golden. Residents set out road lanterns and burn stalker-warning incense here. The monsters are Marsh Slimes, Marsh Serpents, Marsh Stalkers and the Ambermaw Matriarch, so fights happen on a firm mud-and-reed bank beside the water, not in it.

**Palette and light.** Late-morning sun through humid haze, from the upper left. Olive and ochre reeds, amber-honey water, dull sage willow leaves, silver-grey deadwood, dark peat-brown mud. Shadows are cool teal-grey, never violet. Warmer and softer than Hylaea; less enclosed, because the marsh opens to a pale hazy sky.

### A1. Far background → `Far Background.png`

```text
Use case: new region far background, matching the approved Hylaea far background in style and restraint.
Create ONE wide 3:1 opaque FAR BACKGROUND layer for Bernmoor, a humid amber-watered reed marsh in an HD-2D JRPG. This is a reusable horizontally repeating distant backdrop, not a battle scene.
REFERENCE ROLES: the attached approved Hylaea far background and Hylaea sources define painted style, low detail, value restraint and upper-left light ONLY. Do not copy their oaks, enclosed forest or moss.
CONTENT: Looking horizontally across a wide marsh. Two or three uneven, loose groups of distant weeping willows and a few pale silver dead snags, low on the horizon. Between them, broad quiet bands of distant reedbed in muted ochre and olive, with narrow glimpses of still amber water catching a little light. The upper third is a pale, warm, hazy sky with very soft cloud masses; no strong cloud detail. The lower third is broad calm reedbed colour masses with almost no individual stems.
NEGATIVE SPACE: about a third of the panorama quiet; the rest layered but soft. Largest quiet reach slightly right of centre, a calmer one on the left. No dense wall of reeds, no evenly spaced trees, no giant centre tree.
LAYER SEPARATION: no walkable foreground bank, mud floor, path, boardwalk, props, lanterns, boats or buildings. Tree bases disappear behind distant reed masses.
PAINTED STYLE: hand-painted, Unicorn Overlord-like broad matte planes and grouped values, simpler than the approved complete Hylaea trees. No photographic texture, stippling, speckle noise, pixel mosaic or dithering (the 8x8 grid is made later). Suggest depth through paler, cooler colour, not blur.
LIGHT: late-morning sun from the upper left through humid haze; warm highlights on the nearer willow groups, cool teal-grey shadows, lighter and cooler with distance. No sunbeams, fog overlay, bloom, vignette or light pools. No violet or pink anywhere.
HORIZONTAL REPEAT: left and right edges join seamlessly at the same heights, colours and forms; quiet reedbed at both edges, no tree touching either side, no brightness ramp or mirrored symmetry.
Fully opaque, 3:1, target 3072x1024 if available. No people, animals, monsters, text, UI, border or watermark.
```

### A2. Mid layer → `Mid Layer.png`

```text
Create one continuous wide 3:1 mid-distance layer for Bernmoor, painted in the approved Hylaea source style (attached), for an HD-2D JRPG.
Include six or seven weeping willows and two or three silver dead snags in uneven, fairly close groups, with tall reed and cattail stands gathered around some bases. Vary trunk lean, crown size and spacing. Several irregular open gaps show empty space between groups. Willow fronds hang in long grouped curtains with visible gaps, not a solid wall. Trunks and reed stands reach the bottom edge; crowns may continue past the top edge. No water surface, bank, floor, path or ground line.
Slight three-quarter side view at about human eye height. Late-morning light from the upper left; warm frond edges, cool teal-grey shadows on right-facing surfaces. No cast shadows outside the objects, sunbeams, fog, bloom or blur.
Left and right edges join seamlessly when repeated; no object is cut at only one side.
Every empty area, including gaps between fronds and reeds, is flat solid magenta #FF00FF: no sky, transparency, checkerboard, gradient or magenta spill. No pink, magenta or violet in the objects. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI, border or watermark.
```

### A3. Ground tile → `Ground Tile.png`

```text
Create one square seamless top-down ground material for the Bernmoor battle floor, painted in the approved Hylaea ground tile's restrained manner (attached).
Firm dark peat-brown mud, mostly walkable, with a few small, shallow, flat puddles of amber-tinted water, sparse flattened reed stubble, occasional tiny duckweed specks near the puddles and a few small pebbles. Broad quiet areas between details so fighters remain readable. No single dominant feature, deep water, large plants, logs or recognisable repeated landmark.
Directly overhead, even flat lighting, no directional highlights, reflections of sky or cast shadows; the game lights the floor. No bank outline, path shape, border, horizon or perspective.
Tiles seamlessly on all four edges. Opaque edge to edge; no magenta or transparency. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI or watermark.
```

### A4. Props sheet → `Props.png`

```text
Create one prop sheet for Bernmoor, painted in the approved Hylaea props style (attached), for an HD-2D JRPG. Exactly 15 separate complete objects in five columns and three rows, with generous empty gutters and no drawn grid:
Row 1: three reed and cattail clumps of different heights and widths; two low sedge tufts.
Row 2: three wet grey-brown stones with dark waterline stains, small, medium and large; one half-rotted fallen log with bracket fungus; one hollow willow stump.
Row 3: one clump of small yellow marsh marigolds; one tuft of white bog-cotton; one cluster of ordinary brown marsh mushrooms; one low tangle of exposed willow roots; one small flat-topped tussock of grass.
Slight three-quarter side view at about human eye height. Natural relative sizes within each category. Complete silhouettes and ground-contact bases; no water, platforms, soil islands or extra scenery.
Late-morning light from the upper left, restrained teal-grey shading on lower-right surfaces. Readable reed blades, stone planes and wood grain. No photographic noise, cast shadows on the background, fog, sunbeams, bloom or blur.
All empty space, including gaps between reeds, is flat solid magenta #FF00FF: no floor, ground line, gradient, transparency, checkerboard or magenta reflections. No pink, magenta or violet in the objects. Painted source art, no pixel mosaic or dithering. No characters, animals, text, labels, UI, border or watermark.
```

### A5. Canopy → `Canopy.png`

```text
Create one wide 3:1 continuous canopy overlay for an Bernmoor HD-2D JRPG battle scene, painted in the approved Hylaea canopy style (attached).
Long curtains of hanging willow fronds and a few grey-green hanging moss strands drop from the top edge, seen from slightly below, thicker in the upper left and upper right corners and thin through the centre. They occupy only the upper quarter overall; the rest stays empty. Fronds attach to branches that continue past the top and side edges, so no frond floats unattached. Uneven organic silhouette with gaps.
Late-morning light from the upper left, warm frond edges and teal-grey shadows. No sky, sunbeams, fog, bloom or blur; the game supplies near-camera depth of field.
Left and right edges join seamlessly when repeated.
All empty space is flat solid magenta #FF00FF, including gaps between fronds. No pink, magenta or violet. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI, border or watermark.
```

### A6. Tree variants → `Tree Variants.png`

```text
Create a cutout sheet for Bernmoor, painted in the approved Hylaea tree style (attached), with exactly four complete trees in a 2x2 layout: a broad weeping willow with long hanging fronds; a tall silver dead snag with a few broken limbs; a leaning swamp alder with exposed stilt-like roots; and a smaller young willow. Complete crowns and root bases, no cropping, distinct silhouettes, visible gaps between fronds and branches.
Slight three-quarter side view at about human eye height. Late-morning light from the upper left; restrained teal-grey right-side shading. Generous margins between trees. No surrounding scenery, water, soil islands or cast shadows.
Flat solid magenta #FF00FF in all empty areas and internal gaps: no transparency, checkerboard, gradient, floor, ground line or magenta spill. No pink, magenta or violet. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI, grid lines or watermark.
```

### A7. Foreground → `Foreground.png`

```text
Create an Bernmoor cutout sheet, painted in the approved Hylaea style (attached), of exactly six LOW, WIDE near-foreground pieces in three columns and two rows: a tangle of exposed willow roots, a dense clump of reeds and cattails, a wide sedge mound, a half-sunken mossy log, a low mass of marsh ferns, and a broad tussock of grass with marigolds. They sit just in front of the camera at the bottom of the screen, so each is wider than tall (about 2.5:1), with bold shapes, grouped values and modest detail; the game blurs them. Seen from slightly above, at about human eye height. Late-morning light from the upper left, teal-grey shadows. Complete silhouettes with bases, generous gutters, flat solid magenta #FF00FF everywhere else; no water, floor, soil islands, cast shadows, pink or violet. Painted source art, no pixel mosaic. No characters, animals, text or UI.
```

### A8. Near trunks → `Near Trunks.png`

```text
Create an Bernmoor cutout sheet, painted in the approved Hylaea style (attached), of exactly two massive near-camera trunk bases side by side: an old weeping willow with a split, gnarled base and stilt-like roots leaning slightly left, and a silver dead snag with a broken, buttressed base leaning slightly right. Each rises past the TOP edge of the cell (the crown is out of frame). They frame the left and right screen edges near the camera. Bold planes, modest detail (the game blurs them). Slight three-quarter side view at about human eye height; late-morning light from the upper left. Flat solid magenta #FF00FF in all empty space; no water, floor, cast shadows, pink or violet. Painted source art, no pixel mosaic. No characters, animals, text or UI.
```

---

## Erythra Highlands (Rank D)

**Identity.** Cold, high country of rust-red stone: terraced ledges like giant stairways, jagged ridges and scree, with wind-bent pines and pale golden alpine grass. Old snow lies only on the far peaks. Residents need frostproof mortar, summit bell straps and a beacon ember, so it is remote, wind-worn and a little austere. The monsters are Stone Crawlers, Highland Wolves, Ridge Drakes and the Crownstone Wyrm, so fights happen on a broad, flat gravel shelf between ledges.

**Palette and light.** Clear, crisp early-afternoon mountain light from the upper left. Rust red and terracotta stone, slate grey, dark pine green, pale gold dry grass, off-white snow far away. Shadows are cool slate blue, never violet or pink. More open than Hylaea (sky and distant peaks are welcome), but still with plenty of quiet space.

### R1. Far background → `Far Background.png`

```text
Use case: new region far background, matching the approved Hylaea far background in style and restraint.
Create ONE wide 3:1 opaque FAR BACKGROUND layer for Erythra Highlands, a cold high country of rust-red stone in an HD-2D JRPG. This is a reusable horizontally repeating distant backdrop, not a battle scene.
REFERENCE ROLES: the attached approved Hylaea far background and Hylaea sources define painted style, low detail, value restraint and upper-left light ONLY. Do not copy their forest content.
CONTENT: Looking horizontally across highland ridges. Two or three uneven groups of distant rust-red mesas and jagged ridges, with a few far snow-capped peaks, pale and cool with distance. Terraced stone ledges suggested in broad shapes, not detailed steps. A few tiny dark pine clusters on distant slopes. The upper third is a clear, cool, pale blue sky with a few soft high clouds. The lower third is broad, calm, darker ridge masses with little detail.
NEGATIVE SPACE: at least half the panorama quiet (sky and simple distant slopes). Largest quiet interval slightly right of centre, a calmer one on the left. No crowded jagged skyline, no evenly spaced peaks, no giant central mountain.
LAYER SEPARATION: no walkable foreground shelf, path, stairs, props, buildings, beacons or bells. Nearer ridge bases disappear behind the calm lower masses.
PAINTED STYLE: hand-painted, Unicorn Overlord-like broad matte planes and grouped values, simpler than the approved complete Hylaea trees. No photographic rock texture, cracks everywhere, stippling, speckle noise, pixel mosaic or dithering (the 8x8 grid is made later). Depth through paler, bluer colour, not blur.
LIGHT: crisp early-afternoon mountain light from the upper left; warm terracotta on lit faces, cool slate-blue shadows, lighter and cooler with distance. No sunbeams, fog overlay, bloom, vignette or light pools. No violet or pink anywhere.
HORIZONTAL REPEAT: left and right edges join seamlessly at the same heights, colours and forms; quiet slopes and sky at both edges, no peak or mesa touching either side, no brightness ramp or mirrored symmetry.
Fully opaque, 3:1, target 3072x1024 if available. No people, animals, monsters, text, UI, border or watermark.
```

### R2. Mid layer → `Mid Layer.png`

```text
Create one continuous wide 3:1 mid-distance layer for Erythra Highlands, painted in the approved Hylaea source style (attached), for an HD-2D JRPG.
Include five or six rust-red rock outcrops and pillars of different heights, some with stepped ledges, and four or five wind-bent pines growing from cracks and ledges, in uneven groups. Several irregular open gaps show empty space between groups. Pines lean the same way (wind from the right). Rock bases reach the bottom edge; one or two pines may continue past the top edge. No floor, gravel strip, path, stairs or ground line.
Slight three-quarter side view at about human eye height. Early-afternoon light from the upper left; warm terracotta lit faces, cool slate-blue shadows on right-facing surfaces. No cast shadows outside the objects, sunbeams, fog, bloom or blur.
Left and right edges join seamlessly when repeated; no object is cut at only one side.
Every empty area, including gaps between pine needles and rocks, is flat solid magenta #FF00FF: no sky, transparency, checkerboard, gradient or magenta spill. No pink, magenta or violet in the objects. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI, border or watermark.
```

### R3. Ground tile → `Ground Tile.png`

```text
Create one square seamless top-down ground material for the Erythra Highlands battle floor, painted in the approved Hylaea ground tile's restrained manner (attached).
Compacted rust-red and terracotta gravel with a few embedded flat slate-grey stone slabs, sparse tufts of flattened pale golden grass, occasional small pale lichen spots and small pebbles. Mostly quiet, walkable surface with broad calm areas so fighters remain readable. No single dominant feature, cracks everywhere, large rocks, snow or recognisable repeated landmark.
Directly overhead, even flat lighting, no directional highlights or cast shadows; the game lights the floor. No ledge outline, path shape, border, horizon or perspective.
Tiles seamlessly on all four edges. Opaque edge to edge; no magenta or transparency. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI or watermark.
```

### R4. Props sheet → `Props.png`

```text
Create one prop sheet for Erythra Highlands, painted in the approved Hylaea props style (attached), for an HD-2D JRPG. Exactly 15 separate complete objects in five columns and three rows, with generous empty gutters and no drawn grid:
Row 1: three rust-red boulders, small, medium and large, with clear stone planes; one tall split rock; one low scree pile of loose red stones.
Row 2: two different low juniper shrubs; one wind-flattened young pine; one weathered pine stump; one fallen dry pine branch.
Row 3: three tufts of pale golden alpine grass of different sizes; one small stone cairn (a stacked trail marker); one cluster of small white alpine flowers.
Slight three-quarter side view at about human eye height. Natural relative sizes within each category. Complete silhouettes and ground-contact bases; no platforms, soil islands, snow patches or extra scenery.
Early-afternoon light from the upper left, restrained slate-blue shading on lower-right surfaces. Readable rock planes, needle clusters and wood grain. No photographic noise, cast shadows on the background, fog, sunbeams, bloom or blur.
All empty space is flat solid magenta #FF00FF: no floor, ground line, gradient, transparency, checkerboard or magenta reflections. No pink, magenta or violet in the objects. Painted source art, no pixel mosaic or dithering. No characters, animals, text, labels, UI, border or watermark.
```

### R5. Canopy → `Canopy.png`

```text
Create one wide 3:1 continuous framing overlay for a Erythra Highlands HD-2D JRPG battle scene, painted in the approved Hylaea canopy style (attached).
Two or three sparse wind-bent pine boughs reach in from the upper left and upper right corners, seen from slightly below, with grouped dark needle clusters and a few small cones. They occupy only the upper corners; the centre and everything below the upper quarter stays empty. Boughs attach to branches that continue past the top and side edges. Uneven organic silhouette with gaps.
Early-afternoon light from the upper left; warm highlights on needle tips, slate-blue shadows. No sky, sunbeams, fog, bloom or blur; the game supplies near-camera depth of field.
Left and right edges join seamlessly when repeated.
All empty space is flat solid magenta #FF00FF, including gaps between needles. No pink, magenta or violet. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI, border or watermark.
```

### R6. Tree variants → `Tree Variants.png`

```text
Create a cutout sheet for Erythra Highlands, painted in the approved Hylaea tree style (attached), with exactly four complete trees in a 2x2 layout: a tall wind-bent pine leaning left; a straight old pine with a broken top; a twisted dwarf pine growing from a small red rock (the rock is part of the object); and a bare, lightning-struck grey pine snag. Complete crowns and roots, no cropping, distinct silhouettes, visible gaps between needle clusters.
Slight three-quarter side view at about human eye height. Early-afternoon light from the upper left; restrained slate-blue right-side shading. Generous margins between trees. No surrounding scenery, soil islands or cast shadows.
Flat solid magenta #FF00FF in all empty areas and internal gaps: no transparency, checkerboard, gradient, floor, ground line or magenta spill. No pink, magenta or violet. Painted source art, no pixel mosaic or dithering. No characters, animals, text, UI, grid lines or watermark.
```

### R7. Foreground → `Foreground.png`

```text
Create a Erythra Highlands cutout sheet, painted in the approved Hylaea style (attached), of exactly six LOW, WIDE near-foreground pieces in three columns and two rows: a long low rust-red rock shelf, a pile of broken red boulders, a wide juniper mass, a gnarled pine root spread over stone, a broad clump of pale golden grass, and a fallen dry pine trunk. They sit just in front of the camera at the bottom of the screen, so each is wider than tall (about 2.5:1), with bold shapes, grouped values and modest detail; the game blurs them. Seen from slightly above, at about human eye height. Early-afternoon light from the upper left, slate-blue shadows. Complete silhouettes with bases, generous gutters, flat solid magenta #FF00FF everywhere else; no floor, snow, soil islands, cast shadows, pink or violet. Painted source art, no pixel mosaic. No characters, animals, text or UI.
```

### R8. Near trunks → `Near Trunks.png`

```text
Create a Erythra Highlands cutout sheet, painted in the approved Hylaea style (attached), of exactly two massive near-camera framing pieces side by side: a thick old pine trunk growing out of a split red boulder, leaning slightly left, and a tall column of stacked rust-red rock with a wind-bent pine root clinging to it, leaning slightly right. Each rises past the TOP edge of the cell. They frame the left and right screen edges near the camera. Bold planes, modest detail (the game blurs them). Slight three-quarter side view at about human eye height; early-afternoon light from the upper left. Flat solid magenta #FF00FF in all empty space; no floor, cast shadows, pink or violet. Painted source art, no pixel mosaic. No characters, animals, text or UI.
```

---

## Acceptance (same as Hylaea)

- **Counts and silhouettes:** object counts are exact; every silhouette is complete; the camera, light direction and magenta are correct and consistent.
- **Edges and tiles:** loops and tiles pass the seam checks, and are reviewed side by side as well as by numbers.
- **Clean output:** after the pipeline, every block is exactly 8×8; there are no magenta fringes and no stray saturated pixels.
- **Matches Hylaea:** at gameplay size the new sets sit beside the Hylaea set without looking like a different game.
- **Gameplay review:** a small assembly with the current character sprites is reviewed before approval.
