🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-19 Consigned stock is never valued as own stock

# 📏 BR-F7-19 Consigned stock is never valued as own stock

**Status:** ✅ specified

## Statement

Goods that a supplier or a customer still owns are never counted in the company's own stock value, never posted as its
asset and never paid for before use; the company's goods held at a customer's site stay in the company's stock value.

## Why

Valuing goods the company does not own overstates its assets and its debts
([CR-FR-007](../../../10-country-packs/france/accounting/cr-fr-007-annual-stock-count.md)); the owner asked for
consignment stock
([D526](../../../06-decisions/f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)).
[BR-F7-07 Costing method per category](br-f07-07-costing-method-per-category.md) values only the company's own stock.

## Examples

| Case | Result |
|---|---|
| 500 units consigned by the supplier | 0 EUR in the company's stock value |
| 120 units used | 120 units become a purchase to settle at the agreed price |
| Own goods at a customer's site | still in the company's stock value |
| Consigned goods sold to a customer | the sale and the purchase happen together, from the consigned owner |
| Consigned goods returned unused | no purchase, the owner's quantity falls |

## Applies to

- [UC-F7-25](../use-cases/10-consignment-scanning-and-edi/uc-f07-25-keep-consignment-stock.md)
- [E-F7-23 Stock owner](../data/e-f07-23-stock-owner.md)
- [E-F7-06 Item](../data/e-f07-06-item.md)
- [E-F7-04 Transfer](../data/e-f07-04-transfer.md)

## Exceptions

None.

## Configurable

Yes: per item, whether consigned stock is used before own stock.

## Open questions

None.

---

⬅️ [BR-F7-18 The supplier score uses the company's weights](br-f07-18-the-supplier-score-uses-the-companys-weights.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F7-20](br-f07-20-a-scan-that-does-not-match-the-expected-item-stops-the-step.md)
