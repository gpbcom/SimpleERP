🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-17 Dates follow the supplier's confirmed lead time

# 📏 BR-SC02-17 Dates follow the supplier's confirmed lead time

**Status:** 🔄 waiting for the owner

## Statement

The delivery date promised to a customer is never earlier than the date the supplier has confirmed plus the transport
time. When the supplier moves its date, the promised date moves with it and the customer is told the same day.

## Why

A promise made before the supplier's confirmation is a guess; missing it breaks the consumer's right to a stated date
and costs a cancellation. The owner asked for furniture orders
([D546](../../../06-decisions/sectors/d546-benchmark-gaps-sc02-retail.md)).

## Examples

| Case | Result |
|---|---|
| Supplier ready 2027-01-04, transport 3 days | earliest promise 2027-01-07 |
| Promise of 2026-12-18 | refused |
| Supplier moves to 2027-01-18 | promise moves to 2027-01-21, customer told |
| No supplier answer yet | no date promised |

## Applies to

- [UC-SC02-17](../use-cases/06-books-furniture-second-hand-franchise/uc-sc02-17-sell-made-to-order-furniture.md)
- [E-SC02-14 Furniture order](../data/e-sc02-14-furniture-order.md)
- [E-F7-03](../../../02-functional/f07-purchasing-and-stock/data/e-f07-03-purchase-order.md)

## Exceptions

None.

## Configurable

The transport time by delivery zone, by the store manager.

## Open questions

None.

---

⬅️ [BR-SC02-16](br-sc02-16-book-discounts-never-exceed-5-of-the-publishers-price.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC02-18](br-sc02-18-every-purchase-from-a-person-enters-the-police-register.md)
