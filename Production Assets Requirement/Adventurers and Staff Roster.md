# Adventurers and Staff Roster

Written 2026-09-27. This is the character reference for everyone the Company hires: the four starting adventurers, the three starting staff, and the first mage planned for Chapter 2. It is also the **template for later chapters**: every new adventurer or staff member gets an entry in the same format (section 5).

Game rules for these characters (stats, passives, skills, progression) live in `Game Design/IMC GDD.md` sections 6 and 9. This file owns their **look, personality and asset list**. If the two ever disagree about a number, the GDD wins.

## 1. Rules for every hired character

- **Hand-designed, never lost.** Every adventurer and staff member is designed one by one, with their own portrait and sprite. Nobody dies or leaves for good (GDD 6.4a), so each design is permanent.
- **Adult and appealing.** Each character has a deliberate appeal archetype and a clear adult age presentation. Vary age, face, build, height, hair, silhouette and temperament across the cast. The clothes say what they do.
- **Never mistaken for an officer.** New characters must not share an officer's signature. The table below lists what is taken:

| Officer | Signature to avoid copying |
|---|---|
| Tristitia | Long silver hair, violet eyes, black and red officer coat, rapier |
| Elsie | Long blonde hair in a high ponytail, blue-grey eyes, olive jacket, longsword with kicks and punches |
| Liliana | Red hair in a bun |
| Steady Mae | Brown wavy hair, warm homely look |
| Fulker | Black hair with a red streak |
| Valerie | Black hair, glasses, soft and chubby merchant |
| Commander | Young man with short black hair |

- **Readable at 93 pixels.** Each character needs one silhouette hook that still reads in a 64-pixel-wide sprite cell (a hood, a shield shape, a big hammer, a satchel). Colour blocks should be large; small details won't survive.
- **Sprites have no mouth.** Expression lives in the portraits.

## 2. Assets each character needs

Use the existing workflow in `Character Sprites/Gemini Sprite Prompts.md` (sheet first, then the videos, start frame = cleaned sheet pose, one direction per walk video, outfit locked) and the locked portrait style in `Portrait Styles/`.

| Asset | Adventurers | Staff |
|---|---|---|
| Portrait, locked style, 7 expressions (Happy, Serious, Sad, Anger, Fear, Surprise, Laugh) | Yes | Yes |
| Gemini sprite sheet (4 directions, idle) | Yes | Yes |
| Video 1: walk (down, up, sideways) | Yes | Yes |
| Video 2: work, greet and idle | Yes | Yes (their work loop at their station) |
| Video 3: battle idle, attack, skill | Yes | No |
| Video 4: hurt, guard, victory, defeat | Yes | No |
| Key colour | Green #00FF00, unless the character wears green; then magenta #FF00FF | Same rule |

Save them the same way as the officers: `Characters/Portrait Expressions/<Name>/`, `Character Sprites/<Name>/`.

## 3. The four starting adventurers

They are hired in Chapter 1 when recruitment opens (story milestone M02). They are the first party, so they should look like a team that belongs together without matching: four different silhouettes (coat, hood, shield, hammer) and four different hair colours.

### Anselm Voigt: the dependable front line

| | |
|---|---|
| Role | Adventurer, Vanguard. Melee, front row. Signature skill **Phalanx** (DEF +50% for his next 3 actions); passive **Shieldbearer** (+25% DEF in the front row). Defender meter (fills when he is hit). |
| Stats | HP 180, ATK 18, DEF 10, rate 1.0. Hire 250G, wage 90G a week. |
| Kit | Arming sword and a long, heavy watchman's coat (the coat is his armour). |
| Age and build | Late twenties. 180 cm, broad-shouldered, solid rather than bulky. |
| Face and hair | Friendly, open face with a strong jaw and a small scar through one eyebrow. Short chestnut-brown hair, slightly messy. Warm hazel eyes. |
| Outfit | A deep teal, knee-length watchman's greatcoat with brass buttons and a high collar, over a padded grey gambeson. Brown leather belt and bracers, dark trousers, sturdy brown boots. A small brass bridge-watch badge on the collar. |
| Silhouette hook | The long coat flaring below the knee. |
| Appeal | Handsome and dependable: the reliable older brother of the party. |
| Personality | Calm, steady, quietly funny. A former bridge watchman who keeps the line when others waver (traits Steadfast, Shield-trained). Takes blows so younger members don't have to. |
| Battle feel | Solid, planted strikes. **Phalanx:** he plants his feet and raises the sword crosswise in a guard, with a brief pale steel shimmer. |

### Nell Larkin: the tracker

| | |
|---|---|
| Role | Adventurer, Ranger. Ranged, back row. Signature skill **Frost Arrow** (a hit that slows one enemy for 3 actions); passive **Tracker** (+10% group chance for the hunt target, +10% scout find chance). Attacker meter (fills when she hits). |
| Stats | HP 150, ATK 16, DEF 8, rate 1.0. Hire 250G, wage 90G a week. |
| Kit | Wooden recurve bow and a hip arrow case. |
| Age and build | Mid twenties. 165 cm, lean and athletic. |
| Face and hair | Lively, sharp-eyed face with a few freckles. Warm brown skin. Very dark brown hair in one long braid over her shoulder. Amber eyes. |
| Outfit | A short hooded capelet in faded teal-grey (hood down in the portrait, can be up in walk sprites), a cream linen shirt, a brown leather jerkin, a leather bracer on her bow arm, fingerless gloves, a tool pouch, light brown boots. Small carved-wood charm on the braid. |
| Silhouette hook | The hood and the bow on her back. |
| Appeal | Athletic and cheerful: the sharp, playful outdoors expert. |
| Personality | Bright, curious, blunt about danger. She guided timber caravans through Hylaea and reads tracks like text (traits Keen-eyed, Trailwise). Loves a good find more than a good fight. |
| Battle feel | Quick draws from the back row. **Frost Arrow:** a longer draw, then an arrow that leaves a thin pale-blue frost trail. |

### Severa Kaltenbach: the greatsword warden

| | |
|---|---|
| Role | Adventurer, Warden. Melee, front row. Signature skill **Diving Splitter** (2.5× damage to one enemy); passive **Big Game Hunter** (+20% ATK and attack rate against Elite monsters). Attacker meter. |
| Stats | HP 175, ATK 17, DEF 16, rate 1.0. Hire 300G, wage 105G a week. |
| Kit | A greatsword, deliberately **shorter than full body length** (the blade reaches about her chest when planted), because full-length greatswords broke the battle videos. No shield. |
| Age and build | Early thirties. 176 cm, tall, lean and strong, upright posture. |
| Face and hair | Composed, elegant face with high cheekbones and a cool gaze. Fair skin. **Dark navy-black hair** in a neat low bun with a few strands loose. Pale ice-blue eyes. |
| Outfit | Steel half-plate (breastplate, pauldrons, gauntlets) over a dark blue gambeson, with a white-and-steel-blue tabard bearing a steel-blue six-pointed frost emblem. The greatsword has a broad plain blade and a steel-blue wrapped grip. Grey trousers, steel-capped boots. A short dark-blue shoulder cape on one side only. |
| Silhouette hook | The greatsword carried over her shoulder and the one-sided cape. |
| Appeal | Cool and dignified: the knight who rarely smiles, which makes it count when she does. |
| Personality | Disciplined, watchful, dry humour. She held the northern watch through two winters (traits Disciplined, Watchful) and hunts big game because it tests her. Respects Anselm, argues tactics with Otto. |
| Battle feel | Heavy, measured two-handed swings. **Diving Splitter:** a short run-up and leap, then a two-handed downward cleave. Keep the whole blade in frame: never raise it straight overhead. |
| Design note | The old 2D-era art gave her silver hair and a greatsword. Silver hair belongs to Tristitia, so her hair is redesigned. She keeps a greatsword, now shorter than full body length. |

### Otto Grimbald: the breaker *(redesigned 2026-09-28; name to be replaced)*

| | |
|---|---|
| Role | Adventurer, Breaker. Melee, front row. Signature skill **Hammerfall** (a hit that stuns one enemy for 1 action); passive **Ironclad** (+20% DEF in the front row, immune to stun). Defender meter. |
| Stats | HP 205, ATK 18, DEF 8, rate 1.0. Hire 325G, wage 110G a week. |
| Kit | **Full plate armour, a closed helmet, and a heavy two-handed warhammer.** No shield, and no later shield outfit. |
| Design | Owner's redesign, in progress. The earlier look (leather apron, bare arms) read as a generic middle-aged man. The plate and helmet give him a clear armoured silhouette. In portraits the visor can be raised to show his face (owner's call). |
| Silhouette hook | The closed helmet and the warhammer head, with a wide armoured stance. |
| Appeal | The walking fortress: slow, unstoppable, reassuring to stand behind. |
| Personality | Loud, generous, stubborn. A quarry foreman turned adventurer who opens every fight and trusts the others to cover him (traits Unshakable, Heavy-handed). Treats the young ones like his crew. |
| Battle feel | Slow, heavy swings with big follow-through and a clank of plate. **Hammerfall:** an overhead warhammer blow that drives the enemy down with a short stagger shake and a burst of stone dust. |

## 4. The three starting staff

Staff never fight. They work in a department under an officer, visible at their station in the HQ. They are hired alongside the adventurers when their service opens.

### Konrad Metzler: processor (Processing Room, under Steady Mae)

| | |
|---|---|
| Role | Processor. Specialty: field anatomy (traits Methodical, Careful hands). Hire 150G, wage 60G a week. Joins with recruitment (M02); works once processing opens. |
| Age and build | Late fifties. 185 cm, tall and big-framed, slightly stooped. |
| Face and hair | Kind, heavy-browed face and big gentle hands. Bald with a neat grey beard and bushy grey eyebrows. Deep brown skin. Dark eyes behind a squint. |
| Outfit | A long, scrubbed butcher's apron (off-white, a few old stains) over a dark green work shirt with rolled sleeves, leather forearm guards, a belt of wrapped knives and a cleaver, clogs. |
| Silhouette hook | The long apron and the knife belt. |
| Appeal | Gentle giant: a grandfatherly craftsman who is terrifying with a cleaver and kind with everyone else. |
| Personality | Quiet, patient, precise. A lifelong butcher who wants nothing wasted from any creature the Company brings home. Mae's calm right hand. |
| Work loop (video 2) | Sharpening a knife on a whetstone, then inspecting a hide against the light. |

### Cassia Susurra: information clerk (Information Office, under Liliana)

| | |
|---|---|
| Role | Information staff. Specialty: market intelligence (traits Observant, Well connected). Hire 150G, wage 60G a week. |
| Age and build | Early thirties. 158 cm, petite and quick. |
| Face and hair | Sharp, clever face and a knowing half-smile. Olive skin. **Short plum-purple bob** with a straight fringe. Grey eyes. Ink stains on her fingers. (Use a deep plum that reads clearly purple, not pink.) |
| Outfit | A mustard-yellow travelling coat with many pockets, a black high-necked blouse, a brown skirt over leggings and ankle boots. A leather satchel stuffed with notebooks, and a pencil behind one ear. |
| Silhouette hook | The bob, the long mustard coat and the bulging satchel. |
| Appeal | Charming and mysterious: the woman who always knows a little more than she says. |
| Personality | Chatty, nosy, very organised. A former caravan clerk whose notebooks connect distant purchases to tomorrow's demand. Trades gossip like currency. |
| Work loop (video 2) | Flipping through a notebook, then pinning a note to a board. |

### Ulrich Esser: craftsman (Workshop, under Fulker)

| | |
|---|---|
| Role | Craftsman. Specialty: equipment smith (traits Patient, Exacting). Hire 200G, wage 75G a week. Joins when the Workshop opens (M05). |
| Age and build | Late thirties. 183 cm, broad chest and shoulders, strong arms. |
| Face and hair | Serious, handsome face with a short dark stubble. Light skin reddened by forge heat. **Salt-and-pepper hair** tied in a short tail. Steel-grey eyes. Old burn marks on his forearms. |
| Outfit | A heavy brown leather smith's apron over bare arms and a charcoal undershirt, thick gloves tucked in the belt, goggles pushed up on his head, leather trousers, work boots. A hammer and tongs on his belt. |
| Silhouette hook | The goggles on his head and the tail of hair. |
| Appeal | Rugged and handsome: the quiet craftsman whose work speaks for him. |
| Personality | Patient, exacting, a man of few words. A travelling smith who wants a permanent forge and people worth equipping. Clashes with Fulker's speed, respects Fulker's results. |
| Work loop (video 2) | Hammering a glowing blade on the anvil, then quenching it in a hiss of steam. |

## 5. Template for new characters

Copy this for every adventurer or staff member added in later chapters.

```markdown
### <Full Name>: <one-line hook>

| | |
|---|---|
| Role | Adventurer (<Specialty>; melee or ranged; usual row; signature skill and meter role; passive) OR staff (<department>, under <officer>) |
| Stats | HP, ATK, DEF, rate (adventurers). Hire cost and weekly wage. When they join (chapter or story milestone). |
| Kit | Weapon and armour (adventurers) or tools (staff) |
| Age and build | Adult age presentation, height, build |
| Face and hair | Face shape, skin, hair colour and style, eye colour, one distinguishing mark. Check section 1 so nothing matches an officer. |
| Outfit | Main pieces and 2–3 main colours |
| Silhouette hook | The one shape that reads in a 64-pixel sprite |
| Appeal | The appeal archetype |
| Personality | Three traits, background in one or two sentences, a relationship hook |
| Battle feel / Work loop | How attacks and the skill look, or what they do at their station (video 2) |
```

## 6. Planned: the first mage (Chapter 2, proposal)

**Chloris** already has a Gemini sprite sheet and a "Battle to Buff to Attack" clip in `Character Sprites/Chloris Linde/`: dark hair in a loose updo, green eyes, round glasses, a dark-teal scholar's cloak with gold trim, and a green gem at her collar. The GDD proposes her as the first mage (6.2a): a support caster in the back row with the skill **Verdant Blessing** (front row ATK UP and DEF UP), joining after the first promotion.

Before her portrait is made, one thing to decide: she wears glasses and has dark hair, like Valerie. Her gem, cloak and green magic keep her distinct, but her portrait should make the difference obvious: a younger scholar, slimmer, green-and-gold palette, the gem as her signature. Her full entry, in the template above, will be written once she is confirmed.
