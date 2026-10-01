// Plan v7d amendment: the Guild hall (owner-approved redesign, 2026-10-01). Edits v7c in place (git keeps v7c).
const fs = require('fs');
const f = 'D:/Storyboards/Isekai Mercenary Company/Locations/Eurydica/Build Plan/eurydica-plan.json';
const p = JSON.parse(fs.readFileSync(f, 'utf8'));
const hall = p.buildings.find(b => b.id === 'company_house');
const X0 = -38.3, X1 = -25.6, Z0 = 91.0, Z1 = 105.5;
const doorX = (X0 + X1) / 2;
Object.assign(hall, {
  facade_id: 'guild_hall',
  footprint: [X0, Z0, X1, Z1],
  door_face: 's',
  door_position: [doorX, Z1],
  height_m: 7.0,
  roof_height_m: 5.0,
  ground_y_m: 0.6,
  roof_palette: 'slate_blue',
  yaw_deg: 0,
  typology: 'guild_hall',
  display_name: 'Guild hall',
  source_concept: 'Locations/Eurydica/Interiors/Guild House Redesign v2.md; Research/Atmosphere - Kingdoms of Amalur/Interiors/Guild Exterior.jpg',
  roof_binding_note: 'Owner 2026-10-01: slate blue is the Guild colour (Guild hall and Tier 2 annex only).',
  collision_rectangles: [[X0, Z0, X1, Z1]],
  roof_kit: { dormers: ['tower'], chimneys: ['tall_stone'], bays: [], roof_variant: 'guild_hall', bounds_rule: 'Within the footprint; the dormer tower and porch stay inside the height envelope.', source: 'Guild House Redesign v2' },
});
// The store shed moves to the west end of the stables (same size and facade), out of the hall's way.
const shed = p.buildings.find(b => b.id === 'store_shed');
shed.footprint = [-46.0, 95.0, -42.5, 98.5];
shed.door_face = 'w';
shed.door_position = [-46.0, 96.75];
shed.yaw_deg = 0;
shed.collision_rectangles = [shed.footprint.slice()];
const sr = p.routes.find(r => r.id === 'door_store_shed');
sr.centreline = [[-51.7, 96.75], [-48, 96.75], [-46.0, 96.75]];
sr.heights_m = sr.centreline.map(() => 0.6);
sr.grade = sr.centreline.slice(1).map(() => 0);
// A back lane from the yard up the west side of the stables reaches the shed's door spur.
const aisle = p.routes.find(r => r.id === 'guild_court_aisle');
const lane = JSON.parse(JSON.stringify(aisle));
lane.id = 'stable_back_lane';
lane.centreline = [[-43, 108], [-47, 108], [-51.7, 108], [-51.7, 102], [-51.7, 96.75]];
lane.heights_m = lane.centreline.map(() => 0.6);
lane.grade = lane.centreline.slice(1).map(() => 0);
delete lane.owner;
p.routes.splice(p.routes.indexOf(aisle) + 1, 0, lane);
// The garden east of the hall gives way so the cluster's hull stays clear of the lawn.
const edgeX = z => X1 + (-22 - X1) * Math.max(0, Math.min(1, (z - Z0) / (Z1 - Z0)));
const clamp = poly => poly.map(([x, z]) => (z >= Z0 - 1.5 && z <= Z1 + 0.5 && x < edgeX(z) + 0.5) ? [edgeX(z) + 0.5, z] : [x, z]);
for (const sp of p.green.spaces) if (sp.id === 'arrival_south_garden') sp.polygons = sp.polygons.map(clamp);
for (const zn of p.ground_zones) if (zn.id === 'arrival_south_garden_organic') zn.polygon = clamp(zn.polygon);
for (const ln of p.green.lawns) if (ln.id === 'arrival_south_garden_organic') ln.polygon = clamp(ln.polygon);
// The Guild Edge district reaches north to take the deeper hall.
const comp = p.districts.find(d => d.id === 'company');
comp.bounds = comp.bounds.map(q => [q[0], q[1] < 100 ? 89.5 : q[1]]);
// The cluster's ground envelope follows the buildings.
const cl = p.clusters.find(c => c.id === 'guild_compound');
cl.ground_envelope = [[-50, 118], [-50.4, 105.5], [-50.4, 99.4], [-46.4, 98.6], [-46.4, 94.6], [-38.3, 94.6], [-38.3, 91.0], [-25.6, 91.0], [-25.6, 97.8], [-22, 105.5], [-22, 118]];
// The hall's front door: its route, the city interior_door marker and the portal move with it.
const dr = p.routes.find(r => r.id === 'door_company_house');
dr.centreline = [[doorX, 108], [doorX, 106.6], [doorX, Z1]];
const im = p.markers.find(m => m.id === 'city/interior_door');
im.position = [doorX, 107.2];
const portal = p.portals.find(x => x.id === 'guild_interior_portal');
portal.city_position = [doorX, Z1];
p.v7d_changes = [
  'Owner 2026-10-01 (Locations/Eurydica/Interiors/Guild House Redesign v2.md): company_house becomes the two-storey Guild hall, 12.7 x 14.5 m at x -38.3..-25.6, z 91..105.5, facade guild_hall, height 7 m, slate blue roof (the Guild colour), gable front to the yard; its door route, the city interior_door marker and the interior portal move to its front door. The Guild Edge district reaches north to z 89.5.',
  'store_shed keeps its size and facade and moves behind the stables (x -46..-42.5, z 95..98.5, door west); a new stable_back_lane runs from the yard up the west side of the stables to its short door spur.',
  'arrival_south_garden: its west edge next to the hall moves east (at most about 2 m) so the lawn stays outside the Guild compound.',
];
fs.writeFileSync(f, JSON.stringify(p, null, 2) + '\n');
console.log('v7d written', p.buildings.length, 'buildings, door x', doorX);
