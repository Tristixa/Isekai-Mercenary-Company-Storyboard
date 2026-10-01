# Gates: design document set (register + implementation spec v0.1)

OWNS: Game Design/**

Scope: the document register (FGC_00) and the implementation spec (FGC_07) are complete, consistent and cover the GDD before any Godot work starts.

- [x] G1: the register's files exist, the spec has all sections 00-18 with no unmerged drafts or TBDs, and every GDD section is in the spec's coverage table
  CHECK: node tools/check-docs.mjs
  EXPECT: DOCS OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=cb92bc305ae9607fe1e5927072bd8a9a5776ffebb56e10e40ad6d0603b13d735; exit=0; EXPECT=matched; output-sha256=19a0e3bf6b510e1f141b992a7af59e17fee9c7246373fd6b5729e8be239a52fc; output-bytes=8; shell=C:\Windows\system32\cmd.exe; cwd=D:\Storyboards\Isekai Mercenary Company\Game Design; path=47acdbca97b3/43 entries

- [x] G2: Codex's sections (§06 content formats, §07 sim modules, §08 saves/RNG, §16 testing, §18 port list) are reviewed by Claude against the GDD: no invented game rules, every [spec decision] listed, and every GDD system mapped to a sim module
  EVIDENCE: 2026-09-28. Reviewed §07.2–07.4 against the GDD: tick order, 07:00 stamina, monster skill every 5th action, work-order no-idle, night accounting and region transfer match. 27 decisions (D01–D27) listed in Appendix B. Of the §06.7 gaps, items 2/4/5/6 were fixed in the GDD; item 1 (monster skill approval) and item 3 (M3 minigame tuning) remain, as intended. §03/§05 wording aligned to Codex's §07.1 envelopes and absolute ticks.

- [ ] G3: the owner has reviewed the register and the spec
  EVIDENCE:
