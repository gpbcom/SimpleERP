🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-22 Terms above the limit need a recent solvency check

# 📏 BR-F6-22 Terms above the limit need a recent solvency check

**Status:** 🔄 waiting for the owner

## Statement

Payment terms or credit above the customer's credit limit need a solvency report not older than its validity (Proposed:
90 days); without one, the order stays held and the terms are refused.

## Why

Giving credit without a recent look at the customer's solvency exposes the company to unpaid invoices; the owner asked
for solvency checks
([D525](../../../06-decisions/f06-customers-and-sales/d525-benchmark-gaps-f06-customers-and-sales.md));
[BR-F6-11](br-f06-11-over-the-credit-limit-orders-are-held.md) already holds orders over the limit.

## Examples

| Case | Result |
|---|---|
| A report 30 days old, terms within the limit | no new report needed |
| A report 120 days old, terms above the limit | a new report is required |
| No report at all, a prepaid order | no report needed |
| A limit above the recommendation | needs a reason and an approval |
| A provider that is down | the order stays held, the user can retry |

## Applies to

- [UC-F6-30](../use-cases/10-partners-contracts-and-warranties/uc-f06-30-check-a-customers-solvency.md)
- [E-F6-26 Solvency report](../data/e-f06-26-solvency-report.md)
- [E-F6-12 Credit limit](../data/e-f06-12-credit-limit.md)
- [E-F6-01 Customer record](../data/e-f06-01-customer-record.md)

## Exceptions

None.

## Configurable

Yes: the validity of a report, by the owner (Proposed default: 90 days).

## Open questions

None.

---

⬅️ [BR-F6-21](br-f06-21-call-offs-never-exceed-the-balance-without-approval.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-23 The legal conformity guarantee applies first](br-f06-23-the-legal-conformity-guarantee-applies-first.md)
