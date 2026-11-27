🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-03 Labels follow price changes

# 📏 BR-SC02-03 Labels follow price changes

**Status:** ✅ specified

## Statement

A price change prints new labels for the stores holding the product, or updates electronic labels through a connector,
before it applies.

## Why

See [D320](../../../06-decisions/sectors/d320-retail-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| New price from Monday | Labels queued for 4 stores on Friday |

## Applies to

Every SC02 use case concerned.

## Exceptions

None.

## Configurable

Paper or electronic labels per store.

## Open questions

None.

---

⬅️ [BR-SC02-02 Every product priced, with its unit price](br-sc02-02-every-product-priced.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC02-04 Sales only in the legal periods](br-sc02-04-sales-only-in-the-legal-periods.md)
