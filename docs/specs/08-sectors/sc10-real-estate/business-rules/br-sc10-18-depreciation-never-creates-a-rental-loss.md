🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏘️ [SC10 Real estate](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC10-18 Depreciation never creates a rental loss

# 📏 BR-SC10-18 Depreciation never creates a rental loss

**Status:** ✅ specified

## Statement

Depreciation of a furnished rental is deducted only up to the rental result before depreciation of the year; it never
creates or increases a rental loss. The part not deducted is carried forward and used in the next years, within their
results.

## Why

The tax rules allow depreciation only against the rental result; deducting more would be wrong in the return. The owner
asked for furnished rentals ([D554](../../../06-decisions/sectors/d554-benchmark-gaps-sc10-real-estate.md)).
The values of the year come from the France pack ([CR-FR-240](../../../10-country-packs/france/tax-and-vat/cr-fr-240-furnished-rentals-lmnp.md)).

## Examples

| Case | Result |
|---|---|
| Result 3,100, depreciation 4,400 | 3,100 deducted, 1,300 carried forward |
| Result negative | nothing deducted, all carried forward |
| Next year result 5,000, carried 1,300 | 1,300 used |
| Simplified regime | no depreciation, the allowance applies |
| Property sold | the file is closed, the carry-forward is kept in the history |

## Applies to

- [UC-SC10-23](../use-cases/07-short-stays-commercial-and-coworking/uc-sc10-23-keep-furnished-rental-figures.md)
- [E-SC10-19 Furnished property](../data/e-sc10-19-furnished-property.md)
- [E-SC10-09 Rent call](../data/e-sc10-09-rent-call.md)
- France-pack rule:
  [CR-FR-240 Furnished rentals (LMNP)](../../../10-country-packs/france/tax-and-vat/cr-fr-240-furnished-rentals-lmnp.md)

## Exceptions

None.

## Configurable

The depreciation years by component and the yearly values, as data of the country pack and the property file.

## Open questions

None.

---

⬅️ [BR-SC10-17](br-sc10-17-rents-are-indexed-on-ilc-or-ilat-within-the-caps.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC10-19](br-sc10-19-rooms-are-booked-within-the-memberships-credits.md)
