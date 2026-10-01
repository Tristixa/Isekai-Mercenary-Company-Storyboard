# Byte-level preservation report

Source: `db5a41c61b8850f783d0a7321444321f4ee5fa0ede3d5236a83fbb188e334444`
Candidate: `5bfc52f9e40090aaad31aa7766e123eddc41d6f53aa1cea843681df55f601a9d`

498,803 / 499,647 source JSON bytes retained verbatim, in 116 checked spans. 844 source bytes replaced; 51,235 bytes inserted/replaced. 115 surgical edits; no global JSON reserialization.

Every semantic difference is checked against the six-item allowlist. All original routes, junctions, districts, coordinates, building footprints/yaws/heights, terrain, phase-1 polygon, clock tower geometry, HQ reservation and existing markers/portals are unchanged. The added roof_kit field is the only edit on buildings outside the four market businesses. HQ access is attached to new future portals, leaving reservation bytes intact. The v4 build-plan document is retained as an exact byte suffix.

## Every changed ID

**buildings**
- `south_gate`
- `guard_shelter`
- `lodging`
- `stables`
- `arrival_home_1`
- `arrival_home_2`
- `arrival_home_3`
- `company_house`
- `store_shed`
- `company_neighbor`
- `tavern`
- `provisions`
- `repair_supply`
- `market_home_0`
- `market_home_1`
- `market_home_east`
- `market_home_violet`
- `tool_repair`
- `timber_containers`
- `material_sorting`
- `bulk_storehouse`
- `loading_shelter`
- `quay_storehouse`
- `food_shop`
- `clinic`
- `service_home_0`
- `service_home_1`
- `service_home_2`
- `service_home_3`
- `old_hall`
- `watch_tower`
- `old_home_0`
- `old_home_1`
- `old_home_2`
- `toll_records`
- `civic_guard`
- `notice_shelter`
- `res_home_0`
- `res_home_1`
- `res_home_2`
- `res_home_3`
- `waterkeeper`
- `washing`
- `cistern`
- `street_home_0`
- `street_home_1`
- `street_home_2`
- `street_home_3`
- `street_home_4`
- `street_home_5`
- `street_home_6`
- `street_home_7`
- `street_home_8`
- `infill_home_01`
- `infill_home_02`
- `infill_home_03`
- `infill_home_04`
- `infill_home_05`
- `infill_home_06`
- `infill_home_07`
- `infill_home_08`
- `infill_home_09`
- `infill_home_10`
- `infill_home_11`
- `infill_home_12`
- `infill_home_13`
- `infill_home_14`
- `infill_home_15`
- `infill_home_16`
- `infill_home_17`
- `infill_home_18`
- `infill_home_19`
- `infill_home_20`
- `infill_home_21`
- `infill_home_22`
- `infill_home_23`
- `infill_home_24`
- `infill_home_25`
- `infill_home_26`
- `infill_home_27`
- `infill_home_28`
- `infill_home_29`
- `infill_home_30`

**interiors**
- `guild_interior`

**rooms_and_links**
- `guild_interior/two_bed_dormitory`
- `guild_interior/dorm_stair`

## Every added ID

**ground_zones**
- `spine_service_allotments`

**markers**
- `civic_terrace/leaders_1`
- `civic_terrace/leaders_2`
- `civic_terrace/leaders_3`
- `civic_terrace/leaders_4`
- `civic_terrace/leaders_5`
- `civic_terrace/commander`
- `civic_terrace/officers_1`
- `civic_terrace/officers_2`
- `civic_terrace/officers_3`
- `civic_terrace/officers_4`
- `civic_terrace/officers_5`
- `civic_terrace/envoy`
- `civic_terrace/camera_hint`
- `south_gate/envoy_arrival`
- `guild_courtyard/envoy`
- `guild_interior/adventurer_evening_1`
- `guild_interior/adventurer_evening_2`
- `guild_courtyard/adventurer_evening_1`
- `guild_courtyard/adventurer_evening_2`
- `tavern_interior/adventurer_evening_1`
- `tavern_interior/adventurer_evening_2`
- `guild_courtyard/rest_1`
- `guild_courtyard/rest_2`

**npc_spots**
- `guild_interior/adventurer_evening_1`
- `guild_interior/adventurer_evening_2`
- `guild_courtyard/adventurer_evening_1`
- `guild_courtyard/adventurer_evening_2`
- `tavern_interior/adventurer_evening_1`
- `tavern_interior/adventurer_evening_2`

**props**
- `market_court_stall_1`
- `market_court_stall_2`
- `market_edge_stall_1`
- `market_edge_stall_2`
- `allotment_bed_1`
- `allotment_bed_2`
- `allotment_bed_3`
- `allotment_bed_4`
- `allotment_tools`
- `workshop_timber_pile`
- `workshop_stacked_materials`
- `workshop_crates`
- `workshop_work_area`
- `workshop_cart`
- `quays_timber_pile`
- `quays_stacked_materials`
- `quays_crates`
- `quays_work_area`
- `quays_cart`
- `allotment_bed_5`
- `allotment_bed_6`
- `allotment_bed_7`
- `allotment_bed_8`
- `allotment_bed_9`
- `allotment_bed_10`
- `allotment_water_butt`
- `allotment_compost`
- `allotment_fruit_tree_1`
- `allotment_fruit_tree_2`
- `allotment_fence_north`
- `allotment_fence_south`
- `allotment_fence_west`
- `allotment_fence_east_north`
- `allotment_fence_east_south`
- `allotment_gate`
- `quays_crate_stack_wall`
- `quays_barrels_wall`
- `quays_rope_wall`
- `quays_timber_wall`
- `quays_lean_to`
- `quays_cart_2`
- `quays_barrels_south`
- `quays_crates_south`
- `quays_hand_hoist`
- `quays_loading_crates`
- `quays_loading_barrels`
- `quays_loading_rope`
- `quays_cart_3`
- `quays_weigh_scale`
- `quays_north_stock`
- `workshop_timber_wall`
- `workshop_sawhorses`
- `workshop_bench_1`
- `workshop_bench_2`
- `workshop_bench_3`
- `workshop_drying_rack`
- `workshop_stone_stack`
- `workshop_scrap_1`
- `workshop_scrap_2`
- `workshop_tool_shed`
- `workshop_south_timber`
- `workshop_south_stone`
- `workshop_east_sawhorses`
- `workshop_east_bench`
- `workshop_east_stock`
- `market_court_stall_3`
- `market_court_crates`
- `market_court_baskets`
- `market_court_barrow`
- `market_edge_stall_3`
- `market_edge_crates`
- `market_edge_baskets`
- `market_edge_barrow`
- `market_south_stall_1`
- `market_south_stall_2`
- `market_south_stall_3`
- `market_south_crates`
- `market_south_baskets`
- `market_south_barrow`

**new_facades**
- `market_bakery`
- `market_small_shop_east`
- `market_provisions`
- `market_small_shop_south`

**portals**
- `dorm_annex_portal`
- `larger_dorm_portal`

## Density correction versus initial v5

Every other collection is exactly equal to the archived initial v5. No IDs were removed.

**props: changed**
- `allotment_bed_1`
- `allotment_bed_2`
- `allotment_bed_3`
- `allotment_bed_4`
- `allotment_tools`
- `workshop_timber_pile`
- `workshop_stacked_materials`
- `workshop_crates`
- `workshop_work_area`
- `workshop_cart`
- `quays_timber_pile`
- `quays_stacked_materials`
- `quays_crates`
- `quays_work_area`
- `quays_cart`

**props: added**
- `allotment_bed_5`
- `allotment_bed_6`
- `allotment_bed_7`
- `allotment_bed_8`
- `allotment_bed_9`
- `allotment_bed_10`
- `allotment_water_butt`
- `allotment_compost`
- `allotment_fruit_tree_1`
- `allotment_fruit_tree_2`
- `allotment_fence_north`
- `allotment_fence_south`
- `allotment_fence_west`
- `allotment_fence_east_north`
- `allotment_fence_east_south`
- `allotment_gate`
- `quays_crate_stack_wall`
- `quays_barrels_wall`
- `quays_rope_wall`
- `quays_timber_wall`
- `quays_lean_to`
- `quays_cart_2`
- `quays_barrels_south`
- `quays_crates_south`
- `quays_hand_hoist`
- `quays_loading_crates`
- `quays_loading_barrels`
- `quays_loading_rope`
- `quays_cart_3`
- `quays_weigh_scale`
- `quays_north_stock`
- `workshop_timber_wall`
- `workshop_sawhorses`
- `workshop_bench_1`
- `workshop_bench_2`
- `workshop_bench_3`
- `workshop_drying_rack`
- `workshop_stone_stack`
- `workshop_scrap_1`
- `workshop_scrap_2`
- `workshop_tool_shed`
- `workshop_south_timber`
- `workshop_south_stone`
- `workshop_east_sawhorses`
- `workshop_east_bench`
- `workshop_east_stock`
- `market_court_stall_3`
- `market_court_crates`
- `market_court_baskets`
- `market_court_barrow`
- `market_edge_stall_3`
- `market_edge_crates`
- `market_edge_baskets`
- `market_edge_barrow`
- `market_south_stall_1`
- `market_south_stall_2`
- `market_south_stall_3`
- `market_south_crates`
- `market_south_baskets`
- `market_south_barrow`

**ground_zones: changed**
- `spine_service_allotments`

Exact changed JSON paths and byte-span offsets/hashes: `byte-diff-summary.json` and `byte-edit-manifest.json`.
The baseline directory is a byte copy of the approved v4 delivery; its older illustrations are historical references only.
