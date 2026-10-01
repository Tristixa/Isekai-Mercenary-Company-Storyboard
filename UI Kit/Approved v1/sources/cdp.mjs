// Tiny Chrome DevTools Protocol driver (Node 22+ global WebSocket): open a page, run steps, screenshot.
import { spawn } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
export const sleep = ms => new Promise(r => setTimeout(r, ms));
export async function openPage(url, { width = 1320, height = 1900 } = {}) {
  const chrome = ["C:/Program Files/Google/Chrome/Application/chrome.exe", "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"].find(p => fs.existsSync(p));
  if (!chrome) throw new Error("Chrome not found");
  const prof = fs.mkdtempSync(path.join("D:/Codex/IMC/runs/ui-kit-v1", "imc-cdp-")), port = 9300 + Math.floor(Math.random() * 500);
  const proc = spawn(chrome, ["--headless=new", "--no-sandbox", "--disable-gpu", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist", "--no-first-run", "--disable-extensions", "--autoplay-policy=no-user-gesture-required",
    `--remote-debugging-port=${port}`, `--user-data-dir=${prof}`, `--window-size=${width},${height}`, "about:blank"], { stdio: "ignore", windowsHide: true });
  let ws;
  for (let i = 0; i < 60 && !ws; i++) { await sleep(250); try { const list = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); const pg = list.find(t => t.type === "page"); if (pg) ws = new WebSocket(pg.webSocketDebuggerUrl); } catch {} }
  if (!ws) { proc.kill(); throw new Error("no devtools endpoint"); }
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  let id = 0; const pending = new Map(), logs = [];
  ws.onmessage = ev => { const m = JSON.parse(ev.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
    if (m.method === "Runtime.exceptionThrown") logs.push("exception: " + (m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text));
    if (m.method === "Runtime.consoleAPICalled" && m.params.type === "error") logs.push("console.error: " + m.params.args.map(a => a.value ?? a.description).join(" ")); };
  const send = (method, params = {}) => new Promise(res => { const i = ++id; pending.set(i, res); ws.send(JSON.stringify({ id: i, method, params })); });
  await send("Runtime.enable"); await send("Page.enable");
  await send("Emulation.setDeviceMetricsOverride", { width, height, deviceScaleFactor: 1, mobile: false });
  await send("Page.navigate", { url });
  const evaluate = async expr => { const r = await send("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise: true }); if (r.result?.exceptionDetails) throw new Error(r.result.exceptionDetails.text); return r.result?.result?.value; };
  const shot = async (file, clip) => { const r = await send("Page.captureScreenshot", { format: "png", ...(clip ? { clip: { ...clip, scale: 1 } } : {}) }); fs.writeFileSync(file, Buffer.from(r.result.data, "base64")); };
  const key = async (type, key, code, vk) => send("Input.dispatchKeyEvent", { type, key, code, windowsVirtualKeyCode: vk });
  const close = () => { try { ws.close(); } catch {} proc.kill(); };
  return { send, evaluate, shot, key, close, logs };
}
export function wrapPage(builtFile) {
  const tmp = fs.mkdtempSync(path.join("D:/Codex/IMC/runs/ui-kit-v1", "imc-page-")), page = path.join(tmp, "index.html");
  fs.writeFileSync(page, `<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>body{margin:0}</style></head><body>${fs.readFileSync(builtFile, "utf8")}</body></html>`);
  return page;
}

