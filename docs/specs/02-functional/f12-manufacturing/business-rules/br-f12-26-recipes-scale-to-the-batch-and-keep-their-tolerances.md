🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-26 Recipes scale to the batch and keep their tolerances

# 📏 BR-F12-26 Recipes scale to the batch and keep their tolerances

**Status:** ✅ specified

## Statement

A batch scales its recipe's quantities to the batch size; each ingredient is weighed by lot within its tolerance, and
the batch lot records its ingredient lots, yield and best-before.

## Why

The shared recipe model of D457: the same product every batch, traced.

## Examples

| Case | Result |
|---|---|
| 400 L for a 100 L recipe | x4 |
| Rennet +4 %, tolerance 2 % | Out of tolerance |

## Applies to

- [UC-F12-31 Define a recipe and produce in batches](../use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-25](br-f12-25-passport-data-come-from-records-with-their-source.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-27 Only released revisions reach the shop floor](br-f12-27-only-released-revisions-reach-the-shop-floor.md)
