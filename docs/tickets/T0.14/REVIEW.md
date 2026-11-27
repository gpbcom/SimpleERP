# T0.14: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- New `platform` service (package `erp_platform`) with the four AGENT.md layers, `conf/app.yaml` (every default written, no host or port), `conf/logger.yaml`, and an `AppFactory.create()` that uvicorn serves with `--factory` (D406). It has no command line.
- `GET /v1/health` answers `{"status": "ok"}` and is the only path that needs no company. The erp_context `CompanyContextMiddleware` (T0.09) refuses every other path that has no company, with its `CONTEXT-COMPANY-01` problem.
- The service's own failures (404, 405, 422, 500) answer `application/problem+json` with a code from `conf/catalogs/error_codes.yaml`. The body is built only from catalogue keys, so no exception text can reach it.
- The image has two stages (build with `uv sync --locked --package platform --no-editable`, then a slim runtime run as a non-root user with a HEALTHCHECK) and is built from the repository root (D419, D438). Decision K20 copies the shared `refusal_codes.yaml` into the image's `conf/catalogs/`.
- `uv.lock` gains the `platform` member and its fastapi and uvicorn dependencies.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. The image built from the repository root builds and starts | `tests-evidences/pytest-backend-services-platform.txt` (`TestImage::test_the_health_call_answers_ok_after_the_start`, `test_the_container_is_still_running_after_the_calls`, run, not skipped). CI builds it through `images.yml` | ✅ Pass |
| 2. The health endpoint under `/v1` answers | `TestAppBuilder::test_health_answers_ok_without_a_company`, `TestAppFactory::test_uvicorn_serves_the_factory_and_ends_cleanly_on_sigterm`, `TestHealthRouter` | ✅ Pass |
| 3. A refused call answers problem+json with its D122 code | `TestProblemHandler` (404, 405, 422, 500 codes), `TestAppBuilder::test_a_request_without_a_company_is_refused_with_the_context_refusal`, `TestImage::test_a_call_without_a_company_is_refused_as_problem_json` | ✅ Pass |
| 4. No secret is in an error body | `TestProblemHandler::test_an_unexpected_exception_leaks_no_secret_in_the_body`, `TestAppBuilder::test_a_refusal_body_holds_only_problem_members_and_no_secret` | ✅ Pass |
| 5. A request without a company is refused | `TestAppBuilder::test_a_request_without_a_company_is_refused_with_the_context_refusal`, `TestImage::test_a_call_without_a_company_is_refused_as_problem_json` | ✅ Pass |
| 6. `tests/conventions/` passes with no change | `tests-evidences/pytest.txt` (1174 passed). The ticket's diff touches nothing in `tests/conventions/` | ✅ Pass |

## Look at first

- Company isolation: read `backend/services/platform/src/erp_platform/api/http/app_builder.py` (`build`) line by line. The middleware gets `public_paths` from config and matches them exactly, so `/v1/health` is the only open path. The middleware sits outside the exception handlers, so an unknown path without a company is refused (400), not answered 404.
- The refusal catalogue lookup (`_refusal_codes_path`, lines 65 to 70) and `backend/services/platform/Dockerfile:24`. The fallback path exists only in the source tree, and the image depends on the extra COPY (K20).
- The secret path: `backend/services/platform/src/erp_platform/api/http/problem_handler.py`. The body is clean. Under real uvicorn, though, Starlette re-raises after the 500 handler, so the traceback with its message reaches uvicorn's log (see follow-ups).
- The image: `backend/services/platform/Dockerfile` and `backend/services/platform/tests/image/test_image.py`. It runs as non-root uid 10001 and copies only `sdk/pyproject.toml` from the SDK, enough for `--locked`.

## Assumptions accepted

- The context middleware is erp_context's (T0.09): accepted, the only one there is, and it implements REQ-T01-02 criterion 1.
- The package is named `erp_platform`: accepted, because `platform` would shadow the standard library.
- The health path is `GET /v1/health`: accepted, the most conservative choice where the specifications name none.
- No budget is touched: accepted, `05-non-functional` sets none for this ticket.
- The roadmap's "factories" means `AppFactory`: accepted, the skeleton has no runnable (D406, AGENT.md).
- K20, the COPY of `refusal_codes.yaml` into the image: accepted for this ticket, and proved by the image test. It should become package data later.

## Follow-ups

- Platform problems drop the catalogue's `action` and `reference` that D122 requires and that erp_context's bodies carry.
- Every 4xx other than 404 and 405 gets `PLATFORM-INTERNAL-01`.
- The "no message reaches a log" claim does not hold under uvicorn, whose traceback log includes the exception message.
- Ship `refusal_codes.yaml` as erp_context package data, instead of the source-tree fallback and the Dockerfile COPY.
- The ProblemHandler note says a RefusalHandler is registered. It is not.
- The `public_paths` description says "bearer token" where it means "company".
- Move the module-level constants of `test_app_builder.py` into the class. Make the image fixture a classmethod.
- The import-group comments are misordered in several models and in `error_code_repository.py`.
