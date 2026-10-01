# Scene 1 - Opening

## Synopsis
Location: Eurydica Outskirts
Time: Night
Actors: Commander, Tristitia
Music: outskirts_night
Staging: Commander at tree_rest facing south, lying down; Tristitia offstage
Special poses: Commander lie, Commander sit, Commander kneel, Commander salute, Commander salute_seated, Commander think_seated, Commander nod, Tristitia point

|Dialogue options are mostly flavour, so the player can own their character, as in Steambot Chronicles. The bracketed label is the intent shown to the player; the quoted line under it is spoken after it's chosen. The Commander's bag stays equipped all scene.|

---

## Awakening

[control: lock]
[camera: push-in Commander]
[pose: Commander lie]
Commander (Base):
". . . . ."

[shake: light]
[emote: Commander exclaim]
Commander (Surprise):
"!!!"

[pose: Commander idle]
Commander (Fear):
"Where am I?"

Commander (Serious):
"I was…"

1. **[In a library.]**
   "Reading a book in the library."

2. **[Returning home.]**
   "Walking down the road to home."

3. **[Playing a game.]**
   "Playing a game, then I fell asleep."

4. **[Dying.]**
   "On the floor… dying from overwork…"

Commander (Sad):
"And then I remember a bright light…"

Commander:
". . . . . . ."

Commander (Serious):
"I need to find someone—or at least somewhere safe to rest."

[enter: Tristitia tris_watch]
[face: Commander Tristitia]
[camera: two-shot Commander Tristitia]
[emote: Commander exclaim]
Commander (Surprise):
{I didn't realize someone was there. Is that a real sword?}

Tristitia (Serious):
"You're awake."

"Good. I have no intention of carrying you."

"You have the look of a rookie on a battlefield."

"lost, exhausted, and standing where they shouldn't have."

"Do you remember your name?"

[name-entry]
Commander:

1. **[Answer unsure]**
   Commander (Fear):
   "<name>… I think my name is <name>."

2. **[Answer friendly]**
   Commander (Happy):
   "I'm <name>. Nice to meet you."

3. **[Kneel and kiss her hand]**
   [pose: Commander kneel]
   Commander (Happy):
   "<name>."
   [pose: Commander idle]

4. **[Salute]**
   [pose: Commander salute]
   Commander (Serious):
   "<name>."
   [pose: Commander idle]

Tristitia (Base):
". . . . ."

"Tristitia."

[pose: Tristitia point]
Tristitia (Serious):
"Rest there. You are about to collapse."

[pose: Tristitia idle]
Commander (Base):
"Okay."

[pose: Commander sit]
[camera: shared]

## Waiting

Tristitia (Serious):
"The area is safe enough for now."

"Stay there, and watch yourself. The smaller monsters are more nuisance than threat, but they still bite."

[emote: Commander question]
Commander (Surprise):
{What did she mean by monster?}

1. **[Ask for assistance]**
   Commander (Base):
   "Can you help me? I'm lost."

2. **[Be demanding]**
   Commander (Anger):
   "You're leaving me here? I'm lost and exhausted. You should help me."

3. **[Be pensive]**
   Commander (Serious):
   {I should ask her for help.}
   "Can you help me? I'm lost."

Tristitia (Serious):
"I'm in the middle of a hunt."

"The sort that notices when it is being followed."

"Wait here until it is done."

Commander:

1. **[Nod]**
   [pose: Commander nod]
   Commander (Base):
   "I'll wait here."
   [pose: Commander sit]

2. **[Salute]**
   [pose: Commander salute_seated]
   Commander (Serious):
   "I'll wait here."
   [pose: Commander sit]

3. **[Say goodbye]**
   Commander (Happy):
   "I'll wait here. Goodbye Tristitia."

4. **[Thank her]**
   Commander (Happy):
   "I'll wait here. Thank you Tristitia."

Tristitia (Serious):
"Stay out of sight. I'll be back within the hour."

"If you hear anything, stay where you are. Curiosity is not a survival skill."

[exit: Tristitia woods_edge]
[camera: push-in Commander]
Commander (Base):
". . . . ."

{I think I still have food and water in my bag.}

[fade: out]

## One hour later

[fade: in]
[camera: shared]
[enter: Tristitia tris_watch]
Tristitia (Base):
"You stayed."

Commander (Base):
"You told me to."

Tristitia (Happy):
"Most people hear instructions as a challenge."

Commander (Serious):
"Where have you been?"

Tristitia (Serious):
"Finishing the hunt."

Commander (Surprise):
"At night?"

Tristitia (Serious):
"That is when the target feels safest."

"The talking kind. Two legs, a knife, and a habit of taking money from travelers."

[pose: Commander think_seated]
Commander (Serious):
"It's a..."

1. **[Bandit]**
   "Bandit?"

2. **[Goblin]**
   "Goblin?"

3. **[Dragon with a knife]**
   Commander (Surprise):
   "Dragon? with a knife."

[pose: Commander sit]
Tristitia (Base):
"Could be."

Commander (Base):
"Did you catch him?"

Tristitia (Serious):
"You ask a lot."

"Come. Eurydica is ten minutes away."

"Try not to collapse before we reach the gate."

[pose: Commander idle]
Commander (Base):
"I'll follow along."

[move: Tristitia road_gate]
[move: Commander road_gate]
[fade: out]

## Arrival in Eurydica

[location: Eurydica South Gate]
[fade: in]
[camera: pan main_street]
[move: Tristitia main_street]
[move: Commander main_street]
[fade: out]
[goto: Scene 2 - Tavern Talk]
