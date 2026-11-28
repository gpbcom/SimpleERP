## Review note: T0.20 Typed API client package

**Verdict:** Approved. No blocking finding. There are 8 follow-ups.

### What changed

- There is a new pnpm package, `@simpleerp/api-client`. It takes its path types from the committed `platform` OpenAPI document through openapi-typescript and wraps openapi-fetch (both MIT). It ships its TypeScript source with no build step. Callers type their calls with path strings such as `client.GET('/v1/health')`.
- Every non-2xx answer rejects the call with a typed error, thrown from an openapi-fetch middleware. A problem+json body with a usable `code` becomes `ApiProblemError {code, status}`. Every other error answer becomes `ApiUnexpectedResponseError {status}`. The error is built only from the status, the content type and the problem body. The Request, its headers and the Response are never kept.
- `scripts/generate.mjs --check` fails when the committed `src/generated/platform.ts` differs from what the generator would write (prettier-formatted). A Vitest case runs it against the real `backend/services/platform/openapi.json`, so the package's `test` script fails in CI on a stale client.
- CI change detection: a change to `backend/services/<service>/openapi.json`, matched at that exact depth, now also selects every front-end project and image. A regenerated document alone therefore runs the stale check.
- The docs gain a client paragraph in `docs/technical/interfaces/api.md`, a selection sentence in `docs/technical/delivery/ci-cd-and-stages.md`, and a package README.

### Acceptance criteria

| # | Criterion | Evidence | Result |
|---|---|---|---|
| 1 | The document changes and the client is not regenerated, so CI or the build fails | `tests/generate/check-generated.test.ts`: "fails, names the stale file and the command..." and "keeps the committed platform client up to date with its OpenAPI document". `tests/ci/detect_changes/test_detect_changes.py::test_a_changed_openapi_document_selects_its_service_and_every_front_end`. `tests-evidences/test.txt` (api-client 54 passed), `tests-evidences/pytest.txt` | Met |
| 2 | A field is renamed and the client regenerated, so a caller still using the old name fails the type check | `tests/generate/renamed-field.test.ts`: "fails the type check of a caller still using the old name" (real tsc, strict) | Met |
| 3 | A problem+json refusal gives a typed error with the body's code | `tests/client/create-api-client.test.ts`: "rejects a problem+json refusal with its code and the HTTP status" (real local HTTP server). `tests/problem/to-api-error.test.ts`: content-type and code cases | Met |
| 4 | No secret appears in the typed error | `create-api-client.test.ts`: "keeps %s out of the error in every form" (Bearer token, body secrets). `to-api-error.test.ts`: "keeps %s out of every view...", "holds only the code and the status as own fields" | Met |

### What to look at first

- `frontend/packages/api-client/src/client/create-api-client.ts:20-37`: the middleware reads the body only for `application/problem+json` and passes no request data to the error. This is where the Authorization header is kept out.
- `frontend/packages/api-client/src/problem/to-api-error.ts:12-24`: the allow-list. Only `code`, trimmed, and the response status are copied. The body's `status` is ignored.
- `frontend/packages/api-client/src/problem/api-problem-error.ts:8` and `api-unexpected-response-error.ts:7`: `name` is non-enumerable, so own keys are exactly `code` and `status`.
- `frontend/packages/api-client/scripts/generate.mjs:47-50,66-71`: the formatting and the comparison behind the stale check.
- `.github/scripts/detect_changes.py:145-148,204`: `is_service_openapi` and its reuse of the front-end-package branch.
- Company data isolation and permissions: the client holds no company state. Headers (company, authorisation) are given by the caller and never copied into errors. Nothing here crosses companies.

### Assumptions accepted

- The code member is `code`. It matches `Problem.code` of `erp_context` and the platform's ProblemDetails.
- The committed document lives at `backend/services/<service>/openapi.json`. It is the only tracked OpenAPI file, from T0.18.
- Stricter-than-needed leak checks (title, stack) and treating unparseable problem bodies or bad generator input conservatively are in line with REQ-T05-03.
- No separate CI step for `check:generated`: typescript.yml runs the package's Vitest suite, which contains the check.
- The full list is in the structured result.

### Follow-ups

1. Carry D122's small support `reference` on `ApiProblemError` (validated like `code`). T0.23 criterion 1 needs it.
2. Call `code` "the code of the error pattern" rather than "support code", so it is not confused with `reference`.
3. Validate `code` against the error-pattern shape (`Problem.CODE_PATTERN`) before copying it.
4. `api.md`: only the platform document is generated today, not "each service's".
5. `ci-cd-and-stages.md:55`: re-wrap the long line to 120 columns.
6. Cancel unread error bodies in the middleware.
7. `renamed-field.test.ts`: use `process.execPath` instead of `node` from PATH.
8. Pin one shared prettier config so the editor hook and the generator always format alike.
