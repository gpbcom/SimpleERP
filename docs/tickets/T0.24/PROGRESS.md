# T0.24: Bruno collection scaffold, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [D406](../../specs/06-decisions/technical/d406-back-end.md)
- [REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)
- [D426](../../specs/06-decisions/technical/d426-testing-strategy.md)
- [CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa)
- [📌 REQ-T05-01 REST with OpenAPI behind one gateway](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md)
- [📌 REQ-T05-05 Contracts tested](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)
- [🏗️ Back end](../../technical/architecture/backend.md)
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md)
- [🏗️ API](../../technical/interfaces/api.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:14 | Plan written: 14 tasks, 3 waves | ticket-plan | ⏳ Awaiting approval |
| 2026-11-27 18:29 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-28 00:58 | Plan change: test_bruno_changes.py goes to tests/ci/detect_changes/bruno/, like helm/ and terraform/, so that tests/ci/detect_changes/ stays at five Python files (AGENT.md, File shape) | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-28 01:46 | Wave 1: 8 of 8 tasks done | workers | ✅ |
| 2026-11-28 01:46 | Integrate (Waves) | integrator | ✅ 8 integrated, 0 blocked, not committed |
| 2026-11-28 01:46 | Wave 2: 5 of 5 tasks done | workers | ✅ |
| 2026-11-28 01:46 | Integrate (Waves) | integrator | ✅ 5 integrated, 0 blocked, not committed |
| 2026-11-28 01:46 | Wave 3: 1 of 1 tasks done | workers | ✅ |
| 2026-11-28 01:46 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:46 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-28 01:46 | Review 1 (full) | reviewer | ⚠️ 1 blocking, 4 follow-ups |
| 2026-11-28 01:46 | Integrate (Review) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-28 01:46 | Review 2 (confirm fixes) | reviewer | ✅ 0 blocking, 3 follow-ups |
| 2026-11-28 01:46 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | 👀 | 👀 Awaiting code review |
| 2026-11-28 01:50 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 01:50 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| .github/scripts/detect_changes.py | The new docstring paragraph says 'the credential scan and the collections' freshness check run with the repository tests'. The freshness check runs in the services job of python.yml (step 'Bruno collection up to date'), not with the repository tests. Only the credential scan runs there. Correct the sentence (K10). |
| docs/technical/interfaces/api.md | The footer was changed to 'Last reviewed: 2026-11-28 (GH-2)'. Name this ticket, '(T0.24)', as the other two pages do (K08). |
| tests/ci/bruno_credentials/test_bruno_credentials.py tests/ci/bruno_credentials/helpers.py | Move the module-level `plant` function of the test file into helpers.py, or make it a method of TestBrunoCredentials (K02). |
| .github/scripts/bruno_collection.py tests/ci/bruno_collection/test_generate.py | Path parameters become `{{customer_id}}` collection variables in the URL and also get a `params:path` block. Bruno's own path-parameter form is `:customer_id`, which goes with `params:path`. This does not affect platform, which has only GET /v1/health. Settle on one form before the first service with path parameters, and align `seq` to count within each folder as the brief said (K09 records the brief and the tests disagreeing). Owners K09 and K03. |
| docs/tickets/T0.24/tests-evidences/bruno-platform.json docs/tickets/T0.24/tests-evidences/bruno-platform.xml | The JSON report's suitename fields hold the absolute local worktree path (/home/<user>/.../.claude/worktrees/wf_c22066f6-c08-24/...), and the JUnit report holds the machine's hostname. These files get committed. Rerun with paths relative to the collection, or strip them before saving, so that no local path or hostname reaches the repository. Owner K14. |
| docs/tickets/T0.24/tests-evidences/ | Unlike the other evidence files, the Bruno reports do not record the command or the stack they ran against. Add a short bruno-run.txt with the `docker compose -f compose.e2e.yaml up` and `npx --yes @usebruno/cli@4.2.1 run --env stage ...` commands, so the person can see the run matched stage.yml (lines 131-134). Owner K14. |
| tests/ci/workflows/test_stage_workflow.py | The run shows that Bruno CLI 4.2.1 goes into tests/ by default, so stage.yml needs no recursive flag. A later CLI upgrade could change that without anyone noticing. Consider making the stage step fail when the JSON summary reports totalTests == 0. Owners K12 and K06. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.24` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 01:50:23 |
| ⏱️ **Overall ticket time** (first start to last activity) | **7h43m17s** |
| 🤖 Time with agents working (sum of runs) | 26m05s |
| ⏸️ Time between runs (approvals, fixes) | 7h17m11s |
| 🔁 Workflow runs | 3 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **22.21M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 83k | 1.07M | 3.63M | **4.79M** |
| 🔵 sonnet | 0k | 203k | 1.35M | 9.32M | **10.88M** |
| 🟣 opus | 0k | 126k | 477k | 5.95M | **6.55M** |
| **All models** | 0k | 413k | 2.89M | 18.91M | **22.21M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:15:15 · ⏱️ 8m09s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:08:00 | 0m54s | 2 |
| Check | 18:08:00 | 18:08:04 | 0m03s | 1 |
| Plan | 18:08:04 | 18:14:08 | 6m03s | 1 |
| Write | 18:14:08 | 18:15:15 | 1m06s | 2 |

Tokens of this run: 0k · 157k · 708k · 5.51M · **6.37M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.24 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.24 | 🔵 sonnet | 18:07:12 | 18:08:00 | 0m47s | 0k | 27k | 228k | 1.62M | **1.87M** |
| ✅ check TICKET.md T0.24 | 🟢 haiku | 18:08:00 | 18:08:04 | 0m03s | 0k | 0k | 37k | 73k | **112k** |
| ✅ planner T0.24 | 🟣 opus | 18:08:04 | 18:14:08 | 6m03s | 0k | 93k | 227k | 3.26M | **3.58M** |
| ✅ scribe T0.24 | 🟢 haiku | 18:14:08 | 18:15:11 | 1m03s | 0k | 34k | 141k | 446k | **623k** |
| ✅ check PLAN.md T0.24 | 🟢 haiku | 18:15:11 | 18:15:15 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-28 01:31:52 to 01:47:50 · ⏱️ 15m57s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:31:52 | 01:32:36 | 0m43s | 4 |
| Waves | 01:32:37 | 01:39:45 | 7m07s | 17 |
| Verify | 01:39:45 | 01:40:37 | 0m52s | 1 |
| Review | 01:40:38 | 01:46:11 | 5m33s | 5 |
| Finish | 01:46:11 | 01:47:50 | 1m38s | 4 |

Tokens of this run: 0k · 245k · 1.89M · 12.52M · **14.65M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.24 | 🟢 haiku | 01:31:52 | 01:32:03 | 0m10s | 0k | 4k | 44k | 167k | **216k** |
| ✅ plan check T0.24 | 🟢 haiku | 01:32:03 | 01:32:07 | 0m03s | 0k | 0k | 38k | 76k | **115k** |
| ✅ start rule T0.24 | 🟢 haiku | 01:32:07 | 01:32:20 | 0m13s | 0k | 0k | 38k | 76k | **115k** |
| ✅ integrator prepare T0.24 | 🔵 sonnet | 01:32:21 | 01:32:36 | 0m14s | 0k | 0k | 37k | 84k | **122k** |
| ✅ K01 test-writer | 🔵 sonnet | 01:32:37 | 01:34:19 | 1m42s | 0k | 6k | 65k | 758k | **830k** |
| ✅ K02 test-writer | 🔵 sonnet | 01:32:38 | 01:35:16 | 2m37s | 0k | 32k | 72k | 441k | **546k** |
| ✅ K03 test-writer | 🔵 sonnet | 01:32:40 | 01:34:23 | 1m42s | 0k | 40k | 77k | 804k | **921k** |
| ✅ K04 test-writer | 🔵 sonnet | 01:32:41 | 01:34:09 | 1m27s | 0k | 6k | 50k | 369k | **427k** |
| ✅ K05 test-writer | 🔵 sonnet | 01:32:44 | 01:33:09 | 0m24s | 0k | 2k | 45k | 177k | **225k** |
| ✅ K06 test-writer | 🔵 sonnet | 01:32:46 | 01:34:06 | 1m19s | 0k | 4k | 49k | 274k | **327k** |
| ✅ K07 doc-writer | 🟢 haiku | 01:32:48 | 01:33:35 | 0m46s | 0k | 11k | 71k | 612k | **694k** |
| ✅ K08 doc-writer | 🟢 haiku | 01:32:52 | 01:33:26 | 0m33s | 0k | 7k | 50k | 599k | **657k** |
| ✅ integrator Waves | 🔵 sonnet | 01:35:33 | 01:35:53 | 0m19s | 0k | 1k | 42k | 208k | **252k** |
| ✅ K09 implementer | 🔵 sonnet | 01:35:55 | 01:38:10 | 2m15s | 0k | 38k | 79k | 947k | **1.07M** |
| ✅ K10 implementer | 🔵 sonnet | 01:35:56 | 01:36:45 | 0m49s | 0k | 1k | 44k | 137k | **183k** |
| ✅ K11 implementer | 🔵 sonnet | 01:35:58 | 01:36:19 | 0m21s | 0k | 1k | 42k | 180k | **225k** |
| ✅ K12 implementer | 🔵 sonnet | 01:36:01 | 01:36:25 | 0m23s | 0k | 2k | 54k | 333k | **390k** |
| ✅ K13 implementer | 🔵 sonnet | 01:36:03 | 01:36:21 | 0m17s | 0k | 1k | 40k | 177k | **218k** |
| ✅ integrator Waves | 🔵 sonnet | 01:38:27 | 01:38:44 | 0m17s | 0k | 0k | 41k | 167k | **209k** |
| ✅ K14 implementer | 🔵 sonnet | 01:38:46 | 01:39:31 | 0m45s | 0k | 3k | 44k | 815k | **863k** |
| ✅ integrator Waves | 🔵 sonnet | 01:39:34 | 01:39:45 | 0m10s | 0k | 0k | 41k | 168k | **211k** |
| ✅ verifier round 1 | 🟢 haiku | 01:39:45 | 01:40:37 | 0m52s | 0k | 0k | 43k | 76k | **120k** |
| ✅ reviewer round 1 | 🟣 opus | 01:40:38 | 01:43:28 | 2m50s | 0k | 24k | 192k | 2.23M | **2.45M** |
| ✅ FIX-K12+K06+K14 implementer (fix) | 🔵 sonnet | 01:43:30 | 01:44:17 | 0m47s | 0k | 3k | 58k | 489k | **551k** |
| ✅ integrator Review | 🔵 sonnet | 01:44:19 | 01:44:31 | 0m12s | 0k | 0k | 42k | 169k | **213k** |
| ✅ verifier after review 1 | 🟢 haiku | 01:44:32 | 01:45:25 | 0m52s | 0k | 0k | 39k | 80k | **121k** |
| ✅ reviewer round 2 | 🟣 opus | 01:45:25 | 01:46:11 | 0m46s | 0k | 7k | 56k | 461k | **526k** |
| ✅ scribe T0.24 | 🟢 haiku | 01:46:11 | 01:46:37 | 0m26s | 0k | 11k | 115k | 393k | **520k** |
| ✅ explainer T0.24 | 🔵 sonnet | 01:46:11 | 01:47:38 | 1m26s | 0k | 25k | 151k | 915k | **1.09M** |
| ✅ docs check T0.24 1 | 🟢 haiku | 01:47:38 | 01:47:43 | 0m04s | 0k | 0k | 40k | 77k | **117k** |
| ✅ scribe T0.24 (timings) | 🟢 haiku | 01:47:46 | 01:47:50 | 0m04s | 0k | 0k | 72k | 49k | **122k** |

### 3. ticket-run · 2026-11-28 01:48:24 to 01:50:23 · ⏱️ 1m58s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 01:48:24 | 01:49:14 | 0m50s | 4 |
| Waves | | | not run | 0 |
| Verify | 01:49:15 | 01:50:08 | 0m52s | 1 |
| Review | | | not run | 0 |
| Finish | 01:50:08 | 01:50:23 | 0m14s | 3 |

Tokens of this run: 0k · 9k · 295k · 879k · **1.19M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.24 | 🟢 haiku | 01:48:24 | 01:48:38 | 0m14s | 0k | 5k | 53k | 342k | **402k** |
| ✅ plan check T0.24 | 🟢 haiku | 01:48:38 | 01:48:42 | 0m04s | 0k | 0k | 37k | 79k | **117k** |
| ✅ start rule T0.24 | 🟢 haiku | 01:48:45 | 01:48:59 | 0m13s | 0k | 0k | 37k | 40k | **77k** |
| ✅ integrator prepare T0.24 | 🔵 sonnet | 01:48:59 | 01:49:14 | 0m14s | 0k | 0k | 38k | 86k | **124k** |
| ✅ verifier round 1 | 🟢 haiku | 01:49:15 | 01:50:08 | 0m52s | 0k | 0k | 39k | 80k | **121k** |
| ✅ scribe T0.24 | 🟢 haiku | 01:50:08 | 01:50:16 | 0m07s | 0k | 2k | 52k | 169k | **224k** |
| ✅ docs check T0.24 1 | 🟢 haiku | 01:50:16 | 01:50:20 | 0m04s | 0k | 0k | 37k | 80k | **117k** |
| 🔄 integrator finish T0.24 | 🔵 sonnet | 01:50:22 | 01:50:23 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
