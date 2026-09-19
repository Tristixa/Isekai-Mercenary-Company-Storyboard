# Chapter 1 - New Beginning

## Current implementation handoff: Scenes 1-3

This document currently covers only the story and gameplay required through the end of Scene 3, **Starting Up**.

The current scope ends when the Player receives free control and is told to explore Eurydica, then return to Tristitia by 14:00. Content that happens when the Player returns at 14:00 belongs to the next implementation handoff and is not required yet.

## Current playable flow

### Scene 1 - Opening

**Location:** Eurydica Outskirts  
**Time:** Night  
**Actors:** Player, Tristitia  
**Player control:** Locked

Required sequence:

1. The Player wakes in the Eurydica outskirts.
2. The Player selects a short response about what they remember before arriving.
3. Tristitia notices that the Player is awake.
4. The Player enters their name.
5. The entered name is saved and used in later dialogue.
6. The Player chooses how to introduce themselves.
7. Tristitia tells the Player to remain somewhere safe while she finishes her hunt.
8. The Player chooses a response.
9. The screen fades to black and advances one hour.
10. Tristitia returns after completing the bandit hunt.
11. Tristitia escorts the Player toward Eurydica.
12. The scene transitions to an establishing view of Eurydica City.
13. Tristitia and the Player enter the city and continue to the tavern.
14. The scene transitions into the Eurydica Tavern Interior.

Implementation needs:

- Dialogue display.
- Dialogue choices.
- Player-name entry and name substitution.
- Locked-control story sequences.
- Character movement or simple staged transitions.
- Screen fades.
- A one-hour narrative time advance.
- Location transitions.
- Eurydica establishing presentation.

The Mosswood Forest expedition area does not need to be playable yet. It is only referenced by the story at this stage.

### Scene 2 - Tavern Talk

**Location:** Eurydica Tavern Interior  
**Time:** Night  
**Actors:** Player, Tristitia, Mae  
**Player control:** Locked

Required sequence:

1. Tristitia and the Player meet Mae in the tavern.
2. Mae is shown sorting or inspecting materials from an earlier hunt.
3. The Player chooses how to introduce themselves to Mae.
4. The conversation establishes:
   - Tristitia has completed a bandit hunt.
   - Mae processes materials from Tristitia's hunts.
   - Mosswood has become more dangerous because of a chimera and bolder bandits.
   - Eurydica has no organization that manages adventurers.
   - Adventurers currently find work independently.
   - Selling materials reliably is difficult.
5. The Player explains the idea of an adventurer company.
6. The explanation can be handled with a fade-out rather than a fully written speech.
7. Mae and Tristitia consider the practical value of the Company.
8. The conversation establishes that their available money covers only half of the starting cost.
9. The Player agrees to contribute valuable belongings to help fund the Company.
10. Mae proposes that the Player become Commander.
11. The Player accepts through a dialogue choice.
12. The three characters toast to their new beginning.
13. The screen fades to black.
14. The story advances by one week before Scene 3.

Implementation needs:

- Mae's first appearance.
- Tavern dialogue staging.
- Player introduction and Commander-response choices.
- Story flags recording that the Company has been proposed and founded.
- A one-week story time skip.

The sale of the Player's belongings and the base purchase can remain part of the narrative time skip for now. Exact prices, inventory removal, and a playable purchasing sequence are not required unless a later scene needs them.

### Scene 3 - Starting Up

**Starting location:** Tier 1 Company Base - Main Room  
**Secondary location:** Tier 1 Company Base - Courtyard  
**Time:** Morning, one week after Scene 2  
**Actors:** Player, Tristitia, Mae, Elsie  
**Player control:** Locked until the end of the scene

Required sequence:

1. The scene begins in the Tier 1 Company Base main room.
2. Tristitia reviews the Company's current situation with the Player.
3. The conversation establishes the initial responsibilities:
   - The Player is the Commander and makes Company decisions.
   - Tristitia handles recruitment and daily reports.
   - Mae handles processing.
   - Elsie manages and trains adventurers.
4. The conversation establishes the Company's immediate priorities:
   - Build reputation.
   - Keep gold flowing.
   - Obtain requests despite having no reputation yet.
   - Avoid relying on the market because it pays poorly for materials.
5. Tristitia takes the Player to the courtyard.
6. Elsie is introduced.
7. The Player chooses how to introduce themselves to Elsie.
8. Elsie agrees to work with the Player and take responsibility for adventurers.
9. Tristitia and the Player return to the main room.
10. The conversation establishes the starting base limitations:
    - The base is modest and workshop-like rather than grand.
    - The Player has a Commander room.
    - The dormitory currently fits two adventurers.
    - Tristitia and the others still share a room at the inn.
11. Tristitia tells the Player to explore and become familiar with Eurydica.
12. Tristitia tells the Player to return by 14:00, when she expects to have a job and adventurers available.
13. The current objective is displayed.
14. Player control is unlocked.

Current objective:

> Explore Eurydica and return to Tristitia by 14:00.

## Locations required through Scene 3

### Eurydica Outskirts

- Used for the opening story sequence.
- Night presentation.
- Needs enough space to stage the Player and Tristitia.
- Does not need to support free exploration yet.

### Eurydica City

- First shown through an establishing presentation during Scene 1.
- Becomes explorable after Scene 3.
- Must connect the Player to the tavern, market, and Company base as needed by the existing game structure.

### Eurydica Tavern Interior

- Used for Scene 2.
- Must support the Player, Tristitia, and Mae sitting or standing around a table.
- Mae should have visible monster materials or an equivalent processing prop if available.
- Does not need to become a full gameplay hub yet.

### Tier 1 Company Base

The starting base should be small, practical, and workshop-like.

Required spaces:

- Main room.
- Commander room.
- Small courtyard.
- Small dormitory with capacity for two adventurers.

The main room and courtyard are directly used in Scene 3. The Commander room and dormitory should exist for exploration and visual continuity, but they do not need advanced interactions yet.

### Mosswood Forest

- Mentioned during the story.
- Does not need to be playable through Scene 3.
- Hunting, expeditions, and scouting are deferred until the story reaches their introduction.

## Gameplay available after Scene 3

Once Player control is unlocked, the following limited gameplay should be available:

- Explore the Tier 1 Company Base.
- Explore the currently available part of Eurydica City.
- Talk with available NPCs.
- Visit the market.
- Sell materials at 50% of their base value.
- See the current objective to return to Tristitia by 14:00.
- Advance the existing game clock toward 14:00 using the game's current time system.

The Player should not be able to progress into unwritten 14:00 story content. Reaching the current content boundary can show a temporary end-of-current-content message or stop before triggering the next story event.

## Character content required

### Player

- Name entry.
- Name substitution in dialogue.
- Dialogue choices in all three scenes.
- Commander status after Scene 2.

### Tristitia

- Present throughout Scenes 1-3.
- Opening rescue and escort dialogue.
- Company founding dialogue.
- Base tutorial and current-objective dialogue.

### Mae

- Introduced in Scene 2.
- Established as Tristitia's current processor.
- Present or acknowledged during the Scene 3 Company setup.
- Her full processing interface is not required yet.

### Elsie

- Introduced in Scene 3.
- Established as responsible for managing and training adventurers.
- Her adventurer-management interface may remain empty or locked until the Company recruits its first adventurers.

### City NPCs

- Only enough NPCs are needed to support basic city exploration and the existing Talk interaction.
- Chapter-specific request-givers and recruitable adventurers are deferred until their story introduction.

## Required state at the end of Scene 3

- The Player's chosen name is saved.
- The Company has been founded.
- The Player is recognized as Commander.
- One week has passed since the tavern discussion.
- Tristitia, Mae, and Elsie have joined the Company's starting structure.
- The Tier 1 base is available.
- The dormitory capacity is two adventurers.
- The Company has no recruited adventurers yet unless the existing save or test setup provides them.
- Free exploration is unlocked.
- The game is in the morning before 14:00.
- The active objective is to explore Eurydica and return to Tristitia by 14:00.

## Implementation checklist

The current story scope is ready when:

- Scene 1 can be played from waking up through entering the tavern.
- The Player can enter a name and see it used afterward.
- Scene 2 can be played through the founding of the Company.
- The one-week transition leads into Scene 3.
- Scene 3 moves correctly between the base main room and courtyard.
- Elsie is introduced and her responsibility is established.
- The base visibly supports its stated Tier 1 layout and two-adventurer dormitory capacity.
- The objective to explore Eurydica and return by 14:00 appears.
- Player control unlocks only at the end of Scene 3.
- The Player can explore the base and city, talk to available NPCs, and use the low-value market.
- The Player cannot accidentally enter incomplete story content after reaching the current boundary.

## Deferred until later scenes are written

The following items are intentionally on hold:

- The 14:00 return event.
- Recruiting the first two adventurers.
- The five slime-part requests.
- The operational Company Menu and its closeout option.
- Day summary.
- Adventurer management, training, backpacks, and resting.
- Mosswood Forest hunting expeditions.
- Scouting.
- Mae's playable processing orders and quality results.
- Chapter 1 completion conditions.
- Mae becoming an officer.
- Any Chapter 2 transition.
