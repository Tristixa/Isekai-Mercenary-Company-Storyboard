# Scene drafts: Elsie's scouting introduction and Tristitia's contracts explanation

Written 2026-09-30 for sprint S7. They're in `Game Design/Scene Script Format.md`, so they can move into `Manuscript/Chapter 1 - New Beginning/` once you've edited them. The dialogue is a **draft for you to rewrite in your own voice**; the game rules each character explains are from the GDD, so keep those facts even if the words change.

---

# Event: Elsie's scouting introduction

## Synopsis
Location: Guild house (Tier 1) courtyard
Time: Day
Actors: Commander, Elsie
Staging: Elsie at bench_east facing west; Commander at bench_west facing east

|Trigger: the first time the player chooses **Scout** in the expedition preparation, after Scene 5 (GDD 14 M06; scouting is open from the start, owner 2026-09-30). The scene plays before the preparation screen opens, then returns to it. It explains GDD §8 in Elsie's words. A proposed new trigger type is `first: scout-prep`, to add to the format guide's Events if you like it.|

---

## Event: Elsie's scouting introduction
Trigger: first: scout-prep
[control: lock]
[camera: shared]
[face: Elsie Commander]
Elsie (Base):
"A scouting run? Good call. Let me tell you how it works before you pick someone."

Elsie (Serious):
"A scout goes alone. One adventurer, travelling light, no fighting."
"If they see trouble, they get out of its way. Their job is to come back with what they saw."

Commander:

1. **[Ask what they look for]** {Insight}
   Commander (Base):
   "What exactly are they looking for?"
   Elsie (Base):
   "Everything that makes the next hunt easier."
   "The more of an area we've mapped, the more we know what lives there: which species, where their dens are, which paths are safe."
   Elsie (Happy):
   "And sometimes they spot something rare. If they do, we mark it, and the next hunting party can go straight for it."

2. **[Ask how long it takes]**
   Commander (Base):
   "How long are they out?"
   Elsie (Base):
   "You choose, in half-hour steps, up to three hours."
   "Every half hour they finish adds to the map. If you call them back early, they keep what they've already found."

3. **[Ask if it's dangerous]** {Leadership}
   Commander (Serious):
   "Is it dangerous?"
   Elsie (Serious):
   "Less than a hunt, but not safe."
   "Every half hour out there, there's a small chance they get hurt. In Hylaea it's small, and it's worse in the highlands."
   "Someone who's already worn out is careless. Send a rested one."
   Elsie (Happy):
   "Nobody dies on a scouting run under me. At worst they limp home early, and they still bring back what they found."

Elsie (Base):
"A Scout Map helps them find things faster, if we have one."
"And a good report earns the Guild a little Reputation, even on a short run."

Commander (Base):
"Understood. Let's pick our scout."

Elsie (Happy):
"That's the spirit."
[control: unlock]
|The preparation screen opens on the Scout tab.|

---

# Event: Tristitia's contracts explanation

## Synopsis
Location: Guild house (Tier 1) interior
Time: Day
Actors: Commander, Tristitia
Staging: Tristitia at table_north facing south, standing; Commander at table_south facing north
Special poses: Tristitia point

|Trigger: at the next safe paused moment after the **first won ordinary hunt fight** (GDD 14 M08): when the Commander next enters the Guild house during the day. It opens **optional subjugation contracts** on the Request Board (GDD §11.3). The first one offered is EUR-SUB-01, the inn owner's slime nuisance, because the first hunt has returned.|

---

## Event: Tristitia's contracts explanation
Trigger: enter: Guild house (Tier 1) interior
[if: m08_ready]
[control: lock]
[move: Commander table_south]
[face: Commander Tristitia]
[camera: shared]
Tristitia (Happy):
"Our first real fight, and they won it."
"Word travels fast in Eurydica. People have started asking whether we take on monsters for hire."

Commander (Base):
"Isn't that what hunting already is?"

Tristitia (Serious):
"A hunt is our choice: we go where we like and take what we find."
"A contract is someone else's problem, a specific monster in a specific place, and they pay us to deal with it."

[camera: push-in Tristitia]
Tristitia (Base):
"Contracts will appear on the Request Board. Read them carefully."
"The party walks straight to the target, about half an hour, and fights exactly what the client described. No searching, no surprises in the numbers."

Commander:

1. **[Ask about the pay]** {Negotiation}
   Commander (Base):
   "And the pay?"
   Tristitia (Base):
   "Better than a hunt, and it comes with Reputation."
   "We keep the corpses as well, same as any hunt."

2. **[Ask what happens if we fail]** {Leadership}
   Commander (Serious):
   "What if we fail?"
   Tristitia (Serious):
   "Then we lose some Reputation. Once you accept, you've given your word."
   "If a contract fails or runs out, the client may ask again in a week, once we're ready."

3. **[Ask how long they last]**
   Commander (Base):
   "Do we have to take them right away?"
   Tristitia (Base):
   "No. An offer stays up for three days, and you can ignore any of them."
   "Accept only what our people can finish."

[camera: return]
[pose: Tristitia point]
Tristitia (Base):
"The innkeeper has already asked. Slimes in her storeroom again."
[pose: Tristitia idle]
"Small work, but it's a start, and a good first name to have on our list."
[request: EUR-SUB-01]

Commander (Happy):
"Then let's make a name for ourselves."

Tristitia (Happy):
"That's the idea."
[control: unlock]
[end if]

|`[request: EUR-SUB-01]` unlocks the contract on the board. Contracts are requests of type "contract" in the content data. `m08_ready` is a named game state (the first ordinary hunt fight won, M08's condition), to add to the converter's conditions list.|
