# Checks for plan v7c

Run from this folder: `python -B check_plan_v7c.py ../eurydica-plan.json`. It must print `PLAN_CHECK_PASS` and writes `check-result-v7c.json` (the current copy is `check-result.json`). Verified from this location on 2026-10-01.

- `eurydica-plan-v7.json` and `eurydica-plan-v7b.json` are the earlier passes, kept only because the v7c checks compare against them. The v5 source it compares against is `../../Archive/Build Plan v5/eurydica-plan.json`.
- The `build_*`, `landscape_*`, `render_review*`, `write_delivery*` and similar scripts are the authoring record from the Codex run (`D:/Codex/IMC/runs/eurydica-plan-v7/`). Copies here had their v5 path repointed to `Archive/`; the older v7/v7b delivery checks still expect the run folder's layout.
