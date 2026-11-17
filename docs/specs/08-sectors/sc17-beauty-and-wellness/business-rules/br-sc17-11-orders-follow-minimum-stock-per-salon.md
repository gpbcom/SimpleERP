🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-11 Orders follow minimum stock per salon

# 📏 BR-SC17-11 Orders follow minimum stock per salon

**Status:** 🔄 waiting for the owner

## Statement

Orders are proposed per salon from the salon's own minimum stock per product; a salon is never ordered for from another
salon's minimum, and a product held in another salon may be transferred before it is ordered.

## Why

A single company-wide minimum leaves one salon empty and another overstocked. The owner asked for salon retail and stock
([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| Minimum 5 in Rue Verte, 2 in stock | Rue Verte is proposed an order |
| Same product at 12 in another salon | a transfer is proposed first |
| Pack size 6 | the quantity is rounded to 6 |
| Free delivery above 150 EUR | the missing amount is shown |
| Product with no minimum | never proposed |

## Applies to

- [UC-SC17-11](../use-cases/03-salon-retail-and-stock/uc-sc17-11-replenish-the-salon.md)
- [E-F7-09](../../../02-functional/f07-purchasing-and-stock/data/e-f07-09-reordering-rule.md)

## Exceptions

None.

## Configurable

The minimum per product and salon, and the review period, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-10 Back-bar use lowers stock per service](br-sc17-10-back-bar-use-lowers-stock-per-service.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC17-12 Products keep their safety sheet and batch](br-sc17-12-products-keep-their-safety-sheet-and-batch.md)
