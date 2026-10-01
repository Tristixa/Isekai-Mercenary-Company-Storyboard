# FGC region map v1: round-one fixes — look candidate

Open [review.html](review.html). **Everything newly made here is a candidate awaiting the owner's approval.** This package does not install assets, change game code, or lock canon.


## Round-one review fixes

[Before](superseded/review.html) / [After](review.html). The original mockups, overlays and QA were moved to `superseded/`; the original source package, previews, README and review page were copied there so the before view remains self-contained. No existing file was discarded. The painted map master and all three approved-art preview PNGs retain their pre-fix SHA-256 hashes in [fixes-baseline.json](sources/fixes-baseline.json).

1. Folder tabs use clipped kit paper and the kit border palette. Selected parchment joins the card edge; inactive navy tabs sit behind it. C has a locked, grey EURYDICA tab followed by two Frontier tabs. The detached diamond ribbon is removed.
2. All area plates are 280 x 44 px, close to the requested 260 x 44 target while keeping the full Erythra name at 24 px. Hylaea sits below the forest, Erythra below the ridges, and Bernmoor left of the marsh. The kit selected-row wash replaces the blue outline; plates have no end hairlines.
3. The den and stump now sit inside Hylaea's painted trees. A narrow parchment halo follows their transparent ink silhouette. The other three discoveries remain hidden in all screens; all five toggles remain available for review.
4. Italic ink labels read "Eurydica" and "South Gate road" directly on the map, without boxes. A thin parchment stroke around the letters keeps ink readable across painted detail.
5. Screen headers read "Elsie ? Adventurer Office" and "AREA DETAIL". LOOK CANDIDATE means awaiting owner approval; STRUCTURE ONLY means Frontier names and geography are not authored. These notes live here and in the review captions, outside the screen artwork.
6. B uses the complete kit disabled button, including its border, with Disabled #6E6C68 labels and no inner rectangle. The entire disabled piece is rendered at 1.12 brightness for contrast; disabled text remains the exact kit grey. C uses a lighter neutral grey #AAA7A1 on navy to maintain contrast on that dark surface.
7. Locked Erythra remains fully visible. Its composed vignette receives 60% saturation and a 16% parchment wash through a feathered mask. The map master is untouched; its plate holds the lock.
8. The retained approved-art preview has a 1 px Ink inner line inside its kit card frame.

## Review deliverables

- [A: Hylaea selected](mockups/A-hylaea.png): EURYDICA tab, three ranked area markers, Hylaea 42% ring and contained bar, Species 2/3, Dens 1/2, Rare lead none, Scout / Contract / Hunt. Hunt is the single primary action at bottom right. Exactly two discoveries are visible: one den and one other landmark.
- [B: Erythra locked](mockups/B-erythra-locked.png): Erythra preview, Rank D, lock, exact requirement “Requires Guild Rank D”, disabled actions, requirement repeated in the help ribbon. Disabled labels retain strong contrast.
- [C: Frontier tab structure](mockups/C-frontier-structure.png): disabled EURYDICA plus FRONTIER REGION 1 and FRONTIER REGION 2. **Structure only: Frontier names and geography are not authored.** Per the handoff, the same Eurydica map/card remain underneath solely for layout comparison. This is not a playable Frontier state. The handoff explicitly asks for the disabled historical Eurydica tab, although FGC_08 §5.9 describes Frontier-only tabs after the move.
- All mockups are 1920×1080. [720p proof A](checks/A-1280x720.png), [B](checks/B-1280x720.png), and [C](checks/C-1280x720.png) support readability review.
- Elsie's approved face crop uses the kit's dark face backing and thin frame. Her one-line bubble says exactly: “Boar tracks are thick near the South Gate this week.” No new portrait was generated.

## Geography and discoveries are proposals, not canon

The [untouched map master](sources/map-master.png) is 1536×1024. Eurydica is at the upper-left edge; its south-facing gate opens onto the nearby old-oak road to Hylaea. The river flows diagonally downstream toward Bernmoor's reedbeds and slow water. Erythra's red ridges and stone stairway vignette lie farthest away. This is a **proposed geography for owner review, not canon**, and is not a distance scale. The GDD's approximately ten-minute gate-to-outskirts trip is represented by a short nearby road, not converted into an invented world distance.

The map uses small painted area-identity vignettes surrounded by blank or faint parchment. These establish known area identity; they do not reveal discoverable dens, landmarks or hidden paths. No text, area labels, emblems, logos or crests are baked into the master. UI labels and rings are composed separately. The existing kit watermark is confined to the UI card layers, not generated into the map art.

Five transparent, full-map-size PNGs live in `overlays/`: `den-oak`, `den-rock`, `landmark-stump`, `hidden-path-1`, and `hidden-path-2`. They share the master's 1536×1024 coordinate system. The isolated drawings are also retained in `overlays/cutouts/`. [placement-manifest.json](sources/placement-manifest.json) records their locations and the mockup transform. [Alignment proof](overlays/alignment-proof.png) shows all five; it is not the 42% exploration state. The HTML offers independent discovery toggles.

The oak-root den, rocky den, broken stump and two woodland trails are **visual stand-ins proposed for this look test**. They have no new authored names, rewards, species bindings or runtime IDs. One den plus the stump are revealed in A/B/C. The other den and both hidden paths remain absent. This follows the requested two-overlay sample without asserting that 42% guarantees either find; GDD §7.2 also allows eligible random finds before guaranteed milestones.

## Source authority and provenance

Read-only sources under `D:/Storyboards/Isekai Mercenary Company/`:

1. `Game Design/FGC_08_UI_HUD_Spec.md`, §§2.1–2.6, 3, 5.9; `Game Design/IMC GDD.md`, §§7.1–7.2.
2. `UI Kit/Approved v1/README.md`, `kit.json`, `kit/`. The source build at `D:/Codex/IMC/runs/ui-kit-v1/sources/` supplied the established nine-slice convention, palette, fonts and local renderer. The kit was reused, not regenerated.
3. The three `Environment Assets/<area>/Far Background - Approved Source.png` files for Hylaea, Bernmoor and Erythra Highlands. These were the three artistic references **attached to built-in map generation**, plus `UI Kit/Approved v1/kit/layers/paper.png` for parchment tone. The transparent map frame was inspected but not attached as an art reference.
4. `Characters/Officers/Elsie/Base.png` for Elsie's approved portrait.

[provenance.json](sources/provenance.json) lists every reused asset's absolute source path, local copy and SHA-256. [generated-hashes.json](sources/generated-hashes.json) protects the untouched generated masters. No project folders were written. The run and the requested report are the authored destinations; the built-in image service also retains its normal generated-image cache.

The six owner screenshots in `Research/Region Map/` were **viewed only, never attached to generation or copied into the package**. Strange Brigade informed map-plus-detail structure; Atelier Ryza informed painted vignettes and corner advice; Hyrule Warriors and Infinity Strash informed preview placement; Metaphor informed only the corner character idea; FE3H informed the paper list/detail grammar. Their assets, frames, political maps, tilted paper and brush-slash styling were not copied.

## Generated versus composed

**Generated with the built-in image tool:** the painted map and five discovery ink drawings. Prompts are preserved verbatim in [map-prompt.txt](sources/map-prompt.txt), [overlay-prompt.txt](sources/overlay-prompt.txt), and [overlay-revision-prompt.txt](sources/overlay-revision-prompt.txt). The map master is unchanged; no cleaned map derivative was needed. The original discovery sheet remains in [overlay-master.png](sources/overlay-master.png). A transparency-focused revision is retained separately as [overlay-revision.png](sources/overlay-revision.png), but the original was selected after its real alpha was checked. Dark RGB around transparent pixels in the tool preview was not an opaque backdrop. Each drawing was cropped and scaled into its own aligned canvas; round-one fixes add a silhouette-following parchment halo while retaining the original ink and transparent surroundings.

**Composed from approved art, without generating new environments:** [Hylaea](previews/hylaea.png), [Bernmoor](previews/bernmoor.png), [Erythra](previews/erythra.png), each 1600×900 (16:9). All use the approved far painting, ground layer and foreground/mid elements. Hylaea adds `Approved Calibration v1/clean/Ground Tile.png` and its approved individual tree, canopy, fern and bush cutouts. Bernmoor and Erythra use their approved `Ground Tile`, `Mid Layer` and `Foreground` source sheets. Magenta was keyed locally, the selected connected object isolated from adjacent sheet fragments, and the ground blended into the far layer. Extracted sheets remain in `previews/layers/`; placements and crops are in the manifest and composition source. These are static review compositions, not claims of runtime parallax, seamlessness, collision or finalized battle staging.

**Composed UI:** kit paper → separate low-opacity multiply stains (8–9%) → kit watermark (5%) → nine-sliced pattern frame → content. The painted map fills its own framed card. Data strips behind rank/progress text are plain parchment. Help and hint plates are plain tier-3 kit pieces. The header, folder tabs, primary/secondary buttons, contained progress track/fill, rank badges, lock, portrait backing/frame and help/hint pieces are all recorded in `sources/qa.json`. Text plates preserve contrast without altering approved PNGs.

Font C is Cormorant Garamond SemiBold for headings/names and Alegreya with lining figures for body and numbers. Font files and OFL licenses are included under `sources/fonts/`. The parchment/navy GDD palette is retained rather than the unadopted alternate palette table in §2.3.

## Checks and rebuilding

[checks/verification.json](checks/verification.json) records sizes, contrast, overflow, overlay alpha, source and preservation hashes, local links and report length. All 82 text draws pass 4.5:1; the minimum is 5.05:1, including disabled labels. Contrast is sampled beneath actual glyph pixels with mask alpha at least 128 before the text fill, including the parchment outline behind italic map labels. Full bounding boxes are still checked for screen and width overflow: zero overflows. Names are 24 px or larger at 1080p; compact ring percentages are 16 px (10.7 px at 720p), with full 28 px exploration values repeated in the detail panel. The three 1280 x 720 proofs were visually inspected for legibility and clipping. These are scaled screen proofs, not native reflow layouts or runtime accessibility certification.

Build with `node sources/build.mjs`, then `node sources/package.mjs`. The build reads and retains the existing approved preview PNGs verbatim and writes only inside this run. The package step checks the frozen pre-fix hashes instead of replacing them. Preview composition placements are retained from the archived manifest. `sources/compose.js` remains the editable UI and overlay composition.

Run `C:/Users/Tristixa-/.codex/skills/sprite-gen/.venv/Scripts/python.exe sources/verify.py`, then `node sources/verify-review.mjs`. Verification checks approved sources against their originals and the requested six-line report at `D:/Codex/IMC/handoff/region-map-v1-fixes-last.txt`. The report is the explicit exception to the handoff's run-only write scope. The browser check exercises state selection, disclosure captions, discovery toggles, broken-image detection and review overflow at 1280 x 720.

No game integration is performed. Owner selection of this look is the next content decision; approval is not inferred from successful checks.
