# T0.11: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A new shared library, `erp_metering`, provides `MeteringClient.call(paid_call, work)`. Every paid call goes through five steps in order: budget check, reservation, the work, settlement, and one `metering.usage` event written through the T0.10 outbox (TC-21, D405).
- A call without a legal duty is stopped before its work runs in three cases: the budget check says the budget is spent, the reservation is refused with a 409, or the metering server cannot be reached.
- A call with `legal_duty=True` is never stopped (BR-F22-06, D398). Over budget, it goes on with a WARNING and its event has `over_budget=True`. With the server unreachable, it goes on without a reservation.
- When the work fails, the reservation is released and no settlement or event is written. When only the settlement fails, the work's result is still returned and the event is still written.
- The library talks to the metering server through an httpx repository. Every failure is mapped to `SEMeteringServerUnavailableError`, and logs show only ids, outcomes and exception types, never costs.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given a stand-in metering server and a budget already spent, when a paid call is made, then it is refused before the call is made | `TestStopAtBudget::test_a_call_without_legal_duty_is_refused_when_the_budget_is_spent`, `test_a_refused_call_only_reaches_the_budget_check`; tests-evidences/pytest-backend-shared-metering.txt (153 passed) | ✅ Pass |
| 2. Given a call within budget, when it is reserved, made and settled, then exactly one usage event is emitted through the outbox | `TestSettledCall::test_one_usage_event_is_written_for_the_settled_call`, `test_the_server_sees_the_check_the_reservation_and_the_settlement_in_order`; tests-evidences/pytest-backend-shared-metering.txt | ✅ Pass |
| 3. Given an exhausted budget, when a call carries the legal-duty flag, then it passes | `TestStopAtBudget::test_a_call_with_a_legal_duty_goes_on_when_the_budget_is_spent`, `TestUnavailableServer::test_a_call_with_legal_duty_returns_the_result_of_the_work`; tests-evidences/pytest-backend-shared-metering.txt | ✅ Pass |

The repository-wide checks also pass: ruff check, ruff format (68 files), mypy, and the full pytest run (1328 passed). See tests-evidences/.

## Look at first

- **How a call is admitted** (`_admit`, `_stop_or_flag`): a spent budget, a refused reservation and an unreachable server each decide between stopping and flagging, depending on `legal_duty`. Read this line by line. It is where the BR-F22-06 bypass lives: `backend/shared/metering/src/erp_metering/service/metering/metering_client.py`.
- **Company data isolation:** the outbox envelope takes its `company_id` from `PaidCall.company_id`, which the caller supplies, not from the company context library: `backend/shared/metering/src/erp_metering/storage/events/usage_event_writer.py`, `backend/shared/metering/src/erp_metering/models/calls/paid_call.py`.
- **The event write:** each event is committed in its own sqlite transaction, apart from the caller's transaction. If that write fails after the work succeeded, `call()` raises and the work's result is lost: `backend/shared/metering/src/erp_metering/storage/events/usage_event_writer.py`, `backend/shared/metering/src/erp_metering/service/metering/metering_client.py`.
- **Failure mapping and logs:** check that no cost or body reaches the logs: `backend/shared/metering/src/erp_metering/storage/servers/metering_server_repository.py`.

## Assumptions accepted

- BR-F22-06 and D398 are linked in place of a use case: accepted, because they settle the stop and its exception.
- The legal-duty list is not read, only the flag is carried: accepted, because BR-F22-06 puts the list in the country pack.
- A reservation is made before each call, while exactness under parallel calls is still open in TC-21: accepted as the conservative option TC-21 lists.
- The ticket links to the sprint and epics anchors: accepted, because that is how the roadmap anchors its rows.
- A legal-duty call goes on without a reservation when the server is unreachable: accepted, because BR-F22-06 says a legal duty is never cut, and the call still writes an event.

## Follow-ups

- Release the reservation when the work is cancelled, not only when it raises an `Exception`. Owner K16, test K08.
- Stop the event write from blocking the event loop (`asyncio.to_thread`, or write in the caller's transaction as D405's outbox pattern intends), and stop typing the outbox as SQLite only. Owner K15.
- Decide what `call()` does when the event cannot be written after a successful work: keep the raise or return the result with an ERROR log, and document the retry hazard. Owners K16, K12.
- Fix the `Settlement` Notes: they say a failed call is settled at zero cost, but the client releases it. Owner K10.
- Relabel the mislabelled import group comments in the models and storage files. Owners K10, K13, K14, K15.
- Replace the nested lambda in the `outbox_events` fixture with a helper. Owner K04.
- Move the stand-in metering server onto the T0.13 stand-in kit once that kit exists. Owner K04.
- Later: check the `legal_duty` flag against the country pack's list of legal duties, so callers cannot bypass the stop freely.

No relayed user request was part of this review's brief, and no file was changed.
