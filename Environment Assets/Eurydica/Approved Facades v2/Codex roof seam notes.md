# Finish-B seamless roof candidates

**CANDIDATES — NOT APPROVED.** Green is a technical correction of the approved anchor with the same look: green hue family, detailed weathered surface, broad staggered shingles and near-albedo finish. It is not a newly approved anchor. The other three candidates preserve their original violet, brown and red/brown material families. No project assets or runtime files were changed.

All four production PNGs are 512 × 512 RGB, covering 8 × 8 m at 64 px/m. The ridge cap belongs to separate builder geometry.

## Deliverables

- `green.png`, `violet.png`, `brown.png`, `patchwork.png` — corrected candidate tiles.
- `review/tiled-3x3.png` — four labeled before/after pairs. Each individual panel is a 3 × 3 repeat at exactly 50% scale (768 × 768); the complete sheet is 1584 × 3348.
- `check.py` — executable checks; nonzero exit status on failure.
- `review/checks.json` — full measurements and SHA-256 hashes for sources and deliverables.
- `heal.ps1` — reproducible C# / System.Drawing source-patch healing and finishing.
- `sources/` — untouched copies of the four facades-v2 inputs.
- `review/*-offset-before.png`, `review/*-offset-after.png` — half-offset inspection views.

## Source and method

The sole delivered-artwork sources are `D:/Codex/IMC/runs/facades-v2/roofs/{green,violet,brown,patchwork}.png`. No files from `facades-v2-seamfix` were used. The handoff identifies source green as the approved Finish-v2 roof-B anchor copy. Its source hash is recorded in `review/checks.json`; the approved project folder was not modified.

The sources were wrapped by (256,256) for seam inspection. Healing uses periodic coordinates: the original outer wrap becomes the central cross in these offset views. The repair is broader than edge matching:

1. Remove the cap and incomplete final course, rebuilding six ordinary full courses from intact original course donors. Course pitch is 512/6 = 85.333 px (1.333 m), retaining the original approximately 84–86 px scale. Different horizontal placements keep joints staggered. Two additional courses in the single-color tiles reuse translated original course donors.
2. Heal the single-color tiles' horizontal wrap with a 160 px intact interior source patch, with 16 px transition margins. This removes the border and edge vignette through a full material area. The saved half-offset views expose the repaired wrap for inspection.
3. Reassemble patchwork from full original red and brown shingle material patches, inserting original material-joint details. Shingles run around the periodic domain, so neither color changes nor clipped strips occur merely because an image ends. Patchwork joints and widths are revised as required to continue across both seams; it retains broad shingles and its red/brown mix.
4. Apply gentle periodic, low-frequency exposure correction across the full texture, plus complete-course and same-course-phase exposure balancing. RGB channels receive the same gain, preserving hue. Course recesses and fine texture remain; no directional light is added.
5. Place the vertical wrap within an ordinary course, and close the final one-pixel endpoints by averaging. Endpoint equality is only this final step, after material and course continuity have been repaired.

The texture is cyclically repositioned relative to the source. For validation, course identity is `floor(((y + 43) % 512) * 6 / 512)`; the course split across the top/bottom edge is measured as one complete course.

## Verification

Luminance proxy: `0.2126 R + 0.7152 G + 0.0722 B`, using stored RGB values normalized to 0–1 (not linearized). The same definition is used before and after.

For the 2 × 2 repeat, the six-column seam window is `[509:515]`, compared with the six interior columns `[253:259]`. The row check uses the corresponding row windows. These include three pixels on each side of the seam. Targets are inclusive 0.97–1.03. Opposite edges must be exactly equal in all RGB channels. Band deviation is the largest absolute complete-course mean deviation from the median course mean; limit 5%.

| Candidate | Column seam ratio | Row seam ratio | Maximum course deviation | Opposite edges | Result |
|---|---:|---:|---:|---|---|
| green | 1.001763 | 0.992258 | 1.117% | Exact | PASS |
| violet | 0.998224 | 0.993213 | 1.312% | Exact | PASS |
| brown | 0.995300 | 0.999025 | 1.583% | Exact | PASS |
| patchwork | 0.994478 | 1.000226 | 0.806% | Exact | PASS |

Per-course mean luminance, in cyclic course order:

| Candidate | C0 | C1 | C2 | C3 | C4 | C5 |
|---|---:|---:|---:|---:|---:|---:|
| green | 0.315113 | 0.315799 | 0.316955 | 0.312842 | 0.318927 | 0.317642 |
| violet | 0.255981 | 0.256438 | 0.257456 | 0.253576 | 0.259243 | 0.257742 |
| brown | 0.258086 | 0.258913 | 0.260284 | 0.255489 | 0.261693 | 0.260386 |
| patchwork | 0.331965 | 0.333827 | 0.334337 | 0.331224 | 0.334003 | 0.334544 |

Before correction:

| Source | Column seam ratio | Row seam ratio | Maximum course/cap deviation |
|---|---:|---:|---:|
| green | 0.790173 | 1.088532 | 7.329% |
| violet | 0.825835 | 1.164396 | 11.614% |
| brown | 0.850090 | 1.082237 | 6.446% |
| patchwork | 0.846648 | 0.920038 | 6.431% |

The before measurements treat the faulty cap and partial final course separately, as actually drawn. Final measurements cover six complete regular courses.

Visual inspection covered the native-size green and patchwork tiles and the final four-material 3 × 3 review sheet. The dark tile grid, special cap stripe and clipped patchwork strips are removed. Ordinary horizontal course recesses remain intentionally. Source texture motifs still repeat at the tile period, as expected from a fixed tile. These are art candidates; proof/runtime approval is still pending.

## Reproduce

From this directory, on Windows with System.Drawing available:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\heal.ps1
& 'C:\Users\Tristixa-\.codex\skills\sprite-gen\.venv\Scripts\python.exe' .\check.py --write-review
```

Omit `--write-review` for a read-only check. Python is used for validation and the labeled comparison sheet; source-patch processing is in `heal.ps1`.

## Generation provenance and storage exception

An initial built-in ImageGen correction of green was rejected because it changed the texture too much. It is not used in any delivered tile. Its prompt is retained in `rejected-generation-prompt.txt`. No CLI/API generation fallback was used.

Although the prompt requested writes only in this run, the image tool automatically cached that rejected attempt outside the requested write area, at `C:/Users/Tristixa-/AppData/Roaming/orca/codex-runtime-home/home/generated_images/01a0e6bc-d26e-7ae2-844e-6a7aaeb46160/exec-fbd0c58a-1d2f-4779-96ee-baa0c9163f03.png`. This is an exception to the handoff's write-location requirement. All authored scripts, delivered artwork, source copies and review evidence are inside this run; the only authored file outside it is the requested five-line handoff report.
