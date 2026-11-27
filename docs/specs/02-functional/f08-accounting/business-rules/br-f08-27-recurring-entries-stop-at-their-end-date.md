🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-27 Recurring entries stop at their end date

# 📏 BR-F8-27 Recurring entries stop at their end date

**Status:** ✅ specified

## Statement

A recurring entry template creates entries only from its start date up to its end date or its last occurrence; after
that it is Ended and creates nothing, and an end date can be moved later only before it has passed.

## Why

An entry that keeps repeating after a lease or a subscription ended misstates the books every period. The owner asked
for recurring entries ([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md)).

## Examples

| Case | Result |
|---|---|
| A template ending on 30 September | its last entry is created on 1 September |
| The 1 October due date | no entry; the template is Ended |
| An end date moved from 30 September to 31 December before 30 September | allowed |
| An end date moved after the template Ended | refused; a new template is created |
| 12 occurrences chosen | the template ends after the twelfth |

## Applies to

- [UC-F8-35](../use-cases/11-treasury-and-payment-means/uc-f08-35-schedule-recurring-entries.md)
- [E-F8-39 Entry template](../data/e-f08-39-entry-template.md)
- [E-F8-03 Journal entry](../data/e-f08-03-journal-entry.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-26 Payments above the limit need two approvals](br-f08-26-payments-above-the-limit-need-two-approvals.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-28](br-f08-28-the-auditor-reads-only-and-every-view-is-logged.md)
