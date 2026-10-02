import fs from 'node:fs';
const root='D:/Codex/IMC/runs/ui-battle-ring-v1';
let s=fs.readFileSync(root+'/sources/revise-v1b.mjs','utf8');
s=s.replaceAll('history/v1-60-ticks','history/v1b-hub').replace("const tracks=['tl_track_enemy','tl_track_party'];","const tracks=['tl_hub','tl_act_plate'];").replace('for(const n of tracks)for(const suffix','for(const n of [\'tl_hub\'])for(const suffix');
s=s.replace('for(const p of manifest.pieces){const old=',"for(const p of manifest.pieces){if(p.piece==='tl_act_plate')continue;const old=");
s=s.replace("fs.writeFileSync(root+'/sources/revision-verification.json'", "fs.writeFileSync(root+'/sources/revision-v1c-verification.json'");
s=s.replace('backup_pngs:4','backup_pngs:2').replace("manifest_changes:'two track notes only'","manifest_changes:'new ACT plate and hub notes only'");
s=s.replace("console.log('BATTLE_V1B_RENDERED; 42 other piece files unchanged; four backups verified');","console.log('BATTLE_V1C_RENDERED; 45 other piece files unchanged; two hub backups verified');");
fs.writeFileSync(root+'/sources/revise-v1c.mjs',s);
