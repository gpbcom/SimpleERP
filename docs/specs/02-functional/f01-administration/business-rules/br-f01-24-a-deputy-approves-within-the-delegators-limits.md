🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-24 A deputy approves within the delegator's limits

# 📏 BR-F1-24 A deputy approves within the delegator's limits

**Status:** ✅ specified

## Statement

During a delegation, the deputy approves what the manager could, within the manager's amount limits, never their own
requests, and only between the start and end dates.

## Why

Delegation keeps work moving without widening anyone's rights.

## Examples

| Case | Result |
|---|---|
| Expense of 240 EUR, limit 1,000 EUR | Deputy approves |
| Purchase of 7,000 EUR, limit 5,000 EUR | Goes to the next level |
| Deputy's own expense | Goes to the manager's manager |

## Applies to

- [UC-F1-16 Delegate approvals during an absence](../use-cases/11-team-delegation-and-access-review/uc-f01-16-delegate-approvals-during-an-absence.md)
- [UC-F1-17 See my team's accounts and pending requests](../use-cases/11-team-delegation-and-access-review/uc-f01-17-see-my-teams-accounts-and-pending-requests.md)
- [UC-F2-29 Set up an approval chain](../../f02-no-code-configuration/use-cases/11-rights-translations-and-approvals/uc-f02-29-set-up-an-approval-chain.md)

## Exceptions

None.

## Configurable

The approvals a delegation covers: leave, purchases, expenses, or all.

## Open questions

None.

---

⬅️ [BR-F1-23](br-f01-23-site-administrators-stay-within-their-site-and-rights.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-25 Uncertified rights are reported, not removed](br-f01-25-uncertified-rights-are-reported-not-removed.md)
