# Scene 4 Day 1-5

## Synopsis
This is only each characters dialogues/side arc/side quest before the next chapter 1 scene milestone.
Request details are maintained in the Requests folder. Availability notices below add the named request to the request list only on the help/accept branch.

## Gameplay dialogue staging

|On interaction, Player and NPC face each other. Hold one shared dialogue view through the conversation and choices. Both remain in their ordinary idle poses. Return to gameplay when the conversation ends.|

This applies to officer conversations and request-givers. Hold the same view across topics, including Tristitia's silence about her father. Elsie's look-behind joke is the exception noted below. Ambient townspeople have no bespoke staging.

---


# Tristitia Talk
Tristitia: "Commander. Is there something you need?"

### [ Ask about her]
Player: "How do you know so much about running things."
Tristitia: "Someone taught me well."
Player: "Who's the guy?"
Tristitia: "My father."
Player: "Is he around?"
Tristitia: "No."

### [ Ask about Mae ]
Player: "Mae and you seems close."
Tristitia: "Sure, we works well together."
Player: "How long have you met her?"
Tristitia: "From the start of my adventuring days."
"She's the first person I trust."

### [ Ask about Elsie]
Player: "Elsie is your friend?"
Tristitia: "Yes, it's nice being around her."
Player: "What about me?"
Tristitia: "......."
Tristitia: "You are very honest."


---

# Mae Talk
If corpses are awaiting processing:
Mae: "Ah, <name>. We still have something left from the last hunt, if you want me to process it."

Otherwise:
Mae: "Ah, <name>. How are things?"

### [ Ask about her ]
Player: "How long have you been doing this?"
Mae: "Long enough to know how to process any kind of monster."
Player: "Any kind? surely not."
Mae: "Well I never get my hands on dragon before, or monsters from the frontier."

### [ Ask about Tristitia ]
Player: "Tristitia and you seems close."
Mae: "We go long way back, I think I know her better than my lovers."
Player: "You have a lover?"
Mae: "Not anymore, I love what I do and want to focus on this guild for now."

### [ Ask about Eurydica ]
Player: "So what's the city like?"
Mae: "It's a nice and warm place compared to other cities."
Mae: "You will like it soon enough."
Player: "Is there any interesting place?"
Mae: "Try the old city streets, it have the best view."

### [ Ask about The Frontier ] (unlocked after ask about her)
Player: "What's the frontier?"
Mae: "Hmmm I only know vague information about it."
Mae: "Elsie know it better she used to be there."

---

# Elsie Talk
Elsie: "There you are. How's it going?"

### [ Ask about her ]
Player: "You used to lead people?"
Elsie: "I do, somehow people always put me as someone in charge."
Player: "In an army?"
Elsie: "Yeah, In the frontier."
Elsie: "I used to butthead with the officers there."
Player: "Why quit?"
Elsie: "Why indeed, you'll know when you step foot on that place."
Elsie: "I like here more, it's not constricting."

### [ Ask about Tristitia ]
Player: "Tristitia and you seems close."
Elsie: "Shhh don't let her hear that."
"She will stab you."
Player: "really? she seems nice to me."
Elsie: "You think so? you don't think she's unfriendly?"
Player: "Well, maybe she is..."
[Sassy] "A bit sassy."
[Rude] "A bit rude to someone."
[Cold] "A bit cold."
Elsie: "Uh oh, do you hear that Tristitia?"
|When Elsie calls to Tristitia, Player turns to look behind him. Briefly show the empty space he is looking toward. Return to the previous shared view as he faces Elsie again.|
Player: "She's not there."
Elsie: "I'm just teasing you."
Player: "So what's she likes to you?"
Elsie: "Trusted friend, we understand each other."
"she didn't talk much but she's actually nice conversation partner."

### [ Ask about The Frontier ] (unlocked after ask about her)
Player: "What's the frontier?"
Elsie: "It's vast lands that remain largely unexplored."
"Ancient ruins, dangerous creatures, forgotten roads, and remnants of an unknown civilization dot the landscape."
Player: "So civilization only occupies fraction of the world?"
Elsie: "Yeah, small compared to that place."
Player: "Maybe we can send expedition there."
Elsie: "Too dangerous, I say we stay clear."
"People lost their lives all the time there."
"Informations and discoveries are rumors at best."
"Understanding the frontier will need an organization that can verify everything, and make sure folks are safe."
Player: "Like our guild?"
Elsie: "Well now, you do have a point."
Player: "You're teasing me again are you?"
Elsie: "*chuckle*, Apologize commander."

---


# Request 1 (Traveling Merchant in Market Spine) [CH1-REQ-003]
The merchant's muttering appears when Player gets nearby, before interaction.
Travelling Merchant:
"Hmmm there's not much rare slime parts in the market..."
"Must be because of the chimera."
"Where can I get them, I already promised the client."

|Player approaches and starts the standard shared interaction view. No staged merchant departure is needed after the conversation.|
Player:
[Offer help] "I can help you with that."
[Walk away] {It's not my business.}

### If the Player Walk away
the scene end.

### If the Player Offer Help
Travelling Merchant:
"Oh? do you have any rare slime part?"

Player:
"Not yet, you can send the request to <Guild-name>."
"We handle any job involved with monster and adventurer."
"Tristitia will tell you more."

Travelling Merchant:
"Hmmm I don't have much gold but I know a lot of people."
"I can spread your Guild name."

Player:
"Sure."

Travelling Merchant:
"Thank you, I'll go to the Guild building then."

Player:
"Okay."


Request "Merchant's Rare Slime Order" [CH1-REQ-003] is now available.

---

# Request 2 (Dr. Ginger in Service Lanes) [CH1-REQ-004]
Dr.Ginger:
"Hello young man, you don't have any common slime parts by chance are you?"

Player:
"Maybe, in my Guild storage."

Dr.Ginger:
"Can I have some? I need them for my work."

Player:
[Refuse] "No way."
[Accept] "Sure you can make the request at my Guild."
"Tristitia will tell you more."

### If the Player Refuse
Dr.Ginger:
"Well okay sonnie."

### If the Player Offer Help
Dr.Ginger:
"Thanks boy, I'll talk to her."


Request "Clinic Restock" [CH1-REQ-004] is now available.

---

# Request 3 - Hollis: Winter Bedding [CH1-REQ-005]

Location: Stables near the south gate.

|Standard shared interaction view. Hold throughout.|

Hollis: "You're with the new company, aren't you? Do your people bring back wolf pelts?"
Player: "We could. How many do you need?"
Hollis: "Three should do. It's for the bed out here. Whoever watches the stable at night sleeps beside the door, and the cold comes straight underneath it."
Player: "You sleep in the stable?"
Hollis: "Some nights. My son takes the others. He's been bringing his blanket from home, but his mother wants it back."
Player: "Wouldn't fixing the door help?"
Hollis: "Already did. It helped. Still need something warmer on the bed."

Player:
[Offer to arrange it] "We haven't found a place to hunt wolves yet, but we can look into it."
[Decline] "I don't think we can help right now."

### If offering

Hollis: "That's fine. I'm asking before it gets cold enough for him to refuse his turn."
Player: "Talk to Tristitia at <Guild-name>. She'll write down what you need."
Hollis: "All right. Three pelts, and no need to hurry."

Request "Winter Bedding" [CH1-REQ-005] is now available.

### If declining

Hollis: "Fair enough. Let me know if that changes."


### Later visit after completion

Hollis: "The bedding's finished. My son brought a pillow over yesterday, so I suppose he's staying."

---

# Request 4 - Marta: Something Different for Supper [CH1-REQ-006]

Location: Food shop in the Service Lanes.

|Standard shared interaction view. Hold throughout.|

Marta: "You're the one running that adventurer company?"
Player: "Yes. Do you have some work for us?"
Marta: "Possibly. If your people bring back a boar, I'd like to buy some of the meat. I've been meaning to cook something different."
Player: "What do you usually make?"
Marta: "Stew. It sells, so I keep making it. Then everyone asks why I always serve the same thing."
Player: "What would you make with the boar?"
Marta: "I was thinking a roast. Garlic, a few herbs... depends on what I can get."

Player:
[Offer to arrange it] "That sounds good. We can take the request, though it might be a while."
[Decline] "We're not ready to take that on yet."

### If offering

Marta: "That's all right. I haven't promised anyone anything."
Player: "We still need to find where the boars are. You can speak to Tristitia at <Guild-name> about the order."
Marta: "I'll come by when it's quiet."

Request "Something Different for Supper" [CH1-REQ-006] is now available.

### If declining

Marta: "Well, you know where I am if you bring some back."


### Later visit after completion

Marta: "I made the roast. Sold most of it before midday."
Player: "So they liked the change?"
Marta: "Most of them. Someone asked where the stew was."

---

# Request 5 - Beren: Keep the Old Ones Working [CH1-REQ-007]

Location: Repair & Supply shop in the Market Spine.

|Standard shared interaction view. Hold throughout.|

Beren: "If your company starts hunting boars, I could use a couple of hides."
Player: "For armor?"
Beren: "Repairs, mostly. Straps, patches, that sort of thing. I've got people waiting on things they'd rather mend than replace."
Player: "Are they waiting for the hides?"
Beren: "Some are. I've enough leather for the smaller jobs. There's one pair of work boots I haven't started yet."
Player: "Too badly damaged?"
Beren: "He's worn through them again. I told him he ought to buy another pair, but he says these are comfortable."
Player: "Even with holes in them?"
Beren: "Apparently."

Player:
[Offer to arrange it] "We can take the request. We'll need to find a hunting ground first."
[Decline] "You might have to ask someone else for now."

### If offering

Beren: "That's fine. Bring the request here when it's ready, or tell me who I should speak to."
Player: "Tristitia, at <Guild-name>. She handles the arrangements."
Beren: "All right. I'll speak to her."

Request "Keep the Old Ones Working" [CH1-REQ-007] is now available.

### If declining

Beren: "All right. Keep me in mind if you end up with some."


### Later visit after completion

Beren: "Your hides came through. Those boots should last him a while longer."

---

# Ambient Townspeople

Each entry is a separate optional encounter with Player, not a conversation among NPCs. No bespoke staging, quest markers, rewards, required encounter order, or forced explanation. The three women walk separately through the city at night. Completion-dependent lines replace the corresponding ordinary line after the named request is completed.

## Lady in a Red Dress

Location: Market Spine, at night.

Lady in a Red Dress: "Have you met the woman in green? She'll ask you where you've been, who you were with... You don't have to tell her, you know."

## Lady in a Green Dress

Location: Near the Old Bridge, at night.

Lady in a Green Dress: "That woman in red said something about me, didn't she? Never mind. She says something about everyone."

## Lady in a Black Dress

Location: Old City, at night.

Lady in a Black Dress: "Hello, darling. Out for a walk?"

## Tough-Looking Worker

Location: Outside Marta's shop.

Tough-Looking Worker: "If you're going in, ask what she's cooking. I've been smelling it all morning, but I can't leave until the cart gets here."

After Marta's request is completed:
Tough-Looking Worker: "Had the roast yesterday. Asked her to save me some today, but apparently everyone else had the same idea."

## Middle-Aged Guard

Location: South gate, toward evening.

Middle-Aged Guard: "Heading out? Leave yourself enough light to get back. Those roots near Mosswood are hard enough to see in the daytime."

## Intelligent Girl

Location: Near the Old Bridge.

Intelligent Girl: "The bell sounds different here than it does up by the tower. I'm trying to find where it changes. Could you stop talking for a moment? It's nearly time."

## Woman with a Laundry Basket

Location: Residential streets.

Woman with a Laundry Basket: "I washed everything because it looked like rain yesterday. Now it looks like rain today. If I keep waiting, we won't have anything left to wear."

## Well-Dressed Young Man

Location: Outside Repair & Supply.

Well-Dressed Young Man: "I came to collect my boots, but I can't remember which pair I left here. I'd recognize them if he showed me."

This does not establish him as the customer Beren mentioned.

## Older Woman

Location: Old City viewpoint.

Older Woman: "My husband always complained about the stairs. Then he'd spend an hour up here and complain when I wanted to leave."

Her husband's current whereabouts are not established by this line.

## Sleepy Stablehand

Location: Near the stables, in the morning.

Sleepy Stablehand: "If you're looking for my father, he's inside. If he asks, I've already swept out here."

After Hollis's request is completed:
Sleepy Stablehand: "Father says I'm sleeping too well on watch now. He was the one who wanted better bedding."
