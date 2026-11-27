🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-22 Leave pay is the higher of two methods

# 📏 BR-F13-22 Leave pay is the higher of two methods

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

Pay for paid leave taken is the higher of the pay the employee would have earned at work (maintained pay) and one tenth
of the gross earned during the reference period, compared at least at the end of the period and each time
leave is taken.

## Why

The law requires the most favourable method (D470); the leave count follows CR-FR-044, the comparison is
(⚖️ lawyer review before launch, D574) to read: Code du travail L3141-24.

## Examples

| Case | Result |
|---|---|
| 5 days taken, maintained 480.00 EUR, one tenth 512.00 EUR | passes: 512.00 EUR paid |
| 5 days taken, maintained 600.00 EUR, one tenth 540.00 EUR | passes: 600.00 EUR paid |
| Construction worker covered by the BTP fund | passes: paid by the fund, not by the company (CR-FR-088) |

## Applies to

- [UC-F13-29 Value paid-leave pay](../use-cases/08-deductions-savings-and-leave-pay/uc-f13-29-value-paid-leave-pay.md)
- [UC-F13-33 Apply the construction agreements](../use-cases/09-collective-agreements-by-family/uc-f13-33-apply-the-construction-agreements.md)
- [UC-F13-15 End a contract](../use-cases/04-events/uc-f13-15-end-a-contract.md)

## Exceptions

Employees whose leave is paid by a fund (construction, performers) are paid by that fund.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F13-21 Profit-sharing once the threshold is reached](br-f13-21-profit-sharing-once-the-threshold-is-reached.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-23 Payroll cost split by the analytic axes](br-f13-23-payroll-cost-split-by-the-analytic-axes.md)
