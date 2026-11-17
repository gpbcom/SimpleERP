🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-01 Purchases approved by amount and budget

# 📏 BR-F7-01 Purchases approved by amount and budget

**Status:** ✅ specified

## Statement

A purchase request above the requester's amount, or over its project's or department's budget, needs a manager's
approval, and above a second amount the owner's; amounts per role and budgets are configurable.

## Why

See [D267](../../../06-decisions/f07-purchasing-and-stock/d267-purchase-approval.md).

## Examples

| Case | Result |
|---|---|
| 164 EUR, buyer's limit 2,000 | Ordered |
| 3,500 EUR | Manager approves |
| 25,000 EUR | Manager, then owner |
| Over the project's budget | Manager approves, budget shown |

## Applies to

Every F7 use case concerned.

- [UC-F7-20 Order from an approved catalogue or punch-out](../use-cases/08-catalogues-and-stock-levels/uc-f07-20-order-from-an-approved-catalogue-or-punch-out.md)

## Exceptions

None.

## Configurable

Yes: amounts per role, budgets.

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [BR-F7-02 Reorders are suggested, then confirmed](br-f07-02-reorders-are-suggested-then-confirmed.md)
