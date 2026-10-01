# Consumables and the Research Department (proposal)

**Status:** decisions made by the owner on 2026-09-29 (§6). Eurydica's tier 1 is now in GDD 6.6a and enhancement is removed (GDD 12.3). **The full tier 1–5 system and the Research Department are implemented after the sprints reach the Frontier** (owner, 2026-09-29).

## 1. Intent (owner, 2026-09-29)

- Consumables are a **heavy requirement for expeditions**, as in Monster Hunter World. They are never mandatory, but an expedition without them has a **clearly lower success chance**. The risk forecast (GDD 9.3, FGC_07 §11) makes that visible before dispatch.
- Adventurer power comes from four sources: the **stat ladder** (the four tracks, GDD 6.2c), **skills**, **equipment**, and a **consumable boost** for one expedition. There is no other permanent stat source (see §5, Refinement and enhancement).
- **Tiers 1–5.** Eurydica has **tier 1 only**. Tiers 2–5 belong to the Frontier.
- **Region materials:** recipes use the local region's monster parts (the region tag rule, GDD 16a.1). Eurydica tier-1 items use Eurydica parts; Frontier tiers use Frontier parts. No Eurydica material is needed for a Frontier recipe.
- **The Research Department** (Frontier) makes consumables. Fulker's Workshop stays with gear and Reworking.
- **Reference:** Monster Hunter World's consumables (monsterhunterwiki.org, MHWorld/Items/Consumables), adapted to FGC's auto-battle, where nobody presses a button mid-fight.

## 2. How consumables work in an auto-battle

- **Packed in the backpack** at preparation, one cell each (1×1), so they compete with gear for space. This is the "heavy" trade-off: the F/E 4×4 pack can't hold everything.
- **Three trigger kinds:**
  - **On departure:** applied once as the expedition leaves (lure, map, drinks);
  - **Whole expedition:** a buff lasting until the party returns (the Demondrug line);
  - **Automatic in combat:** fires on a rule, like today's potion at ≤40% HP.
- **Consumed when used,** never refunded by a recall. Unused items come home.
- **The risk forecast** includes packed consumables, so the player sees, for example, "High → Moderate" when potions are added.

## 3. Families (MHW → FGC)

| Family | MHW examples | FGC version | Trigger | Tier 1 (Eurydica) |
|---|---|---|---|---|
| **Healing** | Potion → Mega → Max → Ancient | Heals a fighter by a share of max HP | Automatic: ≤40% HP after a hit, one per action | **Potion** (exists: 30%) |
| **Attack boost** | Demondrug → Mega Demondrug, Might Seed | +ATK% for the whole expedition | Whole expedition | **Demondrug** (replaces Refinement, §5) |
| **Defence boost** | Armorskin → Mega Armorskin, Adamant Seed | +DEF% for the whole expedition | Whole expedition | **Armorskin** |
| **Status cure** | Antidote, Herbal Medicine, Nulberry | Removes a status from monster skills (ATK/DEF/SPD down, slow) | Automatic: when a status lands | — (Frontier, tier 2+) |
| **Party powder** | Lifepowder, Demon Powder, Hardshell Powder | Heals or buffs the whole party once | Automatic: when two or more are ≤50% | — (tier 3+) |
| **Endurance** | Energy Drink, Dash Juice, Well-done Steak | Softens Red Fatigue for one expedition | On departure | — (tier 2+) |
| **Environment** | Cool Drink, Hot Drink | Cancels a Frontier region hazard | On departure | — (Frontier regions with hazards) |
| **Combat items** | Flash Pod, Barrel Bomb, traps | Stun an enemy at fight start, or fixed damage | Automatic: first fight of the expedition, or on a boss | — (tier 2+) |
| **Hunting tools** | (FGC's own) | Lure: +target group chance; Scout Map: +find chance | On departure | **Hunting Lure, Scout Map** (exist) |

Charms (MHW's carried passive bonuses) are **not** consumables here; that role belongs to accessories (equipment).

**Tier scaling (starting values to tune):** each tier raises the effect, for example Potion 30 / 40 / 50 / 65 / 80% of max HP, or Demondrug +8 / +12 / +16 / +20 / +25% ATK. Recipes move to rarer materials as tiers rise.

## 4. Where they come from

**In Eurydica (tier 1 only):**
- Bought at the counters that exist today: Elsie's before Commerce, then Valerie's Trading Post (Potion 20 G, Lure 25 G, Scout Map 20 G; Demondrug and Armorskin priced when authored). Dr. Wendt's clinic request keeps its weekly potion allotment.
- **No consumable crafting at the Workshop.** The Hunting Lure and Scout Map recipes move to the Research Department (proposal); Fulker keeps gear and Reworking.

**In the Frontier (tiers 1–5):**
- **The Research Department:** a new department with its own staff role (researcher) and stations, opened in a Frontier chapter. It has a work order like Processing and the Workshop (queue, fee, duration, staff rank factor).
- **Research unlocks tiers:** each tier needs a research milestone (for example, studying a species' parts or a Guild Rank), so tier 5 is late Frontier content.
- **Recipes use Frontier monster parts,** with some bought base supplies, never Eurydica parts.
- Which officer leads Research is open: a new Frontier officer, or Liliana extending Information. Owner's call.

## 5. Refinement and enhancement

**Today (GDD 12.2–12.3):**
- *Refinement* is a crafted material (3 Slime Gel + 10 G).
- *Enhancement* spends Refinements, common parts and gold at Fulker's to raise an adventurer's base HP/ATK/DEF **permanently**: +5% per level, capped at 2 levels (+10%) in Eurydica and 5 levels (+25%) in the Frontier.

**The owner's concern:** a permanent stat raise on top of the four tracks risks overpowered adventurers, and the name "Refinement" misleads (it sounds like improving equipment).

**Proposal:**
1. **Remove enhancement.** Permanent power comes only from the tracks, skills and equipment.
2. **Refinement becomes the Demondrug line:** a tier-1 consumable, +ATK% for one expedition.
3. **Elite parts lose their enhancement use** (levels 4–5 needed one). They need a new purpose: higher-tier Frontier gear and consumable recipes, or a premium sale item.
4. **Knock-on edits:** GDD 12.2 (the Refinement row), 12.3 (the whole enhancement section), 5.4 and 12.2a (Workshop jobs: craft and Rework only), 15 (the Workshop screen), the enhancement lock, Codex A's Workshop code and its tests, and the Eurydica caps in 16a.

## 6. Decisions (owner, 2026-09-29)

1. **Enhancement is removed completely** (GDD 12.3).
2. **Demondrug and Armorskin are added to Eurydica's tier 1**, bought like the others (GDD 6.6a).
3. **The Research Department is new, in the Frontier, with a new officer: Minerva Alraun, Chief of Research** (named 2026-09-30; `Characters/Officers/Minerva Alraun/`). Liliana's Information department keeps market forecasts and also handles information verification there.
4. **How heavy:** without consumables a normal party still succeeds, but some come home near 50% HP, especially the front line. A **solo hunt is impossible without a potion and a Demondrug or Armorskin**. This is the M3 tuning target (GDD 6.6a).
