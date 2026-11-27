🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-11 Over the credit limit, orders are held

# 📏 BR-F6-11 Over the credit limit, orders are held

**Status:** ✅ specified

## Statement

An order whose amount added to the customer's (or group's) open balance passes its credit limit, or whose customer has
an invoice overdue beyond the set days, is held until accounting releases it with a reason or a payment brings it back
within the limit.

## Why

Standard credit control (D463); sales cannot grow a bad debt alone.

## Examples

| Case | Result |
|---|---|
| Balance 18,000 + order 6,000, limit 20,000 | Held |
| Payment brings it to 14,000 | Released |

## Applies to

- [UC-F6-17 Organise accounts with their timeline and emails](../use-cases/06-accounts-and-credit/uc-f06-17-organise-accounts-with-their-timeline-and-emails.md)
- [UC-F6-18 Set a credit limit and hold orders](../use-cases/06-accounts-and-credit/uc-f06-18-set-a-credit-limit-and-hold-orders.md)
- [UC-F6-21 Take orders offline on the road](../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md)

## Exceptions

None.

## Configurable

Limit per customer or group; overdue days (Proposed: 30).

## Open questions

None.

---

⬅️ [BR-F6-10 Usage is billed from metered data](br-f06-10-usage-is-billed-from-metered-data.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-12](br-f06-12-public-invoices-go-through-chorus-pro-with-their-references.md)
