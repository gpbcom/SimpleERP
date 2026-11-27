🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-05 Sessions are used oldest first

# 📏 BR-SC17-05 Sessions are used oldest first

**Status:** ✅ specified

## Statement

When a visit uses a package, the session is taken from the oldest package of that service that still has sessions and
has not expired. A newer package is used first only by a recorded override.

## Why

Taking from the newest package lets older ones expire unused and causes disputes. The owner asked for packages and
prepaid sessions ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| Packages ending 2027-01 and 2027-05 | the one ending 2027-01 is used first |
| The older package has 0 sessions | the next one is used |
| Override by the beautician | the newer package is used and the override recorded |
| Expired package | never used |
| No package | single visit price |

## Applies to

- [UC-SC17-05](../use-cases/02-packages-and-memberships/uc-sc17-05-sell-packages-and-prepaid-sessions.md)
- [E-SC17-04 Session package](../data/e-sc17-04-session-package.md)
- [E-SC17-04 Session package](../data/e-sc17-04-session-package.md)

## Exceptions

A package bought for a person may be shared with a named family member when the sale says so.

## Configurable

The validity of each package and whether a session may be shared, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-04 No-show fees follow the published terms](br-sc17-04-no-show-fees-follow-the-published-terms.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC17-06 Membership dues stop at cancellation](br-sc17-06-membership-dues-stop-at-cancellation.md)
