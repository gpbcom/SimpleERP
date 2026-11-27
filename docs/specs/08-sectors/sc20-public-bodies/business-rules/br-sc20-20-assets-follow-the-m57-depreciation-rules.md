🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-20 Assets follow the M57 depreciation rules

# 📏 BR-SC20-20 Assets follow the M57 depreciation rules

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

An asset is depreciated from its commissioning over the duration of its category in the pack, never from a typed
duration, and a work in progress is not depreciated. At year end the register must agree with the public accountant's
inventory or each difference is explained.

## Why

Wrong depreciation changes the body's accounts, and a register that differs from the accountant's blocks the closing of
the year ([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). (⚖️ lawyer review before launch, D574)
The France-pack rule
[CR-FR-250 Public accounting M57](../../../10-country-packs/france/accounting/cr-fr-250-public-accounting-m57.md) does
not hold the depreciation rules yet: to read the M57 instruction (durations by category, depreciation from
commissioning) and its status after Ordonnance n° 2025-526.

## Examples

| Case | Result |
|---|---|
| Commissioned on 1 September | depreciation from that date |
| Work in progress | not depreciated |
| Category with no duration | cannot be commissioned |
| Land | not depreciated |
| Asset of the previous framework | keeps its value and remaining duration |

## Applies to

- [UC-SC20-20](../use-cases/05-council-registry-permits-and-assets/uc-sc20-20-keep-the-public-assets-register.md)
- [E-SC20-15 Public asset](../data/e-sc20-15-public-asset.md)
- [E-SC20-15 Public asset](../data/e-sc20-15-public-asset.md)
- [E-F8-07 Fixed asset](../../../02-functional/f08-accounting/data/e-f08-07-fixed-asset.md)

## Exceptions

None.

## Configurable

The durations by category and the assets that are not depreciated, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC20-19](br-sc20-19-silence-after-the-legal-delay-counts-as-the-law-says.md) · ⬆️ [Up](README.md)
