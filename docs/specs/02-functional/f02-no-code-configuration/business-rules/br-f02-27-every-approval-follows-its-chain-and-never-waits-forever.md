🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-27 Every approval follows its chain and never waits forever

# 📏 BR-F2-27 Every approval follows its chain and never waits forever

**Status:** ✅ specified

## Statement

An approval follows the record type's chain: levels by amount or condition, one or all approvers per level, nobody
approves their own request, and a decision missing past the time limit escalates.

## Why

One engine for F7, F8, F9 and the sectors (D459), with no request stuck.

## Examples

| Case | Result |
|---|---|
| 6,200 EUR purchase, owner above 5,000 EUR | Manager then owner |
| 48 hours without decision | Escalated |
| Requester is the approver | Next level |

## Applies to

- [UC-F2-29 Set up an approval chain](../use-cases/11-rights-translations-and-approvals/uc-f02-29-set-up-an-approval-chain.md)

## Exceptions

None.

## Configurable

Levels, approvers, time limit, escalation.

## Open questions

None.

---

⬅️ [BR-F2-26](br-f02-26-a-missing-translation-falls-back-to-the-company-language.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-28](br-f02-28-scripts-run-sandboxed-within-time-and-memory-limits.md)
