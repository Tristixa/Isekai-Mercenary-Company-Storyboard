# Scene 7 - Full Operation Part 1

## Synopsis
Location: Guild house (Tier 2) interior
Time: 07:00
Actors: Commander, Tristitia, Elsie, Mae, Fulker
Staging: Tristitia at reception facing west; Commander at reception_west facing west; Fulker offstage; Elsie and Mae offstage until the Workshop
Special poses: Fulker craft, Fulker nod

|Trigger: the start of the next day after objective C1S6-1 (Guild House Tier 2) is completed. Fulker answers the Guild's recruitment poster and becomes Chief of Craftsmen.|

|Unless directed otherwise, characters hold their current idle pose. Camera views continue across dialogue and choices.|

---

[control: lock]
[camera: shared]
[fade: in]
[enter: Fulker courtyard_door]
[move: Fulker hall_centre]
|Fulker looks around the hall before she speaks.|
[face: Fulker west]
[pause: 0.6]
[face: Fulker east]
[pause: 0.6]
[face: Fulker Tristitia]
Fulker (Base):
"Is this <Guild-name>? I saw your poster outside."
"I'm here to apply."

Tristitia (Base):
"Have you read the requirements?"

Fulker (Fear):
"Um... yeah."

Fulker (Laugh):
"You're looking for someone to make gear, right?"
"I've lived and breathed the smithy since I was little."
"And your poster just pulled me in. I feel like I can take my skills further here."

Commander (Laugh):
"Great! So you want to be the Chief of Craftsmen?"

[emote: Fulker exclaim]
Fulker (Surprise):
"Huh!? I'm gonna be the chief?"

|Tristitia and the Commander look at each other without a word, then back at Fulker.|
[face: Commander Tristitia]
[face: Tristitia Commander]
[pause: 1.0]
[face: Commander Fulker]
[face: Tristitia Fulker]
Commander (Laugh):
"Well... at least she seems enthusiastic about it."

Tristitia (Base):
"Enthusiasm isn't skill. We should test her first."

Commander (Laugh):
"Sounds good. Let's move to the workshop."

Fulker (Laugh):
"Okay."

[fade: out]
[location: Guild annex (Tier 2) Workshop]
[time: 08:30]
[enter: Fulker annex_door]
[move: Fulker fulker_station]
[face: Fulker south]
[enter: Commander annex_door]
[move: Commander workshop_watch_w1]
[enter: Tristitia annex_door]
[move: Tristitia workshop_watch_w2]
[enter: Elsie annex_door]
[move: Elsie workshop_watch_e1]
[enter: Mae annex_door]
[move: Mae workshop_watch_e2]
[camera: shared]
[fade: in]
|Everyone watches Fulker work. Play her crafting loop twice (the same work animation she uses at her table in the sim, facing south).|
[pose: Fulker craft]
[sfx: smithing_hammer]
[pause: 2.4]
[pose: Fulker idle]
Fulker (Happy):
"Here you go."

Commander (Surprise):
"That was fast!"

Tristitia (Base):
"How's the quality, Els?"

Elsie (Laugh):
"I do declare, that's pretty solid gear!"

Mae (Happy):
"She's a natural."
"Took me years to get hands that steady."

Fulker (Laugh):
"Thanks."

Commander (Laugh):
"She's definitely the right person for the position."
"What do you think, Tristitia?"

Tristitia (Base):
"She will do."
"I'll train her to be a good officer."

Fulker (Surprise):
"Can someone else train me?"

[camera: push-in Tristitia]
Tristitia (Laugh):
"NO."

[camera: return]
[emote: Fulker sweat]
[pause: 0.8]
|Fulker nods, resigned to her fate.|
[pose: Fulker nod]
[pose: Fulker idle]

[fade: out]
|Everyone goes back to their stations, Fulker included, and the Commander is returned to the main hall.|
[location: Guild house (Tier 2) interior]
[camera: gameplay]
[fade: in]
[control: unlock]

[objectives: C1S7-1]
- Build the Dorm Expansion
- Talk to Fulker
[end objectives]

[objectives: C1S7-2]
Requires: C1S7-1
- Recruit a processor
- Recruit a craftsman
[end objectives]

## Event: Fulker explains crafting
Trigger: talk: Fulker
|To write: Fulker explains how crafting works (the Workshop work order, GDD 12.8). Hearing it completes the "Talk to Fulker" objective.|

|C1S7-2 appears as soon as C1S7-1 is completed. Scene 8 starts at 07:00 on the next day after C1S7-2 is completed.|
