🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D410 API style and authentication

# 📜 D410 API style and authentication

**Status:** ✅ decided

## Context

Step 19d of the technical interview, from TC-07.

## Options

- REST with OpenAPI, or REST with GraphQL.
- OAuth 2 and OpenID Connect with scoped tokens, or API keys.

## Choice

Confirmed by the owner on 2026-11-12: REST with OpenAPI, versioned; OAuth 2 and OpenID Connect with scoped short-lived
tokens.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The API chapter's target design.

## Related

- [API style and authentication](../../../technical/interfaces/api.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D409 Storage choices](d409-storage-choices.md) · ⬆️ [Up](README.md) ·
➡️ [D411 MCP server and client](d411-mcp-server-and-client.md)
