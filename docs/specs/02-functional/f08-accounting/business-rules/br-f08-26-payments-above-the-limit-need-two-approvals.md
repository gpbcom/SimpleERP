🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-26 Payments above the limit need two approvals

# 📏 BR-F8-26 Payments above the limit need two approvals

**Status:** 🔄 waiting for the owner

## Statement

A payment order above the approval limit needs two approvals from two different people before it is authorised and sent;
below the limit one approval is enough; the person who prepared the order cannot give the second approval.

## Why

Two people agreeing on a large payment prevents errors and fraud. The owner asked to pay from the ERP
([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md));
[BR-F8-12 Spend follows card and approval limits](br-f08-12-spend-follows-limits.md) sets spend limits for cards in the
same spirit.

## Examples

| Case | Result |
|---|---|
| A payment of 1,240 EUR, limit 10,000 EUR | one approval is enough |
| A payment of 18,000 EUR | two approvals from two people |
| The preparer gives the first approval and the second | refused |
| An order split into three of 6,000 EUR for the same bill | counted as one for the limit |
| An approval older than 7 days | expires and is asked again |

## Applies to

- [UC-F8-34](../use-cases/11-treasury-and-payment-means/uc-f08-34-pay-suppliers-from-the-erp.md)
- [E-F8-38 Payment order](../data/e-f08-38-payment-order.md)
- [E-F8-28 Payment run](../data/e-f08-28-payment-run.md)
- [E-F7-05 Supplier invoice](../../f07-purchasing-and-stock/data/e-f07-05-supplier-invoice.md)

## Exceptions

None.

## Configurable

Yes: the limit and the validity of an approval, by the owner.

## Open questions

None.

---

⬅️ [BR-F8-25](br-f08-25-the-forecast-uses-only-open-items-and-approved-plans.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-27 Recurring entries stop at their end date](br-f08-27-recurring-entries-stop-at-their-end-date.md)
