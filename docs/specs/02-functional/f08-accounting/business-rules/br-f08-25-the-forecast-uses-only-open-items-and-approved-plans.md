🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-25 The forecast uses only open items and approved plans

# 📏 BR-F8-25 The forecast uses only open items and approved plans

**Status:** ✅ specified

## Statement

The cash forecast is built only from open items (unpaid invoices and bills, scheduled instalments, payroll and tax
dates) and from plans that have been approved; draft or unapproved plans, quotes and hopes never enter it.

## Why

A forecast that includes unconfirmed money gives false comfort. The owner asked for the daily cash position
([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md)); plans are approved in
[UC-F8-19](../use-cases/06-benchmark-additions/uc-f08-19-plan-and-forecast.md).

## Examples

| Case | Result |
|---|---|
| An open invoice due on the 10th | in the forecast |
| A quote not yet accepted | not in the forecast |
| A budget plan in Draft | not in the forecast |
| An approved plan with a planned receipt | in the forecast |
| An invoice already paid | never counted twice |

## Applies to

- [UC-F8-33](../use-cases/11-treasury-and-payment-means/uc-f08-33-follow-the-daily-cash-position.md)
- [E-F8-37 Cash forecast](../data/e-f08-37-cash-forecast.md)
- [E-F8-16 Budget plan](../data/e-f08-16-budget-plan.md)
- [E-F6-05 Invoice](../../f06-customers-and-sales/data/e-f06-05-invoice.md)
- [E-F7-05 Supplier invoice](../../f07-purchasing-and-stock/data/e-f07-05-supplier-invoice.md)

## Exceptions

None.

## Configurable

Yes: the horizon (default 13 weeks), the floor and the delay model, by the treasurer.

## Open questions

None.

---

⬅️ [BR-F8-24](br-f08-24-unrealised-differences-are-reversed-next-period.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-26 Payments above the limit need two approvals](br-f08-26-payments-above-the-limit-need-two-approvals.md)
