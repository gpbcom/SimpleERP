🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-08 Credentials in the vault

# 📏 BR-F24-08 Credentials in the vault

**Status:** ✅ specified

## Statement

Every connector's credentials and tokens are in the vault (D240), never shown to a model or a log, refreshed
automatically.

## Why

See [D427](../../../06-decisions/f24-integrations-hub/d427-integrations-hub-coverage.md).

## Examples

| Case | Result |
|---|---|
| Token expires | Refreshed; if refused, the administrator asked once |

## Applies to

Every F24 use case concerned.

- [UC-F24-22 Automate with n8n, Make or Zapier](../use-cases/06-business-tools/uc-f24-22-automate-with-n8n-make-or-zapier.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F24-07 Two-way sync with an owner per field](br-f24-07-two-way-sync-with-ownership.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-09 Connector errors are visible and retried](br-f24-09-connector-errors-visible.md)
