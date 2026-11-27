# T0.09: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A new shared library `erp_context` in `backend/shared/context` holds the company context. A pure ASGI middleware refuses every HTTP request that has no valid company (400 `CONTEXT-COMPANY-01`) or no user (401 `CONTEXT-USER-01`). For any other request it binds the user, the company and the request id in a `ContextVar` until the response is sent. Websockets are closed with code 1008. Public paths pass through.
- Rights go through one decision path, `RightsService.decide`. A record of another company is refused before any policy is asked. One DENY wins over any ALLOW. When no policy allows the action, the answer is the deny-by-default `no-policy`. `allowed()` (a direct call) and `RightsGuard.check` (HTTP) both use this path.
- Refusals are answered as `application/problem+json`. The body is built from the refusal catalogue only (`conf/catalogs/refusal_codes.yaml`), and its `instance` is the request id. Every refusal is logged at WARNING with its code, reason, user, company, action and record ids.
- The lock problem of rounds 1 to 3 is fixed. `uv.lock` now belongs to T0.09, and it adds only `erp-context` and its dependencies on top of the committed lock, which already holds T0.10's outbox.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. A request without a company is refused | `test_company_context_middleware.py::test_a_request_without_a_company_is_refused_with_the_catalogue_status`, `test_an_invalid_company_is_refused_like_a_missing_one`, `test_a_refused_request_never_reaches_the_application`; tests-evidences/pytest-backend-shared-context.txt (363 passed) | ✅ Pass |
| 2. The same user, action and record give the same decision from HTTP and from a direct call | `tests/api/rights/test_decision_parity.py::test_http_and_a_direct_call_give_the_same_decision` (allowed, no policy, other company, unknown action) | ✅ Pass |
| 3. With no policy that allows it, `allowed()` denies by default | `tests/service/rights/test_rights_service.py::test_with_no_policy_every_action_is_denied`, `test_enforce_raises_no_policy_when_nothing_votes` | ✅ Pass |
| 4. A refusal is problem+json with its code and no secret | `tests/api/problems/test_refusal_handler.py::test_a_refusal_is_problem_json_with_its_code`, `test_the_body_holds_no_header_value_of_the_request`; `test_company_context_middleware.py::test_the_body_and_the_logs_never_hold_a_secret_or_the_raw_company` | ✅ Pass |
| 5. A refusal is logged with its code, who, what and why | `test_rights_service.py::test_each_refusal_is_logged_at_warning_with_its_details`, `test_a_refusal_for_another_company_is_logged_with_its_code`; `test_company_context_middleware.py::test_the_refusal_log_line_holds_the_code_the_reason_the_method_and_the_path` | ✅ Pass |

The checks pass on the ticket's own tree: tests-evidences/ruff-check.txt, ruff-format.txt, mypy.txt (no issues in 223 files) and pytest.txt (1174 repository tests passed, conventions included).

## Look at first

- **Where company isolation is enforced, read line by line:** `backend/shared/context/src/erp_context/service/rights/rights_service.py` (`decide`: the company check comes first, then deny wins, then the default refusal) and `backend/shared/context/src/erp_context/api/middleware/company_context_middleware.py` (`__call__`: lifespan passes, other non-http scopes are refused, public paths are matched exactly, and the context is released in `finally`).
- **Where identity is trusted:** the middleware takes `X-Company-Id` and `X-User-Id` from the client and checks no token and no membership. This is safe only behind the gateway, which is out of scope and comes later. The assumption is not written down anywhere yet (follow-up).
- **The context crosses tasks:** `backend/shared/context/src/erp_context/storage/context/request_context_store.py` uses a ClassVar `ContextVar`. The exception handler runs inside the middleware, so `RefusalHandler` still sees the request id.
- **No secret leaks:** `backend/shared/context/src/erp_context/api/problems/problem_builder.py` fills the body from the catalogue only, never from the exception message or the headers.
- **Lock:** check that `uv.lock` adds only `erp-context` and its dependencies (fastapi 0.165, starlette, httpx and their own dependencies).

## Assumptions accepted

- The sprint anchor `#s02` and the `#epics` link stand in for the missing roadmap row anchor: accepted, because it is only a link.
- "Logged for the audit" is a WARNING log line with the code, who, what and why: accepted, because the I-T03-01 audit writer is not in this ticket and REQ-T02-06 criterion 1 is met.
- Out of scope (the RLS storage guard, the gateway, the refusal-burst alert, the first service): accepted, as the roadmap row reads. TICKET.md and security.md also say the audit writer comes "in T0.10". That is not true, since T0.10 is the outbox, and it is listed as a follow-up.

## Follow-ups

- Fix the claim in security.md and TICKET.md that the audit writer comes in T0.10.
- Write down the gateway trust assumption for the `X-Company-Id` and `X-User-Id` headers (README, security.md).
- Correct the README: `allowed` returns `bool`, and the `public_paths` default is an empty list.
- `SEAccessDeniedError.CODE` is fixed to `RIGHTS-DENIED-02` for all three refusal reasons: derive it from the reason, or document that it is not authoritative.
- Register the refusal codes in the shared `error_codes.yaml`, or record why they stay apart.
- Rename `title_key`, `why_key` and `action_key`, because a field ending in `_key` means a secret store entry.
- Write `Union[...]` instead of `X | Y` in four model validators, and fix the import group in `rights_decision.py`.
- Keep one copy of the test `AllowActionPolicy`.
- Add an `erp_context` paragraph to backend.md once T0.12 releases the file.
