---
name: imc-dialogue-drafting
description: Draft, review, personalize, or revise dialogue and story scenes for Isekai Mercenary Company while preserving its character sheets, conversational style, player voice, and separation from Chasm of Hope canon. Use for IMC manuscript dialogue, scene previews, dialogue reviews, character voice passes, and dialogue-focused story work.
---

# IMC Dialogue Drafting

Produce dialogue that sounds like people affecting one another in the moment, not characters taking turns delivering an outline.

## Authority

Use sources in this order:

1. The user's current request and corrections.
2. `IMC_WORLD_CANON_HANDOFF.md` for stable setting canon.
3. Current files in `Characters/` for character identity and voice.
4. The current manuscript for scene events and user-written wording.
5. `IMC_STORY_AGENT_BIBLE.md` for narrative principles and anti-contamination rules.
6. Chasm of Hope only for transferable conversation mechanics.

When manuscript dialogue conflicts with a character sheet, preserve the event or structural purpose but revise the voice toward the character sheet. Never let draft dialogue silently redefine a locked character.

For any dialogue task, read [references/chasm-dialogue-mechanics.md](references/chasm-dialogue-mechanics.md). Consult the original Chasm scenes listed there only when a deeper comparison or recalibration is needed.

## Separate style from canon

Chasm of Hope is evidence for the user's conversational instincts, not a source of IMC world facts or default voices. Do not import Fallout, Mojave, cowboy cadence, wasteland grimness, quest logic, or Chasm Elsie's gunslinger identity.

IMC Elsie may share warmth, companion-like attachment, light teasing, restrained sincerity, and a love of freedom. Express those qualities through her army background, expedition responsibility, and fantasy-world voice. She does not say “partner,” use a western drawl, or behave like a bounty-hunting cowgirl.

## Determine the task mode

- **Review:** Diagnose voice, structure, conversational flow, exposition, humor, and emotional turns. Do not edit files.
- **Brainstorm:** Develop intentions, pressures, relationships, and possible turns. Do not present provisional ideas as canon.
- **Preview revision:** Explain the intended changes, then show the complete proposed dialogue with enough action context to judge the exchange. Do not edit files.
- **Apply approved revision:** Modify only the approved material, preserve newer user edits, and verify the resulting scene.
- **New scene draft:** Establish scene purpose and conversational pressure, then draft. If the draft is intended to replace manuscript text, treat it as a preview until approved.

Review, brainstorming, and preview requests never authorize manuscript edits.

## Prepare the conversation

Read the full target scene and the current sheets of every speaking character. Do not rely on the bible's compact voice cards when a more current character sheet exists.

Before drafting, establish:

- The concrete situation happening now.
- What each person wants from this conversation.
- What each person would rather not say directly.
- What each person believes the other person needs or is getting wrong.
- The relationship temperature at the beginning.
- The practical decision, responsibility, or relationship change at the end.
- Any game information the scene must communicate.

Convert required information into conversational pressure. Ask who needs the information, why they need it now, what they might question, and how hearing it changes their next choice.

## Build a turn map

Map the exchange by cause and reaction, not by assigning facts to speakers. A useful shape is:

`concrete prompt → personal reaction → answer, deflection, or reframe → response or pushback → shared conclusion or emotional pivot`

For every planned turn, know:

- **Cause:** What previous line, action, silence, or shared fact prompted it?
- **Intention:** Is the speaker answering, asking, reassuring, testing, avoiding, teasing, correcting, persuading, challenging, or redirecting?
- **Effect:** What new reaction or choice does it invite from the listener?

If a turn exists only because the audience needs information, create a believable in-scene need or move the information outside dialogue.

## Draft in conversational units

Treat one naturally unfolding thought as one conversational unit even when it uses several sentences.

- Use short lines for genuine reactions, acknowledgments, refusals, corrections, or pressure.
- Use longer turns when someone explains, remembers, persuades, qualifies, or reluctantly admits something.
- Do not split a thought into several isolated aphorisms.
- Do not make every turn equally brief, polished, witty, or complete.
- Allow contractions, interrupted starts, repeated words, modest fillers, and changes of direction when they fit the speaker.
- Do not add grammatical mistakes merely to imitate natural speech.
- Let characters answer implications, delay answers, or partially answer when that behavior creates a response from the listener.
- Preserve ordinary connective language. Not every sentence needs to be memorable by itself.

Write forward from the previous line. Do not draft each character's lines separately and interleave them afterward.

## Preserve character ownership

Use the character sheet's worldview, work, emotional armor, care language, and relationship—not only its example lines or sentence-length label.

- “Concise” means the character avoids unnecessary explanation; it does not mean every line must be clipped.
- “Unhurried” concerns timing and proportion; it does not make Mae passive, lazy, or limited to one-liners.
- “Polished” concerns Tristitia's control and word choice; it does not make her speak in slogans.
- “Warm” does not make Elsie constantly joke or flirt.
- “Unsure” does not make Liliana unintelligent.
- Player flexibility does not make the Commander blank. Preserve his curious, reactive, conversational Vanilla-inspired base across different player intentions.

## Handle humor and emotion

Humor must react to something already present: another person's wording, a practical absurdity, shared history, a mismatch in priorities, or a character's habitual defense. It should ease, test, deflect, or deepen the relationship. Do not insert a joke as an independent beat.

Build emotional turns from ordinary activity, work, teasing, or disagreement. Let sincerity arrive through a small admission, a practical offer, a deferred promise, or a change in responsibility. Avoid having a character announce the theme or summarize their emotional arc.

## Keep exposition human

Do not use Tristitia, Elsie, Mae, or another officer as a game-system presenter. When rules or systems must be explained:

- Give the listener a reason to ask.
- Let the explanation reflect the officer's own concern.
- Permit questions, corrections, resistance, or misunderstanding.
- Break information across relevant actions and decisions.
- Stop once the listener has enough information for the current choice.

## Audit the dialogue

Read the exchange aloud as continuous speech. Revise until each substantial turn passes these checks:

- What caused this line now?
- What is the speaker trying to do to or with the listener?
- Does the listener respond to the meaning or pressure of the line?
- Could another character say it unchanged?
- Is this speech, or author information placed inside quotation marks?
- Has one natural thought been broken into multiple quote-ready fragments?
- Is the character performing their profile instead of living it?
- Does humor belong to this person and this moment?
- Does the emotional turn grow from the exchange?
- Does the scene communicate only the information needed now?

Also run the bible's contamination check.

## Present and apply revisions

Before changing an existing manuscript scene:

1. Tell the user the intended changes and why they address the scene's actual problem.
2. Show the full proposed dialogue in scene order. Include relevant action beats and do not substitute a sample excerpt for the complete exchange.
3. Wait for explicit approval.
4. Apply only the approved version with `apply_patch`.
5. Re-read the edited scene to confirm no user revision was overwritten and the dialogue still flows around the changed passage.

Do not treat approval of an earlier version as approval of a newly rewritten version.
