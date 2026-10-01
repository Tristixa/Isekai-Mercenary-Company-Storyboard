# Eurydica: approved big red tree v1 (owner approved 2026-09-30; the iconic red-tree court landmark, 13 m)
Owner review required; no game integration or approval implied.

## Deliverables
- red-tree.png: 2048 × 2048 RGBA upright painted cutout.
- red-tree-leaves-ground.png: 2048 × 2048 RGBA, top-down horizontal ground decal.
- camera-preview.png: rendered court mock, due north, 40° down, vertical FOV 30°.
- review.html: local review page with light/dark backgrounds, scale information and labeled preview.
- sources/: untouched native generated PNG masters (1254 × 1254).
- court-preview.blend and build-preview.py: reproducible measured mockup.
- export.ps1 and qa.json: export procedure, native alpha statistics and master hashes.

## Design and metres
Plan v5 landmark red_tree at world (x,z)=(-7,93), red-tree court beside tavern.
Tree target 13 m height within requested 12–14 m; crown approximately 12 m wide.
Mock uses a 12.5 m wide × 13 m tall upright quad, rooted at its bottom centre. Painted perspective depicts upper foliage and root surfaces.
Ground leaf decal spans 10 × 10 m, horizontal and centred beneath tree. It is top-down deliberately, so the camera projects it once.
Use Y-axis billboard orientation in Godot; the fixed south-facing mock plane represents that orientation for a due-north camera.
Gold post in preview is 1.68 m high. Tavern footprint follows v5 at x=-18.5..-9.5, z=78.5..89.5; its roof and facade are illustrative context, not a revised building specification.
The preview is a Blender court mock, not a game capture or a replacement for 02-market.png. Perspective framing is pulled back to show the full crown. No live runtime, collisions, occlusion or movement checks were performed.

## Generation and reference roles
Built-in image_gen used for both assets. Exact prompts: tree-prompt.txt and leaves-prompt.txt.
Copies of the four attached references are retained in sources/references. Four attachments to each generation, rooted at D:/Storyboards/Isekai Mercenary Company:
1. Environment Assets/Hylaea/Approved Calibration v1/objects/tree-broad.png — painting manner, edges and value grouping.
2. Environment Assets/Hylaea/Approved Calibration v1/objects/tree-leaning.png — bark, natural branching and paint handling.
3. Locations/Eurydica/concepts/eurydica-market-spine-approved.png — landmark context and relative scale, not camera azimuth.
4. Environment Assets/Eurydica/Approved Facades v2/tavern/s.png — palette harmony and painted finish.
Research/Atmosphere - Kingdoms of Amalur/kingdoms-of-amalur-scenery.jpg and README were inspected for sunlit storybook autumn mood ONLY. The image was never attached to generation and its silhouette was not used as a design template.
Plan source: Locations/Eurydica/Build Plan v5/eurydica-plan.json. Camera contract verified: north heading, pitch 40°, FOV 30°.
HD-2D Proof/out/town/02-market.png was inspected for gameplay context; the allowed court-mock option was selected.

## Processing and review
Generated masters preserved byte-for-byte from tool-returned PNG data. Native masters are 1254 px square, not native 2K. Final exports use bicubic enlargement to 2048 px; no detail-generation claim.
Native alpha preserved; bottom padding cropped to the tree bounds measured at alpha > 16 before resizing, without chroma keying, palette quantization or pixel-unfake. Most subject pixels have partial alpha from the generator. See qa.json for measurements.
Tree root reaches bottom edge. Deep red/crimson foliage, warm highlights, wine depths, twisting trunk and branch gaps were inspected against the requested anchors.
No painted ground or cast shadow is included in either production PNG; the mock's environment illumination belongs to the render.
Review candidate at intended camera size and on both backgrounds before owner selection. All project and storyboard assets remain read-only.

