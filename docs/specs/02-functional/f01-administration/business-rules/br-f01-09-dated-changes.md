🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-09 Dated changes

# 📏 BR-F1-09 Dated changes

**Status:** ✅ specified

## Statement

A change of roles can take effect at once or from a chosen date; a dated change applies automatically at the start of
that day, in the company's time zone.

## Why

Promotions and transfers often start on a set date. See
[D70](../../../06-decisions/f01-administration/d70-role-change-timing.md).

## Examples

| Change | Result |
|---|---|
| Add Manager at once | Applies at the user's next action |
| Add Manager from 1 December | Waits on the user's page; applies on 1 December at 00:00 |
| Remove Accounting at once | The right ends immediately |

## Applies to

- [UC-F1-04](../use-cases/03-user-lifecycle/uc-f01-04-change-a-users-role-or-site.md)
- [UC-F1-15 Administer the users of one's own site](../use-cases/10-bring-users-in-at-scale/uc-f01-15-administer-the-users-of-ones-own-site.md)

## Exceptions

A dated change can be cancelled until its date.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-08 Rights add up](br-f01-08-rights-add-up.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-10 A leaver's AI assistant history is deleted](br-f01-10-leavers-assistant-history-deleted.md)
