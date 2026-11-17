🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-22 Bulk invitations are checked line by line

# 📏 BR-F1-22 Bulk invitations are checked line by line

**Status:** ✅ specified

## Statement

Every line of a bulk invitation is checked (email, duplicates, role, site, manager) before sending; a line in error is
never sent.

## Why

One wrong role sent to 40 people is 40 accounts to fix.

## Examples

| Case | Result |
|---|---|
| Two lines with the same email | Both in error, "appears twice" |
| Unknown site | Line in error, "site not found" |
| Valid line | Sent |

## Applies to

- [UC-F1-14 Invite users in bulk](../use-cases/10-bring-users-in-at-scale/uc-f01-14-invite-users-in-bulk.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-21](br-f01-21-deprovisioned-users-are-deactivated-never-deleted.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-23](br-f01-23-site-administrators-stay-within-their-site-and-rights.md)
