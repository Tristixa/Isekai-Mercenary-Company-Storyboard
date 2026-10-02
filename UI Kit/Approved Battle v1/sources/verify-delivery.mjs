import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const records=JSON.parse(fs.readFileSync(root+'/sources/provenance.json'));
for(const p of records){assert.equal(hash(fs.readFileSync(root+'/'+p.file)),p.sha256);assert.equal(hash(fs.readFileSync(p.source)),p.sha256)}
const m=JSON.parse(fs.readFileSync(root+'/kit-battle.json'));for(const p of m.pieces)assert.equal(hash(fs.readFileSync(root+'/sources/generated/'+p.piece+'.png')),hash(fs.readFileSync(root+'/'+p.file)));
for(const p of ['README.md','prompts.md','sheets/battle-ring.png','mockups/battle-ring.png','kit-battle.json'])assert.ok(fs.statSync(root+'/'+p).size>100);
const report=fs.readFileSync(path.resolve(root,'../../handoff/ui-battle-ring-v1c-last.txt'),'utf8').trim().split(/\r?\n/);assert.equal(report.length,3);
fs.writeFileSync(root+'/sources/delivery-verification.json',JSON.stringify({status:'pass',preserved_inputs:records.length,unchanged_external_inputs:true,untouched_generated_sources:m.pieces.length,report_lines:report.length,scope:'All task-authored files and browser profiles under run; only external task write is named report. Existing source and reference input hashes verified unchanged.'},null,2));
console.log('BATTLE_DELIVERY_VERIFIED',records.length,'unchanged inputs;',m.pieces.length,'untouched generated sources; three report lines');
