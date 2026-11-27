🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-23 Site administrators stay within their site and rights

# 📏 BR-F1-23 Site administrators stay within their site and rights

**Status:** ✅ specified

## Statement

A site administrator manages only the users of their sites and gives only the roles the administrator listed for them,
never one with rights they do not hold.

## Why

Site managers need autonomy without becoming company administrators (D458).

## Examples

| Case | Result |
|---|---|
| Store manager gives Seller | Allowed |
| Store manager gives Accounting | Refused |
| Store manager opens a user of another shop | Not shown |

## Applies to

- [UC-F1-15 Administer the users of one's own site](../use-cases/10-bring-users-in-at-scale/uc-f01-15-administer-the-users-of-ones-own-site.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-22 Bulk invitations are checked line by line](br-f01-22-bulk-invitations-are-checked-line-by-line.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F1-24](br-f01-24-a-deputy-approves-within-the-delegators-limits.md)
