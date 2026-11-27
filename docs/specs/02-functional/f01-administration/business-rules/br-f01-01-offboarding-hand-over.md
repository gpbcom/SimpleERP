🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-01 Offboarding hand-over

# 📏 BR-F1-01 Offboarding hand-over

**Status:** ✅ specified

## Statement

When a user leaves, the administrator picks a colleague who takes over the leaver's open items; the leaver's account is
deactivated, never deleted.

## Why

Nothing a customer or a colleague waits for is lost, and the history stays readable. See
[D56](../../../06-decisions/f01-administration/d56-offboarding-hand-over.md).

## Examples

| Case | Result |
|---|---|
| A sales person leaves with 12 open quotes | The 12 quotes move to the colleague picked; each quote's history still shows who wrote it |
| A manager leaves with 3 pending approvals | The 3 approvals move to the colleague picked |
| An administrator tries to delete a leaver's account | Refused: the account can only be deactivated |

## Applies to

- [UC-F1-05 Deactivate and offboard a user](../use-cases/03-user-lifecycle/uc-f01-05-deactivate-and-offboard-a-user.md)
- [UC-F1-15 Administer the users of one's own site](../use-cases/10-bring-users-in-at-scale/uc-f01-15-administer-the-users-of-ones-own-site.md)

## Exceptions

A leaver with no open item needs no hand-over.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F1-02 Administrator sees settings only](br-f01-02-administrator-sees-settings-only.md)
