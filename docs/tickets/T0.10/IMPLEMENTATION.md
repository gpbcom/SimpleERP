# T0.10: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- An event is written in the same transaction as the change, and a rolled-back change publishes nothing ([TICKET.md](TICKET.md), criteria 1 and 2; D405).
- Delivery is at least once through a publisher interface, with a test publisher in place of the bus chosen in P2 ([TICKET.md](TICKET.md), criterion 3).
- The library lives in `backend/shared/outbox`, imports `erp_models` and no service, and the envelope is a model of `backend/models` (D438, [AGENT.md](../../../AGENT.md)).
- Layers go `api`, `service`, `storage`, `models`; one class per file, at most five files per folder, no `unittest.mock` ([AGENT.md](../../../AGENT.md)).
- The roadmap states no storage for the outbox, and no retry or ordering rule beyond at least once ([TICKET.md](TICKET.md), assumptions).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Transaction ownership | `add` never commits | `add` opens and commits its own transaction | The caller must commit |
| [D2](#d2) | Test storage | Generic `OutboxStore` with a SQLite store | PostgreSQL store now | No PostgreSQL store yet |
| [D3](#d3) | Order of publish and mark | Publish, then mark | Mark, then publish | Duplicates are possible |
| [D4](#d4) | Refused publish | Stop the pass | Skip the event and go on | A refused event blocks later ones |
| [D5](#d5) | Relay shape | Synchronous one-pass `Runnable` | Looping or async relay | Scheduling is left to the service |
| [D6](#d6) | Envelope fields | Five fields, `company_id` required | Optional tenant, extra metadata | No other metadata yet |
| [D7](#d7) | Publisher placement | Storage layer, recorder in `src/` | Recorder in `tests/` only | Test code ships in the package |

## <a id="d1"></a>D1: Transaction ownership

**Chosen:** `add` writes on the caller's connection and never commits · **Where:** [`sqlite_outbox_store.py:95-110`](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L95-L110) · **Source:** read from the diff, [REVIEW.md](REVIEW.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Caller's transaction | A rollback drops the change and its event together (criterion 2) | The caller must commit |
| Own transaction in `add` | Simpler call | The event could commit without the change, or the reverse |

**Trade-off:** the caller owns the commit, which is what makes the outbox atomic.

**Revisit when:** a service wraps transactions in a unit of work that hides the connection.

## <a id="d2"></a>D2: Test storage

**Chosen:** generic [`OutboxStore`](../../../backend/shared/outbox/src/erp_outbox/storage/outbox_store.py#L12) with a [SQLite store](../../../backend/shared/outbox/src/erp_outbox/storage/sqlite/sqlite_outbox_store.py#L18) · **Source:** PLAN.md, accepted assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ SQLite behind an interface | Stdlib, a real file in `tmp_path`, no mock; T0.13 is not a prerequisite | Not the production database |
| PostgreSQL store | The storage page of the technical docs names PostgreSQL | Needs the test server of T0.13, not a prerequisite |

**Trade-off:** the relay is still typed on `sqlite3.Connection` (follow-up, K11).

**Revisit when:** the first service owning a database adopts the outbox.

## <a id="d3"></a>D3: Publish, then mark

**Chosen:** publish, then mark · **Where:** [`outbox_relay.py:82-95`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L82-L95) · **Source:** read from the diff, D405

| Option | For | Against |
| --- | --- | --- |
| ✅ Publish then mark | No event lost (at least once) | A stop between the two publishes it again |
| Mark then publish | No duplicate | An event is lost if the stop comes after the mark |

**Trade-off:** consumers deduplicate by `event_id`.

**Revisit when:** the bus offers transactional publishing, a P2 matter.

## <a id="d4"></a>D4: Refused publish stops the pass

**Chosen:** return at the first refusal · **Where:** [`outbox_relay.py:85-93`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L85-L93) · **Source:** read from the diff, reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ Stop | Later events never overtake the refused one | One bad event blocks the rest |
| Skip and go on | Throughput | Breaks write order |

**Trade-off:** order over throughput. The roadmap states no ordering rule, so this is the conservative reading.

**Revisit when:** a bus requires no order, or a dead-letter rule is specified. Open point: no worker gave a reason beyond order.

## <a id="d5"></a>D5: A synchronous one-pass relay

**Chosen:** sync `Runnable`, one pass · **Where:** [`outbox_relay.py:16`](../../../backend/shared/outbox/src/erp_outbox/service/relay/outbox_relay.py#L16) · **Source:** PLAN.md, accepted assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ One pass | Testable with no timer; retry and back-off belong to the service | Blocks the event loop in a lifespan |
| `AsyncRunnable` loop | Fits the lifespan of [AGENT.md](../../../AGENT.md) | Needs scheduling and retry rules the roadmap does not state |

**Trade-off:** the service must schedule the pass. **Revisit when:** the first service uses it (follow-up, K11).

## <a id="d6"></a>D6: The envelope

**Chosen:** [five fields](../../../backend/models/src/erp_models/events/event_envelope.py#L26), `company_id` required, frozen · **Source:** PLAN.md, accepted assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Five fields, required `company_id` | Specifications fix no field (I-T03-01); D405 isolates data per company | No version or correlation fields |
| Optional `company_id` | Fits platform events | Weakens isolation |

**Trade-off:** minimal contract, easy to extend. **Revisit when:** I-T03-01 or the bus fix a schema.

## <a id="d7"></a>D7: Publisher placement

**Chosen:** [`Publisher`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/publisher.py#L10) and [`RecordingPublisher`](../../../backend/shared/outbox/src/erp_outbox/storage/publishers/recording_publisher.py#L13) in the storage layer, recorder in `src/` · **Source:** accepted assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ In `src/` | T0.11 and services' tests reuse it; the layering holds | Test double ships in the package |
| In `tests/` | Keeps `src/` clean | Other packages cannot import it |

**Trade-off:** a small test double in the library. **Revisit when:** a shared test-helpers library exists.

## 📝 Assumptions behind the choices

- SQLite reference store: supports [D2](#d2).
- Five envelope fields, `company_id` required: supports [D6](#d6).
- Synchronous one-pass relay: supports [D5](#d5).
- Refused publish stops the pass, duplicates allowed: supports [D3](#d3) and [D4](#d4).
- Recorder in `src/`: supports [D7](#d7).
