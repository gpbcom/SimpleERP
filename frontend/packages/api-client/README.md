# @simpleerp/api-client

The typed client of the platform API, for the front ends of SimpleERP. It is one of the shared TypeScript packages of
`frontend/packages/` ([D438](../../../docs/specs/06-decisions/technical/d438-repository-layout.md)), and it is built on
[`openapi-fetch`](https://openapi-ts.dev/openapi-fetch/).

## What it is

The client is typed from the committed OpenAPI document of the `platform` service,
`backend/services/platform/openapi.json`. The path types of `src/generated/platform.ts` are generated from that
document by `scripts/generate.mjs`, with `openapi-typescript`. The paths carry the `/v1` prefix, so a caller gives the
root of the API as `baseUrl`.

Every non-2xx answer rejects the call with one of two typed errors, described below. The package exports:

- `createApiClient`, which builds the client;
- the types `ApiClientOptions`, `PlatformClient` and `PlatformPaths`;
- `ApiProblemError` and `ApiUnexpectedResponseError`;
- `toApiError` and `PROBLEM_CODE_MEMBER`, which map an answer to an error.

## Using the client

```ts
import { createApiClient } from '@simpleerp/api-client'

const client = createApiClient({ baseUrl: 'http://localhost:8000' })

const { data } = await client.GET('/v1/health')
```

`createApiClient` takes three options: `baseUrl` (required), `headers` (sent with every call, such as the company or the
authorisation) and `fetch` (the global `fetch` by default).

## Errors

A call that the API refuses rejects with one of these errors. Nothing else of the response body is kept.

| Error | When | Fields |
|---|---|---|
| `ApiProblemError` | The answer is `application/problem+json` and carries a `code` member | `code`: the D122 support code of the refusal, such as `RIGHTS-DENIED-02`. `status`: the HTTP status |
| `ApiUnexpectedResponseError` | Any other non-2xx answer, or a problem body without a usable `code` | `status`: the HTTP status |

Only the code and the status are copied. The rest of the problem body is dropped on purpose, so that no secret or
internal detail of a refusal reaches the front end's logs or screens ([REQ-T05-03](../../../docs/specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md),
[D122](../../../docs/specs/06-decisions/ux/d122-error-message-standard.md)).

## Generating the client

`src/generated/` is generated and is never edited by hand. To regenerate it after the API of `platform` has changed,
first export the OpenAPI document (see [API](../../../docs/technical/interfaces/api.md#http)), then run:

```bash
pnpm --filter ./frontend/packages/api-client run generate
```

To check that the committed client matches the committed OpenAPI document, without writing anything, run:

```bash
pnpm --filter ./frontend/packages/api-client run check:generated
```

The Vitest suite of the package (`pnpm --filter ./frontend/packages/api-client run test`) includes a check of the
generated file, so it fails when the client is stale. CI runs this suite with the other front-end tests, so a stale
client fails the pipeline.

## Scripts

| Script | Does |
|---|---|
| `lint` | Lints the package with ESLint |
| `typecheck` | Type-checks the package with `tsc --noEmit` |
| `test` | Runs the Vitest suite |
| `generate` | Writes `src/generated/platform.ts` from the committed OpenAPI document |
| `check:generated` | Fails when `src/generated/platform.ts` differs from what `generate` would write |

## Layout

| Path | Holds |
|---|---|
| `src/index.ts` | The public exports |
| `src/client/` | `createApiClient` and its options |
| `src/problem/` | The two error classes and `toApiError` |
| `src/generated/` | The generated path types, never edited by hand |
| `scripts/generate.mjs` | The generator, with its `--check` mode |
| `tests/` | The Vitest suite |
