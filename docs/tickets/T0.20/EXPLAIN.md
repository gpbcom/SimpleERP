# T0.20: Typed API client package

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- A new front-end package, `@simpleerp/api-client`, gives the front ends a typed client of the platform API, with its types generated from the committed OpenAPI document.
- Every non-2xx answer rejects the call with a typed error: a problem+json refusal gives an error carrying the body's code and the HTTP status, and any other error answer gives an error carrying only the status. No secret reaches either error.
- A stale client fails the package's tests, so CI fails when the OpenAPI document changes and the client is not regenerated. A renamed field fails the type check of a caller that still uses the old name.
- CI change detection selects every front end when a service's committed OpenAPI document changes, so the stale check runs on a regenerated document alone.

## ⚙️ How it works

1. **Generate the types:** the script reads the OpenAPI document, runs openapi-typescript, prepends a header and formats the text with prettier, in [`frontend/packages/api-client/scripts/generate.mjs:45-51`](../../../frontend/packages/api-client/scripts/generate.mjs#L45-L51). The `generate` and `check:generated` scripts point it at the platform document and at the committed `src/generated/platform.ts` ([`frontend/packages/api-client/package.json:21-22`](../../../frontend/packages/api-client/package.json#L21-L22)).
2. **Check the committed client:** with `--check` the script compares the whole generated text with the file and exits 1 with the regenerate command when they differ, in [`frontend/packages/api-client/scripts/generate.mjs:74-79`](../../../frontend/packages/api-client/scripts/generate.mjs#L74-L79). Bad arguments or an unreadable document exit 2 ([`frontend/packages/api-client/scripts/generate.mjs:58-73`](../../../frontend/packages/api-client/scripts/generate.mjs#L58-L73)).
3. **Run the check in CI:** a Vitest case runs the check against the real platform document ([`frontend/packages/api-client/tests/generate/check-generated.test.ts`](../../../frontend/packages/api-client/tests/generate/check-generated.test.ts)), and the package `test` script is run by the TypeScript workflow ([`frontend/packages/api-client/package.json:20`](../../../frontend/packages/api-client/package.json#L20)).
4. **Select the front ends:** `is_service_openapi` matches `backend/services/<service>/openapi.json` at that exact depth ([`.github/scripts/detect_changes.py:145-148`](../../../.github/scripts/detect_changes.py#L145-L148)), and the main loop treats it like a change under `frontend/packages/` ([`.github/scripts/detect_changes.py:204`](../../../.github/scripts/detect_changes.py#L204)).
5. **Create the client:** `createApiClient` builds an openapi-fetch client typed with the generated `paths`, then registers the rejecting middleware, in [`frontend/packages/api-client/src/client/create-api-client.ts:48-56`](../../../frontend/packages/api-client/src/client/create-api-client.ts#L48-L56).
6. **Reject a non-2xx answer:** the middleware lets a 2xx pass, otherwise reads the content type and the body and throws `toApiError(...)`, in [`frontend/packages/api-client/src/client/create-api-client.ts:33-42`](../../../frontend/packages/api-client/src/client/create-api-client.ts#L33-L42).
7. **Read the body:** the body is parsed as JSON only for `application/problem+json`, and an invalid body gives nothing, in [`frontend/packages/api-client/src/client/create-api-client.ts:21-31`](../../../frontend/packages/api-client/src/client/create-api-client.ts#L21-L31).
8. **Map to a typed error:** `toApiError` is the allow-list. It copies only the trimmed `code` member of an object body of the right media type, and the response status, in [`frontend/packages/api-client/src/problem/to-api-error.ts:12-25`](../../../frontend/packages/api-client/src/problem/to-api-error.ts#L12-L25). The member name is the constant at [`frontend/packages/api-client/src/problem/to-api-error.ts:5`](../../../frontend/packages/api-client/src/problem/to-api-error.ts#L5).
9. **Build the error:** [`frontend/packages/api-client/src/problem/api-problem-error.ts:2-11`](../../../frontend/packages/api-client/src/problem/api-problem-error.ts#L2-L11) holds `code` and `status`, and [`frontend/packages/api-client/src/problem/api-unexpected-response-error.ts:2-9`](../../../frontend/packages/api-client/src/problem/api-unexpected-response-error.ts#L2-L9) holds `status`. Both make `name` non-enumerable, so their own keys are exactly the allowed fields and their JSON leaks nothing.
10. **Export:** the public surface is in [`frontend/packages/api-client/src/index.ts`](../../../frontend/packages/api-client/src/index.ts).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py) | Modified | [24-27](../../../.github/scripts/detect_changes.py#L24), [51](../../../.github/scripts/detect_changes.py#L51), [145-150](../../../.github/scripts/detect_changes.py#L145), [204](../../../.github/scripts/detect_changes.py#L204) | +12 | −1 |
| [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) | Modified | [60](../../../docs/technical/delivery/ci-cd-and-stages.md#L60) | +1 | −1 |
| [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) | Modified | [48-53](../../../docs/technical/interfaces/api.md#L48) | +6 | −0 |
| [`frontend/packages/api-client/README.md`](../../../frontend/packages/api-client/README.md) | Added | [1-85](../../../frontend/packages/api-client/README.md#L1) | +85 | −0 |
| [`frontend/packages/api-client/eslint.config.js`](../../../frontend/packages/api-client/eslint.config.js) | Added | [1-11](../../../frontend/packages/api-client/eslint.config.js#L1) | +11 | −0 |
| [`frontend/packages/api-client/package.json`](../../../frontend/packages/api-client/package.json) | Added | [1-37](../../../frontend/packages/api-client/package.json#L1) | +37 | −0 |
| [`frontend/packages/api-client/scripts/generate.mjs`](../../../frontend/packages/api-client/scripts/generate.mjs) | Added | [1-87](../../../frontend/packages/api-client/scripts/generate.mjs#L1) | +87 | −0 |
| [`frontend/packages/api-client/src/client/create-api-client.ts`](../../../frontend/packages/api-client/src/client/create-api-client.ts) | Added | [1-56](../../../frontend/packages/api-client/src/client/create-api-client.ts#L1) | +56 | −0 |
| [`frontend/packages/api-client/src/generated/platform.ts`](../../../frontend/packages/api-client/src/generated/platform.ts) | Added | [1-84](../../../frontend/packages/api-client/src/generated/platform.ts#L1) | +84 | −0 |
| [`frontend/packages/api-client/src/index.ts`](../../../frontend/packages/api-client/src/index.ts) | Added | [1-6](../../../frontend/packages/api-client/src/index.ts#L1) | +6 | −0 |
| [`frontend/packages/api-client/src/problem/api-problem-error.ts`](../../../frontend/packages/api-client/src/problem/api-problem-error.ts) | Added | [1-12](../../../frontend/packages/api-client/src/problem/api-problem-error.ts#L1) | +12 | −0 |
| [`frontend/packages/api-client/src/problem/api-unexpected-response-error.ts`](../../../frontend/packages/api-client/src/problem/api-unexpected-response-error.ts) | Added | [1-10](../../../frontend/packages/api-client/src/problem/api-unexpected-response-error.ts#L1) | +10 | −0 |
| [`frontend/packages/api-client/src/problem/to-api-error.ts`](../../../frontend/packages/api-client/src/problem/to-api-error.ts) | Added | [1-25](../../../frontend/packages/api-client/src/problem/to-api-error.ts#L1) | +25 | −0 |
| [`frontend/packages/api-client/tests/client/create-api-client.test.ts`](../../../frontend/packages/api-client/tests/client/create-api-client.test.ts) | Added | [1-92](../../../frontend/packages/api-client/tests/client/create-api-client.test.ts#L1) | +92 | −0 |
| [`frontend/packages/api-client/tests/fixtures/check/openapi-v1.json`](../../../frontend/packages/api-client/tests/fixtures/check/openapi-v1.json) | Added | [1-25](../../../frontend/packages/api-client/tests/fixtures/check/openapi-v1.json#L1) | +25 | −0 |
| [`frontend/packages/api-client/tests/fixtures/check/openapi-v2.json`](../../../frontend/packages/api-client/tests/fixtures/check/openapi-v2.json) | Added | [1-25](../../../frontend/packages/api-client/tests/fixtures/check/openapi-v2.json#L1) | +25 | −0 |
| [`frontend/packages/api-client/tests/fixtures/renamed/openapi-after.json`](../../../frontend/packages/api-client/tests/fixtures/renamed/openapi-after.json) | Added | [1-28](../../../frontend/packages/api-client/tests/fixtures/renamed/openapi-after.json#L1) | +28 | −0 |
| [`frontend/packages/api-client/tests/fixtures/renamed/openapi-before.json`](../../../frontend/packages/api-client/tests/fixtures/renamed/openapi-before.json) | Added | [1-28](../../../frontend/packages/api-client/tests/fixtures/renamed/openapi-before.json#L1) | +28 | −0 |
| [`frontend/packages/api-client/tests/generate/check-generated.test.ts`](../../../frontend/packages/api-client/tests/generate/check-generated.test.ts) | Added | [1-75](../../../frontend/packages/api-client/tests/generate/check-generated.test.ts#L1) | +75 | −0 |
| [`frontend/packages/api-client/tests/generate/renamed-field.test.ts`](../../../frontend/packages/api-client/tests/generate/renamed-field.test.ts) | Added | [1-80](../../../frontend/packages/api-client/tests/generate/renamed-field.test.ts#L1) | +80 | −0 |
| [`frontend/packages/api-client/tests/helpers/problem-server.ts`](../../../frontend/packages/api-client/tests/helpers/problem-server.ts) | Added | [1-56](../../../frontend/packages/api-client/tests/helpers/problem-server.ts#L1) | +56 | −0 |
| [`frontend/packages/api-client/tests/problem/api-problem-error.test.ts`](../../../frontend/packages/api-client/tests/problem/api-problem-error.test.ts) | Added | [1-49](../../../frontend/packages/api-client/tests/problem/api-problem-error.test.ts#L1) | +49 | −0 |
| [`frontend/packages/api-client/tests/problem/to-api-error.test.ts`](../../../frontend/packages/api-client/tests/problem/to-api-error.test.ts) | Added | [1-96](../../../frontend/packages/api-client/tests/problem/to-api-error.test.ts#L1) | +96 | −0 |
| [`frontend/packages/api-client/tsconfig.json`](../../../frontend/packages/api-client/tsconfig.json) | Added | [1-10](../../../frontend/packages/api-client/tsconfig.json#L1) | +10 | −0 |
| [`frontend/packages/api-client/vitest.config.ts`](../../../frontend/packages/api-client/vitest.config.ts) | Added | [1-9](../../../frontend/packages/api-client/vitest.config.ts#L1) | +9 | −0 |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Modified | [87-117](../../../pnpm-lock.yaml#L87), [595-604](../../../pnpm-lock.yaml#L595), [944-947](../../../pnpm-lock.yaml#L944), [954-957](../../../pnpm-lock.yaml#L954), [970-972](../../../pnpm-lock.yaml#L970), [1008-1010](../../../pnpm-lock.yaml#L1008), [1027-1029](../../../pnpm-lock.yaml#L1027), [1057-1059](../../../pnpm-lock.yaml#L1057), [1071-1073](../../../pnpm-lock.yaml#L1071), [1361-1364](../../../pnpm-lock.yaml#L1361), [1381-1384](../../../pnpm-lock.yaml#L1381), [1486-1489](../../../pnpm-lock.yaml#L1486), [1493-1496](../../../pnpm-lock.yaml#L1493), [1509-1511](../../../pnpm-lock.yaml#L1509), [1644-1647](../../../pnpm-lock.yaml#L1644), [1710-1721](../../../pnpm-lock.yaml#L1710), [1734-1737](../../../pnpm-lock.yaml#L1734), [1798-1801](../../../pnpm-lock.yaml#L1798), [1818-1822](../../../pnpm-lock.yaml#L1818), [1859-1862](../../../pnpm-lock.yaml#L1859), [1931-1934](../../../pnpm-lock.yaml#L1931), [1981-1984](../../../pnpm-lock.yaml#L1981), [2055-2057](../../../pnpm-lock.yaml#L2055), [2257-2263](../../../pnpm-lock.yaml#L2257), [2411](../../../pnpm-lock.yaml#L2411), [2496-2518](../../../pnpm-lock.yaml#L2496), [2661](../../../pnpm-lock.yaml#L2661), [2672](../../../pnpm-lock.yaml#L2672), [2691](../../../pnpm-lock.yaml#L2691), [2707](../../../pnpm-lock.yaml#L2707), [2878-2879](../../../pnpm-lock.yaml#L2878), [2889-2890](../../../pnpm-lock.yaml#L2889), [2899-2900](../../../pnpm-lock.yaml#L2899), [2937-2938](../../../pnpm-lock.yaml#L2937), [2953-2956](../../../pnpm-lock.yaml#L2953), [2993-2994](../../../pnpm-lock.yaml#L2993), [3005-3006](../../../pnpm-lock.yaml#L3005), [3035](../../../pnpm-lock.yaml#L3035), [3038-3039](../../../pnpm-lock.yaml#L3038), [3192](../../../pnpm-lock.yaml#L3192), [3345-3351](../../../pnpm-lock.yaml#L3345), [3360-3361](../../../pnpm-lock.yaml#L3360), [3466-3467](../../../pnpm-lock.yaml#L3466), [3470-3473](../../../pnpm-lock.yaml#L3470), [3499-3500](../../../pnpm-lock.yaml#L3499), [3606-3609](../../../pnpm-lock.yaml#L3606), [3662-3677](../../../pnpm-lock.yaml#L3662), [3695-3700](../../../pnpm-lock.yaml#L3695), [3754-3755](../../../pnpm-lock.yaml#L3754), [3770-3771](../../../pnpm-lock.yaml#L3770), [3808-3809](../../../pnpm-lock.yaml#L3808), [3909-3910](../../../pnpm-lock.yaml#L3909), [3952-3953](../../../pnpm-lock.yaml#L3952), [3994-3995](../../../pnpm-lock.yaml#L3994), [4055](../../../pnpm-lock.yaml#L4055), [4170-4173](../../../pnpm-lock.yaml#L4170) | +242 | −8 |
| [`tests/ci/detect_changes/helpers.py`](../../../tests/ci/detect_changes/helpers.py) | Modified | [5](../../../tests/ci/detect_changes/helpers.py#L5), [32](../../../tests/ci/detect_changes/helpers.py#L32), [87-91](../../../tests/ci/detect_changes/helpers.py#L87) | +7 | −0 |
| [`tests/ci/detect_changes/test_detect_changes.py`](../../../tests/ci/detect_changes/test_detect_changes.py) | Modified | [17](../../../tests/ci/detect_changes/test_detect_changes.py#L17), [30](../../../tests/ci/detect_changes/test_detect_changes.py#L30), [132-176](../../../tests/ci/detect_changes/test_detect_changes.py#L132) | +47 | −0 |
| **28 files** | | | **+1301** | **−10** |
<!-- /changes -->

- [`frontend/packages/api-client/package.json`](../../../frontend/packages/api-client/package.json), [`frontend/packages/api-client/tsconfig.json`](../../../frontend/packages/api-client/tsconfig.json), [`frontend/packages/api-client/eslint.config.js`](../../../frontend/packages/api-client/eslint.config.js), [`frontend/packages/api-client/vitest.config.ts`](../../../frontend/packages/api-client/vitest.config.ts), [`pnpm-lock.yaml`](../../../pnpm-lock.yaml): the new pnpm package, exporting its source ([`frontend/packages/api-client/package.json:10-16`](../../../frontend/packages/api-client/package.json#L10-L16)), with pinned dependencies and the node test environment.
- [`frontend/packages/api-client/scripts/generate.mjs`](../../../frontend/packages/api-client/scripts/generate.mjs): the generator and its `--check` mode.
- [`frontend/packages/api-client/src/generated/platform.ts`](../../../frontend/packages/api-client/src/generated/platform.ts): the generated types of the platform document, never edited by hand.
- [`frontend/packages/api-client/src/client/create-api-client.ts`](../../../frontend/packages/api-client/src/client/create-api-client.ts), [`frontend/packages/api-client/src/problem/to-api-error.ts`](../../../frontend/packages/api-client/src/problem/to-api-error.ts), [`frontend/packages/api-client/src/problem/api-problem-error.ts`](../../../frontend/packages/api-client/src/problem/api-problem-error.ts), [`frontend/packages/api-client/src/problem/api-unexpected-response-error.ts`](../../../frontend/packages/api-client/src/problem/api-unexpected-response-error.ts), [`frontend/packages/api-client/src/index.ts`](../../../frontend/packages/api-client/src/index.ts): the client and its two typed errors.
- [`frontend/packages/api-client/tests/problem/to-api-error.test.ts`](../../../frontend/packages/api-client/tests/problem/to-api-error.test.ts), [`frontend/packages/api-client/tests/problem/api-problem-error.test.ts`](../../../frontend/packages/api-client/tests/problem/api-problem-error.test.ts), [`frontend/packages/api-client/tests/client/create-api-client.test.ts`](../../../frontend/packages/api-client/tests/client/create-api-client.test.ts), [`frontend/packages/api-client/tests/helpers/problem-server.ts`](../../../frontend/packages/api-client/tests/helpers/problem-server.ts): the mapping, the leak checks over five views, and the client against a real local HTTP server.
- [`frontend/packages/api-client/tests/generate/check-generated.test.ts`](../../../frontend/packages/api-client/tests/generate/check-generated.test.ts), [`frontend/packages/api-client/tests/generate/renamed-field.test.ts`](../../../frontend/packages/api-client/tests/generate/renamed-field.test.ts), the fixtures [`frontend/packages/api-client/tests/fixtures/check/openapi-v1.json`](../../../frontend/packages/api-client/tests/fixtures/check/openapi-v1.json), [`frontend/packages/api-client/tests/fixtures/check/openapi-v2.json`](../../../frontend/packages/api-client/tests/fixtures/check/openapi-v2.json), [`frontend/packages/api-client/tests/fixtures/renamed/openapi-before.json`](../../../frontend/packages/api-client/tests/fixtures/renamed/openapi-before.json) and [`frontend/packages/api-client/tests/fixtures/renamed/openapi-after.json`](../../../frontend/packages/api-client/tests/fixtures/renamed/openapi-after.json): the generator as a child process, the stale check and a real `tsc` run on a renamed field (acceptance criteria 1 and 2).
- [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py), lines [`24-27`](../../../.github/scripts/detect_changes.py#L24-L27), [`51`](../../../.github/scripts/detect_changes.py#L51), [`145-148`](../../../.github/scripts/detect_changes.py#L145-L148) and [`204`](../../../.github/scripts/detect_changes.py#L204): the OpenAPI selection rule.
- [`tests/ci/detect_changes/helpers.py`](../../../tests/ci/detect_changes/helpers.py) and [`tests/ci/detect_changes/test_detect_changes.py`](../../../tests/ci/detect_changes/test_detect_changes.py): the tests of that rule, including the nested-name negatives and a repository with no front end.
- [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md), [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) and [`frontend/packages/api-client/README.md`](../../../frontend/packages/api-client/README.md): the selection rule, the client paragraph, and the package's usage, errors and regeneration.

## 🧪 How to test it

```bash
pnpm install
pnpm --filter ./frontend/packages/api-client run lint
pnpm --filter ./frontend/packages/api-client run typecheck
pnpm --filter ./frontend/packages/api-client run test
pnpm --filter ./frontend/packages/api-client run check:generated
uv run pytest tests/ci/detect_changes -n 2
```

The last command shows the CI selection rule. `check:generated` exits 0 on the committed client and 1 once the document differs.

## 🔗 Evidence

- [Lint](tests-evidences/lint.txt): the package lint output.
- [Type check](tests-evidences/typecheck.txt): the package type check output.
- [Vitest](tests-evidences/test.txt): the package suite, 54 tests passed.
- [Pytest](tests-evidences/pytest.txt): the detect_changes tests.
- [Ruff check](tests-evidences/ruff-check.txt) and [ruff format](tests-evidences/ruff-format.txt): the Python changes.
- [Mypy](tests-evidences/mypy.txt): the Python type check.
- [Install](tests-evidences/pnpm-install.txt): the pnpm install.
- [Plan view](tests-evidences/plan-view.txt) and [ticket references](tests-evidences/ticket-refs.txt): the plan and ticket checks.

## 📝 Assumptions accepted

- The problem+json member carrying the error-pattern code is `code`, as `Problem.code` of the shared context and the platform's ProblemDetails say.
- The constructor signatures `new ApiProblemError(code, status)` and `new ApiUnexpectedResponseError(status)` are internal choices.
- The messages name the code and status only. The code is a catalogue code, not a secret.
- The title and the stack of a body count as values that must not reach the error, which is stricter than REQ-T05-03.
- The JSON of an unexpected-response error is exactly `{"status":500}`, with `name` non-enumerable.
- The health path is `/v1/health` with body `{status: 'ok'}`, as the platform document says, and non-2xx calls reject.
- The committed document is `backend/services/<service>/openapi.json`, the only tracked OpenAPI file, from T0.18, and the committed client is `src/generated/platform.ts`.
- prettier 3.10.1 formats the generated file and `--check` compares the whole text, header included. The versions of eslint, globals and prettier match the lock, and [`pnpm-workspace.yaml`](../../../pnpm-workspace.yaml) already covers `frontend/packages/*`.
- Unreadable or invalid generator input exits 2, and a problem+json body that is not valid JSON becomes an unexpected-response error, both conservative.
- The extra exports `ApiClientOptions`, `PlatformClient` and `PROBLEM_CODE_MEMBER` are small public types.
- The CI page states the path pattern `detect_changes.py` matches, and the staleness check runs in the Vitest suite that `typescript.yml` runs, so no separate CI step is needed.
- `http://localhost:8000` in the README is the laptop uvicorn example of AGENT.md, and the README link to `api.md#http` resolves.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`frontend/packages/api-client/src/problem/api-problem-error.ts`](../../../frontend/packages/api-client/src/problem/api-problem-error.ts), [`frontend/packages/api-client/src/problem/to-api-error.ts`](../../../frontend/packages/api-client/src/problem/to-api-error.ts) | The allow-list keeps only `code` and `status`, but D122 also has a small support `reference`. T0.23 criterion 1 needs it: add it to `ApiProblemError`, check it against `Problem.CODE_PATTERN`, and extend the leak tests. |
| [`frontend/packages/api-client/README.md`](../../../frontend/packages/api-client/README.md), [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) | Call `code` "the code of the error pattern (D122)", not "the support code", so it is not confused with `reference`. |
| [`frontend/packages/api-client/src/problem/to-api-error.ts`](../../../frontend/packages/api-client/src/problem/to-api-error.ts) | Any non-empty string is accepted as the code. Accept only the error-pattern shape (`^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-[0-9]{2}$`), map the rest to the unexpected-response error, and add a test. |
| [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) | Say that only the platform document is generated today, and that other services are added the same way later. |
| [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) | Re-wrap the new long sentence of the paragraph to 120 columns. |
| [`frontend/packages/api-client/src/client/create-api-client.ts`](../../../frontend/packages/api-client/src/client/create-api-client.ts) | Cancel an unread error body (`response.body?.cancel()`) so the connection is released at once. |
| [`frontend/packages/api-client/tests/generate/renamed-field.test.ts`](../../../frontend/packages/api-client/tests/generate/renamed-field.test.ts) | Spawn `process.execPath` instead of `node` from PATH, as the check test does. |
| [`frontend/packages/api-client/package.json`](../../../frontend/packages/api-client/package.json) | Pin one shared prettier config, for example from `@simpleerp/config`, so the editor hook and the generator always format alike. |
