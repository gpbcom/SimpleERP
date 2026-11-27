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
| Export the OpenAPI document | The application serves it at `/openapi.json`; a script of `.github/scripts/` writes the committed copy |
| Check the contract | A test of the service's `tests/`, run by CI |
| Run a job beside the service | An `AsyncRunnable` that the application's lifespan initialises and closes |
| Run an operation a person starts | An endpoint, behind the rights it needs |

## HTTP

None yet. When the first endpoint is added, this chapter lists each one (method, path, request, response, errors), its
OpenAPI definition, and its requests in the Bruno collection `bruno/`.

**Company and user headers.** Every request carries the company (`X-Company-Id`) and the user (`X-User-Id`) headers. The
`CompanyContextMiddleware` of [`erp_context`](../../../backend/shared/context/README.md) checks them on every path that is
not public, and tags each request with its request id (`X-Request-Id`).

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

Last reviewed: 2026-11-27 (GH-2)
