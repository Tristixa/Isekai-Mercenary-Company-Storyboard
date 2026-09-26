# Animation sources (approved 2026-09-26)

These are the video clips to build each animation from. The pipeline extracts the named segment, keys out the magenta background, snaps the frames to the character's grid, applies the costume lock and mouth removal, recolours to the sheet palette, retimes (holding key poses and dropping in-between frames), outlines and packs.

## Walks (all seven: Commander, Tristitia, Elsie, Fulker, Mae, Liliana, Valerie)

| Direction | Source |
|---|---|
| Down | `Walk Down-Front.mp4` |
| Left | `Walk Sideways.mp4` (Elsie: `Walking Sideways.mp4`) |
| Right | the left walk, **mirrored**. This is accepted even where the design is asymmetric, to save credits. |
| Up | `Walk Up-Back.mp4` (Valerie's file is named `Walk Up-Front.mp4`) |

In every walk, skip any stumble and use one clean step cycle.

## Battle

| Animation | Tristitia | Elsie (plain-spear version) |
|---|---|---|
| Battle idle | `Batch 1.1 (Idle, Attack)` | `Batch 1 (Idle, Attack, Skill)` |
| Attack | `Batch 1.1 (Idle, Attack)` | `Batch 1 (Idle, Attack, Skill)` |
| Skill | `Batch 1.2 Skill` (the better motion, even though it is less smooth) | `Batch 1 (Idle, Attack, Skill)` |
| Hurt | `Batch 2` | `Batch 2.1` (in 2.2 the model made her hit instead of getting hit) |
| Guard | `Batch 2` | `Batch 2.2` |
| Victory | `Batch 2` | `Batch 2.2` (2.1 has a third hand) |
| Defeat | `Batch 2` | either; they are the same, so use `Batch 2.2` for consistency with the guard |

Elsie keeps her **plain spear**. The winged "lacquer spear" remake is dropped: dual-wielding with crossed arms made the model duplicate hands and weapons.
