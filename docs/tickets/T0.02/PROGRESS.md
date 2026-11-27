# T0.02: Progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Repository layout](../../technical/architecture/repository-layout.md)
- [D407](../../specs/06-decisions/technical/d407-front-end.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:13 | Plan written: 13 tasks, 3 waves | ⏳ planner | ⏳ Awaiting approval |
| 2026-11-27 18:27 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 19:17 | Wave 1: 7 of 7 tasks done | workers | ✅ |
| 2026-11-27 19:17 | Integrate (Waves) | integrator | ✅ 7 integrated, 1 blocked, not committed |
| 2026-11-27 19:17 | Wave 2: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 19:17 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 19:17 | Wave 3: 4 of 4 tasks done | workers | ✅ |
| 2026-11-27 19:17 | Integrate (Waves) | integrator | ✅ 4 integrated, 0 blocked, not committed |
| 2026-11-27 19:17 | Verify 1 (2 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 19:17 | Stopped: checks failing: pytest in tests/ci/detect_changes/test_repository_layout.py, test_a_change_to_the_shared_front_end_packages_selects_every_front_end: the change matrix selects frontend/packages/config as a front end, expected only frontend/backoffice and frontend/mobile (1 failed, 1049 passed) | verifier | ❌ |
| 2026-11-27 19:17 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.02 continues it | run | ⚠️ |
| 2026-11-27 19:21 | Waits for T0.08: the failing test is T0.01's `tests/ci/detect_changes/test_repository_layout.py`, which hard-codes the front ends; T0.08's K11 owns its fix (plan change of 19:19), and T0.02 runs again once T0.08 is committed | coordinator | ⏸️ |
| 2026-11-27 19:44 | Verify 1 | verifier | ✅ passed |
| 2026-11-27 19:44 | Review 1 (full) | reviewer | ✅ 0 blocking, 4 follow-ups |
| 2026-11-27 19:44 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 19:46 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 19:46 | Verify 1 (2 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| `tests/conventions/scanner/test_new_packages.py`, `tests/conventions/scanner/test_plugin_and_sdk_imports.py`, `tests/conventions/scanner/test_shared_library_imports.py`, `tests/conventions/scanner/test_shared_models_imports.py` | The same `write()` helper and almost the same clean service tree are copied into four test files. Move them to one shared helpers module, for example `tests/conventions/scanner/helpers.py`, and import it by its full path. Add the missing module docstring to `test_shared_models_imports.py` so it matches the other three files. Owner: the test-writer task of the convention tests. |
| `frontend/packages/config/eslint.base.js` | The first entry, `{ files: [...] }`, holds nothing but a file pattern and repeats the pattern of the next entry. `globals.es2021` also sits beside `ecmaVersion` 2022. Remove the redundant entry and line up the globals with the ECMAScript version. Owner: the frontend config task. |
| `frontend/backoffice/package.json`, `frontend/mobile/package.json` | The existing back-office and mobile front ends do not yet depend on `@simpleerp/config` or extend it. When they get their first sources, add the workspace devDependency, an `eslint.config.js` and a `tsconfig.json` that extend the shared settings, as the package README describes. |
| `pnpm-lock.yaml` | The root lockfile is changed by this ticket, and another open ticket adds `frontend/packages/tokens` to the same pnpm workspace. The root lockfile belongs to no area, so the area lock does not keep the two tickets apart. Whichever ticket finishes second must regenerate the lockfile. Consider making the root lockfiles an area in the harness. |


<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.02` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 19:47:05 |
| ⏱️ **Overall ticket time** (first start to last activity) | **1h39m59s** |
| 🤖 Time with agents working (sum of runs) | 20m04s |
| ⏸️ Time between runs (approvals, fixes) | 1h19m55s |
| 🔁 Workflow runs | 4 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **17.72M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 108k | 970k | 3.94M | **5.02M** |
| 🔵 sonnet | 0k | 120k | 1.01M | 7.75M | **8.88M** |
| 🟣 opus | 0k | 93k | 267k | 3.46M | **3.82M** |
| **All models** | 0k | 321k | 2.25M | 15.16M | **17.72M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:14:03 · ⏱️ 6m57s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:41 | 0m35s | 2 |
| Check | 18:07:41 | 18:07:45 | 0m03s | 1 |
| Plan | 18:07:45 | 18:13:01 | 5m15s | 1 |
| Write | 18:13:01 | 18:14:03 | 1m01s | 2 |

Tokens of this run: 0k · 138k · 600k · 3.98M · **4.71M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.02 | 🟢 haiku | 18:07:05 | 18:07:12 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.02 | 🔵 sonnet | 18:07:12 | 18:07:41 | 0m28s | 0k | 11k | 150k | 711k | **873k** |
| ✅ check TICKET.md T0.02 | 🟢 haiku | 18:07:41 | 18:07:45 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.02 | 🟣 opus | 18:07:45 | 18:13:01 | 5m15s | 0k | 76k | 153k | 2.64M | **2.87M** |
| ✅ scribe T0.02 | 🟢 haiku | 18:13:01 | 18:13:59 | 0m58s | 0k | 48k | 154k | 469k | **672k** |
| ✅ check PLAN.md T0.02 | 🟢 haiku | 18:13:59 | 18:14:03 | 0m03s | 0k | 0k | 68k | 40k | **109k** |

### 2. ticket-run · 2026-11-27 19:10:06 to 19:17:27 · ⏱️ 7m20s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 19:10:06 | 19:10:47 | 0m40s | 4 |
| Waves | 19:10:51 | 19:16:14 | 5m23s | 16 |
| Verify | 19:16:14 | 19:17:15 | 1m00s | 1 |
| Review | | | not run | 0 |
| Finish | 19:17:15 | 19:17:27 | 0m11s | 1 |

Tokens of this run: 0k · 118k · 1.00M · 8.10M · **9.22M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.02 | 🟢 haiku | 19:10:06 | 19:10:18 | 0m12s | 0k | 7k | 47k | 234k | **289k** |
| ✅ plan check T0.02 | 🟢 haiku | 19:10:20 | 19:10:23 | 0m03s | 0k | 0k | 34k | 37k | **71k** |
| ✅ start rule T0.02 | 🟢 haiku | 19:10:24 | 19:10:29 | 0m04s | 0k | 0k | 34k | 37k | **71k** |
| ✅ integrator prepare T0.02 | 🔵 sonnet | 19:10:29 | 19:10:47 | 0m17s | 0k | 0k | 34k | 80k | **115k** |
| ✅ K01 test-writer | 🔵 sonnet | 19:10:51 | 19:11:36 | 0m45s | 0k | 7k | 48k | 435k | **491k** |
| ✅ K02 test-writer | 🔵 sonnet | 19:10:56 | 19:11:52 | 0m56s | 0k | 7k | 49k | 526k | **583k** |
| ✅ K03 test-writer | 🔵 sonnet | 19:11:00 | 19:12:01 | 1m00s | 0k | 10k | 46k | 481k | **538k** |
| ✅ K04 test-writer | 🔵 sonnet | 19:11:06 | 19:12:11 | 1m05s | 0k | 13k | 54k | 436k | **504k** |
| ✅ K05 test-writer | 🔵 sonnet | 19:11:13 | 19:11:55 | 0m41s | 0k | 4k | 51k | 262k | **317k** |
| ✅ K06 test-writer | 🔵 sonnet | 19:11:20 | 19:12:00 | 0m40s | 0k | 11k | 41k | 508k | **561k** |
| ✅ K07 test-writer | 🔵 sonnet | 19:11:27 | 19:12:07 | 0m40s | 0k | 7k | 43k | 375k | **427k** |
| ✅ integrator Waves | 🔵 sonnet | 19:12:16 | 19:12:42 | 0m26s | 0k | 1k | 42k | 198k | **241k** |
| ✅ K08 implementer | 🔵 sonnet | 19:12:45 | 19:13:24 | 0m39s | 0k | 6k | 69k | 637k | **713k** |
| ✅ K09 frontend-implementer | 🔵 sonnet | 19:12:47 | 19:13:56 | 1m09s | 0k | 7k | 49k | 913k | **970k** |
| ✅ integrator Waves | 🔵 sonnet | 19:14:05 | 19:14:18 | 0m13s | 0k | 1k | 42k | 199k | **243k** |
| ✅ K10 frontend-implementer | 🔵 sonnet | 19:14:20 | 19:15:39 | 1m18s | 0k | 6k | 44k | 652k | **703k** |
| ✅ K11 frontend-implementer | 🔵 sonnet | 19:14:23 | 19:15:03 | 0m40s | 0k | 3k | 42k | 518k | **565k** |
| ✅ K12 doc-writer | 🟢 haiku | 19:14:25 | 19:14:55 | 0m30s | 0k | 8k | 52k | 707k | **768k** |
| ✅ K13 doc-writer | 🟢 haiku | 19:14:27 | 19:14:58 | 0m30s | 0k | 6k | 40k | 248k | **295k** |
| ✅ integrator Waves | 🔵 sonnet | 19:15:54 | 19:16:14 | 0m20s | 0k | 1k | 43k | 206k | **250k** |
| ✅ verifier round 1 | 🟢 haiku | 19:16:14 | 19:17:15 | 1m00s | 0k | 1k | 42k | 150k | **194k** |
| ✅ scribe T0.02 | 🟢 haiku | 19:17:15 | 19:17:27 | 0m11s | 0k | 3k | 44k | 248k | **296k** |

### 3. ticket-run · 2026-11-27 19:41:09 to 19:45:11 · ⏱️ 4m01s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 19:41:09 | 19:41:44 | 0m35s | 4 |
| Waves | | | not run | 0 |
| Verify | 19:41:44 | 19:42:38 | 0m53s | 1 |
| Review | 19:42:39 | 19:44:04 | 1m25s | 1 |
| Finish | 19:44:04 | 19:45:11 | 1m06s | 4 |

Tokens of this run: 0k · 54k · 545k · 2.17M · **2.77M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.02 | 🟢 haiku | 19:41:09 | 19:41:20 | 0m10s | 0k | 5k | 76k | 169k | **251k** |
| ✅ plan check T0.02 | 🟢 haiku | 19:41:20 | 19:41:23 | 0m03s | 0k | 0k | 34k | 37k | **72k** |
| ✅ start rule T0.02 | 🟢 haiku | 19:41:24 | 19:41:30 | 0m05s | 0k | 0k | 34k | 37k | **72k** |
| ✅ integrator prepare T0.02 | 🔵 sonnet | 19:41:31 | 19:41:44 | 0m13s | 0k | 0k | 36k | 81k | **118k** |
| ✅ verifier round 1 | 🟢 haiku | 19:41:44 | 19:42:38 | 0m53s | 0k | 0k | 35k | 78k | **114k** |
| ✅ reviewer round 1 | 🟣 opus | 19:42:39 | 19:44:04 | 1m25s | 0k | 16k | 113k | 820k | **950k** |
| ✅ scribe T0.02 | 🟢 haiku | 19:44:04 | 19:44:28 | 0m23s | 0k | 14k | 61k | 419k | **495k** |
| ✅ explainer T0.02 | 🔵 sonnet | 19:44:04 | 19:45:00 | 0m55s | 0k | 16k | 82k | 409k | **507k** |
| ✅ docs check T0.02 1 | 🟢 haiku | 19:45:00 | 19:45:04 | 0m04s | 0k | 0k | 35k | 75k | **110k** |
| ✅ scribe T0.02 (timings) | 🟢 haiku | 19:45:07 | 19:45:11 | 0m04s | 0k | 0k | 35k | 42k | **77k** |

### 4. ticket-run · 2026-11-27 19:45:21 to 19:47:05 · ⏱️ 1m43s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 19:45:21 | 19:45:56 | 0m34s | 4 |
| Waves | | | not run | 0 |
| Verify | 19:45:56 | 19:46:51 | 0m54s | 1 |
| Review | | | not run | 0 |
| Finish | 19:46:51 | 19:47:05 | 0m13s | 3 |

Tokens of this run: 0k · 9k · 99k · 912k · **1.02M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.02 | 🟢 haiku | 19:45:21 | 19:45:33 | 0m11s | 0k | 5k | 14k | 230k | **250k** |
| ✅ plan check T0.02 | 🟢 haiku | 19:45:33 | 19:45:36 | 0m03s | 0k | 0k | 2k | 70k | **72k** |
| ✅ start rule T0.02 | 🟢 haiku | 19:45:36 | 19:45:42 | 0m05s | 0k | 0k | 0k | 110k | **110k** |
| ✅ integrator prepare T0.02 | 🔵 sonnet | 19:45:42 | 19:45:56 | 0m13s | 0k | 0k | 3k | 114k | **118k** |
| ✅ verifier round 1 | 🟢 haiku | 19:45:56 | 19:46:51 | 0m54s | 0k | 0k | 3k | 149k | **153k** |
| ✅ scribe T0.02 | 🟢 haiku | 19:46:51 | 19:46:58 | 0m07s | 0k | 1k | 43k | 122k | **167k** |
| ✅ docs check T0.02 1 | 🟢 haiku | 19:46:58 | 19:47:02 | 0m03s | 0k | 0k | 0k | 110k | **110k** |
| 🔄 integrator finish T0.02 | 🔵 sonnet | 19:47:03 | 19:47:05 | 0m02s | 0k | 0k | 32k | 4k | **37k** |
<!-- /timings -->
