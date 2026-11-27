# T0.05: Lifecycle and factories library, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Architecture](../../technical/architecture/architecture.md)
- [Back end](../../technical/architecture/backend.md)
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:13 | Plan written: 9 tasks, 4 waves | planner | ⏳ Awaiting approval |
| 2026-11-27 18:27 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 19:21 | Wave 1: 5 of 5 tasks done | workers | ✅ |
| 2026-11-27 19:21 | Integrate (Waves) | integrator | ✅ 5 integrated, 0 blocked, not committed |
| 2026-11-27 19:21 | Wave 2: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 19:21 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 19:21 | Wave 3: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 19:21 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 19:21 | Wave 4: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 19:21 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 19:21 | Verify 1 (3 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 19:21 | Integrate (Verify) | integrator | ✅ 1 integrated, 1 blocked, not committed |
| 2026-11-27 19:21 | Verify 2 (3 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 19:21 | Verify 3 (3 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 19:21 | Stopped: checks failing | verifier | ❌ mypy on backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py: "Source file found twice under different module names: backend.shared.lifecycle.src.erp_lifecycle.runnables.async_runnable and erp_lifecycle.runnables.async_runnable" (repeated in the output, detail truncated by checks.py, not an environment failure) |
| 2026-11-27 19:21 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.05 continues it | scribe | ⚠️ |
| 2026-11-27 19:33 | Waits for the harness fix #878: the checks ran mypy without MYPYPATH, so a library file was found under two module names; runs again once `feature/tickets` holds the fix | coordinator | ⏸️ |

| 2026-11-27 20:30 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-27 20:30 | Review 1 (full) | reviewer | ⚠️ 1 blocking, 7 follow-ups |
| 2026-11-27 20:30 | Integrate (Review) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 20:30 | Review 2 (confirm fixes) | reviewer | ⚠️ 1 blocking, 0 follow-ups |
| 2026-11-27 20:30 | Integrate (Review) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 20:30 | Review 3 (confirm fixes) | reviewer | ⚠️ 1 blocking, 1 follow-ups |
| 2026-11-27 20:30 | Stopped: blocking review findings left after the fix rounds; the person decides | scribe | ❌ uv.lock (owner K05): the erp-models hunk (around lines 84-93, `dependencies = [pydantic, pyyaml]` and its `requires-dist`) came back in round 3, taken from another ticket's uncommitted backend/models/pyproject.toml, which still says `dependencies = []` at HEAD. CI's `uv sync --locked --all-packages` would refuse the commit. Fix: restore the d4ee0b2 version of uv.lock (only T0.05's hunks), do not run uv in the shared checkout, then run `uv lock --check` and `uv sync --locked --all-packages` in the clean ticket tree and save the output in tests-evidences/ |
| 2026-11-27 20:30 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.05 continues it | scribe | ⚠️ |
| 2026-11-27 20:49 | Person's decision (P0 approval): `uv.lock` reset to T0.05's own hunks only (regenerated with `uv lock` on HEAD plus T0.05's files; `uv lock --check` passes); T0.03's erp-models hunk returns with T0.03 once T0.05 is committed. `reports/lifecycle.xml`, a JUnit report written by a test run, deleted | coordinator | 🟢 |
| 2026-11-27 20:54 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-27 20:54 | Review 1 (full) | reviewer | ✅ 0 blocking, 8 follow-ups |
| 2026-11-27 20:54 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 20:57 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 20:57 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| `reports/lifecycle.xml` | A local JUnit output of `.github/scripts/check_python_project.sh` got into the ticket's files at the repository root, and it holds the machine's hostname. Move it to `docs/tickets/T0.05/tests-evidences/` or drop it from the ticket, and consider adding `reports/` to `.gitignore`, because CI uploads it as an artifact. The test evidence is already in `docs/tickets/T0.05/tests-evidences/`. |
| `backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py` `backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py` | The two `execute()` methods log differently. `Runnable` logs `INFO Ran %s.` on success, while `AsyncRunnable` logs no INFO line and uses different messages (`Failed %s with %s.` against `Failed to execute %s: %s.`). Use the same INFO and ERROR messages in both. Also, a `close()` that raises in `finally` after a failed `initialize` or `run` replaces the original error: the `Runnable` docstring (`unchanged`) should say so, or close failures should be logged and the first error kept. |
| `backend/shared/lifecycle/tests/factories/test_runnable_factory.py` | `test_the_logger_defaults_to_a_logger_and_a_given_one_is_kept` asserts `RunnableFactory.__init__(...) is None` (line 360), which is always true. Replace it with an `isinstance(Logger)` check on a factory built without a logger, or split it into two tests like the runnable tests. |
| `backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py` `backend/shared/lifecycle/tests/factories/stand_in_runnable.py` | The import group comments are misplaced: `# First-party imports` sits above the `backend.shared...` import, while `erp_lifecycle` sits under the standard-library group. Remove the group comments, as for the other test files, or put them in the right place. |
| `backend/shared/lifecycle/tests/factories/test_runnable_factory.py` `backend/shared/lifecycle/tests/runnables/test_runnable.py` `backend/shared/lifecycle/tests/runnables/test_async_runnable.py` `backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py` | The helpers are imported as `backend.shared.lifecycle.tests...` from the repository root, while the `backend/models` package imports them as `tests....` with its own `pythonpath = ["."]`. The plan approved this choice. Align the shared packages on one style once both have landed. |
| `tests/conventions` | Acceptance criterion 4 is proven only by the factory's own tests. No convention test refuses a runnable constructor called in `src/` outside a `factories/` package. Add one when the first service lands (T0.14). |
| `docs/technical/architecture/backend.md` | The added T0.05 paragraph (line 10) is one line of about 380 characters. Wrap it like the surrounding text. |
| `pyproject.toml` `uv.lock` | The root project now depends on `erp-lifecycle` (`dependencies` plus a `[tool.uv.sources]` entry), while CI installs every member with `uv sync --locked --all-packages` and `erp-models` is not a root dependency. No agent reported it as a decision. Record why in `IMPLEMENTATION.md`, or drop it so the root stays a dependency-free virtual workspace. |
| `docs/tickets/T0.05/tests-evidences/` | The person's decision says `uv lock --check` passes on HEAD plus T0.05's files, but no evidence file holds that output. Save the output of `uv lock --check` and `uv sync --locked --all-packages` from the clean ticket tree in `tests-evidences/`. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.05` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 20:57:32 |
| ⏱️ **Overall ticket time** (first start to last activity) | **2h50m26s** |
| 🤖 Time with agents working (sum of runs) | 34m27s |
| ⏸️ Time between runs (approvals, fixes) | 2h15m59s |
| 🔁 Workflow runs | 5 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **22.44M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 114k | 1.44M | 4.18M | **5.73M** |
| 🔵 sonnet | 0k | 115k | 1.23M | 9.18M | **10.53M** |
| 🟣 opus | 0k | 131k | 578k | 5.47M | **6.18M** |
| **All models** | 0k | 361k | 3.25M | 18.83M | **22.44M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:14:18 · ⏱️ 7m12s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:43 | 0m37s | 2 |
| Check | 18:07:44 | 18:07:47 | 0m03s | 1 |
| Plan | 18:07:48 | 18:13:13 | 5m25s | 1 |
| Write | 18:13:13 | 18:14:18 | 1m04s | 2 |

Tokens of this run: 0k · 122k · 604k · 4.20M · **4.93M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.05 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.05 | 🔵 sonnet | 18:07:12 | 18:07:43 | 0m31s | 0k | 16k | 170k | 880k | **1.07M** |
| ✅ check TICKET.md T0.05 | 🟢 haiku | 18:07:44 | 18:07:47 | 0m03s | 0k | 0k | 37k | 73k | **112k** |
| ✅ planner T0.05 | 🟣 opus | 18:07:48 | 18:13:13 | 5m25s | 0k | 74k | 178k | 2.59M | **2.85M** |
| ✅ scribe T0.05 | 🟢 haiku | 18:13:13 | 18:14:14 | 1m01s | 0k | 30k | 144k | 539k | **715k** |
| ✅ check PLAN.md T0.05 | 🟢 haiku | 18:14:14 | 18:14:18 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-27 19:10:06 to 19:21:08 · ⏱️ 11m02s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 19:10:06 | 19:10:46 | 0m39s | 4 |
| Waves | 19:10:50 | 19:16:21 | 5m31s | 13 |
| Verify | 19:16:22 | 19:20:57 | 4m35s | 6 |
| Review | | | not run | 0 |
| Finish | 19:20:58 | 19:21:08 | 0m10s | 1 |

Tokens of this run: 0k · 78k · 997k · 6.58M · **7.65M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.05 | 🟢 haiku | 19:10:06 | 19:10:18 | 0m12s | 0k | 4k | 44k | 237k | **286k** |
| ✅ plan check T0.05 | 🟢 haiku | 19:10:18 | 19:10:22 | 0m03s | 0k | 0k | 34k | 37k | **71k** |
| ✅ start rule T0.05 | 🟢 haiku | 19:10:23 | 19:10:27 | 0m04s | 0k | 0k | 34k | 37k | **71k** |
| ✅ integrator prepare T0.05 | 🔵 sonnet | 19:10:28 | 19:10:46 | 0m18s | 0k | 0k | 34k | 80k | **115k** |
| ✅ K01 test-writer | 🔵 sonnet | 19:10:50 | 19:11:48 | 0m58s | 0k | 8k | 49k | 528k | **585k** |
| ✅ K02 test-writer | 🔵 sonnet | 19:10:56 | 19:11:52 | 0m56s | 0k | 11k | 48k | 384k | **444k** |
| ✅ K03 test-writer | 🔵 sonnet | 19:11:00 | 19:11:51 | 0m51s | 0k | 6k | 43k | 341k | **391k** |
| ✅ K04 test-writer | 🔵 sonnet | 19:11:06 | 19:11:57 | 0m51s | 0k | 1k | 42k | 218k | **262k** |
| ✅ K09 doc-writer | 🟢 haiku | 19:11:13 | 19:11:44 | 0m30s | 0k | 6k | 49k | 367k | **423k** |
| ✅ integrator Waves | 🔵 sonnet | 19:12:03 | 19:12:31 | 0m27s | 0k | 1k | 40k | 356k | **398k** |
| ✅ K05 implementer | 🔵 sonnet | 19:12:33 | 19:13:28 | 0m54s | 0k | 3k | 42k | 429k | **475k** |
| ✅ integrator Waves | 🔵 sonnet | 19:13:40 | 19:13:55 | 0m15s | 0k | 1k | 41k | 323k | **366k** |
| ✅ K06 implementer | 🔵 sonnet | 19:13:57 | 19:14:40 | 0m43s | 0k | 6k | 44k | 484k | **535k** |
| ✅ K07 implementer | 🔵 sonnet | 19:13:59 | 19:14:32 | 0m32s | 0k | 2k | 40k | 301k | **345k** |
| ✅ integrator Waves | 🔵 sonnet | 19:14:46 | 19:15:04 | 0m17s | 0k | 1k | 39k | 199k | **240k** |
| ✅ K08 implementer | 🔵 sonnet | 19:15:07 | 19:15:51 | 0m43s | 0k | 3k | 40k | 260k | **304k** |
| ✅ integrator Waves | 🔵 sonnet | 19:16:01 | 19:16:21 | 0m20s | 0k | 1k | 41k | 408k | **450k** |
| ✅ verifier round 1 | 🟢 haiku | 19:16:22 | 19:17:14 | 0m51s | 0k | 1k | 39k | 76k | **116k** |
| ✅ K07 implementer (fix) | 🔵 sonnet | 19:17:15 | 19:18:15 | 0m59s | 0k | 2k | 39k | 257k | **300k** |
| ✅ integrator Verify | 🔵 sonnet | 19:18:15 | 19:18:37 | 0m21s | 0k | 2k | 43k | 416k | **462k** |
| ✅ verifier round 2 | 🟢 haiku | 19:18:37 | 19:19:32 | 0m55s | 0k | 1k | 37k | 117k | **156k** |
| ❌ K07 implementer (fix) | 🔵 sonnet | 19:19:35 | 19:20:05 | 0m30s | 0k | 3k | 44k | 387k | **435k** |
| ✅ verifier round 3 | 🟢 haiku | 19:20:06 | 19:20:57 | 0m51s | 0k | 1k | 37k | 117k | **156k** |
| ✅ scribe T0.05 | 🟢 haiku | 19:20:58 | 19:21:08 | 0m10s | 0k | 3k | 43k | 207k | **254k** |

### 3. ticket-run · 2026-11-27 20:20:27 to 20:30:44 · ⏱️ 10m17s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 20:20:27 | 20:21:11 | 0m44s | 4 |
| Waves | | | not run | 0 |
| Verify | 20:21:12 | 20:22:01 | 0m49s | 1 |
| Review | 20:22:04 | 20:30:19 | 8m15s | 9 |
| Finish | 20:30:20 | 20:30:44 | 0m24s | 1 |

Tokens of this run: 0k · 85k · 702k · 5.20M · **5.99M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.05 | 🟢 haiku | 20:20:27 | 20:20:41 | 0m13s | 0k | 6k | 47k | 236k | **290k** |
| ✅ plan check T0.05 | 🟢 haiku | 20:20:43 | 20:20:46 | 0m03s | 0k | 0k | 34k | 37k | **72k** |
| ✅ start rule T0.05 | 🟢 haiku | 20:20:47 | 20:20:55 | 0m08s | 0k | 0k | 34k | 74k | **109k** |
| ✅ integrator prepare T0.05 | 🔵 sonnet | 20:20:57 | 20:21:11 | 0m14s | 0k | 0k | 35k | 81k | **117k** |
| ✅ verifier round 1 | 🟢 haiku | 20:21:12 | 20:22:01 | 0m49s | 0k | 0k | 37k | 75k | **113k** |
| ✅ reviewer round 1 | 🟣 opus | 20:22:04 | 20:24:28 | 2m24s | 0k | 27k | 147k | 1.28M | **1.46M** |
| ✅ K05 implementer (fix) | 🔵 sonnet | 20:24:30 | 20:25:35 | 1m05s | 0k | 6k | 52k | 616k | **674k** |
| ✅ integrator Review | 🔵 sonnet | 20:25:36 | 20:25:53 | 0m16s | 0k | 1k | 43k | 416k | **461k** |
| ✅ verifier after review 1 | 🟢 haiku | 20:25:53 | 20:26:40 | 0m47s | 0k | 0k | 0k | 113k | **113k** |
| ✅ reviewer round 2 | 🟣 opus | 20:26:41 | 20:27:11 | 0m29s | 0k | 4k | 49k | 249k | **304k** |
| ✅ K05 implementer (fix) | 🔵 sonnet | 20:27:12 | 20:28:35 | 1m23s | 0k | 8k | 51k | 890k | **949k** |
| ✅ integrator Review | 🔵 sonnet | 20:28:36 | 20:28:50 | 0m14s | 0k | 1k | 10k | 403k | **416k** |
| ✅ verifier after review 2 | 🟢 haiku | 20:28:51 | 20:29:37 | 0m46s | 0k | 0k | 0k | 113k | **113k** |
| ✅ reviewer round 3 | 🟣 opus | 20:29:38 | 20:30:19 | 0m41s | 0k | 6k | 52k | 393k | **452k** |
| ✅ scribe T0.05 | 🟢 haiku | 20:30:20 | 20:30:44 | 0m24s | 0k | 21k | 105k | 216k | **343k** |

### 4. ticket-run · 2026-11-27 20:51:28 to 20:55:43 · ⏱️ 4m15s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 20:51:28 | 20:52:04 | 0m35s | 4 |
| Waves | | | not run | 0 |
| Verify | 20:52:04 | 20:52:53 | 0m48s | 1 |
| Review | 20:52:54 | 20:54:33 | 1m39s | 1 |
| Finish | 20:54:33 | 20:55:43 | 1m10s | 4 |

Tokens of this run: 0k · 64k · 634k · 2.11M · **2.81M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.05 | 🟢 haiku | 20:51:28 | 20:51:38 | 0m09s | 0k | 2k | 47k | 116k | **166k** |
| ✅ plan check T0.05 | 🟢 haiku | 20:51:38 | 20:51:41 | 0m03s | 0k | 0k | 37k | 34k | **72k** |
| ✅ start rule T0.05 | 🟢 haiku | 20:51:41 | 20:51:49 | 0m07s | 0k | 0k | 34k | 74k | **109k** |
| ✅ integrator prepare T0.05 | 🔵 sonnet | 20:51:51 | 20:52:04 | 0m12s | 0k | 0k | 40k | 76k | **117k** |
| ✅ verifier round 1 | 🟢 haiku | 20:52:04 | 20:52:53 | 0m48s | 0k | 0k | 39k | 112k | **152k** |
| ✅ reviewer round 1 | 🟣 opus | 20:52:54 | 20:54:33 | 1m39s | 0k | 19k | 150k | 953k | **1.12M** |
| ✅ scribe T0.05 | 🟢 haiku | 20:54:33 | 20:55:01 | 0m28s | 0k | 19k | 126k | 240k | **386k** |
| ✅ explainer T0.05 | 🔵 sonnet | 20:54:33 | 20:55:35 | 1m01s | 0k | 20k | 84k | 351k | **455k** |
| ✅ docs check T0.05 1 | 🟢 haiku | 20:55:35 | 20:55:39 | 0m04s | 0k | 0k | 37k | 72k | **109k** |
| ✅ scribe T0.05 (timings) | 🟢 haiku | 20:55:39 | 20:55:43 | 0m04s | 0k | 0k | 37k | 78k | **117k** |

### 5. ticket-run · 2026-11-27 20:55:52 to 20:57:32 · ⏱️ 1m39s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 20:55:52 | 20:56:29 | 0m36s | 4 |
| Waves | | | not run | 0 |
| Verify | 20:56:29 | 20:57:15 | 0m46s | 1 |
| Review | | | not run | 0 |
| Finish | 20:57:16 | 20:57:32 | 0m16s | 3 |

Tokens of this run: 0k · 9k · 309k · 739k · **1.06M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.05 | 🟢 haiku | 20:55:52 | 20:56:02 | 0m10s | 0k | 4k | 45k | 196k | **246k** |
| ✅ plan check T0.05 | 🟢 haiku | 20:56:02 | 20:56:07 | 0m04s | 0k | 0k | 36k | 72k | **109k** |
| ✅ start rule T0.05 | 🟢 haiku | 20:56:07 | 20:56:14 | 0m07s | 0k | 0k | 34k | 37k | **72k** |
| ✅ integrator prepare T0.05 | 🔵 sonnet | 20:56:16 | 20:56:29 | 0m13s | 0k | 0k | 35k | 81k | **117k** |
| ✅ verifier round 1 | 🟢 haiku | 20:56:29 | 20:57:15 | 0m46s | 0k | 0k | 37k | 75k | **113k** |
| ✅ scribe T0.05 | 🟢 haiku | 20:57:16 | 20:57:24 | 0m08s | 0k | 3k | 50k | 200k | **253k** |
| ✅ docs check T0.05 1 | 🟢 haiku | 20:57:24 | 20:57:28 | 0m04s | 0k | 0k | 37k | 72k | **109k** |
| 🔄 integrator finish T0.05 | 🔵 sonnet | 20:57:29 | 20:57:32 | 0m03s | 0k | 0k | 32k | 4k | **37k** |
<!-- /timings -->
