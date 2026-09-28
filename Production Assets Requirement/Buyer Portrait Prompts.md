# Buyer portrait prompts (Counter-offer minigame)

Written 2026-09-28. Portraits for the five negotiation buyers in `Characters/Negotiation Buyers Roster.md`: the Travelling Merchant (Eurydica) and the four Frontier faction traders. The designs are **proposals**; change anything in the roster before generating.

## What each buyer needs

Save them like the officers: `Characters/Buyers/<Name>/Base.png` plus one PNG per expression. Candidates are made in `D:/Codex/IMC/Buyers/<Name>/`, and only approved portraits go into the project.

| File | Expression | Meaning in the minigame |
|---|---|---|
| `Base.png` | **Neutral**: the identity master, calm and listening | Default and opening look |
| `Pleased.png` | Pleased, a warm small smile | Your price is comfortably under their ceiling |
| `Considering.png` | Considering, thinking it over (hand to chin, eyes aside) | Close to their ceiling |
| `Doubtful.png` | Doubtful, one brow raised, lips pressed | A little over, or an unconvincing tactic |
| `Irritated.png` | Irritated, frowning, cold look | Well over, or an offending tactic |
| `Surprised.png` | Surprised, eyes widened, leaning back slightly | A strong tactic (Pristine goods, a generous bundle) |
| `Deal.png` | Deal, satisfied, a confident smile, hand offered | Closing the deal |
| `WalkAway.png` | Walk-away, dismissive, turning the head or shoulder away | Patience gone |
| `Bluff.png` (**Silas Crane only**) | Mock irritation with the eyes still smiling | His fake-irritation tell |

That's 8 images per buyer (9 for Silas), **41 in total**.

## Workflow

1. **Base first:**
   - Generate the Base portrait with the style master attached as the **style** reference: `Portrait Styles/tristitia.png`, or the skill copy `C:/Users/Tristixa-/.codex/skills/imc-portrait-art-direction/assets/tristitia-style-master.png`.
   - Use the shared block below, plus the buyer's identity block, plus "Expression: Neutral".
   - Get the Base approved before making expressions.
2. **Expressions:** attach the approved Base as the **identity, costume and composition** reference (and the style master as style). Change only the face, and the hand gesture where the table above says so. Same crop, angle, lighting, outfit and palette.
3. **Delivery:**
   - Keep the untouched masters (1086×1448).
   - The game deliverable is **768×1024 RGBA PNG with transparency**, prepared separately (the portrait guide's technical standard).
   - Review at dialogue-crop size, since the expressions must read apart when small.

## Shared block (every call)

```text
IMC portrait in the locked style of the attached style reference: sculpted cel-painted JRPG portrait illustration, strong anime foundation, controlled clean contours, planar shadow shapes, painted tonal changes with selective soft transitions, broad quiet regions between organised details. Expressive eyes with purposeful lids and brows, simplified nose and lips, clearly adult facial structure. Hair built from broad flowing ribbons and readable locks, no filament flyaways. Distinct material treatment: quiet skin, ribboned hair highlights, cloth in large value planes, metal with bright bevels, leather muted. One coherent light from the upper left. Framing: head to upper thighs, characterful torso turn and a purposeful hand gesture, facing slightly toward the viewer's left (the buyer sits across the counter from the Commander, who is on the left of the dialogue view). Plain flat light-grey background, no scenery, no text, no logo, no frame, no signature. Do not copy the style reference's character, hair, outfit, pose or weapon; take only its drawing and rendering.
```

For an expression call, add:

```text
Keep the attached Base portrait's exact identity, face, hair, outfit, palette, crop, camera angle and lighting. Change only the facial expression (and the hand gesture if stated) to: [EXPRESSION LINE FROM THE TABLE].
```

## Identity blocks

### The Travelling Merchant (man, Eurydica)

```text
A man in his mid-forties, 170 cm, wiry and restless, half-turned as if the next customer is already calling. Weathered friendly face with smile lines, sharp nose, quick bright brown eyes that seem to be doing sums, salt-and-pepper stubble, light olive skin. Salt-and-pepper curly hair under a wide-brimmed traveller's hat with a single feather. A patched long travelling coat covered in pockets, a bright mustard scarf, a crossbody satchel stuffed with papers and receipts, fingerless gloves, a ring of mismatched keys on his belt. One hand lifts his hat brim in greeting. Appeal: the lovable, well-connected fixer who never has much gold. Palette: faded brown and olive coat, mustard scarf accent, worn leather.
```

### Silas Crane (man, the Frontier Exchange)

```text
A man in his early thirties, 186 cm, tall and loose-limbed, lounging even when standing. Handsome fox-like face, narrow eyes that are always smiling, wide easy grin, pale skin. Dark hair slicked back with one stray lock falling across his forehead. A sharp charcoal three-piece suit with a loosened cravat, black gloves, and a sand-coloured Frontier greatcoat worn over his shoulders like a cape. A brass pocket-watch chain twirled around one gloved finger. Appeal: the charming spectator who bets on you and enjoys the gamble a little too much, friendly and faintly unsettling (original design; the personality is inspired by a thrill-loving broker type). Palette: charcoal and sand, brass accent, black gloves.
```

Silas's extra expression:
```text
Bluff: a mock-irritated frown and a sharp word on his lips, but his narrow eyes are still visibly smiling, as if enjoying the test.
```

### Aldric Harrow (man, the Iron Ledger Consortium)

```text
A man in his late forties, 188 cm, broad-shouldered and very upright. Strong, severe, handsome face, cool grey eyes, fair skin. Ash-blond hair combed straight back, greying at the temples, and a short, precisely trimmed beard. A long charcoal frock coat with iron-grey trim and a high collar over a dark waistcoat; a small iron-bound ledger hanging on a chain at his hip; a heavy iron signet ring. One hand rests on the ledger. Appeal: the stern gentleman whose rare approval is worth more than gold, exact and quietly fair. Palette: charcoal, iron grey, a dark oxblood waistcoat as the only warm accent. No glasses and no monocle.
```

Aldric barely shows feeling, so draw his expressions as **small, controlled changes**: a tightened jaw, a slight narrowing of the eyes. Pleased and Surprised are subtle; Deal is the only clear smile.

### Madame Ottilie Valcourt (woman, House Valcourt)

```text
A woman in her late twenties, 168 cm, graceful and slender. Delicate doll-like face, long lashes, bright green eyes, a sweet dimpled smile, porcelain skin. Blue-black hair in an elaborate braided updo held with a jewelled pin. An emerald and gold travelling gown with a structured riding jacket, lace gloves, pearl earrings, and a lacquered folding fan held near her face. Appeal: the glamorous noblewoman with a collector's hunger, sweet-voiced and fiercely acquisitive underneath. Palette: emerald and gold, black hair, pearl white.
```

Ottilie's **Considering** shows her **lowering the fan** and looking at the goods with a sharp, calculating expression. It's her real tell, so it must look clearly different from her Pleased face.

### Captain Sabine Duquesne (woman, the Meridian Charter Company)

```text
A woman in her mid-thirties, 178 cm, athletic and strong. Bold open face, confident grin, dark amber eyes, freckles across sun-bronzed skin. Cropped ash-brown hair under a wide charter-captain's hat with a brass company badge. A long navy and cream charter coat with brass company buttons and rolled sleeves, a sabre at her hip, a leather map-case slung across her back, tall riding boots. One hand rests on the sabre hilt. Appeal: the dashing captain whose laugh fills the room, warm, decisive and loyal to anyone who keeps their word. Palette: navy and cream, brass, warm leather.
```

## Checks before approval (from the portrait guide)

- The locked style matches the style master; the character reads as themselves at thumbnail and dialogue-crop size.
- **The 8 expressions read clearly apart when small.** That matters most here, because the face is the gameplay.
- No officer signature is copied: no long silver hair, no blonde high ponytail, no red bun, no black-with-red-streak hair, no glasses.
- Clean edges on the transparent deliverable; masters kept untouched.
