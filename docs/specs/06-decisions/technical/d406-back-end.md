🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) › 📜 D406 Back end

# 📜 D406 Back end

**Status:** ✅ decided

## Context

Step 19v of the technical interview (PLAN D35).

## Options

- FastAPI, Litestar or Django.
- OpenAPI from the code or contract first.
- A service kit or a minimal shared package.
- Rules as pure functions or service methods.

## Choice

Confirmed by the owner on 2026-11-12: FastAPI; OpenAPI generated from the code, with MCP tools, A2A skills, clients and
the Bruno collection generated from it; `packages/` as a service kit without business rules; business rules as pure
functions over data.

Confirmed by the owner on 2026-11-27: every service is a regular FastAPI application, as in the other gpbcom projects.
There is never a `cli` module: the service's `api` layer is its FastAPI application, built by an application factory
and served by uvicorn, and no package has a command line.

## Decided by

The owner, on 2026-11-12, in the specification interview, and on 2026-11-27 for the regular FastAPI application.

## Consequences

The back-end chapter's target design. `AGENT.md` ("Layout") states how a service is built and served and what replaces
a command, and the tests of `tests/conventions/entrypoints/` fail on any command line in a package.

## Related

- [Back end](../../../technical/architecture/backend.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D405 Architecture and scalability](d405-architecture-and-scalability.md) · ⬆️ [Up](README.md) ·
➡️ [D407 Front end](d407-front-end.md)
