🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-10 Back-bar use lowers stock per service

# 📏 BR-SC17-10 Back-bar use lowers stock per service

**Status:** 🔄 waiting for the owner

## Statement

Each service that uses a product records the quantity used and its lot; stock of the product falls by that quantity, and
the quantity proposed is the service's recipe unless the beautician enters another. A use above the recipe by more than
the tolerance is flagged.

## Why

Without it stock never matches, the true cost of a service is unknown and a recalled lot cannot be traced to the
clients. The owner asked for salon retail and stock
([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)).

## Examples

| Case | Result |
|---|---|
| Recipe 60 g, used 65 g | saved, within the tolerance |
| Used 100 g | saved and flagged |
| Recalled lot picked | refused |
| Visit cancelled | the use is cancelled, stock returns |
| Product not in the recipe | added and flagged |

## Applies to

- [UC-SC17-10](../use-cases/03-salon-retail-and-stock/uc-sc17-10-record-products-used-in-services.md)
- [E-SC17-07 Product use](../data/e-sc17-07-product-use.md)
- [E-SC17-07 Product use](../data/e-sc17-07-product-use.md)

## Exceptions

A salon that does not track back-bar products may switch the recording off for a product.

## Configurable

The recipes and the tolerance, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-09 Retail sales go through the certified till](br-sc17-09-retail-sales-go-through-the-certified-till.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC17-11 Orders follow minimum stock per salon](br-sc17-11-orders-follow-minimum-stock-per-salon.md)
