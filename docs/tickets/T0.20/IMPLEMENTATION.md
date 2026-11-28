# T0.20: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- A stale generated client must fail CI or the build, and a renamed field must fail the caller's type check (acceptance criteria 1 and 2 of [TICKET.md](TICKET.md)).
- A problem+json refusal gives a typed error with the body's code, and no secret appears in it (criteria 3 and 4, REQ-T05-03).
- Clients are generated from the OpenAPI document ([D406](../../specs/06-decisions/technical/d406-back-end.md)), and shared TypeScript packages live under `frontend/packages/<pkg>` ([D438](../../specs/06-decisions/technical/d438-repository-layout.md)).
- The front ends are Vue 3 with TypeScript and Vite ([D407](../../specs/06-decisions/technical/d407-front-end.md)), and the roadmap names no generator, so the licence and the supply-chain rules of the specifications decide.
- Python code follows [AGENT.md](../../../AGENT.md) (no nested function, one class per file, typing). The CI selection is in [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py).
- Front-end tests run in the package's own Vitest suite, which the TypeScript workflow runs.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Generator and runtime | openapi-typescript with openapi-fetch | openapi-generator, orval, @hey-api/openapi-ts | No per-operation functions: callers use path strings |
| [D2](#d2) | How errors reach the caller | A middleware that throws | A Proxy around the methods, or returning `{error}` | Relies on openapi-fetch letting a middleware error propagate |
| [D3](#d3) | What the typed error keeps | An allow-list of `code` and `status`, with `name` non-enumerable | Keep the response or the request | Stricter than needed, and no `reference` yet |
| [D4](#d4) | How a stale client is detected | A `--check` mode run by a Vitest case | A separate CI step | The check hides in the test suite |
| [D5](#d5) | How the package is shipped | TypeScript source, no build step | A `dist` build as `@simpleerp/ui` | Only Vite consumers work |
| [D6](#d6) | CI selection of an OpenAPI change | A depth-exact predicate that reuses the front-end branch | Add the file to `SHARED_FILES` | A new rule to maintain |
| [D7](#d7) | Formatting of the generated file | prettier through its API, as a package dependency | Raw output, or prettier at the root | One more dependency and an open config question |
| [D8](#d8) | How the tests run the generator | Child processes (`node`, `tsc`) in temp folders | In-process calls or Vitest typecheck mode | Slower, with a 60 s timeout |
| [D9](#d9) | Test server and leak checks | A real local HTTP server and five views per secret | Mocks, or checking the message only | More test cases |
| [D10](#d10) | Documentation and the `name` field details | One README, one paragraph per page, `name` via `defineProperty` | New sections, plain `this.name` | Longer paragraphs |

## <a id="d1"></a>D1: Generator and runtime

**Chosen:** openapi-typescript 7.13.0 with openapi-fetch 0.17.0 · **Where:** [`frontend/packages/api-client/package.json:24-33`](../../../frontend/packages/api-client/package.json#L24-L33) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ openapi-typescript and openapi-fetch | Types only, a runtime of about 6 kB, no generated runtime code to review, both MIT | No generated per-operation functions: callers pass path strings typed by the generated `paths` |
| openapi-generator | A well-known generator | Generates more code, and needs a JVM |
| orval | Generates operation functions | Generates more code to review |
| @hey-api/openapi-ts | Generates operation functions | Generates more code to review |

**Trade-off:** callers write `client.GET('/v1/health')` rather than a named function, in exchange for a small, reviewable output.

**Revisit when:** callers need generated operation functions or hooks.

## <a id="d2"></a>D2: How errors reach the caller

**Chosen:** an openapi-fetch middleware that throws in `onResponse` · **Where:** [`frontend/packages/api-client/src/client/create-api-client.ts:33-42`](../../../frontend/packages/api-client/src/client/create-api-client.ts#L33-L42) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Throwing middleware | Keeps the openapi-fetch types, and every method rejects the same way (the brief says non-2xx rejects) | Depends on openapi-fetch letting the error propagate, which the tests confirm |
| A Proxy around the client methods | Full control of each call | Loses the library's typing and adds code |
| Return `{error}` and let callers check | Library default | A caller who forgets the check ignores the refusal, and the brief fixes rejection |

**Trade-off:** coupling to a middleware behaviour of the library, covered by [`frontend/packages/api-client/tests/client/create-api-client.test.ts`](../../../frontend/packages/api-client/tests/client/create-api-client.test.ts).

**Revisit when:** an openapi-fetch upgrade changes how middleware errors propagate.

## <a id="d3"></a>D3: What the typed error keeps

**Chosen:** only `code` (trimmed) and the response status, read from the status, the content type and the body, never the Request or Response · **Where:** [`frontend/packages/api-client/src/problem/to-api-error.ts:12-25`](../../../frontend/packages/api-client/src/problem/to-api-error.ts#L12-L25), [`frontend/packages/api-client/src/client/create-api-client.ts:21-31`](../../../frontend/packages/api-client/src/client/create-api-client.ts#L21-L31) · **Source:** K01, K09, K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Allow-list of `code` and `status` | No `Authorization` header or body text can leak (criterion 4, REQ-T05-03) | The support `reference` of D122 is not carried yet, a follow-up |
| Keep the Response or Request on the error | More detail for callers | The request headers, including `Authorization`, would be reachable |
| Always try to parse JSON | Reads more bodies | Reads HTML or other bodies for nothing |

**Trade-off:** the leak checks are stricter than REQ-T05-03 (the title and the stack of a body count too), and an unparseable problem body becomes an unexpected-response error. Both are conservative. The `name` is defined with `Object.defineProperty`, non-enumerable ([`frontend/packages/api-client/src/problem/api-problem-error.ts:8`](../../../frontend/packages/api-client/src/problem/api-problem-error.ts#L8)), because `this.name = ...` would add an own enumerable key and break the exact-keys and `{"status":500}` tests; an `override get name()` was the other option (K09, no reason recorded against it beyond the chosen one fitting).

**Revisit when:** T0.23 needs the `reference`, or the code is validated against the error-pattern shape (both follow-ups).

## <a id="d4"></a>D4: How a stale client is detected

**Chosen:** `generate.mjs --check` compares the whole generated text with the committed file, and a Vitest case runs it on the real platform document · **Where:** [`frontend/packages/api-client/scripts/generate.mjs:74-79`](../../../frontend/packages/api-client/scripts/generate.mjs#L74-L79), [`frontend/packages/api-client/tests/generate/check-generated.test.ts`](../../../frontend/packages/api-client/tests/generate/check-generated.test.ts) · **Source:** PLAN, K03, K08, K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Check inside the Vitest suite | `typescript.yml` already runs the package's tests, so no workflow change | The check is not a named CI step |
| A separate CI step | Visible by name | Needs a workflow change, and the reviewer judged none necessary |

The script is a plain ES module with manual argument parsing (exit 2 and a usage message on bad input), not `node:util parseArgs` or commander: a few more lines, no dependency (K08).

**Trade-off:** a failure shows as a failed test, not a failed named step.

**Revisit when:** more services are generated and the check deserves its own CI job.

## <a id="d5"></a>D5: How the package is shipped

**Chosen:** export the TypeScript source, with no build step · **Where:** [`frontend/packages/api-client/package.json:10-16`](../../../frontend/packages/api-client/package.json#L10-L16) · **Source:** K06

| Option | For | Against |
| --- | --- | --- |
| ✅ Source export | Simpler, and Vite apps compile it directly | Only Vite consumers work |
| A `dist` build with a development export condition, as `@simpleerp/ui` does | Works for any consumer | A build step to maintain |

**Trade-off:** acceptable because every consumer is a Vite app ([D407](../../specs/06-decisions/technical/d407-front-end.md)).

**Revisit when:** a non-Vite consumer, such as a Node service, imports it.

## <a id="d6"></a>D6: CI selection of an OpenAPI change

**Chosen:** `is_service_openapi`, an exact four-part path match, reusing the `frontend/packages` branch · **Where:** [`.github/scripts/detect_changes.py:145-148`](../../../.github/scripts/detect_changes.py#L145-L148), [`.github/scripts/detect_changes.py:204`](../../../.github/scripts/detect_changes.py#L204) · **Source:** K07

| Option | For | Against |
| --- | --- | --- |
| ✅ Predicate with exact depth | Covers any future service, ignores nested files named `openapi.json`, selects only front ends and images besides the service | A rule to document and test |
| A regex constant | Compact | K07 preferred the readable predicate (no other reason recorded) |
| Add the document to `SHARED_FILES` | One line | Selects everything, Python packages included |

**Trade-off:** documented in [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) and tested in [`tests/ci/detect_changes/test_detect_changes.py`](../../../tests/ci/detect_changes/test_detect_changes.py). The no-front-end case builds its repository by removing `frontend/` from `write_repo` ([`tests/ci/detect_changes/helpers.py:87-89`](../../../tests/ci/detect_changes/helpers.py#L87-L89)), so it cannot drift from the fixture, at the cost of writing then deleting files (K05).

**Revisit when:** the document is published elsewhere than `backend/services/<service>/openapi.json`.

## <a id="d7"></a>D7: Formatting of the generated file

**Chosen:** format with prettier's API, `resolveConfig` for the output path, prettier 3.10.1 as a devDependency of the package · **Where:** [`frontend/packages/api-client/scripts/generate.mjs:45-51`](../../../frontend/packages/api-client/scripts/generate.mjs#L45-L51), [`frontend/packages/api-client/package.json:33`](../../../frontend/packages/api-client/package.json#L33) · **Source:** K06, K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Prettier API, per-package dependency | The editor hook's prettier run leaves the file unchanged, so `--check` is stable; the root [`package.json`](../../../package.json) was outside the task's files | One more entry in the lock |
| Raw openapi-typescript output | No dependency | The editor hook would reformat it and `--check` would drift |
| Prettier at the workspace root | One copy | Outside the task's files |
| The prettier CLI as a child process | Same result | A process per run (no reason recorded beyond the API choice) |

**Trade-off:** the package has no prettier config, so defaults format the generated file while hand-written sources use single quotes and no semicolons.

**Revisit when:** a shared prettier config is added (follow-up).

## <a id="d8"></a>D8: How the tests run the generator and the compiler

**Chosen:** child processes in a temp folder per test, with a strict `tsconfig` · **Where:** [`frontend/packages/api-client/tests/generate/check-generated.test.ts:10-35`](../../../frontend/packages/api-client/tests/generate/check-generated.test.ts#L10-L35), [`frontend/packages/api-client/tests/generate/renamed-field.test.ts:15`](../../../frontend/packages/api-client/tests/generate/renamed-field.test.ts#L15) · **Source:** K03, K04

| Option | For | Against |
| --- | --- | --- |
| ✅ `spawnSync` of node and the package's `tsc` | Tests the real exit codes, stderr and a real type failure | Slower, hence the 60 s timeout ([`frontend/packages/api-client/vitest.config.ts:5-8`](../../../frontend/packages/api-client/vitest.config.ts#L5-L8)) |
| Import the generator, or the compiler API in-process | Faster | Does not exercise the exit codes the brief fixes |
| Vitest typecheck mode | Built in | Not chosen by K04, no further reason recorded |
| One shared temp folder | Less I/O | Cases would depend on each other |

Outputs go to the OS temp folder, outside the workspace, which keeps the tree clean. The failing rename case is its own test because it also asserts the compiler names `displayName`.

**Trade-off:** more time per run. `renamed-field.test.ts` spawns `node` from PATH, not `process.execPath` (a follow-up).

**Revisit when:** the suite grows slow.

## <a id="d9"></a>D9: Test server and leak checks

**Chosen:** `ProblemServer`, a real server on `127.0.0.1` port 0 with one current reply, `closeAllConnections()` before `close()`, and a `const` holder object, and leak checks over five views per secret · **Where:** [`frontend/packages/api-client/tests/helpers/problem-server.ts:27-55`](../../../frontend/packages/api-client/tests/helpers/problem-server.ts#L27-L55), [`frontend/packages/api-client/tests/client/create-api-client.test.ts:70-86`](../../../frontend/packages/api-client/tests/client/create-api-client.test.ts#L70-L86) · **Source:** K01, K02

| Option | For | Against |
| --- | --- | --- |
| ✅ Real local server, one reply at a time | No mock ([AGENT.md](../../../AGENT.md) prefers real things); each test makes one call | A multi-call test would need a reply queue |
| A queue of replies | Multi-call tests | Not needed today |
| `server.close()` only | Shorter | Keep-alive connections of fetch make `afterEach` hang |
| `let` instead of the holder | Shorter | A `prefer-const` lint error, and a suppression was the alternative |
| Check the message only | Simpler | Misses `JSON.stringify`, `String`, `Object.values` and `Object.keys` |

The checks run with `it.each` per secret, so a failure names the leaking secret. `toApiError` is also tested directly with `(status, contentType, body)`, with no `Response` and no network ([`frontend/packages/api-client/tests/problem/to-api-error.test.ts:73`](../../../frontend/packages/api-client/tests/problem/to-api-error.test.ts#L73)).

**Trade-off:** more cases, and tests stricter than needed for the unexpected-response error.

**Revisit when:** a test needs several replies in sequence.

## <a id="d10"></a>D10: Documentation placement

**Chosen:** the error table and the D122 wording in the README, a bold paragraph in `api.md` before the refusals paragraph, and one sentence inside the existing selection paragraph of the CI page · **Where:** [`docs/technical/interfaces/api.md:48-53`](../../../docs/technical/interfaces/api.md#L48-L53), [`docs/technical/delivery/ci-cd-and-stages.md:60`](../../../docs/technical/delivery/ci-cd-and-stages.md#L60), [`frontend/packages/api-client/README.md`](../../../frontend/packages/api-client/README.md) · **Source:** K10, K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Table and short paragraphs | Quick to scan; keeps the pages' structure and the brief's "a few lines" | The table must follow the classes; the CI paragraph is longer (a re-wrap follow-up) |
| New H2 sections, or a bullet list of every rule | Visible | A larger change than the brief named |
| Prose only, or duplicating the logic in the README | No table to maintain | Harder to scan, or drifts from the code |

**Trade-off:** the README and the pages must be kept in step with the code.

**Revisit when:** the error classes change, for example when `reference` is added.

## 📝 Assumptions behind the choices

- The committed document lives at `backend/services/<service>/openapi.json`: supports [D4](#d4) and [D6](#d6).
- The code member is `code`: supports [D3](#d3).
- `typescript.yml` runs the package's Vitest suite, so no separate CI step is needed: supports [D4](#d4).
- [`pnpm-workspace.yaml`](../../../pnpm-workspace.yaml) already covers `frontend/packages/*`, and the dependency versions match the lock: supports [D1](#d1) and [D7](#d7).
