# T0.11: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Every paid call goes through one library: budget check, reservation, call, settlement, usage event (TC-21 and the [architecture page](../../technical/architecture/architecture.md)).
- At 100 % new paid calls stop, except calls a legal duty needs ([BR-F22-06](../../specs/02-functional/f22-unified-cost-management/business-rules/br-f22-06-stop-at-budget-legal-duties-kept.md), [D398](../../specs/06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md)).
- The usage event goes through the outbox of T0.10 ([D405](../../specs/06-decisions/technical/d405-architecture-and-scalability.md)).
- AGENT.md: layers `models`, `storage`, `service`; no module-level TypeVar or constants; one class per file; async methods after sync ones; logs without secrets or typed values.
- The metering server protocol is not specified, and the stand-in server kit of T0.13 is out of scope ([TICKET.md](TICKET.md)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Where the legal-duty bypass is decided | In the client | In the server | The flag is trusted from the caller |
| [D2](#d2) | Budget check before the call | Check, then reserve, then settle | Check only | One more round trip per call |
| [D3](#d3) | Legal-duty call with the server down | Goes on, no reservation | Refuse it | Its cost is not counted on the server |
| [D4](#d4) | Failed work or failed settlement | Release on failure, keep the result on a failed settlement | Settle at zero, or raise | A cancelled task keeps its reservation |
| [D5](#d5) | How the event is written | Own transaction, then a raise on failure | Caller's transaction | Blocks the loop, result lost on failure |
| [D6](#d6) | Server protocol and stand-in | Own routes, stand-in on `http.server` | Wait for T0.13 | A later move onto the kit |

## <a id="d1"></a>D1: Where the legal-duty bypass is decided

**Chosen:** the client · **Where:** [`../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py:61-80`](../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py#L61-L80) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ In the client | The architecture page says a flag bypasses the stop; the server only answers within budget or not | Any caller can set the flag |
| In the server | One place to decide | Needs the server to know the duty; the server does not exist yet |

**Trade-off:** the flag is carried, not checked, because BR-F22-06 puts the list in the country pack.

**Revisit when:** a ticket reads the country pack, so the flag can be checked against its list.

## <a id="d2"></a>D2: Budget check, reservation and settlement

**Chosen:** check, reserve, call, settle · **Where:** [`../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py:98-102`](../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py#L98-L102) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Check then reserve | TC-21 lists "budget counters reserved before a call and settled after it"; a 409 stops a race the check missed | Two requests before the work |
| Check only | One request | Parallel calls could all pass; TC-21 leaves exactness open |

**Trade-off:** an extra request for the conservative reading of an open question.

**Revisit when:** TC-21 settles whether exactness under parallel calls is needed.

## <a id="d3"></a>D3: A legal-duty call when the server is unreachable

**Chosen:** it goes on without a reservation, and still writes an event · **Where:** [`../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py:106-112`](../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py#L106-L112) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Go on | TC-21: a stop must never cut an e-invoice or a payroll declaration | The server never counts its cost |
| Refuse it | Fails closed | Cuts a legal duty |

**Trade-off:** an uncounted cost, recorded in the usage event (`reservation_id` is None) so it can be reconciled.

**Revisit when:** the metering server has a reconciliation path.

## <a id="d4"></a>D4: Failed work and failed settlement

**Chosen:** release on an `Exception` of the work, keep the result when only the settlement fails · **Where:** [`../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py:166-170`](../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py#L166-L170), [`../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py:139-142`](../../../backend/shared/metering/src/erp_metering/service/metering/metering_client.py#L139-L142) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Release, no event | Nothing was spent; the work's exception is unchanged | A cancelled task is not covered (follow-up) |
| Settle at zero cost | Keeps one path | The Notes of `Settlement` say this, but the code releases (follow-up) |
| Raise when settlement fails | Visible | Loses a result already paid for |

**Trade-off:** a cancellation leaves its reservation held.

**Revisit when:** the cancellation follow-up (K16) is done.

## <a id="d5"></a>D5: Writing the usage event

**Chosen:** own connection and transaction, raising when it fails · **Where:** [`usage_event_writer.py:44-62`](../../../backend/shared/metering/src/erp_metering/storage/events/usage_event_writer.py#L44-L62) · **Source:** PLAN.md and read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Own transaction | The outbox's `add` never commits; the library has no caller transaction | Sync sqlite in an async method; ties the type to SQLite |
| Caller's transaction | D405's outbox pattern | The call API takes no connection |

**Trade-off:** a blocked event loop and a lost result on a failed write, to keep no paid call unrecorded.

**Revisit when:** a caller needs one transaction, or the follow-ups of K15 and K16 are taken.

## <a id="d6"></a>D6: Server routes and the stand-in

**Chosen:** the client defines its routes and the tests use a stand-in on the standard library · **Where:** [`metering_server_repository.py:38-40`](../../../backend/shared/metering/src/erp_metering/storage/servers/metering_server_repository.py#L38-L40), [`stand_in_metering_server.py:18`](../../../backend/shared/metering/tests/stand_in/stand_in_metering_server.py#L18) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Own routes and stand-in | The specifications name no protocol; T0.13 is not a prerequisite | Routes may change when the server is built |
| Wait for T0.13 | Shared kit | Blocks the ticket |

**Trade-off:** a later move onto the kit, listed as a follow-up.

**Revisit when:** T0.13 lands or the metering server fixes its API.

## 📝 Assumptions behind the choices

- Legal duties come from the country pack, not read here: supports [D1](#d1).
- A reservation before each call as the conservative option: supports [D2](#d2).
- A legal-duty call goes on without a reservation when the server is unreachable: supports [D3](#d3).
