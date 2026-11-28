# API

The entry points of SimpleERP: what calls it, and how.

## How a service is served

Every service is a regular FastAPI application ([D406](../../specs/06-decisions/technical/d406-back-end.md)). Its `api`
layer is the application, and `AppFactory.create()` in `api/app_factory.py` builds it: it reads `conf/app.yaml`,
configures logging and returns the `FastAPI` application. uvicorn serves it, in the image and on a laptop:

```bash
uvicorn --factory <service_pkg>.api.app_factory:AppFactory.create --host <host> --port <port>
```

SimpleERP has no command line. No package of `backend/`, `plugins/` or `sdk/` holds a `cli` module, a `__main__.py`, a
console script or an argument parser, and `tests/conventions/entrypoints/` fails on any of them (`AGENT.md`, "Layout").

| What a command would have done | How it is done |
|---|---|
| Serve the service | uvicorn serves the application factory |
| Export the OpenAPI document | The application serves it at `/openapi.json`; `.github/scripts/export_openapi.py` writes the committed copy |
| Check the contract | The tests of `backend/services/platform/tests/contracts/`, run by CI through `.github/scripts/check_contract.sh` |
| Run a job beside the service | An `AsyncRunnable` that the application's lifespan initialises and closes |
| Run an operation a person starts | An endpoint, behind the rights it needs |

## HTTP

Each endpoint is listed here as it is added, this chapter lists each one (method, path, request, response, errors), its
OpenAPI definition, and its requests in the Bruno collection `bruno/`.

**OpenAPI of the platform service.** As [REQ-T05-01](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-01-rest-openapi.md) and the registry of [I-T05-02](../../specs/03-technical/t05-api-and-webhooks/interfaces/i-t05-02-openapi-registry.md) require, `platform` serves its OpenAPI document, generated from its code, at the FastAPI
OpenAPI URL (`/openapi.json`). The same document is committed at `backend/services/platform/openapi.json`, and the
tests of `backend/services/platform/tests/contracts/` ([REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)) fail when the committed copy differs from the served one. A stale
copy fails CI. To regenerate it after a change of the API:

```bash
uv run --package platform python .github/scripts/export_openapi.py backend/services/platform
```

The script exits 0 when it writes the document, and 2 with one line on stderr when the folder has no single package or
the application cannot be built. The contract tests also compare the document with the one of a base commit, given in
`ERP_CONTRACT_BASELINE`, as described in [CI/CD](../delivery/ci-cd-and-stages.md#workflows).

**Bruno collection of the platform.** The collection `bruno/platform/` is generated from the committed OpenAPI document
of `platform` ([D406](../../specs/06-decisions/technical/d406-back-end.md)), with one request per operation under
`requests/<tag>/`. To regenerate it after a change of the API, run:

```bash
python3 .github/scripts/bruno_collection.py generate --service backend/services/platform
```

CI fails while the collection is stale ([REQ-T05-05](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-05-contract-tests.md)).
The hand-written requests with their tests live in `bruno/platform/tests/`: the health call, and one refused call whose
body is an `application/problem+json` document with its code and no secret ([REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)).
To run the collection locally against [`compose.e2e.yaml`](../../../compose.e2e.yaml), run:

```bash
cd bruno/platform && npx --yes @usebruno/cli@4.2.1 run --env stage
```

A local secret goes in an ignored `.env` file, and never in a committed file ([TEST-1](../../specs/06-decisions/technical/d426-testing-strategy.md), [D426](../../specs/06-decisions/technical/d426-testing-strategy.md)).

**Company and user headers.** Every request carries the company (`X-Company-Id`) and the user (`X-User-Id`) headers. The
`CompanyContextMiddleware` of [`erp_context`](../../../backend/shared/context/README.md) checks them on every path that is
not public, and tags each request with its request id (`X-Request-Id`).

**Typed front-end client.** The typed client of the platform API lives in
[`frontend/packages/api-client`](../../../frontend/packages/api-client/README.md). It is generated from each service's
committed OpenAPI document, and it maps every `application/problem+json` error to a typed `ApiProblemError` that carries
the D122 code of the refusal ([D122](../../specs/06-decisions/ux/d122-error-message-standard.md)); any other error answer
becomes an `ApiUnexpectedResponseError` with its status.

**Refusals.** A refusal is an `application/problem+json` response ([D410](../../specs/06-decisions/technical/d410-api-style-and-auth.md)).
It carries the refusal code of the catalogue (for example `RIGHTS-DENIED-02`), and its `instance` is the request id, so
that a support request names the exact occurrence.

## Target design (specified in GH-2, not built yet)

**Style (D410).** JSON over HTTP, an OpenAPI per service behind one gateway, the version in the path (`/v1`), cursor
paging, filtering and sorting conventions, idempotency keys on writes, signed webhooks, `application/problem+json`
errors carrying the error codes of the error message pattern (D122).

**Authentication.** OAuth 2 and OpenID Connect through the self-hosted identity provider (Keycloak,
[Security](../security/security.md)); apps get scoped, short-lived tokens on a user's or a service account's behalf;
personal access tokens only with scopes and expiry; every call carries the company and the user's rights.

The MCP and A2A entry points are in [MCP](mcp.md) and [A2A](a2a.md).

Decided in [D410](../../specs/06-decisions/technical/d410-api-style-and-auth.md).

Last reviewed: 2026-11-28 (GH-2)
