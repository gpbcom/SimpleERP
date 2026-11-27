🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-09 Connector errors are visible and retried

# 📏 BR-F24-09 Connector errors are visible and retried

**Status:** ✅ specified

## Statement

A failed sync is retried (BR-F3-32), then shown with its cause and fix; an outside API change is detected and flagged to
the maintainers.

## Why

See [D427](../../../06-decisions/f24-integrations-hub/d427-integrations-hub-coverage.md).

## Examples

| Case | Result |
|---|---|
| CRM field renamed | Mapping flagged, sync paused for that field |

## Applies to

Every F24 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F24-08 Credentials in the vault](br-f24-08-credentials-in-the-vault.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-10 Disconnect cleanly](br-f24-10-disconnect-cleanly.md)
