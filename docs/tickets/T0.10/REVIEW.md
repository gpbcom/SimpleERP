# T0.10: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A frozen `EventEnvelope` in `erp_models` is the public contract of an event. It holds `event_id`, `event_type`, `company_id` (required), `occurred_at` (UTC) and an opaque JSON `payload`, and each field raises its own `SE` exception.
- `erp_outbox` stores an event in the caller's own transaction. `SqliteOutboxStore.add` never commits, so a rollback drops the change and its event together. Only `mark_published` commits.
- `OutboxRelay`, a `Runnable` built by `SqliteRelayFactory`, makes one pass in write order. It marks an event only after the `Publisher` returns, which gives at-least-once delivery. A refused publish stops the pass so that later events never overtake the refused one.
- `RecordingPublisher` stands in for the event bus, which is chosen in P2. It is the bus's only connection point.
- `uv.lock` adds only `erp-outbox`. The round-1 blocking finding on the lock is resolved.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. An event written with a change, then the process stopped before publishing, is published after the restart | `test_an_event_written_before_a_stop_is_published_after_the_restart` (a child process commits, then calls `os._exit`), `tests-evidences/pytest-backend-shared-outbox.txt` | ✅ Pass |
| 2. A rolled-back change publishes nothing | `test_a_rolled_back_change_publishes_nothing`, `test_a_change_and_its_event_rolled_back_leave_neither_the_row_nor_a_pending_event` | ✅ Pass |
| 3. With a test publisher, every written event is published at least once through the interface | `test_every_written_event_is_published_once_in_write_order`, `test_a_stop_between_publish_and_mark_publishes_the_event_again_later`, `test_a_refused_publish_leaves_the_event_pending_and_the_next_run_publishes_it` | ✅ Pass |
| 4. The conventions tests pass: the library imports `erp_models` and no service, and the envelope is a model of `backend/models` | `tests-evidences/pytest.txt` (1174 passed, `tests/conventions/` included), `tests-evidences/mypy.txt`, `tests-evidences/ruff-check.txt` | ✅ Pass |
| 5. The library's own tests pass with no mock library | `tests-evidences/pytest-backend-shared-outbox.txt` (36 passed), `tests-evidences/pytest-backend-models.txt` (397 passed). They use real SQLite files and stand-in subclasses, and no `unittest.mock` | ✅ Pass |

## Look at first

- **The transaction boundary** decides whether an event can be lost or invented. `add` writes but never commits or rolls back, `create_table` and `mark_published` commit, and `connect` opens with `autocommit=False`: `backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py` lines 61-154.
- **Publishing before marking**, and stopping the pass on a refusal: `backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py` lines 69-100.
- **Company data isolation.** `company_id` is required on every envelope (`backend/models/src/erp_models/events/event_envelope.py` lines 47, 101-127). The outbox is one table per database, and so per company under D405. `pending()` returns every event of that database, so a service that shared one database between companies would mix them. Read these with the services that adopt the outbox.
- **No secret in the logs.** Only event ids, types, counts and the database path are logged. The payload never is.
- **The `uv.lock` diff** is the `erp-outbox` member and its package entry only, so CI's `uv sync --locked --all-packages` matches this commit.

## Assumptions accepted

- **SQLite reference store behind the generic `OutboxStore`:** accepted. TICKET.md leaves the test storage to the plan, and a PostgreSQL store (storage.md) comes with the first service that owns a database.
- **The five envelope fields and no others:** accepted. The specifications fix none (I-T03-01), and a required `company_id` is the conservative choice for isolation.
- **A synchronous, one-pass relay**, with scheduling, retry and back-off left to the service: accepted. The roadmap asks only for at least once.
- **A refused publish stops the pass, and duplicates are possible:** accepted. At least once (D405) allows duplicates, and consumers deduplicate by `event_id`.
- **`Publisher` and `RecordingPublisher` in the storage layer**, with `RecordingPublisher` in `src/`: accepted. The layering holds.
- **Marking an unknown id raises an error:** accepted as the conservative option.
- **The `events/exceptions/fields/` layout and the `erp_outbox` name:** accepted. The layout matches `erp_models/ids/exceptions`, and the name follows the roadmap and D572.

## Follow-ups

- Make `OutboxRelay` generic over the connection type and keep `sqlite3` out of the service layer, so that a PostgreSQL store fits without changing the relay (K11).
- Add an `AsyncRunnable` relay, or a wrapper, for a FastAPI lifespan (K11).
- Make `pending()` wrap a corrupt row's decoding error in `SEOutboxStoreError`, with a log line and a test (K09).
- Bound the backlog: add a batch size and end the read transaction after each pass (K09, K11).
- Say that only one relay runs per outbox, or make a second relay's "not pending" mark a warning (K09, K11).
- Replace the per-event INFO and DEBUG lines with the per-pass summary (K09, K10).
- Share the near-duplicate test helpers, and drop the import comments in the test files (K02, K04).
- Close the harness gap: `uv.lock` is shared by running tickets with no owner, and `checks.py` does not run `uv lock --check`. This is already listed in PROGRESS.md.
