# erp_context: company context and rights

`erp_context` is the shared library that every SimpleERP service uses for two things: knowing which company and which
user a request is for, and deciding whether that user may do an action on a record. It holds no business rule of its
own. A service imports it, registers its policies and calls it on each request.

The library is in `backend/shared/context/` (package `erp_context`, [pyproject](pyproject.toml)). It follows the
repository layout of [D438](../../../docs/specs/06-decisions/technical/d438-repository-layout.md) and the back-end
decision [D406](../../../docs/specs/06-decisions/technical/d406-back-end.md).

## What the library holds

| Layer | Holds |
|---|---|
| `api/` | The entry points a service mounts: `CompanyContextMiddleware`, `RightsGuard` and `RefusalHandler` |
| `service/` | The business rules: `CompanyContextService` reads the headers, `RightsService` evaluates the policies, `Policy` is the contract a policy implements |
| `storage/` | `RequestContextStore`, which keeps the request's context for the code below the routes |
| `models/` | The Pydantic models and enums: `ContextConfig`, `RequestContext`, `UserContext`, `RecordRef`, `RightsDecision`, `PolicyEffect`, `RefusalReason`, `RefusalCode`, `RefusalCatalog` and `Problem`, and their `SE` exceptions |
| `conf/catalogs/refusal_codes.yaml` | The refusal catalogue, one code per reason a request is refused |

The layers follow [AGENT.md](../../../AGENT.md#layout): `api` calls `service`, `service` calls `storage`, and all three
import `models`.

## How a service uses it

**1. Add the company context middleware.** `CompanyContextMiddleware` reads each request's headers, with a
`ContextConfig`:

| Field | Default | Meaning |
|---|---|---|
| `company_header` | `X-Company-Id` | The request header that carries the company |
| `user_header` | `X-User-Id` | The request header that carries the user |
| `request_header` | `X-Request-Id` | The request header that carries the request id |
| `public_paths` | a list of paths | The paths that need no company and no user |

A request without a company or a user, on a path that is not public, is refused.

**2. Register the refusal handler.** `RefusalHandler` turns every `SEAccessError` into an `application/problem+json`
response, with the code of the refusal catalogue. Register it once on the FastAPI application, for `SEAccessError`.

**3. Give the rights service its policies.** `RightsService` evaluates the policies of the service, each a `Policy`
that answers `PolicyEffect` for an action on a `RecordRef`. Then decide in one of two ways:

- in a route, call `RightsGuard.check(action, record)`, which raises `SEAccessError` when the action is refused;
- anywhere else, call `RightsService.allowed(user, action, record)`, which returns a `RightsDecision`.

Both give the same answer: the guard calls the same `allowed` decision. A test of `tests/api/rights/` checks that parity.

**Notes:**

- **The library ships no allowing policy.** Every action is denied until the service registers a policy that allows it.
- **Deny by default, and deny wins.** When no policy allows the action, the decision is a refusal. When one policy
  denies it, no other policy can allow it.
- **A record of another company is refused,** whatever the policies say.
- **Every refusal is logged** with its code, who asked, what was asked and why, so that the audit trail can hold it
  ([REQ-T02-06](../../../docs/specs/03-technical/t02-identity-and-access/requirements/req-t02-06-refusals-audited.md)).

**4. Read the context in storage.** The routes put the request's company and user in `RequestContextStore`. Storage
code reads them from there, and never from the request object, so that every query filters on the company of the
request ([REQ-T01-02](../../../docs/specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md)).

## Refusal codes

Each refusal has one code, its HTTP status and the keys of its messages. The codes are in
`conf/catalogs/refusal_codes.yaml`:

| Reason | Code | Status |
|---|---|---|
| `no-company` | `CONTEXT-COMPANY-01` | 400 |
| `no-user` | `CONTEXT-USER-01` | 401 |
| `no-policy` | `RIGHTS-DENIED-01` | 403 |
| `policy-denied` | `RIGHTS-DENIED-02` | 403 |
| `other-company` | `RIGHTS-COMPANY-01` | 403 |

The problem document carries the code, the status, the translation keys of the title, the reason and the action, and a
`reference`. Its `instance` is the request id, so that a support request can name the exact occurrence
([REQ-T05-03](../../../docs/specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md),
[D122](../../../docs/specs/06-decisions/ux/d122-error-message-standard.md)).

The interface of the decision is [I-T02-02](../../../docs/specs/03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md),
and the security design is [D414](../../../docs/specs/06-decisions/technical/d414-security-design.md).
The HTTP style is [D410](../../../docs/specs/06-decisions/technical/d410-api-style-and-auth.md).

## Tests

```bash
uv run --package erp-context pytest backend/shared/context/tests -n 2
```

The tests mirror the layers: `tests/api/`, `tests/service/`, `tests/storage/` and `tests/models/`. They use real
policies, such as an allowing test policy, and no mocks.
