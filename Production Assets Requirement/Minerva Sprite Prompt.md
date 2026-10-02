# Minerva Alraun: base sprite sheet prompt (Gemini)

Written 2026-10-02 from her approved portrait. It follows the base-sheet format in `Gemini Sprite Prompts - Cast v2.md` §1, and the cleaning and mirroring rules in `Gemini Sprite Prompts.md`.

**Attach, in this order:**
1. `Character Sprites/Officers/Liliana/Sprite Sheet.jpg`: style and proportion.
2. `Characters/Officers/Minerva Alraun/Base.png`: design.

**Choices made here:**
- **Height:** about 94 art px, for the proposed 170 cm.
- **Key colour:** green `#00FF00`, because her outfit has dark wine-red panels and a red vial. This follows the standing rule of green for red or violet designs.
- **Three columns:** facing right is mirrored in the engine.
- **Emblem-like ornaments dropped:** the compass pendant, the hanging armillary charm, the pouch ornament and the stocking pattern.
- **Boots:** the portrait doesn't show her feet, so plain black heeled ankle boots are proposed.
- **Prop:** the book from the portrait.

```
Pixel-art character sprite sheet of Minerva Alraun for an HD-2D JRPG.

References:
- Image 1 (Liliana's sprite sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), the same large eyes with a single highlight, the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. Minerva must look like a member of the same cast as Liliana. Ignore Image 1's costume, hair and colours, and ignore its background colour and its four-column layout.
- Image 2 (Minerva's portrait) is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height, pose or face drawing.

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about 94 art pixels tall from the top of the hair to the soles, every sprite on the sheet at the same scale. She is slightly taller than Liliana.

Face: large red-brown eyes with a highlight, like the reference. NO mouth, NO lips, NO nose.

Design: an elf woman in her late twenties with long pointed ears showing through her hair. Very long, full, wavy auburn-brown hair, side-parted, framing her face and falling to her hips. Small round gold wire glasses with a faint red tint; her eyes stay clearly visible through them. A plain black choker with no buckle and no pendant. A black sleeveless halter dress: a dark sheer upper panel, a fitted black bodice with a dark wine-red centre panel and two small gold clasps, thin gold trim along the edges, and long open skirt panels, black outside and dark wine-red inside, parted at the front to show her legs and falling to about calf length. A brown leather belt slung low across the hips, with a plain brown pouch on one hip and two small glass vials, one red and one blue, on the other. Bare hands with black nails. Black thigh-high stockings with plain tops and a thin garter strap. Plain black heeled ankle boots. She carries a closed brown leather book with gold corners in one arm, as in Image 2. Keep only details large enough to read at this size; few buckles; no emblems, symbols or logos (no pendant, no hanging charm, no ornament on the pouch, no pattern on the stockings).

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid pure green #00FF00 filling the whole image. No gradient, floor, ground shadow, text, labels or panels.
```

**After the sheet:** clean it with the usual snap-and-clean pass. Then make her walks and her work loop (`Officer Work Animation Prompts.md`, Minerva Alraun) from the cleaned start frames. The work loop's design line is older; update it to this design before using it.
