🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-21 Deprovisioned users are deactivated, never deleted

# 📏 BR-F1-21 Deprovisioned users are deactivated, never deleted

**Status:** ✅ specified

## Statement

A user the identity provider deactivates or deletes is deactivated in simple-ERP, with the hand-over of their open
items; their records and history stay.

## Why

Deleting a user would break the history of what they did (BR-F2-01) and the audit trail.

## Examples

| Case | Result |
|---|---|
| Provider deactivates Luc | Luc deactivated, hand-over task to his manager |
| Provider deletes Luc | Same as deactivated |
| Provider reactivates Luc | Luc active again with his roles |

## Applies to

- [UC-F1-13 Provision users from the identity provider](../use-cases/10-bring-users-in-at-scale/uc-f01-13-provision-users-from-the-identity-provider.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-20 Provider sessions are visible](br-f01-20-provider-sessions-are-visible.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-22 Bulk invitations are checked line by line](br-f01-22-bulk-invitations-are-checked-line-by-line.md)
