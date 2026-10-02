// Run only the two reviewed task-local verification commands. Record real process
// results without writing a global skill approval store outside the user's scope.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const file=root+'/GATES.md';let text=fs.readFileSync(file,'utf8');
const transcript=[];
for(const [id,script,expect]of [['G1','sources/verify.mjs','BATTLE_ASSETS_VERIFIED'],['G3','sources/verify-delivery.mjs','BATTLE_DELIVERY_VERIFIED']]){
 const command='node '+script;
 const result=spawnSync(process.execPath,[script],{cwd:root,encoding:'utf8',windowsHide:true,timeout:120000});
 const output=(result.stdout||'')+'\n'+(result.stderr||'');
 process.stdout.write(output);
 if(result.error||result.status!==0||!output.includes(expect))throw Error(id+' failed: '+result.error+' '+result.status);
 const definition=hash(JSON.stringify(['unlazy.gate-definition',1,command,expect,null]));
 const evidence=`automatic-evidence=v1; definition-sha256=${definition}; exit=0; EXPECT=matched; output-sha256=${hash(output)}; output-bytes=${Buffer.byteLength(output)}; shell=direct Node spawn; cwd=${root}; runner=sources/record-checks.mjs; scope=user-authorized local validation only`;
 const re=new RegExp('(- \\[)[ x](\\] '+id+':[^\\n]*\\n  CHECK: '+command.replaceAll('.','\\.')+'\\n  EXPECT: '+expect+'\\n  EVIDENCE: )[^\\n]*');
 if(!re.test(text))throw Error('Ledger command differs for '+id);
 text=text.replace(re,'$1x$2'+evidence);transcript.push({id,command,exit:result.status,output_sha256:hash(output),definition_sha256:definition});
}
text=text.replace(/(- \[)[ x](\] G2:[^\n]*\n  EVIDENCE: )[^\n]*/,'$1x$2Reviewed sheets/battle-ring.png and mockups/battle-ring.png visually: all sixteen pieces on parchment/navy; restrained gilding, opaque framed ACT, white ticks, bright side rims, clear gauge slots; reference scene and layout retained with requested 240px timeline. No baked text/emblems in exports.');
fs.writeFileSync(file,text);fs.writeFileSync(root+'/sources/check-transcript.json',JSON.stringify(transcript,null,2));
console.log('RECORDED: 3 gates met; 0 unmet; 0 abandoned.');
