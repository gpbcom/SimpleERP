🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F12-04 Lots traced both ways

# 📏 BR-F12-04 Lots traced both ways

**Status:** ✅ specified

## Statement

Each consumed lot or serial is recorded, so a finished lot leads to its component lots and back; in France:
[CR-FR-061 Food traceability](../../../10-country-packs/france/products/cr-fr-061-food-traceability.md),
[CR-FR-062 Product recall](../../../10-country-packs/france/products/cr-fr-062-product-recall.md).

## Why

See [D312](../../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md).

## Examples

| Case | Result |
|---|---|
| Recall of flour lot F-22 | Every finished lot and customer found |

## Applies to

Every F12 use case concerned.

- [UC-F12-31 Define a recipe and produce in batches](../use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md)

## Exceptions

None.

## Configurable

Products tracked by lot or serial.

## Open questions

None.

---

⬅️ [BR-F12-03 Components checked before start](br-f12-03-components-checked-before-start.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-05 Consumption never below zero](br-f12-05-consumption-never-below-zero.md)
