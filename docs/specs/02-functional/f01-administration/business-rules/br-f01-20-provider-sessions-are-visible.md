🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-20 Provider sessions are visible

# 📏 BR-F1-20 Provider sessions are visible

**Status:** ✅ specified

## Statement

Each time the IT provider administrator enters a client company, a session is opened in the client's provider access
log, with who, when and what was done, and the client's administrators are notified.

## Why

The provider may enter at any time (D53) and sees everything (D90); the client always knows. See
[D89](../../../06-decisions/f01-administration/d89-provider-sessions-visible.md).

## Examples

| Provider action | Client sees |
|---|---|
| Enters Acme at 10:02 | Notification "Your IT provider (Paul, NetServ) entered simple-ERP at 10:02"; a new session in the log |
| Changes a role | The change in the session's list |
| Leaves, or 30 minutes idle | The session closes |

## Applies to

- [UC-F1-11](../use-cases/08-provider-and-client-companies/uc-f01-11-enter-a-client-company-to-support-it.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-19 Templates copy configuration only](br-f01-19-templates-copy-configuration-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-21](br-f01-21-deprovisioned-users-are-deactivated-never-deleted.md)
