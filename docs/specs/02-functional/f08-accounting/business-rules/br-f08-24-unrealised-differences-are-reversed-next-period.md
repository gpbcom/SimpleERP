🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-24 Unrealised differences are reversed next period

# 📏 BR-F8-24 Unrealised differences are reversed next period

**Status:** ✅ specified

## Statement

Unrealised exchange differences posted at a period end are reversed on the first day of the next period, and only the
real difference, computed against the original booked value, is recognised when an item is settled.

## Why

Counting the same difference at the end of the period and again at settlement would double it. The owner asked for FX
revaluation ([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md)); posted entries are
never changed ([BR-F8-01 Posted entries never change](br-f08-01-posted-entries-never-change.md)), so the reversal is a
new entry.

## Examples

| Case | Result |
|---|---|
| A gain of 300 EUR on an open invoice at the period end | posted at the period end, reversed on the next day |
| The invoice is paid for 9,500 EUR against a booked 9,200 EUR | a real gain of 300 EUR on settlement |
| A currency without a closing rate | not posted, items listed |
| A locked period | refused |
| A run recomputed before posting | replaces the previous computation |

## Applies to

- [UC-F8-32](../use-cases/11-treasury-and-payment-means/uc-f08-32-revalue-foreign-currency-items.md)
- [E-F8-36 Revaluation run](../data/e-f08-36-revaluation-run.md)
- [E-F8-03 Journal entry](../data/e-f08-03-journal-entry.md)
- [E-F8-10 Fiscal period](../data/e-f08-10-fiscal-period.md)

## Exceptions

None.

## Configurable

No; the accounts used for gains and losses are set in the chart of accounts.

## Open questions

None.

---

⬅️ [BR-F8-23](br-f08-23-a-cheque-or-lcr-is-posted-when-the-bank-credits-it.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-25](br-f08-25-the-forecast-uses-only-open-items-and-approved-plans.md)
