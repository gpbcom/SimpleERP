# T0.01: Mono-repo folders and workspaces, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Repository layout](../../technical/architecture/repository-layout.md)
- [D406 Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [D407 Front end](../../specs/06-decisions/technical/d407-front-end.md)
- [Configuration](../../technical/architecture/configuration.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [📜 D415 Supply chain controls](../../specs/06-decisions/technical/d415-supply-chain-controls.md)
- [🏗️ Supply chain and licences](../../technical/security/supply-chain-and-licences.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:15 | Plan written: 14 tasks, 3 waves | scribe | ⏳ Awaiting approval |
| 2026-11-27 18:27 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 18:52 | Wave 1: 5 of 5 tasks done | workers | ✅ |
| 2026-11-27 18:52 | Integrate (Waves) | integrator | ✅ 5 integrated, 0 blocked, not committed |
| 2026-11-27 18:52 | Wave 2: 7 of 7 tasks done | workers | ✅ |
| 2026-11-27 18:52 | Integrate (Waves) | integrator | ✅ 7 integrated, 0 blocked, not committed |
| 2026-11-27 18:52 | Wave 3: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 18:52 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 18:52 | Verify 1 (2 not applicable) | verifier | ❌ 9 failures |
| 2026-11-27 18:52 | Integrate (Verify) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 18:52 | Verify 2 (2 not applicable) | verifier | ✅ passed |
| 2026-11-27 18:52 | Review 1 (full) | reviewer | ✅ 0 blocking, 7 follow-ups |
| 2026-11-27 18:52 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 19:09 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 19:09 | Verify 1 (2 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| docs/tickets/T0.01/tests-evidences/ | Add a `uv sync --locked` evidence file for acceptance criterion 1, and consider adding that command to checks.py next to the pnpm install check. Owner: verifier (K06 done_when). |
| backend/models/pyproject.toml | Pin the `uv_build` backend exactly (`uv_build==0.12.21`) so that building erp_models is reproducible, or record why a range is accepted. Owner: K06. |
| README.md | Reword the Project structure paragraph: say that every folder listed in D438's first tickets exists and that `frontend/portals/` and `compose.e2e.yaml` come later. Owner: K12. |
| docs/technical/architecture/configuration.md | Add one line saying that today's root `conf/logger.yaml` moves into each service when services arrive (T0.06), or mark the per-service logger row as planned too. Owner: K13. |
| tests/layout/test_pnpm_workspace.py | In `test_the_engines_allow_node_22_only`, compare only the major numbers of engines.node, not every digit run, so that `^22.11` is accepted. Owner: K03. |
| pyproject.toml | Wrap the first line of the rewritten `[tool.uv]` comment, which is about 122 characters, at 120. Owner: K06. |
| tests/ci/detect_changes/test_repository_layout.py tests/layout/test_uv_workspace.py tests/layout/test_readme_quick_start.py | Drop the '# Standard library imports' group comments, as AGENT.md leaves them out of tests. Owner: K04, K02, K05. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.01` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 19:09:23 |
| ⏱️ **Overall ticket time** (first start to last activity) | **1h02m17s** |
| 🤖 Time with agents working (sum of runs) | 27m47s |
| ⏸️ Time between runs (approvals, fixes) | 34m30s |
| 🔁 Workflow runs | 4 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **24.27M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 100k | 1.46M | 4.11M | **5.67M** |
| 🔵 sonnet | 0k | 128k | 1.28M | 8.46M | **9.87M** |
| 🟣 opus | 0k | 130k | 596k | 8.01M | **8.74M** |
| **All models** | 0k | 359k | 3.33M | 20.58M | **24.27M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:15:36 · ⏱️ 8m30s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:43 | 0m37s | 2 |
| Check | 18:07:43 | 18:07:47 | 0m03s | 1 |
| Plan | 18:07:48 | 18:14:28 | 6m40s | 1 |
| Write | 18:14:28 | 18:15:36 | 1m08s | 2 |

Tokens of this run: 0k · 152k · 811k · 6.94M · **7.90M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.01 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.01 | 🔵 sonnet | 18:07:12 | 18:07:43 | 0m30s | 0k | 15k | 177k | 791k | **985k** |
| ✅ check TICKET.md T0.01 | 🟢 haiku | 18:07:43 | 18:07:47 | 0m03s | 0k | 0k | 37k | 73k | **112k** |
| ✅ planner T0.01 | 🟣 opus | 18:07:48 | 18:14:28 | 6m40s | 0k | 100k | 394k | 5.32M | **5.81M** |
| ✅ scribe T0.01 | 🟢 haiku | 18:14:28 | 18:15:32 | 1m04s | 0k | 34k | 125k | 607k | **766k** |
| ✅ check PLAN.md T0.01 | 🟢 haiku | 18:15:33 | 18:15:36 | 0m03s | 0k | 0k | 37k | 73k | **112k** |

### 2. ticket-run · 2026-11-27 18:29:49 to 18:30:13 · ⏱️ 0m24s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 18:29:49 | 18:30:13 | 0m24s | 4 |
| Waves | | | not run | 0 |
| Verify | | | not run | 0 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 5k · 196k · 219k · **422k** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.01 | 🟢 haiku | 18:29:49 | 18:29:57 | 0m08s | 0k | 4k | 83k | 74k | **161k** |
| ✅ plan check T0.01 | 🟢 haiku | 18:29:57 | 18:30:01 | 0m04s | 0k | 0k | 37k | 34k | **72k** |
| ✅ start rule T0.01 | 🟢 haiku | 18:30:02 | 18:30:06 | 0m04s | 0k | 0k | 34k | 37k | **72k** |
| ✅ integrator prepare T0.01 | 🔵 sonnet | 18:30:07 | 18:30:13 | 0m06s | 0k | 0k | 41k | 73k | **115k** |

### 3. ticket-run · 2026-11-27 18:37:10 to 18:54:28 · ⏱️ 17m17s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 18:37:10 | 18:37:46 | 0m35s | 4 |
| Waves | 18:37:48 | 18:41:53 | 4m05s | 17 |
| Verify | 18:41:54 | 18:49:48 | 7m54s | 5 |
| Review | 18:49:50 | 18:52:32 | 2m42s | 1 |
| Finish | 18:52:33 | 18:54:28 | 1m54s | 4 |

Tokens of this run: 0k · 191k · 1.93M · 12.78M · **14.90M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.01 | 🟢 haiku | 18:37:10 | 18:37:22 | 0m11s | 0k | 3k | 49k | 229k | **282k** |
| ✅ plan check T0.01 | 🟢 haiku | 18:37:22 | 18:37:26 | 0m03s | 0k | 0k | 36k | 34k | **71k** |
| ✅ start rule T0.01 | 🟢 haiku | 18:37:26 | 18:37:31 | 0m05s | 0k | 0k | 36k | 70k | **107k** |
| ✅ integrator prepare T0.01 | 🔵 sonnet | 18:37:32 | 18:37:46 | 0m14s | 0k | 0k | 38k | 74k | **114k** |
| ✅ K01 test-writer | 🔵 sonnet | 18:37:48 | 18:38:24 | 0m36s | 0k | 8k | 45k | 419k | **473k** |
| ✅ K02 test-writer | 🔵 sonnet | 18:37:49 | 18:38:31 | 0m41s | 0k | 4k | 42k | 342k | **389k** |
| ✅ K03 test-writer | 🔵 sonnet | 18:37:51 | 18:38:24 | 0m32s | 0k | 9k | 46k | 377k | **433k** |
| ✅ K04 test-writer | 🔵 sonnet | 18:37:53 | 18:38:23 | 0m30s | 0k | 6k | 45k | 401k | **453k** |
| ✅ K05 test-writer | 🔵 sonnet | 18:37:55 | 18:38:24 | 0m29s | 0k | 8k | 46k | 470k | **526k** |
| ✅ integrator Waves | 🔵 sonnet | 18:38:35 | 18:38:53 | 0m17s | 0k | 0k | 37k | 155k | **194k** |
| ✅ K06 implementer | 🔵 sonnet | 18:38:55 | 18:39:32 | 0m37s | 0k | 5k | 51k | 423k | **480k** |
| ✅ K07 implementer | 🔵 sonnet | 18:38:56 | 18:39:35 | 0m39s | 0k | 8k | 46k | 558k | **613k** |
| ✅ K08 implementer | 🔵 sonnet | 18:38:57 | 18:39:40 | 0m42s | 0k | 7k | 45k | 514k | **567k** |
| ✅ K09 implementer | 🔵 sonnet | 18:38:59 | 18:39:16 | 0m17s | 0k | 1k | 37k | 126k | **165k** |
| ✅ K10 frontend-implementer | 🔵 sonnet | 18:39:00 | 18:40:38 | 1m37s | 0k | 11k | 66k | 1.48M | **1.56M** |
| ✅ K11 frontend-implementer | 🔵 sonnet | 18:39:02 | 18:39:28 | 0m26s | 0k | 3k | 42k | 337k | **383k** |
| ✅ K12 doc-writer | 🟢 haiku | 18:39:04 | 18:39:34 | 0m30s | 0k | 11k | 99k | 839k | **951k** |
| ✅ integrator Waves | 🔵 sonnet | 18:40:40 | 18:41:01 | 0m20s | 0k | 0k | 38k | 155k | **194k** |
| ✅ K13 doc-writer | 🟢 haiku | 18:41:02 | 18:41:37 | 0m34s | 0k | 8k | 49k | 373k | **431k** |
| ✅ K14 doc-writer | 🟢 haiku | 18:41:04 | 18:41:33 | 0m29s | 0k | 7k | 47k | 427k | **482k** |
| ✅ integrator Waves | 🔵 sonnet | 18:41:43 | 18:41:53 | 0m09s | 0k | 0k | 37k | 116k | **154k** |
| ✅ verifier round 1 | 🟢 haiku | 18:41:54 | 18:47:54 | 6m00s | 0k | 3k | 120k | 35k | **159k** |
| ❌ FIX-K07+K12+K11+K08+K09 implementer (fix) | 🔵 sonnet | 18:47:55 | 18:48:28 | 0m32s | 0k | 2k | 52k | 295k | **350k** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 18:47:57 | 18:48:18 | 0m21s | 0k | 2k | 49k | 202k | **254k** |
| ✅ integrator Verify | 🔵 sonnet | 18:48:29 | 18:48:39 | 0m10s | 0k | 0k | 46k | 192k | **239k** |
| ✅ verifier round 2 | 🟢 haiku | 18:48:41 | 18:49:48 | 1m07s | 0k | 0k | 67k | 119k | **187k** |
| ✅ reviewer round 1 | 🟣 opus | 18:49:50 | 18:52:32 | 2m42s | 0k | 29k | 201k | 2.69M | **2.92M** |
| ✅ scribe T0.01 | 🟢 haiku | 18:52:33 | 18:53:02 | 0m29s | 0k | 12k | 97k | 322k | **433k** |
| ✅ explainer T0.01 | 🔵 sonnet | 18:52:33 | 18:54:17 | 1m44s | 0k | 28k | 199k | 873k | **1.10M** |
| ✅ docs check T0.01 1 | 🟢 haiku | 18:54:17 | 18:54:21 | 0m03s | 0k | 0k | 39k | 69k | **108k** |
| ✅ scribe T0.01 (timings) | 🟢 haiku | 18:54:23 | 18:54:28 | 0m04s | 0k | 0k | 66k | 46k | **113k** |

### 4. ticket-run · 2026-11-27 19:07:48 to 19:09:23 · ⏱️ 1m35s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 19:07:48 | 19:08:23 | 0m34s | 4 |
| Waves | | | not run | 0 |
| Verify | 19:08:23 | 19:09:10 | 0m46s | 1 |
| Review | | | not run | 0 |
| Finish | 19:09:10 | 19:09:23 | 0m12s | 3 |

Tokens of this run: 0k · 9k · 395k · 645k · **1.05M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.01 | 🟢 haiku | 19:07:48 | 19:08:00 | 0m12s | 0k | 5k | 85k | 156k | **248k** |
| ✅ plan check T0.01 | 🟢 haiku | 19:08:00 | 19:08:04 | 0m03s | 0k | 0k | 37k | 34k | **72k** |
| ✅ start rule T0.01 | 🟢 haiku | 19:08:04 | 19:08:09 | 0m05s | 0k | 0k | 37k | 72k | **110k** |
| ✅ integrator prepare T0.01 | 🔵 sonnet | 19:08:10 | 19:08:23 | 0m12s | 0k | 0k | 40k | 76k | **117k** |
| ✅ verifier round 1 | 🟢 haiku | 19:08:23 | 19:09:10 | 0m46s | 0k | 0k | 77k | 72k | **150k** |
| ✅ scribe T0.01 | 🟢 haiku | 19:09:10 | 19:09:19 | 0m08s | 0k | 1k | 79k | 159k | **240k** |
| ✅ docs check T0.01 1 | 🟢 haiku | 19:09:19 | 19:09:23 | 0m04s | 0k | 0k | 37k | 72k | **110k** |
| 🔄 integrator finish T0.01 | 🔵 sonnet | 19:09:23 | 19:09:23 | 0m00s | 0k | 0k | 0k | 0k | **0k** |
<!-- /timings -->
