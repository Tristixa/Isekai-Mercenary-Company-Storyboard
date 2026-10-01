# Generation prompts

## Tavern v1 — rejected: incorrect silhouettes

Create a production texture sheet containing exactly FOUR straight-on orthographic exterior wall elevations of the EURYDICA TAVERN, arranged in a clean 2 by 2 grid. No text or labels anywhere. Reference 1 is architectural identity: use ONLY the left tavern, warm cream plaster, dark timber framing, quiet grey stone base/corners, projecting upper room expressed through framing. Reference 2 Hylaea clean props is painted finish compatibility only, no foliage or rocks in output. Reference 3 approved Eurydica is simplified broad-material/detail standard. Reference 4 game screenshot is world complexity only; ignore portraits, UI, lighting and characters. Neutral near-albedo colors with ONLY soft ambient occlusion at recesses and structural joins. No directional lighting, cast shadows, glowing windows, highlights or props. Broad matte painted surfaces; no grain, tiny details, pixel grid or quantization. Each elevation faces viewer squarely, no perspective, no visible side, roof plane, ground plane, awning, sign, chimney, steps or barrel. Four isolated wall silhouettes on flat vivid magenta background with clear gutters. Top-left EAST entrance wall, rectangle width 11 m height 9.3 m: centered door 1.4 m wide 2.3 m tall reaching ground, one replacement plank. Three storeys with bands 3.1 and 6.2 m above ground, dark unlit windows. Top-right WEST back wall same rectangle dimensions and aligned storey bands, simpler windows, no door. Bottom-left NORTH gable wall width 9 m, rectangular wall 9.3 m high topped by 4.95 m tall concave sweeping gable. Bottom-right SOUTH gable same shape and scale, matching storey heights. For both gables top height above base is 9.3+4.95*(1-abs(x-4.5)/4.5)^1.4, sharp central apex, concave sides. These are plaster/timber gable walls, no roof covering. Paint extends to all wall boundaries, full coherent wall construction. Keep the 4 elevations large, distinct, complete and uncropped; landscape high resolution sheet. Candidate game texture assets, no lettering, logos, people or baked props.


## Tavern v2 — intermediate; gables missing storey

Paint the FOUR flat wall silhouettes in reference 1 (layout guide), preserving their exact positions and shapes. Top left NORTH gable, top right SOUTH gable, bottom left EAST rectangular entrance wall, bottom right WEST rectangular back wall. This is a UV texture atlas of the SAME Eurydica tavern. No labels. Keep the magenta outside each shape. DO NOT put gables on the bottom two RECTANGULAR shapes. DO NOT paint roof surfaces. The cream silhouettes are actual walls to texture all the way to edges. Gables measure 9m wide, lower wall 9.3m high and gable rise4.95m. Rectangular walls11m wide9.3m high. On ALL four faces use three storeys and identical horizontal timber floor bands at3.1m and6.2m above the ground and top beam at9.3m. Windows on three storeys, dark unlit, restrained simple frames. Door is ONLY the existing brown rectangle bottom left; preserve its exact size and centre (1.4m wide2.3m tall). Reference2 approved market exterior: reconstruct the TAVERN at left only, cream/peach plaster, dark structural timber, grey stone base/corners, restrained replacement door plank, no props. Reference3 clean Hylaea props: compatible clean painted broad matte finish only, no natural objects transferred. Reference4 accepted game look: broad forms, sparse joints; ignore its perspective and lighting. Reference5 runtime: environment simplicity only; ignore UI portrait characters night and effects. Straight-on ORTHOGRAPHIC elevations without depth, no side faces or top surfaces visible. Near-albedo neutral lighting, only soft recess AO. No cast shadows, highlights, sun gradient, emissive window, awning, roof tiles, chimney, steps, labels, lettering, tiny grain, fine texture, people, props or pixel grid. Maintain coherent thick framing and plain large material areas across all four elevations.


## Tavern v3 — selected candidate sheet

Correct ONLY the two TOP gable elevations in reference1. They incorrectly have only TWO rectangular storeys under the gable beam. Add a third full rectangular storey with dark windows and a horizontal timber floor band to BOTH TOP elevations, so each has THREE equal-height rectangular storeys BELOW its gable triangle, plus one attic window in the gable. Each storey is3.1m tall; width9m, three-storey wall9.3m, gable4.95m. Enlarge canvas vertically as needed so top elevations are taller, never reduce them to two storeys again. Preserve bottom two rectangular elevations exactly: three storeys, centered door only on bottom-left, identical neutral painted cream plaster grey stone dark timber finish. Preserve all four separate elevations, 2x2, no text, roof surfaces, props, directional light or shadows. Keep hard clean silhouette boundaries. Reference2 is the source tavern architecture at left only; reference3 is clean painted Hylaea finish compatibility only. Finish reference1 governs entire set. Make fully opaque painted faces on flat magenta background, with enough gaps for cutting. No transparency processing; this is a raw chroma sheet.


# Resume production / 2026-09-27

All new exports are candidate, not approved. Accepted source: sources/tavern-v2.png (RESUME NOTE authority); not regenerated.

## company_house

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\company_house.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-company-edge-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Create four straight-on orthographic exterior wall elevations of the modest EURYDICA COMPANY HOUSE. Reference1 is the exact layout guide: paint its four silhouettes fully to edges, preserve locations, shapes and door rectangle. Top left NORTH gable, top right SOUTH gable, bottom left EAST rectangular entrance wall, bottom right WEST rectangular back wall. Reference2 is identity: ONLY the small Company House marked03, warm cream plaster, dark timber, grey stone base and corners. No porch roof, chimney, dormer, steps, barrel or surrounding scenery painted into these wall faces. Reference3 is clean Hylaea painted finish compatibility only; transfer no plants or rocks. Reference4 is the accepted tavern source: FINISH AND DETAIL LEVEL OF THIS SET, same broad matte painted material treatment and neutral colours. Reference2 also supplies approved simplified game appearance: broad surfaces only. Reference5 actual game screenshot: environment complexity only, ignore portrait UI people and night lighting. All elevations are squarely front-on without perspective or visible side planes. Same neutral near-albedo treatment on all four faces, soft recess AO only, no directional light, cast shadows or specular highlights. All windows dark and unlit. Walls 7.5m wide4.4m tall, gables add4.13m with concave sweeping sides matching guide. One main storey and loft; no multi-storey tall house. East centered door1.4m wide2.3m tall, ground at bottom. Plain back and side windows, one restrained plaster repair patch. Exactly four isolated silhouettes, magenta background and gutters. No labels, lettering, symbols, people, props, roofs, awnings, grain, tiny tiles, pixel grid or palette quantization.
```

## repair_supply

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\repair_supply.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-market-building-exteriors-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. REPAIR & SUPPLY, the broad low RIGHT building in identity reference. NORTH and SOUTH are gable walls10m wide: lower wall4.8m and gable5m high. EAST and WEST are rectangular walls12m wide4.8m high. Single tall workshop storey and gable loft. Only WEST (bottom right) has centered DOUBLE work doors3m wide2.8m high. One replaced door brace. Older stone base and corner quoins, quiet peach plaster, sparse high dark windows. NORTH and SOUTH gables have concave swept top edges exactly as guide. No chimney or workcloth painted in.
```

## provisions

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\provisions.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-market-building-exteriors-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. PROVISIONS SHOP, the compact MIDDLE building in identity reference. NORTH and SOUTH gables8m wide with lower wall6.2m plus4.4m gable rise. EAST and WEST rectangular walls8m wide6.2m high. TWO equal3.1m storeys on ALL faces below gable. One horizontal floor band3.1m above ground matching around every corner. EAST bottom-left has centered entrance door1.4m wide2.3m tall, dark wide selling counter opening beside it. NORTH has one small side storage door, broad restrained plaster repair patch. Few upper windows, plain rear face, all dark and unlit. No shelves, goods or props.
```

## gatehouse

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\gatehouse.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-arrival-ward-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. SOUTH GATE, stone building marked05 in identity reference. NORTH and SOUTH (top row) are IDENTICAL pale grey dressed-stone RECTANGLES12.4m wide7.2m high with ONE central round arch opening. Opening center6.2m from left, width4.6m, vertical sides rise3m then semicircle radius2.3m apex5.3m. Opening same magenta as background. No gate or door leaves within opening. EAST and WEST (bottom row) are NARROW gable end walls2.4m wide, wall7.2m high plus1.32m gable rise. Preserve slender proportions guide. Stone only, a few broad quiet joints and small dark slit recesses, no plaster timber patterns from tavern except shared finish. No roof or crenellations.
```

## lodging

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\lodging.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-arrival-ward-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. LODGING HOUSE marked02 in identity image. NORTH and SOUTH top row RECTANGLES10m wide6.2m high, no gables. EAST and WEST bottom row gables8m wide with6.2m wall and4.4m gable rise. TWO wall storeys of3.1m and loft. Horizontal floor band at3.1m on all faces. Only WEST bottom-right has centered door1.4m wide2.3m tall. Simple dark windows, warm cream walls dark structural timber and grey stone bases, restrained maintained repair. No third storey, no canopy or banner baked in.
```

## stables

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\stables.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-arrival-ward-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. HOLLIS'S STABLES, adapted from timber shelters near cart yard in identity image. Timber-boarded walls, low grey stone base. NORTH and SOUTH top row long RECTANGLES11m wide3.4m high with three broad half-height closed stall doors along each long wall. EAST and WEST bottom row gables5.5m wide with3.4m wall and3.03m gable rise. Loft hay hatch in each gable, no hay painted in. Only WEST bottom-right has centered stable opening3m wide2.3m high, dark interior and lower half-doors. Dark brown structural timber, broad painted plank grouping, no fine wood grain. Work-worn maintained, no animals, hay, cart, trough or props.
```

## guard_shelter

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\guard_shelter.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-arrival-ward-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. GUARD SHELTER marked04, small timber booth. NORTH and SOUTH top row gables3.5m wide3.1m lower wall plus1.93m gable rise. EAST and WEST bottom row rectangles3.5m wide3.1m tall. Single storey only, timber boarded walls with small cream infill and grey stone footing, darker structural framing. EAST bottom-left centered door1.4m wide2.3m tall with small dark counter window beside. One blank notice board on WEST side wall, no paper marks or writing. Keep front door exactly centered in guide, do not move it to fit window. No attached props, fixtures or roof.
```

## store_shed

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\store_shed.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-company-edge-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. COMPANY STORE SHED, small patched shed beside expansion yard in identity reference. NORTH and SOUTH top row rectangles3.5m wide2.8m tall. EAST and WEST bottom row gables3.5m wide with2.8m wall and1.93m gable rise. Single small utilitarian shed. Broad reused dark brown timber boards, muted red-brown replacement board, simple heavy support corners, no cream plaster and no windows except tiny dark vent in back gable. EAST bottom-left gable has precisely CENTERED plank door1.2m wide2.3m high. Do not paint patchwork roof, roof supplied separately.
```

## house_violet

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\house_violet.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-company-edge-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. GENERIC RESIDENTIAL HOUSE, plain neighboring violet-roof houses at edges of identity scene. NORTH and SOUTH top row rectangular walls8m wide6.2m tall. EAST and WEST bottom row gables6m wide6.2m lower wall plus3.3m gable rise. TWO equal3.1m wall storeys on every face, sparse dark small windows and attic window, matched floor bands. SOUTH top-right has centered door1.4m wide2.3m high, no doors on other faces. Cream plaster dark timber quiet stone base. Simpler than tavern and shops. Roof itself absent, not violet plaster.
```

## house_green

Built-in image generation. Ordered attachments:

1. `D:\Codex\IMC\runs\facades-v1\guides\house_green.png` — exact silhouette/layout and door guide.
2. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-market-spine-approved.png` — architectural identity and approved simplified game appearance.
3. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility; no foliage copied.
4. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production UV texture sheet, exactly FOUR wall elevations of ONE building, 2x2. Reference1 is the exact layout/silhouette guide: paint its four shapes all the way to their boundaries, preserve proportions and the brown door marker's exact size. Top-left NORTH, top-right SOUTH, bottom-left EAST, bottom-right WEST. Reference2 is architectural identity and approved simple game appearance ONLY, ignore its camera, scenery and labels. Reference3 clean Hylaea props: clean painted broad matte finish compatibility only, no natural objects copied. Reference4 accepted tavern: FINISH AND DETAIL LEVEL OF THIS SET. Reference5 actual game screenshot: environment simplicity only, ignore UI portrait people lighting. STRICT straight-on orthographic outside elevations, no perspective, side planes or roof surfaces visible. Near-albedo, identical neutral treatment for all four faces, only soft recess AO. No directional sunlight, shadows, highlights, glowing fixtures or lit windows. Broad cream/peach plaster, thick dark structural timber, quiet grey stone base/corners. No tiny grain or detail, pixel grid or quantization. No baked props, awnings, roof planes, ground, steps, signage, text, labels, lettering or people. Background MUST be flat vivid MAGENTA #ff00ff with ample gutters, no gradient or glow; painted faces opaque. GENERIC MARKET STREET HOUSE, simple plain neighboring green-roof houses in identity scene. NORTH and SOUTH top row gables9m wide with6.2m lower wall plus4.95m gable rise. EAST and WEST bottom row rectangles8m wide6.2m tall. TWO equal3.1m storeys on all faces below gable, aligned horizontal bands, simple dark windows. EAST bottom-left has centered door1.4m wide2.3m high, small CLOSED shutter shopfront beside it. No other doors. Cream plaster, dark timber, quiet grey stone base, plainer than named shops. No roof surface.
```

## roof_tiles

Built-in image generation. Ordered attachments:

1. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-market-spine-approved.png` — regional object/material design and palette only.
2. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility only.
3. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
4. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Create one full-bleed square material atlas containing FOUR EQUAL SQUARE roof texture tiles in a 2x2 arrangement, no gutters or dividers or labels. TOP LEFT deep muted green roof, TOP RIGHT muted violet/plum roof, BOTTOM LEFT warm dark brown roof, BOTTOM RIGHT patched reused red-and-brown roof boards. Each quadrant is an independent seamless repeating flat texture covering8m by8m at512x512 export. Broad courses run perfectly HORIZONTALLY across each square, ONLY 6 to8 broad horizontal course bands, very few quiet broad vertical joints. No tiny shingles or tiles, no grain, scratches or noisy marks. View directly normal to roof surface, flat orthographic material swatch, no roof silhouette, no trim, no edges or perspective. Near albedo with only very soft occlusion at broad course joints, no directional sun, cast shadows, highlight, gradients or glow. Each tile MUST tile continuously at opposite left/right AND top/bottom edges. Fill every pixel opaquely; no border, transparency or background. Ref1 approved Eurydica supplies roof materials/colours and low-detail surfaces only. Ref2 Hylaea clean painted props finish only. Ref3 accepted tavern supplies finish and detail level of this set, not wall content. Ref4 actual game screenshot world simplicity only, no UI portrait characters or lighting.
```

## city_wall

Built-in image generation. Ordered attachments:

1. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-arrival-ward-approved.png` — regional object/material design and palette only.
2. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility only.
3. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
4. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate ONE full-bleed rectangular seamless city-wall material tile, straight-on orthographic elevation, final aspect256x218 corresponding4m wide3.4m high. Reference1 South Gate scene supplies pale grey dressed stone city curtain wall identity. Reference2 clean Hylaea finish compatibility only. Reference3 accepted tavern supplies finish and detail level of this set. Reference4 game screenshot environment simplicity only. Wall fills entire canvas to all four edges, opaque; NO background, border, side face or ground. A slightly projecting broad coping course across the top, 4 or5 broad large quiet stone courses below, staggered large slabs, restrained joints, no tiny blocks or grain. MUST repeat seamlessly horizontally, correct matching course heights and values on left/right edges. Same colour family as pale grey gatehouse, matte near-albedo flat neutral light, recess AO only. No cast shadow, directional sunlight, highlights, vines, moss, people, objects, labels or text.
```

## attachments

Built-in image generation. Ordered attachments:

1. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-market-building-exteriors-approved.png` — regional object/material design and palette only.
2. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility only.
3. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
4. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Generate a production cutout sheet of SIX separate cloth/sign attachments for Eurydica, arranged 2 columns3 rows with generous magenta gutters. Background flat #ff00ff, no shadows. Row1 LEFT wine-red scalloped cloth tavern awning, RIGHT cream-and-wine striped scalloped provisions awning. Row2 LEFT saffron work-cloth repair cover, RIGHT cream cloth lodging awning. These four are straight-on exterior front elevations of wide cloth covers, shallow vertical drop, width to height about3:1, no visible perspective or side planes; simple supported top edge and a few broad folds. Row3 LEFT a single slim hanging wine-red banner with no emblem or text, aspect0.6:1.4, RIGHT a small square dark wooden hanging tavern sign with simple cream TANKARD pictogram only and a small support hook, no lettering. Each object isolated and complete, no shared supports or baked walls. Ref1 architecture sheet dictates wine cream saffron textile palette, ref2 Hylaea clean painted material finish compatibility, ref3 accepted tavern FINISH AND DETAIL LEVEL OF THIS SET, ref4 runtime environment simplicity only. Broad matte surfaces, neutral near-albedo, soft form AO, no directional light or cast shadows, highlights, emissions, grain, pixel grid, people or text.
```

## props

Built-in image generation. Ordered attachments:

1. `D:\Storyboards\Isekai Mercenary Company\Locations\Eurydica\concepts\eurydica-arrival-ward-approved.png` — regional object/material design and palette only.
2. `D:\Storyboards\Isekai Mercenary Company\Environment Assets\Hylaea\Approved Calibration v1\clean\Props.png` — clean painted finish compatibility only.
3. `D:\Codex\IMC\runs\facades-v1\sources\tavern-v2.png` — finish and detail level of this set.
4. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\camera\pixel-courtyard.jpg` — front-facing elevated camera construction only; no pixel styling.
5. `D:\Godot Projects\IMC-Companion-Skill-Environment\references\media\imc-runtime-appearance-reference.png` — environment complexity only; ignore portrait/UI/people/lighting.

Exact submitted prompt:

```text
Create a production game prop cutout sheet of EXACTLY12 different objects, clean regular4-column by3-row grid on SOLID PURE MAGENTA #ff00ff background, separated with generous empty gutters. No labels or writing. ROW1 left to right: one barrel (1m tall), one wooden crate(0.8m), stacked pair of crates(1.5m), upright spare cart wheel(1.2m). ROW2: small board stack(0.45m), low wooden bench(0.55m), slender street lamp post(3.6m tall, UNLIT grey glass, no light colour or bloom), blank notice board on legs(1.8m). ROW3: simple empty wooden handcart(1.3m), basket pair(0.6m), EMPTY dry stone water trough(0.65m, absolutely no water), one tied hay bale(0.7m). Each object stays in its own cell, whole outline visible, no contact/cast shadow, ground, shared scenery, extra objects or people. Keep all objects at consistent relative metric scale; lamp tallest. Camera for ALL props: perspective about40 degrees DOWN, looking NORTH, front-facing with NO diagonal/isometric turn; front faces square to viewer and tops clearly visible. This is NOT the wall elevation camera. Ref1 Arrival Ward supplies regional object design only. Ref2 Hylaea CLEAN props supplies painted material finish compatibility only. Ref3 accepted tavern supplies FINISH AND DETAIL LEVEL OF THIS SET, not camera or building shapes. Ref4 courtyard is CAMERA ONLY: elevated front-facing construction and visible tops, ignore pixel art and scenery; use40-degree downward mild perspective. Ref5 screenshot environment complexity only, ignore UI portraits people night and lighting. Broad matte clean painted materials, brown timber grey iron pale grey stone muted straw, restrained joints and few large forms. No tiny grain, dense straw lines, uniform outlines, pixel grid, quantization, letters, logos, directional highlights, glowing glass or baked light. Every prop has a clear bottom-center ground contact.
```
