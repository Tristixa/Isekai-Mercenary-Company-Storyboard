# Higgsfield prompts: Mosswood battleground and area kit

Updated 2026-09-27. This revision preserves the proof-2 asset-handling contract and expands the prompts for reusable Mosswood scenery. It supersedes the earlier chat prompts that offered transparent backgrounds, neutral lighting for all objects, and only a loosely pixel-like appearance.

The five core outputs remain:

1. far background panorama
2. mid background tree line
3. ground texture
4. foreground props
5. canopy overlay (optional)

These are cut, keyed out, and placed in the 3D scene. Scene depth, lighting, and depth of field finish the presentation. This is IMC's assembly approach inspired by Octopath's appearance, not a claim that these five image layers reproduce Octopath II's internal construction.

## Handling rules and reference use

The far panorama, the mid tree line and the canopy must loop horizontally (their left and right edges join). The game scrolls them sideways at different speeds while a hunting party or scout walks, then stops them when a fight starts.

- **Negative space — user direction:** every background must retain substantial quiet space. Do not fill the frame with trunks, foliage, or fine texture. Concentrate detail in a few uneven groups, leave broad openings of subdued distant colour, and keep the lower region visually calm. Negative space is low-detail scenery, not transparency or a visible battle floor. For the far-background revision, aim for roughly half or more of the frame to remain quiet; this is a composition target, not a universal measured quota. Later layers must preserve these openings in the assembled view.
- **Pixel grid:** every art pixel must become an exact **8×8 block of image pixels**, without anti-aliasing. This is the existing target for matching the character artwork. Ask for it in generation, then enforce it through the existing sprite-snapping pipeline if necessary. A prompt alone does not guarantee an exact grid. Check apparent pixel size again after scene scaling.
- **Object lighting:** warm late-afternoon light from the **upper left**, with subdued green/brown shadows on lower-right surfaces. Keep this restrained so the engine can add lighting. Do not replace it with the previous neutral-lighting brief.
- **Ground exception:** tiling ground textures use even, flat lighting and the same warm-compatible material palette. The 3D floor receives light and shadows in the game.
- **Key colour:** `Mid Trees.png`, `Props.png`, `Canopy.png`, and every supplementary cutout sheet use **flat solid magenta #FF00FF** in all empty areas, including holes between leaves and branches. No transparent-background alternative, checkerboard, gradient, magenta spill, floor, ground line, or cast shadow on the background.
- **Opaque images:** the far panorama is an opaque background with distant scenery and restrained sky gaps. Ground tiles are opaque edge-to-edge materials. Neither uses magenta.
- **Camera:** standing props use the existing slight three-quarter side view at approximately human eye height. Do not switch to top-down or isometric map objects. Ground textures are directly overhead; canopy is seen from below. These intentional asset-specific views match their different placement roles.
- **Effects:** keep pixel edges sharp. Do not bake depth-of-field blur, vignette, bloom, distinct sunbeams, particles, or local light pools into the images. The far panorama may imply atmospheric distance through paler colours and simpler shapes, without blurring the pixel grid.
- **Isolation:** individual props need complete silhouettes, usable ground-contact bases, and generous empty margins. Nothing touches another object or crosses a sheet cell. The continuous mid-tree and canopy layers have their own intentional edge-cropping rules.
- **No characters, animals, text, UI, grid lines, borders, signatures, or watermark.** Small ordinary mushrooms and wildflowers remain allowed where specifically listed; no giant or glowing fantasy ornaments.

Attach the proposed Mosswood concept as a **material, palette, foliage, and woodland-identity reference**. Do not copy its characters, HUD, complete arena layout, baked sunlight, or blur. The rules above take precedence over the concept's smooth rendering and over the previous chat prompts. Once one sheet is selected, use it as an additional pixel-style reference for later sheets.

Save the generated outputs in `Environment Assets/Mosswood/` with the names below. Keep the core filenames unchanged. Supplementary filenames are proposed additions for manual cutting and placement; this document does not establish automatic runtime loading for them.

Suggested working canvases: 3072×1024 for 3:1 layers, 1024×1024 for ground tiles, 2048×2048 for four-object sheets, and 3072×2048 for larger sheets. Use a supported size and preserve the intended ratio; final dimensions should be multiples of eight. These are output targets, not verified Higgsfield model capabilities. Each prompt below is self-contained.

## 1. Far background panorama → `Far Background.png`

```text
Create one wide panoramic pixel-art background for Mosswood, an ancient moss-covered forest in an HD-2D JRPG. Use the attached Mosswood concept only for woodland identity, material colours, and foliage shapes.

Use a sparse composition with only two or three uneven tree groups, concentrated toward the outer portions of the panorama. Leave roughly half or more of the frame as broad, low-contrast openings of pale cool-green distant woodland, with just a few faint slender tree silhouettes. Make the largest opening slightly off-centre and include smaller openings elsewhere. Avoid evenly spaced columns, a continuous overhead foliage roof, and a solid shrub wall. Preserve depth with separated silhouettes and colour, not by filling every gap with more trees. Do not draw a literal path or floor into the openings.

Warm late-afternoon light comes from the upper left. Nearer woodland shapes are deeper green; distant groups become paler and cooler teal-green through discrete pixel-colour clusters. Suggest atmospheric depth through colour and simplified shapes, not blurred pixels. No distinct sunbeams or fog overlay.

Very wide composition, about 3:1. Keep the bottom third quiet: broad subdued dark-green distant vegetation masses, sparse simplified low silhouettes, and very little individual leaf detail. No dense continuous hedge. Include NO visible ground plane, dirt clearing, path, floor, foreground props, or circular arena. This is one opaque far backdrop, not a cutout sheet; no magenta background. The left and right edges must join seamlessly: anything crossing the right edge continues from the left edge at the same height, so the layer can repeat sideways without a visible seam.

True pixel art: every art pixel is an exact 8×8 image-pixel block on one consistent grid. Hard pixel edges, no anti-aliasing, no photographic detail, no brushy painting, no depth-of-field blur, no vignette or bloom. No characters, animals, text, UI, borders, or watermark.
```

## 2. Mid background tree line → `Mid Trees.png`

```text
Create one continuous wide pixel-art mid-distance tree-line layer for Mosswood, an HD-2D JRPG forest. Use the attached concept for mossy bark, irregular foliage clusters, and woodland palette.

Include 5 to 6 large old forest trees arranged in uneven groups. Vary their diameter, lean, branching, and spacing. Some trunks overlap within groups, while several irregular openings reveal the empty background between groups. Avoid a solid hedge and a regular fence-like row. Thick mossy trunks have readable root flares, low branches, and grouped leaves; a few modest ferns and bushes gather around selected bases without sealing every gap.

Match the battle's slight three-quarter side view at approximately human eye height. Tree trunks reach the bottom edge and crowns may continue beyond the top edge. Do not add a floor, path, terrain strip, or ground line. About 3:1 landscape composition. The left and right edges must join seamlessly: anything crossing the right edge continues from the left edge at the same height, so the layer can repeat sideways without a visible seam.

Warm late-afternoon illumination from the upper left, restrained warm leaf edges and deeper green shadows on right-facing surfaces. No cast shadows outside the objects, no sunlight shafts, no fog, no bloom, and no baked blur.

Every empty area, including gaps inside foliage, is perfectly flat solid magenta #FF00FF: no sky, transparency, checkerboard, gradient, or magenta reflections. True pixel grid: each art pixel is exactly an 8×8 image-pixel block, no anti-aliasing. No characters, animals, text, UI, borders, or watermark.
```

## 3. Ground texture → `Ground Tile.png`

```text
Create one square seamless top-down pixel-art ground texture for the Mosswood battle floor: packed muted brown earth mixed with restrained irregular moss and short-grass patches, sparse brown and gold fallen leaves, a few small pebbles, tiny twigs, and occasional clover.

Use broad quiet areas between details so combatants remain readable. No single dominant feature, large roots, tall plants, or recognisable repeated landmark. The texture is an edge-to-edge surface material, not a scene: no clearing outline, oval arena, path shape, border, horizon, or perspective.

View directly overhead with even flat illumination, no directional highlights or cast shadows. Material colours must harmonise with the forest's warm upper-left late-afternoon lighting, but the game will light the floor itself. No sunlight patches, fog, glow, blur, or vignette.

Tile seamlessly across left/right and top/bottom edges. Opaque material across the whole image, no magenta and no transparency. True pixel art with each art pixel an exact 8×8 image-pixel block, no anti-aliasing. No characters, animals, text, UI, or watermark.
```

## 4. Foreground props sheet → `Props.png`

```text
Create one pixel-art prop sheet for Mosswood, an HD-2D JRPG forest. Use the attached concept for material colours and object design. Arrange exactly 15 separate complete objects in five columns and three rows, with generous empty gutters and no drawn grid:

Row 1: three leafy bushes with distinct silhouettes and sizes; two different fern clumps.
Row 2: three mossy boulders, small, medium, and large; one fallen mossy log; one old moss-covered stump.
Row 3: one small ordinary woodland mushroom cluster; three distinct tall-grass tufts; one modest cluster of small pale wildflowers.

Use a consistent slight three-quarter side view at approximately human eye height. Preserve natural relative size within each object category; do not enlarge a flower clump to boulder size. Show every complete silhouette and ground-contact base. No cropped tips, merged objects, decorative ground islands, supporting platforms, or extra scenery.

Warm late-afternoon light from the upper left, with restrained shading on lower-right surfaces. Readable bark ridges, rock planes, moss cushions, and grouped leaves. No photographic noise, cast shadows on the background, fog, sunlight beams, bloom, or depth-of-field blur.

All empty space is perfectly flat solid magenta #FF00FF, including holes between fronds: no floor, ground line, gradient, transparency, checkerboard, or magenta reflections. Every art pixel is an exact 8×8 image-pixel block on one grid, no anti-aliasing. No characters, animals, text, labels, UI, borders, or watermark.
```

## 5. Canopy overlay (optional) → `Canopy.png`

```text
Create one wide continuous pixel-art canopy overlay for a Mosswood HD-2D JRPG battle scene. Close leafy branches and a few hanging vines extend down from the top edge, seen from below. Dark green grouped leaves have restrained warm late-afternoon highlights from the upper left.

About 3:1 composition. Occupy only the upper quarter overall, thicker at the left and right corners and thinner through the centre. Keep the remaining lower area empty. Use an uneven organic silhouette with gaps between branches and foliage. Branches may intentionally continue beyond the upper and side edges. This is one framing layer, not a sheet of separate trees. The left and right edges must join seamlessly: anything crossing the right edge continues from the left edge at the same height, so the layer can repeat sideways without a visible seam.

All empty space is flat solid magenta #FF00FF, including foliage gaps. No sky, floor, gradient, transparency, checkerboard, magenta reflections, or shadows on the background. No sunlight shafts, fog, vignette, bloom, or blur; the game supplies near-camera depth of field.

Every art pixel is exactly an 8×8 image-pixel block, with hard grid-aligned edges and no anti-aliasing. No characters, animals, text, UI, borders, or watermark.
```

## Supplementary sheets for the wider Mosswood area

The five core images cover the initial assembly. These seven additional sheets provide reusable pieces for trail bends, dense groves, root-heavy clearings, rocky verges, and deadwood pockets. They are optional additions, not replacements for the original filenames.

Keep the fighting floor open. Place banks, roots, trees, and rocks mainly around its perimeter; use changes in their grouping to distinguish locations. Ground-scatter pieces need to be placed against the floor, while standing props remain upright cutouts. These assets suit the existing battle camera; a different exploration angle needs corresponding views.

### 6. Individual trees → `Tree Variants.png`

```text
Create a Mosswood pixel-art cutout sheet with exactly four complete trees in a 2×2 layout: a broad asymmetrical old hardwood, a tall narrow hardwood, a gently leaning tree, and a smaller forked young tree. Include complete crowns and root flares, without cropping. Use irregular branching, visible foliage gaps, moss concentrated at the lower trunks, and different recognisable silhouettes. No surrounding scenery or ground islands. Match the attached forest reference and existing battle camera: slight three-quarter side view at approximately human eye height.

Warm late-afternoon light from the upper left; restrained right-side form shading. Every art pixel an exact 8×8 image-pixel block, no anti-aliasing or blur. Generous margins between all objects. Perfectly flat solid magenta #FF00FF in all empty areas and internal gaps; no transparency, checkerboard, gradient, floor, ground line, cast shadows, or magenta spill. No sunbeams, fog, bloom, characters, animals, text, UI, grid lines, or watermark.
```

### 7. Landmark trunks → `Ancient Trunks.png`

```text
Create a Mosswood pixel-art cutout sheet with exactly four ancient lower-trunk modules in a 2×2 layout: a massive buttressed trunk, a twisted trunk with a small dark hollow, paired trunks sharing one root system, and a leaning trunk with a long lateral root. Each has complete roots, readable bark ridges, and restrained moss growth. These are trunk modules without crowns; leave each upper end visible inside its cell for later concealment behind canopy. No extra scenery, pedestal, or soil island. Match the attached reference and the battle's slight three-quarter side view at approximately human eye height.

Warm late-afternoon upper-left light and restrained right-side form shading. Exact 8×8 image-pixel blocks on one grid, no anti-aliasing or blur. Wide gutters and complete root silhouettes. Flat solid magenta #FF00FF in all empty areas: no transparency, checkerboard, gradient, floor, ground line, cast shadows, or magenta spill. No sunbeams, fog, bloom, characters, animals, text, UI, grid lines, or watermark.
```

### 8. Understory variations → `Understory.png`

```text
Create a Mosswood pixel-art cutout sheet of exactly six plant groups in three columns and two rows: a low wide shrub, a taller open-branched shrub, a broad fern, a compact asymmetric fern, a sparse short grass clump, and a low broad-leaf woodland plant. Give each a distinct silhouette with visible empty gaps between stems and fronds. Use grouped olive and deep-green leaves rather than photographic fine detail. Complete bases, no pots, soil disks, rocks, or extra scenery. Match the attached reference and the battle's slight three-quarter side view at approximately human eye height.

Warm late-afternoon light from the upper left, restrained right-side shading. Exact 8×8 image-pixel blocks, no anti-aliasing or blur. Separate all objects with generous margins. Empty areas are perfectly flat solid magenta #FF00FF: no transparency, checkerboard, gradient, floor, ground line, cast shadows, or magenta reflections. No sunbeams, fog, bloom, characters, animals, text, UI, grid lines, or watermark.
```

### 9. Rocks and boulders → `Rock Variants.png`

```text
Create a Mosswood pixel-art cutout sheet of exactly six stone objects in three columns and two rows: a large angular mossy boulder, a low rounded boulder, a taller split rock, three naturally touching small stones as one group, a long low boundary rock, and a broad embedded-looking rock cluster. Clear stone planes, subdued gray-brown colours, and irregular moss coverage with exposed stone on every object. Complete stable bases without ground platforms. Match the attached reference and the battle's slight three-quarter side view at approximately human eye height.

Warm late-afternoon light from the upper left, restrained right-side shading. Exact 8×8 image-pixel blocks, no anti-aliasing or blur. Generous empty gutters. Perfectly flat solid magenta #FF00FF in every empty area: no transparency, checkerboard, gradient, floor, ground line, cast shadows, or magenta spill. No sunbeams, fog, bloom, characters, animals, text, UI, grid lines, or watermark.
```

### 10. Low terrain edges → `Roots and Banks.png`

```text
Create a Mosswood pixel-art cutout sheet of exactly six shallow terrain-edge modules in three columns and two rows: a low straight mossy earth bank, an inward-curving bank, an outward-curving bank, an exposed-root bank, a shallow mossy rock rise, and a tapering earth-and-root edge. Show a shallow front face and a modest visible upper surface, consistent with the battle's slight three-quarter side view at approximately human eye height. Organic tapering ends should allow overlap during assembly. These are low perimeter pieces, not tall cliffs or floating islands. No trees, bushes, paths, or surrounding floor.

Warm late-afternoon upper-left light and restrained right-side shading. Exact 8×8 image-pixel blocks, no anti-aliasing or blur. Complete separate silhouettes with generous gutters. Flat solid magenta #FF00FF in all empty areas: no transparency, checkerboard, gradient, ground line outside each object, cast shadows, or magenta spill. No sunbeams, fog, bloom, water, characters, animals, text, UI, grid lines, or watermark.
```

### 11. Deadwood variations → `Deadwood.png`

```text
Create a Mosswood pixel-art cutout sheet of exactly six deadwood objects in three columns and two rows: a long fallen mossy trunk, a short hollow log, a broad broken stump, a small weathered stump, one long crooked branch, and a modest two-branch cluster. Distinct silhouettes, readable wood grain, believable thickness and broken ends, restrained decay, and selective moss. Vary object orientation while retaining the same slight three-quarter side-view battle camera at approximately human eye height. Complete objects, no cropping, soil islands, or attached scenery.

Warm late-afternoon upper-left illumination with restrained right-side shading. Exact 8×8 image-pixel blocks, no anti-aliasing or blur. Wide empty gutters. Flat solid magenta #FF00FF everywhere outside the objects: no transparency, checkerboard, gradient, floor, ground line, cast shadows, or magenta spill. No sunbeams, fog, bloom, characters, animals, text, UI, grid lines, or watermark.
```

### 12. Ground transitions → `Ground Scatter.png`

```text
Create a Mosswood pixel-art cutout sheet of exactly six thin ground-cover patches in three columns and two rows: an irregular moss fringe, a sparse short-grass fringe, a broad broken leaf-litter patch, a compact moss patch with holes, a sparse small-pebble scatter, and a sparse leaf-and-twig patch.

These pieces will lie flat against the 3D ground: view directly overhead with no perspective. Give each a broken organic outline and empty gaps so it can blend across dirt and moss surfaces. No rectangular backing, raised terrain, large roots, or standing scenery. Even flat lighting without directional shadows, using the forest's warm-compatible palette.

Exact 8×8 image-pixel blocks, no anti-aliasing, feathering, or blur. Complete isolated patches with generous gutters. All surrounding space and holes are flat solid magenta #FF00FF: no transparency, checkerboard, gradient, floor, ground line, cast shadows, or magenta spill. No effects, characters, animals, text, UI, grid lines, or watermark.
```

## Optional ground materials for area variation

Keep `Ground Tile.png` as the default mixed floor. Generate these as separate opaque materials when more distinct clearings and trails are needed. They require deliberate material assignment or blending during assembly; generating the images does not create a terrain-blending system.

### 13. Quiet trail material → `Ground Dirt.png`

```text
Create one square seamless top-down pixel-art material for Mosswood: muted warm brown compacted forest earth with broad quiet variation, very sparse tiny pebbles, and occasional small leaf fragments. Mostly clear dirt, no grass border or path outline. Direct overhead orthographic view, even flat illumination, no directional highlights or shadows. No dominant landmark, roots, scenery, horizon, perspective, vignette, or blur. Match the attached concept's material palette without its lighting effects. Opaque surface across the entire image; no magenta or transparency. Tile seamlessly on all four edges. Every art pixel exactly an 8×8 image-pixel block, no anti-aliasing. No characters, animals, text, UI, or watermark.
```

### 14. Mossy grove material → `Ground Moss.png`

```text
Create one square seamless top-down pixel-art material for Mosswood: dense muted olive and deep-green moss in broad irregular cushions, with occasional small gaps of subdued brown soil. Restrained clustered detail without bright speckling. Direct overhead orthographic view, even flat illumination, no directional highlights or shadows. No standing plants, rocks, roots, path outlines, scenery, horizon, perspective, vignette, or blur. Match the attached concept's material palette without its lighting effects. Opaque surface across the entire image; no magenta or transparency. Tile seamlessly on all four edges. Every art pixel exactly an 8×8 image-pixel block, no anti-aliasing. No characters, animals, text, UI, or watermark.
```

### 15. Shaded woodland material → `Ground Leaf Litter.png`

```text
Create one square seamless top-down pixel-art material for Mosswood: thin irregular coverage of subdued brown and dull-gold fallen leaves with a few tiny twigs over dark forest soil. Leave broad quiet soil patches between leaf clusters. No thick piles or repeated dominant leaf motif. Direct overhead orthographic view, even flat illumination, no directional highlights or shadows. No standing plants, large branches, roots, rocks, path outlines, scenery, horizon, perspective, vignette, or blur. Match the attached concept's material palette without its lighting effects. Opaque surface across the entire image; no magenta or transparency. Tile seamlessly on all four edges. Every art pixel exactly an 8×8 image-pixel block, no anti-aliasing. No characters, animals, text, UI, or watermark.
```

## Placement and acceptance

- **Far background:** opaque large backdrop plane behind the clearing; small camera movement may create parallax relative to nearer planes. No baked floor to conflict with the actual battle floor.
- **Mid trees:** remove magenta and place in front of the far backdrop. Tree-group openings reveal the far scenery. Use scene depth of field rather than blurred source art.
- **Ground:** tile the opaque material over the 3D battle floor. Create the irregular clearing and receding path through floor layout, material distribution, and surrounding props, rather than painting a fixed path into the far panorama.
- **Props and supplementary sheets:** cut into individual pieces, remove magenta, and place with ground-contact bases anchored to the floor. Keep most scenery around the combat perimeter. Use roots and banks outside the level fighting area. Preserve each object's complete source for reuse.
- **Ground scatter:** place flat against the floor with a suitable small offset to prevent overlapping surfaces flickering. Do not use these as upright plants.
- **Canopy:** key out magenta and position close to the camera, framing the upper view without hiding the turn-order UI or combatants. Larger close foreground props can supply lower-corner framing.
- **Lighting:** the source artwork retains restrained warm upper-left form shading. The game supplies ground/contact shadows and additional lighting. Do not duplicate baked sunbeams or strong light pools.

Before accepting an output, verify object count, silhouette completeness, camera consistency, light direction, exact flat magenta, and usable spacing for cuts. Reject merged objects and invented scenery. Inspect ground textures in a repeated layout to verify seams. After cleanup/snapping, verify the exact 8×8 grid and removal of magenta fringes. Soft or off-grid generated edges can be processed by the existing sprite pipeline, but successful generation alone is not proof that this processing has passed.

Review a small assembly with the current character sprites at gameplay size before scaling up production. Flat scenery supports this battle presentation and modest camera changes; it does not provide full 3D volume for large camera orbits. No runtime files or import bindings are changed by this prompt document.
