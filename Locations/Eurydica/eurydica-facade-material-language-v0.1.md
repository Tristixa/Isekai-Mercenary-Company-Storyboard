# Eurydica Facade and Material Language v0.1

Status: proposed concept layer for approval. This develops the approved district, silhouette and density studies. It is not production artwork, geometry or authorization to change the game.

Companion studies:

- `eurydica-city-concept-v0.1.md`
- `eurydica-district-diagram-v0.1.md`
- `eurydica-silhouette-density-study-v0.1.md`

Visual study: `diagrams/eurydica-facade-material-language-v0.1.svg`

Rendered preview: `diagrams/eurydica-facade-material-language-v0.1.png`

## 1. Design thesis

Eurydica should look like one regional city built over several generations, not a plaza assembled from matching pristine prefabs. Buildings share a recognizable material grammar, but age, trade, wealth and present ownership alter how that grammar appears.

The common construction stack is:

1. **Durable river-stone base:** foundations, retaining walls, bridgework and lower service walls.
2. **Lighter occupied body:** colored lime plaster, masonry infill and painted structural joinery.
3. **Strong protective roof:** clay tile, dark slate-like tile or repaired copper sheet with visible drainage pieces.
4. **Owner layer:** awnings, shutters, signs, balconies, loading frames, garden walls or work attachments.
5. **Age layer:** a restrained patch, replaced bay, faded finish, reused stone course or roof repair.

Every building does not need every element. The city-wide identity comes from repetition with controlled variation.

## 2. What the Steambot references contribute

The three Nefroburg images remain location and urban-life references, not rendering-style or camera locks.

### Canal and bridge

Use:

- Major infrastructure embedded in ordinary daily frontage.
- A strong bridge crossing that organizes the surrounding city.
- Balconies, awnings and occupied edges touching the water corridor.
- Repeated civic fixtures establishing route rhythm.

Do not copy:

- Sepia sunset treatment.
- Exact European block proportions.
- Eye-level camera or painted runtime illumination.

### Station facade

Use:

- Clear structural bays and a readable base/body/roof hierarchy.
- Ornament concentrated into bands rather than scattered everywhere.
- Practical planting and signage connected to the building's use.
- A large public building that still reads through ordinary materials.

Do not copy:

- The exact half-timber railway-station design.
- Its pointed roof finials as a universal Eurydica motif.
- Purple color cast or industrial-period specificity.

### City overview

Use:

- District-scale roof variation and recognizable larger civic/trade masses.
- Trees and open courts interrupting the built fabric.
- Mountains and water giving the city a strong geographic setting.

Do not copy:

- Empty, uniformly clean streets.
- Broad lavender grading.
- The precise waterfront grid.

## 3. Proposed city palette

The palette should be warm and varied without becoming uniformly brown.

| Role | Color | Hex guide | Use |
| --- | --- | --- | --- |
| River stone | Warm grey | `#8A8B82` | Foundations, bridge masonry, retaining walls. |
| Pale plaster | Warm cream | `#D8CBAE` | Most occupied wall fields. |
| Ochre plaster | Muted ochre | `#C69B62` | Market and older sun-facing walls. |
| Sage plaster | Dusty sage | `#91A18D` | Residential and waterworks accents. |
| Structural timber | Charred umber | `#4E4038` | Joinery, braces, frames and repaired beams. |
| Clay roof | Weathered terracotta | `#A75F4C` | Common pitched roofs and patch tiles. |
| Dark roof | Blue charcoal | `#465765` | Older roofs, civic reuse and visual cooling. |
| Aged copper | Muted verdigris | `#638D84` | Select gutters, roofs, caps and water-facing details. |
| Painted accent | River indigo | `#3F6274` | Doors, shutters, signs and Company-related accents. |
| Metal accent | Old brass | `#B08C50` | Restrained hardware, sign brackets and civic markers. |

These are concept guides rather than final shader or texture values. Each material needs lighter and darker value families when the rendering option is chosen.

## 4. Core facade grammar

### Foundations and lower walls

- Use coursed river stone with broad, readable blocks rather than tiny noisy joints.
- Allow foundations to step with the terraces and reveal older height changes.
- Add repair through one changed stone family or rebuilt corner, not random cracks across every wall.
- Market, quay and workshop lower walls should tolerate visible loading contact and splash wear.

### Wall bodies and structural rhythm

- Divide facades into unequal but intentional bays.
- Use dark painted joinery selectively: corners, major floor lines, window groupings and structural braces.
- Avoid placing the same timber grid on every building.
- Let plaster colors shift by owner and age while staying inside the city palette.
- Concentrate carved or ceramic motifs in one band, lintel, railing or drainage line.

### Roofs and drainage

- Use three roof families: clay tile, blue-charcoal tile and repaired copper sheet.
- Vary ridge height and roof direction between attached groups.
- Use shallow curved eaves or clipped corners on selected buildings to establish fantasy character.
- Show gutters, chains, ceramic spouts or collection barrels where water management is practical.
- Keep finials rare: the watch-bell tower, bridgeheads and a few old mercantile roofs only.

### Windows and doors

- Group windows by the building's internal use rather than placing identical openings on a perfect grid.
- Market buildings favor wider lower openings and smaller upper rooms.
- Workshops use broad doors, high vents and reinforced lower frames.
- Homes use shutters, deep sills, small balconies and garden-facing windows.
- Civic buildings use legible entrances but remain modest in scale and decoration.
- Glazing should not make every window glow; runtime lighting remains separate.

## 5. District facade families

### Market Spine — adapted mercantile frontage

- Two to three storeys with attached street edges.
- Stone or masonry base, colored plaster upper floors and projecting shade structures.
- Awnings, hanging signs and stall fixing points belong to individual owners.
- Frequent door and window alterations show businesses changing over time.
- Keep the central road clear; display life at thresholds and under awnings.

### Old City — inherited, compressed fabric

- Two to four storeys, irregular party walls and overlapping roof ages.
- More exposed older stone, darker joinery and reused carved bands.
- Upper-floor bridges or passage arches may occur rarely where blocks accumulated together.
- The watch-bell tower uses the same materials at greater vertical proportion, preventing it from reading as a separate palace style.

### Arrival Ward and Company Edge — practical and expandable

- One to two storeys with larger yards, sheds and visible delivery access.
- Simpler plaster fields, robust doors and broad roof overhangs.
- Inns and stables gain owner-specific porches, mounting rails, water points and storage edges.
- The first Company building should look newly occupied rather than newly constructed: reused frontage, repaired sign bracket and available expansion yard.

### Civic Terrace — modest reused administration

- One to two storeys around an imperfect public court.
- Plain stone base, faded plaster and restrained indigo or brass identification markers.
- Small notice shelter, toll office and records room should appear adapted from ordinary buildings.
- No monumental stairs, dome, palace facade, huge columns or dominant symmetry.

### Quays and Workshops — working construction

- Larger ground-floor openings, masonry bases and replaceable upper panels.
- Timber loading frames, hoists, vents and short chimneys attached where their work requires them.
- Roof repairs and wall protection are more visible, but structures remain maintained and safe.
- Keep grime localized to loading, heat, runoff and contact zones.

### Residential and Waterworks — quieter variation

- Pale and sage plaster, small courts, garden walls and restrained balcony planting.
- Roof breaks and extensions show households changing over time.
- Waterworks use more stone, copper drainage and practical open service access.
- Plants are cared for and clustered, not procedural overgrowth covering every surface.

## 6. Controlled variation rule

Use a **70 / 20 / 10 design balance** when developing building families:

- **70% shared regional grammar:** common material stack, roof logic, joinery proportions and motifs.
- **20% owner adaptation:** trade frontage, awning, balcony, sign, storage, garden or work attachment.
- **10% age and repair:** one or two legible interventions such as a patched roof run, rebuilt bay or replaced finish.

This is a design discipline, not a literal pixel or asset percentage.

## 7. Pristine-asset failure checks

Reject a facade family when:

- Every building has the same cream walls, timber grid and roof pitch.
- Windows, doors and signs repeat at identical intervals regardless of use.
- Materials are uniformly clean, uniformly dirty or covered in procedural scratches.
- Repairs appear as random decals rather than construction changes.
- Props are scattered to simulate life without showing circulation or ownership.
- Fantasy identity depends mainly on crystals, glow or oversized ornament.
- The Civic Terrace looks wealthier or more organized than the Market Spine.
- The Company looks like a completed guild headquarters at the beginning of the story.

## 8. Proposed approval locks

- Eurydica uses the river-stone / colored-plaster / painted-joinery / clay-dark-copper roof stack.
- The palette combines warm mineral walls with cool indigo, charcoal and verdigris accents.
- Regional fantasy identity comes from selective curved eaves, clipped corners, braces, ceramic drainage and restrained river-geometric motifs.
- Building variation follows shared construction plus owner adaptation and restrained age/repair.
- Market and Old City facades are attached and layered; Arrival and Company buildings remain simpler and more open.
- Civic buildings reuse ordinary architecture and never become monumental.
- Lived-in evidence remains functional and concentrated at edges, thresholds and work zones.

## 9. Still unresolved after this study

- Exact facade drawings and modular building-kit dimensions.
- Final material rendering under the selected visual style.
- Exact motif design and Company sign language.
- Daytime lighting, season and weather for the concept image.
- Concept-image and playable-production camera selection.
- Final rendering family.

