// Checks the design-document set: the register's files exist, the implementation spec is complete, and it covers every GDD section.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const gd = path.join(path.dirname(fileURLToPath(import.meta.url)), ".."), root = path.join(gd, "..");
const fail = [];
const read = f => fs.readFileSync(f, "utf8");

// 1. every concrete path in the register's current-document table exists
const reg = read(path.join(gd, "FGC_00_Document_Register.md"));
const table = reg.slice(reg.indexOf("## 1. Current document set"), reg.indexOf("## 2. Authority order"));
for (const m of table.matchAll(/^\| \d\d \| `([^`]+)`/gm)) {
  const p = m[1];
  if (p.includes("<")) continue; // per-chapter / per-officer patterns
  const abs = /^[A-Z]:\//.test(p) ? p : path.join(root, p.replace(/\/$/, ""));
  if (!fs.existsSync(abs)) fail.push("register lists a missing file: " + p);
}

// 2. the spec has sections 00-18, no unmerged placeholders, no TBD/TODO
const spec = read(path.join(gd, "FGC_07_Implementation_Spec.md"));
for (let i = 0; i <= 18; i++) { const n = String(i).padStart(2, "0"); if (!new RegExp("^# " + n + "\\. ", "m").test(spec)) fail.push("spec section missing: " + n); }
if (/Codex draft, merged below after review/.test(spec)) fail.push("spec still has an unmerged Codex placeholder");
if (/\b(TBD|TODO)\b/.test(spec)) fail.push("spec contains TBD/TODO");

// 3. every top-level GDD section number appears in the spec's coverage appendix
const gdd = read(path.join(gd, "IMC GDD.md"));
const appendix = spec.slice(spec.indexOf("## Appendix A: GDD coverage"));
for (const m of gdd.matchAll(/^## (\d+)[a-z]?\. /gm)) if (!new RegExp("\\| (" + m[1] + "\\b|[^|]*, " + m[1] + "[ a-z])").test(appendix) && !appendix.includes("| " + m[1] + " ")) fail.push("GDD section " + m[1] + " not in the spec coverage table");

if (fail.length) { console.log(fail.join("\n")); console.log("DOCS FAILED"); process.exitCode = 1; } else console.log("DOCS OK");
