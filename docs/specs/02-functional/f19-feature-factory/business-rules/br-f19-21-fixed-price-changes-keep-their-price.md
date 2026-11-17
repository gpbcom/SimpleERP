🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-21 Fixed-price changes keep their price

# 📏 BR-F19-21 Fixed-price changes keep their price

**Status:** ✅ specified

## Statement

A catalogue change keeps the price and the committed date it had at the moment of the order: the customer pays that
price whatever the work takes, a later change of the catalogue's price does not touch an order already made, and nothing
is charged before the customer accepts the change.

## Why

A fixed price is a promise: if it moves with the effort it is only an estimate. The owner asked for a fixed-price
catalogue ([D538](../../../06-decisions/f19-feature-factory/d538-benchmark-gaps-f19-feature-factory.md)). The
France-pack rule on price display to businesses is written later.

## Examples

| Case | Result |
|---|---|
| Ordered at 150 EUR, built in two days more than planned | 150 EUR |
| Ordered at 150 EUR, catalogue raised to 170 EUR the next day | 150 EUR |
| Ordered and refused at the try-out | no charge |
| Ordered with a small correction asked later | same price |
| A change needing a second form | turned into a normal request with a quote |

## Applies to

- [UC-F19-28](../use-cases/07-catalogue-and-co-funding/uc-f19-28-order-a-fixed-price-change.md)
- [E-F19-17 Catalogue change](../data/e-f19-17-catalogue-change.md)
- [E-F19-01 Feature request](../data/e-f19-01-feature-request.md)

## Exceptions

A change the customer enlarges after ordering becomes a new order at its own price.

## Configurable

The catalogue, its prices and delays, by the simple-ERP team in the catalogue file.

## Open questions

None.

---

⬅️ [BR-F19-20 Similar features are shown before any quote](br-f19-20-similar-features-are-shown-before-any-quote.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F19-22](br-f19-22-pledges-are-charged-only-when-the-goal-is-met.md)
