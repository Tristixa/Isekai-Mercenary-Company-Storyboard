# Scene 6 - First Guild Meeting

## Synopsis
Location: Guild house (Tier 1) interior
Time: 07:00
Actors: Commander, Tristitia, Elsie, Mae
Staging: Tristitia at table_north facing south, seated; Commander at table_south facing north, seated; Elsie at table_east facing west, seated; Mae at table_west facing east, seated
Special poses: Tristitia sit, Commander sit, Elsie sit, Mae sit, Tristitia nod, Elsie nod, Mae nod

|Trigger: the start of the next day after the Guild reaches 400 Reputation. The day opens at 07:00 with all four seated at the meeting table in the main room. This is the first Guild meeting; it sets the Guild House Tier 2 objective (GDD 5.1, 12.7).|

|Unless directed otherwise, characters hold their current idle pose. Camera views continue across dialogue and choices.|

---

[control: lock]
[camera: shared]
[fade: in]
Tristitia (Happy):
"Let's start our first Guild meeting."
"I've written up all the reports from everyone."
"Who do you want to hear first, Commander?"

[choices: all]
Commander:

1. **[Elsie]**
   Commander (Happy):
   "I want to hear what Elsie has to say."

   Elsie (Serious):
   "Good, because I have plenty to say and I want everyone to hear all about it."
   "Our adventurers are well cared for, I've trained them well, and they have plenty of success in the field."

   Elsie (Serious):
   "But it's only a matter of time until they struggle with the monsters from other regions."
   Elsie (Sad):
   "I don't even want to think about what will happen to them when they encounter the Chimera."
   Elsie (Serious):
   "I've trained them and it helps, but they need gear!"

   Commander (Base):
   "Can you make them, Mae?"

   Mae (Sad):
   "No, that's outside my expertise."
   Mae (Laugh):
   "I'm good at breaking things apart, not making things."

   Commander (Base):
   "Okay, then we'll find someone who's good at smithing."

   Elsie (Happy):
   "Thank you, Commander. I'm glad you're not cutting corners."

2. **[Mae]**
   Commander (Happy):
   "I want to hear what Mae has to say."

   Mae (Sad):
   "This might surprise you, Commander."
   "But I can't keep up with all the processing work."
   "I even need to schedule my 'picking flowers' with this much processing work."

   Commander (Laugh):
   "Picking flowers? Do you like flowers, Mae?"

   [camera: push-in Mae]
   Mae (Surprise):
   "........."

   Commander (Base):
   "?"

   |Tristitia kicks the Commander under the table.|
   [camera: pan Tristitia]
   [camera: push-in Commander]
   [shake: medium]
   [emote: Commander exclaim]
   Commander (Fear):
   "!!!"
   "Ow, what was that, Tristitia?"

   [camera: return]
   Tristitia (Laugh):
   "Drop it."

   Elsie (Laugh):
   "You kind of deserved that, Commander."

   Commander (Surprise):
   "I was just asking about flowers."

   [camera: push-in Tristitia]
   [vignette: ominous]
   |No special pose: the vignette and her Laugh portrait carry the menace (Tristitia rarely shows an open face).|
   Tristitia (Laugh):
   "I. Said. Drop. It."

   [vignette: off]
   [camera: return]
   Commander (Fear):
   "Okay, please stop smiling like that."
   "You're scaring me."

   [shake: medium]
   Commander (Fear):
   "Ow! Okay, I'm sorry."

   Tristitia (Laugh):
   "You're welcome."

   Mae (Laugh):
   "Ahem, so continuing from before..."

   Mae (Happy):
   "I need a new pair of hands."

   Commander (Laugh):
   "Right, new processing staff."
   "We need more if we want to increase our production."

   Mae (Happy):
   "Thank you, Commander. That's all from me."

3. **[Tristitia]**
   Commander (Base):
   "What do you have in mind, Tristitia?"

   Tristitia (Base):
   "I'll make it simple."
   "We need a new source of income."

   Commander (Happy):
   "So the plan to sell our materials outside is now a go?"

   Tristitia (Happy):
   "Yes. For that we need two new officers."
   "One will be in charge of commerce, the other in charge of information."
   "I already have the people in mind."

   Mae (Surprise):
   "Valerie and Liliana?"

   [pose: Tristitia nod]
   Tristitia (Base):
   "They are the best candidates."
   [pose: Tristitia sit]
   "Valerie's skill in negotiation can surpass even a noble's."
   "And Liliana always has her finger on the pulse."
   "With those two together, we will always come out on top in the outside market."

   Mae (Serious):
   "That sounds good, but Valerie wouldn't give us the slightest bit of attention before."
   "Remember? She rejected us when we asked to partner up."

   Tristitia (Base):
   "That's in the past. Back then we were still small-time adventurers."
   Tristitia (Happy):
   "But now we have leverage, with how well things have been going."
   "I'm sure she's already aware of our Guild's rising reputation."
   "We could just wait, and sooner or later she would be the one to approach us."
   Tristitia (Base):
   "But I'd rather speed things up. I'll be the one to approach her."

   Elsie (Happy):
   "Just like you approached me?"

   Tristitia (Surprise):
   "I won't be using a sword this time."

   Elsie (Laugh):
   "That's too bad, I prefer the sword."
   "More interesting that way."

   Mae (Laugh):
   "That does sound interesting."
   "I'm curious what she looks like when she's scared."

   |The next choice is flavour only: Tristitia is playing along, and nothing changes later.|
   Commander:

   1. **[Approach with a sword]**
      Commander (Laugh):
      "I agree with Elsie."
      "Prepare your sword, Tristitia."

      Tristitia (Laugh):
      "Sword it is, then."

   2. **[Approach normally]**
      Commander (Fear):
      "You must all be joking? That's no good."

      Tristitia (Happy):
      "I'm glad the Commander is making sense."

   Tristitia (Base):
   "Regardless, I will bring those two into the fold."

   Commander (Base):
   "Okay, I'll leave that to you, Tristitia."
   "Tell me if you need help with them."

   Tristitia (Happy):
   "Understood. Thank you, Commander."

Tristitia (Base):
"That's all for the Guild meeting."
"You can go back to your posts."

[pose: Elsie nod]
[pose: Mae nod]
[pose: Elsie idle]
[pose: Mae idle]
[exit: Elsie courtyard_door]
[move: Mae processing_corner]
[pose: Mae idle]

Commander (Base):
"Do you still have something for me, Tristitia?"

Tristitia (Base):
"Yes. I've written the plan for our Guild going forward."
"Starting with what we've discussed."
"To bring in the new officers, we need to expand the Guild house."
"I've written it on your objective paper as usual."

Commander (Happy):
"Okay, I'll pin that as our immediate goal."

[pose: Tristitia nod]
[pose: Tristitia sit]

[camera: gameplay]
[control: unlock]

[objectives: C1S6-1]
- Upgrade the Guild House to Tier 2
[end objectives]

|Guild House Tier 2 (GDD 12.7: 1,000G + 6 Standard+ Boar Hides, 48 hours) adds, in one upgrade: a second officers' room (Fulker, Valerie and Liliana sleep there), the Workshop (Mae moves her processing there; Fulker and the processing and craftsman staff work there too) and one Commerce + Information room (in Eurydica they share a room; they separate in the Frontier, where the information department verifies reports). Interior design: Locations/Eurydica/Interiors/Guild House Interiors.md.|

|Tier 2 also unlocks the Dorm Expansion from 4 to 8 beds. All staff (recruitables: adventurers and workers) sleep in the dormitory; the expansion gives room for the starter processing, craftsman and information staff. The information staff member (Cassia Susurra) becomes available after Liliana joins (after objective C1S7-1).|
