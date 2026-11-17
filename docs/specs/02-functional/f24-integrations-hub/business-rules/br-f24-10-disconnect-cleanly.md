🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-10 Disconnect cleanly

# 📏 BR-F24-10 Disconnect cleanly

**Status:** ✅ specified

## Statement

Disconnecting a tool stops the sync, revokes the tokens and lets the administrator keep or delete the synced data.

## Why

See [D427](../../../06-decisions/f24-integrations-hub/d427-integrations-hub-coverage.md).

## Examples

| Case | Result |
|---|---|
| Disconnect Pipedrive | Tokens revoked, data kept |

## Applies to

Every F24 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F24-09 Connector errors are visible and retried](br-f24-09-connector-errors-visible.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-11 Connector costs are metered](br-f24-11-connector-costs-metered.md)
