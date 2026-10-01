# Gates: Eurydica v7c final candidate refinement

OWNS: runs/eurydica-plan-v7/*v7c*, runs/eurydica-plan-v7/Eurydica Build Plan.md, handoff/eurydica-plan-v7c-last.txt

Scope: Four requested refinements from v7b, preserved identities and functional checks, three reviewed images, appended plan and six-line report. Candidate only.

- [x] G1: Candidate preserves buildings, clusters and markers; roads, doors, grove planting and reshaped courts meet v7c geometry checks
  CHECK: C:/Users/Tristixa-/.codex/skills/sprite-gen/.venv/Scripts/python.exe -B check_plan_v7c.py --self-test
  EXPECT: PLAN_CHECK_PASS
  EVIDENCE: automatic-evidence=v1; definition-sha256=c0a2215e17f034e53e55c11bbb703e14876403a9b90f2c19aa9a98679c66d399; exit=0; EXPECT=matched; output-sha256=3bc735e1439ec85c84d4a3f38ccf31405aeb073e2295f734c16b0c479c6cd277; output-bytes=4480; shell=cmd.exe; cwd=D:\Codex\IMC\runs\eurydica-plan-v7; runner=task-local run_gates.mjs; path-sha256=5e17988682b0046811a117cff647f6741c8c9ea252850fa6e17f5b92b5e97ac8

- [x] G2: Three review images match checked geometry; all prior files preserved; v7c documentation and six-line report agree with measurements
  CHECK: C:/Users/Tristixa-/.codex/skills/sprite-gen/.venv/Scripts/python.exe -B check_delivery_v7c.py
  EXPECT: DELIVERY_CHECK_PASS
  EVIDENCE: automatic-evidence=v1; definition-sha256=7a34aa17ee81792e06a778d01b4724e1d7f4fbded4b2d92ce7bdcb3f75d436f2; exit=0; EXPECT=matched; output-sha256=cd9c26610f32bb56b05101818ce3153c4c2cc47e10cec6f668c166f03c7c001c; output-bytes=157; shell=cmd.exe; cwd=D:\Codex\IMC\runs\eurydica-plan-v7; runner=task-local run_gates.mjs; path-sha256=5e17988682b0046811a117cff647f6741c8c9ea252850fa6e17f5b92b5e97ac8

- [x] G3: Final views visibly show soft road bends, simpler branches, clumped groves and irregular civic and south-east yards against f03
  EVIDENCE: Viewed cluster map, north-facing massing and equal-scale comparison against f03; bends, dense groves, irregular paving/hedge and retained groups visible. Road target shortfall disclosed. visual-review-v7c.json sha256=2347bd03efc199e15d8486501ca2cd4bb66e10324270070a6d4496130d4ad3e7; candidate only.
