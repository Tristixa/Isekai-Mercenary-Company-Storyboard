# Minerva Alraun: portrait design and prompts

Written 2026-09-30. **Minerva Alraun, Chief of Research** (Frontier). She makes the Frontier's consumables, tiers 1–5.

- **Her V1 pass** (four images, not yet in the IMC portrait style): `C:/Users/Tristixa-/Pictures/IMC/Officers/V2/Candidate/Chief Of Research/`.
- **This document** turns that pass into one locked design for the portrait skill (`$imc-portrait-art-direction`): what to keep, what to remove or redesign, her personality, and paste-ready prompts for the base portrait and the seven expressions.
- **It's a design plan, per the standing rule:** agree it before generating.

## 1. Identity at a glance

| | |
|---|---|
| Role | Chief of Research, the new Frontier officer who heads the Research Department |
| Race and age | Elf (long pointed ears). Looks late twenties; as an elf she may be older than she looks, which is a story option, not a visual change. |
| Height and build | About 170 cm (proposed); slender with a curvy figure |
| Palette | Black and charcoal, wine red, cream, antique gold (restrained); auburn-brown hair; red-brown eyes |
| **Visual identity (owner, locked)** | **Small round wire glasses that never hide her eyes**, and a **plain black choker with no buckle** |
| Silhouette hook | The side-swept wavy hair over one eye, the round glasses, and the long open alchemist's coat |
| Signature gesture | Two fingers pushing her glasses up the bridge of her nose |
| Signature prop | A round-bottomed potion flask of red liquid in a slim gold cage |

## 2. Keep, remove, redesign (from the V1 pass)

### Keep
- **The elf ears:** long, pointed, angled slightly back through the hair.
- **The hair:** long, wavy **auburn-brown**, a deep side part with the fringe sweeping across one eye, and waves down past the shoulders. In the portrait style it's built as broad ribbon-like locks with pale highlight ribbons, not fine strands.
- **The glasses (identity):** **small, perfectly round, thin dark-gold wire rims**, sitting a little low on the nose. The lenses are **clear, or at most a very faint rose tint, so both eyes read clearly through them**. There's no dark or opaque tint and no glare covering the iris. The eyes behind them are red-brown and fully readable at dialogue size.
- **The choker (identity):** a **plain black band**, narrow and smooth, with **no buckle, no ring, no pendant**.
- **The alchemist's coat:** long, black, with a **wine-red lining**, a high structured collar, and wide sleeves turned back into **cream cuffs**. It's worn open, slipping off the shoulders.
- **The black corset bodice** under the coat, with a sheer black high neckline rising to the choker.
- **The flask:** a round-bottomed flask of red liquid in a slim gold cage (from V1 #1 and #4).
- **The vials:** **two** glass vials at the belt, one red and one blue, in simple leather loops.
- **Her expression and appeal:** the sly, knowing half-smile of someone who already knows the answer.

### Remove
- **Every emblem and symbol** (the owner's standing rule):
  - the wheel and compass medallions on the coat shoulder, the pouch and the belt;
  - the pendant hanging from the choker (the choker stays plain);
  - the arcane circle sigils on the book covers;
  - the cross-shaped and star-shaped metal fittings;
  - the rune pattern on the sash;
  - the embroidered symbols on the coat hem.
- **Buckle clutter** (the fewer-buckles rule): the second and third belts, the buckled wrist cuffs, the harness straps, and the thigh garter straps with metal ornaments.
- **Dark sunglasses-like lenses** that hide the eyes.
- **Extra props:** no stacked grimoires, no loose papers.

### Redesign
- **One belt:** a single brown leather belt, worn slightly low, with **one** small leather satchel and the two vials. It has one simple buckle, the only functional one.
- **Lower outfit:** a **black high-waisted skirt with a front slit over dark stockings**, or fitted black shorts over dark stockings. **Recommended: the skirt**, since it reads more scholar than adventurer. The owner's call.
- **Trim:** plain **antique-gold piping** on the coat edges and the collar. It's trim only, never a symbol.
- **Hands:** bare, with dark nail varnish. No gloves, which keeps the glasses gesture clean.

## 3. Personality (for the expressions)

- **Curious to the bone.** Every Frontier monster part is a puzzle and every failure is data. She lights up at the unknown.
- **Playful and teasing.** She speaks in a lazy, amused register, likes to watch people squirm a little, and is always a step ahead in a conversation. Never cruel.
- **Unflappable in the lab**, and blunt about findings: "It'll kill you. Fascinating, isn't it?"
- **Her anger is cold, not loud.** It comes from waste: ruined samples, careless handling, people who ignore her warnings.
- **Her softness is private.** She is quietly caring about the Guild's adventurers, since her potions keep them alive, but she hides it behind the smile.
- **Tells:** she pushes her glasses up when she's pleased with herself, and looks over them when she's judging someone.

## 4. The style master and references (every call)

| Reference | Role |
|---|---|
| `Portrait Styles/tristitia.png` (or the skill copy `assets/tristitia-style-master.png`) | **Style only:** drawing, rendering and finish. Don't copy Tristitia's face, silver hair, red scarf, armour, neckline, sword or pose. |
| V1 image `ChatGPT Image Sep 30, 2026, 05_21_21 AM.png` | **Design:** hair, ears, coat, flask, and the glasses gesture. Take the design only, per section 2; not its rendering, symbols or straps. |
| V1 image `ChatGPT Image Sep 30, 2026, 06_37_36 AM.png` | **Design (secondary):** the plain choker and the coat's red lining |

Output: a 1086×1448 master, and the game deliverable at **768×1024 RGBA with a transparent background**. Head to upper thighs; dialogue-crop first. Save candidates under `D:/Codex/IMC/Officers/Minerva Alraun/`; approved portraits go in `Characters/Officers/Minerva Alraun/`.

## 5. Prompts

### Shared block (every call)

```text
IMC portrait in the locked style of the attached style reference: sculpted cel-painted JRPG portrait illustration, strong anime foundation, controlled clean contours, planar shadow shapes, painted tonal changes with selective soft transitions, broad quiet regions between organised details. Expressive eyes with purposeful lids and brows, simplified nose and lips, clearly adult facial structure. Hair built from broad flowing ribbons and readable locks, no filament flyaways. Distinct material treatment: quiet skin, ribboned hair highlights, cloth in large value planes, metal with bright bevels, leather muted, glass clear and bright. One coherent light from the upper left. Framing: head to upper thighs, characterful torso turn and a purposeful hand gesture, facing slightly toward the viewer's left. Plain flat light-grey background, no scenery, no text, no logo, no frame, no signature. Do not copy the style reference's character, hair, outfit, pose or weapon; take only its drawing and rendering.
```

### Identity block (every call)

```text
Minerva Alraun, an elf alchemist and the Chief of Research, a woman who looks in her late twenties, about 170 cm, slender and curvy. Long pointed elf ears angled slightly back through her hair. Long wavy auburn-brown hair with a deep side part, the fringe sweeping across one eye, waves falling past her shoulders. Red-brown eyes, clearly visible. Small perfectly round glasses with thin dark-gold wire rims, sitting a little low on her nose, with clear lenses (at most a very faint rose tint) so both eyes read clearly through them, no dark tint and no glare over the irises. A plain narrow black choker band, smooth, no buckle, no ring, no pendant. A long black alchemist's coat with a wine-red lining and a high structured collar, plain antique-gold piping on the edges, worn open and slipping off her shoulders, wide sleeves turned back into cream cuffs. A black corset bodice with a sheer black high neckline rising to the choker. A black high-waisted skirt with a front slit over dark stockings. One brown leather belt worn slightly low with a single simple buckle, one small leather satchel, and two glass vials in leather loops, one red and one blue. Bare hands with dark nail varnish. Palette: black and charcoal, wine red, cream, antique gold, auburn hair. No emblems, no symbols, no sigils, no medallions, no runes, no crests, no logos anywhere on the costume or props; plain trim only. Few buckles: no harness straps, no garter straps, no buckled cuffs.
```

### Base (the identity master; approve this first)

```text
[SHARED BLOCK]
[IDENTITY BLOCK]
Expression: Base. A sly, knowing half-smile, eyes calm and amused, looking at the viewer as if she already knows the answer. Pose: two fingers of her right hand pushing her round glasses up the bridge of her nose; her left hand holds a round-bottomed flask of red liquid in a slim gold cage at shoulder height, slightly away from her body.
```

### Expressions

Attach the **approved Base** as the identity, costume and composition reference, plus the style master for style. Change only the face and the hands noted. Keep the same crop, angle, lighting, outfit and palette, the **glasses on and the eyes visible in every expression**, and the choker plain.

| File | Expression line to add after the two blocks |
|---|---|
| `Happy.png` | `Expression: Happy. Bright, delighted curiosity, eyes shining behind the glasses, a warm open smile. Same pose; the flask tilted slightly toward her as if admiring a result.` |
| `Laugh.png` | `Expression: Laugh. An amused laugh, eyes closed into curves, head tipped slightly back, the back of her right hand raised near her mouth. Flask hand as in the Base.` |
| `Serious.png` | `Expression: Serious. Analytical focus: she looks over the top of her lowered glasses (the glasses slid down her nose, the eyes still clearly visible above the rims), lips pressed, brows level. Right hand lowered, the flask held still at chest height.` |
| `Anger.png` | `Expression: Anger. Cold irritation, not shouting: eyes narrowed over the glasses, brows drawn down, lips tight in a thin line, jaw set. Right hand lowered and closed; the flask gripped firmly.` |
| `Sad.png` | `Expression: Sad. Quiet and private: eyes lowered and soft, brows slightly lifted at the inner ends, a small closed mouth. Her right fingertips touch the plain choker; the flask hand is lowered.` |
| `Surprise.png` | `Expression: Surprise. Eyes wide behind the glasses, brows raised high, lips parted; the glasses slipping slightly askew. The flask raised a little higher, as if a reaction just went unexpectedly.` |
| `Fear.png` | `Expression: Fear. Tense and alert: eyes wide, brows pulled up and together, lips parted; she draws the coat closed across her chest with her right hand, the flask held protectively close to her body.` |

## 6. Checks before approval

- **The locked style** matches the Tristitia master, and she reads as herself at thumbnail and dialogue-crop size.
- **The glasses:** small, round, thin wire rims. **Both eyes are clearly visible** in all eight images, with no dark lenses and no glare over the irises.
- **The choker:** plain black, **with no buckle or pendant**.
- **No emblems or symbols anywhere,** and few buckles (one belt buckle).
- **The eight expressions read apart when small.** Serious (looking over the glasses) and Anger (cold narrowed eyes) must be distinct.
- **She is distinct from the other officers** (Tristitia's silver hair and red scarf, Elsie's blonde ponytail, Mae's brown hair and leather vest, Fulker's black hair with a red streak, Liliana's red buns and red capelet, Valerie's black hair and glasses with a fur collar). **Valerie also wears glasses**, so Minerva's must stay small, round and wire-rimmed, and she keeps the auburn hair, the elf ears and the coat as her separators.
- **The technical deliverable:** 768×1024 RGBA, clean alpha edges on light and dark backgrounds, and the master kept untouched.
