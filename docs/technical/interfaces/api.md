# API

The entry points of simple-erp: what calls it, and how.

## Command line

| Command | Defined in | Does |
|---|---|---|
| `simple-erp` | `src/api/cli/main.py` (`[project.scripts]` in `pyproject.toml`) | Prints a greeting. It is the place where commands will be added, through `api/factories/` |

Only `api/cli/` prints to the terminal; every other layer logs.

## HTTP

None yet. When the first endpoint is added, this chapter lists each one (method, path, request, response, errors), its
OpenAPI definition, and its requests in the Bruno collection `bruno/` (rule TEST-1).

## Target design (specified in GH-2, not built yet)

**Style (D410).** JSON over HTTP, an OpenAPI per service behind one gateway, the version in the path (`/v1`), cursor
paging, filtering and sorting conventions, idempotency keys on writes, signed webhooks, `application/problem+json`
errors carrying the error codes of the error message pattern (D122).

**Authentication.** OAuth 2 and OpenID Connect through the self-hosted identity provider (Keycloak,
[Security](../security/security.md)); apps get scoped, short-lived tokens on a user's or a service account's behalf;
personal access tokens only with scopes and expiry; every call carries the company and the user's rights.

The MCP and A2A entry points are in [MCP](mcp.md) and [A2A](a2a.md).

Decided in [D410](../../specs/06-decisions/technical/d410-api-style-and-auth.md).

Last reviewed: 2026-11-12 (GH-2)
