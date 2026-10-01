# Scene 5 - Operation Begin

## Synopsis
Location: Guild house (Tier 1) interior
Time: Day
Actors: Commander, Tristitia, Elsie
Staging: Tristitia at table_north facing south, standing; Elsie at bench_east facing west in Guild house (Tier 1) courtyard, offstage until the player talks to her
Special poses: Tristitia nod

|Trigger: the Commander enters the Guild house at 14:00 or later on Day 1 (or is brought back by Scene 3's "Late return" event at 16:00). He walks up to Tristitia automatically and the scene plays. This is the GDD 14 recruitment beat (milestone M02): it opens hiring of the four starting adventurers and the first two requests. Once an objective group is completed it is removed and replaced by the next group.|

---

[control: lock]
[move: Commander table_south]
[face: Commander Tristitia]
[camera: shared]
Tristitia (Happy):
"Good, you're back."

Tristitia (Serious):
"Have you decided on the Guild name?"

Commander (Happy):
"I have. The name will be..."
[guild-name-entry]

[pose: Tristitia nod]
Tristitia (Base):
"The Guild will be called <Guild-name> from now on."
[pose: Tristitia idle]
"Here's the list of adventurers and requests."
"They are ready for your decision."

[request: CH1-REQ-001]
[request: CH1-REQ-002]
[menu: recruitment]
|The recruitment screen shows adventurers only; no staff departments are open yet.|

[camera: gameplay]
[control: unlock]

[objectives: C1S5-1]
- Recruit adventurers (0/2)
- Accept a request that asks for slime parts
[end objectives]

[objectives: C1S5-2]
Requires: C1S5-1
- Talk to Elsie about preparation
[end objectives]

## Event: Elsie's preparation
Trigger: talk: Elsie
[if: done: C1S5-1]
Commander (Base):
"Is everyone ready to depart?"

Elsie (Happy):
"Yes, I've checked them, and they're all fit for departure."
"They are waiting for your instruction."

Elsie (Happy):
"I suggest we send someone to hunt and someone to scout."
"But the decision is yours."
[complete: C1S5-2]

[objectives: C1S5-3]
Requires: C1S5-2
- Send an adventurer to hunt
- Send an adventurer to scout
[end objectives]
[end if]

|After C1S5-3 is completed, no new objective group is shown. Scene 6 (Chief of Commerce, Valerie joins) starts when the Guild reaches **400 Reputation** (owner, 2026-09-30; GDD 14). Scouting is open from the start (GDD 14 M06, owner 2026-09-30).|