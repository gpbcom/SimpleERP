🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC05-16 Excise is due when goods leave the bonded warehouse

# 📏 BR-SC05-16 Excise is due when goods leave the bonded warehouse

**Status:** 🔄 waiting for the owner

## Statement

Excise is due on a lot when it leaves the bonded warehouse for consumption, and only then. The duty is the volume of
pure alcohol multiplied by the rate of the lot's category on the day of release. A movement under suspension, an export
or a destruction creates no duty but needs its document.

## Why

Declaring on production instead of release would tax stock that is still held under suspension, and missing a release
would leave duty unpaid. The owner asked for alcohol excise
([D549](../../../06-decisions/sectors/d549-benchmark-gaps-sc05-manufacturing.md)). (Proposed) The France-pack rule is
written later.

## Examples

| Case | Result |
|---|---|
| Lot released on 3 October | the duty uses the rate in force on 3 October |
| Lot produced but still in the warehouse | no duty, state Bonded |
| Lot sent to another bonded warehouse | no duty, document attached |
| Release without a strength | refused |
| Goods returned after release | the duty is claimed back with the next declaration |

## Applies to

- [UC-SC05-16](../use-cases/06-excise-refurbishment-and-cutting/uc-sc05-16-declare-alcohol-excise.md)
- [E-SC05-15 Bonded stock](../data/e-sc05-15-bonded-stock.md)
- [E-F8-06 Tax return](../../../02-functional/f08-accounting/data/e-f08-06-tax-return.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-234 Alcohol excise and bonded warehouses](../../../10-country-packs/france/tax-and-vat/cr-fr-234-alcohol-excise.md)

## Exceptions

None.

## Configurable

The tolerance for losses in the warehouse and the reminder delay, by accounting within the limits of the country pack.

## Open questions

None.

---

⬅️ [BR-SC05-15 Standards' texts licensed](br-sc05-15-standards-texts-licensed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC05-17 Every refurbished unit is graded and tested](br-sc05-17-every-refurbished-unit-is-graded-and-tested.md)
