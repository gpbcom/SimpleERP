🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D100 Where custom data appears

# 📜 D100 Where custom data appears

**Status:** ✅ decided

## Context

Whether custom fields and new record types appear outside the screens.

## Options

- In the API and webhooks.
- To the AI assistant.
- In MCP and A2A.
- In imports and exports.

## Choice

In the API and webhooks, to the AI assistant (and the RAG index), and through MCP and A2A, always within permissions.
Spreadsheet imports and exports were not chosen.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Spreadsheet imports and exports cover the standard fields only (as answered; to be corrected by the owner if wrong).

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)
- [BR-F2-02](../../02-functional/f02-no-code-configuration/business-rules/br-f02-02-custom-data-follows-permissions.md)

---

⬅️ [D99 Archive, never delete](d99-archive-never-delete.md) · ⬆️ [Up](README.md) ·
➡️ [D101 Custom field types](d101-custom-field-types.md)
