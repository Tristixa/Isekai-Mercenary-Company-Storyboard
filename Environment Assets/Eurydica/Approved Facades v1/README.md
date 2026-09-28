# Eurydica: approved facades v1

The user approved these on 2026-09-27, after reviewing them in the explorable-town proof (https://claude.ai/artifact/N7VYKQzNWXJWwfDhYrUtRb, version 2 and later).

Codex painted them using `$imc-environment-art-direction`. The approved Eurydica concepts in `Locations/Eurydica/concepts/` supplied the design identity, and Codex's accepted tavern sheet (`sources/tavern-v2.png`) set the finish. The source run is `D:/Codex/IMC/runs/facades-v1`. `Codex run notes.md` records its brief, its references and the parts it designed beyond the concepts.

## Contents

- **Building faces:** `<building>/<n|e|s|w>.png`, 44 faces for 11 buildings:
  - tavern, company_house, provisions, repair_supply, lodging, stables, guard_shelter, store_shed, gatehouse;
  - generic house_violet and house_green, reused for other lots.

  Each face is a straight-on orthographic elevation at 64 px per metre, with the ground on the bottom edge. Gable faces use the concave profile in `facades-spec.json`; the gatehouse's north and south faces have a transparent arch.
- **`roofs/`:** green, violet, brown and patchwork tiles, 512×512, covering 8×8 m, seamless in both axes.
- **`walls/city_wall.png`:** 256×218, covering 4×3.4 m, seamless horizontally.
- **`attachments/`:** awnings (tavern, provisions, lodging), the Repair & Supply cover, the wine banner and the tavern sign.
- **`props/`:** 12 cutouts painted for the gameplay camera (about 40° down, looking north), with bottom-centre anchors in `props/anchors.json`.
- **Records:**
  - `facades-spec.json`: the exact contract (sizes, doors, silhouettes);
  - `manifest.json`, `check-summary.txt` (422/422 checks passed) and `door-registration.json`;
  - `prompts.md` and `prompts/`, `references/` with `reference-provenance.json`, and `sources/` (untouched generated sheets);
  - `review/`: the labeled overview and paper assemblies.

## Use

- **Where they're used:** `HD-2D Proof/tools/build-town.mjs` inlines these files into the town proof. `HD-2D Proof/src/town.html` maps each face onto its building box, and puts curved roofs and awnings over them.
- **Reuse on another footprint:** the generic houses turn with the building's door face and stretch to fit its size.
- **Lighting:** the paint is near-albedo on purpose. The engine owns the sun, shadows, lamp light and water.
- **New buildings:** follow the HD-2D buildings reference in `$imc-environment-art-direction`.
