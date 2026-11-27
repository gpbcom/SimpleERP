🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC05-02 Recipes scale with potency

# 📏 BR-SC05-02 Recipes scale with potency

**Status:** ✅ specified

## Statement

A batch recipe follows the shared recipes capability: it scales to the batch size and keeps its tolerances,
[BR-F12-26 Recipes scale to the batch and keep their tolerances](../../../02-functional/f12-manufacturing/business-rules/br-f12-26-recipes-scale-to-the-batch-and-keep-their-tolerances.md).
Manufacturing adds only this: ingredients are corrected by their measured potency, and yields are recorded per batch.

## Why

See [D329](../../../06-decisions/sectors/d329-manufacturing-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Potency 95 % | Ingredient raised by 5.3 % |

## Applies to

Every SC05 use case concerned.

## Exceptions

None.

## Configurable

Potency per ingredient.

## Open questions

None.

---

⬅️ [BR-SC05-01](br-sc05-01-manufacturing-sector-follows-the-country-pack.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC05-03 Configured products stay valid](br-sc05-03-configured-products-stay-valid.md)
