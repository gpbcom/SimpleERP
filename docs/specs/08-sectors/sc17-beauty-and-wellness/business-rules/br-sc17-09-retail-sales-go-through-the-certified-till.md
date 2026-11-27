🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-09 Retail sales go through the certified till

# 📏 BR-SC17-09 Retail sales go through the certified till

**Status:** ✅ specified

## Statement

Every retail sale of the salon, with or without services, is recorded through the certified till; no sale is kept
outside it, and a closed sale is corrected only by a credit, never by editing it.

## Why

A sale outside the certified till breaks the inalterability duty and the till's closures. The owner asked for retail at
the desk ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)). The values come from
the point of sale rules
([CR-FR-024](../../../10-country-packs/france/point-of-sale/cr-fr-024-certified-till-software.md)).

## Examples

| Case | Result |
|---|---|
| Shampoo sold with a facial | one sale on the till |
| Product sold by a beautician from their own pocket | refused: it must go through the till |
| A wrong price after closing | a credit and a new sale |
| Till not closed for the day | the next sale is blocked |
| Refund of a product | a credit and stock returned |

## Applies to

- [UC-SC17-09](../use-cases/03-salon-retail-and-stock/uc-sc17-09-sell-products-at-the-desk.md)
- [E-F10-03](../../../02-functional/f10-point-of-sale/data/e-f10-03-point-of-sale-order.md)

## Exceptions

None.

## Configurable

The products on sale and their prices, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-08 Balances are shown before each sale](br-sc17-08-balances-are-shown-before-each-sale.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC17-10 Back-bar use lowers stock per service](br-sc17-10-back-bar-use-lowers-stock-per-service.md)
