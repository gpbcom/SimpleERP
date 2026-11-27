🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC05-17 Every refurbished unit is graded and tested

# 📏 BR-SC05-17 Every refurbished unit is graded and tested

**Status:** ✅ specified

## Statement

A refurbished unit is sold only when every test of its family has passed, its data erasure has a certificate and a grade
has been confirmed by the quality manager. The grade follows the criteria in the settings and cannot be higher than the
tests allow.

## Why

A unit sold as tested that was not, or that still holds the previous owner's data, harms the customer and the company.
The owner asked for refurbishment ([D549](../../../06-decisions/sectors/d549-benchmark-gaps-sc05-manufacturing.md)).
The France-pack rule on refurbished products is
[CR-FR-278 Refurbished products](../../../10-country-packs/france/products/cr-fr-278-refurbished-products.md).

## Examples

| Case | Result |
|---|---|
| All tests passed, certificate present, grade confirmed | the unit goes to stock for sale |
| Erasure without certificate | no grade |
| Battery below the grade's minimum | the grade drops one level or the battery is replaced |
| Unit that fails the screen test | sent to repair, not graded |
| Returned unit | its history reopens and it is tested again |

## Applies to

- [UC-SC05-17](../use-cases/06-excise-refurbishment-and-cutting/uc-sc05-17-refurbish-electronics.md)
- [E-SC05-16 Graded unit](../data/e-sc05-16-graded-unit.md)
- [E-F12-07](../../../02-functional/f12-manufacturing/data/e-f12-07-quality-control-point.md)

## Exceptions

None.

## Configurable

The grade criteria and the share of units sampled each day, by the quality manager.

## Open questions

None.

---

⬅️ [BR-SC05-16](br-sc05-16-excise-is-due-when-goods-leave-the-bonded-warehouse.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC05-18](br-sc05-18-production-starts-only-after-the-proof-is-approved.md)
