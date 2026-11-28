# T0.11: Metering client, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Architecture, Metering (TC-21)](../../technical/architecture/architecture.md)
- [BR-F22-06](../../specs/02-functional/f22-unified-cost-management/business-rules/br-f22-06-stop-at-budget-legal-duties-kept.md)
- [📜 D398: Budgets warn, then stop](../../specs/06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md)
- [📜 D405: Architecture and scalability](../../specs/06-decisions/technical/d405-architecture-and-scalability.md)
- [🧗 TC-21: Metering every paid call, and stopping on a budget](../../specs/03-technical/challenges/tc-21-metering-every-paid-call.md)
- [🏗️ Back end](../../technical/architecture/backend.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:15 | Plan written: 16 tasks, 5 waves | ⏳ | Awaiting approval |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-28 00:50 | Verify 1 (3 not applicable) | verifier | ❌ 5 failures |
| 2026-11-28 00:50 | Integrate (Verify) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-28 00:50 | Verify 2 (3 not applicable) | verifier | ❌ 1 failures |
| 2026-11-28 00:50 | Stopped: checks failing: pytest tests, tests/harness/checks/test_checks_cleanup.py::TestChecksCleanup::test_pytest_keeps_its_temporary_files_beside_the_clean_tree failed at line 140: assert "--basetemp" not in call(...checks.pytest_command('tests', ROOT)). The command was ['uv', 'run', '--all-packages', 'pytest', 'tests', '-q', ...] with a --basetemp argument in it. Summary: 1 failed, 1327 passed, 3 skipped. Not environment. | ❌ | Stopped |
| 2026-11-28 00:50 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.11 continues it | ⚠️ | Uncommitted |
| 2026-11-28 00:56 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-28 00:56 | Review 1 (full) | reviewer | ✅ 0 blocking, 8 follow-ups |
| 2026-11-28 00:56 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | 👀 | Awaiting code review |
| 2026-11-28 01:00 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-28 01:00 | Verify 1 (3 not applicable) | verifier | ✅ passed |


## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| backend/shared/metering/src/erp_metering/service/metering/metering_client.py backend/shared/metering/tests/service/metering/metering_client/test_failed_call.py | In MeteringClient.call, the reservation is released only on `except Exception`. A cancelled task (asyncio.CancelledError, a BaseException) leaves its reservation held on the server. Release it on cancellation too, for example `except BaseException` around the work with a re-raise, and add a test that cancels the work. Owner K16 (test K08). |
| backend/shared/metering/src/erp_metering/storage/events/usage_event_writer.py | UsageEventWriter.write is async but does its sqlite connect, insert and commit synchronously, so it blocks the event loop on every paid call. Run _store in a thread (asyncio.to_thread), or take the caller's connection so the event joins the caller's own transaction, which is the outbox pattern of D405. The parameter is also typed as OutboxStore[sqlite3.Connection], which ties the library to SQLite. No NFR measure covers metering, so this does not block. Owner K15. |
| backend/shared/metering/src/erp_metering/service/metering/metering_client.py backend/shared/metering/README.md | When the usage event cannot be written after the work succeeded and was settled, call() raises SEMeteringUsageEventNotWrittenError and the work's result is lost. A caller that retries pays twice. Decide and document whether the result should be returned with an ERROR log instead, or keep the raise and state the retry hazard in the README. Owner K16, README K12. |
| backend/shared/metering/src/erp_metering/models/calls/settlement.py | The Notes of Settlement say a failed call is settled with a zero cost. The client actually releases it with DELETE /v1/reservations/{id}. Fix the Notes to match. Owner K10. |
| backend/shared/metering/src/erp_metering/models/calls/paid_call.py backend/shared/metering/src/erp_metering/models/calls/budget_check.py backend/shared/metering/src/erp_metering/models/calls/reservation.py backend/shared/metering/src/erp_metering/models/calls/settlement.py backend/shared/metering/src/erp_metering/models/events/usage_event.py backend/shared/metering/src/erp_metering/storage/events/usage_event_writer.py backend/shared/metering/src/erp_metering/storage/servers/metering_server_repository.py | The import group comments are mislabelled. In the models files, erp_models sits under 'First-party imports' above a 'Third-party imports' group that also holds erp_metering. In storage, erp_models and erp_outbox sit under 'Third-party imports'. Relabel the groups to match how ruff's isort orders them, in the order standard library, third-party, first-party. Owners K10, K13, K14, K15. |
| backend/shared/metering/tests/conftest.py | The outbox_events fixture returns a nested tuple-indexing lambda (`(lambda events: (connection.rollback(), events)[1])(...)`). Replace it with a small helper class or a plain function in a helpers.py. Owner K04. |
| backend/shared/metering/tests/stand_in/stand_in_metering_server.py backend/shared/metering/tests/stand_in/stand_in_metering_handler.py | The stand-in metering server is local to this package's tests, which is acceptable. Once T0.13 delivers the shared stand-in server kit, move it onto that kit. Owner K04. |
| backend/shared/metering/src/erp_metering/models/calls/paid_call.py | Any caller can set legal_duty=True and pass an exhausted budget. The ticket only carries the flag, so this is in scope. A later ticket should check the flag against the country pack's list of legal duties, so the bypass cannot be claimed freely. Owner K10. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.11` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-28 01:00:38 |
| ⏱️ **Overall ticket time** (first start to last activity) | **6h53m32s** |
| 🤖 Time with agents working (sum of runs) | 38m45s |
| ⏸️ Time between runs (approvals, fixes) | 6h14m46s |
| 🔁 Workflow runs | 5 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **37.45M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 152k | 1.42M | 4.30M | **5.88M** |
| 🔵 sonnet | 0k | 384k | 2.28M | 24.41M | **27.07M** |
| 🟣 opus | 0k | 123k | 378k | 3.99M | **4.50M** |
| **All models** | 1k | 660k | 4.08M | 32.70M | **37.45M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:16:59 · ⏱️ 9m53s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:07:53 | 0m47s | 2 |
| Check | 18:07:53 | 18:08:10 | 0m16s | 3 |
| Plan | 18:08:10 | 18:15:40 | 7m29s | 1 |
| Write | 18:15:40 | 18:16:59 | 1m18s | 2 |

Tokens of this run: 0k · 192k · 683k · 4.94M · **5.81M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.11 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m05s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.11 | 🔵 sonnet | 18:07:12 | 18:07:53 | 0m40s | 0k | 21k | 171k | 1.43M | **1.62M** |
| ✅ check TICKET.md T0.11 | 🟢 haiku | 18:07:53 | 18:07:57 | 0m03s | 0k | 0k | 35k | 38k | **74k** |
| ✅ ticket-writer fix T0.11 | 🔵 sonnet | 18:07:57 | 18:08:06 | 0m08s | 0k | 2k | 46k | 162k | **211k** |
| ✅ check TICKET.md T0.11 | 🟢 haiku | 18:08:06 | 18:08:10 | 0m03s | 0k | 0k | 2k | 71k | **73k** |
| ✅ planner T0.11 | 🟣 opus | 18:08:10 | 18:15:40 | 7m29s | 0k | 103k | 213k | 2.68M | **3.00M** |
| ✅ scribe T0.11 | 🟢 haiku | 18:15:40 | 18:16:54 | 1m14s | 0k | 64k | 138k | 407k | **610k** |
| ✅ check PLAN.md T0.11 | 🟢 haiku | 18:16:55 | 18:16:59 | 0m04s | 0k | 0k | 37k | 73k | **112k** |

### 2. ticket-run · 2026-11-28 00:27:42 to 00:44:21 · ⏱️ 16m39s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:27:42 | 00:28:31 | 0m48s | 4 |
| Waves | 00:28:32 | 00:43:01 | 14m29s | 24 |
| Verify | 00:43:01 | 00:44:21 | 1m19s | 2 |
| Review | | | not run | 0 |
| Finish | | | not run | 0 |

Tokens of this run: 0k · 366k · 1.98M · 22.40M · **24.75M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.11 | 🟢 haiku | 00:27:42 | 00:28:00 | 0m18s | 0k | 10k | 119k | 181k | **310k** |
| ✅ plan check T0.11 | 🟢 haiku | 00:28:01 | 00:28:05 | 0m04s | 0k | 0k | 39k | 77k | **118k** |
| ✅ start rule T0.11 | 🟢 haiku | 00:28:05 | 00:28:16 | 0m10s | 0k | 0k | 39k | 77k | **117k** |
| ✅ integrator prepare T0.11 | 🔵 sonnet | 00:28:16 | 00:28:31 | 0m14s | 0k | 0k | 37k | 86k | **124k** |
| ✅ K01 test-writer | 🔵 sonnet | 00:28:32 | 00:30:18 | 1m46s | 0k | 14k | 61k | 842k | **918k** |
| ✅ K02 test-writer | 🔵 sonnet | 00:28:34 | 00:29:45 | 1m11s | 0k | 23k | 68k | 1.05M | **1.14M** |
| ✅ K03 test-writer | 🔵 sonnet | 00:28:35 | 00:30:21 | 1m45s | 0k | 18k | 77k | 870k | **966k** |
| ✅ K04 test-writer | 🔵 sonnet | 00:28:37 | 00:30:41 | 2m03s | 0k | 34k | 94k | 1.57M | **1.70M** |
| ✅ K05 test-writer | 🔵 sonnet | 00:28:40 | 00:30:00 | 1m19s | 0k | 22k | 75k | 1.18M | **1.28M** |
| ✅ K06 test-writer | 🔵 sonnet | 00:28:43 | 00:30:09 | 1m26s | 0k | 10k | 80k | 1.09M | **1.18M** |
| ✅ K07 test-writer | 🔵 sonnet | 00:28:45 | 00:29:46 | 1m00s | 0k | 11k | 74k | 906k | **993k** |
| ✅ K08 test-writer | 🔵 sonnet | 00:28:47 | 00:30:49 | 2m01s | 0k | 25k | 77k | 1.04M | **1.14M** |
| ✅ integrator Waves | 🔵 sonnet | 00:30:49 | 00:31:09 | 0m19s | 0k | 1k | 44k | 301k | **347k** |
| ❌ K09 implementer | 🔵 sonnet | 00:31:11 | 00:31:56 | 0m44s | 0k | 5k | 50k | 695k | **752k** |
| ✅ K10 implementer | 🔵 sonnet | 00:31:12 | 00:34:31 | 3m18s | 0k | 61k | 148k | 3.68M | **3.89M** |
| ✅ K11 implementer | 🔵 sonnet | 00:31:14 | 00:31:55 | 0m41s | 0k | 15k | 52k | 812k | **880k** |
| ✅ K12 doc-writer | 🟢 haiku | 00:31:15 | 00:32:18 | 1m02s | 0k | 15k | 84k | 864k | **963k** |
| ✅ K08 test-writer (fix) | 🔵 sonnet | 00:34:33 | 00:35:11 | 0m37s | 0k | 1k | 51k | 229k | **282k** |
| ✅ integrator Waves | 🔵 sonnet | 00:35:20 | 00:35:33 | 0m12s | 0k | 1k | 42k | 302k | **347k** |
| ✅ K09 implementer | 🔵 sonnet | 00:35:34 | 00:36:32 | 0m57s | 0k | 4k | 46k | 461k | **511k** |
| ✅ integrator Waves | 🔵 sonnet | 00:36:35 | 00:36:50 | 0m15s | 0k | 1k | 41k | 254k | **298k** |
| ✅ K13 implementer | 🔵 sonnet | 00:36:52 | 00:38:38 | 1m46s | 0k | 26k | 93k | 1.26M | **1.38M** |
| ✅ K14 implementer | 🔵 sonnet | 00:36:53 | 00:38:34 | 1m40s | 0k | 24k | 64k | 1.04M | **1.13M** |
| ✅ integrator Waves | 🔵 sonnet | 00:38:50 | 00:39:02 | 0m11s | 0k | 0k | 52k | 216k | **269k** |
| ✅ K15 implementer | 🔵 sonnet | 00:39:03 | 00:40:10 | 1m07s | 0k | 7k | 75k | 632k | **715k** |
| ✅ integrator Waves | 🔵 sonnet | 00:40:21 | 00:40:33 | 0m11s | 0k | 1k | 54k | 256k | **312k** |
| ✅ K16 implementer | 🔵 sonnet | 00:40:34 | 00:42:51 | 2m16s | 0k | 15k | 82k | 1.48M | **1.58M** |
| ✅ integrator Waves | 🔵 sonnet | 00:42:52 | 00:43:01 | 0m08s | 0k | 0k | 42k | 126k | **168k** |
| ✅ verifier round 1 | 🟢 haiku | 00:43:01 | 00:43:21 | 0m19s | 0k | 3k | 52k | 124k | **180k** |
| 🔄 FIX-K01+K02+K03+K04+K05+K06+K07+K08 test-writer (fix) | 🔵 sonnet | 00:43:22 | 00:44:21 | 0m59s | 0k | 5k | 57k | 685k | **747k** |

### 3. ticket-run · 2026-11-28 00:46:08 to 00:50:54 · ⏱️ 4m45s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:46:08 | 00:46:50 | 0m42s | 4 |
| Waves | | | not run | 0 |
| Verify | 00:46:51 | 00:50:43 | 3m52s | 5 |
| Review | | | not run | 0 |
| Finish | 00:50:43 | 00:50:54 | 0m10s | 1 |

Tokens of this run: 0k · 19k · 425k · 1.65M · **2.09M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.11 | 🟢 haiku | 00:46:08 | 00:46:21 | 0m12s | 0k | 6k | 83k | 134k | **224k** |
| ✅ plan check T0.11 | 🟢 haiku | 00:46:21 | 00:46:24 | 0m03s | 0k | 0k | 36k | 39k | **76k** |
| ✅ start rule T0.11 | 🟢 haiku | 00:46:24 | 00:46:37 | 0m12s | 0k | 0k | 39k | 76k | **116k** |
| ✅ integrator prepare T0.11 | 🔵 sonnet | 00:46:37 | 00:46:50 | 0m13s | 0k | 0k | 39k | 87k | **128k** |
| ✅ verifier round 1 | 🟢 haiku | 00:46:51 | 00:48:12 | 1m21s | 0k | 2k | 44k | 122k | **169k** |
| ✅ K08 test-writer (fix) | 🔵 sonnet | 00:48:14 | 00:48:41 | 0m27s | 0k | 2k | 48k | 369k | **419k** |
| ✅ K07 test-writer (fix) | 🔵 sonnet | 00:48:15 | 00:48:59 | 0m43s | 0k | 2k | 44k | 271k | **318k** |
| ✅ integrator Verify | 🔵 sonnet | 00:49:07 | 00:49:18 | 0m10s | 0k | 0k | 43k | 168k | **212k** |
| ✅ verifier round 2 | 🟢 haiku | 00:49:18 | 00:50:43 | 1m25s | 0k | 1k | 1k | 159k | **162k** |
| ✅ scribe T0.11 | 🟢 haiku | 00:50:43 | 00:50:54 | 0m10s | 0k | 2k | 44k | 214k | **261k** |

### 4. ticket-run · 2026-11-28 00:53:04 to 00:58:02 · ⏱️ 4m57s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:53:04 | 00:53:48 | 0m44s | 4 |
| Waves | | | not run | 0 |
| Verify | 00:53:49 | 00:55:10 | 1m21s | 1 |
| Review | 00:55:10 | 00:56:48 | 1m37s | 1 |
| Finish | 00:56:49 | 00:58:02 | 1m12s | 4 |

Tokens of this run: 0k · 71k · 642k · 2.96M · **3.67M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.11 | 🟢 haiku | 00:53:04 | 00:53:17 | 0m12s | 0k | 6k | 54k | 207k | **269k** |
| ✅ plan check T0.11 | 🟢 haiku | 00:53:17 | 00:53:21 | 0m04s | 0k | 0k | 37k | 79k | **116k** |
| ✅ start rule T0.11 | 🟢 haiku | 00:53:23 | 00:53:34 | 0m11s | 0k | 0k | 39k | 76k | **116k** |
| ✅ integrator prepare T0.11 | 🔵 sonnet | 00:53:35 | 00:53:48 | 0m13s | 0k | 0k | 40k | 87k | **128k** |
| ✅ verifier round 1 | 🟢 haiku | 00:53:49 | 00:55:10 | 1m21s | 0k | 0k | 39k | 80k | **120k** |
| ✅ reviewer round 1 | 🟣 opus | 00:55:10 | 00:56:48 | 1m37s | 0k | 20k | 164k | 1.31M | **1.50M** |
| ✅ scribe T0.11 | 🟢 haiku | 00:56:49 | 00:57:15 | 0m26s | 0k | 22k | 70k | 326k | **419k** |
| ✅ explainer T0.11 | 🔵 sonnet | 00:56:49 | 00:57:54 | 1m04s | 0k | 19k | 121k | 662k | **803k** |
| ✅ docs check T0.11 1 | 🟢 haiku | 00:57:54 | 00:57:58 | 0m04s | 0k | 0k | 39k | 76k | **116k** |
| ✅ scribe T0.11 (timings) | 🟢 haiku | 00:57:58 | 00:58:02 | 0m03s | 0k | 0k | 37k | 44k | **81k** |

### 5. ticket-run · 2026-11-28 00:58:08 to 01:00:38 · ⏱️ 2m29s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 00:58:08 | 00:58:54 | 0m45s | 4 |
| Waves | | | not run | 0 |
| Verify | 00:58:54 | 01:00:20 | 1m26s | 1 |
| Review | | | not run | 0 |
| Finish | 01:00:21 | 01:00:38 | 0m17s | 3 |

Tokens of this run: 0k · 11k · 344k · 762k · **1.12M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.11 | 🟢 haiku | 00:58:08 | 00:58:22 | 0m13s | 0k | 6k | 51k | 177k | **235k** |
| ✅ plan check T0.11 | 🟢 haiku | 00:58:22 | 00:58:26 | 0m03s | 0k | 0k | 39k | 76k | **116k** |
| ✅ start rule T0.11 | 🟢 haiku | 00:58:26 | 00:58:38 | 0m12s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.11 | 🔵 sonnet | 00:58:39 | 00:58:54 | 0m14s | 0k | 0k | 40k | 87k | **128k** |
| ✅ verifier round 1 | 🟢 haiku | 00:58:54 | 01:00:20 | 1m26s | 0k | 0k | 37k | 123k | **161k** |
| ✅ scribe T0.11 | 🟢 haiku | 01:00:21 | 01:00:29 | 0m08s | 0k | 2k | 68k | 173k | **244k** |
| ✅ docs check T0.11 1 | 🟢 haiku | 01:00:29 | 01:00:34 | 0m04s | 0k | 0k | 37k | 79k | **116k** |
| 🔄 integrator finish T0.11 | 🔵 sonnet | 01:00:35 | 01:00:38 | 0m02s | 0k | 0k | 34k | 4k | **39k** |
<!-- /timings -->
