# Scene 8 - Full Operation Part 2

## Synopsis
Location: Guild house (Tier 2) interior
Time: 07:00
Actors: Commander, Tristitia, Elsie, Mae, Fulker, Valerie, Liliana
Staging: Commander at wait_1 facing south; Elsie at wait_2 facing south; Mae at wait_3 facing south; Fulker at wait_4 facing south; Tristitia, Valerie and Liliana offstage

|Trigger: the start of the next day after objective C1S7-2 is completed (Fulker has joined and the processor and craftsman are recruited). All the officers are gathered in the hall when Tristitia brings in Valerie and Liliana.|

|Unless directed otherwise, characters hold their current idle pose. Camera views continue across dialogue and choices.|

---

[control: lock]
[camera: shared]
[fade: in]
[enter: Tristitia courtyard_door]
[move: Tristitia arrival_1]
[enter: Valerie courtyard_door]
[move: Valerie arrival_2]
[enter: Liliana courtyard_door]
[move: Liliana arrival_3]
|Valerie and Liliana look around the hall.|
[face: Valerie west]
[face: Liliana north]
[pause: 0.6]
[face: Valerie north]
[face: Liliana west]
[pause: 0.6]
[face: Valerie east]
[face: Liliana east]
Valerie (Happy):
"What a pleasant space. You didn't mention it was so welcoming."

[face: Tristitia Valerie]
Tristitia (Surprise):
"That's hardly worth mentioning."

Valerie (Laugh):
"On the contrary. A client who's comfortable stays longer, and a client who stays longer agrees to more."

Liliana (Base):
"I agree with her. Clearly you're not the designer."

Liliana (Flustered):
"Not that you couldn't come up with an innovative idea like this."
"What I mean is, if you can't appreciate it, then..."

Liliana (Fear):
"I'll just... stop talking."

Valerie (Happy):
"*chuckles* So who's the designer?"

Tristitia (Base):
"That would be the Commander."

|The officers, who have been watching, walk over to the three.|
[move: Commander greet_1]
[move: Elsie greet_2]
[move: Mae greet_3]
[move: Fulker greet_4]
[face: Tristitia Commander]
Commander (Base):
"Who are they, Tristitia?"

[face: Tristitia Valerie]
Tristitia (Base):
"This is Valerie. She will be in charge of commerce."

[face: Valerie Commander]
Commander (Happy):
"I'm <name>. Pleasure to meet you."

Valerie (Happy):
"A pleasure to meet you, Commander."
"A commander who designs his own guild house. I'd like to know what else you've thought of."

Valerie (Wink):
"Let's chat more in private sometime."

Commander (Laugh):
"Sure, I'd love to."

[face: Tristitia Liliana]
Tristitia (Base):
"Meet Liliana. She will be our Chief of Information."

[face: Liliana Commander]
Commander (Happy):
"Nice to meet you, Liliana."

Liliana (Happy):
"Nice to meet you, Commander."

Liliana (Base):
"The request board is by the door, so clients never have to cross the hall."
"And the workshop is in its own building, so the smell stays out."

Liliana (Flustered):
"Sorry. I notice how places are laid out. It's... a habit."

Commander (Happy):
"Thanks. It's based on what I know from Eart—"

Commander (Fear):
"I mean, my hometown."

Liliana (Happy):
"Really? I want to hear about your hometown."
"Let's talk more about it later."

Commander (Base):
"Okay. I'll tell everyone about it someday."

[face: Tristitia Valerie]
Tristitia (Base):
"Now that you've met the Commander,"
"we can begin the tour, starting with your workstations."
"Follow me."

[exit: Tristitia courtyard_door]
[exit: Valerie courtyard_door]
[exit: Liliana courtyard_door]
[pause: 0.6]
[face: Fulker Commander]
[face: Commander Fulker]
Fulker (Base):
"I'll take my leave."

Fulker (Laugh):
"You should visit the workshop more often, Commander."
"I want to make more gear with you."
"That thing you said about lighter armour is still stuck in my head."

Commander (Laugh):
"Okay. I'll see you later, Fulker."

[exit: Fulker courtyard_door]
[face: Commander Mae]
[face: Mae Commander]
[face: Elsie Commander]
Mae (Happy):
"Watch yourself around Valerie, Commander."
"She's quite dangerous."
"She loves to lay traps. It's one of her negotiation techniques."

Elsie (Surprise):
"I didn't sense any danger from her. Maybe because I'm not a man."

Commander (Surprise):
"Yeah, I didn't sense any danger either. Is she really dangerous?"

Commander (Base):
"She seems like a nice lady to me."

[camera: push-in Mae]
Mae (Surprise):
". . . . ."

[camera: return]
Elsie (Laugh):
"Hahaha."
"That's so you, Commander."
"Don't mind Mae. I think you should just go and get along with everyone."

Mae (Laugh):
"I'm sorry, Commander. Elsie is right."
"You should just be your usual self with her."
"That suits you more."

[camera: gameplay]
[control: unlock]

[objectives: C1S8-1]
- Talk to Valerie
- Talk to Liliana
[end objectives]

[objectives: C1S8-2]
Requires: C1S8-1
- Recruit an information staff member
- Make a sale at the Trading Post
[end objectives]

## Event: Valerie explains commerce
Trigger: talk: Valerie
|To write: Valerie explains how the Commerce department works (the Trading Post). Hearing it completes "Talk to Valerie".|

## Event: Liliana explains information
Trigger: talk: Liliana
|To write: Liliana explains how the Information department works. Hearing it completes "Talk to Liliana". The information staff member (Cassia Susurra) becomes recruitable after this scene.|
