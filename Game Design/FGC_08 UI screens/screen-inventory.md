# FGC UI-HUD screen inventory

Documentation draft • 28 September 2026 • expands GDD §15; does not replace it.

Count convention: **102 inventory entries** includes full screens, overlays, HUD elements, an audio-only city-bell boundary, and explicitly proposed/later entries. **69 shared components**, **26 distinct gaps**. These are not counts of approved new features or new scene files. FGC_07 §12.3 still requires one scene per GDD §15 screen; child entries may be reusable controls within it.

Source authority, highest first:

1. [IMC GDD.md](<D:/Storyboards/Isekai Mercenary Company/Game Design/IMC GDD.md>), current v2.1 with 28 September changes; whole document reviewed, particularly §§2.5–16b. Historical proof/change-log statements do not override current rules.
2. [FGC_07 Implementation Spec](<D:/Storyboards/Isekai Mercenary Company/Game Design/FGC_07_Implementation_Spec.md>), §§04, 07.1, 09, 11–14 (plus save/content references where needed).
3. [Scene Script Format](<D:/Storyboards/Isekai Mercenary Company/Game Design/Scene Script Format.md>), complete format including name-entry cues, talks, barks and ambient lines.
4. [FGC_09 Sprint Plan](<D:/Storyboards/Isekai Mercenary Company/Game Design/FGC_09_Sprint_Plan.md>), approved v0.1; owns sequencing, not rules.
5. All 17 supplied Three Houses screenshots, individually inspected; catalogue below. File names and owner annotations are retained.

No project files are changed and no images are generated. Only layout patterns are adapted. Fire Emblem: Three Houses is the single UI visual reference; Dragon Quest XI contributes only the rule **simple, clean, readable**, not another layout or asset system.

### Rules shared by every entry

- **Read models and commands:** field tags use GDD sections and, where applicable, FGC_07 §07.1 aggregate names. Content, Settings, Saves and world geometry are services/presentation data, not invented simulation aggregates. Every member of a grouped field list inherits its adjacent source tag. Source tables supply all authored row values; the UI must bind those records rather than duplicate tuning.
- **Proposals:** all snake_case action names in this inventory are interface proposals unless explicitly identified as existing FGC_07 names. Navigation, focus, drafts and settings route through presentation/application services; they are not all SimCommands. Actual simulation commits use §07.1, including command ID, expected revision, immutable receipt and atomic resource/state validation. Existing scene-tag commands and `session_result` retain their specified names.
- **Preview/commit:** selection, sorting, tooltips, risk estimates and draft editing never mutate gameplay. Label commits with the actual act: Dispatch, Buy, Hire, Deliver, Build, Pay, Choose permanently. Cancel discards only uncommitted edits; a committed job uses its own cancellation/refund rule. Recall is immediate as specified, with consequences visible at the button. Advisory reserve crossing warns; it does not invent a spending prohibition.
- **Clock/context:** FGC_07 §04 permits an overlay stack with one interactive foreground; GDD §4 prohibits independent stacked pause toggles. Preserve a single pause owner and return context. HUD children do not independently pause and inherit any host pause. Management/dialogue/shop/minigame overlays pause; last close restores prior chosen speed. Selected Pause survives Watch. Only a visible watched fight uses optional ¼ global speed; search/scout never do. Closeout is paused. Sleep/transfer are explicit calendar advances, not live operating simulation.
- **Input:** §13 supplies movement, run, interact/advance, cancel, speed and Ongoing. Generic menu focus, tabs, scrolling, grid controls and a hub shortcut below are **proposed**. Scope inputs to foreground context: speed hotkeys must not type into name fields, run B must not also cancel a menu, and D-pad cannot both navigate a list and change speed. All actions remain reachable as labelled buttons with mouse or controller focus. No hold-to-confirm duration is invented.
- **Lifecycle proposal (G18):** loading shows real pending content/snapshot/receipt state, never fabricated zero stock or reward. Keep drafts on error; authoritative refusal names the exact next requirement. Missing art uses the prescribed name-only/available sprite treatment, never a fake face. Acceptance work in S5 must cover each entry's empty/loading/blocked/error state.
- **Faces:** dialogue waist-length Commander left/current other speaker right; small adventurer/staff slots use their own idle-left pixel sprite in a frame, including battle HUD slots. Officers may use painted crops in small slots and large portrait+guidance on department screens. Important-NPC profiles show full uncropped portrait on left. Eurydica NPCs without portraits show name only; Merchant's supplied negotiation set is the explicit exception. This handoff overrides GDD §9.4's older front-idle bust wording and proof-4 '?' card.
- **Style/layers:** GDD §2.5 tokens and fonts are mandatory: navy/gold panels, parchment/ink cards, blue selected state, text+icon status cues; Marcellus headings, Alegreya Sans text/all lining numbers, Pixelify Sans in-battle names only. FGC_07 §12.2 layers: world0, world labels10, HUD20, screens30, dialogue40, letterbox/fades50. Debug90 is developer-only and outside this player inventory. The spec's 140px dialogue box is retained as a source baseline; scale behavior is G21.
- **Scope gaps:** G02/G18/G21 are shared UX specification gaps, not missing gameplay balance. Individual entries cite additional gap IDs; repeated references count once. G10 is a live source conflict. FGC_07 §06.7's old bond/reservation/Morale/perk issues were explicitly resolved by its review note and current GDD; they are not reopened here.

### Inspected Three Houses reference catalogue

Only the game frame is a reference. Browser/gallery navigation, copy buttons and analysis sidebars in the screenshots are not FGC UI.

| Key | Exact screenshot file | Observed layout pattern |
|---|---|---|
| R01 | 3D Battle UI.png | compact combat identity and HP plates at the edges; floating damage over the action. FGC retains its own party-bottom/enemy-top contract. |
| R02 | Adventurer Stat.png | compact identity card left, selectable equipment list right, numeric comparison rows beneath. |
| R03 | Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png | tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. |
| R04 | Maybe For Main Menu.png | vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule. |
| R05 | Menu.png | centred settings list with tabs above, left/right value selectors, help strip below. |
| R06 | Mini Game Result.png | activity header, prominent grade band, separate outcome bands, progress rows below. |
| R07 | Modal Info 1.png | small centred parchment information card over the retained world. |
| R08 | Modal Info 2.png | centred item card with icon/title, numeric rows and explanatory text. |
| R09 | Notification on the Left.png | compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. |
| R10 | Player Menu.png | right-side folio menu, world still visible left, purse/header above and hints below. |
| R11 | Region Map.png | parchment map left, selectable destination list upper right, contextual detail/reward card lower right. |
| R12 | Request, Rhea Replaced With Tristitia.png | two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. |
| R13 | Request-Contract Reward.png | separate horizontal reward bands over the retained scene, one outcome per row. |
| R14 | Screenshot 2026-09-28 135745.png | bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. |
| R15 | Skill Use.png | brief horizontal skill-name banner over the action; no imported skill text or artwork. |
| R16 | Staff Detail.png | identity above a short list left, large selected-detail card right, help and input hints at the bottom. |
| R17 | Staff Roster.png | wide roster list left with small face slots and progress rows; compact selected-person identity and details right. |

## A. Navigation map

The tree is a reachability map, not an instruction to place all officers in one room. Walking to the named room/corner and the permitted hub shortcut instantiate the same management screen with different return contexts. No shortcut grants physical relocation or bypasses an HQ-only action. Off-map shortcut availability is G02.

```text
Launch → validation → Title
  ├─ Profile select → New Game → authored opening scenes
  │    ├─ Commander name cue → name entry → same scene
  │    └─ Guild-name cue → Guild-name entry → same scene
  ├─ Continue / Load / backup recovery → saved context, paused
  └─ Settings → Difficulty (active campaign: next 07:00)
World / HQ / city (HUD; clock follows chosen speed)
  ├─ Nearby interaction → talk topics / dialogue / ambient line
  │    ├─ authored choices / narration / cues → next node or world
  │    ├─ request offer → notice → Request Board (not auto-accepted)
  │    └─ proposed backlog / auto control
  ├─ Proximity → non-pausing bark; clock time → outdoor city bell only
  ├─ Menu/hub shortcut → same service screens, plus profile/projects/journal/save/settings
  ├─ Walk to Commander's Office / Tristitia
  │    └─ Request Board → deliveries / optional contracts / flashpoints
  │         ├─ client profile; reward receipt
  │         ├─ payroll / Rank / debt & rescue / chapter readiness
  │         └─ later Frontier transfer quote → checkpoints / payroll → arrival
  ├─ Walk to Adventurer Office / Elsie
  │    ├─ Roster → adventurer profile → Progression / Rest / Backpack
  │    ├─ Recruitment / Former staff → hire/rehire
  │    └─ New Expedition → Region Map → Area Detail → target/scout/contract
  │         └─ Preparation → two templates / backpack draft → Dispatch
  ├─ Tab / Y, or Office Ongoing → active list / returned-today history
  │    └─ Watch/View/Follow → field search / scout / battle
  │         ├─ discovery notices, combat HUD, labels, skill banner
  │         └─ Leave → previous navigation context; Recall → immediate return
  ├─ Walk to Processing / Mae → work order → corpse/job → Cutting Chart
  ├─ Walk to Workshop / Fulker → recipes / enhancement / Reworking mixed order → Fitting
  ├─ Walk to Information / Liliana → forecasts / rumours / source → Cross-check
  ├─ Walk to Commerce / Valerie → listings / supply counter / daily order → Counter-offer
  ├─ Elsie → Expedition Planning; each session → its own result → caller/safe cutoff
  ├─ Each department → officer profile → friendship scenes / Bond5 permanent choice
  ├─ Department staff roster → staff profile / promotion / Recruitment
  ├─ Storage detail → production / request / listing / any-trader sale
  ├─ HQ building map / expansion yard → quote → Build / cancellation
  ├─ Meal venue → solo/shared meal; Commander profile → personal activity routes / later rank-3 abilities
  └─ HUD/source/project alerts → relevant object → Back to initiating context
20:00 safe cutoff → Resolution → Day Summary (weekly Payroll when due)
  └─ Night world → talks / meals / desk reports / city walk
       ├─ later Frontier NPC → romance / gifts / date / relationship scenes
       └─ bed after20:00 or automatic01:00 → Sleep → Morning → world07:00 paused
```

Back restores the previous screen, selected object, scroll/focus and draft where valid (presentation proposal), not a hard-coded Office landing page. Mandatory scenes, due payroll and committed sleep/transfer follow their safe handoff; Back does not undo a committed transaction. GDD takes precedence over FGC_07's simplified `field → world` row (G11).

| Screen / element | Entry points | Where Back returns |
|---|---|---|
| [ui_boot_report](#ui_boot_report) | Launch/content validation failure | Stop at boot on validation failure; successful boot opens Title |
| [ui_title](#ui_title) | Successful boot; return-to-title action | Application exit; loaded game resumes paused |
| [ui_profile_select](#ui_profile_select) | Title New Game/Load/Continue when a profile is needed | Title, preserving selected menu item |
| [ui_new_game](#ui_new_game) | Title → profile select | Profile select before starting; after Start, opening scene |
| [ui_name_entry](#ui_name_entry) | Authored [name-entry] cue | Suspended scene resumes after accepted name; Back policy unresolved |
| [ui_guild_name_entry](#ui_guild_name_entry) | Authored [guild-name-entry] cue | Suspended scene after confirmed name; Back policy unresolved |
| [ui_world_hud](#ui_world_hud) | World exploration; closing management; night/morning handoff | Persistent host; menu children return to same position/context |
| [ui_top_bar](#ui_top_bar) | World, field and applicable screen shell | Host remains |
| [ui_objectives](#ui_objectives) | Story objective changes, project/request events | Click detail then Back to originating host |
| [ui_alerts](#ui_alerts) | Sim events, including unwatched variants | Source detail Back returns to feed/previous host |
| [ui_minimap](#ui_minimap) | World HUD | Persistent; hidden while dialogue is open |
| [ui_interact_prompt](#ui_interact_prompt) | Approaching an interactable actor, bed, desk or service | World after interaction ends |
| [ui_speed_controls](#ui_speed_controls) | Top bar in world/field | Host remains |
| [ui_battle_pace](#ui_battle_pace) | Top bar; setting applies to watched fights in S6 | Host remains |
| [ui_hub](#ui_hub) | World HUD menu; permitted field/menu contexts | Exact previous world/field location and focus |
| [ui_dialogue](#ui_dialogue) | Story scene, talk, working-session introduction/result | Caller at safe end; next authored scene for [goto] |
| [ui_talk_menu](#ui_talk_menu) | Interact with officer/NPC; dialogue returns from {topic} branch | Automatic Leave returns to previous world/service context |
| [ui_barks](#ui_barks) | Proximity to authored bark NPC, once per day | World stays controllable |
| [ui_ambient](#ui_ambient) | Interact with ambient NPC in matching time band | Same world position |
| [ui_choices](#ui_choices) | Authored choice node | Chosen branch, then authored rejoin; talk topics loop |
| [ui_narration](#ui_narration) | Authored > narration node | Next scene node |
| [ui_dialogue_history](#ui_dialogue_history) | Proposed Log button on dialogue | Exact current line/choice without replay |
| [ui_auto_advance](#ui_auto_advance) | Proposed dialogue button | Same dialogue; turning off restores manual advance |
| [ui_scene_staging](#ui_scene_staging) | Authored cues; emotes above sprites | Scene/camera handoff; no independent Back |
| [ui_commander_profile](#ui_commander_profile) | Hub; Commander desk/person menu | Exact caller |
| [ui_hunger](#ui_hunger) | World HUD; Commander profile; meal screen | Host remains; meal detail returns to caller |
| [ui_meals](#ui_meals) | HQ table, tavern, food stall, later Frontier cookhouse | Same venue/talk context |
| [ui_personal_activities](#ui_personal_activities) | Hub; desk; officer evening interactions | World/caller; selected activity routes to its own view |
| [ui_bonds](#ui_bonds) | Hub proposed Bonds route; officer profile | Caller/profile |
| [ui_officer_profile](#ui_officer_profile) | Owning department header; Bonds overview | Owning department or Bonds at previous selection |
| [ui_bond_perk_choice](#ui_bond_perk_choice) | Eligible officer profile/personal story beat | Profile; Cancel leaves choice uncommitted |
| [ui_important_npc_profile](#ui_important_npc_profile) | Request client link; journal; later romance/buyer link | Exact originating request/journal context |
| [ui_romance](#ui_romance) | Frontier NPC talk/profile; later personal-activities route | NPC/caller; authored scene on commit |
| [ui_adventurer_office](#ui_adventurer_office) | Walk to Elsie/Adventurer Office; hub shortcut | World/talk/hub caller |
| [ui_roster](#ui_roster) | Adventurer Office; hub; prep member picker | Exact caller; picker returns to prep draft |
| [ui_adventurer_profile](#ui_adventurer_profile) | Roster, prep, recruitment, returned-operation member | Caller with selected person preserved |
| [ui_progression](#ui_progression) | Roster/profile; Adventurer Office | Caller; Cancel discards complete build draft |
| [ui_rest_orders](#ui_rest_orders) | Office/Roster/profile; morning readiness link | Caller |
| [ui_backpack](#ui_backpack) | Profile; Preparation equipment button | Profile after save, or unchanged prep draft parent |
| [ui_staff_roster](#ui_staff_roster) | Department staff route; Recruitment; payroll member link | Caller department/recruitment/payroll |
| [ui_staff_profile](#ui_staff_profile) | Staff roster, production worker row, Recruitment/payroll | Exact caller |
| [ui_recruitment](#ui_recruitment) | Office/department; roster empty state; HQ waiting recruit; rescue link | Caller |
| [ui_region_map](#ui_region_map) | New Expedition; hub; material-source link | Caller; detail returns to same area selection |
| [ui_area_detail](#ui_area_detail) | Region map; Information; known source links | Exact caller/map selection |
| [ui_hunt_targets](#ui_hunt_targets) | Area detail Hunt; rare alert | Area detail/source alert |
| [ui_preparation](#ui_preparation) | Hunt target; Scout; Contracts; Flashpoint | Exact source with uncommitted edits discarded on Cancel |
| [ui_prep_templates](#ui_prep_templates) | Preparation templates button | Same prep draft |
| [ui_ongoing](#ui_ongoing) | Tab/Y from world; Office; hub; operation alert | Exact caller; Watch suspends this context for later return |
| [ui_field_view](#ui_field_view) | Ongoing Watch/View/Follow; operation alert via Ongoing | Previous navigation context per GDD; world fallback when no caller |
| [ui_scout_field](#ui_scout_field) | Field Follow on active scout | Field/Ongoing caller; no simulation change |
| [ui_battle_hud](#ui_battle_hud) | Live field encounter | Search resumes after victory; field exit uses caller |
| [ui_battle_labels](#ui_battle_labels) | Combat events in watched field | Automatic end of visual event; no navigation |
| [ui_discovery_notice](#ui_discovery_notice) | Scout discovery or milestone event | Field; inspect then return to same live context |
| [ui_request_board](#ui_request_board) | Commander's Office/Tristitia; hub; client offer; request notice | Exact caller; client-turn-in returns to interaction |
| [ui_request_notice](#ui_request_notice) | [request:] cue or offer-branch {request:} tag | Current safe dialogue/world context; details return here |
| [ui_contracts](#ui_contracts) | Request Board Contracts tab; Area Detail; Office | Caller with selected contract |
| [ui_flashpoint](#ui_flashpoint) | Office/Board/story offer; chapter route | Caller or explicit authored scene; retry returns to offer |
| [ui_reward_receipt](#ui_reward_receipt) | Committed delivery/victory/reward event | Request/caller; later result history |
| [ui_processing](#ui_processing) | Walk to Processing corner/room; hub; corpse result/source link | Previous navigation context |
| [ui_workshop](#ui_workshop) | Walk to Fulker/Workshop corner; hub; recipe source | Caller |
| [ui_recipe_detail](#ui_recipe_detail) | Workshop recipe list; Gerd/Elsie early preview; material/project links | Exact caller, including pre-Workshop source |
| [ui_enhancement](#ui_enhancement) | Workshop Enhance; adventurer profile | Workshop/profile caller |
| [ui_reworking](#ui_reworking) | Workshop Reworking; material detail | Workshop/material caller |
| [ui_information](#ui_information) | Information Office/corner; hub; market forecast link | Caller |
| [ui_commerce](#ui_commerce) | Commerce/Trading Post; hub; inventory sell link | Caller |
| [ui_walk_up_sale](#ui_walk_up_sale) | Any-trader interaction at any base; Commerce; stock link | Counter/Commerce/caller |
| [ui_consumable_counter](#ui_consumable_counter) | Elsie's Office; Commerce potion counter; clinic benefit route | Same counter/office |
| [ui_storage](#ui_storage) | Hub proposed storage route; production/Commerce/request item picker | Caller with selection/draft preserved |
| [ui_hq_building_map](#ui_hq_building_map) | Walk to room/expansion yard; hub HQ route; Annex preview | Same world/room/hub context |
| [ui_payroll](#ui_payroll) | Weekly closeout; Office preview; transfer payroll checkpoint | Closeout Summary/transfer checkpoint; preview returns to Office |
| [ui_rank](#ui_rank) | Top bar Rank; Office; hub | Caller |
| [ui_debt_rescue](#ui_debt_rescue) | Payroll aftermath/Day Summary rescue state; Office debt detail | Caller; rehire receipt if rescue applied |
| [ui_resolution](#ui_resolution) | Cutoff after safe dialogue end; returned-operation history detail | Continue to Day Summary flow; history Back to caller |
| [ui_day_summary](#ui_day_summary) | Resolution; desk archived recap route | Proceed to night after due payroll; archived recap Back to desk |
| [ui_projects](#ui_projects) | HUD/project source/recipe/build card; Summary; hub | Exact source caller |
| [ui_reports_journal](#ui_reports_journal) | Commander desk at night; proposed hub Journal; contact/history link | Desk/world/hub caller |
| [ui_night](#ui_night) | Day Summary completion | World night; bed/01:00 leads to Sleep |
| [ui_sleep](#ui_sleep) | Bed after 20:00; automatic at 01:00 | Manual Cancel returns to night; committed transition to Morning |
| [ui_morning](#ui_morning) | Sleep/night jump and new-day autosave | World at 07:00 paused; resume only through speed controls |
| [ui_city_bell](#ui_city_bell) | 09:00/12:00/15:00/18:00 while outdoors in Eurydica | World unchanged |
| [ui_chapter_transition](#ui_chapter_transition) | Player elects Chapter 1 conclusion; later Chapter 2 transition beat | Cancel returns to caller; commit runs authored transition scene |
| [ui_frontier_transfer](#ui_frontier_transfer) | Chapter2 transition beat; Office relocation route | Cancel before transfer to readiness/Office; confirmed transfer to checkpoints/Arrival |
| [ui_transfer_checkpoint](#ui_transfer_checkpoint) | Confirmed transfer; crossed payroll boundary; arrival | Payroll returns to transfer; Arrival continues to world paused at arrival time |
| [ui_save](#ui_save) | Hub/settings; world/management/combat; transfer checkpoint | Exact caller after save; simulation stays paused while overlay open |
| [ui_load](#ui_load) | Title/profile; hub Save/Load; save-error recovery | Cancel to caller; successful load to saved context paused |
| [ui_settings](#ui_settings) | Title; hub; save/load family | Exact caller; restore previous chosen speed when last overlay closes |
| [ui_difficulty](#ui_difficulty) | New Game setup; Settings | Caller; active campaign change pending until next 07:00 |
| [ui_session_offer](#ui_session_offer) | Owning department/talk; Commander skill link | Owning department/talk; completed play goes to its result |
| [ui_expedition_planning_play](#ui_expedition_planning_play) | ui_session_offer at Elsie | Own result screen on completion; abort return policy G09 |
| [ui_expedition_planning_result](#ui_expedition_planning_result) | Completed Expedition Planning play and authoritative session_result receipt | Elsie's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution |
| [ui_counter_offer_play](#ui_counter_offer_play) | ui_session_offer at Valerie | Own result screen on completion; abort return policy G09 |
| [ui_counter_offer_result](#ui_counter_offer_result) | Completed Counter-offer play and authoritative session_result receipt | Valerie's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution |
| [ui_cross_check_play](#ui_cross_check_play) | ui_session_offer at Liliana | Own result screen on completion; abort return policy G09 |
| [ui_cross_check_result](#ui_cross_check_result) | Completed Cross-check play and authoritative session_result receipt | Liliana's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution |
| [ui_cutting_chart_play](#ui_cutting_chart_play) | ui_session_offer at Mae | Own result screen on completion; abort return policy G09 |
| [ui_cutting_chart_result](#ui_cutting_chart_result) | Completed Cutting Chart play and authoritative session_result receipt | Mae's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution |
| [ui_fitting_play](#ui_fitting_play) | ui_session_offer at Fulker | Own result screen on completion; abort return policy G09 |
| [ui_fitting_result](#ui_fitting_result) | Completed Fitting play and authoritative session_result receipt | Fulker's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution |
| [ui_confirm](#ui_confirm) | A labelled action needing cost, destructive change or permanent-choice review | Exact caller with draft and focus preserved; committed action returns receipt |
| [ui_info_help](#ui_info_help) | Field/stat/item/rule help; authored dispatch and contract explanations | Exact caller; tutorial advances only its authored acknowledgement |
| [ui_error_notice](#ui_error_notice) | Failed command, missing content or save I/O; boot failures use ui_boot_report | Caller with uncommitted draft preserved; retry only after revalidation |
| [ui_commander_rank_actions](#ui_commander_rank_actions) | Commander profile rank-3 unlock; Preparation; Commerce/negotiation counter | Exact profile/prep/counter caller |

### GDD §15 contract coverage

All 24 source-table rows are expanded below; additional entries do not replace them.

| GDD §15 row | Inventory entries |
|---|---|
| Top bar | [ui_top_bar](#ui_top_bar), [ui_speed_controls](#ui_speed_controls), [ui_battle_pace](#ui_battle_pace) |
| Adventurer Office | [ui_adventurer_office](#ui_adventurer_office) |
| Roster | [ui_roster](#ui_roster), [ui_adventurer_profile](#ui_adventurer_profile) |
| Progression | [ui_progression](#ui_progression) |
| Region Map and Area Detail | [ui_region_map](#ui_region_map), [ui_area_detail](#ui_area_detail) |
| Hunt target cards | [ui_hunt_targets](#ui_hunt_targets) |
| Preparation | [ui_preparation](#ui_preparation), [ui_prep_templates](#ui_prep_templates), [ui_backpack](#ui_backpack) |
| Ongoing Expeditions | [ui_ongoing](#ui_ongoing) |
| Field view | [ui_field_view](#ui_field_view), [ui_scout_field](#ui_scout_field), [ui_battle_hud](#ui_battle_hud), [ui_battle_labels](#ui_battle_labels), [ui_discovery_notice](#ui_discovery_notice) |
| Alerts | [ui_alerts](#ui_alerts) |
| HQ / Building Map | [ui_hq_building_map](#ui_hq_building_map) |
| Request Board | [ui_request_board](#ui_request_board), [ui_request_notice](#ui_request_notice) |
| Processing | [ui_processing](#ui_processing) |
| Workshop | [ui_workshop](#ui_workshop), [ui_recipe_detail](#ui_recipe_detail), [ui_enhancement](#ui_enhancement), [ui_reworking](#ui_reworking) |
| Information | [ui_information](#ui_information) |
| Commerce | [ui_commerce](#ui_commerce), [ui_walk_up_sale](#ui_walk_up_sale) |
| Recruitment | [ui_recruitment](#ui_recruitment), [ui_staff_roster](#ui_staff_roster), [ui_staff_profile](#ui_staff_profile) |
| Payroll | [ui_payroll](#ui_payroll) |
| Rank | [ui_rank](#ui_rank) |
| Flashpoint | [ui_flashpoint](#ui_flashpoint) |
| 20:00 Resolution | [ui_resolution](#ui_resolution) |
| Day Summary | [ui_day_summary](#ui_day_summary) |
| Frontier transfer | [ui_frontier_transfer](#ui_frontier_transfer), [ui_transfer_checkpoint](#ui_transfer_checkpoint) |
| Save/load/settings | [ui_save](#ui_save), [ui_load](#ui_load), [ui_settings](#ui_settings), [ui_difficulty](#ui_difficulty) |

## B. Screen, overlay and HUD entries

<a id="ui_boot_report"></a>

### Boot validation report

**ID**: `ui_boot_report`

**Name**: Boot validation report

**Owner officer**: none

**GDD refs**: §16, §16b; FGC_07 §04/§06

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Launch/content validation failure → Stop at boot on validation failure; successful boot opens Title.

**Clock**: No campaign simulation in boot/title/profile flow (FGC_07 §04); no battle pace.

**Shows**: Validation findings and content identifiers [§16; FGC_07 §06, Content service]; build/schema/content revision [§16b; Saves/Content].

**Actions**: Retry validation → `retry_boot_validation` (application proposal); exit → `quit_application` (application proposal). Never start an invalid campaign.

**States**: Empty — No errors: proceed to Title. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Content invalid: identify the failing record and required correction; no Continue into campaign. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G23 — Boot validation failure/report and save corruption UI need player-facing diagnostics and recovery copy; integrity mechanics exist, diagnostic wording does not. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_title"></a>

### Title

**ID**: `ui_title`

**Name**: Title

**Owner officer**: none

**GDD refs**: §16b; FGC_07 §04

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Successful boot; return-to-title action → Application exit; loaded game resumes paused.

**Clock**: No campaign simulation in boot/title/profile flow (FGC_07 §04); no battle pace.

**Shows**: Frontier Guild Chronicle title [§1]; Continue/New Game/Load/Settings [FGC_07 §04; application]; selected campaign/save availability [§16b; Saves].

**Actions**: Continue → `continue_campaign`; New Game → `open_new_game`; Load → `open_load`; Settings → `open_settings` (application proposals). Loading/replacing current progress uses a labelled Load confirmation.

**States**: Empty — No saves: New Game remains available. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Continue requires a valid selected save; show Load/recovery route. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G05 — Starting New Game flow beyond profile/scene handoff is undefined: title art, default save selection, profile replacement/deletion policy and initial difficulty placement. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_profile_select"></a>

### Campaign profile select

**ID**: `ui_profile_select`

**Name**: Campaign profile select

**Owner officer**: none

**GDD refs**: §16b; FGC_07 §04

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Title New Game/Load/Continue when a profile is needed → Title, preserving selected menu item.

**Clock**: No campaign simulation in boot/title/profile flow (FGC_07 §04); no battle pace.

**Shows**: Three profile positions, occupied/empty state, campaign identity and available saves [§16b; Saves; commander/guild identity].

**Actions**: Select → `select_profile`; create in empty profile → `create_profile` (application proposals). Selection only previews; occupied-profile replacement is not silently committed.

**States**: Empty — Empty profile: offer New Game. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unreadable profile: offer last-good recovery through Load; do not erase it. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G05 — Starting New Game flow beyond profile/scene handoff is undefined: title art, default save selection, profile replacement/deletion policy and initial difficulty placement. G23 — Boot validation failure/report and save corruption UI need player-facing diagnostics and recovery copy; integrity mechanics exist, diagnostic wording does not. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_new_game"></a>

### New Game setup

**ID**: `ui_new_game`

**Name**: New Game setup

**Owner officer**: none

**GDD refs**: §1, §14, §16b; FGC_07 §04

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Title → profile select → Profile select before starting; after Start, opening scene.

**Clock**: No campaign simulation in boot/title/profile flow (FGC_07 §04); no battle pace.

**Shows**: Selected profile [§16b; Saves]; Standard/Relaxed description [§16b; difficulty]; opening Chapter 1 scene destination [§14; story].

**Actions**: Preview difficulty → `preview_new_campaign`; labelled Start → `start_new_campaign`; Cancel → `close_new_game` (application proposals). No personality quiz or extra rule inferred from other files.

**States**: Empty — Unused profile ready for setup. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Occupied destination requires explicit safe profile policy (G05); absent opening scene requires authored content. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G05 — Starting New Game flow beyond profile/scene handoff is undefined: title art, default save selection, profile replacement/deletion policy and initial difficulty placement. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_name_entry"></a>

### Commander name entry

**ID**: `ui_name_entry`

**Name**: Commander name entry

**Owner officer**: none

**GDD refs**: §2.6, §5a; Scene Format §3 [name-entry]

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Authored [name-entry] cue → Suspended scene resumes after accepted name; Back policy unresolved.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Editable Commander name and preview of <name> replacement [§5a; commander; Scene Format §2/§3].

**Actions**: Type/edit → `edit_name_draft` (UI); labelled Confirm name → `set_commander_name` (proposed). Preview never updates saved identity.

**States**: Empty — Empty draft: no invented default. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Name must pass the eventual authored validation contract; show its exact reason, not guessed limits. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Commander waist-length portrait only if part of the invoking dialogue; no extra face slot.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots.

**Input**: Text keyboard entry; proposed platform on-screen keyboard for gamepad, A selects Confirm, B follows cue cancel policy; text capture suppresses gameplay hotkeys.

**Gaps**: G01 — Name-entry validation is undefined: defaults, length, accepted characters, localisation, renaming, and whether Back can leave a required cue. G19 — Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_guild_name_entry"></a>

### Guild-name entry

**ID**: `ui_guild_name_entry`

**Name**: Guild-name entry

**Owner officer**: none

**GDD refs**: §2.6, §5.1; Scene Format §3 [guild-name-entry]

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Authored [guild-name-entry] cue → Suspended scene after confirmed name; Back policy unresolved.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Editable Guild name and <Guild-name> substitution preview [§5.1; guild; Scene Format §2/§3].

**Actions**: Edit → `edit_guild_name_draft` (UI); labelled Confirm Guild name → `set_guild_name` (proposed). No save mutation before commit.

**States**: Empty — Empty draft: no invented default. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Apply only the approved name policy; G01 records missing constraints. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Invoking dialogue retains waist-length speaker portraits; the input card has no face.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots.

**Input**: Keyboard text; proposed gamepad on-screen keyboard; A confirms, B follows authored cue policy; suppress global hotkeys during entry.

**Gaps**: G01 — Name-entry validation is undefined: defaults, length, accepted characters, localisation, renaming, and whether Back can leave a required cue. G19 — Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_world_hud"></a>

### World HUD shell

**ID**: `ui_world_hud`

**Name**: World HUD shell

**Owner officer**: none

**GDD refs**: §4, §5.3, §15; FGC_07 §12.2

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: World exploration; closing management; night/morning handoff → Persistent host; menu children return to same position/context.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Top bar, objective/notifications, alerts, minimap, interact prompt, speed and battle-pace chip [§15; FGC_07 §12; clock/guild/story]; Fed/Hungry indicator [§5a.1; commander]. Subentries below specify all fields.

**Actions**: Open menu → `open_hub` (UI proposal); interact → `interact` (presentation routing); Ongoing → `open_ongoing` (§13); no world movement command mutates management state.

**States**: Empty — No objective/alert: leave the world readable. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Hungry: 'Eat a meal to run'; story-locked control follows scene handoff. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No extra portraits; world uses the actual actors.

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: WASD/arrows or ground click; left stick. Hold Shift/B to run, E/Space/Enter/click or A to interact; Tab/Y opens Ongoing; P/1/2/4 or D-pad controls speed (§13).

**Gaps**: G02 — Menu/hub availability away from HQ, direct shortcuts, and controller focus/tab/scroll bindings are not specified by §13. Proposed navigation must not imply teleporting or bypass service gates. G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_top_bar"></a>

### Top bar and 19:00 warning state

**ID**: `ui_top_bar`

**Name**: Top bar and 19:00 warning state

**Owner officer**: none

**GDD refs**: §4, §5.3, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: World, field and applicable screen shell → Host remains.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Day/time [§4; clock]; Guild purse, Reputation, Morale, Guild Rank [§5.3; guild]; orange state from 19:00 [§15; clock]; speed/pace widgets in their own entries.

**Actions**: Inspect stat → `inspect_guild_stat`; Rank link → `open_rank` (UI proposals); no currency changes from inspection.

**States**: Empty — Campaign not loaded: hide campaign values rather than zeros. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — No action blocked by orange alone; dispatch rule remains 20:00 cutoff. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. R10 (Player Menu.png): right-side folio menu, world still visible left, purse/header above and hints below.

**Input**: Proposed mouse hover/click or focused A shows explanation; host §13 controls remain.

**Gaps**: G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_objectives"></a>

### Objective and notification area

**ID**: `ui_objectives`

**Name**: Objective and notification area

**Owner officer**: none

**GDD refs**: §3, §14, §15; FGC_07 §12

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Story objective changes, project/request events → Click detail then Back to originating host.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Current authored objective, including 14:00 return when active [§14; story]; project progress/next action [§3; projects]; event summary/source/time [§15; journal/clock].

**Actions**: Inspect source → `open_objective_source`; inspect project → `open_project` (UI proposals). Reading never completes an objective.

**States**: Empty — No current objective: omit strip. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Missing target object: retain event text and explain unavailable destination; never invent a target. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: Proposed click/focused A opens source; §13 Back returns. Keyboard/gamepad HUD focus binding remains proposed.

**Gaps**: G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_alerts"></a>

### Alerts feed and toast

**ID**: `ui_alerts`

**Name**: Alerts feed and toast

**Owner officer**: none

**GDD refs**: §10.0, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Sim events, including unwatched variants → Source detail Back returns to feed/previous host.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Info/success/warning/critical/rare classification, source event ID, timestamp, source object and message [§15; journal/clock]; unwatched VARIANT notice [§10.0; operations/combat].

**Actions**: Open alert → `open_alert_source`; proposed mark-read → `mark_alert_read` (application/journal command proposal). Deduplicate by event ID; never replay rewards.

**States**: Empty — No alerts: quiet feed. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unavailable historical object: show archived event; no empty disabled link. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: Click or proposed focus+A opens; Esc/right click/B returns from opened detail (§13).

**Gaps**: G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_minimap"></a>

### World minimap

**ID**: `ui_minimap`

**Name**: World minimap

**Owner officer**: none

**GDD refs**: §15; FGC_07 §12.2/§12.4

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: World HUD → Persistent; hidden while dialogue is open.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Local map and Commander position [FGC_07 §12.2; presentation world geometry]; marker set is G03. No discovery or NPC knowledge inferred from map icons.

**Actions**: Passive map; proposed `open_local_map` inspection only if adopted. No teleport action.

**States**: Empty — Location map missing: text location fallback is proposed. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Dialogue open: hide minimap to prevent textbox overlap (§12.4). Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No face markers specified.

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: Passive; any zoom/map shortcut is proposed and undefined (§13 lacks it).

**Gaps**: G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_interact_prompt"></a>

### Interact prompt and world name labels

**ID**: `ui_interact_prompt`

**Name**: Interact prompt and world name labels

**Owner officer**: none

**GDD refs**: §2.6, §5.1; FGC_07 §12/§13

**Milestone/sprint**: M2 / S4 (proposed interaction minimum for walk test); full HUD integration S5.

**Opens from / returns to**: Approaching an interactable actor, bed, desk or service → World after interaction ends.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Interactable name and context action [§5.1/§5a.3; world interaction data]; E/A input hint [FGC_07 §13].

**Actions**: Interact → `interact` routes to the correct scene/service; no remote commit. Walk/run follow §13.

**States**: Empty — No nearby target: hide prompt. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Locked service: name exact story predicate from §14; bed before 20:00: show sleep available after 20:00. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: World actors only; no face badge.

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: WASD/arrows or ground click; left stick. Hold Shift/B to run, E/Space/Enter/click or A to interact; Tab/Y opens Ongoing; P/1/2/4 or D-pad controls speed (§13).

**Gaps**: G02 — Menu/hub availability away from HQ, direct shortcuts, and controller focus/tab/scroll bindings are not specified by §13. Proposed navigation must not imply teleporting or bypass service gates. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_speed_controls"></a>

### Pause and speed controls

**ID**: `ui_speed_controls`

**Name**: Pause and speed controls

**Owner officer**: none

**GDD refs**: §4, §15; FGC_07 §13

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Top bar in world/field → Host remains.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Chosen Pause/1×/2×/4×; effective paused overlay state [§4; clock/application pause owner].

**Actions**: Pause → `set_clock_pause`; 1/2/4 → `set_clock_speed` (proposed command names). Direct labelled actions, no confirmation modal; never override overlay/cutoff pause.

**States**: Empty — No campaign: unavailable. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Paused overlay: explain 'Close the current screen to resume'; no stacked pause toggles. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below.

**Input**: P/1/2/4; gamepad D-pad (§13). Which D-pad direction maps to which speed is not specified; show resolved bindings, not guessed ones.

**Gaps**: G02 — Menu/hub availability away from HQ, direct shortcuts, and controller focus/tab/scroll bindings are not specified by §13. Proposed navigation must not imply teleporting or bypass service gates. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_battle_pace"></a>

### Battle-pace chip

**ID**: `ui_battle_pace`

**Name**: Battle-pace chip

**Owner officer**: none

**GDD refs**: §4, §8.3, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Top bar; setting applies to watched fights in S6 → Host remains.

**Clock**: Live `field` (FGC_07 §04/§11). Preserve chosen Pause; otherwise only a visible fight applies optional ¼ selected global speed. Search/scout do not invoke battle pace.

**Shows**: Battle pace enabled/disabled, active/inactive state, ¼ multiplier of selected global speed [§4; Settings + clock/combat].

**Actions**: Toggle → `set_battle_pace` (Settings proposal); direct labelled setting. No fight-specific simulation acceleration.

**States**: Empty — No watched fight: chip inactive. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Chosen Pause remains Pause; scout/search never activate slowdown. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below.

**Input**: Proposed click/focused A toggle; existing speed keys/D-pad remain §13.

**Gaps**: G02 — Menu/hub availability away from HQ, direct shortcuts, and controller focus/tab/scroll bindings are not specified by §13. Proposed navigation must not imply teleporting or bypass service gates. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_hub"></a>

### Menu / hub shortcut

**ID**: `ui_hub`

**Name**: Menu / hub shortcut

**Owner officer**: none

**GDD refs**: §5.1, §15; FGC_07 §04

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: World HUD menu; permitted field/menu contexts → Exact previous world/field location and focus.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Department routes, Commander, projects/journal, HQ, save/load/settings [§3/§5/§15/§16b; story/guild]; availability predicates [§14; story].

**Actions**: Choose destination → `open_screen` (UI); Back → `close_hub` (UI). Same management views as walking; no instant relocation or bypass of HQ-only edits.

**States**: Empty — No service joined: show authored prerequisites plus already available routes. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Service route states exact joining requirement (§14); shortcut reach is G02. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Optional owner portrait preview only; no gathering all officers in one physical room.

**Three Houses pattern**: R10 (Player Menu.png): right-side folio menu, world still visible left, purse/header above and hints below. R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule.

**Input**: Proposed M/gamepad Menu opens; §13 activation/cancel and proposed focus navigation. Tab/Y remains Ongoing.

**Gaps**: G02 — Menu/hub availability away from HQ, direct shortcuts, and controller focus/tab/scroll bindings are not specified by §13. Proposed navigation must not imply teleporting or bypass service gates. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_dialogue"></a>

### Dialogue view

**ID**: `ui_dialogue`

**Name**: Dialogue view

**Owner officer**: speaking officer, otherwise none

**GDD refs**: §2.6; Scene Format §2–4; FGC_07 §09/§12.4

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Story scene, talk, working-session introduction/result → Caller at safe end; next authored scene for [goto].

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Speaker name, text, expression (Base/Happy/Serious/Sad/Anger/Fear/Surprise/Laugh as authored), <name>/<Guild-name> substitutions, advance cue [§2.6; story/commander/guild; Format §2]; thoughts italic in parentheses, no talk sound [Format §2].

**Actions**: Reveal/advance → `advance_dialogue` (UI); choice routes use ui_choices. No skip-to-reward; checkpoint at scene start/each choice (§09).

**States**: Empty — No next line: finish or chain scene. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unfinished required choice: choose an authored option; control stays locked until handoff. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Waist-length Commander left, current other speaker right; inactive portrait 55% brightness (§12.4). Eurydica NPC without art: name only. No '?' face. Minimap hidden.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots.

**Input**: E/Space/Enter/click or A reveals text then advances (§13/§09). Esc/right click or B leaves only when the scene/talk permits; proposed arrows/stick select choice.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G19 — Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_talk_menu"></a>

### Talk topic menu

**ID**: `ui_talk_menu`

**Name**: Talk topic menu

**Owner officer**: current officer, otherwise none

**GDD refs**: §2.6, §5.4; Scene Format §4a; FGC_07 §09

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Interact with officer/NPC; dialogue returns from {topic} branch → Automatic Leave returns to previous world/service context.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Authored topic labels, heard/read marks [§2.6; story heard flags]; available {after:} topics only [Format §4a].

**Actions**: Topic → `select_talk_topic` (UI) then authored tag commands; Leave → `leave_talk` (UI). Heard flag → `mark_topic_heard` (proposed sim command); reopening does not award a second daily talk.

**States**: Empty — No optional topics: greeting plus Leave. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — {after:} unmet: topic hidden, as format requires; service action separately explains its exact gate. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Same waist-length dialogue slots; NPC without portraits name only.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter/click or A reveals text then advances (§13/§09). Esc/right click or B leaves only when the scene/talk permits; proposed arrows/stick select choice.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_barks"></a>

### Proximity bark bubble

**ID**: `ui_barks`

**Name**: Proximity bark bubble

**Owner officer**: none

**GDD refs**: §2.6; Scene Format §4a; FGC_07 §09/§12

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Proximity to authored bark NPC, once per day → World stays controllable.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Authored bark lines over speaker [§2.6; story/day bark receipt].

**Actions**: No player commit; proximity → `trigger_bark` (presentation proposal) with once-per-day tracking. Continue walking.

**States**: Empty — No eligible bark: hidden. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Already heard today: no replay; do not show a disabled bubble. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No portraits.

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: No direct input; inherits the host's §13 controls. Any optional focus/inspection control is explicitly proposed.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_ambient"></a>

### Ambient NPC line

**ID**: `ui_ambient`

**Name**: Ambient NPC line

**Owner officer**: none

**GDD refs**: §2.6, §5a.3; Scene Format §4a; FGC_07 §09

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Interact with ambient NPC in matching time band → Same world position.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: NPC name and authored line; completed-request variant [§2.6/§11; story/requests]; availability Morning 07–11, Day 11–17, Evening 17–20, Night 20–01 [FGC_07 §09].

**Actions**: Advance → `advance_dialogue`; close → `leave_talk` (UI proposals). No invented rewards from ordinary ambient lines.

**States**: Empty — No NPC in this band: no prompt. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Time-band absence never removes request-owned access to an accepted delivery (§11.1). Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Name only; no face or fake portrait.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: E/Space/Enter/click or A reveals text then advances (§13/§09). Esc/right click or B leaves only when the scene/talk permits; proposed arrows/stick select choice.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_choices"></a>

### Dialogue choice buttons

**ID**: `ui_choices`

**Name**: Dialogue choice buttons

**Owner officer**: none

**GDD refs**: §2.6, §5a.2, §5.4; Scene Format §4; FGC_07 §09

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Authored choice node → Chosen branch, then authored rejoin; talk topics loop.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Numbered authored label, nested branch structure, eligible options [§2.6; story]. Skill/bond/request tags are runtime data; visible tag disclosure is not specified.

**Actions**: Select → `select_scene_choice` (UI proposal); tagged effects use §09 `grant_skill_points`, `add_bond`, `set_flag`, `unlock_request`. Explicit option click is the commit; reveal request is not acceptance; idempotent checkpoint receipts.

**States**: Empty — No eligible options in a required choice: content error. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Condition false: hide branch per format; no invented substitute response. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Retain dialogue waist-length slots, name-only NPC fallback.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below.

**Input**: §13 click/Enter/A selects; proposed arrows/stick moves focus. Number-key choice shortcuts are not assumed because speed keys exist.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_narration"></a>

### Narration box

**ID**: `ui_narration`

**Name**: Narration box

**Owner officer**: none

**GDD refs**: §2.6; Scene Format §2; FGC_07 §12.4

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Authored > narration node → Next scene node.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Authored narration text only [§2.6; story scene data]; consecutive lines advance separately [Format §2].

**Actions**: Reveal/advance → `advance_narration` (UI proposal); no state mutation except authored progression.

**States**: Empty — End of narration: next node. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Missing text: scene-data error, not generated narration. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No speaker name, no portrait; separate centred box.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots.

**Input**: E/Space/Enter/click or A reveals text then advances (§13/§09). Esc/right click or B leaves only when the scene/talk permits; proposed arrows/stick select choice.

**Gaps**: G19 — Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_dialogue_history"></a>

### Dialogue backlog (proposed, not mandated)

**ID**: `ui_dialogue_history`

**Name**: Dialogue backlog (proposed, not mandated)

**Owner officer**: none

**GDD refs**: §2.6; FGC_07 §09; reference only for feature

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Proposed Log button on dialogue → Exact current line/choice without replay.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Proposed previously displayed speaker/text transcript [§2.6; presentation history, persistence undefined]. Neither GDD nor Format implies a mandatory backlog.

**Actions**: Open/close → `open_dialogue_history` / `close_dialogue_history`; scroll → `scroll_history` (UI proposals). No choice replay or second tag execution.

**States**: Empty — No shown lines: empty history. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unseen future lines never available; history scope awaits G04. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Proposed text-only transcript; no additional face assets.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: Proposed L/LB opens Log, wheel/right stick scrolls, Esc/B returns; not existing §13 bindings.

**Gaps**: G04 — The sources specify dialogue advance, not backlog or auto-advance rules. History scope/persistence, auto timing, stop conditions and bindings need a decision. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_auto_advance"></a>

### Dialogue auto-advance control (proposed)

**ID**: `ui_auto_advance`

**Name**: Dialogue auto-advance control (proposed)

**Owner officer**: none

**GDD refs**: §2.6; FGC_07 §09; reference only for feature

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Proposed dialogue button → Same dialogue; turning off restores manual advance.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Proposed on/off indicator [§2.6; application setting]. No authored timing or persisted preference.

**Actions**: Toggle → `set_dialogue_auto` (UI proposal). Proposed stop at choices/name entry; never auto-select or auto-commit.

**States**: Empty — No dialogue: hide. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Awaiting choice/name input: proposed suspended Auto, pending source decision. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No new portrait slots.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots.

**Input**: Proposed click or T/gamepad X toggles; Enter/A still advances; bindings not in §13.

**Gaps**: G04 — The sources specify dialogue advance, not backlog or auto-advance rules. History scope/persistence, auto timing, stop conditions and bindings need a decision. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_scene_staging"></a>

### Scene letterbox, fades and emotes

**ID**: `ui_scene_staging`

**Name**: Scene letterbox, fades and emotes

**Owner officer**: none

**GDD refs**: §2.6; Scene Format §3/§5; FGC_07 §12.2

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Authored cues; emotes above sprites → Scene/camera handoff; no independent Back.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Letterbox/fade presentation [§2.6; scene cues]; exclaim/question/dots/sweat/anger/laugh/heart/music/sleep/idea/sigh icons [Format §5; presentation actors].

**Actions**: No independent commit; `play_scene_cue` (presentation proposal) follows authored cues. Never map a fade to an unrequested time skip.

**States**: Empty — No active cue: hidden. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Missing cue asset: diagnostic/fallback rather than invented pose; idle fallback per spec for missing poses. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No added face slots; actors and existing dialogue portraits retain identity.

**Three Houses pattern**: R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. R15 (Skill Use.png): brief horizontal skill-name banner over the action; no imported skill text or artwork.

**Input**: No direct input; inherits the host's §13 controls. Any optional focus/inspection control is explicitly proposed.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G19 — Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_commander_profile"></a>

### Commander profile

**ID**: `ui_commander_profile`

**Name**: Commander profile

**Owner officer**: none

**GDD refs**: §5a.1–§5a.3

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: Hub; Commander desk/person menu → Exact caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Name [§5a; commander]; Leadership/Negotiation/Insight/Know-how rank 0–5, points, cumulative 10/25/45/70/100 thresholds, Eurydica rank-2 ceiling [§5a.2; commander]; per-rank effects (Leadership Morale losses −10%, Negotiation request/contract gold +4% and market buyers +2%, Insight scout find +2 points and forecast accuracy +2%, Know-how processing/crafting time −3%), rank-3 unlock descriptions/usage [§5a.2; commander]; Fed/Hungry and expiry [§5a.1; commander].

**Actions**: Inspect skill → `inspect_commander_skill`; session route → `open_session_offer`; personal activities → `open_personal_activities` (UI proposals). Skills grow from authored sessions/choices, not a buy-rank button. Rank-3 active ability route → `open_commander_rank_actions` (UI proposal); actual effects have their own entry.

**States**: Empty — No earned points: rank 0 with requirements. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Ranks 3–5: requires Frontier harder sessions; no expedition/fight participation ever. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Commander full uncropped portrait left (profile layout proposal applying important-person rule); no invented biography.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_hunger"></a>

### Fed / Hungry status

**ID**: `ui_hunger`

**Name**: Fed / Hungry status

**Owner officer**: none

**GDD refs**: §5a.1

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: World HUD; Commander profile; meal screen → Host remains; meal detail returns to caller.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Fed until eight Guild hours after meal, or Hungry; Hungry prevents running and has no other penalty [§5a.1; commander/clock].

**Actions**: Inspect → `inspect_hunger`; meal route → `open_meals` (UI proposals, no remote eat implied). Run uses §13 and current status.

**States**: Empty — No loaded Commander: hidden. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Hungry run: 'Eat a meal to run'; walking remains possible. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: Shift/B run in world; proposed click/focused A inspects status; Back returns (§13).

**Gaps**: G06 — Commander personal-activity details are incomplete: HQ kitchen opening predicate, meal duration, shared-meal selection and gift-shop catalogue/prices. Do not invent time costs or stock. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_meals"></a>

### Meal and shared-meal panel

**ID**: `ui_meals`

**Name**: Meal and shared-meal panel

**Owner officer**: none; invited officer if applicable

**GDD refs**: §5a.1, §5.4

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: HQ table, tavern, food stall, later Frontier cookhouse → Same venue/talk context.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Venue/meal price: HQ free once kitchen running, tavern 8G, stall 5G [§5a.1; commander/guild]; Fed expiry preview [§5a.1; commander/clock]; selected present officer and daily talk/meal eligibility, +1 bond shared once [§5.4; bonds].

**Actions**: Choose → `preview_meal` (UI); labelled Eat/Share meal → `eat_meal` (proposed). Show purse/reserve effect; counts as today's talk, never both awards. Cancel discards selection.

**States**: Empty — No companion present: solo meal remains. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — HQ free meal needs running kitchen; paid meal needs displayed price; exact kitchen predicate G06. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Shared officer waist-length in conversation; no invented cook/NPC portrait.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G06 — Commander personal-activity details are incomplete: HQ kitchen opening predicate, meal duration, shared-meal selection and gift-shop catalogue/prices. Do not invent time costs or stock. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_personal_activities"></a>

### Personal activities and evening choices

**ID**: `ui_personal_activities`

**Name**: Personal activities and evening choices

**Owner officer**: none

**GDD refs**: §4.2, §5a.3, §5b

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: Hub; desk; officer evening interactions → World/caller; selected activity routes to its own view.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Meals, evening talk, desk reports, city walks, gift shopping and later dates [§5a.3; commander/story]; operating/night context, adventurer talk available until 21:00, auto-sleep at 01:00 [§4.2/§5a.3; clock].

**Actions**: Choose route → `open_personal_activity` (UI proposal). Walk closes overlay; no points for reports; no unsupported action-point budget.

**States**: Empty — No scheduled activity: retain walk/meals/reports allowed by source. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Dates require Frontier romance content; gifts need authored shop catalogue G06/G07. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Officer crops for selection, waist-length once dialogue opens; NPC without art name-only.

**Three Houses pattern**: R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule. R10 (Player Menu.png): right-side folio menu, world still visible left, purse/header above and hints below.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G06 — Commander personal-activity details are incomplete: HQ kitchen opening predicate, meal duration, shared-meal selection and gift-shop catalogue/prices. Do not invent time costs or stock. G07 — Romance cast, gift likes/dislikes and point values, dates, endings and authored scenes are later Frontier content; no sprint beyond S9 is assigned. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_bonds"></a>

### Officer bonds overview

**ID**: `ui_bonds`

**Name**: Officer bonds overview

**Owner officer**: Tristitia for optional overview; each officer owns their bond

**GDD refs**: §5.4

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Hub proposed Bonds route; officer profile → Caller/profile.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Six officer names, bond 0–5 and cumulative points, next thresholds 5/12/20/30/42, weekly level limit, next scene hint and personal-beat gate [§5.4; bonds/story]; talk/meal/session source receipts [§5.4; bonds].

**Actions**: Inspect officer → `open_officer_profile`; available scene → `play_friendship_scene` (proposed route; authored effects only). No manual purchase of levels.

**States**: Empty — No bond earned: show 0 and both future perks via profile. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Next level: exact remaining points and weekly/story requirement; Bond 5 needs personal beat. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Painted officer crops in rows; no employee sprite substitution.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G22 — Chapter conclusion and permanent Bond 5 choice need final authored warning/confirmation copy; no additional unlock threshold is implied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_officer_profile"></a>

### Officer profile

**ID**: `ui_officer_profile`

**Name**: Officer profile

**Owner officer**: selected officer

**GDD refs**: §5.2, §5.4

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Owning department header; Bonds overview → Owning department or Bonds at previous selection.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Full name/nameplate, department/role [§5.2; content/story]; bond level/points, next scene hint, weekly/story gate, both permanent Bond-5 benefits and costs visible from start, chosen perk if any [§5.4; bonds]. Six authored perk pairs retain exact §5.4 arithmetic.

**Actions**: Inspect perks → `preview_bond_perk`; choose if eligible → `open_bond_perk_choice`; talk → `open_talk` (UI proposals). No mutation on hovering a perk.

**States**: Empty — Not yet met: no invented biography; joined profiles show Bond 0. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Perks show Bond 5 plus personal-story/weekly requirement; no premature grant. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Full uncropped painted portrait left; nameplate Fulker for Sigrid Fulker. Officer header elsewhere may crop.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_bond_perk_choice"></a>

### Bond 5 permanent perk choice

**ID**: `ui_bond_perk_choice`

**Name**: Bond 5 permanent perk choice

**Owner officer**: selected officer

**GDD refs**: §5.4

**Milestone/sprint**: Later: Chapter 2/Frontier content as applicable; no assigned sprint in FGC_09 M1–M3.

**Opens from / returns to**: Eligible officer profile/personal story beat → Profile; Cancel leaves choice uncommitted.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Two exact perk descriptions, benefit/cost and permanence [§5.4; bonds]; current department impacts [§5.4; relevant aggregate]. Tristitia Tight Ship/Open Door; Elsie Hard Drills/Easy Pace; Mae Quick Hands/Careful Cuts; Fulker Rough Patch/Master's Salvage; Liliana Wide Net/Deep Analysis; Valerie Volume Trader/Premium Seller.

**Actions**: Preview → `preview_bond_perk` (UI); labelled Choose permanently → `choose_bond_perk` (proposed sim command). Confirm one selection and trade-off; no respec promised.

**States**: Empty — No perk chosen: compare both. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Requires Bond 5 + personal beat; if already chosen show receipt and selected perk, no alternate commit. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Full officer portrait left; confirmation may use crop.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G22 — Chapter conclusion and permanent Bond 5 choice need final authored warning/confirmation copy; no additional unlock threshold is implied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_important_npc_profile"></a>

### Important NPC profile / contact

**ID**: `ui_important_npc_profile`

**Name**: Important NPC profile / contact

**Owner officer**: none

**GDD refs**: §11.2, §5b, §16a; owner portrait rule

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: Request client link; journal; later romance/buyer link → Exact originating request/journal context.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Authored identity/role, known request/contact aftermath and repeat-order next appearance [§11.2; journal/requests/repeat_orders]; later authored Frontier relationship information [§5b; romance]. No assumed age/height/likes/history fields.

**Actions**: Inspect request → `open_request`; view recorded history → `open_contact_history` (UI proposals). No hidden relationship XP for Eurydica customers.

**States**: Empty — No recorded history: name/known role only. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unwritten Frontier identity/biography: content gap, not placeholder canon. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Important NPC with art: full portrait uncropped on left. Eurydica NPC without portraits: name only; Merchant uses available approved portrait set.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_romance"></a>

### Romance, gifts and date invitation (later)

**ID**: `ui_romance`

**Name**: Romance, gifts and date invitation (later)

**Owner officer**: none

**GDD refs**: §5b

**Milestone/sprint**: Later: Chapter 2/Frontier content as applicable; no assigned sprint in FGC_09 M1–M3.

**Opens from / returns to**: Frontier NPC talk/profile; later personal-activities route → NPC/caller; authored scene on commit.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Authored Frontier partner, bond 0–5, scene progress, weekly limit, Bond-4 personal-beat requirement, current exclusive romance/friendship status [§5b; romance/story]; authored gift/date choices only [§5b; inventory/romance].

**Actions**: Proposed routes `offer_gift`, `invite_date`, `choose_relationship`, `end_relationship`; preview known choice then labelled commit. Exclusivity and ending handled through scenes; no stat perks.

**States**: Empty — No Frontier cast authored: no fabricated roster. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Frontier required; officer/Eurydica resident ineligible; one romance at a time; exact scene condition must be authored. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Profile full uncropped portrait left; scene uses waist-length portraits. No invented cast.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G07 — Romance cast, gift likes/dislikes and point values, dates, endings and authored scenes are later Frontier content; no sprint beyond S9 is assigned. G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_adventurer_office"></a>

### Adventurer Office

**ID**: `ui_adventurer_office`

**Name**: Adventurer Office

**Owner officer**: Elsie

**GDD refs**: §5.2, §6, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Walk to Elsie/Adventurer Office; hub shortcut → World/talk/hub caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Event dialogue [§14; story]; New Expedition, Ongoing, Roster, Progression, Rest routes [§15]; readiness (HP, stamina, restrictions) [§6; roster]; payroll exposure/reserve [§13.2; guild].

**Actions**: Open each route → `open_expedition`, `open_ongoing`, `open_roster`, `open_progression`, `open_rest_orders` (UI proposals). Officer header → `open_officer_profile`. No dispatch from merely opening a route.

**States**: Empty — No hired adventurers: show Recruitment. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Hunting needs M03: M02 + at least one hire + Elsie's explanation; scouting needs M06 introduction after first return. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Elsie large painted portrait and guidance box (§2.3); employee small slots idle-left sprite.

**Three Houses pattern**: R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_roster"></a>

### Adventurer roster

**ID**: `ui_roster`

**Name**: Adventurer roster

**Owner officer**: Elsie

**GDD refs**: §6.1–§6.5, §12.6, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Adventurer Office; hub; prep member picker → Exact caller; picker returns to prep draft.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Name, specialty, fixed passive/effect, reach, HP current/max, four stamina bars, primary state, Red Fatigue overlay and injury expiry [§6; roster]; wage/employment/former status [§12.6/§13.2; roster/former_staff]; inspect/hire/rest routes [§15].

**Actions**: Inspect → `open_adventurer_profile`; choose for prep → `select_prep_member` (draft); rest → `open_rest_orders`; hire route → `open_recruitment` (UI proposals). No mutation on selection.

**States**: Empty — No employed people: show named Recruitment/Former staff routes. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Picker gives exact reason: injury until time, already assigned, 0 stamina, rest order, event lock or reservation. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Every small face slot uses own idle-left pixel sprite in a frame; Elsie painted owner portrait.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_adventurer_profile"></a>

### Adventurer profile

**ID**: `ui_adventurer_profile`

**Name**: Adventurer profile

**Owner officer**: Elsie

**GDD refs**: §6.1–§6.6, §12.3, §12.6

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Roster, prep, recruitment, returned-operation member → Caller with selected person preserved.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Identity/specialty/traits, fixed passive, melee/ranged reach [§6.1/§6.2; roster/content]; HP/ATK/DEF/rate/rounded interval, signature/meter role and selected modifiers [§6.2b/c/§9.3; roster]; stamina/state/fatigue/injury [§6.3–§6.5; roster]; spendable/lifetime XP/cap, track levels, enhancement, active gear [§6.2c/§6.6/§12.3; roster/inventory]; wage/arrears [§13.2; guild/former_staff].

**Actions**: Open build/backpack/rest → `open_progression`, `open_backpack`, `open_rest_orders`; dismiss → `dismiss_employee` (proposed): labelled confirm shows accrued settlement/arrears and returned gear. No permanent deletion.

**States**: Empty — Candidate not employed: retained stats plus hire route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Edits require each action's actual HQ/state gate; left staff require rehire and bed, not a free stat reset. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Small identity face: idle-left sprite in frame; never substitute an officer. Elsie owner portrait.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_progression"></a>

### Adventurer progression / rebuild

**ID**: `ui_progression`

**Name**: Adventurer progression / rebuild

**Owner officer**: Elsie

**GDD refs**: §6.2a–§6.2c, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Roster/profile; Adventurer Office → Caller; Cancel discards complete build draft.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Power/Toughness/Speed/Focus levels and bonuses; sequential cost 100n XP; spendable/lifetime XP; Eurydica level-6/3,000 cap vs Frontier 10/12,000 [§6.2c; roster]; every character-specific level-5/8 modifier, selected max two rank-1/one rank-2, same-track prerequisite [§6.2a/c; roster]; stat/interval deltas and rebuild free-once then 100G [§6.2c; roster/guild].

**Actions**: Draft track/choice → `edit_build_draft` (UI); labelled Buy build → `commit_adventurer_build`; labelled Rebuild → `rebuild_adventurer`; Cancel → `discard_build_draft` (proposals). Atomic complete-build preview; no enhancement refund.

**States**: Empty — No XP: show costs and locked previews. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Show exact missing XP, Frontier gate, same-track rank-1 prerequisite or modifier-slot conflict. Rebuild requires HQ and displayed fee. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed person sprite; Elsie owner portrait.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_rest_orders"></a>

### Rest-day orders

**ID**: `ui_rest_orders`

**Name**: Rest-day orders

**Owner officer**: Elsie

**GDD refs**: §6.3–§6.5, §5.4

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Office/Roster/profile; morning readiness link → Caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Four-bar stamina before and at 20:00/next sleep; today's dispatch history and rest flag, injury timer, enhancement/operation state [§6.3–§6.5; roster/operations]; Hard Drills/Easy Pace effects when chosen [§5.4; bonds].

**Actions**: Assign → `assign_rest_day`; cancel → `cancel_rest_day` (proposed). Label lock on dispatch/enhancement and loss of recovery entitlement on cancel; injured person may rest without clearing Injured label.

**States**: Empty — No employed adventurers: Recruitment route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Already dispatched today: cannot retroactively rest; enhancement/operation restriction explains exact required completion/cancel. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed rows; Elsie portrait.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_backpack"></a>

### Backpack and loadout editor

**ID**: `ui_backpack`

**Name**: Backpack and loadout editor

**Owner officer**: Elsie

**GDD refs**: §6.6, §12.2, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Profile; Preparation equipment button → Profile after save, or unchanged prep draft parent.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Grid 4×4 F/E, 5×4 D/C, 5×5 B/A/S; item instances/footprints/rotation [§6.6; inventory/roster]; active weapon/armour/accessory, flat stats, bow/Arrow Case adjacency +15%, Route Map active/nonstacking [§6.6/§12.2; inventory]; potions, lure/map consumption, bound starter exclusions, available/reserved stock [§6.6; reservations].

**Actions**: Move/rotate/category choice → `edit_loadout_draft`; labelled Save loadout → `commit_loadout`; prep keeps draft until `dispatch_operation` (proposals). Preview HP clamp/no heal, consumed lure/map and invalid placement; Cancel preserves original inventory.

**States**: Empty — No movable items: show bound starter explanation; Nell starter bow token is 1×3. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Equipment edits require Available at HQ; reserved item names its claim; overlap/out-of-grid keeps original intact. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed adventurer identity; item icons, no material/corpse grid items.

**Three Houses pattern**: R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: Mouse select/drag and click placement; proposed arrows/controller stick move a grid cursor, Enter/A pick/drop, R/RB rotate 90°, Z/X undo, Esc/right click/B cancel the current draft operation. Confirm remains a labelled button (§13 base actions; missing grid bindings proposed).

**Gaps**: G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_staff_roster"></a>

### Department staff roster

**ID**: `ui_staff_roster`

**Name**: Department staff roster

**Owner officer**: Mae / Fulker / Liliana for own staff

**GDD refs**: §12.6, §13.2

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Department staff route; Recruitment; payroll member link → Caller department/recruitment/payroll.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Konrad processor, Ulrich craftsman, Cassia clerk; rank, station, assignment, total productive hours, wage and employment state [§12.6; roster/former_staff/processing/workshop/information]; officer fallback station shown distinctly [§12.6].

**Actions**: Inspect → `open_staff_profile`; hire/former staff → `open_recruitment` (UI proposals). Automatic highest-rated worker assignment is not a manual idle-worker selector.

**States**: Empty — No hired worker: explain baseline officer fallback, not closed service. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Hiring requires opened department and free staffed station; no adventurer bed consumed. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed staff sprites; owning officer painted portrait.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_staff_profile"></a>

### Staff profile and promotion

**ID**: `ui_staff_profile`

**Name**: Staff profile and promotion

**Owner officer**: owning department officer

**GDD refs**: §12.6, §13.2

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Staff roster, production worker row, Recruitment/payroll → Exact caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Name/role, descriptive traits if authored, rank, productive total/fractional hours, current job and finish, station [§12.6; roster/processing/workshop/information]; rank-2 40h+200G, rank-3 Frontier+100h+400G, duration/forecast and wage changes [§12.6/§12.5; roster/guild]; projected next bill/accrued vs future wage [§13.2; guild].

**Actions**: Promote → `promote_staff`; dismiss → `dismiss_employee` (proposed), labelled confirmations with future wage bill and accrued settlement. Inspect hours read-only; no reassignment reroll.

**States**: Empty — New staff: zero productive hours. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Show remaining productive hours, promotion fee and Frontier gate; hours from aborted jobs don't count; station needed to rehire. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Own idle-left framed sprite, officer owner portrait; no invented staff painted face.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_recruitment"></a>

### Recruitment and Former staff

**ID**: `ui_recruitment`

**Name**: Recruitment and Former staff

**Owner officer**: Elsie; Mae/Fulker/Liliana for routine staff

**GDD refs**: §6.4a, §12.6, §14, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Office/department; roster empty state; HQ waiting recruit; rescue link → Caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Authored candidates: Anselm 250/90G, Nell 250/90G, Severa 300/105G, Otto 325/110G, Chloris 400/120G, Konrad 150/60G, Cassia 150/60G, Ulrich 200/75G (hire/weekly base) [§12.6; roster/content]; exact eligibility, free bed/station, original hire/arrears and preserved stats/stamina/injury [§6.4a/§12.6; former_staff/construction]; coming bill/reserve [§13.2; guild].

**Actions**: Hire → `hire_employee`; Rehire → `rehire_employee` (proposed): preview full cost, bed/station, current injury/stamina and payroll before labelled commit. No paid/random refresh; officers absent from pool.

**States**: Empty — No newly eligible candidates: show retained named previews/former staff. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Anselm/Nell M02+bed; Severa/Otto Annex+bed; Chloris Ch2+E+bed; Konrad Processing+station; Cassia Information+station; Ulrich M05+bench; exact missing funds including arrears. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Candidate/former rows idle-left framed sprites; relevant officer painted header.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_region_map"></a>

### Region map

**ID**: `ui_region_map`

**Name**: Region map

**Owner officer**: Elsie for expedition route

**GDD refs**: §7.1, §14, §15, §16a

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: New Expedition; hub; material-source link → Caller; detail returns to same area selection.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Hylaea F, Bernmoor E, Erythra D; active base and campaign context [§7.1/§16a; discoveries/guild/active_base_id]; area locks and known map labels [§7; discoveries/story].

**Actions**: Select area → `open_area_detail`; inspect source → `open_material_source` (UI proposals). No scouting progress or travel on map click.

**States**: Empty — No Frontier names authored: never populate invented regions. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Area access shows exact required rank and story service predicate. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No character-face map markers required; Elsie header on department route.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_area_detail"></a>

### Area detail / Region Knowledge

**ID**: `ui_area_detail`

**Name**: Area detail / Region Knowledge

**Owner officer**: Elsie

**GDD refs**: §7.2–§7.3, §8, §9.1, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Region map; Information; known source links → Exact caller/map selection.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Exploration %, local fog, ordinary species known /3, landmarks /3, paths /2; 25/50/75/100% milestones [§7.2; discoveries]; current tick-rounded search duration, target probabilities, den/path/healing/risk benefits [§7.3/§8.2/§9.1; discoveries]; rare availability/reservation [§8.4; discoveries/reservations]; material links to recipe/request/project [§7.3; projects/requests/inventory].

**Actions**: Hunt → `open_hunt_targets`; Scout/repeat survey → `open_scout_prep`; Contracts → `open_contracts`; inspect find/source → `inspect_discovery` (UI proposals). No map click awards discoveries.

**States**: Empty — 0%: known starting species and locked milestones, not all species disclosed. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Scout needs M06; 100% changes discovery scouting to repeat survey for rare leads, not a disabled region. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Elsie portrait; no NPC portraits on fog.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_hunt_targets"></a>

### Hunt target cards

**ID**: `ui_hunt_targets`

**Name**: Hunt target cards

**Owner officer**: Elsie

**GDD refs**: §8.4, §9.1–§9.3b, §10, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Area detail Hunt; rare alert → Area detail/source alert.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Known species names, HP/ATK/DEF/rate and approved skill data reference [§9.3b/§10; content]; target odds, group chance/size danger, Ordinary/Elite:Rare/Variant/Boss labels [§6.2/§9/§10; discoveries]; outputs, processing time, per-unit Standard values vs raw-corpse reference, XP tier [§10; content]; rare reservation state, source/project links [§8.4/§7.3; reservations/projects].

**Actions**: Select → `select_hunt_target` (draft); Prepare → `open_preparation`; inspect output → `open_item_detail` (UI proposals). Never reserve rare until dispatch.

**States**: Empty — No eligible sighting: ordinary targets plus scouting route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unidentified target requires exploration threshold; rare reserved names operation holding it; boss via its contract/flashpoint, not ordinary hunt. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Monster still/icon; Elsie owner portrait; no human face on monster cards.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_preparation"></a>

### Expedition preparation

**ID**: `ui_preparation`

**Name**: Expedition preparation

**Owner officer**: Elsie; Tristitia briefing for flashpoints

**GDD refs**: §6.3/§6.6, §8.1/§8.5, §9.1–§9.3, §11.3/§11.4, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Hunt target; Scout; Contracts; Flashpoint → Exact source with uncommitted edits discarded on Cancel.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Operation/area/target; party names, reach/passives, three front + three back slots, max five and at least one front for combat [§9.1a; roster]; exactly one scout [§8.1]; equipment draft and consumables [§6.6; inventory]; HP/state/stamina before→after/fatigue [§6.3; roster]; hunt 1/2/3h or scout 30min increments ≤3h, actual finish/cutoff, contract 30min approach [§8/§9/§11; clock]; Low/Moderate/High advice/main causes from isolated 100-seed risk sim, scout cumulative injury forecast/find chance [§8.5/§9.3; operations query]; two template names [§15; prep_templates]; Briefed/encouragement/story guests when applicable [§5a.2/§9.3; commander/story].

**Actions**: Select/swap/remove member, duration/row/consumable edit → `edit_prep_draft`; template → `open_prep_templates`; Backpack → `open_backpack`; labelled Dispatch → `dispatch_operation`; Cancel → `discard_prep` (proposed). Revalidate people/HP/stamina/gear/reservations/target/cutoff atomically, debit stamina and consumables only on dispatch.

**States**: Empty — No candidates: Recruitment/rest/readiness explanation. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Display exact invalid row, max-party/scout count, HP/injury/state, missing item or rare claim; after 20:00 wait until next operating day; melee back warns ×0.5 damage, post-debit ≤1 warns fatigue. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed adventurer slots; officer painted crops for explicit story guests; owning officer portrait.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G11 — FGC_07 §04 lists field exit as world, while GDD §15 requires the previous navigation context. Inventory follows GDD and proposes suspending/restoring the caller; implementation state routing must reconcile this. G15 — Formation-template naming/overwrite UX is undefined beyond two named templates and missing-member/item/fatigue feedback. No automatic substitutions. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_prep_templates"></a>

### Two named formation/loadout templates

**ID**: `ui_prep_templates`

**Name**: Two named formation/loadout templates

**Owner officer**: Elsie

**GDD refs**: §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Preparation templates button → Same prep draft.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Two template slots/names, saved member IDs, row and equipment arrangement; absent people, missing items, fatigue differences [§15; prep_templates/roster/inventory].

**Actions**: Save/rename → `save_prep_template`; Apply → `apply_prep_template_draft` (proposed). Label template storage commit separately from dispatch; overwrite preview. Applying changes draft only; never substitutes people.

**States**: Empty — Empty slot: Save current draft. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Missing person/item: list each requirement and retain invalid draft for repair; Dispatch still validates. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed adventurer slots; officer crops only for authored guest preview.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G15 — Formation-template naming/overwrite UX is undefined beyond two named templates and missing-member/item/fatigue feedback. No automatic substitutions. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_ongoing"></a>

### Ongoing expeditions and returned-today history

**ID**: `ui_ongoing`

**Name**: Ongoing expeditions and returned-today history

**Owner officer**: Elsie

**GDD refs**: §8–§9, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Tab/Y from world; Office; hub; operation alert → Exact caller; Watch suspends this context for later return.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Each operation party/target/area, phase, start/finish/time left, progress/finds or secured corpses [§8/§9; operations/discoveries/inventory]; returned-today history and reason [§4.1; journal/operations].

**Actions**: Watch/View/Follow → `watch_operation` (UI proposal) closes active overlay pause while preserving return context; Recall → `recall_operation` (proposed) immediate with visible no-stamina-refund/secured-yield consequence, no added confirmation delay; history → `open_operation_result`.

**States**: Empty — No active expeditions: returned-today history or New Expedition route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Already returned operation: open recorded result, no live Recall; stale clicks cannot recall another ID. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left member faces; officer guest crops; Elsie large owner portrait.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: §13 Tab/Y opens; E/Enter/click/A activates, Esc/right click/B returns; proposed focus/scroll as menu.

**Gaps**: G11 — FGC_07 §04 lists field exit as world, while GDD §15 requires the previous navigation context. Inventory follows GDD and proposes suspending/restoring the caller; implementation state routing must reconcile this. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_field_view"></a>

### Field view shell / search walk

**ID**: `ui_field_view`

**Name**: Field view shell / search walk

**Owner officer**: none

**GDD refs**: §8.3, §9.4–§9.5, §15; FGC_07 §11

**Milestone/sprint**: M2 / S6 field and battle presentation.

**Opens from / returns to**: Ongoing Watch/View/Follow; operation alert via Ongoing → Previous navigation context per GDD; world fallback when no caller.

**Clock**: Live `field` (FGC_07 §04/§11). Preserve chosen Pause; otherwise only a visible fight applies optional ¼ selected global speed. Search/scout do not invoke battle pace.

**Shows**: Place/target, phase/search progress, remaining time, secured corpses, live log, top speed/pace [§9.4/§9.5; operations/combat/clock]; walking formation then battle, FRONT/BACK per member [§9.1a/§15; roster/combat].

**Actions**: Leave → `leave_field_view` (UI proposal); Recall → `recall_operation` immediate. Search/battle rendering never controls RNG, progress or action timing. Reopen binds live state.

**States**: Empty — No active operation: open its return receipt/Ongoing. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Ended during transition: display committed result; no new action at return/cutoff. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed small member slots override older front-idle bust wording by handoff; actual field sprites retain combat poses.

**Three Houses pattern**: R01 (3D Battle UI.png): compact combat identity and HP plates at the edges; floating damage over the action. FGC retains its own party-bottom/enemy-top contract. R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: §13 speed P/1/2/4/D-pad, Tab/Y Ongoing; proposed Esc/B Leave, click/A Recall after focus selection.

**Gaps**: G11 — FGC_07 §04 lists field exit as world, while GDD §15 requires the previous navigation context. Inventory follows GDD and proposes suspending/restoring the caller; implementation state routing must reconcile this. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_scout_field"></a>

### Scout field HUD and field map

**ID**: `ui_scout_field`

**Name**: Scout field HUD and field map

**Owner officer**: none

**GDD refs**: §7.2–§7.3, §8.1–§8.5

**Milestone/sprint**: M2 / S6 field and battle presentation.

**Opens from / returns to**: Field Follow on active scout → Field/Ongoing caller; no simulation change.

**Clock**: Live `field` (FGC_07 §04/§11). Preserve chosen Pause; otherwise only a visible fight applies optional ¼ selected global speed. Search/scout do not invoke battle pace.

**Shows**: Scout identity, exploration%, next interval/time remaining, parchment fog map, information/find list and event log [§8.3; operations/discoveries]; repeat-survey state at 100%, risk-related injury return notice [§7.2/§8.5; roster].

**Actions**: Inspect discovery → `inspect_discovery` (UI); Leave → `leave_field_view`; Recall → `recall_operation` immediate. Inspect modal pauses as overlay; scout watching alone never battle-slows.

**States**: Empty — No finds: 'No new lead' when pool empty; don't fabricate. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Returned/injured scout: read receipt; no live Follow. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Scout idle-left framed portrait if shown; no painted stand-in.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: Field §13 controls; proposed click/A inspect map/find; Esc/B closes detail before Leave.

**Gaps**: G11 — FGC_07 §04 lists field exit as world, while GDD §15 requires the previous navigation context. Inventory follows GDD and proposes suspending/restoring the caller; implementation state routing must reconcile this. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_battle_hud"></a>

### Battle HUD: party, enemies and log

**ID**: `ui_battle_hud`

**Name**: Battle HUD: party, enemies and log

**Owner officer**: none

**GDD refs**: §9.1a, §9.3–§9.4, §10.0

**Milestone/sprint**: M2 / S6 field and battle presentation.

**Opens from / returns to**: Live field encounter → Search resumes after victory; field exit uses caller.

**Clock**: Live `field` (FGC_07 §04/§11). Preserve chosen Pause; otherwise only a visible fight applies optional ¼ selected global speed. Search/scout do not invoke battle pace.

**Shows**: Enemy bars top centre: identity/current-max HP, RARE/VARIANT/Elite subtype [§9.4/§10; combat]; party bottom without enclosing box: name, large HP number/bar, gold clockwise readiness ring, orange 0–100 meter/glowing SKILL, FRONT/BACK every member, statuses/action counters [§9.1a/§9.3a/§9.4; combat]; left place/target/time/corpses and right log [§9.4; operations]; no turn-order bar or MP.

**Actions**: Observe; proposed `inspect_combatant` tooltip only. Leave/Recall/speed delegated to field shell; no direct attack/skill button.

**States**: Empty — No encounter: hide enemy bars, return search view. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Downed member marked down; no revive/potion button. Status values come from committed combat, never animation guesses. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Adventurer bust slots use framed idle-left sprites per owner; officer guest may use painted crop. No duplicate player Commander fighter.

**Three Houses pattern**: R01 (3D Battle UI.png): compact combat identity and HP plates at the edges; floating damage over the action. FGC retains its own party-bottom/enemy-top contract. R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath.

**Input**: No direct input; inherits the host's §13 controls. Any optional focus/inspection control is explicitly proposed.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_battle_labels"></a>

### In-world battle labels and skill banner

**ID**: `ui_battle_labels`

**Name**: In-world battle labels and skill banner

**Owner officer**: none

**GDD refs**: §2.5, §9.3b–§9.6, §10.0; FGC_07 §11/§12

**Milestone/sprint**: M2 / S6 field and battle presentation.

**Opens from / returns to**: Combat events in watched field → Automatic end of visual event; no navigation.

**Clock**: Live `field` (FGC_07 §04/§11). Preserve chosen Pause; otherwise only a visible fight applies optional ¼ selected global speed. Search/scout do not invoke battle pace.

**Shows**: Body-height damage numbers; combatant names; FRONT/BACK identifiers; ATK UP/DOWN, DEF UP/DOWN, SPD UP/DOWN, PROVOKE and authored stun/status counters [§9.3/§9.3b/§9.6; combat]; skill name banner and RARE/VARIANT badges [§9.4/§10; combat/content]. Numeric values Alegreya Sans lining figures; in-battle names Pixelify Sans [§2.5].

**Actions**: No commit/input; `present_combat_event` (presentation proposal) consumes immutable events, never rerolls/rewards. Skill cinematic follows action; reduced VFX only changes presentation.

**States**: Empty — No event: no label. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Late renderer compresses visuals per FGC_07 §11; never delays sim ticks. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No extra cut-in face required; retain current combat actors. Officer art only if an authored presentation uses it.

**Three Houses pattern**: R01 (3D Battle UI.png): compact combat identity and HP plates at the edges; floating damage over the action. FGC retains its own party-bottom/enemy-top contract. R15 (Skill Use.png): brief horizontal skill-name banner over the action; no imported skill text or artwork.

**Input**: No direct input; inherits the host's §13 controls. Any optional focus/inspection control is explicitly proposed.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_discovery_notice"></a>

### Discovery parchment notice

**ID**: `ui_discovery_notice`

**Name**: Discovery parchment notice

**Owner officer**: none

**GDD refs**: §7.2–§7.3, §8.2–§8.4

**Milestone/sprint**: M2 / S6 field and battle presentation.

**Opens from / returns to**: Scout discovery or milestone event → Field; inspect then return to same live context.

**Clock**: Live `field` (FGC_07 §04/§11). Preserve chosen Pause; otherwise only a visible fight applies optional ¼ selected global speed. Search/scout do not invoke battle pace.

**Shows**: Find name/kind, area, newly cleared fog, known benefit, rare availability or hint-only text [§8.2; discoveries]; source event/time [§15; journal/clock]; no duplicated unique find reward.

**Actions**: Inspect → `open_discovery_detail` (UI overlay proposal); dismiss → `dismiss_discovery_notice` (UI). Notice itself nonmodal proposed; only detail pauses.

**States**: Empty — No find: 'No new lead' in log rather than reward card. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Already known/reserved find: retain event identity, no second award. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No face; map/material/monster icon as applicable.

**Three Houses pattern**: R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: Proposed click/A inspect or dismiss; field §13 controls remain until detail opens.

**Gaps**: G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_request_board"></a>

### Request Board and delivery detail

**ID**: `ui_request_board`

**Name**: Request Board and delivery detail

**Owner officer**: Tristitia

**GDD refs**: §11.1–§11.2, §14–§15, §16a

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Commander's Office/Tristitia; hub; client offer; request notice → Exact caller; client-turn-in returns to interaction.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Offered/Accepted/history (Hidden excluded), ID/title/client, appearance/absolute deadline/remaining time or no deadline [§11.1; requests/clock]; goods/quality, owned/listed/reserved/available/exact consumed lots [§11.1; inventory/reservations/markets]; full gold/Rep/persistent benefit and active modifiers [§11.2/§5a.2; requests]; core-vs-15-gel alternative eligibility and exclusive exchange, courier/client access [§11.2; requests/story]; repeat order next appearance/suspension [§11.2/§16a; repeat_orders].

**Actions**: Accept → `accept_request`; Reserve/release → `reserve_request_goods` / `release_request_goods`; Deliver → `deliver_request`; gel alternative → `deliver_request_alternative`; decline/abandon → `decline_request` / `abandon_request` (proposed). Preview exact lots/full reward and any −10 accepted-failure Rep; labelled whole-order commit, lowest acceptable quality first. Reading offer never accepts.

**States**: Empty — No visible requests: exclude Hidden, retain history. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Missing exact qty/quality shown; before Jeb courier visit client (Jeb first turn-in local); after relocation accepted Eurydica deliveries use protected courier; never require trader schedule. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia large painted portrait/guidance left; client without portrait name-only; client profile respects full portrait rule.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_request_notice"></a>

### Request available notice

**ID**: `ui_request_notice`

**Name**: Request available notice

**Owner officer**: Tristitia for admin context; otherwise none

**GDD refs**: §11.1, §14; Scene Format §3/§4

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: [request:] cue or offer-branch {request:} tag → Current safe dialogue/world context; details return here.

**Clock**: Dialogue overlay pauses (FGC_07 §04/§09); authored scene control handoff is retained. Non-dialogue scene clock policy is G19. No battle-pace action.

**Shows**: Newly Offered request title/client, deadline/remaining time and Board route [§11.1; requests/clock]; source event [§15; journal].

**Actions**: View → `open_request`; acknowledge → `acknowledge_request_notice` (UI proposals). `unlock_request` reveals once; explicit Accept remains on Board.

**States**: Empty — Duplicate reveal: no second notice/restart. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Required scene still active: queue navigation until safe moment, retain authored line. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia crop optional for admin notice; portraitless client name only.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: E/Enter/click/A acknowledges; proposed focused View opens Board; no automatic acceptance (§13).

**Gaps**: G03 — HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. G19 — Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_contracts"></a>

### Optional contract list and detail

**ID**: `ui_contracts`

**Name**: Optional contract list and detail

**Owner officer**: Tristitia

**GDD refs**: §11.3, §14–§15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Request Board Contracts tab; Area Detail; Office → Caller with selected contract.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Eight EUR-SUB-01…08 authored clients/problems, rank/species/story gates, fixed encounter, gold/Rep/ending flag [§11.3; contracts]; absolute deadline + remaining from 72h appearance baseline, accepted status, seven-day reoffer after unsuccessful outcome [§11.3/§16b; contracts/difficulty]; 30min approach, secured corpse/XP rules and −10 failure Rep [§11.3; operations].

**Actions**: Accept → `accept_contract`; Prepare → `open_contract_preparation`; Decline → `decline_contract`; Abandon → `abandon_contract` (proposed). Confirm accepted-risk/absolute deadline; dispatch separately in Prep. No hunt group/variant rolls for fixed encounters.

**States**: Empty — No eligible offer: history and known exact gates. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — M08 requires won ordinary fight + Tristitia explanation; individual rank/known-species/Chapter2 gates; already successful never recurs. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; client name-only if no art; party uses idle-left slots in linked prep.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_flashpoint"></a>

### Flashpoint briefing

**ID**: `ui_flashpoint`

**Name**: Flashpoint briefing

**Owner officer**: Tristitia

**GDD refs**: §11.4, §13.4, §14–§15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Office/Board/story offer; chapter route → Caller or explicit authored scene; retry returns to offer.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Chimera: Ch2+E+300 Rep; Ambermaw: Chimera+E+800 Rep; Crownstone: Ambermaw+D+1,400 Rep [§11.4; flashpoints/guild/story]; solo boss stats/30min approach; explicit story guest formation [§9.3/§10/§11.4]; 900G+250Rep /1,400G+350Rep /2,000G+450Rep and exact lasting area aftermath [§11.4; flashpoints/discoveries]; no expiry/no failure Rep/once-only victory reward.

**Actions**: Prepare → `open_flashpoint_preparation`; dispatch via `dispatch_operation` with pre-dispatch autosave; acknowledgement → `acknowledge_flashpoint_briefing` (proposed). Preview guests/rewards/aftermath; no hidden rescue or invented phase.

**States**: Empty — No eligible attempt: early named threat previews. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — List every unmet chapter/rank/Rep/predecessor gate. Failure/recall/cutoff leaves retry once party ready. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; explicit guests painted crops, adventurers idle-left framed.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_reward_receipt"></a>

### Request / contract / story reward receipt

**ID**: `ui_reward_receipt`

**Name**: Request / contract / story reward receipt

**Owner officer**: Tristitia where administering

**GDD refs**: §11, §13.3, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Committed delivery/victory/reward event → Request/caller; later result history.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Actual items/quantity/quality, gross gold, fee if applicable, debt sweep/net cash, Rep and source, unlocked aftermath [§11/§13.3/§13.4; journal/guild/inventory]; event receipt ID [§15; effect_receipts].

**Actions**: Continue → `acknowledge_reward_receipt`; inspect item → `open_item_detail` (UI proposals). Receipt reflects already committed reward; Continue is not a second payout.

**States**: Empty — No material reward: show actual cash/flag outcome without fabricated item row. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Receipt unavailable: show error/reference; never rerun grant to rebuild a display. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Admin officer portrait only when part of caller; no required extra face.

**Three Houses pattern**: R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row. R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_processing"></a>

### Processing work order

**ID**: `ui_processing`

**Name**: Processing work order

**Owner officer**: Mae

**GDD refs**: §10.5, §12.1, §12.6, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Walk to Processing corner/room; hub; corpse result/source link → Previous navigation context.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Corpse IDs/species/tier, raw reference value, possible common/rare/elite yields [§10; inventory]; up-to-30 ordered corpses, active/waiting assignments, processor rank/productive hours, fallback Mae, per-job/order finish estimate and cutoff [§12.1/§12.6; processing/roster]; quality categories/modifier provenance, numeric pre-start odds gated pending G10 [§5a.2/§12.1; processing/bonds]; fixed identity/roll retention, storage unlimited/no spoilage [§12.1].

**Actions**: Queue → `queue_processing`; reorder → `reorder_processing`; remove waiting → `remove_processing_order`; cancel active → `cancel_processing_job` (proposed). Preview yields/cutoff; labelled commits. Cancel returns whole corpse, retains roll identity; worker assigned automatically by rank then productive hours. Session route → `open_cutting_chart`.

**States**: Empty — No corpses: known hunting-source route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Queue full: remove a waiting entry; claimed corpse names reservation owner; no start after 20:00; valid queues resume at 07:00 after revalidation. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Mae large painted portrait + dialogue; worker small slots idle-left sprites; fallback marked Mae, not anonymous worker.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G10 — Processing quality visibility conflicts: §12.1/§15 ask for odds while §5a.2 reserves seeing pre-start odds to Trained eye at rank 3. Exact public fields before rank 3 need reconciliation within the GDD. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_workshop"></a>

### Workshop mixed work order

**ID**: `ui_workshop`

**Name**: Workshop mixed work order

**Owner officer**: Fulker

**GDD refs**: §12.2–§12.3, §12.8, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Walk to Fulker/Workshop corner; hub; recipe source → Caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: All recipe previews and category filter; mixed crafting/enhancement/Reworking queue up to 20; waiting intent vs active input/fee reservation [§12.2/§12.2a; workshop/reservations]; automatic highest-ranked/free craftsman, productive-hours tie, Fulker fallback, current job/finish/order estimate/cutoff [§12.2a/§12.6; workshop/roster]; exact ingredients, result/footprint/stat/source links and campaign locks [§12.2/§12.3; inventory].

**Actions**: Open recipe/enhancement/rework → `open_recipe`, `open_enhancement`, `open_reworking`; queue → `queue_workshop_job`; reorder/remove/cancel → `reorder_workshop`, `remove_workshop_order`, `cancel_workshop_job` (proposed). Preview then labelled commit; **Reserve** in §15 maps to job-start transaction, not a waiting-queue material claim. Refund active inputs+fees on cancellation/cutoff; Fitting route available.

**States**: Empty — No jobs: recipe previews remain. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Missing start inputs identify exact quantities/claims; no worker idle while an eligible job/table available; no start at cutoff; service needs M05 joining scene. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Fulker large painted portrait; Ulrich own idle-left framed worker sprite.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_recipe_detail"></a>

### Recipe preview and crafting quote

**ID**: `ui_recipe_detail`

**Name**: Recipe preview and crafting quote

**Owner officer**: Fulker when joined; Elsie for early preview

**GDD refs**: §3, §7.3, §12.2, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Workshop recipe list; Gerd/Elsie early preview; material/project links → Exact caller, including pre-Workshop source.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Recipe/output form, Standard+ inputs/available-reserved counts, fee, duration/finish/cutoff, footprint, flat stat/effect and one-output quantity [§12.2; workshop/inventory/reservations]; known source links, pin status and missing goods/gold [§3/§7.3; projects/discoveries]; ten §12.2 recipe rows including Refinement, no extra recipes invented.

**Actions**: Select recipe form → `edit_recipe_draft`; labelled Queue craft → `queue_workshop_job`; pin → `pin_project`; inspect source → `open_material_source` (proposed). Preview consumes nothing; inputs/fee reserved only at job start.

**States**: Empty — No eligible input stock: retain useful preview. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Workshop closed: boar material seen or known source card + speak to Fulker; queue intent doesn't guarantee stock at start. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Owning officer portrait; recipe/item icon. Gerd without portrait name-only.

**Three Houses pattern**: R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_enhancement"></a>

### Adventurer enhancement quote

**ID**: `ui_enhancement`

**Name**: Adventurer enhancement quote

**Owner officer**: Fulker

**GDD refs**: §12.3, §6.3, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Workshop Enhance; adventurer profile → Workshop/profile caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Target name/current enhancement and next sequential level, permanent +5% base HP/ATK/DEF per level, no rate change [§12.3; roster]; destination 1–5 input/common-species/refinement/elite-part/fee/time table, opening cap 2, Frontier 3–5 [§12.3; inventory/workshop]; before→after permanent stats, person lock and cutoff refund [§12.3; roster].

**Actions**: Select target/species → `edit_enhancement_draft`; labelled Queue enhancement → `queue_workshop_job` (proposed). Start revalidates resources/person; cancellation returns inputs+fee, no partial enhancement.

**States**: Empty — No employed eligible person: roster/recruitment route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Adventure/rest/enhancement mutually exclusive; show completion/cancel-rest requirement, exact material/fee shortfall or Frontier lock. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Target idle-left framed sprite; Fulker portrait.

**Three Houses pattern**: R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_reworking"></a>

### Reworking quote

**ID**: `ui_reworking`

**Name**: Reworking quote

**Owner officer**: Fulker

**GDD refs**: §12.8, §12.2a, §5.4

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Workshop Reworking; material detail → Workshop/material caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: One material/grade, available vs reserved units; Mend 2 Damaged→1 Standard/4h, Refine grade 2 Standard→1 Pristine/4h, Master's Salvage 3 Damaged→1 Pristine/6h [§12.8; inventory/workshop]; staff duration, Rough Patch half time/Mend-only or Master's Salvage unlock, no Morale factor [§5.4/§12.8; bonds/roster]; input/output sale-value comparison and recipe/request access [§12.8; inventory/requests].

**Actions**: Preview conversion → `preview_rework`; labelled Queue rework → `queue_workshop_job` (proposed). No invented fee or profit guarantee; reserve only when started, refund at cutoff.

**States**: Empty — No compatible units: sources/other uses remain. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unsellable cannot rework; mixed materials invalid; show exact grade/count needed; Rough Patch bars Pristine outcomes, Salvage needs chosen perk. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Fulker portrait; material icons and quality badges, no worker portrait fabrication.

**Three Houses pattern**: R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_information"></a>

### Information / forecasts / rumours

**ID**: `ui_information`

**Name**: Information / forecasts / rumours

**Owner officer**: Liliana

**GDD refs**: §12.5, §5a.2, §5.4, §16a.1, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Information Office/corner; hub; market forecast link → Caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Dated category forecast Low/Normal/High, confidence, horizon; clerk ranks 1/2/3: 1/2/3 days at 70/80/90%, Liliana fallback 1 day/60% [§12.5; information]; actual historical demand [§12.5; markets]; known source links, one morning opportunity baseline and unverified rumours, skill/perk modifiers [§12.5/§5a.2/§5.4; information/commander/bonds]; active-base tags [§16a.1].

**Actions**: Inspect date/category → `inspect_forecast`; source/lead → `open_information_source`; Cross-check → `open_cross_check` (UI proposals). Read delivered predictions without reroll/reassignment refresh; rumours grant no exploration.

**States**: Empty — No uncompleted known opportunity: no random quest fabricated. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Service requires first scout return + Liliana joining scene; future horizon shows rank requirement. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Liliana portrait; Cassia idle-left framed staff slot; portraitless rumour NPC name-only.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_commerce"></a>

### Commerce listings

**ID**: `ui_commerce`

**Name**: Commerce listings

**Owner officer**: Valerie

**GDD refs**: §12.4, §5.4, §5a.2, §13.4, §16a.1, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Commerce/Trading Post; hub; inventory sell link → Caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Available/listed/reserved material lots/quality [§12.4; inventory/reservations]; capacity 3/5/8 at Rep 0/200/700 plus shelves/perks, used slots [§12.4/§5.4; markets/guild/construction]; 1–99 stack, whole-Gold unit price, demand/date/category, hourly shared buyer/quota, fee/gross/net/debt-sweep preview [§12.4/§13.4; markets/guild]; persistent listings/age and active-base tag eligibility [§16a.1; markets].

**Actions**: Edit quote → `edit_listing_draft`; labelled List → `create_listing`; Reprice → `reprice_listing`; Withdraw → `withdraw_listing`; Walk-up → `open_walk_up_sale`; negotiation → `open_negotiation_order` (proposed). Preview never reserves; commit claims stock. Explain expected capacity not guaranteed sale.

**States**: Empty — No sellable material: Processing/Walk-up routes as relevant. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unsellable blocked; Premium Seller blocks Damaged; Volume Trader minimum 10; new listing requires free slot/current valid region stock; over-capacity existing listings persist. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Valerie large painted portrait, always glasses; stock has item icons.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_walk_up_sale"></a>

### Any-trader walk-up sale

**ID**: `ui_walk_up_sale`

**Name**: Any-trader walk-up sale

**Owner officer**: Valerie at her counter; otherwise none

**GDD refs**: §12.4, §13.4, §16a.1

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Any-trader interaction at any base; Commerce; stock link → Counter/Commerce/caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Sellable stock instances/quality/origin/cost and exact available qty [§12.4; inventory/reservations]; processed 50% base×quality floored, raw half reference, crafted 25% consumed Standard-material value excluding fees, purchased consumable at most half actual purchase cost [§12.4]; gross/no listing fee/net after debt sweep, cumulative sales Rep progress [§12.4/§13.4; guild]; Eurydica existing stock still sellable in Frontier [§16a.1].

**Actions**: Select/count → `edit_sale_draft`; labelled Sell → `sell_to_trader` (proposed). Show actual items/quantity/payout and reserve crossing before atomic commit. No visit schedule or volume cap.

**States**: Empty — No available sellable stock: no sale total manufactured. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Reserved/equipped/bound items remain protected; Unsellable and Premium Seller Damaged cannot sell; name exact holding claim. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Trader without art name-only; Valerie portrait if her route. Important buyer profile uses full uncropped portrait.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_consumable_counter"></a>

### Potion / supply counter

**ID**: `ui_consumable_counter`

**Name**: Potion / supply counter

**Owner officer**: Elsie; Valerie after Commerce

**GDD refs**: §6.6, §12.2, §11.2

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Elsie's Office; Commerce potion counter; clinic benefit route → Same counter/office.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Potion 20G, Lure 25G, Scout Map 20G once scouting opens; item footprint/effect [§6.6/§12.2; inventory/content]; clinic completion allowance four potions/week at 18G, remaining allotment/reset week [§11.2; requests/clock]; total spend/purse/reserve [§13.1; guild].

**Actions**: Quantity → `edit_purchase_draft`; labelled Buy → `buy_consumables` (proposed). Atomic purse+stock/clinic allowance; no automatic packing into an invalid grid.

**States**: Empty — Clinic allowance exhausted: normal-price potion remains. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Show missing funds; Scout Map requires scouting; no fictitious vendor stock cap. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Elsie/Valerie painted portrait; clinic NPC without art name only; item icons.

**Three Houses pattern**: R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_storage"></a>

### Shared storage and item/corpse detail

**ID**: `ui_storage`

**Name**: Shared storage and item/corpse detail

**Owner officer**: none; department owner when embedded

**GDD refs**: §6.6, §10, §12, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Hub proposed storage route; production/Commerce/request item picker → Caller with selection/draft preserved.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Material/corpse/equipment IDs, names, quantity, quality, available/listed/reserved ownership, item origin/resale basis [§10/§12; inventory/reservations]; corpse identity/tier/raw reference separate from processed per-unit value [§10]; footprint/effect/category for gear [§6.6/§12.2]; source/use/project links [§3/§7.3; projects/discoveries].

**Actions**: Inspect/filter → `inspect_inventory` / `filter_inventory` (UI); route to process/craft/sell/request/pack via `open_item_action` (UI). No consume/transfer on hover or picker selection.

**States**: Empty — Empty storage: known source links; no capacity warning (unlimited materials/corpses). Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Reserved lots name exact owning listing/request/job; no illicit release from generic item screen. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Items/monster stills, no new face; embedded officer header inherited.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_hq_building_map"></a>

### HQ / building map and construction quote

**ID**: `ui_hq_building_map`

**Name**: HQ / building map and construction quote

**Owner officer**: none; Tristitia as proposed administrator

**GDD refs**: §5.1, §12.7, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Walk to room/expansion yard; hub HQ route; Annex preview → Same world/room/hub context.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Current rooms and services, purchased/free beds/stations/listing slots, waiting Severa/Otto; six upgrade cards [§5.1/§12.7; construction/roster]; exact quote/materials/quality/gold/calendar duration/prerequisites/effect, active build/completion/cancel refund [§12.7; construction/inventory/guild]; free service corners distinct from paid capacity.

**Actions**: Select Preview → `preview_construction`; labelled Build → `start_construction`; Cancel active → `cancel_construction` (proposed). Quote consumes inputs at start, full refund before completion; one job at a time, visuals update next safe transition.

**States**: Empty — No active construction: room/capacity map remains. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Show each unmet gate and quantity: first hunt for Annex; Annex+E Larger Dorm; ten corpses for table; Fulker+E workbench plus Crawler Plates from Erythra; Valerie shelves; all three later officers for Quarters II; overdue debt blocks optional purchases. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Waiting recruits idle-left framed slots; room owner crops; no all-officers-in-one-room staging.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_payroll"></a>

### Payroll allocation

**ID**: `ui_payroll`

**Name**: Payroll allocation

**Owner officer**: Tristitia

**GDD refs**: §13.2, §15, §16a

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Weekly closeout; Office preview; transfer payroll checkpoint → Closeout Summary/transfer checkpoint; preview returns to Office.

**Clock**: Paused `closeout` (FGC_07 §04); all due cutoff events resolve before presentation. No battle pace. An optional archived/Office preview is a paused overlay rather than a new closeout.

**Shows**: Payday day7/14/21…20:00, each employee accrued balance with once-per-employee final rounding, purse/advisory reserve/projected bill [§13.2; guild/roster]; rank/difficulty accrual provenance, full-balance selection and unpaid departure/arrears/gear return/Morale consequences [§13.2/§16b; guild/former_staff]; transfer calendar liability [§16a; transfer].

**Actions**: Draft full-balance allocation → `edit_payroll_allocation`; labelled Pay selected / Confirm unpaid departures → `settle_payroll` (proposed). Preview all consequences; no partial employee balance payment and no duplicate accrual at arrival.

**States**: Empty — No nonzero balances: no fictional fully-paid bonus. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Selected full balances exceed purse: choose affordable balances or reduce selection; reserve is warning only. Due payroll cannot be skipped by Back. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Idle-left framed employee rows; Tristitia painted portrait.

**Three Houses pattern**: R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right. R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_rank"></a>

### Guild Rank promotion

**ID**: `ui_rank`

**Name**: Guild Rank promotion

**Owner officer**: Tristitia

**GDD refs**: §13.3–§13.4, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Top bar Rank; Office; hub → Caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Current/previous rank, standing (not spendable), target fee/gates/unlocks [§13.3; guild]; E 200Rep/300G, D 700/700G, C 1,500/1,500G, B 3,000/3,000G, A 6,000/6,000G, S 12,000/12,000G [§13.3]; Frontier gate B/A/S, overdue debt restriction, charter conditions C+Crownstone+zero debt [§13.4; guild/story].

**Actions**: Preview target → `preview_rank`; labelled Promote → `promote_guild_rank`; Cancel → `discard_rank_preview` (proposals). Charge gold only; never deduct Reputation, demote or promise unauthored rewards.

**States**: Empty — Rank F: show next promotion; Rank S: current standing retained. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — List missing preceding rank, exact Rep/funds, Frontier access or overdue principal; debt-free charter differs from promotion's no-overdue rule. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; rank emblem is original FGC asset.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_debt_rescue"></a>

### Debt, emergency loan and rescue advance

**ID**: `ui_debt_rescue`

**Name**: Debt, emergency loan and rescue advance

**Owner officer**: Tristitia

**GDD refs**: §13.4, §13.1, §15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Payroll aftermath/Day Summary rescue state; Office debt detail → Caller; rehire receipt if rescue applied.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Principal/due date/overdue state, 25% later-positive-receipt sweep with remainder, voluntary repayment amount [§13.4; guild]; emergency 2,500G no-interest loan due seven days, eligibility explanation [§13.4]; direct rescue equal to cheapest eligible rehire shortfall, destination/arrears and new principal [§13.4; former_staff/guild].

**Actions**: Accept loan → `accept_emergency_loan`; repay → `repay_debt`; rescue rehire → `accept_rescue_advance` (proposed). Label amounts/due dates/restrictions; refund optional reservations before eligibility evaluation; direct rescue gives no purse windfall.

**States**: Empty — No debt: no repay; loan only if exact recovery predicate holds. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Loan requires no employed adventurer able to return without hire/rehire and no affordable eligible candidate with accommodation; resting/injured alone insufficient. Rescue only all Left+existing debt and later unpaid-payroll eligibility. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; rescue candidate idle-left framed.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_resolution"></a>

### 20:00 Resolution / operation detail

**ID**: `ui_resolution`

**Name**: 20:00 Resolution / operation detail

**Owner officer**: Tristitia

**GDD refs**: §4.1, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Cutoff after safe dialogue end; returned-operation history detail → Continue to Day Summary flow; history Back to caller.

**Clock**: Paused `closeout` (FGC_07 §04); all due cutoff events resolve before presentation. No battle pace. An optional archived/Office preview is a paused overlay rather than a new closeout.

**Shows**: Party/target/start/finish, original prep estimate, actual rewards/status: completed, returned, returned at 20:00, returned (recalled), returned (injured), failed [§4.1; operations/journal]; secured yields/path-den effects/injury cause/potions used/XP [§4.1]; aborted jobs/refunds and retained queues, continuing injuries/construction/listings/unused rares [§4.1; processing/workshop/construction/markets/discoveries].

**Actions**: Inspect operation → `open_operation_result`; Continue → `continue_closeout` (application proposal). Display already settled event receipts; never resolve an interrupted action to make the result look complete.

**States**: Empty — No expeditions: show no operations plus ongoing persistent work. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Safe dialogue still open at cutoff: wait for safe end with sim frozen; no operations continue past cutoff. Mandatory closeout cannot be dismissed to daytime. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; party idle-left framed faces, guest officer crops.

**Three Houses pattern**: R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_day_summary"></a>

### Day Summary

**ID**: `ui_day_summary`

**Name**: Day Summary

**Owner officer**: Tristitia

**GDD refs**: §3, §4.1–§4.2, §13.1–§13.4, §15

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Resolution; desk archived recap route → Proceed to night after due payroll; archived recap Back to desk.

**Clock**: Paused `closeout` (FGC_07 §04); all due cutoff events resolve before presentation. No battle pace. An optional archived/Office preview is a paused overlay rather than a new closeout.

**Shows**: Revenue/expenses/personal Commander spending; cash, Rep source and Morale cause breakdown; operations/finds/project completions [§13.1; journal/guild]; stamina before/after rest, injuries/readiness/next sleep preview [§6.3/§13.1; roster]; accrued wages/reserve/payroll/rescue, debt principal/due [§13]; up to three pins with quantities/gold shortfall/source/next action [§3; projects].

**Actions**: Inspect source → `open_summary_detail`; pin/unpin → `pin_project` / `unpin_project`; reserve → `set_advisory_reserve`; Continue to night → `begin_evening` (proposed). Pins/reserve explicit commits; no automatic pin replacement; accounting already applied.

**States**: Empty — No income/operation: actual zero ledger and existing pins, no invented rewards. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Due payroll allocation must settle; fourth pin asks which existing pin to unpin, never silently replaces. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; readiness rows idle-left framed.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R17 (Staff Roster.png): wide roster list left with small face slots and progress rows; compact selected-person identity and details right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_projects"></a>

### Pinned projects and project detail

**ID**: `ui_projects`

**Name**: Pinned projects and project detail

**Owner officer**: none

**GDD refs**: §3, §7.3, §13.1

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: HUD/project source/recipe/build card; Summary; hub → Exact source caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Up to three selected projects, progress/remaining quantities and gold, known material source, next action, completion [§3/§13.1; projects/inventory/guild/discoveries]; suggested near-done/funding/future candidates labelled suggestion only [§3].

**Actions**: Pin → `pin_project`; unpin → `unpin_project`; source → `open_project_source` (proposed). Label any explicit replacement; pinning never reserves goods or spends money.

**States**: Empty — No pins: choose from visible recipes/orders/Annex. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Three already pinned: identify a pin to remove first; inaccessible source gives rank/story gate. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Source officer crop optional; waiting recruit idle-left frame.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_reports_journal"></a>

### Desk reports, journal and contacts

**ID**: `ui_reports_journal`

**Name**: Desk reports, journal and contacts

**Owner officer**: none; Tristitia for supplied reports

**GDD refs**: §5a.3, §11.2, §16a

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: Commander desk at night; proposed hub Journal; contact/history link → Desk/world/hub caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Recorded daily trends (cash/operations/readiness from Summary), requests/customer aftermath/recurrence, discoveries and inactive Eurydica record [§5a.3/§11.2/§16a; journal/repeat_orders/discoveries]; active base context [§16a; active_base_id].

**Actions**: Browse → `open_journal_entry`; source/profile → `open_record_source` (UI proposals). Read reports earns no skill/bond points and no inactive-base production.

**States**: Empty — No recorded history: explain no reports yet. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unknown/unrecorded content remains unavailable; request-owned accepted delivery access stays available after transfer. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: NPC name-only without portrait; important profile opens full uncropped portrait; staff mini faces idle-left.

**Three Houses pattern**: R03 (Important NPC Profile I prefer to have the portrait full size on the left not cropped since prolly there will be plenty negative space.png): tabbed dossier with identity at left and history/details at right. Owner alteration: full uncropped portrait on the left for important NPC profiles. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G24 — Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_night"></a>

### Night HUD / evening state

**ID**: `ui_night`

**Name**: Night HUD / evening state

**Owner officer**: none

**GDD refs**: §4.2, §5a.3

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Day Summary completion → World night; bed/01:00 leads to Sleep.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: Night time, closed operations state, objective/personal routes [§4.2; clock/story]; talks/meals/reports, adventurers until 21:00, officer free-time routines, 01:00 auto-sleep [§5a.3; clock/roster/story]. Existing HUD children remain.

**Actions**: Walk/talk/eat/reports → existing world actions; bed → `open_sleep`; no new hunt/production dispatch. No new day just from closing Summary.

**States**: Empty — No night-specific task: ordinary free time remains. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Operating actions: reopen next operating day; departed-to-bed adventurer unavailable after 21:00 except request guarantees where applicable. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: World actors only; conversation uses established portraits.

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right. R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule.

**Input**: WASD/arrows or ground click; left stick. Hold Shift/B to run, E/Space/Enter/click or A to interact; Tab/Y opens Ongoing; P/1/2/4 or D-pad controls speed (§13).

**Gaps**: G06 — Commander personal-activity details are incomplete: HQ kitchen opening predicate, meal duration, shared-meal selection and gift-shop catalogue/prices. Do not invent time costs or stock. G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_sleep"></a>

### Sleep confirmation and night transition

**ID**: `ui_sleep`

**Name**: Sleep confirmation and night transition

**Owner officer**: none

**GDD refs**: §4.1–§4.2, §6.3; FGC_07 §04

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Bed after 20:00; automatic at 01:00 → Manual Cancel returns to night; committed transition to Morning.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Current time and 07:00 destination, once-only overnight +1 stamina capped four, injury/request/debt/construction timers affected [§4.1/§6.3; clock/roster/construction/requests/guild]; no overnight production/buyers [§4.1].

**Actions**: Labelled Sleep → `sleep_until_morning` (proposed); Cancel before commit → `close_sleep`. At 01:00 automatic transition, no consent timer/new penalty. `sleep` state processes only remaining night hours, autosaves and opens Morning (§04).

**States**: Empty — No recovery needed: still valid sleep. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Before 20:00: bed cannot end operating day; exact condition shown. During committed transition no Back that undoes accounting. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No portrait required.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below.

**Input**: §13 Enter/click/A sleeps, Esc/right click/B cancels before commit; auto-sleep needs no input.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_morning"></a>

### Morning screen

**ID**: `ui_morning`

**Name**: Morning screen

**Owner officer**: none; Tristitia proposed briefing

**GDD refs**: §3, §4, §12.5, §5a.2a; FGC_07 §04

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Sleep/night jump and new-day autosave → World at 07:00 paused; resume only through speed controls.

**Clock**: FGC_07 §04 `sleep` handoff to morning: display paused after the once-only jump/autosave; Continue leaves world at 07:00 paused. No battle pace.

**Shows**: Proposed arrangement of actual new day/time, overnight stamina/injury outcomes, payroll/deadline/construction changes [§4/§6.3/§13; clock/journal/roster]; morning forecasts/rumours/negotiation order and resumed valid queues [§12.1/§12.5/§5a.2a; information/negotiation/processing/workshop]; pins/readiness [§3; projects]. No authored extra daily reward.

**Actions**: Inspect → `open_morning_source`; Continue → `acknowledge_morning` (application proposal). Acknowledge never unpauses or credits a second sleep bar.

**States**: Empty — No morning opportunity: show real events only. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Incomplete autosave/load recovery: explain actual error, avoid double morning delivery. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait if briefing adopted; readiness faces idle-left.

**Three Houses pattern**: R04 (Maybe For Main Menu.png): vertical action cards left, large contextual panel right, description strip and button hints below; its calendar is not an FGC rule. R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G16 — The morning screen is named in FGC_07 §04 but its precise contents and acknowledgement flow are not authored; proposed contents are existing morning events only. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_city_bell"></a>

### City bell cue (no required visual screen)

**ID**: `ui_city_bell`

**Name**: City bell cue (no required visual screen)

**Owner officer**: none

**GDD refs**: §4.3

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: 09:00/12:00/15:00/18:00 while outdoors in Eurydica → World unchanged.

**Clock**: Does not pause in `world` (FGC_07 §04; GDD §4); respects chosen Pause/1×/2×/4×. No battle pace outside a watched fight.

**Shows**: No required visual fields. Audible clock cue, roughly 8–10 seconds; north-bank louder/South Gate softer [§4.3; clock + Audio/world location]. Optional caption would show cue/time only, pending G17.

**Actions**: No action or commit; `play_city_bell` (presentation event proposal). No pause, rule change or mandatory modal.

**States**: Empty — Indoors, field, other times: silent. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — No Frontier sound until authored for that base; don't reuse Eurydica bell by assumption. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R09 (Notification on the Left.png): compact objective/notification strips left, minimap upper right, contextual label near the NPC and hints bottom right.

**Input**: No direct input; inherits the host's §13 controls. Any optional focus/inspection control is explicitly proposed.

**Gaps**: G17 — City bell has no specified visual UI or caption option. Keep it audio-only unless an accessibility indicator is approved; no mandatory popup. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_chapter_transition"></a>

### Chapter conclusion / readiness warning

**ID**: `ui_chapter_transition`

**Name**: Chapter conclusion / readiness warning

**Owner officer**: Tristitia

**GDD refs**: §11.1, §14, §16a

**Milestone/sprint**: M3 / S7 Chapter 1 flow.

**Opens from / returns to**: Player elects Chapter 1 conclusion; later Chapter 2 transition beat → Cancel returns to caller; commit runs authored transition scene.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Three officer-joining completion states [§14; story]; unaccepted CH1-REQ-003…007 that disappear at Ch1 end, accepted carryover and separate 001/002 timers [§11.1; requests]; later charter/readiness C+Crownstone+zero-debt and transition beat [§13.4/§16a; story/guild].

**Actions**: Review request → `open_request`; labelled Conclude chapter → `conclude_chapter` (proposed); Cancel → `close_chapter_review`. Autosave before/after chapter change; don't require every side request or max XP.

**States**: Empty — No expiring local offers: still show chapter readiness. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Chapter1 needs Commerce/Crafting/Information officers joined; later readiness uses exact charter predicates. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; no invented Frontier character preview.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R07 (Modal Info 1.png): small centred parchment information card over the retained world.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G22 — Chapter conclusion and permanent Bond 5 choice need final authored warning/confirmation copy; no additional unlock threshold is implied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_frontier_transfer"></a>

### Frontier transfer quote and departure

**ID**: `ui_frontier_transfer`

**Name**: Frontier transfer quote and departure

**Owner officer**: Tristitia

**GDD refs**: §16a–§16a.1, §15

**Milestone/sprint**: Later: Chapter 2/Frontier content as applicable; no assigned sprint in FGC_09 M1–M3.

**Opens from / returns to**: Chapter2 transition beat; Office relocation route → Cancel before transfer to readiness/Office; confirmed transfer to checkpoints/Arrival.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: 1,500G/48 calendar-hour quote, actual departure+48h arrival, preconditions [§16a; transfer/guild/clock]; full carryover persons/former staff/XP/builds/gear/items/requests/flags/capacities [§16a]; payroll dates/amounts during travel; protected accepted delivery exact remainders vs unaccepted offers/optional contracts still expiring; local recurring suspension [§16a; requests/contracts/repeat_orders]; expedition/construction/production/listing cleanup/refund preview.

**Actions**: Inspect cleanup routes → `open_transfer_requirement`; labelled Confirm transfer → `begin_transfer` (proposed). Revalidate transition/charter/no debt/fee, no active expedition/construction; settle/cancel production and cancel listings with disclosed refunds; no extra capacity purchase.

**States**: Empty — No transferable stock still retains identity/capacity/obligations. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — List each exact unsatisfied condition; finish/recall each operation, finish/cancel build, clear debt and afford fee; no invented travel deadline. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; people rows idle-left, officer crops.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G20 — Transfer checkpoint presentation and cancellation after departure are not defined; only pre-confirmation Cancel is promised. Arrival content and later region labels must be authored. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_transfer_checkpoint"></a>

### Transfer progress / payroll checkpoint / arrival ledger

**ID**: `ui_transfer_checkpoint`

**Name**: Transfer progress / payroll checkpoint / arrival ledger

**Owner officer**: Tristitia

**GDD refs**: §16a, §16b; FGC_07 §04

**Milestone/sprint**: Later: Chapter 2/Frontier content as applicable; no assigned sprint in FGC_09 M1–M3.

**Opens from / returns to**: Confirmed transfer; crossed payroll boundary; arrival → Payroll returns to transfer; Arrival continues to world paused at arrival time.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Departure/arrival/time remaining, chronological ledger, two crossed-night credits (no second arrival credit), injury expiry/healthy-hour healing, debts/wages [§16a; transfer/clock/roster/guild]; protected deadline remainders/resumption, suspended local operations/recurrence, carried capacity and active-base change [§16a; requests/construction/active_base_id]; no verified-route authority before later story beat.

**Actions**: Continue checkpoint → `advance_transfer_checkpoint`; payroll → `open_payroll`; Save → `open_save`; arrival acknowledge → `acknowledge_arrival` (proposed). Time advance is explicit calendar transfer, not ordinary live production. No post-departure cancellation invented.

**States**: Empty — No changed ledger row: show transfer state, no fabricated event. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Payroll shortage pauses for ordinary full-balance allocation; no hidden paid wages in transfer fee. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Tristitia portrait; affected employees idle-left framed.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G20 — Transfer checkpoint presentation and cancellation after departure are not defined; only pre-confirmation Cancel is promised. Arrival content and later region labels must be authored. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_save"></a>

### Save game

**ID**: `ui_save`

**Name**: Save game

**Owner officer**: none

**GDD refs**: §16b, §15; FGC_07 §08/§09

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: Hub/settings; world/management/combat; transfer checkpoint → Exact caller after save; simulation stays paused while overlay open.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Selected profile, unlimited named manual slots, three rotating autosaves, schema/content revision/time and safe scene checkpoint [§16b; Saves/story]; save status/last-good backup [§16b; Saves].

**Actions**: Edit name → `edit_save_name`; labelled Save → `save_campaign`; overwrite existing manual slot with explicit destination confirmation → `overwrite_save` (application proposals). Atomic write/checksum/backup; repeat clicks don't create unintended duplicate transaction.

**States**: Empty — No manual saves: Create named save. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — I/O failure: preserve existing save/backup; show failed path/reason safely. Mid-cutscene stores latest safe scene checkpoint, not arbitrary text cursor. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No portraits required.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G05 — Starting New Game flow beyond profile/scene handoff is undefined: title art, default save selection, profile replacement/deletion policy and initial difficulty placement. G23 — Boot validation failure/report and save corruption UI need player-facing diagnostics and recovery copy; integrity mechanics exist, diagnostic wording does not. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_load"></a>

### Load and backup recovery

**ID**: `ui_load`

**Name**: Load and backup recovery

**Owner officer**: none

**GDD refs**: §16b, §15; FGC_07 §08

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: Title/profile; hub Save/Load; save-error recovery → Cancel to caller; successful load to saved context paused.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Profile/manual/autosave slots, names/schema/content revision/time, validity and last-good recovery availability [§16b; Saves]; migration notices for returned invalid reservations [§16b; inventory/reservations].

**Actions**: Select → `preview_save`; labelled Load → `load_campaign`; labelled Recover backup → `recover_backup` (application proposals). Warn about current unsaved progress before replacement; no offline progression or reroll/replayed payout.

**States**: Empty — No saves: New Game route. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Invalid save: show integrity/version issue and verified backup option if present; never silently erase/reset campaign. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R07 (Modal Info 1.png): small centred parchment information card over the retained world.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G23 — Boot validation failure/report and save corruption UI need player-facing diagnostics and recovery copy; integrity mechanics exist, diagnostic wording does not. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_settings"></a>

### Settings

**ID**: `ui_settings`

**Name**: Settings

**Owner officer**: none

**GDD refs**: §2.5, §15–§16b; FGC_07 §12/§13/§15

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Title; hub; save/load family → Exact caller; restore previous chosen speed when last overlay closes.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Font/UI scale, reduced shake/flash/VFX, optional cinematic zoom, battle pace and speed controls [§15/§16b; Settings]; active/pending difficulty link [§16b; difficulty]; proposed audio controls reflect Master/Music/SFX/UI buses, unused Voice not presented as supported speech [FGC_07 §15].

**Actions**: Preview visual setting → `preview_setting`; labelled Apply → `apply_settings`; Cancel → `discard_settings_draft`; difficulty → `open_difficulty` (application proposals). Visual settings never change combat outcome.

**States**: Empty — No campaign: presentation settings remain; no pending-campaign difficulty fabricated. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Unsupported value shows valid configured choice after ranges approved; do not invent scale min/max. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G21 — Font/UI-scale ranges, reduced-VFX controls/defaults and audio setting ranges are not specified. Do not manufacture resolution, size or timing limits. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_difficulty"></a>

### Difficulty selection / next-day change

**ID**: `ui_difficulty`

**Name**: Difficulty selection / next-day change

**Owner officer**: none

**GDD refs**: §16b

**Milestone/sprint**: M3 / S7 (proposed for complete New Game/Chapter 1 flow; not individually assigned in FGC_09).

**Opens from / returns to**: New Game setup; Settings → Caller; active campaign change pending until next 07:00.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Standard vs Relaxed, current and pending mode/effective boundary [§16b; difficulty/clock]; identical combat/loot/market, injury 48h vs24h, wage ×1 vs×0.75, new timed durations baseline vs×2 [§16b]; unchanged existing injury/deadline and transfer/debt/payroll/stamina rules.

**Actions**: Preview → `preview_difficulty`; labelled Schedule change → `set_pending_difficulty` (proposed); New Game records selected initial mode with Start. No repeated extension of existing deadlines.

**States**: Empty — No pending change: show current mode. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Existing timers unchanged; no permadeath choice. Apply waits until next 07:00, not the next button click. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: none

**Three Houses pattern**: R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G05 — Starting New Game flow beyond profile/scene handoff is undefined: title art, default save selection, profile replacement/deletion policy and initial difficulty placement. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_session_offer"></a>

### Working-session offer / daily negotiation order

**ID**: `ui_session_offer`

**Name**: Working-session offer / daily negotiation order

**Owner officer**: Elsie / Valerie / Liliana / Mae / Fulker

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Owning department/talk; Commander skill link → Owning department/talk; completed play goes to its result.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Session kind, officer/presence, today-used flag, relevant skill/rank/cap/points and required work item [§5a.2; commander/roster/story]; one-hour Guild time cost, hint A cap and grade rewards [§5a.2a/§5.4; commander/bonds]; Valerie's daily order buyer/item/quantity/market value/expires20:00, drawn from fitting unreserved storage [§5a.2a; negotiation/inventory/reservations].

**Actions**: Preview → `preview_session`; labelled Begin one-hour session → `start_session` (proposed); Cancel → `close_session_offer` (UI). Reserve/revalidate context through authoritative session transaction, never by browsing. Completed play sends existing §14 `session_result` once; results are receipts.

**States**: Empty — No matching sellable storage: Valerie has no order today; Mae/Fulker show exact required queued/active job. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Once per officer/day, present, operating hours and something to work on; Mae needs corpse queued/processing; Fulker crafting/enhancement queued/active, not Reworking. Late/cutoff/abort policy remains G09. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Owning officer large portrait and waist-length before/after dialogue; buyer portrait where supplied, otherwise name only.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_expedition_planning_play"></a>

### Expedition Planning — play

**ID**: `ui_expedition_planning_play`

**Name**: Expedition Planning — play

**Owner officer**: Elsie

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: ui_session_offer at Elsie → Own result screen on completion; abort return policy G09.

**Clock**: Paused `overlay` during play; `session_result` advances one Guild hour with ordinary operations once (FGC_07 §14; GDD §5a.2). No battle pace. Cutoff/abort edge is G09.

**Shows**: Map grid 9×7 Eurydica/up to15×11 Frontier, start/goal, road1/grass2/forest3/marsh4 hour costs, cliffs/deep water blocked, threat radii, water/rest spots, 12h budget/10 stamina, route and up-to-two rests costing2h/restoring3 stamina [§5a.2a; commander session template]. Later fog, one mid-route event and double-cost night tiles only with authored Frontier templates. One free hint, grade capped A when used, session skill/bond effects and one-hour cost [§5a.2a/§5.4; commander/bonds].

**Actions**: Draw route → `edit_planning_route`; undo → `undo_planning_step`; place rest → `place_planning_rest` (UI proposals). Labelled Dispatch tests the puzzle route, not a real expedition; final route outcome → `session_result` exactly once. Hint → `use_session_hint` (local proposal) displays A-cap before use. Outcome commit is tied to session ID; repeating finish cannot grant another hour or reward.

**States**: Empty — No eligible authored puzzle/context: remain at offer with no consumed daily session. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Invalid/impassable next tile or rest without rest spot/water: show exact correction; time/stamina exhaustion is D, not a disabled finish. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Elsie waist-length portrait in before/after/commentary dialogue; optional painted crop in board header. Counter-offer uses current buyer expression, no fabricated NPC face.

**Three Houses pattern**: R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text. The puzzle itself comes from GDD §5a.2a; these screenshots supply framing and information hierarchy, not a claimed matching puzzle reference.

**Input**: Mouse draws/selects tiles; proposed arrows/stick cursor, Enter/A append, Z/X undo, R/RB rest, labelled Dispatch; Esc/B cancellation is G09. Core accept/cancel from §13.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_expedition_planning_result"></a>

### Expedition Planning — result

**ID**: `ui_expedition_planning_result`

**Name**: Expedition Planning — result

**Owner officer**: Elsie

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Completed Expedition Planning play and authoritative session_result receipt → Elsie's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Hours/stamina left, threats crossed, solver-best comparison, grade S within5%/A15%/B30%/C goal reached/D budget failure [§5a.2a; session receipt]; Briefed next party today: starts each fight +10 meter, S +15; failed-output interpretation G09 [§5a.2a; commander]. Leadership points D1/C2/B3/A4/S5, previous→new cumulative points/rank with Eurydica rank2 cap; officer bond D0/C1/B2/A2/S3 with thresholds/weekly/story gate, hint flag/A cap, settled one-hour start→end [§5a.2/§5.4; commander/bonds/clock]. Fitting has no D branch.

**Actions**: Continue → `acknowledge_session_result`; inspect applied output → `open_session_output` (UI proposals). Result is already committed by `session_result`; Continue never reapplies sale/bonus/points/time. No replay for a better grade today.

**States**: Empty — No result receipt: return to unresolved session state, never synthesize rewards. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Daily session spent: next attempt next day with eligible work. Pending cutoff takes priority after safe result acknowledgement; failed reward interpretation remains G09. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Elsie waist-length after-session portrait; painted crop in result header if needed; buyer name/portrait only for negotiation receipt.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_counter_offer_play"></a>

### Counter-offer — play

**ID**: `ui_counter_offer_play`

**Name**: Counter-offer — play

**Owner officer**: Valerie

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: ui_session_offer at Valerie → Own result screen on completion; abort return policy G09.

**Clock**: Paused `overlay` during play; `session_result` advances one Guild hour with ordinary operations once (FGC_07 §14; GDD §5a.2). No battle pace. Cutoff/abort edge is G09.

**Shows**: Daily buyer persona/portrait/tell, ordered item/quantity/quality, market value, asking-price slider, patience/round progress (3–5), tactic choices Hold firm/Show quality/Add a unit/Mention another buyer/Give ground [§5a.2a; negotiation/inventory]. Hidden ceiling80–140% and acceptance are NOT shown; no exact hidden number in tooltip. Later authored barter/bundles and active-region buyers only. One free hint, grade capped A when used, session skill/bond effects and one-hour cost [§5a.2a/§5.4; commander/bonds].

**Actions**: Price/tactic draft → `edit_counter_offer`; labelled Make offer → `submit_counter_offer_round` (session-local proposal); hint → shared session hint. Accepted final deal/failure → `session_result` with actual sale once; no listing fee, preview exact units/price before Make offer. Hint → `use_session_hint` (local proposal) displays A-cap before use. Outcome commit is tied to session ID; repeating finish cannot grant another hour or reward.

**States**: Empty — No eligible authored puzzle/context: remain at offer with no consumed daily session. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Order expires at20:00; requires sellable unreserved specified stock, no invented order on empty day; Show quality only helps Standard/Pristine; bundle requires extra available unit. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Valerie waist-length portrait in before/after/commentary dialogue; optional painted crop in board header. Counter-offer uses current buyer expression, no fabricated NPC face.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R14 (Screenshot 2026-09-28 135745.png): bottom dialogue band with nameplate, portrait beside it, advance indicator and log/auto hints; FGC changes portrait framing to waist length and uses both speaker slots. R05 (Menu.png): centred settings list with tabs above, left/right value selectors, help strip below. The puzzle itself comes from GDD §5a.2a; these screenshots supply framing and information hierarchy, not a claimed matching puzzle reference.

**Input**: Mouse slider/tactic buttons; proposed Left/Right or stick changes price, A selects tactic/Make offer, B returns from draft only under G09; no invented price-step size. §13 accept/cancel.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_counter_offer_result"></a>

### Counter-offer — result

**ID**: `ui_counter_offer_result`

**Name**: Counter-offer — result

**Owner officer**: Valerie

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Completed Counter-offer play and authoritative session_result receipt → Valerie's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Agreed units/price or buyer walked/no sale, grade from final-price/hidden-ceiling ratio S≥95%/A≥85%/B≥70%/C deal/D patience exhausted [§5a.2a; negotiation receipt]; actual removed lots, gold/barter receipt/no listing fee and any applicable debt-sweep ledger [§5a.2a/§13.4; inventory/guild]. Do not disclose hidden ceiling merely to explain grade. Negotiation points D1/C2/B3/A4/S5, previous→new cumulative points/rank with Eurydica rank2 cap; officer bond D0/C1/B2/A2/S3 with thresholds/weekly/story gate, hint flag/A cap, settled one-hour start→end [§5a.2/§5.4; commander/bonds/clock]. Fitting has no D branch.

**Actions**: Continue → `acknowledge_session_result`; inspect applied output → `open_session_output` (UI proposals). Result is already committed by `session_result`; Continue never reapplies sale/bonus/points/time. No replay for a better grade today.

**States**: Empty — No result receipt: return to unresolved session state, never synthesize rewards. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Daily session spent: next attempt next day with eligible work. Pending cutoff takes priority after safe result acknowledgement; failed reward interpretation remains G09. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Valerie waist-length after-session portrait; painted crop in result header if needed; buyer name/portrait only for negotiation receipt.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_cross_check_play"></a>

### Cross-check — play

**ID**: `ui_cross_check_play`

**Name**: Cross-check — play

**Owner officer**: Liliana

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: ui_session_offer at Liliana → Own result screen on completion; abort return policy G09.

**Clock**: Paused `overlay` during play; `session_result` advances one Guild hour with ordinary operations once (FGC_07 §14; GDD §5a.2). No battle pace. Cutoff/abort edge is G09.

**Shows**: Desk with2–4 authored documents; selectable distances/directions/landmarks/counts/dates/times; 3–6 conflicts; source provenance/date/position/weather clues, discrepancy links/resolution choice, candle about3min [§5a.2a; commander session template]. Later mixed units/forgeries/rival records must be authored. One free hint, grade capped A when used, session skill/bond effects and one-hour cost [§5a.2a/§5.4; commander/bonds].

**Actions**: Link facts → `link_report_facts`; remove/change link → `edit_report_link`; trust source → `resolve_discrepancy`; labelled Finish record → `session_result` (local commands proposed except existing result). False links cost score; timeout lowers one grade, never fails alone. Hint → `use_session_hint` (local proposal) displays A-cap before use. Outcome commit is tied to session ID; repeating finish cannot grant another hour or reward.

**States**: Empty — No eligible authored puzzle/context: remain at offer with no consumed daily session. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Choose two facts from documents then trust an evidenced source; missing template fails load rather than invented facts. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Liliana waist-length portrait in before/after/commentary dialogue; optional painted crop in board header. Counter-offer uses current buyer expression, no fabricated NPC face.

**Three Houses pattern**: R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. R11 (Region Map.png): parchment map left, selectable destination list upper right, contextual detail/reward card lower right. The puzzle itself comes from GDD §5a.2a; these screenshots supply framing and information hierarchy, not a claimed matching puzzle reference.

**Input**: Click two facts then trust choice; proposed stick/arrows fact cursor, A selects endpoint/source, X removes draft link, LB/RB document; §13 B follows G09.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_cross_check_result"></a>

### Cross-check — result

**ID**: `ui_cross_check_result`

**Name**: Cross-check — result

**Owner officer**: Liliana

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Completed Cross-check play and authoritative session_result receipt → Liliana's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Found/correctly resolved discrepancies, false links, timeout/hint modifiers; S all correct/no false links, A all found, B≥70% found, C≥one, D none [§5a.2a; session receipt]; exact rumour→lead/new known-area find, later surveyed route / Guild Verified only after authority [§5a.2a/§16a; information/discoveries/story]; no double path search bonus. Insight points D1/C2/B3/A4/S5, previous→new cumulative points/rank with Eurydica rank2 cap; officer bond D0/C1/B2/A2/S3 with thresholds/weekly/story gate, hint flag/A cap, settled one-hour start→end [§5a.2/§5.4; commander/bonds/clock]. Fitting has no D branch.

**Actions**: Continue → `acknowledge_session_result`; inspect applied output → `open_session_output` (UI proposals). Result is already committed by `session_result`; Continue never reapplies sale/bonus/points/time. No replay for a better grade today.

**States**: Empty — No result receipt: return to unresolved session state, never synthesize rewards. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Daily session spent: next attempt next day with eligible work. Pending cutoff takes priority after safe result acknowledgement; failed reward interpretation remains G09. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Liliana waist-length after-session portrait; painted crop in result header if needed; buyer name/portrait only for negotiation receipt.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_cutting_chart_play"></a>

### Cutting Chart — play

**ID**: `ui_cutting_chart_play`

**Name**: Cutting Chart — play

**Owner officer**: Mae

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: ui_session_offer at Mae → Own result screen on completion; abort return policy G09.

**Clock**: Paused `overlay` during play; `session_result` advances one Guild hour with ordinary operations once (FGC_07 §14; GDD §5a.2). No battle pace. Cutoff/abort edge is G09.

**Shows**: Selected queued/processing corpse ID/species diagram,3–6 dotted cut guides, red no-cut zones, current stroke, accuracy/steadiness feedback [§5a.2a; processing session template]. Exact scoring weights/speed band are G08; never expose hidden quality roll. One free hint, grade capped A when used, session skill/bond effects and one-hour cost [§5a.2a/§5.4; commander/bonds].

**Actions**: Trace → `trace_cut`; next cut → `advance_cut`; labelled Finish cutting → `session_result` (local proposals/result existing). Crossing no-cut zone ruins that cut; no invented restart loop. Hint → `use_session_hint` (local proposal) displays A-cap before use. Outcome commit is tied to session ID; repeating finish cannot grant another hour or reward.

**States**: Empty — No eligible authored puzzle/context: remain at offer with no consumed daily session. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Require actual corpse in processing/queue; wrong/missing species diagram is content error. No-cut crossing reduces grade, doesn't delete corpse. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Mae waist-length portrait in before/after/commentary dialogue; optional painted crop in board header. Counter-offer uses current buyer expression, no fabricated NPC face.

**Three Houses pattern**: R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. The puzzle itself comes from GDD §5a.2a; these screenshots supply framing and information hierarchy, not a claimed matching puzzle reference.

**Input**: Mouse traces one stroke; proposed left-stick cursor with held A draws, release ends stroke; §13 Back governed by G09. Controller precision/speed equivalence needs prototype validation.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G10 — Processing quality visibility conflicts: §12.1/§15 ask for odds while §5a.2 reserves seeing pre-start odds to Trained eye at rank 3. Exact public fields before rank 3 need reconciliation within the GDD. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_cutting_chart_result"></a>

### Cutting Chart — result

**ID**: `ui_cutting_chart_result`

**Name**: Cutting Chart — result

**Owner officer**: Mae

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Completed Cutting Chart play and authoritative session_result receipt → Mae's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Per-cut/average score and grade S≥90/A≥75/B≥55/C≥30/D below30 [§5a.2a; receipt]; same job's Pristine odds +5/+8/+11/+15 points C/B/A/S from Standard, D no worsening; retained corpse roll and quality-visibility conflict [§12.1/§5a.2; processing]. Know-how points D1/C2/B3/A4/S5, previous→new cumulative points/rank with Eurydica rank2 cap; officer bond D0/C1/B2/A2/S3 with thresholds/weekly/story gate, hint flag/A cap, settled one-hour start→end [§5a.2/§5.4; commander/bonds/clock]. Fitting has no D branch.

**Actions**: Continue → `acknowledge_session_result`; inspect applied output → `open_session_output` (UI proposals). Result is already committed by `session_result`; Continue never reapplies sale/bonus/points/time. No replay for a better grade today.

**States**: Empty — No result receipt: return to unresolved session state, never synthesize rewards. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Daily session spent: next attempt next day with eligible work. Pending cutoff takes priority after safe result acknowledgement; failed reward interpretation remains G09. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Mae waist-length after-session portrait; painted crop in result header if needed; buyer name/portrait only for negotiation receipt.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G10 — Processing quality visibility conflicts: §12.1/§15 ask for odds while §5a.2 reserves seeing pre-start odds to Trained eye at rank 3. Exact public fields before rank 3 need reconciliation within the GDD. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_fitting_play"></a>

### Fitting — play

**ID**: `ui_fitting_play`

**Name**: Fitting — play

**Owner officer**: Fulker

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: ui_session_offer at Fulker → Own result screen on completion; abort return policy G09.

**Clock**: Paused `overlay` during play; `session_result` advances one Guild hour with ordinary operations once (FGC_07 §14; GDD §5a.2). No battle pace. Cutoff/abort edge is G09.

**Shows**: Target crafting/enhancement job, jig grid/frame, fixed pegs, notched part tray, required first key part, placements, moves/time/par [§5a.2a; workshop session template]. Frontier authored adjacency/unstable materials only; par algorithm is G08. One free hint, grade capped A when used, session skill/bond effects and one-hour cost [§5a.2a/§5.4; commander/bonds].

**Actions**: Drag/rotate/drop → `place_fitting_part`; undo → `undo_fitting_move` (counts as move); ask Fulker to finish → `assist_fitting`; labelled Complete fitting → `session_result` (local proposals/result existing). Grid preview doesn't consume production materials. Hint → `use_session_hint` (local proposal) displays A-cap before use. Outcome commit is tied to session ID; repeating finish cannot grant another hour or reward.

**States**: Empty — No eligible authored puzzle/context: remain at offer with no consumed daily session. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Requires queued/active crafting or enhancement; key part first, all cells filled and pegs in notches. Invalid placement retains part; Fulker completion gives C, no D. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Fulker waist-length portrait in before/after/commentary dialogue; optional painted crop in board header. Counter-offer uses current buyer expression, no fabricated NPC face.

**Three Houses pattern**: R02 (Adventurer Stat.png): compact identity card left, selectable equipment list right, numeric comparison rows beneath. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom. The puzzle itself comes from GDD §5a.2a; these screenshots supply framing and information hierarchy, not a claimed matching puzzle reference.

**Input**: Mouse select/drag and click placement; proposed arrows/controller stick move a grid cursor, Enter/A pick/drop, R/RB rotate 90°, Z/X undo, Esc/right click/B cancel the current draft operation. Confirm remains a labelled button (§13 base actions; missing grid bindings proposed).

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. G25 — FGC_09 S8 exit wording says each session D–S, but GDD Fitting has no D and completes with C assistance. GDD wins; sprint acceptance must preserve that exception. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_fitting_result"></a>

### Fitting — result

**ID**: `ui_fitting_result`

**Name**: Fitting — result

**Owner officer**: Fulker

**GDD refs**: §5a.2–§5a.2a, §5.4; FGC_07 §14

**Milestone/sprint**: M3 / S8 working sessions/bonds.

**Opens from / returns to**: Completed Fitting play and authoritative session_result receipt → Fulker's department/talk; if one-hour settlement triggers cutoff, safe handoff to Resolution.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Moves/time versus par, assistance/hint use, S at/under par, A+25%, B+50%, C complete/assisted [§5a.2a; receipt]; job duration reduction10/15/20/25% C/B/A/S [§5a.2a; workshop]; no D grade despite FGC_09 S8 shorthand. Know-how points D1/C2/B3/A4/S5, previous→new cumulative points/rank with Eurydica rank2 cap; officer bond D0/C1/B2/A2/S3 with thresholds/weekly/story gate, hint flag/A cap, settled one-hour start→end [§5a.2/§5.4; commander/bonds/clock]. Fitting has no D branch.

**Actions**: Continue → `acknowledge_session_result`; inspect applied output → `open_session_output` (UI proposals). Result is already committed by `session_result`; Continue never reapplies sale/bonus/points/time. No replay for a better grade today.

**States**: Empty — No result receipt: return to unresolved session state, never synthesize rewards. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Daily session spent: next attempt next day with eligible work. Pending cutoff takes priority after safe result acknowledgement; failed reward interpretation remains G09. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Fulker waist-length after-session portrait; painted crop in result header if needed; buyer name/portrait only for negotiation receipt.

**Three Houses pattern**: R06 (Mini Game Result.png): activity header, prominent grade band, separate outcome bands, progress rows below. R13 (Request-Contract Reward.png): separate horizontal reward bands over the retained scene, one outcome per row.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G08 — Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. G09 — Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. G14 — Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. G25 — FGC_09 S8 exit wording says each session D–S, but GDD Fitting has no D and completes with C assistance. GDD wins; sprint acceptance must preserve that exception. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_confirm"></a>

### Commit confirmation / irreversible-choice review

**ID**: `ui_confirm`

**Name**: Commit confirmation / irreversible-choice review

**Owner officer**: inherit originating department, otherwise none

**GDD refs**: §15; action-specific GDD section

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: A labelled action needing cost, destructive change or permanent-choice review → Exact caller with draft and focus preserved; committed action returns receipt.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Action-specific resource/person/capacity changes, exact quantities/fees/refunds, result and all unmet requirements [§15; relevant read model]; payroll reserve crossing where spending [§13.1; guild]; permanence for Bond5 [§5.4; bonds]. No invented generic fee.

**Actions**: Confirm → originating snake_case command in its screen entry; Cancel → `cancel_confirmation` (UI proposal). Expected revision, command ID and atomic validation follow FGC_07 §07.1. A second click reuses the receipt. Recall remains immediate and need not pass this modal.

**States**: Empty — No material change in draft: explain nothing to commit. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Exact authoritative requirement returned by action, including quantities and reservation owner where relevant; no generic disabled Confirm. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Optional owning officer crop; employee references idle-left framed; no new face requirement.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. G22 — Chapter conclusion and permanent Bond 5 choice need final authored warning/confirmation copy; no additional unlock threshold is implied. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_info_help"></a>

### Context information / tutorial / tooltip detail

**ID**: `ui_info_help`

**Name**: Context information / tutorial / tooltip detail

**Owner officer**: inherit department if guidance, otherwise none

**GDD refs**: §3, §6–§15; FGC_07 §12

**Milestone/sprint**: M2 / S5 (proposed integration alongside core UI; not individually assigned in FGC_09).

**Opens from / returns to**: Field/stat/item/rule help; authored dispatch and contract explanations → Exact caller; tutorial advances only its authored acknowledgement.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Selected sourced rule/effect, exact prerequisite/source link, item/stat interpretation [§6–§15; content + relevant aggregate]; authored tutorial text [§14; story]. Each invocation must carry its precise section/topic; no extra game systems inferred from FE references.

**Actions**: Inspect → `open_context_help`; close → `close_context_help` (UI); required tutorial acknowledgement → `acknowledge_tutorial` (proposed sim command tied to authored story predicate). Hover tooltip alone is passive and does not pause; opened detail is overlay.

**States**: Empty — No authored help: concise sourced field label only. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — No eligible story acknowledgement until its actual authored interaction; reading a tooltip doesn't unlock M03/M08. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: Officer waist-length if actual dialogue; ordinary tooltip no face; portraitless NPC name-only.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world. R08 (Modal Info 2.png): centred item card with icon/title, numeric rows and explanatory text.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G13 — Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_error_notice"></a>

### Command refusal / loading failure notice

**ID**: `ui_error_notice`

**Name**: Command refusal / loading failure notice

**Owner officer**: inherit caller, otherwise none

**GDD refs**: §15, §16b; FGC_07 §07.1/§04

**Milestone/sprint**: M2 / S5 dialogue and core UI.

**Opens from / returns to**: Failed command, missing content or save I/O; boot failures use ui_boot_report → Caller with uncommitted draft preserved; retry only after revalidation.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Readable reason and affected object/required next step, stable error category: stale_revision, invalid_argument, not_available, insufficient_gold, reserved, locked, cutoff or command_id_conflict [§15; FGC_07 §07.1 CommandResult]; no fake success/RNG advancement.

**Actions**: Refresh quote → `refresh_read_model`; Retry → same command with reconciled revision and proper idempotency ID semantics; Back → `close_error` (UI). Never blindly turn a rejected payload into a different paid action.

**States**: Empty — No error: no notice. Loading — wait for the relevant content/read model/receipt; show pending rather than zero values and retain the caller/draft. Blocked — Display concrete returned requirement, e.g. required minus available gold or specific competing reservation; unresolved content failure remains a diagnostic, not invented gameplay data. Error — preserve uncommitted edits, show the precise source/command failure and refresh/revalidate before retry; no successful result or RNG change is inferred (shared G18; save/boot-specific recovery uses its own entries).

**Faces and portraits**: No new face; retained caller portraits may remain behind card.

**Three Houses pattern**: R07 (Modal Info 1.png): small centred parchment information card over the retained world.

**Input**: E/Space/Enter/click or A to inspect/continue; Esc/right click or B to return (§13). Proposed: wheel/right stick scroll; arrows/stick choose rows.

**Gaps**: G18 — Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. G23 — Boot validation failure/report and save corruption UI need player-facing diagnostics and recovery copy; integrity mechanics exist, diagnostic wording does not. Shared focus/lifecycle/scale gaps remain as stated above.

<a id="ui_commander_rank_actions"></a>

### Commander rank-3 active abilities / Standing offer

**ID**: `ui_commander_rank_actions`

**Name**: Commander rank-3 active abilities / Standing offer

**Owner officer**: Elsie for encouragement; Valerie for Standing offer

**GDD refs**: §5a.2, §16a.1

**Milestone/sprint**: Later: Frontier rank-3 skills; no assigned sprint in FGC_09 M1–M3.

**Opens from / returns to**: Commander profile rank-3 unlock; Preparation; Commerce/negotiation counter → Exact profile/prep/counter caller.

**Clock**: Pauses in `overlay` (FGC_07 §04); restore the previous chosen speed only when the foreground overlay chain closes. No battle pace while covered.

**Shows**: Leadership rank3 Word of encouragement availability once/day, selected adventurer and next-dispatch Red Fatigue cancellation [§5a.2; commander/roster]; Negotiation rank3 Standing offer once/week, held material/available quantity, repeat-customer/trader and +20% order effect [§5a.2; commander/inventory/negotiation]; active-region content [§16a.1]; Insight Sharp ear and Know-how Trained eye are passive displays in Information/Processing, not extra spend buttons.

**Actions**: Select encouragement target → `preview_encouragement`; labelled Encourage → `use_word_of_encouragement`; preview Standing offer → `preview_standing_offer`; labelled Request Standing offer → `request_standing_offer` (proposed). Usage receipts prevent repeated daily/weekly spend; resulting order's sale/acceptance awaits G26, not an invented immediate payout.

**States**: Empty — No eligible next-dispatch target or held sellable material: show prerequisite, not random substitute. Loading — retain caller and wait for current usage/order read model; no fake order. Blocked — Requires relevant skill rank3 through harder Frontier sessions; show daily/weekly use state. Exact Standing offer fulfilment details G26 remain unavailable rather than fabricated. Error — preserve preview, show precise command failure, refresh before retry; no usage or sale assumed on failure.

**Faces and portraits**: Elsie/Valerie portrait; selected adventurer idle-left framed; customer portraitless name-only.

**Three Houses pattern**: R12 (Request, Rhea Replaced With Tristitia.png): two parchment cards: officer guidance left, request title, requirements and reward rows right. Use Tristitia, not the reference character. R16 (Staff Detail.png): identity above a short list left, large selected-detail card right, help and input hints at the bottom.

**Input**: E/Space/Enter or left click activates; Esc/right click cancels; gamepad A/B (FGC_07 §13). Proposed: arrows/stick navigate focus, Q/E or LB/RB change tabs when text entry is inactive, wheel/right stick scroll. Scope E to activation on screens without tab mode.

**Gaps**: G12 — Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. G26 — Rank-3 Standing offer specifies once/week, a held material and +20%, but not quantity selection, baseline price calculation detail, acceptance/deadline or buyer-generation contract. Keep undefined order fields unfilled until authored.

## C. Shared components

This is the painted asset/control kit, not a request to generate artwork. Component counts are logical reusable parts; state variants, nine-slice borders and glyph atlases do not multiply the count. “All entries” means shared shell/theme rules only; a passive bark does not acquire an interactive menu. Every consumer is an inventory ID, including later/proposed views. Original FGC artwork and GDD colours replace the reference artwork.

| Component ID | Reusable part and contract | Screens/elements using it |
|---|---|---|
| `cmp_theme` | **Theme, typography and status tokens** — Navy panels/top bar, gold frames/headings, parchment maps/notices, ink text; blue selection. Exact GDD §2.5 palette. Marcellus headings, Alegreya Sans all body text/numbers with lining figures; Pixelify Sans in-battle names only. | All entries, as applicable to their visible shell |
| `cmp_screen_frame` | **Screen frame and retained-context backdrop** — Shared panel border, heading area and world backdrop treatment. No imported FE crests, ornaments or text. | All entries, as applicable to their visible shell |
| `cmp_list_card` | **List card** — Selectable row surface, clear selected/focused/blocked/read states; selection never commits. | `ui_profile_select`, `ui_hub`, `ui_roster`, `ui_staff_roster`, `ui_recruitment`, `ui_ongoing`, `ui_processing`, `ui_workshop`, `ui_information`, `ui_commerce`, `ui_storage`, `ui_payroll`, `ui_request_board`, `ui_contracts`, `ui_load`, `ui_save` |
| `cmp_detail_card` | **Detail card** — Title, labelled facts, source-aware sections and actionable requirements; list selection updates read model only. | `ui_adventurer_profile`, `ui_officer_profile`, `ui_important_npc_profile`, `ui_staff_profile`, `ui_area_detail`, `ui_hunt_targets`, `ui_recipe_detail`, `ui_enhancement`, `ui_reworking`, `ui_request_board`, `ui_contracts`, `ui_flashpoint`, `ui_information`, `ui_storage`, `ui_commander_rank_actions` |
| `cmp_tab_bar` | **Tab bar** — Text tabs with visible focus; proposed controller bumpers do not conflict with activation. | `ui_settings`, `ui_roster`, `ui_progression`, `ui_officer_profile`, `ui_important_npc_profile`, `ui_request_board`, `ui_commerce`, `ui_workshop`, `ui_information`, `ui_storage`, `ui_load` |
| `cmp_stat_row` | **Stat row and delta bar** — Label/value/unit, current versus preview delta; all numbers lining figures; never fabricate max ranges. | `ui_commander_profile`, `ui_adventurer_profile`, `ui_staff_profile`, `ui_progression`, `ui_preparation`, `ui_enhancement`, `ui_battle_hud` |
| `cmp_small_face` | **Employee idle-left sprite frame** — Adventurers and staff use their own idle-left pixel sprite, framed; include normal/selected/restricted appearance without changing identity. | `ui_roster`, `ui_adventurer_profile`, `ui_staff_roster`, `ui_staff_profile`, `ui_recruitment`, `ui_preparation`, `ui_prep_templates`, `ui_ongoing`, `ui_battle_hud`, `ui_payroll`, `ui_rest_orders`, `ui_day_summary`, `ui_morning`, `ui_debt_rescue` |
| `cmp_officer_header` | **Officer header and guidance box** — Large painted officer portrait plus department/nameplate and authored guidance; small officer slots may use painted crop. | `ui_adventurer_office`, `ui_roster`, `ui_progression`, `ui_processing`, `ui_workshop`, `ui_recipe_detail`, `ui_enhancement`, `ui_reworking`, `ui_information`, `ui_commerce`, `ui_recruitment`, `ui_payroll`, `ui_rank`, `ui_flashpoint`, `ui_request_board`, `ui_resolution`, `ui_day_summary`, `ui_officer_profile` |
| `cmp_full_portrait` | **Full portrait dossier slot** — Full uncropped important-NPC portrait left, text/details right. Portraitless Eurydica NPCs name-only. | `ui_important_npc_profile`, `ui_officer_profile`, `ui_commander_profile`, `ui_romance` |
| `cmp_dialogue_portraits` | **Waist-length dialogue portrait slots** — Commander left/current other speaker right; 55% inactive dimming from spec; no face placeholder for portraitless NPCs. | `ui_dialogue`, `ui_talk_menu`, `ui_choices`, `ui_ambient`, `ui_meals`, `ui_session_offer`, `ui_expedition_planning_play`, `ui_expedition_planning_result`, `ui_counter_offer_play`, `ui_counter_offer_result`, `ui_cross_check_play`, `ui_cross_check_result`, `ui_cutting_chart_play`, `ui_cutting_chart_result`, `ui_fitting_play`, `ui_fitting_result` |
| `cmp_nameplate` | **Nameplate** — Authored display name including Fulker; distinguish internal IDs from player-facing Guild terminology. | `ui_dialogue`, `ui_ambient`, `ui_talk_menu`, `ui_narration`, `ui_name_entry`, `ui_guild_name_entry`, `ui_important_npc_profile`, `ui_battle_labels`, `ui_officer_profile` |
| `cmp_dialogue_box` | **Dialogue/thought box and advance cue** — 140px source textbox contract in FGC_07 §12.4; scale behavior G21. Thought italics/parentheses, no talk sound; reveal/advance indicator. | `ui_dialogue`, `ui_ambient`, `ui_talk_menu`, `ui_choices` |
| `cmp_narration_box` | **Narration card** — Centred, no name/portrait; separate from thought. | `ui_narration` |
| `cmp_choice_button` | **Choice/topic button** — Authored label, focus/read state; conditional topics hidden; nested choices and Leave. | `ui_choices`, `ui_talk_menu`, `ui_romance`, `ui_counter_offer_play`, `ui_cross_check_play` |
| `cmp_text_entry` | **Text-entry field** — Draft, selected text, validation message and labelled Confirm; lengths/defaults undefined. | `ui_name_entry`, `ui_guild_name_entry`, `ui_save`, `ui_prep_templates`, `ui_new_game` |
| `cmp_button_hints` | **Input hint bar** — Keyboard/mouse and gamepad glyph variants, context-sensitive action names; mark proposed bindings in spec, not as gameplay prose. | All entries, as applicable to their visible shell |
| `cmp_tooltip` | **Tooltip and expanded help** — Short source/effect explanation; passive hover/focus tooltip never changes clock; opened detailed card is overlay. | `ui_info_help`, `ui_top_bar`, `ui_hunger`, `ui_hunt_targets`, `ui_progression`, `ui_backpack`, `ui_processing`, `ui_recipe_detail`, `ui_enhancement`, `ui_reworking`, `ui_commerce`, `ui_information`, `ui_battle_hud` |
| `cmp_confirm` | **Confirmation card** — Exact cost/delta/permanence/refund/next requirement plus labelled commit and Cancel. No generic OK for irreversible actions. | `ui_confirm`, `ui_new_game`, `ui_progression`, `ui_bond_perk_choice`, `ui_meals`, `ui_payroll`, `ui_recruitment`, `ui_rank`, `ui_debt_rescue`, `ui_hq_building_map`, `ui_chapter_transition`, `ui_frontier_transfer`, `ui_save`, `ui_load`, `ui_commander_rank_actions` |
| `cmp_refusal` | **Requirement/refusal strip** — Exact authoritative blocker, quantity or time and next action; no generic grey button with no reason. | All entries, as applicable to their visible shell |
| `cmp_loading` | **Loading/busy/error state** — Snapshot/content/receipt pending indicator, no fake zero values; preserve draft. Recover via ui_error_notice, save-specific recovery or boot report. | All entries, as applicable to their visible shell |
| `cmp_toast` | **Notification toast** — Source event/time, severity icon+text, click target; dedup event ID. Retention G03. | `ui_alerts`, `ui_objectives`, `ui_request_notice`, `ui_discovery_notice`, `ui_reward_receipt` |
| `cmp_objective_row` | **Objective / project progress strip** — Authored objective or player pin progress and next action; never auto-replace pins. | `ui_objectives`, `ui_projects`, `ui_day_summary`, `ui_morning`, `ui_world_hud` |
| `cmp_top_stat` | **Guild-stat top-bar cell** — Day/time/purse/Rep/Morale/Rank; orange from19:00, with text/time still legible. | `ui_top_bar`, `ui_world_hud`, `ui_field_view`, `ui_night` |
| `cmp_speed_button` | **Speed selection button** — Pause/1×/2×/4×, selected/effective pause state and input hint. | `ui_speed_controls`, `ui_world_hud`, `ui_field_view`, `ui_battle_hud` |
| `cmp_pace_chip` | **Battle-pace chip** — On/off/inactive/active, ¼ selected speed in watched fight; never MP-like bar. | `ui_battle_pace`, `ui_field_view`, `ui_battle_hud`, `ui_settings` |
| `cmp_minimap_frame` | **Minimap frame and local markers** — Upper-right map field; marker taxonomy/zoom undecided; hide in dialogue. | `ui_minimap`, `ui_world_hud`, `ui_night` |
| `cmp_world_prompt` | **World interaction label / speech bubble** — Interactable identity/action hint and separate proximity bark bubble; no control lock for bark. | `ui_interact_prompt`, `ui_barks`, `ui_world_hud` |
| `cmp_emotes` | **Shared emote icon set** — Exactly exclaim/question/dots/sweat/anger/laugh/heart/music/sleep/idea/sigh; no image generation in this task. | `ui_scene_staging` |
| `cmp_letterbox` | **Letterbox/fade layer** — Authored key-beat bars and fades; layer50 over dialogue40; no automatic rule/time changes. | `ui_scene_staging`, `ui_dialogue`, `ui_sleep`, `ui_transfer_checkpoint` |
| `cmp_stamina` | **Four-bar stamina and fatigue preview** — Four discrete bars, before→after debit, Red Fatigue marker, sleep/rest result; injury separate. | `ui_roster`, `ui_adventurer_profile`, `ui_preparation`, `ui_rest_orders`, `ui_day_summary`, `ui_morning`, `ui_recruitment` |
| `cmp_condition` | **Primary state / injury / timer badge** — Single primary state, independent fatigue/injury expiry/rest flags where allowed; no Dead state. | `ui_roster`, `ui_adventurer_profile`, `ui_staff_profile`, `ui_recruitment`, `ui_preparation`, `ui_ongoing`, `ui_rest_orders`, `ui_day_summary` |
| `cmp_quality` | **Quality and tier badges** — Pristine/Standard/Damaged/Unsellable material grades distinct from Ordinary/Elite Rare/Variant/Boss monster tiers; icon+text beyond colour. | `ui_storage`, `ui_processing`, `ui_reworking`, `ui_commerce`, `ui_walk_up_sale`, `ui_request_board`, `ui_recipe_detail`, `ui_hunt_targets`, `ui_battle_hud` |
| `cmp_inventory_counts` | **Inventory availability / reservation row** — Owned/listed/reserved/available counts and exact claim owner; quantities/grade/origin displayed where relevant. | `ui_storage`, `ui_request_board`, `ui_commerce`, `ui_walk_up_sale`, `ui_processing`, `ui_workshop`, `ui_recipe_detail`, `ui_enhancement`, `ui_reworking`, `ui_backpack` |
| `cmp_item_icon` | **Item/corpse/recipe icon and source link** — Stable content ID binding; raw corpse reference versus per-unit processed value clearly labelled; source links carry navigation context. | `ui_hunt_targets`, `ui_storage`, `ui_recipe_detail`, `ui_request_board`, `ui_processing`, `ui_workshop`, `ui_commerce`, `ui_walk_up_sale`, `ui_consumable_counter`, `ui_projects` |
| `cmp_number_stepper` | **Quantity / price stepper** — Constrained to authoritative allowed quantities; total, unit price and affordability separate. No invented controller step increment. | `ui_commerce`, `ui_walk_up_sale`, `ui_consumable_counter`, `ui_request_board`, `ui_reworking`, `ui_debt_rescue` |
| `cmp_money_quote` | **Money quote, reserve and debt rows** — Gross/fee/net/debt sweep, current→remaining purse, advisory reserve warning, next payroll liability; use sim arithmetic. | `ui_commerce`, `ui_walk_up_sale`, `ui_recruitment`, `ui_staff_profile`, `ui_payroll`, `ui_rank`, `ui_debt_rescue`, `ui_hq_building_map`, `ui_frontier_transfer`, `ui_meals`, `ui_recipe_detail` |
| `cmp_reward_table` | **Reward / expense / consequence table** — Actual item/Gold/Rep/XP or result effects per row, preview distinguished from committed receipt, event ID dedup. | `ui_reward_receipt`, `ui_resolution`, `ui_day_summary`, `ui_contracts`, `ui_flashpoint`, `ui_request_board`, `ui_transfer_checkpoint`, `ui_expedition_planning_result`, `ui_counter_offer_result`, `ui_cross_check_result`, `ui_cutting_chart_result`, `ui_fitting_result` |
| `cmp_progress_track` | **Progress/XP/bond track** — Source-specific label (Commander rank, adventurer track level, modifier rank, staff rank, Guild Rank never conflated), thresholds/cap/selected slots. | `ui_commander_profile`, `ui_progression`, `ui_staff_profile`, `ui_bonds`, `ui_officer_profile`, `ui_romance`, `ui_expedition_planning_result`, `ui_counter_offer_result`, `ui_cross_check_result`, `ui_cutting_chart_result`, `ui_fitting_result`, `ui_commander_rank_actions` |
| `cmp_perk_pair` | **Permanent perk comparison cards** — Both perk benefits/costs shown from start with Bond5 lock, later permanent choice and selected receipt. | `ui_officer_profile`, `ui_bond_perk_choice` |
| `cmp_party_slots` | **Formation slot cards** — Three front/three back, max5/one front; reach/passive, swap/remove and melee warning; scout exactly1 in its variant. | `ui_preparation`, `ui_prep_templates` |
| `cmp_grid` | **Grid and draggable footprint pieces** — 90-degree orientation, valid/invalid placement ghosts, original retained on failure; distinct pack and jig data. | `ui_backpack`, `ui_preparation`, `ui_fitting_play` |
| `cmp_template_slot` | **Named loadout-template slots** — Exactly two; saved names, missing person/item/fatigue diff, no substitution. | `ui_prep_templates`, `ui_preparation` |
| `cmp_risk_card` | **Prep risk and time forecast** — Actual shortened return, cutoff, scout cumulative injury formula and hunt advice/main causes; estimate not guarantee. | `ui_preparation`, `ui_area_detail`, `ui_hunt_targets` |
| `cmp_map` | **Parchment map and fog layers** — Known areas/discoveries, selected region/route and associated detail card; no fabricated Frontier map names. | `ui_region_map`, `ui_area_detail`, `ui_scout_field`, `ui_discovery_notice`, `ui_expedition_planning_play`, `ui_hq_building_map` |
| `cmp_discovery_counter` | **Discovery counters and benefit rows** — Species/landmarks/paths counts, milestones, exact path/den effects, rare reservation and source links. | `ui_area_detail`, `ui_scout_field`, `ui_discovery_notice` |
| `cmp_operation_row` | **Live operation / history row** — Party/phase/start/finish/progress/yields, live Watch vs history result, immediate Recall. | `ui_ongoing`, `ui_resolution`, `ui_field_view` |
| `cmp_queue` | **Ordered work-order list and worker station card** — Waiting/active distinction, job type, exact assigned worker/rank, finish/cutoff, reorder/remove, no manual idle-worker mechanic. | `ui_processing`, `ui_workshop` |
| `cmp_recipe_quote` | **Recipe/enhancement/Reworking comparison** — Inputs, quality, output, footprint/stat or permanent target delta, time and locks; job-start reservation distinction. | `ui_recipe_detail`, `ui_enhancement`, `ui_reworking`, `ui_workshop` |
| `cmp_forecast` | **Forecast card and actual-demand comparison** — Dated category/confidence/horizon, delivered prediction vs later actual, unverified rumour marker; no reroll UI. | `ui_information`, `ui_commerce`, `ui_morning` |
| `cmp_request_card` | **Request/client/contract card** — Lifecycle, absolute deadline/remaining, goods/encounter/reward/benefit, alternatives and courier state. | `ui_request_board`, `ui_contracts`, `ui_flashpoint`, `ui_request_notice`, `ui_session_offer`, `ui_commander_rank_actions` |
| `cmp_deadline` | **Deadline / calendar-event row** — Absolute and remaining time, no-deadline label, paused-on-transfer vs still-expiring categories. | `ui_request_board`, `ui_contracts`, `ui_session_offer`, `ui_payroll`, `ui_debt_rescue`, `ui_frontier_transfer`, `ui_transfer_checkpoint` |
| `cmp_construction` | **Room capacity tile and construction quote** — Current versus added beds/stations/shelves, named waiting recruits, gate, inputs, calendar duration/completion. | `ui_hq_building_map`, `ui_recruitment`, `ui_frontier_transfer` |
| `cmp_save_slot` | **Profile/save-slot and recovery card** — Three profiles; named manual/rotating autosave distinctions, time/version/integrity/backup; no deletion assumed. | `ui_profile_select`, `ui_save`, `ui_load`, `ui_boot_report` |
| `cmp_settings_row` | **Setting toggle/selector/slider row** — Current/draft/pending value and help; mode effect date separate from visual preference. | `ui_settings`, `ui_difficulty`, `ui_battle_pace`, `ui_speed_controls` |
| `cmp_battle_hp` | **HP number/bar and status strip** — Enemy top-centre, party bottom; statuses above names, FRONT/BACK every member; no enclosing party box. | `ui_battle_hud`, `ui_adventurer_profile`, `ui_preparation`, `ui_roster` |
| `cmp_readiness_ring` | **Gold clockwise attack readiness ring** — Attack timing, separate from orange skill meter; no turn-order strip. | `ui_battle_hud` |
| `cmp_skill_meter` | **Orange skill meter / SKILL glow** — 0–100 meter per sim, role-driven; never blue MP styling. | `ui_battle_hud` |
| `cmp_battle_log` | **Combat/field event log** — Committed event order, damage/status/secured rewards/finds; stable on re-open. | `ui_battle_hud`, `ui_field_view`, `ui_scout_field` |
| `cmp_damage_label` | **Damage/status world labels** — Body-height numeric pop, offset multi-hit visuals; no extra mechanical hit/meter event. | `ui_battle_labels` |
| `cmp_skill_banner` | **Skill-name banner** — Horizontal readable authored name; presentation duration follows action and reduced-VFX settings. | `ui_battle_labels` |
| `cmp_result_band` | **Grade/result banner and progress rows** — D/C/B/A/S sourced grade, hint cap, precise skill/bond/output receipt; Fitting no D. | `ui_expedition_planning_result`, `ui_counter_offer_result`, `ui_cross_check_result`, `ui_cutting_chart_result`, `ui_fitting_result`, `ui_day_summary`, `ui_reward_receipt` |
| `cmp_session_header` | **Session context, hour cost and hint widget** — Officer, skill, used today/context job/order; one free hint with A-cap disclosure. | `ui_session_offer`, `ui_expedition_planning_play`, `ui_counter_offer_play`, `ui_cross_check_play`, `ui_cutting_chart_play`, `ui_fitting_play` |
| `cmp_route_puzzle` | **Planning route/terrain/rest overlays** — Sourced grid, impassability, route path, threat radius, time/stamina budgets and rest placement. | `ui_expedition_planning_play` |
| `cmp_negotiation` | **Buyer tell, price and tactic controls** — Portrait/tell/round/patience, market value and offer; hide ceiling/acceptance; approved persona behavior only. | `ui_counter_offer_play`, `ui_session_offer` |
| `cmp_document_puzzle` | **Document fact/link/candle pieces** — Selectable fact anchors, discrepancy connectors, trust-source choice, soft candle timer; no fabricated facts. | `ui_cross_check_play` |
| `cmp_cut_puzzle` | **Carcass guide and stroke feedback** — Species diagram, cut guides/no-cut zones, accuracy and steady-speed feedback from approved prototype. | `ui_cutting_chart_play` |
| `cmp_fitting_puzzle` | **Jig pegs/notches/part tray** — Key-part-first marking, rotation, move/time/par readouts and assistance route. | `ui_fitting_play` |
| `cmp_transfer_ledger` | **Transfer and arrival ledger** — Carryover checklist, cleanup/refunds, protected deadlines, payroll checkpoints, chronological changes. | `ui_frontier_transfer`, `ui_transfer_checkpoint` |
| `cmp_sleep_readiness` | **Night recovery preview** — Current/07:00 readiness, timers and once-only sleep credit, closed operations label. | `ui_sleep`, `ui_night`, `ui_morning`, `ui_day_summary` |

Asset variants required across this kit: idle/hover/focus/selected/pressed; locked with explanation; read/unread; pending/error/success; source-defined status and grade badges. The same focus treatment works with mouse and controller. No new pixel sizes, padding, timing, pagination limits or icon counts beyond the source emote set are asserted. Cards must fit long labels and lining figures under the eventual UI-scale range (G21). Screens preserve reading order: identity → relevant state → consequence/price → labelled action → input hint.

## D. Build order

FGC_09 defines **M1/S0–S3 as headless**, with no player screens: S0 content/bus; S1 clock/operations/combat; S2 economy/requests/payroll; S3 saves/story/Commander/bonds/transfer/difficulty. Those are dependencies, not invented UI deliveries. Build the views against those real read models. FGC_09 S5 explicitly owns acceptance states; S6 integrates watched field presentation; S7 completes New Game through Chapter 1 including night; S8 implements the five sessions; S9 validates/balances the existing slice.

In the per-screen table below, **proposed** means this inventory places an otherwise unassigned screen at the earliest useful integration point; it does not claim FGC_09 named that screen. “Later” has no sprint/date allocation. A test fixture for later headless rules does not promise release-ready Chapter 2/Frontier content in M3.

### M2 / S4 — world interaction minimum (proposed)

The source sprint requires walking, collisions, camera, cutaway and time of day. A small context prompt is proposed for reachable interactions; complete HUD is S5.

### M2 / S5 — dialogue, theme and management

First deliver all explicitly named core screens on the real simulation, with their empty/loading/blocked/error acceptance states. Reuse the shell/face frames/panels/quotes before detailed painted treatment. Source IDs and approved placeholders may unblock work; never invent canonical content. Proposed companion screens fill links required by those core flows.

### M2 / S6 — field and battle

Add live search/scout/battle renderers and HUD, not a second combat simulation. Validate dispatch → Watch → search/fight → Leave/reopen → Recall/cutoff → Resolution with selected Pause preserved and watched/unwatched outcomes equal.

### M3 / S7 — New Game through Chapter 1

Integrate profiles, saves, naming cues, authored scenes, meals/personal status, night/sleep/morning and chapter conclusion. Name cues already work in S5 scenes; this sprint connects their complete campaign path. Include proposed helper profiles/journal where their links are exposed.

### M3 / S8 — five working sessions and bonds

Each play/result pair uses one session identity and one authoritative result application. Prototypes supply only the currently missing approved tuning; output values already in GDD remain unchanged unless the owner retunes the GDD. S8's generic D–S exit statement must preserve Fitting's no-D exception (G25). Friendship scene content is supplied by the owner.

### Later — no allocated FGC_09 sprint

Keep interface compatibility and source-defined previews for Bond5, romance, rank-3 active skills and Frontier transfer. Chapter2 flashpoints may use an S5 proposed briefing shell, but their final scenes/encounters are later than the Chapter1 slice. Frontier maps, cast, gift values, recipes and scenes remain authored content, never generated placeholders promoted to canon.

### First-needed screen ledger

All entries appear exactly once. “Minimum” includes the global nonmutating preview, explicit commit, authoritative refusal and prescribed portrait/input behavior.

| First need | Inventory entry | Minimum version at that point |
|---|---|---|
| S4 (proposed) | `ui_interact_prompt` | Nearby actor/service/bed/desk name and interact input. |
| S5 | `ui_name_entry` | Cue-driven name draft/commit and exact scene resume. |
| S5 | `ui_guild_name_entry` | Cue-driven Guild-name draft/commit and exact scene resume. |
| S5 | `ui_world_hud` | Wire top bar, objective, alerts, minimap and prompt to current world. |
| S5 | `ui_top_bar` | Live six Guild stats, 19:00 orange state, no false currency data. |
| S5 | `ui_objectives` | Authored objective and event/project links with retained return context. |
| S5 | `ui_alerts` | Severity/source/time notices, event-ID dedup, relevant-object link. |
| S5 | `ui_minimap` | Location map/Commander position, hidden while dialogue open; markers await design. |
| S5 | `ui_speed_controls` | Pause/1/2/4 chosen/effective states with modal-safe input. |
| S5 | `ui_battle_pace` | Setting/chip shell in S5; actual watched-fight activation in S6. |
| S5 | `ui_dialogue` | Waist-length speaker slots, expressions, thoughts, advance and scene checkpoints. |
| S5 | `ui_talk_menu` | Authored topics, heard flags, hidden after-topics and automatic Leave. |
| S5 | `ui_barks` | Once/day proximity speech bubble without pause/control lock. |
| S5 | `ui_ambient` | Time-band NPC and name-only line with request-state variant. |
| S5 | `ui_choices` | Nested authored choices and exactly-once tag effects. |
| S5 | `ui_narration` | Separate no-speaker narration box with advance. |
| S5 | `ui_scene_staging` | Authored cue layer, emotes, letterbox and fade handoffs. |
| S5 | `ui_adventurer_office` | Event/readiness/payroll shell and all core adventure routes. |
| S5 | `ui_roster` | Real names/passives/reach/HP/stamina/state/fatigue and inspect/rest/hire routes. |
| S5 | `ui_rest_orders` | Assign/cancel with dispatch-history and injury-aware recovery preview. |
| S5 | `ui_recruitment` | Authored candidates/former staff, exact eligibility and hire/rehire quote. |
| S5 | `ui_hunt_targets` | Known target stats/groups/tier/yields and rare-reservation availability. |
| S5 | `ui_preparation` | Party/rows/equipment/duration/risk/fatigue/cutoff preview and atomic dispatch. |
| S5 | `ui_ongoing` | Live list/history, immediate Recall; watch route becomes live in S6. |
| S5 | `ui_request_board` | All visible lifecycle states, quantities/deadlines/alternatives/courier and atomic delivery. |
| S5 | `ui_request_notice` | Once-only offer notice from cue/tag without auto-accept. |
| S5 | `ui_processing` | Real auto-assigned work order, identity-preserving cancel, yields/finish; G10 visibility unresolved. |
| S5 | `ui_workshop` | Mixed order with waiting intents vs active reservations and real refunds. |
| S5 | `ui_recipe_detail` | Pre-unlock recipe previews, exact ingredients/source/footprint/result and queue route. |
| S5 | `ui_enhancement` | Person/sequential-level quote, mutually exclusive state, full refund. |
| S5 | `ui_reworking` | Mend/Refine-grade/salvage previews and perk-aware mixed-order jobs. |
| S5 | `ui_commerce` | Listings/slots/stock/price/fee/net/debt quote and hourly shared-buyer explanation. |
| S5 | `ui_walk_up_sale` | Immediate exact-stock sale with origin-sensitive resale and no schedule dependency. |
| S5 | `ui_payroll` | Projected/due balances, full employee allocations and confirmed departures. |
| S5 | `ui_resolution` | Every operation result/secured reward/interrupt and persistent-job state. |
| S5 | `ui_day_summary` | Actual ledger, readiness, payroll/rescue/debt, pins and night handoff. |
| S5 | `ui_confirm` | Caller-specific consequence/price/permanence and labelled atomic commit. |
| S5 | `ui_error_notice` | Stable refusal reasons, retained drafts and safe refreshed retry. |
| S5 (proposed) | `ui_boot_report` | Content validation report with stop/recovery route before campaign starts. |
| S5 (proposed) | `ui_hub` | Same department screens from contextual shortcut; no physical teleport. |
| S5 (proposed) | `ui_dialogue_history` | Optional proposal only: transcript frame; do not implement unspecified persistence/timing as canon. |
| S5 (proposed) | `ui_auto_advance` | Optional proposal only: control and unresolved behavior; not a mandatory S5 feature. |
| S5 (proposed) | `ui_officer_profile` | Identity/bond/scene hint and both Bond5 trade-offs visible from start. |
| S5 (proposed) | `ui_adventurer_profile` | Read-only combat/build/equipment/employment summary plus gated action routes. |
| S5 (proposed) | `ui_progression` | Complete four-track build preview and atomic Buy/Rebuild/Cancel. |
| S5 (proposed) | `ui_backpack` | Valid grid editing, active categories, stock claims and unchanged inventory on cancel. |
| S5 (proposed) | `ui_staff_roster` | Named staff/stations/jobs/ranks and officer fallback. |
| S5 (proposed) | `ui_staff_profile` | Productive hours, promotion prerequisites/result and future payroll exposure. |
| S5 (proposed) | `ui_region_map` | Known regions/rank locks and navigation to Area Detail. |
| S5 (proposed) | `ui_area_detail` | Fog/counts/milestones/benefits/odds/source links and Hunt/Scout/Contracts. |
| S5 (proposed) | `ui_prep_templates` | Two saved drafts, missing-person/item/fatigue report and no substitutions. |
| S5 (proposed) | `ui_contracts` | Offer/accept/prepare/history shell with fixed encounters and existing deadlines; final scenes later. |
| S5 (proposed) | `ui_flashpoint` | Exact gate/reward/formation/retry preview shell; final Chapter2 content later. |
| S5 (proposed) | `ui_reward_receipt` | Display already committed outcome once; acknowledgement pays nothing again. |
| S5 (proposed) | `ui_information` | Saved dated forecast/confidence/actuals and unverified source links. |
| S5 (proposed) | `ui_consumable_counter` | Sourced prices, clinic allowance and purchase to storage. |
| S5 (proposed) | `ui_storage` | Stock identities/quality/claims and correct action/source routes. |
| S5 (proposed) | `ui_hq_building_map` | Actual rooms/capacity and six sourced upgrade quotes, one build at a time. |
| S5 (proposed) | `ui_rank` | Exact standing/fee/gates/unlocks and gold-only promotion. |
| S5 (proposed) | `ui_debt_rescue` | Correct loan trigger/repayment/overdue sweep/direct rescue preview. |
| S5 (proposed) | `ui_projects` | Up to three explicit pins, progress/shortfall/source/next action. |
| S5 (proposed) | `ui_settings` | Source-defined presentation preferences and difficulty link; ranges remain unassigned. |
| S5 (proposed) | `ui_info_help` | Authored/sourced explanation and tutorial acknowledgements without accidental unlock. |
| S6 | `ui_field_view` | Live search/battle shell, Leave/Recall and speed controls. |
| S6 | `ui_scout_field` | Live walking scout, progress/map/find log, no battle-pace slowdown. |
| S6 | `ui_battle_hud` | Enemy HP and party HP/readiness/skill/status/row identity. |
| S6 | `ui_battle_labels` | Body-height damage, status labels, rare/variant notice and skill banner. |
| S6 | `ui_discovery_notice` | Real find/milestone parchment with source/effect and no duplicate reward. |
| S7 | `ui_title` | Continue/New Game/Load/Settings routes with valid-save availability. |
| S7 | `ui_profile_select` | Three profiles and safe empty/occupied selection. |
| S7 | `ui_new_game` | Chosen profile → explicit Start → opening authored scene. |
| S7 | `ui_night` | Closed-operation world with available talks/meals/reports and bed route. |
| S7 | `ui_sleep` | Manual after20:00 / automatic01:00, remaining-night accounting once. |
| S7 | `ui_morning` | Proposed actual-event/readiness briefing; continue to07:00 paused. |
| S7 | `ui_chapter_transition` | Officer gates and unaccepted-request warning before elective chapter end. |
| S7 (proposed) | `ui_commander_profile` | Four skills/ranks/points/caps/effects and personal status. |
| S7 (proposed) | `ui_hunger` | Fed/Hungry and run eligibility, no added penalty. |
| S7 (proposed) | `ui_meals` | Sourced venue prices, Fed result and daily shared-talk accounting. |
| S7 (proposed) | `ui_personal_activities` | Routes to meals/talks/reports/night; later features visibly excluded. |
| S7 (proposed) | `ui_important_npc_profile` | Known identity/contact record, full-left portrait or name-only. |
| S7 (proposed) | `ui_reports_journal` | Existing records/trends/contact history; no points or inactive-base simulation. |
| S7 (proposed) | `ui_city_bell` | Audio-only outdoor clock cue; visual caption remains optional undecided. |
| S7 (proposed) | `ui_save` | Named manual slots, autosave visibility, safe-checkpoint/atomic-backup status. |
| S7 (proposed) | `ui_load` | Valid slot/backup selection, progress-replacement confirmation and paused resume. |
| S7 (proposed) | `ui_difficulty` | Standard/Relaxed comparison and pending next07:00 effect. |
| S8 | `ui_bonds` | Point/level/weekly gates and authored friendship triggers. |
| S8 | `ui_session_offer` | Officer/day/context validation, hour cost/hint rule and real daily buyer order. |
| S8 | `ui_expedition_planning_play` | Playable authored puzzle, one hint, deterministic grade and exactly-once session_result; missing tuning from S8 prototype. |
| S8 | `ui_expedition_planning_result` | Real grade/skill/bond/output/time receipt, Continue without another payout; Fitting preserves no-D exception. |
| S8 | `ui_counter_offer_play` | Playable authored puzzle, one hint, deterministic grade and exactly-once session_result; missing tuning from S8 prototype. |
| S8 | `ui_counter_offer_result` | Real grade/skill/bond/output/time receipt, Continue without another payout; Fitting preserves no-D exception. |
| S8 | `ui_cross_check_play` | Playable authored puzzle, one hint, deterministic grade and exactly-once session_result; missing tuning from S8 prototype. |
| S8 | `ui_cross_check_result` | Real grade/skill/bond/output/time receipt, Continue without another payout; Fitting preserves no-D exception. |
| S8 | `ui_cutting_chart_play` | Playable authored puzzle, one hint, deterministic grade and exactly-once session_result; missing tuning from S8 prototype. |
| S8 | `ui_cutting_chart_result` | Real grade/skill/bond/output/time receipt, Continue without another payout; Fitting preserves no-D exception. |
| S8 | `ui_fitting_play` | Playable authored puzzle, one hint, deterministic grade and exactly-once session_result; missing tuning from S8 prototype. |
| S8 | `ui_fitting_result` | Real grade/skill/bond/output/time receipt, Continue without another payout; Fitting preserves no-D exception. |
| Later | `ui_bond_perk_choice` | Permanent comparison/confirmation once exact eligibility is satisfied. |
| Later | `ui_romance` | Authored Frontier cast, story choices/gifts/dates and single-partner state; no stat perks. |
| Later | `ui_frontier_transfer` | Quote, carryover, cleanup/deadline/payroll disclosures and predeparture validation. |
| Later | `ui_transfer_checkpoint` | Calendar ledger/payroll stops/save support and paused arrival. |
| Later | `ui_commander_rank_actions` | Rank3 daily encouragement/weekly Standing-offer interface; no invented G26 order details. |

### S9 verification and handoff

FGC_09 S9 adds no newly named screen. It verifies the integrated Chapter1 slice and revises source tuning only through the GDD. UI acceptance should include actual clock restoration; cutoff and payroll order; save/reload without duplicate receipts; mouse/controller reachability; names/long text/UI scale; missing/blocked states; correct portrait sources; source links returning to their caller; no unapproved Frontier content. This document performs a documentation audit, not a Godot runtime test.

### Gap register

These are the **26 distinct gaps** counted in the report. Repeated per-screen citations refer to these same questions. They do not block documenting settled behavior; implementation/content decisions belong in the owning source. Highest-impact implementation dependencies: **G09** (session time/abort settlement), **G10** (pre-start quality visibility), **G08** (prototype tuning).

| ID | Undefined or conflicting contract |
|---|---|
| G01 | Name-entry validation is undefined: defaults, length, accepted characters, localisation, renaming, and whether Back can leave a required cue. |
| G02 | Menu/hub availability away from HQ, direct shortcuts, and controller focus/tab/scroll bindings are not specified by §13. Proposed navigation must not imply teleporting or bypass service gates. |
| G03 | HUD objective selection, notification retention/dismissal, minimap markers/zoom and missing-data fallback copy need acceptance design; no limits or ranges are supplied. |
| G04 | The sources specify dialogue advance, not backlog or auto-advance rules. History scope/persistence, auto timing, stop conditions and bindings need a decision. |
| G05 | Starting New Game flow beyond profile/scene handoff is undefined: title art, default save selection, profile replacement/deletion policy and initial difficulty placement. |
| G06 | Commander personal-activity details are incomplete: HQ kitchen opening predicate, meal duration, shared-meal selection and gift-shop catalogue/prices. Do not invent time costs or stock. |
| G07 | Romance cast, gift likes/dislikes and point values, dates, endings and authored scenes are later Frontier content; no sprint beyond S9 is assigned. |
| G08 | Minigame tuning remains assigned to M3 prototypes: negotiation acceptance/tactics/tells, Cutting Chart weights/speed band, Fitting par, and grade edge cases. No provisional numbers become rules. |
| G09 | Session exit/abort/retry and starting late enough to cross 20:00 need a contract, including output eligibility if the one-hour advance completes/cancels the associated job. Failed Planning/Cross-check output details are incomplete. |
| G10 | Processing quality visibility conflicts: §12.1/§15 ask for odds while §5a.2 reserves seeing pre-start odds to Trained eye at rank 3. Exact public fields before rank 3 need reconciliation within the GDD. **Resolved 2026-09-28:** odds always shown; Trained eye is now a passive (GDD 5a.2). |
| G11 | FGC_07 §04 lists field exit as world, while GDD §15 requires the previous navigation context. Inventory follows GDD and proposes suspending/restoring the caller; implementation state routing must reconcile this. |
| G12 | Specific schedule is not assigned for several §15 screens, Bond 5, Chapter 2/Frontier content and romance. S5/S7 associations below are explicit integration proposals, not new FGC_09 promises. |
| G13 | Portraits/content still need production: final friendship, officer introduction, request/contract aftermath, chapter transition and Frontier scenes. Missing art must not become a '?' portrait or invented biography. |
| G14 | Backpack and puzzle controller cursor, rotate, undo, reorder and slider controls are absent from §13. Bindings below are proposals requiring controller testing. |
| G15 | Formation-template naming/overwrite UX is undefined beyond two named templates and missing-member/item/fatigue feedback. No automatic substitutions. |
| G16 | The morning screen is named in FGC_07 §04 but its precise contents and acknowledgement flow are not authored; proposed contents are existing morning events only. |
| G17 | City bell has no specified visual UI or caption option. Keep it audio-only unless an accessibility indicator is approved; no mandatory popup. |
| G18 | Screen-level loading/error/recovery text and focus restoration are not authored. The shared lifecycle treatment is a UI proposal using existing command errors, not new simulation rules. |
| G19 | Dialogue scene clock/control handoff needs explicit scene-authoring confirmation for non-dialogue cinematics; overlay dialogue pauses, but §04 does not define every scene's time policy. |
| G20 | Transfer checkpoint presentation and cancellation after departure are not defined; only pre-confirmation Cancel is promised. Arrival content and later region labels must be authored. |
| G21 | Font/UI-scale ranges, reduced-VFX controls/defaults and audio setting ranges are not specified. Do not manufacture resolution, size or timing limits. |
| G22 | Chapter conclusion and permanent Bond 5 choice need final authored warning/confirmation copy; no additional unlock threshold is implied. |
| G23 | Boot validation failure/report and save corruption UI need player-facing diagnostics and recovery copy; integrity mechanics exist, diagnostic wording does not. |
| G24 | Journal/report filters and layout, important-NPC biography fields and visibility rules are unspecified. Show only already authored or recorded information. |
| G25 | FGC_09 S8 exit wording says each session D–S, but GDD Fitting has no D and completes with C assistance. GDD wins; sprint acceptance must preserve that exception. |
| G26 | Rank-3 Standing offer specifies once/week, a held material and +20%, but not quantity selection, baseline price calculation detail, acceptance/deadline or buyer-generation contract. Keep undefined order fields unfilled until authored. |

Frontier content gaps are kept separate from UI proposals: existing numbers, bonds, reservation timing, Reworking Morale exclusion, perk arithmetic and fixed rolls are settled in the current GDD. No invented rule or numeric fallback is supplied for an unresolved field.

