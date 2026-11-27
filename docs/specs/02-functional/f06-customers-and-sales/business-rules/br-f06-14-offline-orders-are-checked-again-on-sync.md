🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-14 Offline orders are checked again on sync

# 📏 BR-F6-14 Offline orders are checked again on sync

**Status:** ✅ specified

## Statement

An order taken offline keeps its offline time and is priced and checked again (price, stock, credit limit) on sync; any
difference needs the rep's acceptance before confirmation.

## Why

Prices and stock may change while the rep is offline.

## Examples

| Case | Result |
|---|---|
| Nothing changed | Confirmed |
| Price up 0.50 EUR | Rep accepts or removes the line |

## Applies to

- [UC-F6-21 Take orders offline on the road](../use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F6-13 Each payer pays its share up to its cap](br-f06-13-each-payer-pays-its-share-up-to-its-cap.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F6-15 A pro-forma is not an invoice](br-f06-15-a-pro-forma-is-not-an-invoice.md)
