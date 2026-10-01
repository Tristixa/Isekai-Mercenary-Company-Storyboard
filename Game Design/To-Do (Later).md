# To-do later (big items)

Owner, 2026-10-01: big features to pick up when weekly usage resets. They are agreed directions, not yet designed in the GDD. Minor visual fixes live in the game repo's `docs/polish-backlog.md`.

## Flashpoint battles: Grandia 3-style, hands-on

- **What:** the story flashpoints and officer crisis fights (Chimera, Ambermaw, Crownstone, rare officer fights) are played by hand. Routine hunts stay automatic.
- **The system:** a Grandia-style timeline. Every fighter has a marker moving along a shared timeline; when one of yours reaches the command point, time pauses and you choose an action. Hits that land while an enemy is casting can cancel or knock back its turn.
- **Grandia 3's movement (owner's pitch):** fighters **move around the field** during the fight (running to targets, repositioning), not standing still in rows.
- **Fits with:** the battle stage, skill meter, hit-stop, skill cinematics and officer battle sets.
- **Cost:** a second battle mode (interface, enemy design, balance). Do it once, before the Chapter 2 flashpoints.

## Weather system (Eurydica and Frontier)

- **What:** a reusable weather system, built once and used in both Eurydica and the Frontier (owner: it's a system, so it isn't wasted on the short Eurydica act).
- **Ideas:** clear, overcast, rain, fog, maybe snow in the Frontier highlands. Each one changes sky colour, sun strength and haze. Rain falls outdoors and streaks on windows. Interiors get greyer light through the windows (the hall's window setup already supports this). Weather can follow the Guild clock and change by day.
- **Later hooks:** weather could affect hunts or scouting (fog lowers discovery, rain slows travel). That's a design question for when it's built.

## Standing orders for hunts (proposal, owner discussing)

Keep hunts automatic, and give each adventurer a few simple rules that the existing combat engine follows. See the discussion of 2026-10-01; the open question is how signature skills fit (below). It should stay much simpler than Unicorn Overlord's or Pillars of Eternity's systems.

## Art follow-ups

- Codex: redo the `tankard` and `seal_letter` small items (they failed the glance test).
- Redo the Tier 2 annex and the tavern in the Guild hall's style (3D furniture, fantasy plants, windows, bigger rooms).
