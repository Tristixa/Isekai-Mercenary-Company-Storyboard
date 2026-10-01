# Scene 4 - Day 2-5

## Synopsis
Location: Eurydica (the Guild house and the city)
Time: Days 2–5, any time unless stated
Actors: Commander, Tristitia, Mae, Elsie, request-givers, townspeople

|This scene is each character's talks, side arcs and side requests before the next Chapter 1 milestone. Request details live in the Requests folder. A request is added to the request list only on its help/accept branch (`{request: …}`). Talks use the default talk staging (face each other, shared view); only Elsie's look-behind joke is specially staged. Ambient townspeople have no bespoke staging, markers, rewards or required order.|

---

## Talk: Tristitia
Where: Commander's Office

Tristitia (Base):
"Commander. Is there something you need?"

Commander:

1. **[Ask about her]** {topic}
   Commander (Surprise):
   "How do you know so much about running things."
   Tristitia (Surprise):
   "Someone taught me well."
   Commander (Base):
   "Who's the guy?"
   Tristitia (Surprise):
   "My father."
   Commander (Base):
   "Is he around?"
   Tristitia (Base):
   "No."

2. **[Ask about Mae]** {topic}
   Commander (Base):
   "Mae and you seems close."
   Tristitia (Surprise):
   "Sure, we works well together."
   Commander (Base):
   "How long have you met her?"
   Tristitia (Surprise):
   "From the start of my adventuring days."
   Tristitia (Happy):
   "She's the first person I trust."

3. **[Ask about Elsie]** {topic}
   Commander (Base):
   "Elsie is your friend?"
   Tristitia (Surprise):
   "Yes, it's nice being around her."
   Commander (Happy):
   "What about me?"
   Tristitia (Surprise):
   "......."
   Tristitia (Surprise):
   "You are very honest."

---

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
   Mae (Happy):
   "Long enough to know how to process any kind of monster."
   Commander (Surprise):
   "Any kind? surely not."
   Mae (Laugh):
   "Well I never get my hands on dragon before, or monsters from the frontier."

2. **[Ask about Tristitia]** {topic}
   Commander (Base):
   "Tristitia and you seems close."
   Mae (Happy):
   "We go long way back, I think I know her better than my lovers."
   Commander (Surprise):
   "You have a lover?"
   Mae (Base):
   "Not anymore, I love what I do and this guild is my focus for now."

3. **[Ask about Eurydica]** {topic}
   Commander (Base):
   "So what's the city like?"
   Mae (Happy):
   "It's a nice place compared to other cities."
   "You will like it soon enough."
   Commander (Base):
   "Is there any interesting place?"
   Mae (Happy):
   "Try the old city streets, it have the best view."

4. **[Ask about The Frontier]** {topic} {after: Ask about her}
   Commander (Base):
   "What's the frontier?"
   Mae (Serious):
   "Hmmm I only know vague information about it."
   Mae (Base):
   "Elsie should know it better, she used to be there."

---

## Talk: Elsie
Where: Courtyard

Elsie (Happy):
"There you are. How's it going?"

Commander:

1. **[Ask about her]** {topic}
   Commander (Base):
   "You used to lead people?"
   Elsie (Happy):
   "I do, somehow people always put me as someone in charge."
   Commander (Surprise):
   "In an army?"
   Elsie (Happy):
   "Yeah, In the frontier."
   Elsie (Laugh):
   "I used to argue all the time with the officers there."
   Commander (Base):
   "Why quit?"
   Elsie (Happy):
   "Why indeed, you'll know when you step foot on that place."
   Elsie (Happy):
   "I like it here more, it's not constricting."

2. **[Ask about Tristitia]** {topic}
   Commander (Base):
   "Tristitia and you seems really close."
   Elsie (Surprise):
   "Shhh don't let her hear that."
   Elsie (Fear):
   "She will stab you, if you ask her that."
   Commander (Surprise):
   "really? she seems nice to me."
   Elsie (Surprise):
   "You think so? you don't think she's unfriendly?"
   Commander (Base):
   "Well, maybe she is..."
   Commander:
   1. **[Sassy]**
      Commander (Laugh):
      "A bit sassy."
   2. **[Rude]**
      Commander (Laugh):
      "A bit rude to someone."
   3. **[Cold]**
      Commander (Laugh):
      "A bit cold."
   Elsie (Laugh):
   "Uh oh, do you hear that Tristitia?"
   [face: Commander back]
   [camera: gaze Commander]
   [pause: 1.0]
   [emote: Commander question]
   [face: Commander Elsie]
   [camera: return]
   Commander (Surprise):
   "She's not there."
   Elsie (Laugh):
   "I'm just teasing you."
   Commander (Base):
   "So what's she likes to you?"
   Elsie (Happy):
   "Trusted friend, we understand each other."
   "she didn't talk much but she's actually nice conversation partner."

3. **[Ask about The Frontier]** {topic} {after: Ask about her}
   Commander (Base):
   "What's the frontier?"
   Elsie (Base):
   "It's a vast lands that remain largely unexplored."
   "Ancient ruins, dangerous creatures, forgotten roads, and remnants of an unknown civilization dot the landscape."
   Commander (Surprise):
   "So civilization only occupies fraction of the world?"
   Elsie (Base):
   "Yeah, small compared to that place."
   Commander (Laugh):
   "Maybe we can send expedition there."
   Elsie (Serious):
   "Too dangerous, I say we stay clear."
   Elsie (Sad):
   "People lost their lives all the time there."
   Elsie (Serious):
   "Informations and discoveries are rumors at best."
   "Understanding the frontier will need an organization that can verify everything, and make sure folks are safe."
   Commander (Surprise):
   "Like our guild?"
   Elsie (Laugh):
   "Well now, you do have a point."
   Commander (Surprise):
   "You're teasing me again are you?"
   [emote: Elsie laugh]
   Elsie (Laugh):
   "*chuckle*, Apologize commander."

---

## Bark: Travelling Merchant
Trigger: nearby
"Hmmm there's not much rare slime parts in the market..."
"Must be because of the chimera."
"Where can I get them, I already promised the client."

## Talk: Travelling Merchant (Request 1, CH1-REQ-003)
Where: Market Spine stall

Commander:

1. **[Offer help]** {request: CH1-REQ-003}
   Commander (Base):
   "I can help you with that."
   Travelling Merchant (Surprised):
   "Oh? do you have any rare slime part?"
   Commander (Base):
   "Not yet, you can send the request to <Guild-name>."
   "We handle any job involved with monster and adventurer."
   "Tristitia will tell you more."
   Travelling Merchant (Considering):
   "Hmmm I don't have much gold but I know a lot of people."
   Travelling Merchant (Pleased):
   "I can spread your Guild name."
   Commander (Happy):
   "Sure."
   Travelling Merchant (Deal):
   "Thank you, I'll go to the Guild building then."
   Commander (Base):
   "Okay."

2. **[Walk away]**
   Commander (Base):
   {It's not my business.}
   [end]

---

## Talk: Dr. Emmerich (Request 2, CH1-REQ-004)
Where: Clinic, Service Lanes

Dr. Emmerich (Base):
"Hello young man, you don't have any common slime parts by chance are you?"

Commander (Base):
"Maybe, in my Guild storage."

Dr. Emmerich (Happy):
"Can I have some? I need them for my work."

Commander:

1. **[Refuse]**
   Commander (Serious):
   "No way."
   Dr. Emmerich (Sad):
   "Well okay sonnie."

2. **[Accept]** {request: CH1-REQ-004}
   Commander (Happy):
   "Sure you can make the request at my Guild."
   "Tristitia will tell you more."
   Dr. Emmerich (Happy):
   "Thanks boy, I'll talk to her."

---

## Talk: Jeb (Request 3, CH1-REQ-005: Winter Bedding)
Where: Stables near the South Gate

[if: done: CH1-REQ-005]
Jeb (Happy):
"The bedding's finished. My son brought a pillow over yesterday, so I suppose he's staying."
[else]
Jeb (Base):
"You're with the new guild, aren't you? Do your people bring back wolf pelts?"

Commander (Base):
"We could. How many do you need?"

Jeb (Base):
"Three should do. It's for the bed out here. Whoever watches the stable at night sleeps beside the door, and the cold comes straight underneath it."

Commander (Surprise):
"You sleep in the stable?"

Jeb (Base):
"Some nights. My son takes the others. He's been bringing his blanket from home, but his mother wants it back."

Commander (Base):
"Wouldn't fixing the door help?"

Jeb (Serious):
"Already did. It helped. Still need something warmer on the bed."

Commander:

1. **[Offer to arrange it]** {request: CH1-REQ-005}
   Commander (Base):
   "We haven't found a place to hunt wolves yet, but we can look into it."
   Jeb (Base):
   "That's fine. I'm asking before it gets cold enough for him to refuse his turn."
   Commander (Base):
   "Talk to Tristitia at <Guild-name>. She'll write down what you need."
   Jeb (Happy):
   "All right. Three pelts, and no need to hurry."

2. **[Decline]**
   Commander (Sad):
   "I don't think we can help right now."
   Jeb (Base):
   "Fair enough. Let me know if that changes."
[end if]

---

## Talk: Hilde (Request 4, CH1-REQ-006: Something Different for Supper)
Where: Food shop, Service Lanes

[if: done: CH1-REQ-006]
Hilde (Happy):
"I made the roast. Sold most of it before midday."

Commander (Happy):
"So they liked the change?"

Hilde (Laugh):
"Most of them. Someone asked where the stew was."
[else]
Hilde (Base):
"You're the one running that adventurer guild?"

Commander (Base):
"Yes. Do you have some work for us?"

Hilde (Base):
"Possibly. If your people bring back a boar, I'd like to buy some of the meat. I've been meaning to cook something different."

Commander (Base):
"What do you usually make?"

Hilde (Sad):
"Stew. It sells, so I keep making it. Then everyone asks why I always serve the same thing."

Commander (Base):
"What would you make with the boar?"

Hilde (Happy):
"I was thinking a roast. Garlic, a few herbs... depends on what I can get."

Commander:

1. **[Offer to arrange it]** {request: CH1-REQ-006}
   Commander (Happy):
   "That sounds good. We can take the request, though it might be a while."
   Hilde (Base):
   "That's all right. I haven't promised anyone anything."
   Commander (Base):
   "We still need to find where the boars are. You can speak to Tristitia at <Guild-name> about the order."
   Hilde (Happy):
   "I'll come by when it's quiet."

2. **[Decline]**
   Commander (Sad):
   "We're not ready to take that on yet."
   Hilde (Base):
   "Well, you know where I am if you bring some back."
[end if]

---

## Talk: Gerd (Request 5, CH1-REQ-007: Keep the Old Ones Working)
Where: Repair & Supply, Market Spine

[if: done: CH1-REQ-007]
Gerd (Happy):
"Your hides came through. Those boots should last him a while longer."
[else]
Gerd (Base):
"If your guild starts hunting boars, I could use a couple of hides."

Commander (Base):
"For armor?"

Gerd (Base):
"Repairs, mostly. Straps, patches, that sort of thing. I've got people waiting on things they'd rather mend than replace."

Commander (Base):
"Are they waiting for the hides?"

Gerd (Base):
"Some are. I've enough leather for the smaller jobs. There's one pair of work boots I haven't started yet."

Commander (Surprise):
"Too badly damaged?"

Gerd (Sad):
"He's worn through them again. I told him he ought to buy another pair, but he says these are comfortable."

Commander (Surprise):
"Even with holes in them?"

Gerd (Laugh):
"Apparently."

Commander:

1. **[Offer to arrange it]** {request: CH1-REQ-007}
   Commander (Base):
   "We can take the request. We'll need to find a hunting ground first."
   Gerd (Base):
   "That's fine. Bring the request here when it's ready, or tell me who I should speak to."
   Commander (Base):
   "Tristitia, at <Guild-name>. She handles the arrangements."
   Gerd (Happy):
   "All right. I'll speak to her."

2. **[Decline]**
   Commander (Sad):
   "You might have to ask someone else for now."
   Gerd (Base):
   "All right. Keep me in mind if you end up with some."
[end if]

---

## Ambient: Lady in a Red Dress
Where: Market Spine
When: Night
Lady in a Red Dress:
"Have you met the woman in green? She'll ask you where you've been, who you were with... You don't have to tell her, you know."

## Ambient: Lady in a Green Dress
Where: Near the Old Bridge
When: Night
Lady in a Green Dress:
"That woman in red said something about me, didn't she? Never mind. She says something about everyone."

## Ambient: Lady in a Black Dress
Where: Old City
When: Night
Lady in a Black Dress:
"Hello, darling. Out for a walk?"

## Ambient: Tough-Looking Worker
Where: Outside Hilde's shop
[if: done: CH1-REQ-006]
Tough-Looking Worker:
"Had the roast yesterday. Asked her to save me some today, but apparently everyone else had the same idea."
[else]
Tough-Looking Worker:
"If you're going in, ask what she's cooking. I've been smelling it all morning, but I can't leave until the cart gets here."
[end if]

## Ambient: Middle-Aged Guard
Where: South Gate
When: Evening
Middle-Aged Guard:
"Heading out? Leave yourself enough light to get back. Those roots near Hylaea are hard enough to see in the daytime."

## Ambient: Intelligent Girl
Where: Near the Old Bridge
Intelligent Girl:
"The bell sounds different here than it does up by the tower. I'm trying to find where it changes. Could you stop talking for a moment? It's nearly time."

## Ambient: Woman with a Laundry Basket
Where: Residential streets
Woman with a Laundry Basket:
"I washed everything because it looked like rain yesterday. Now it looks like rain today. If I keep waiting, we won't have anything left to wear."

## Ambient: Well-Dressed Young Man
Where: Outside Repair & Supply
|This line does not establish him as the customer Gerd mentioned.|
Well-Dressed Young Man:
"I came to collect my boots, but I can't remember which pair I left here. I'd recognize them if he showed me."

## Ambient: Older Woman
Where: Old City viewpoint
|Her husband's current whereabouts are not established by this line.|
Older Woman:
"My husband always complained about the stairs. Then he'd spend an hour up here and complain when I wanted to leave."

## Ambient: Sleepy Stablehand
Where: Near the stables
When: Morning
[if: done: CH1-REQ-005]
Sleepy Stablehand:
"Father says I'm sleeping too well on watch now. He was the one who wanted better bedding."
[else]
Sleepy Stablehand:
"If you're looking for my father, he's inside. If he asks, I've already swept out here."
[end if]
