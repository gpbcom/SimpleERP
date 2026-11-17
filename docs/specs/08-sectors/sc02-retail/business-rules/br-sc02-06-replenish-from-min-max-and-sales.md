🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-06 Replenish from min, max and sales

# 📏 BR-SC02-06 Replenish from min, max and sales

**Status:** ✅ specified

## Statement

Store replenishment is proposed from each store's minimum, maximum and sales; a transfer from a store with excess comes
before a purchase.

## Why

See [D320](../../../06-decisions/sectors/d320-retail-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Lyon 1 short, Lyon 2 in excess | Transfer proposed |

## Applies to

Every SC02 use case concerned.

## Exceptions

None.

## Configurable

Min and max per store and product.

## Open questions

None.

---

⬅️ [BR-SC02-05 Reductions show the reference price](br-sc02-05-reductions-show-the-reference-price.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC02-07 Transfers in transit](br-sc02-07-transfers-in-transit.md)
