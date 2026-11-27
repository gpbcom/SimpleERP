# T0.10: Event outbox library

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- A service can write an event in the same transaction as its change: a rollback drops both, a commit keeps both.
- A relay publishes each written event at least once, in write order, through a publisher interface, and resumes after a restart.
- A recording publisher stands in for the event bus, which is chosen in P2.
- A frozen event envelope is the public contract of an event, in the shared models.

## ⚙️ How it works

1. **The envelope:** [`EventEnvelope`](../../../backend/models/src/erp_models/events/event_envelope.py#L26) holds `event_id`, `event_type`, `company_id`, `occurred_at` and `payload`. Each field has its own validator and raises its own `SE` exception: [`event_id`](../../../backend/models/src/erp_models/events/event_envelope.py#L52), [`event_type`](../../../backend/models/src/erp_models/events/event_envelope.py#L82), [`company_id`](../../../backend/models/src/erp_models/events/event_envelope.py#L102) (required), [`occurred_at`](../../../backend/models/src/erp_models/events/event_envelope.py#L130), [`payload`](../../../backend/models/src/erp_models/events/event_envelope.py#L160).
2. **The storage contract:** [`OutboxStore`](../../../backend/shared/outbox/src/erp_outbox/storage/outbox_store.py#L12) is generic over the connection type. `add` never commits, and `mark_published` is the one method that commits.
3. **Opening a connection:** [`SqliteOutboxStore.connect`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L61) opens SQLite with `autocommit=False` ([line 71](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L71)), so the caller's change and its event share one transaction. The table is made by [`create_table`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L78) from the SQL at [lines 37-44](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L37-L44).
4. **Writing an event:** [`add`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L95) inserts the envelope as JSON without committing ([line 107](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L107)). The caller commits or rolls back.
5. **Starting the relay:** [`SqliteRelayFactory.create`](../../../backend/shared/outbox/src/erp_outbox/service/factories/sqlite/sqlite_relay_factory.py#L40) builds the store and the [`OutboxRelay`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L16). [`initialize`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L54) connects and creates the table.
6. **One pass:** [`run`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L69) reads [`pending`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L113) (unpublished rows by `sequence`, write order) and calls the publisher for each event first, then marks it with [`mark_published`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L133). A stop between the two means a later re-publish, which is at least once.
7. **A refused publish:** an `SEOutboxPublishError` is logged as a warning and the pass returns ([lines 82-95](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L82-L95)), so later events never overtake the refused one. They stay pending for the next run.
8. **The test publisher:** [`RecordingPublisher.publish`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py#L37) appends each event to a list, in place of the bus. [`Publisher`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/publisher.py#L10) is the only connection point of the future bus.
9. **Closing:** [`close`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L102) is safe after a failed `initialize` and when called twice.

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`backend/models/src/erp_models/events/__init__.py`](../../../backend/models/src/erp_models/events/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/events/event_envelope.py`](../../../backend/models/src/erp_models/events/event_envelope.py) | Added | [1-179](../../../backend/models/src/erp_models/events/event_envelope.py#L1) | +179 | −0 |
| [`backend/models/src/erp_models/events/exceptions/__init__.py`](../../../backend/models/src/erp_models/events/exceptions/__init__.py) | Added | [1-15](../../../backend/models/src/erp_models/events/exceptions/__init__.py#L1) | +15 | −0 |
| [`backend/models/src/erp_models/events/exceptions/fields/__init__.py`](../../../backend/models/src/erp_models/events/exceptions/fields/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_company_id.py`](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_company_id.py) | Added | [1-7](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_company_id.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_event_id.py`](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_event_id.py) | Added | [1-7](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_event_id.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_event_type.py`](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_event_type.py) | Added | [1-7](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_event_type.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_occurred_at.py`](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_occurred_at.py) | Added | [1-7](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_occurred_at.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_payload.py`](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_payload.py) | Added | [1-7](../../../backend/models/src/erp_models/events/exceptions/fields/se_event_envelope_invalid_payload.py#L1) | +7 | −0 |
| [`backend/models/src/erp_models/events/exceptions/se_invalid_event_envelope_exception.py`](../../../backend/models/src/erp_models/events/exceptions/se_invalid_event_envelope_exception.py) | Added | [1-10](../../../backend/models/src/erp_models/events/exceptions/se_invalid_event_envelope_exception.py#L1) | +10 | −0 |
| [`backend/models/tests/events/test_event_envelope.py`](../../../backend/models/tests/events/test_event_envelope.py) | Added | [1-134](../../../backend/models/tests/events/test_event_envelope.py#L1) | +134 | −0 |
| [`backend/shared/outbox/README.md`](../../../backend/shared/outbox/README.md) | Added | [1-125](../../../backend/shared/outbox/README.md#L1) | +125 | −0 |
| [`backend/shared/outbox/pyproject.toml`](../../../backend/shared/outbox/pyproject.toml) | Added | [1-19](../../../backend/shared/outbox/pyproject.toml#L1) | +19 | −0 |
| [`backend/shared/outbox/src/erp_outbox/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/models/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/models/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/models/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/models/exceptions/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/__init__.py) | Added | [1-11](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/__init__.py#L1) | +11 | −0 |
| [`backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_error.py`](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_error.py) | Added | [1-7](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_error.py#L1) | +7 | −0 |
| [`backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_publish_error.py`](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_publish_error.py) | Added | [1-7](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_publish_error.py#L1) | +7 | −0 |
| [`backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_store_error.py`](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_store_error.py) | Added | [1-7](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_store_error.py#L1) | +7 | −0 |
| [`backend/shared/outbox/src/erp_outbox/py.typed`](../../../backend/shared/outbox/src/erp_outbox/py.typed) | Added | ➖ | +0 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/service/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/service/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/factories/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/service/factories/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/service/factories/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/factories/relay_factory.py`](../../../backend/shared/outbox/src/erp_outbox/service/factories/relay_factory.py) | Added | [1-17](../../../backend/shared/outbox/src/erp_outbox/service/factories/relay_factory.py#L1) | +17 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/factories/sqlite/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/service/factories/sqlite/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/service/factories/sqlite/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/factories/sqlite/sqlite_relay_factory.py`](../../../backend/shared/outbox/src/erp_outbox/service/factories/sqlite/sqlite_relay_factory.py) | Added | [1-48](../../../backend/shared/outbox/src/erp_outbox/service/factories/sqlite/sqlite_relay_factory.py#L1) | +48 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/relay/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/service/relay/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/service/relay/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py) | Added | [1-108](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L1) | +108 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/storage/__init__.py) | Added | [1](../../../backend/shared/outbox/src/erp_outbox/storage/__init__.py#L1) | +1 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/outbox_store.py) | Added | [1-69](../../../backend/shared/outbox/src/erp_outbox/storage/outbox_store.py#L1) | +69 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/publishers/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/publishers/publisher.py`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/publisher.py) | Added | [1-33](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/publisher.py#L1) | +33 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py) | Added | [1-44](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py#L1) | +44 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/sqlite/__init__.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py) | Added | [1-154](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L1) | +154 | −0 |
| [`backend/shared/outbox/tests/models/exceptions/test_outbox_exceptions.py`](../../../backend/shared/outbox/tests/models/exceptions/test_outbox_exceptions.py) | Added | [1-38](../../../backend/shared/outbox/tests/models/exceptions/test_outbox_exceptions.py#L1) | +38 | −0 |
| [`backend/shared/outbox/tests/service/factories/sqlite/test_sqlite_relay_factory.py`](../../../backend/shared/outbox/tests/service/factories/sqlite/test_sqlite_relay_factory.py) | Added | [1-42](../../../backend/shared/outbox/tests/service/factories/sqlite/test_sqlite_relay_factory.py#L1) | +42 | −0 |
| [`backend/shared/outbox/tests/service/relay/conftest.py`](../../../backend/shared/outbox/tests/service/relay/conftest.py) | Added | [1-35](../../../backend/shared/outbox/tests/service/relay/conftest.py#L1) | +35 | −0 |
| [`backend/shared/outbox/tests/service/relay/helpers.py`](../../../backend/shared/outbox/tests/service/relay/helpers.py) | Added | [1-35](../../../backend/shared/outbox/tests/service/relay/helpers.py#L1) | +35 | −0 |
| [`backend/shared/outbox/tests/service/relay/refusing_publisher.py`](../../../backend/shared/outbox/tests/service/relay/refusing_publisher.py) | Added | [1-30](../../../backend/shared/outbox/tests/service/relay/refusing_publisher.py#L1) | +30 | −0 |
| [`backend/shared/outbox/tests/service/relay/test_outbox_relay.py`](../../../backend/shared/outbox/tests/service/relay/test_outbox_relay.py) | Added | [1-105](../../../backend/shared/outbox/tests/service/relay/test_outbox_relay.py#L1) | +105 | −0 |
| [`backend/shared/outbox/tests/service/relay/unmarkable_store.py`](../../../backend/shared/outbox/tests/service/relay/unmarkable_store.py) | Added | [1-15](../../../backend/shared/outbox/tests/service/relay/unmarkable_store.py#L1) | +15 | −0 |
| [`backend/shared/outbox/tests/service/relay/write_then_stop.py`](../../../backend/shared/outbox/tests/service/relay/write_then_stop.py) | Added | [1-29](../../../backend/shared/outbox/tests/service/relay/write_then_stop.py#L1) | +29 | −0 |
| [`backend/shared/outbox/tests/storage/publishers/test_recording_publisher.py`](../../../backend/shared/outbox/tests/storage/publishers/test_recording_publisher.py) | Added | [1-40](../../../backend/shared/outbox/tests/storage/publishers/test_recording_publisher.py#L1) | +40 | −0 |
| [`backend/shared/outbox/tests/storage/sqlite/conftest.py`](../../../backend/shared/outbox/tests/storage/sqlite/conftest.py) | Added | [1-32](../../../backend/shared/outbox/tests/storage/sqlite/conftest.py#L1) | +32 | −0 |
| [`backend/shared/outbox/tests/storage/sqlite/helpers.py`](../../../backend/shared/outbox/tests/storage/sqlite/helpers.py) | Added | [1-32](../../../backend/shared/outbox/tests/storage/sqlite/helpers.py#L1) | +32 | −0 |
| [`backend/shared/outbox/tests/storage/sqlite/test_sqlite_outbox_store.py`](../../../backend/shared/outbox/tests/storage/sqlite/test_sqlite_outbox_store.py) | Added | [1-101](../../../backend/shared/outbox/tests/storage/sqlite/test_sqlite_outbox_store.py#L1) | +101 | −0 |
| [`uv.lock`](../../../uv.lock) | Modified | [11](../../../uv.lock#L11), [140-154](../../../uv.lock#L140) | +16 | −0 |
| **47 files** | | | **+1579** | **−0** |
<!-- /changes -->

- [`backend/models/src/erp_models/events/`](../../../backend/models/src/erp_models/events/event_envelope.py): the envelope, with one exception per field under `exceptions/fields/` to stay within five files per folder, as `erp_models/ids` does.
- [`backend/models/tests/events/test_event_envelope.py`](../../../backend/models/tests/events/test_event_envelope.py): the standard model tests.
- [`backend/shared/outbox/pyproject.toml`](../../../backend/shared/outbox/pyproject.toml), [`README.md`](../../../backend/shared/outbox/README.md), [`uv.lock`](../../../uv.lock): the new `erp-outbox` member; the lock adds only that member.
- [`backend/shared/outbox/src/erp_outbox/models/exceptions/`](../../../backend/shared/outbox/src/erp_outbox/models/exceptions/se_outbox_error.py): `SEOutboxError`, `SEOutboxStoreError` and `SEOutboxPublishError`.
- [`storage/outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/outbox_store.py) and [`storage/sqlite/sqlite_outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py): the store interface and its SQLite reference store (lines 18-154).
- [`storage/publishers/`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/publisher.py): the `Publisher` interface and `RecordingPublisher`.
- [`service/relay/outbox_relay.py`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py) and [`service/factories/`](../../../backend/shared/outbox/src/erp_outbox/service/factories/relay_factory.py): the one-pass relay and its factories.
- [`backend/shared/outbox/tests/`](../../../backend/shared/outbox/tests/service/relay/test_outbox_relay.py): real SQLite files, stand-in subclasses and a child process that commits then calls `os._exit` ([`write_then_stop.py`](../../../backend/shared/outbox/tests/service/relay/write_then_stop.py)). No mock library.

## 🧪 How to test it

```bash
uv run --package erp-outbox pytest backend/shared/outbox/tests -n 2
uv run --package erp-models pytest backend/models/tests/events -n 2
uv run pytest tests/conventions -n 2
uv run ruff check backend
uv run mypy backend/models/src backend/shared/*/src
```

## 🔗 Evidence

- [Outbox tests](tests-evidences/pytest-backend-shared-outbox.txt): 36 passed.
- [Models tests](tests-evidences/pytest-backend-models.txt): 397 passed.
- [Whole suite, conventions included](tests-evidences/pytest.txt): 1174 passed.
- [mypy](tests-evidences/mypy.txt), [ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt): clean.
- [Specification links](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt).

## 📝 Assumptions accepted

- A generic `OutboxStore` with a SQLite reference store (stdlib `sqlite3`, real file); a PostgreSQL store comes with the first service that owns a database.
- The envelope holds only `event_id`, `event_type`, `company_id`, `occurred_at` and `payload`; `company_id` is required (D405).
- The API is synchronous and the relay is a one-pass `Runnable`; scheduling, retry and back-off are left to the service.
- A refused publish stops the pass and leaves that event and later ones pending; a failed mark leads to a later re-publish, and consumers deduplicate by `event_id`.
- `Publisher` and `RecordingPublisher` sit in the storage layer, with `RecordingPublisher` in `src/` for T0.11 and the services' tests.
- `mark_published` of an unknown or already-published id raises `SEOutboxStoreError`.
- Envelope exceptions sit in `erp_models/events/exceptions/fields/` to keep to the five-files rule.
- The package is named `erp_outbox` (distribution `erp-outbox`), per the roadmap and D572.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`outbox_relay.py`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L35), [`relay_factory.py`](../../../backend/shared/outbox/src/erp_outbox/service/factories/relay_factory.py), [`test_outbox_relay.py`](../../../backend/shared/outbox/tests/service/relay/test_outbox_relay.py) | `OutboxRelay` is typed on `sqlite3.Connection` and imports `sqlite3` in the service layer. Make it generic over the connection type so a PostgreSQL store fits. Owner: K11. |
| [`outbox_relay.py`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py) | The relay is a sync `Runnable` and would block the event loop in a lifespan. Add an `AsyncRunnable` variant or a documented wrapper. Owner: K11. |
| [`sqlite_outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L131), [`test_sqlite_outbox_store.py`](../../../backend/shared/outbox/tests/storage/sqlite/test_sqlite_outbox_store.py) | `pending()` decodes rows outside the `try`, so a corrupt row does not raise `SEOutboxStoreError`. Wrap it, log the sequence and error type, and test a bad row. Owner: K09. |
| [`sqlite_outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py), [`outbox_relay.py`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py) | `pending()` has no limit, and a pass that publishes nothing keeps its read transaction open until `close()`. Add a batch size and end the read transaction after each pass. Owners: K09, K11. |
| [`sqlite_outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L146), [`test_outbox_relay.py`](../../../backend/shared/outbox/tests/service/relay/test_outbox_relay.py) | With two relays on one database, the second mark raises "not pending" and stops that pass with an ERROR. Say in the README that one relay runs per outbox, or treat it as a WARNING. Owners: K09, K11. |
| [`sqlite_outbox_store.py`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py), [`recording_publisher.py`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py) | Per-event INFO and DEBUG lines: keep the relay's per-pass summary and drop or reduce them. Owners: K09, K10. |
| [`relay/helpers.py`](../../../backend/shared/outbox/tests/service/relay/helpers.py), [`sqlite/helpers.py`](../../../backend/shared/outbox/tests/storage/sqlite/helpers.py), [`sqlite/conftest.py`](../../../backend/shared/outbox/tests/storage/sqlite/conftest.py) | Two near-identical helper modules: share them, and drop the import group comments from the storage conftest and helpers. Owners: K02, K04. |
