# Scene Script Format (HD-2D)

Written 2026-09-28. This is the format for rewriting the manuscript for the HD-2D game. It stays close to how the manuscript is already written (speaker lines, `|…|` stage notes, numbered `**[Tone]**` choices), so writing still feels like writing. It adds a **small fixed vocabulary** the engine can read directly: a portrait expression for each line and a handful of stage cues. A converter turns each scene file into game data, so the rules below are strict wherever they say *exact*.

The staging follows GDD 2.6 (approved):
- Everyday talk stays in the diorama at the straight-north heading; the camera eases in, and the sprites turn and emote.
- Portraits carry the faces.
- Letterboxing and bigger camera moves are only for key beats.

## 1. The scene header

```markdown
# Scene 2 - Tavern Talk

## Synopsis
Location: Eurydica Tavern        ← an existing location ID or name
Time: Night                      ← Morning / Day / Evening / Night (lighting and NPC schedule)
Actors: Commander, Tristitia, Mae
Music: tavern_evening            ← optional; the track keeps playing until changed
Staging: Commander at table_west facing east; Tristitia at table_north facing south; Mae at table_east facing west
Special poses: Mae sit, Tristitia sit, Commander sit, Commander kneel   ← sprite poses beyond idle/walk (see 5)

|Mae has been waiting for Tristitia at the tavern. Three mugs are on the table.|
```

- **Staging** names **markers**: positions placed in the location scene (`table_west`, `door`, `counter`…) and the **facing** of each actor: north/south/east/west, the four sprite directions.
- **Special poses** lists every sprite pose the scene needs that isn't idle or walk. It doubles as the **asset list** for sprite production. If a pose isn't made yet, the engine falls back to idle.
- **Free notes** in `|…|` stay allowed anywhere. The converter keeps them as writer notes, and the engine ignores them.

## 2. Dialogue lines

```markdown
Mae (Laugh):
"Mm-hmm, That is usually how people begin."
```

- **Exact:** `Speaker (Expression):` on its own line, then the line of dialogue in quotes on the next line.
- **Speaker:** a character name, or `Commander`. The old `Player` still works and means the Commander.
- **Expression:** one of that character's portrait expressions.
  - Officers and the Commander: **Base, Happy, Serious, Sad, Anger, Fear, Surprise, Laugh**. Base is neutral.
  - Buyers: the 8 negotiation expressions (`Characters/Negotiation Buyers Roster.md`).
  - Leave it out, as in `Mae:`, and the portrait **keeps its last expression**, which starts at Base.
  - **Extra expressions** *(added 2026-10-02)*: a character may also use the extra expressions listed for them in `Research/Portrait Expressions.md` (for example Liliana (Flustered), Valerie (Wink)). Until an extra expression is drawn, the line shows the fallback that file names for it.
- **Inner monologue:** a line in `{braces}` instead of quotes is the speaker's thought. It shows in italics in parentheses, with no talk sound, and can sit between spoken lines under the same speaker. This is the manuscript's existing convention, and in Chapter 1 only the Commander thinks aloud.
- **Placeholders:** `<name>` (the Commander's name) and `<Guild-name>` stay as they are; the game fills them in.
- **Several lines by the same speaker:** each quoted line is one text box. A quoted or `{thought}` line with no speaker line directly above it **continues the previous speaker**, and blank lines between them are fine. Repeat the speaker line only to change the expression.

### Narration (no speaker)

```markdown
> You explain what you know about adventurer guilds.
```

- **Exact:** a line starting with `> ` is **narration**. It has **no speaker name** and no portrait, and shows in a separate narration box. It may address the player as "you".
- **Narration isn't thought.** The Commander's inner monologue is `{braces}` under his name. Narration describes what happens and belongs to no one.
- Several `> ` lines in a row show one after another.

**Characters without a portrait set** (for now every Eurydica NPC: Jeb, Hilde, Gerd, Dr. Emmerich and the townspeople; owner, 2026-09-28) show their **name only, with no face**. Expression tags in their lines are kept for later but ignored until portraits exist. The one exception is the Travelling Merchant, whose negotiation expressions are needed for Valerie's Counter-offer session (`Production Assets Requirement/Buyer Portrait Prompts.md`).

**Who is shown:** the Commander's portrait sits on the left; the current other speaker is on the right. With three people, the right portrait follows whoever speaks.

## 3. Stage cues

A cue sits on **its own line in square brackets**, before the dialogue line it belongs to. Several cues in a row play together.

### Camera (GDD 2.6)

| Cue | What it does |
|---|---|
| `[camera: shared]` | Default framing of all actors in the scene (the diorama push-in). Every scene starts here. |
| `[camera: push-in Tristitia]` | Eases in closer to one actor, who stays readable at centre |
| `[camera: two-shot Tristitia Mae]` | Frames two actors |
| `[camera: pan door]` | Slowly pans to a marker or actor, and stays there |
| `[camera: gaze Commander]` | Briefly pans to what that actor is looking at (for a look-behind or a glance at something), then holds there |
| `[camera: hold 0.6]` | Holds the current shot for 0.6 seconds before the next line |
| `[camera: return]` | Eases back to `shared` |
| `[camera: turn 20]` | **Key beats only.** Turns the heading up to ±30° (negative turns left) |
| `[letterbox: on]` / `[letterbox: off]` | **Key beats only.** Cinematic bars |

### Control and system

| Cue | What it does |
|---|---|
| `[control: lock]` / `[control: unlock]` | Scenes start locked; unlock hands control back to the player |
| `[camera: gameplay]` | Returns to the normal exploration camera |
| `[location: Eurydica South Gate]` | Switches the scene to another location (use it between a `[fade: out]` and a `[fade: in]`); its markers become available |
| `[name-entry]` | Opens the Commander's name screen; `<name>` is valid after it |
| `[request: CH1-REQ-001]` | Unlocks a request unconditionally and shows the game's own "request available" notice (use `{request: …}` on a choice for offer branches) |
| `[guild-name-entry]` | Opens the Guild naming screen; `<Guild-name>` is valid after it |
| `[time: 08:30]` | Sets the Guild clock (use it inside a fade for a time skip within a scene; added for Scene 7) |

### Effects and sound

| Cue | What it does |
|---|---|
| `[shake: light]` / `medium` / `heavy` | A brief, decaying screen shake |
| `[fade: out]` / `[fade: in]` | Fade to black and back (time skips, scene cuts) |
| `[pause: 1.0]` | Wait with no text box |
| `[sfx: door_open]` | Play a sound effect |
| `[music: tavern_evening]` / `[music: stop]` | Change or stop the music |
| `[vignette: ominous]` / `[vignette: off]` | A dark screen vignette for a menacing beat (added for Scene 6); `off` eases it away |

### Sprites (acting in the diorama)

| Cue | What it does |
|---|---|
| `[face: Mae Commander]` | Mae turns to face the Commander (or a direction: `north`, `east`…; or `back` to turn and look behind) |
| `[move: Commander table_west]` | Walks to a marker, then continues |
| `[pose: Mae sit]` | Switches to a special pose listed in the header; `[pose: Mae idle]` returns to idle. A pose can also be a character's looping work animation from the sim (`craft`, `process`), which plays until the next pose cue |
| `[emote: Mae laugh]` | A small icon over the sprite (list in 5) |
| `[enter: Liliana door]` / `[exit: Liliana door]` | An actor walks in from, or out to, a marker |

## 4. Choices, conditions and story flags

The manuscript's numbered choices stay the same, with optional tags added after the label:

```markdown
Commander:

1. **[Be friendly]** {Leadership}
   "I'm <name>. Nice to meet you."
   Mae (Happy):
   "How polite."

2. **[Be shy]**
   "<name>."

3. **[Kneel and kiss her hand]** {bond: Mae +1}
   [pose: Commander kneel]
   "I'm <name>."
   [pose: Commander idle]
```

- **Exact:** `N. **[Label]**`. The Commander's words go under it, and any replies are indented beneath. Choices can nest.
- **Tags in `{…}` after the label:**
  - `{Leadership}`, `{Negotiation}`, `{Insight}` or `{Know-how}`: a Commander-skill choice (+2 points, GDD 5a.2);
  - `{bond: Mae +1}`: officer bond points;
  - `{set: met_mae}`: set a story flag;
  - `{request: CH1-REQ-003}`: this choice unlocks that request (the offer branch).
- **Conditions:** `[if: met_mae]` … `[else]` … `[end if]` around lines or choices. Use them for "later visit" lines and for different follow-ups. Conditions can test:
  - a story flag (`[if: met_mae]`);
  - a request's state (`[if: done: CH1-REQ-005]`);
  - a named game state (`[if: corpses_waiting]`), where the name must be one the game defines. The converter lists unknown names.
- **Must-pick-all menus:** `[choices: all]` on the line before `Commander:` makes the menu return after each option until every option has been picked; picked options are greyed. The dialogue continues after the last one (added for Scene 6's Guild meeting).
- **Long branches:** when an option's reply is long, keep it nested under the option, however long it gets. The dialogue rejoins automatically after the last option, so no "rejoins here" heading is needed.
- **Endings:** `[end]` finishes the scene early; otherwise it ends at the last line. `[goto: Scene 3 - Day 1]` chains straight into the next scene.

## 4a. Talks, barks and ambient lines

Not every script is a linear scene. Gameplay conversations (officers, request-givers, townspeople) use these section types inside a scene file.

### Talks: repeatable conversations with a topic menu

```markdown
## Talk: Mae
Where: Processing corner

[if: corpses_waiting]
Mae (Happy):
"Ah, <name>. We still have something left from the last hunt, if you want me to process it."
[else]
Mae (Base):
"Ah, <name>. How are things?"
[end if]

Commander:

1. **[Ask about her]** {topic}
   Commander (Base):
   "How long have you been doing this?"
   …

2. **[Ask about The Frontier]** {topic} {after: Ask about her}
   …
```

- **`{topic}`:** after the reply, the conversation returns to the same menu. A **[Leave]** option is added automatically.
- **`{after: Label}`:** hides the option until that topic has been heard. Heard topics stay available, marked as read.
- **Default staging:** the two face each other in a `shared` view, so a talk needs no staging cues unless something special happens.
- **Talks don't lock control** for longer than the conversation itself, and they use the day's clock pause (GDD 4).

### Barks: lines spoken near the player

```markdown
## Bark: Travelling Merchant
Trigger: nearby
"Hmmm there's not much rare slime parts in the market..."
"Must be because of the chimera."
```

- Barks show as small speech bubbles over the sprite, with no portrait and no control lock.
- `Trigger: nearby` fires when the Commander walks close. They play once per day.

### Ambient lines: one-off townspeople

```markdown
## Ambient: Lady in a Red Dress
Where: Market Spine
When: Night
Lady in a Red Dress:
"Have you met the woman in green? …"
```

- `When:` (Morning / Day / Evening / Night) limits when the townsperson appears. Leave it out for any time.
- A `[if: done: …]` block replaces the line after a request is completed.
- Ambient townspeople have **no portrait expressions**; their lines show with the name only.

## 4b. Objectives, screens and events *(added 2026-09-30 for Scenes 3 and 5)*

### Objective groups

```markdown
[objectives: C1S5-1]
- Recruit adventurers (0/2)
- Accept a request that asks for slime parts
[end objectives]

[objectives: C1S5-2]
Requires: C1S5-1
- Talk to Elsie about preparation
[end objectives]
```

- **The ID** is `C<chapter>S<scene>-<n>`, unique in the game.
- **Each `-` line** is one objective shown in the HUD's objective scroll (FGC_08 §5.1). A counter such as `(0/2)` updates itself. The game defines how each line completes, and the converter lists every line so it can be matched to a game check.
- **`Requires: ID`** hides the group until that group is completed. Without it, the group appears at once.
- **A completed group is removed** and the next one appears.
- **`[complete: ID]`** completes a group from inside a scene (for example, after a talk).

### Screens

- `[menu: recruitment]` opens a game screen from a script. The name must be one from the screen inventory (`FGC_08 UI screens/screen-inventory.md`). The script continues when the screen closes.

### Events: scripts that start themselves

```markdown
## Event: Late return
Trigger: time 16:00
[if: not seen: Scene 5 - Operation Begin]
…
[end if]
```

- `Trigger:` takes one of:
  - `time HH:MM`: the Guild clock reaches that time;
  - `enter: <location>`: the Commander enters a location;
  - `talk: <character>`: the player talks to that character;
  - `reputation <n>`: the Guild reaches that Reputation.
- An event plays **once**. Its `[if: …]` guard decides whether it applies when triggered.
- **New conditions:**
  - `[if: not seen: <scene>]`;
  - `[if: done: C1S5-1]` for an objective group.

  `done:` already tests requests.

## 5. Emote icons

Small icons over a sprite's head, since sprites have no mouths:

`exclaim` (!), `question` (?), `dots` (…), `sweat`, `anger` (vein), `laugh`, `heart`, `music`, `sleep` (zzz), `idea` (bulb), `sigh`.

This set is an asset to draw once and share across the whole cast.

## 6. Writing from the old 3D staging

The existing manuscript has 3D-era directions: seated cameras, close-ups, over-the-shoulder shots and orbits. Translate them like this:

| Old 3D direction | HD-2D version |
|---|---|
| Close-up, reaction shot, over-the-shoulder | `[camera: push-in X]`, plus the portrait expression doing the acting |
| Two-shot | `[camera: two-shot A B]` |
| Establishing wide shot, reveal | `[camera: pan place]` or `[fade: in]` onto `[camera: shared]` |
| Orbit or big camera move | **Key beats only:** `[letterbox: on]` + `[camera: turn 20]` + `[camera: pan …]`. Otherwise drop it. |
| Body acting (shrugs, hand gestures, facial detail) | Portrait expression + `[emote: …]`. Put a special pose in the header only when the pose itself matters (sitting, kneeling, handing over an object). |

**Rule of thumb:** a normal conversation should need at most one or two cues. Let the portraits act.

## 7. Example: the "Mae!" moment (Scene 2)

The current manuscript:

```markdown
|Camera: Cut closer to Tristitia, keeping Mae at the edge of the frame. Add one brief, slight camera shake as Tristitia speaks.|

Tristitia:
"Mae!"

|Briefly hold on Tristitia, then return to the shared table view. Mae remains in her relaxed seated pose.|

Mae:
"So, who is he?"
```

In the new format:

```markdown
[camera: two-shot Tristitia Mae]
[shake: light]
Tristitia (Anger):
"Mae!"

[camera: hold 0.6]
[camera: return]
Mae (Happy):
"So, who is he?"
```

A two-shot keeps Mae at the edge of the frame. Tristitia's Anger portrait carries the outburst, the light shake punctuates it, and the camera returns to the shared table view.

## 8. File layout

- **Scene files stay in `Manuscript/<Chapter>/`**, one Markdown file per scene. When you rewrite a scene, replace its content in place. The old 3D version is kept in git history.
- **Location markers** used in `Staging:` and cues are listed in `Locations/Eurydica/markers.md`, one section per location. If a marker is missing, the converter reports it instead of guessing.
- **The converter** checks every scene against this format and reports:
  - unknown expressions, cues, markers, poses and tags;
  - missing quotes.

  The converter itself isn't built yet; it arrives with the Godot build.
