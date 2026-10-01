// Builds the ready-to-paste section of "Gemini Sprite Prompts - Cast v2.md" from the templates and fill-ins.
const fs = require("fs");
const DOC = "D:/Storyboards/Isekai Mercenary Company/Production Assets Requirement/Gemini Sprite Prompts - Cast v2.md";
const FENCE = "```";
const MAGENTA = "pure magenta #FF00FF", GREEN = "pure green #00FF00";

const C = [
  { name: "Anselm Voigt", folder: "Anselm Voigt", sex: "man", he: "he", his: "his", key: MAGENTA, h: 98, adv: true,
    design: "young and enthusiastic; warm golden-blond short messy hair; brown eyes; silver-steel plate armour over a deep-teal surcoat; a medium teal kite shield with a steel rim on his LEFT arm (viewer's right in the front view); an arming sword on his right side. No emblems",
    lock: "silver-steel plate armour over a deep-teal surcoat, the teal kite shield on his left arm, the arming sword, short golden-blond hair; no emblems",
    sleep: "lying on his back, armour on, shield set down beside him, one arm behind his head",
    stance: "Pose: shield raised in front at chest height, sword held back and ready, feet planted.",
    weapon: "an arming sword and a teal kite shield", skill: "Phalanx: he plants his feet and raises the sword crosswise in a guard behind the shield, holds it, then relaxes back to the stance",
    guard: "the kite shield held up in front, covering his body, sword ready behind it", victory: "sword raised high in his right hand, shield lowered at his side", defeat: "shield lying flat beside him, sword still gripped" },
  { name: "Nell Larkin", folder: "Nell Larkin", sex: "woman", he: "she", his: "her", key: MAGENTA, h: 91, adv: true,
    design: "warm brown skin, freckles; very dark brown hair in one long braid over her shoulder; amber eyes; a green hooded capelet (hood down), cream shirt, fitted green tunic and legwear, brown leather jerkin, a bracer on her bow arm, fingerless gloves, light brown boots; a wooden recurve bow on her back and a hip arrow case",
    lock: "the green hooded capelet with the hood down, fitted green tunic and legwear, brown leather jerkin, the single long braid, the bow and hip arrow case",
    sleep: "curled on her side, hood up over her head, bow set beside her",
    stance: "Pose: bow held forward at the ready, an arrow nocked and half drawn, back straight.",
    weapon: "a wooden recurve bow", skill: "Frost Arrow: a longer, deeper draw, a held aim, then the release, and back to the stance",
    guard: "the bow held horizontally across her body, leaning back", victory: "bow raised overhead in one hand, the other hand on her hip", defeat: "bow resting on the ground under her hand" },
  { name: "Severa Kaltenbach", folder: "Severa Kaltenbach", sex: "woman", he: "she", his: "her", key: GREEN, h: 97, adv: true,
    design: "fair skin; navy-black hair in a neat low bun with a few loose strands; ice-blue eyes; steel half-plate (breastplate, pauldrons, gauntlets) over a dark-blue gambeson; a white and steel-blue tabard with the same pattern as the design image; a short dark-blue cape on one shoulder only; grey trousers, steel-capped boots; a broad plain greatsword shorter than her full height (the blade reaches her chest when planted), carried over her shoulder",
    lock: "steel half-plate over a dark-blue gambeson, the white and steel-blue tabard, the short dark-blue cape on one shoulder only, grey trousers, navy-black hair in a low bun, the greatsword shorter than her height",
    sleep: "sitting against an unseen wall, knees drawn up, greatsword leaning across her shoulder, head bowed",
    stance: "Pose: two-handed greatsword held diagonally in front, point up and slightly forward, feet apart.",
    weapon: "a two-handed greatsword", skill: "Diving Splitter: a short run-up and leap, then a two-handed downward cleave, and back to the stance. Keep the whole blade in frame; never raise it straight overhead",
    guard: "the greatsword held flat and horizontal in front with both hands, blade across her body", victory: "greatsword planted point-down in front, both hands on the pommel", defeat: "greatsword planted beside her, holding it to stay up" },
  { name: "Otto Grimbald", folder: "Otto Grimbald", sex: "man", he: "he", his: "his", key: GREEN, h: 96, adv: true,
    design: "full plate armour from head to toe in gunmetal steel with darkened-silver trim and small ochre padding at the joints; a closed German sallet helmet (rounded crown, lowered visor, narrow sight slit, swept neck guard) with a bevor covering the face; a heavy two-handed warhammer with a long wooden shaft and a rectangular iron head; no shield; a wide, planted stance",
    lock: "full plate armour head to toe with the closed sallet helmet and visor down at all times, the two-handed warhammer; no shield",
    sleep: "sitting on the ground against an unseen wall, helmet and armour still on, the warhammer across his lap",
    stance: "Pose: warhammer held diagonally across the body in both hands, head low and forward, feet wide.",
    weapon: "a heavy two-handed warhammer", skill: "Hammerfall: he raises the hammer high to one side and brings it down in a heavy overhead blow with a short stagger of follow-through, then back to the stance",
    guard: "the warhammer shaft held horizontally in front with both hands", victory: "warhammer resting on his shoulder, free fist on his hip", defeat: "warhammer head on the ground, both hands on the shaft" },
  { name: "Konrad Metzler", folder: "Konrad Metzler", sex: "man", he: "he", his: "his", key: MAGENTA, h: 99, adv: false,
    design: "late fifties, very tall, big-framed and slightly stooped; deep brown skin; bald with a neat grey beard and bushy grey eyebrows; a kind, heavy-browed face with a squint; a long off-white butcher's apron with a few old stains over a dark-green work shirt with rolled sleeves; leather forearm guards; a belt of wrapped knives and a cleaver; wooden clogs",
    lock: "the long off-white butcher's apron over the dark-green shirt with rolled sleeves, leather forearm guards, the knife belt, clogs, bald head and neat grey beard",
    work: "sharpening a knife on a hand-held whetstone, then holding a hide up to inspect it" },
  { name: "Cassia Susurra", folder: "Cassia Susurra", sex: "woman", he: "she", his: "her", key: GREEN, h: 87, adv: false,
    design: "early thirties, petite; olive skin; a short deep-plum bob with a straight fringe (clearly purple, not pink); grey eyes; a knowing look; a long mustard-yellow travelling coat with many pockets over a black high-necked blouse, a brown skirt over leggings, ankle boots; a leather satchel stuffed with notebooks; a pencil behind one ear",
    lock: "the long mustard-yellow coat, black high-necked blouse, brown skirt over leggings, ankle boots, the satchel, the short deep-plum bob",
    work: "flipping through a notebook held in one hand, then reaching out to pin a note to an unseen board" },
  { name: "Ulrich Esser", folder: "Ulrich Esser", sex: "man", he: "he", his: "his", key: GREEN, h: 100, adv: false,
    design: "late thirties, broad chest and shoulders, strong arms; light skin reddened by forge heat; salt-and-pepper hair tied in a short tail; short dark stubble; steel-grey eyes; goggles pushed up on his head; a heavy brown leather smith's apron over a charcoal undershirt with bare arms; thick gloves tucked in the belt; leather trousers, work boots; a hammer and tongs on his belt",
    lock: "the heavy brown leather apron over the charcoal undershirt, bare arms, goggles pushed up on his head, salt-and-pepper hair in a short tail",
    work: "hammering on an unseen anvil at waist height with a hand hammer, holding tongs in the other hand, in a steady rhythm" },
];

const refSheet = c => c.sex === "woman" ? "Character Sprites/Officers/Elsie/Reference Sheet.png" : "Character Sprites/Officers/Commander/Reference Sheet.png";
const refName = c => c.sex === "woman" ? "Elsie" : "Commander";
const block = t => `${FENCE}\n${t}\n${FENCE}\n`;

function sheet(c) {
  const design = c.adv
    ? `- Image 2 is the DESIGN reference: take ONLY the costume, colours, hair and equipment from it. Do NOT copy its body proportions, head size, height or face drawing.`
    : `- There is no design image for this character: follow the design description below exactly.`;
  return `Pixel-art character sprite sheet of ${c.name} for an HD-2D JRPG.

References:
- Image 1 (${refName(c)} reference sheet) is the STYLE AND PROPORTION reference. Match it exactly: the same head size (about one third of the total height), ${c.name === "Otto Grimbald" ? "" : "the same large eyes with a single highlight, "}the same short legs and stylised JRPG body, the same outline weight, the same pixel size and the same shading. ${c.name} must look like a member of the same cast as that character.
${design}

Pixel rules:
- True pixel grid. Every art pixel is an exact square block of 8×8 image pixels, aligned to one grid across the whole image.
- No anti-aliasing, no blur, no half-pixels (mixels), no soft gradients. Eyes are simple chunky pixel clusters, like the reference.
- Clean dark outline, a darker shade of the neighbouring colour rather than pure black. Soft light from the upper left.

Size: about ${c.h} art pixels tall from the top of the ${c.name === "Otto Grimbald" ? "helmet" : "hair"} to the soles, every sprite on the sheet at the same scale.

${c.name === "Otto Grimbald" ? "Face: none visible. The sallet visor is closed in every sprite; only the dark sight slit shows." : "Face: large eyes with a highlight, like the reference. NO mouth, NO lips, NO nose."}

Design: ${c.design}. Keep only details large enough to read at this size; few buckles; no emblems or logos.

Layout: a grid of 3 columns × 2 rows.
- Columns, left to right: facing down (front), facing left (side), facing up (back).
- Row 1: idle standing pose.
- Row 2: walking pose mid-stride (first frame of the walk), same directions.
- At least 60 image pixels of empty background between sprites.

Background: one flat solid ${c.key} filling the whole image. No gradient, floor, ground shadow, text, labels or panels.`;
}

const still = (c, subject, pose, extra = "") => `Pixel-art sprite of ${c.name} ${subject}, matching the attached sprite exactly: same design, colours, ${c.name === "Otto Grimbald" ? "closed helmet (no face shows), " : "face (NO mouth, NO nose), "}${extra}pixel size (8×8 image pixels per art pixel) and proportions. True pixel grid, no anti-aliasing, no mixels.
${pose} One sprite, centred, on a flat solid ${c.key} background, with no shadow, no effects${subject.includes("battle pose") ? ", no impact marks" : ""} and no text.`;

const shared = c => `Pixel-art sprite animation of ${c.name}, matching the attached sprite exactly: same design, colours, pixel size (8×8 image pixels per art pixel) and scale (about ${c.h} art pixels tall). True pixel grid, no blur, no anti-aliasing, no smoothing between frames.
Fixed camera: no zoom, no pan, no camera shake. The character animates in place, centred, and does not travel across the screen.
Background: one flat solid ${c.key} for the whole video. No floor, no shadow, no scenery, no text, no captions.
No visual effects of any kind: no glow, particles, magic circles, trails, slashes or impact flashes. Effects are added later in the game engine, so show only the character's body and props.
Keep the outfit exactly as in the attached sprite in every frame: ${c.lock}. ${c.name === "Otto Grimbald" ? "Keep the helmet visor closed in every frame; no face shows." : "Keep the face exactly as in the sprite: large eyes, NO mouth, NO nose."}
Steady rhythm with no stumbles, pauses or hesitations. Smooth frame-to-frame motion at 24 fps.`;

const walk = (c, dir) => `${shared(c)}
Starting exactly from the attached frame, ${c.name} walks in place ${dir} for the whole video. It is a steady, looping walk cycle: legs step, arms swing and hair and clothes move naturally, but the body stays centred and does not travel across the screen or turn. Every step has the same rhythm, with no stumbles. The last step leads cleanly back into the first.`;

const HIT = "recoiling from a blow from the left: upper body knocked back to the right, head turned aside, eyes squeezed shut, weapon arm thrown out of guard, feet still on the ground";

let out = `## 7. Ready to paste, per character\n\nEvery prompt below is complete: nothing to fill in. Work top to bottom for each character; each step's result is the next step's reference. "Clean" means the usual snap-and-clean pass from \`Gemini Sprite Prompts.md\`, which produces the start frames. Facing right is mirrored in the engine.\n\n`;
let n = 0;
for (const c of C) {
  out += `### ${c.name} (${c.adv ? "adventurer" : "HQ staff"}; key ${c.key.replace("pure ", "")}; about ${c.h} px)\n\n`;
  const design = c.adv ? `\`Character Sprites/Recruitable Staff/Adventurers/${c.folder}/Idle Front.png\` (design)` : null;
  out += `**1. Base sheet.** Attach: \`${refSheet(c)}\` (style and proportion)${design ? `, ${design}` : ""}.\n\n` + block(sheet(c)) + "\n"; n++;
  if (c.adv) {
    out += `**2. Sleeping.** Attach: the approved base sheet from step 1.\n\n` + block(still(c, "asleep", `Pose: ${c.sleep}. Seen from the same three-quarter game camera as the sheet. Eyes closed. No bed, pillow, blanket, floor, "Z" letters.`)) + "\n"; n++;
    out += `**3. Battle stance.** Attach: the approved base sheet from step 1.\n\n` + block(still(c, "in a battle stance facing left", c.stance)) + "\n"; n++;
    const poses = [["4. Getting Hit", HIT], ["5. Guard", `braced facing left, weight on the back foot, blocking with ${c.guard}`], ["6. Victory", `${c.victory}, relaxed and proud, still turned toward the left`], ["7. Defeat", `dropped to one knee, head down, one hand on the ground, ${c.defeat}`]];
    for (const [t, p] of poses) {
      out += `**${t}.** Attach: the approved battle stance from step 3. It must face screen LEFT (head, torso, feet and the protected side).\n\n` + block(still(c, "facing left in a battle pose", `Pose: ${p}.`, "weapon, ")) + "\n"; n++;
    }
  }
  const s = c.adv ? 8 : 2;
  const dirs = [["facing down, toward the camera", "front", "Start - Walk Down"], ["facing left, in side view", "side", "Start - Walk Left"], ["facing up, away from the camera", "back", "Start - Walk Up"]];
  dirs.forEach(([d, label, file], i) => {
    out += `**${s + i}. Walk ${label} (video, Omniflash, Start frame).** Start frame: \`${file}.png\` from the cleaned sheet.\n\n` + block(walk(c, d)) + "\n"; n++;
  });
  if (c.adv) {
    out += `**${s + 3}. Battle idle → attack → skill (video, 10 s, Omniflash, Start frame).** Start frame: the cleaned battle stance from step 3.\n\n` + block(`${shared(c)}
Starting exactly from the attached frame, the character faces left the whole time, holding ${c.weapon}. About 10 seconds:
1. Battle idle (0–3 s): ready stance with a small breathing bounce, looping.
2. Attack (3–6 s): a basic attack with ${c.weapon.replace(/^(a|an) /, "the ")}: step in toward the left, strike, recover to the stance.
3. Skill (6–10 s): ${c.skill}. Show only the body motion, with no effects. End back in the battle stance.`) + "\n"; n++;
  } else {
    out += `**${s + 3}. Work loop (video, 4 s, Omniflash, Start frame).** Start frame: \`Start - Facing Down.png\` (row 1, front) from the cleaned sheet.\n\n` + block(`${shared(c)}
Starting exactly from the attached frame, the character faces down (toward the camera) the whole time. About 4 seconds of ${c.work}, a small repeating motion that ends in the same pose it started in, so it loops. Mime the workstation: no table, anvil, board or bench appears; the station is placed in the game.`) + "\n"; n++;
  }
}
let doc = fs.readFileSync(DOC, "utf8");
const at = doc.indexOf("## 7. Ready to paste");
if (at >= 0) doc = doc.slice(0, at).trimEnd() + "\n\n";
else doc = doc.trimEnd() + "\n\n";
fs.writeFileSync(DOC, doc + out);
console.log("prompts:", n);
