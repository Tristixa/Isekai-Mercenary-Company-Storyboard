# Scene 3 - Starting Up

## Synopsis
Location: Guild house (Tier 1) interior
Time: Morning
Actors: Tristitia, Elsie, Commander
Staging: Tristitia at table_north facing south, seated; Commander at table_south facing north, standing beside the opposite chair; Elsie at bench_east facing west in Guild house (Tier 1) courtyard, offstage until the courtyard transition
Special poses: Tristitia sit, Tristitia stand_from_chair, Commander sit, Commander look_down_seated, Commander stand_from_chair, Elsie look_down, Commander kneel_reach, Elsie withdraw_hand, Commander stand_from_kneel, Commander salute, Elsie salute

> One week after the discussion in the tavern.

|Unless directed otherwise, characters hold their current idle pose. Camera views continue across dialogue and choices.|

---

[control: lock]
[camera: shared]
[pose: Tristitia sit]
|Tristitia is seated, with an open ledger on the table. Commander stands beside the opposite chair.|

Tristitia (Base):
"Everything is ready."
"Sit. We should decide how the work will be divided."

Commander (Base):
"Okay."

[pose: Commander sit]
Tristitia (Serious):
"For the present, I will handle the requests and daily reports."
"Mae has taken charge of processing and storage."

Commander (Base):
"And I make the decisions."

Tristitia (Base):
"Yes. You did accept the title."

Tristitia (Serious):
"We have another concern."

[pose: Commander look_down_seated]
Commander (Serious):
"Money?"

[pose: Commander sit]
[face: Commander Tristitia]
Tristitia (Serious):
"Our lack of it, yes."
"We spent most of what we had on this building."
"I can find us requests, but no one is going to trust a new guild before it has a reputation."

Commander (Base):
"What about selling monster materials?"

Tristitia (Serious):
"We can do that at the market."
"But I suggest we wait. They know we need the coin, so they’ll offer as little as they can."

Commander (Serious):
"So requests first."

Tristitia (Serious):
"Requests first."
"Once we have enough material to sell regularly, we can find someone who understands the market better than either of us."

Commander (Base):
"Sounds reasonable."
"Then where do we find adventurers to take the requests?"

Tristitia (Base):
"I have already found the person who will answer that."

[emote: Commander question]
Commander (Surprise):
"You have?"

Tristitia (Base):
"Come outside."

[pose: Tristitia stand_from_chair]
[pose: Commander stand_from_chair]
[pose: Tristitia idle]
[pose: Commander idle]
[move: Tristitia courtyard_door]
[move: Commander courtyard_door]
[fade: out]
[location: Guild house (Tier 1) courtyard]
[camera: shared]
[pose: Elsie look_down]
[face: Elsie west]
[fade: in]
|A travel pack with a visibly damaged strap rests on the bench. Elsie stands looking down at it.|

[enter: Tristitia interior_door]
[move: Tristitia bench_south]
[enter: Commander interior_door]
[move: Commander bench_west]
[face: Tristitia Elsie]
[face: Commander Elsie]
Elsie (Serious):
"This will split before it reaches the city gate."

Tristitia (Base):
"Then it is fortunate we found someone who notices such things."

[face: Elsie Commander]
[pose: Elsie idle]
Elsie (Happy):
"So this is the Commander."

Tristitia (Base):
"<name>, this is Elsie."
"She will hold the position of Chief of Adventurers."

Elsie (Laugh):
"Considering."
"She left that part out."

Commander (Base):

1. **[Be friendly]**
   Commander (Happy):
   "I’m <name>. Nice to meet you."
   Elsie (Laugh):
   "Elsie. Good to meet you, Commander."

2. **[Be polite]**
   Commander (Base):
   "My name is <name>. Pleasure to meet you."
   Elsie (Happy):
   "Elsie. Good to meet you, Commander."

3. **[Kneel and kiss her hand]**
   [move: Commander elsie_side]
   [pose: Commander kneel_reach]
   Commander (Happy):
   "I’m <name>."
   [pose: Elsie withdraw_hand]
   Elsie (Laugh):
   "You can stand."
   "I’m not anyone you need to bow to."
   [pose: Commander stand_from_kneel]
   [pose: Commander idle]
   [pose: Elsie idle]
   [move: Commander bench_west]
   [face: Commander Elsie]

4. **[Salute]**
   [pose: Commander salute]
   Commander (Serious):
   "<name>."
   [pose: Elsie salute]
   [pose: Elsie idle]
   [pose: Commander idle]
   Elsie (Base):
   "...Old habit."

Elsie (Base):
"Tristitia told me what you’re trying to build."
"Steady work, supplies, and somewhere for adventurers to come back to."

Commander (Happy):
"That’s the plan."

Elsie (Happy):
"It’s a good one."

Elsie (Serious):
"But you’ll be accepting the work while someone else has to walk out that gate and do it."

Commander (Base):
"Of course."

[camera: two-shot Elsie Commander]
|Keep Tristitia at the edge of the closer framing.|
Elsie (Serious):
"Then let me ask you something."
"Say we accept a request and the adventurer refuses it. What do you do?"

[camera: push-in Commander]
Commander (Serious):

1. **[Respect their choice]**
   [camera: two-shot Elsie Commander]
   Commander (Serious):
   "Then we offer it to someone else. It’s their life."
   Elsie (Happy):
   "Good."
   Elsie (Serious):
   "A contract is work, not a chain."

2. **[Ask why]**
   [camera: two-shot Elsie Commander]
   Commander (Serious):
   "I’d ask why. They might know something we don’t."
   Elsie (Laugh):
   "Exactly."
   Elsie (Happy):
   "People on the road may notice something we missed from behind a desk."

3. **[Be firm]**
   [camera: two-shot Elsie Commander]
   Commander (Serious):
   "If they already accepted it, they owe us an explanation."
   Elsie (Base):
   "Fair."
   "They may refuse the work, but they don’t get to waste everyone else’s time."

4. **[Ask her]**
   [camera: two-shot Elsie Commander]
   Commander (Base):
   "I don’t know yet. What would you do?"
   Elsie (Happy):
   "I’d ask why."
   "Then I’d decide whether they need better preparation, or we need a better request."

Elsie (Happy):
"All right."
"I can work with you."

[camera: return]
Tristitia (Surprise):
"That was a shorter interview than mine."
Tristitia (Base):
"Then I assume the position is settled."

Elsie (Happy):
"It is."

[face: Elsie Commander]
Elsie (Happy):
"I’ll handle training, preparation, and the expeditions."

Elsie (Happy):
"If someone isn’t ready to leave, I’ll tell you."

Commander (Base):
"And the decision is still mine?"

Elsie (Laugh):
"It is."
"I’m only asking you to listen before you make it."

Commander (Happy):
"I can do that."
"I’m counting on you, Elsie."

Elsie (Laugh):
"Then we understand each other."

Tristitia (Base):
"We should finish the tour."

Elsie (Base):
"Go ahead. I want to check the rest of this equipment."

Commander (Surprise):
"Is it all that bad?"

Elsie (Laugh):
"No. Some of it might survive until lunch."

Tristitia (Base):
"Make a list."

Elsie (Happy):
"Already on it."

[face: Elsie west]
[move: Tristitia interior_door]
[move: Commander interior_door]
[fade: out]
[location: Guild house (Tier 1) interior]
[enter: Tristitia courtyard_door]
[move: Tristitia office_door_west]
[enter: Commander courtyard_door]
[move: Commander office_door_east]
[face: Tristitia Commander]
[face: Commander Tristitia]
[camera: shared]
[fade: in]
|Frame the open doorway and the small furnished room beyond it. Both doorway markers leave the passage clear.|

Tristitia (Base):
"This room is yours."
"It will also serve as your office."

Commander (Base):
"What about everyone else?"

Tristitia (Base):
"The dormitory can hold two adventurers."
"Those beds remain theirs."

Commander (Base):
"How about you, Mae, and Elsie?"

Tristitia (Base):
"The three of us share the room across the hall."
"When more people join, we'll need another."

[face: Commander south]
[camera: push-in Commander]
[letterbox: on]
[camera: pan unfinished_west]
[camera: turn 20]
[camera: hold 1.0]
[camera: pan unfinished_east]
[camera: hold 1.0]
|Slowly reveal the unfinished interior, keeping Commander in frame throughout the pan.|
[letterbox: off]
[camera: return]
[face: Commander Tristitia]
Commander (Base):
"What do I do first?"

Tristitia (Base):
"Learn the city."
"Start with the market and the gate."
"Find out where people gather and share informations."

Commander (Base):
"So I walk around and talk to people."

Tristitia (Serious):
"Talk to them, yes."
"But look around before you begin asking questions. You will learn more that way."

Commander (HappY):
"All right. I can do that."

Tristitia (Happy):
"Be back by two."
"I should have our first request by then, and someone interested in joining."

Commander (Base):

1. **[Be friendly]**
   Commander (Happy):
   "All right. I’ll see you at two."

2. **[Thank her]**
   Commander (Happy):
   "Understood. Thank you, Tristitia."

3. **[Say goodbye]**
   Commander (Happy):
   "Two o’clock. See you later."

Tristitia (Base):
"While you're out, think of a name for the Guild."
"We've postponed it long enough."

[camera: gameplay]
[control: unlock]
|Commander remains clear of Tristitia and the doorway. Commander can explore the base and Eurydica.|

[objectives: C1S3-1]
- Explore Eurydica's districts (0/4)
- Return to the Guild house at 14:00
[end objectives]

|The objectives are optional: the Commander can visit only some districts and come back late. The four districts open on Day 1 are the plan's phase-1 districts: Guild Edge, Arrival Ward, Market Spine and Service Lanes (the South Gate belongs to Arrival Ward). Entering the Guild house at 14:00 or later plays Scene 5. When the player returns to Tristitia, all four starting adventurers can be recruited, and Tristitia also has two new requests, plus any request the player picked up from townspeople in the city.|

## Event: Late return
Trigger: time 16:00
[if: not seen: Scene 5 - Operation Begin]
[control: lock]
Commander (Base):
{I should return to base.}
{.....}
{I hope she won't get mad I'm late.}
[fade: out]
[location: Guild house (Tier 1) interior]
[goto: Scene 5 - Operation Begin]
[end if]
