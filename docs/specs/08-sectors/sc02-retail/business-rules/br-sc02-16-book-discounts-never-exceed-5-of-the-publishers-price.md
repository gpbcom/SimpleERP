🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-16 Book discounts never exceed 5 % of the publisher's price

# 📏 BR-SC02-16 Book discounts never exceed 5 % of the publisher's price

**Status:** ✅ specified

## Statement

A new book is never sold below its publisher's price less 5 %. The discount, any promotion and any loyalty reward count
together toward the cap, and the till refuses a line that would go below the lowest allowed price.

## Why

The fixed book price protects small bookshops from price wars; selling below it is unlawful for the shop. The owner
asked for the book trade ([D546](../../../06-decisions/sectors/d546-benchmark-gaps-sc02-retail.md)). The
France-pack rule is listed below.

## Examples

| Case | Result |
|---|---|
| Price 21.00 EUR, discount 5 % | 19.95 EUR, accepted |
| Price 21.00 EUR, discount 10 % | refused, lowest price 19.95 EUR |
| Discount 3 % and a reward worth 3 % | the reward is cut to 2 % |
| Out-of-print book with a lower printed price | the printed price applies from its date |
| School customer with a data cap of 9 % | the cap of the customer type applies |

## Applies to

- [UC-SC02-16](../use-cases/06-books-furniture-second-hand-franchise/uc-sc02-16-sell-books-under-the-fixed-price-law.md)
- [E-SC02-13 Book title](../data/e-sc02-13-book-title.md)
- [E-F10-08](../../../02-functional/f10-point-of-sale/data/e-f10-08-price-promotion.md)
- France-pack rule:
  [CR-FR-227 Fixed book price (5 % cap)](../../../10-country-packs/france/trade/cr-fr-227-fixed-book-price.md)

## Exceptions

Customer types with another cap in the country pack (schools, libraries).

## Configurable

The cap by customer type, as data of the country pack.

## Open questions

None.

---

⬅️ [BR-SC02-15 Targets per store and staff](br-sc02-15-targets-per-store-and-staff.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC02-17](br-sc02-17-dates-follow-the-suppliers-confirmed-lead-time.md)
