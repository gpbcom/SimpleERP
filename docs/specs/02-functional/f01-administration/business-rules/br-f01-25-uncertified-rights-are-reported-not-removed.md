🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-25 Uncertified rights are reported, not removed

# 📏 BR-F1-25 Uncertified rights are reported, not removed

**Status:** ✅ specified

## Statement

At the end of an access review, a right nobody certified is reported to the administrator, who decides; nothing is
removed automatically.

## Why

Removing rights automatically could stop a team's work on the deadline day.

## Examples

| Case | Result |
|---|---|
| Line certified | Kept |
| Line removed by the manager | Removed on confirmation |
| Line left open | Reported to the administrator |

## Applies to

- [UC-F1-18 Run an access review campaign](../use-cases/11-team-delegation-and-access-review/uc-f01-18-run-an-access-review-campaign.md)

## Exceptions

None.

## Configurable

Automatic removal at the deadline can be turned on per campaign.

## Open questions

None.

---

⬅️ [BR-F1-24](br-f01-24-a-deputy-approves-within-the-delegators-limits.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-26 Portal accounts see only their own records](br-f01-26-portal-accounts-see-only-their-own-records.md)
