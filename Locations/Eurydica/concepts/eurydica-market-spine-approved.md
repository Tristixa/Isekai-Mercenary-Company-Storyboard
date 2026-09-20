# Eurydica — simplified game presentation v0.3

Date: 2026-09-20  
Status: user-approved environment rendering reference, 2026-09-20. The user accepted this appearance and requested it as the persistent default for future IMC places. This approves the rendering direction; runtime geometry and production assets still require implementation and verification.

[View approved image](eurydica-market-spine-approved.png)

## User correction

The v0.2 image was still too detailed and illustrative. Match the complexity visible in the actual game world of the supplied screenshot, while keeping attractive curves and fantasy architecture. The detailed dialogue portrait is not an environment rendering reference.

## Rendering direction

Use the current game screenshot as the primary standard. The previous city images supply architectural ideas and layout only. The earlier interpretation of the retained 3D-to-2D portrait examples did not achieve the requested game appearance.

- Roofs: broad curved surfaces with a few seams; omit individual shingles.
- Walls: plain plaster and substantial supports; restrained broad wear and repair patches.
- Ground: larger, quieter paving slabs.
- Trees: grouped foliage shapes and broad shadows.
- Merchants: a small number of readable crates, barrels and goods.
- Lighting: simple daylight, clear cast shadows and little surface gloss.
- Fantasy character: retain roof sweeps, substantial eaves and varied building volumes.

## Retained section

The zoomed-out diagonal view includes the three main market businesses, copper-red tree pocket, side passage, river and one Old Bridge, with two small civic premises at the northern landing. Curved roofs and warm walls remain visible at this lower detail level.

## Visual review

The new image substantially reduces tile detail, ornamental metalwork, flowers and merchandise relative to v0.2. Large material areas and cast shadows more closely resemble the supplied game screenshot. The primary route, bridge deck, shop approaches and side stair remain readable.

Remaining decisions:
- The copper tree still has more small foliage marks than some trees in the game reference.
- Dense perimeter planting and repeated banners can be reduced further when planning actual assets.
- Lamp panes are pale yellow without visible halos; this does not specify runtime emission.
- Actual performance depends on geometry, textures, materials and rendering choices. A generated image cannot establish engine capacity or a polygon budget.
- Actor scale, collision, occlusion, scene extent and source density remain untested.

## Production status

This is a concept of the assembled scene. It does not supply meshes or separate environment assets. River water appears to explain geography; water and dynamic lighting would be controlled separately in production. The isometric section view is a concept framing choice, not a tested camera implementation.

All work is stored in the storyboard project.

The reusable standard is recorded in [Environment Rendering Standard](../../../Notes/Environment_Rendering_Standard.md) and installed in the `imc-environment-art-direction` skill with retained image copies.

[Prompt and references](eurydica-market-spine-generation.md)
