# T0.10: Event outbox library, progress

**Status:** 🟡 Planned

<!-- ticket:specs -->
## 📚 Specifications

The specification and design pages of [TICKET.md](TICKET.md), copied by `python3 .claude/scripts/tickets/ticket_refs.py sync`.

- [Architecture](../../technical/architecture/architecture.md)
- [Repository layout](../../technical/architecture/repository-layout.md)
- [I-T03-01](../../specs/03-technical/t03-audit-trail/interfaces/i-t03-01-audit-writer.md)
- [📜 D405 Architecture and scalability](../../specs/06-decisions/technical/d405-architecture-and-scalability.md)
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md)
- [Back end](../../technical/architecture/backend.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md)
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md)
<!-- /ticket:specs -->

## 📝 Events

| Time | Event | By | Result |
| --- | --- | --- | --- |
| 2026-11-27 18:14 | Plan written: 13 tasks, 5 waves | ticket-plan | ⏳ Awaiting approval |
| 2026-11-27 18:28 | Plan approved by the person (group approval) | 👤 person | 🟢 Approved |
| 2026-11-27 21:41 | Wave 1: 6 of 6 tasks done | workers | ✅ |
| 2026-11-27 21:41 | Integrate (Waves) | integrator | ✅ 6 integrated, 0 blocked, not committed |
| 2026-11-27 21:41 | Wave 2: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 21:41 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 21:41 | Wave 3: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 21:41 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 21:41 | Wave 4: 1 blocking file(s) sent to their owners: backend/shared/outbox/tests/service/relay/test_outbox_relay.py | workers | 🔁 |
| 2026-11-27 21:41 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 21:41 | Wave 4: 1 of 1 tasks done | workers | ✅ |
| 2026-11-27 21:41 | Integrate (Waves) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 21:41 | Wave 5: 2 of 2 tasks done | workers | ✅ |
| 2026-11-27 21:41 | Integrate (Waves) | integrator | ✅ 2 integrated, 0 blocked, not committed |
| 2026-11-27 21:41 | Verify 1 (3 not applicable) | verifier | ❌ 1 failures |
| 2026-11-27 21:41 | Stopped: checks failing | verifier | ❌ pytest in tests (environment: false): 2 failed, 1172 passed. FAILED tests/ci/detect_changes/test_repository_layout.py::TestRepositoryLayout::test_the_front_end_apps_are_listed_as_typescript_projects and ::test_a_change_to_the_shared_front_end_packages_selects_every_front_end. AssertionError: images {'folder': 'frontend/backoffice', 'name': 'backoffice'} listed where [] expected |
| 2026-11-27 21:41 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.10 continues it | scribe | ⚠️ |
| 2026-11-27 22:14 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-27 22:14 | Review 1 (full) | reviewer | ⚠️ 1 blocking, 6 follow-ups |
| 2026-11-27 22:14 | Integrate (Review) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 22:14 | Review 2 (confirm fixes) | reviewer | ⚠️ 1 blocking, 0 follow-ups |
| 2026-11-27 22:14 | Integrate (Review) | integrator | ✅ 1 integrated, 0 blocked, not committed |
| 2026-11-27 22:14 | Review 3 (confirm fixes) | reviewer | ⚠️ 1 blocking, 1 follow-ups |
| 2026-11-27 22:14 | Stopped: blocking review findings left after the fix rounds; the person decides. uv.lock: the round-1 blocking finding is still open, it was fixed and then undone. The fix diff since 8f24384ff puts back erp-context and erp-country-rules in `[manifest] members`, with their package entries and those of annotated-doc, anyio, certifi, fastapi, h11, httpcore, httpx, idna, opentelemetry-api and starlette. The likely cause is another running ticket (T0.09 company context, T0.12 country-pack rules) that ran `uv lock` in the main checkout. `ticket_tree.py finish` would commit that lock, and CI's `uv sync --locked --all-packages` (.github/workflows/python.yml:48, 81, 109) would refuse it, as the folders backend/shared/context and backend/shared/country-rules are not in the commit. Fix: just before finish, set uv.lock to develop's lock plus erp-outbox only, check it in the clean tree with `uv lock --check` or `uv sync --locked --all-packages`, then hand off that version. Coordinate with T0.09 and T0.12 so they do not rewrite it before T0.10 commits. Owner: K08. | reviewer | ❌ |
| 2026-11-27 22:14 | Work left uncommitted in /home/guillaume/Documents/Projects/Others/simple-erp on feature/tickets; /ticket-run T0.10 continues it | scribe | ⚠️ |
| 2026-11-27 22:17 | Lock fix by the coordinator: uv.lock set to develop's lock plus erp-outbox only (uv lock in a clean tree of 972c4aaa6); T0.09's and T0.12's libraries parked in .git/erp/parked/ until T0.10 is committed, so that no uv run in the main checkout re-adds them. T0.09 and T0.12 re-lock on top of it afterwards | 👤 person (P0 standing order) | 🟢 Approved |
| 2026-11-27 22:19 | Verify 1 (3 not applicable) | verifier | ✅ passed |
| 2026-11-27 22:19 | Review 1 (full) | reviewer | ✅ 0 blocking, 7 follow-ups |
| 2026-11-27 22:19 | Waiting for the person's code review: nothing is committed or pushed until PLAN.md says **Push:** 🟢 Approved (TKT-18) | scribe | 👀 |
| 2026-11-27 22:22 | Push approved after the code review | 👤 person | 🟢 |
| 2026-11-27 22:22 | Verify 1 (3 not applicable) | verifier | ✅ passed |

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| `backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py` | OutboxRelay is a sync Runnable that makes one pass. A service that runs it from its FastAPI lifespan will block the event loop during the SQLite reads and the publish calls. Either provide an AsyncRunnable relay, or a documented async wrapper the services' lifespan can use, when the first service adopts the outbox. Owner: K11. |
| `backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py`, `backend/shared/outbox/src/erp_outbox/service/factories/relay_factory.py` | OutboxStore is generic over its connection, but OutboxRelay is typed `OutboxStore[sqlite3.Connection]` and imports sqlite3 in the service layer, so a PostgreSQL store cannot be used without changing the relay. Make OutboxRelay generic over ConnectionT, and keep sqlite3 in storage/sqlite only. Owner: K11. |
| `backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py`, `backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py` | `mark_published` logs at INFO once per event, and `add` and `RecordingPublisher.publish` log at DEBUG once per event. Keep the relay's pass summary at INFO and drop or reduce the per-event lines. Owners: K09, K10. |
| `backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py`, `backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py` | `pending()` loads every unpublished event into memory in one read, with no limit. If the bus is down for a long time the backlog has no bound. A pass with no event, or one stopped by a refused publish, also leaves the read transaction open until close(). Consider a batch size and ending the read transaction at the end of each pass. Owners: K09, K11. |
| `backend/shared/outbox/tests/service/relay/helpers.py`, `backend/shared/outbox/tests/storage/sqlite/helpers.py`, `backend/shared/outbox/tests/storage/sqlite/conftest.py` | Two near-identical helper modules build the synthetic customers table and envelopes. The storage conftest and helpers carry import group comments, which tests do not need. Share the helpers and drop the comments. Owners: K02, K04. |
| `.claude/scripts/tickets/ticket_tree.py`, `.claude/scripts/tickets/tickets.py`, `.claude/rules/tickets.md`, `.claude/rules/enforcement.json` | uv.lock is owned by several running tickets at once (T0.10, T0.11, T0.13, T0.14). No area lock covers it, and `finish` commits it as a whole file. Close the gap with a fix (regenerate the lock from the ticket's clean tree at finish, or lock the root lock files), a test that fails without it, and the rule with its enforcers. |
| `.claude/scripts/tickets/checks.py`, `tests/harness/checks/` | This is a harness gap, and it let the defect come back without anyone seeing it. checks.py should run `uv lock --check`, or `uv sync --locked --all-packages`, in the clean worktree, as CI does. That needs a test that fails on a lock naming a member missing from the clean tree. Separately, a file several running tickets share (uv.lock, pnpm-lock.yaml) needs one owner or a per-ticket rebuild at finish. Record it in enforcement.json. |
| `backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py`, `backend/shared/outbox/tests/storage/sqlite/test_sqlite_outbox_store.py` | `pending()` runs `EventEnvelope.model_validate_json` on every row outside the try block. A corrupt or old-schema row raises `SEInvalidEventEnvelopeException` or `ValidationError` instead of `SEOutboxStoreError`, so the relay does not log it. Wrap the decoding, log the event's sequence and the error type, raise `SEOutboxStoreError` from the error, and add a test that writes a bad row. Owner: K09. |
| `backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py`, `backend/shared/outbox/tests/service/relay/test_outbox_relay.py` | When two relays run on the same database, both can publish the same event, and the second `mark_published` raises "not pending", which stops that pass with an ERROR. Document that only one relay runs per outbox, or treat the second mark as a WARNING and let the pass go on. Owners: K09, K11. |

<!-- timings -->
## ⏱️ Timings

Measured from the agents' transcripts by `python3 .claude/scripts/reports/progress.py timings --ticket T0.10` (TKT-10).

| Measure | Value |
| --- | --- |
| 🕒 Ticket started | 2026-11-27 18:07:05 |
| 🕒 Last activity | 2026-11-27 22:22:37 |
| ⏱️ **Overall ticket time** (first start to last activity) | **4h15m31s** |
| 🤖 Time with agents working (sum of runs) | 38m36s |
| ⏸️ Time between runs (approvals, fixes) | 3h36m55s |
| 🔁 Workflow runs | 5 |
| 🪙 **Tokens consumed** (input, output, cache write, cache read) | **34.31M** |

#### 🪙 Tokens by model

| Model | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- |
| 🟢 haiku | 0k | 155k | 1.40M | 5.12M | **6.68M** |
| 🔵 sonnet | 0k | 219k | 1.67M | 16.21M | **18.10M** |
| 🟣 opus | 0k | 157k | 762k | 8.61M | **9.53M** |
| **All models** | 1k | 532k | 3.84M | 29.94M | **34.31M** |

### 1. ticket-plan · 2026-11-27 18:07:05 to 18:15:38 · ⏱️ 8m33s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Ticket | 18:07:05 | 18:08:04 | 0m58s | 2 |
| Check | 18:08:04 | 18:08:08 | 0m03s | 1 |
| Plan | 18:08:09 | 18:14:24 | 6m15s | 1 |
| Write | 18:14:25 | 18:15:38 | 1m13s | 2 |

Tokens of this run: 0k · 173k · 772k · 6.17M · **7.12M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ done check T0.10 | 🟢 haiku | 18:07:05 | 18:07:11 | 0m06s | 0k | 0k | 37k | 73k | **112k** |
| ✅ ticket-writer T0.10 | 🔵 sonnet | 18:07:12 | 18:08:04 | 0m51s | 0k | 26k | 218k | 1.94M | **2.18M** |
| ✅ check TICKET.md T0.10 | 🟢 haiku | 18:08:04 | 18:08:08 | 0m03s | 0k | 0k | 35k | 38k | **73k** |
| ✅ planner T0.10 | 🟣 opus | 18:08:09 | 18:14:24 | 6m15s | 0k | 88k | 310k | 3.47M | **3.87M** |
| ✅ scribe T0.10 | 🟢 haiku | 18:14:25 | 18:15:35 | 1m10s | 0k | 56k | 134k | 613k | **804k** |
| ✅ check PLAN.md T0.10 | 🟢 haiku | 18:15:35 | 18:15:38 | 0m03s | 0k | 0k | 35k | 38k | **73k** |

### 2. ticket-run · 2026-11-27 21:28:06 to 21:41:32 · ⏱️ 13m25s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 21:28:06 | 21:28:46 | 0m40s | 4 |
| Waves | 21:28:49 | 21:40:17 | 11m28s | 21 |
| Verify | 21:40:17 | 21:41:18 | 1m00s | 1 |
| Review | | | not run | 0 |
| Finish | 21:41:18 | 21:41:32 | 0m14s | 1 |

Tokens of this run: 0k · 195k · 1.38M · 13.92M · **15.50M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.10 | 🟢 haiku | 21:28:06 | 21:28:21 | 0m14s | 0k | 6k | 44k | 158k | **209k** |
| ✅ plan check T0.10 | 🟢 haiku | 21:28:21 | 21:28:24 | 0m02s | 0k | 0k | 34k | 37k | **72k** |
| ✅ start rule T0.10 | 🟢 haiku | 21:28:24 | 21:28:32 | 0m08s | 0k | 0k | 34k | 37k | **72k** |
| ✅ integrator prepare T0.10 | 🔵 sonnet | 21:28:32 | 21:28:46 | 0m13s | 0k | 0k | 35k | 80k | **115k** |
| ✅ K01 test-writer | 🔵 sonnet | 21:28:49 | 21:30:09 | 1m20s | 0k | 23k | 61k | 696k | **781k** |
| ✅ K02 test-writer | 🔵 sonnet | 21:28:52 | 21:30:20 | 1m28s | 0k | 22k | 76k | 1.57M | **1.67M** |
| ✅ K03 test-writer | 🔵 sonnet | 21:28:56 | 21:29:56 | 1m00s | 0k | 4k | 44k | 559k | **608k** |
| ✅ K04 test-writer | 🔵 sonnet | 21:28:59 | 21:30:13 | 1m14s | 0k | 15k | 65k | 794k | **874k** |
| ✅ K05 test-writer | 🔵 sonnet | 21:29:02 | 21:30:13 | 1m10s | 0k | 10k | 64k | 1.06M | **1.13M** |
| ✅ K06 test-writer | 🔵 sonnet | 21:29:06 | 21:30:45 | 1m38s | 0k | 11k | 53k | 1.07M | **1.14M** |
| ✅ integrator Waves | 🔵 sonnet | 21:30:46 | 21:31:04 | 0m17s | 0k | 1k | 41k | 278k | **321k** |
| ✅ K07 implementer | 🔵 sonnet | 21:31:06 | 21:32:04 | 0m58s | 0k | 13k | 69k | 706k | **789k** |
| ✅ K08 implementer | 🔵 sonnet | 21:31:07 | 21:32:38 | 1m31s | 0k | 8k | 53k | 857k | **919k** |
| ✅ integrator Waves | 🔵 sonnet | 21:32:39 | 21:32:58 | 0m18s | 0k | 2k | 45k | 513k | **561k** |
| ✅ K09 implementer | 🔵 sonnet | 21:33:00 | 21:34:16 | 1m16s | 0k | 15k | 70k | 1.00M | **1.09M** |
| ✅ K10 implementer | 🔵 sonnet | 21:33:01 | 21:34:08 | 1m06s | 0k | 3k | 43k | 348k | **395k** |
| ✅ integrator Waves | 🔵 sonnet | 21:34:22 | 21:34:38 | 0m15s | 0k | 1k | 43k | 293k | **338k** |
| ❌ K11 implementer | 🔵 sonnet | 21:34:40 | 21:35:45 | 1m04s | 0k | 7k | 61k | 525k | **594k** |
| ✅ K04 test-writer (fix) | 🔵 sonnet | 21:35:55 | 21:36:42 | 0m46s | 0k | 1k | 38k | 167k | **207k** |
| ✅ integrator Waves | 🔵 sonnet | 21:37:02 | 21:37:13 | 0m10s | 0k | 0k | 40k | 159k | **200k** |
| ✅ K11 implementer | 🔵 sonnet | 21:37:15 | 21:38:46 | 1m30s | 0k | 14k | 65k | 937k | **1.02M** |
| ✅ integrator Waves | 🔵 sonnet | 21:38:57 | 21:39:07 | 0m10s | 0k | 0k | 39k | 157k | **197k** |
| ✅ K12 implementer | 🔵 sonnet | 21:39:10 | 21:39:51 | 0m41s | 0k | 5k | 49k | 447k | **502k** |
| ✅ K13 doc-writer | 🟢 haiku | 21:39:12 | 21:39:58 | 0m46s | 0k | 14k | 64k | 768k | **847k** |
| ✅ integrator Waves | 🔵 sonnet | 21:39:59 | 21:40:17 | 0m17s | 0k | 1k | 45k | 428k | **475k** |
| ✅ verifier round 1 | 🟢 haiku | 21:40:17 | 21:41:18 | 1m00s | 0k | 1k | 39k | 111k | **152k** |
| ✅ scribe T0.10 | 🟢 haiku | 21:41:18 | 21:41:32 | 0m14s | 0k | 6k | 53k | 155k | **214k** |

### 3. ticket-run · 2026-11-27 22:04:27 to 22:14:26 · ⏱️ 9m59s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 22:04:27 | 22:05:08 | 0m40s | 4 |
| Waves | | | not run | 0 |
| Verify | 22:05:08 | 22:06:04 | 0m55s | 1 |
| Review | 22:06:04 | 22:14:01 | 7m56s | 9 |
| Finish | 22:14:01 | 22:14:26 | 0m25s | 1 |

Tokens of this run: 0k · 77k · 797k · 5.62M · **6.50M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.10 | 🟢 haiku | 22:04:27 | 22:04:41 | 0m13s | 0k | 6k | 56k | 202k | **266k** |
| ✅ plan check T0.10 | 🟢 haiku | 22:04:41 | 22:04:44 | 0m03s | 0k | 0k | 39k | 37k | **76k** |
| ✅ start rule T0.10 | 🟢 haiku | 22:04:45 | 22:04:53 | 0m08s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.10 | 🔵 sonnet | 22:04:54 | 22:05:08 | 0m14s | 0k | 0k | 43k | 82k | **125k** |
| ✅ verifier round 1 | 🟢 haiku | 22:05:08 | 22:06:04 | 0m55s | 0k | 0k | 43k | 76k | **120k** |
| ✅ reviewer round 1 | 🟣 opus | 22:06:04 | 22:09:06 | 3m01s | 0k | 32k | 180k | 2.51M | **2.72M** |
| ✅ K08 implementer (fix) | 🔵 sonnet | 22:09:08 | 22:09:39 | 0m30s | 0k | 4k | 50k | 462k | **516k** |
| ✅ integrator Review | 🔵 sonnet | 22:09:39 | 22:09:51 | 0m11s | 0k | 0k | 41k | 167k | **210k** |
| ✅ verifier after review 1 | 🟢 haiku | 22:09:51 | 22:10:45 | 0m53s | 0k | 0k | 5k | 114k | **120k** |
| ✅ reviewer round 2 | 🟣 opus | 22:10:45 | 22:11:23 | 0m38s | 0k | 3k | 58k | 432k | **494k** |
| ✅ K08 implementer (fix) | 🔵 sonnet | 22:11:24 | 22:11:59 | 0m35s | 0k | 1k | 43k | 176k | **221k** |
| ✅ integrator Review | 🔵 sonnet | 22:12:00 | 22:12:12 | 0m11s | 0k | 0k | 8k | 204k | **214k** |
| ✅ verifier after review 2 | 🟢 haiku | 22:12:12 | 22:13:05 | 0m53s | 0k | 0k | 5k | 114k | **120k** |
| ✅ reviewer round 3 | 🟣 opus | 22:13:05 | 22:14:01 | 0m55s | 0k | 9k | 65k | 584k | **659k** |
| ✅ scribe T0.10 | 🟢 haiku | 22:14:01 | 22:14:26 | 0m25s | 0k | 14k | 118k | 418k | **551k** |

### 4. ticket-run · 2026-11-27 22:15:46 to 22:20:32 · ⏱️ 4m45s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 22:15:46 | 22:16:30 | 0m43s | 4 |
| Waves | | | not run | 0 |
| Verify | 22:16:30 | 22:17:23 | 0m52s | 1 |
| Review | 22:17:23 | 22:19:26 | 2m02s | 1 |
| Finish | 22:19:26 | 22:20:32 | 1m05s | 4 |

Tokens of this run: 0k · 75k · 740k · 3.14M · **3.96M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.10 | 🟢 haiku | 22:15:46 | 22:16:01 | 0m15s | 0k | 4k | 93k | 213k | **311k** |
| ✅ plan check T0.10 | 🟢 haiku | 22:16:02 | 22:16:05 | 0m03s | 0k | 0k | 39k | 37k | **76k** |
| ✅ start rule T0.10 | 🟢 haiku | 22:16:05 | 22:16:15 | 0m09s | 0k | 0k | 36k | 39k | **76k** |
| ✅ integrator prepare T0.10 | 🔵 sonnet | 22:16:15 | 22:16:30 | 0m14s | 0k | 0k | 38k | 86k | **125k** |
| ✅ verifier round 1 | 🟢 haiku | 22:16:30 | 22:17:23 | 0m52s | 0k | 0k | 39k | 80k | **120k** |
| ✅ reviewer round 1 | 🟣 opus | 22:17:23 | 22:19:26 | 2m02s | 0k | 22k | 146k | 1.61M | **1.78M** |
| ✅ scribe T0.10 | 🟢 haiku | 22:19:26 | 22:19:57 | 0m30s | 0k | 26k | 156k | 631k | **814k** |
| ✅ explainer T0.10 | 🔵 sonnet | 22:19:26 | 22:20:24 | 0m57s | 0k | 18k | 77k | 313k | **410k** |
| ✅ docs check T0.10 1 | 🟢 haiku | 22:20:24 | 22:20:28 | 0m03s | 0k | 0k | 39k | 76k | **116k** |
| ✅ scribe T0.10 (timings) | 🟢 haiku | 22:20:28 | 22:20:32 | 0m04s | 0k | 0k | 72k | 48k | **121k** |

### 5. ticket-run · 2026-11-27 22:20:44 to 22:22:37 · ⏱️ 1m52s

| Phase | Start | End | Elapsed | Steps |
| --- | --- | --- | --- | --- |
| Gate | 22:20:44 | 22:21:26 | 0m41s | 4 |
| Waves | | | not run | 0 |
| Verify | 22:21:26 | 22:22:19 | 0m53s | 1 |
| Review | | | not run | 0 |
| Finish | 22:22:20 | 22:22:37 | 0m17s | 3 |

Tokens of this run: 0k · 11k · 147k · 1.08M · **1.24M** (input · output · cache write · cache read · total)

| Step | Model | Start | End | Elapsed | Input | Output | Cache write | Cache read | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ gate T0.10 | 🟢 haiku | 22:20:44 | 22:20:58 | 0m13s | 0k | 7k | 49k | 317k | **373k** |
| ✅ plan check T0.10 | 🟢 haiku | 22:20:58 | 22:21:01 | 0m03s | 0k | 0k | 2k | 74k | **76k** |
| ✅ start rule T0.10 | 🟢 haiku | 22:21:02 | 22:21:11 | 0m09s | 0k | 0k | 2k | 74k | **76k** |
| ✅ integrator prepare T0.10 | 🔵 sonnet | 22:21:12 | 22:21:26 | 0m13s | 0k | 0k | 4k | 121k | **125k** |
| ✅ verifier round 1 | 🟢 haiku | 22:21:26 | 22:22:19 | 0m53s | 0k | 0k | 5k | 114k | **120k** |
| ✅ scribe T0.10 | 🟢 haiku | 22:22:20 | 22:22:31 | 0m11s | 0k | 2k | 46k | 299k | **348k** |
| ✅ docs check T0.10 1 | 🟢 haiku | 22:22:31 | 22:22:34 | 0m03s | 0k | 0k | 2k | 74k | **76k** |
| 🔄 integrator finish T0.10 | 🔵 sonnet | 22:22:35 | 22:22:37 | 0m01s | 0k | 0k | 34k | 4k | **39k** |
<!-- /timings -->
