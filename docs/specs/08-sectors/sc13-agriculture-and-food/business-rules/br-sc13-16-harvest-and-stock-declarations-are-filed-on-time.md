🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC13-16 Harvest and stock declarations are filed on time

# 📏 BR-SC13-16 Harvest and stock declarations are filed on time

**Status:** 🔄 waiting for the owner

## Statement

The harvest of each plot is recorded and declared by the date of the country pack, and the stock of wine is declared
each year from the cellar lots. A plot whose yield is above the limit of its appellation has its excess volume marked
and kept out of the appellation. A declaration is not filed while a plot lacks its harvest.

## Why

A late or incomplete declaration brings penalties and an excess sold as the appellation breaks its rules. The owner
asked for vineyards ([D557](../../../06-decisions/sectors/d557-benchmark-gaps-sc13-agriculture-and-food.md)).
The France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Plot with a harvest and a yield under the limit | declared with the campaign |
| Plot above its limit | the excess volume is marked and not declared as appellation wine |
| Plot not harvested at the declaration date | the declaration stays in review |
| Wine sent under suspension | no duty, the document is attached to the lot |
| Stock declaration with a lot of unknown origin | refused until the origin is entered |

## Applies to

- [UC-SC13-21](../use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-21-run-the-vineyard-and-the-cellar.md)
- [E-SC13-17 Vine plot](../data/e-sc13-17-vine-plot.md)
- [E-SC13-04 Lot](../data/e-sc13-04-lot.md)
- [E-F8-06 Tax return](../../../02-functional/f08-accounting/data/e-f08-06-tax-return.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-249 Harvest and stock declarations](../../../10-country-packs/france/agriculture/cr-fr-249-vineyard-declarations.md)

## Exceptions

None.

## Configurable

The declaration dates and yield limits by campaign, from the country pack, and the reminder delay by the farmer.

## Open questions

None.

---

⬅️ [BR-SC13-15 Offline in the field](br-sc13-15-offline-in-the-field.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC13-17](br-sc13-17-jobs-are-billed-by-hectare-or-hour-as-agreed.md)
