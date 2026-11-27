🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-19 Sector templates carry the sector's mandatory information

# 📏 BR-F18-19 Sector templates carry the sector's mandatory information

**Status:** ✅ specified

## Statement

A sector page template shows the information the law requires for that sector, taken from the ERP: allergens on a
restaurant menu, fees on a health practice's site, energy and diagnostic figures on property listings; a page missing it
stays in the preview.

## Why

[CR-FR-107 Allergen information](../../../10-country-packs/france/consumer/cr-fr-107-allergen-information.md),
[CR-FR-130 Fee display](../../../10-country-packs/france/health-practice/cr-fr-130-fee-display.md),
[CR-FR-144 Property diagnostics](../../../10-country-packs/france/real-estate/cr-fr-144-property-diagnostics.md).

## Examples

| Case | Result |
|---|---|
| Menu page with each dish's allergens from SC06 recipes | passes |
| Dish with no allergen information | fails: page held, dish listed |
| Listing with no energy class | fails: page held |

## Applies to

- [UC-F18-25 Use a sector page template](../use-cases/06-content-and-search/uc-f18-25-use-a-sector-page-template.md)

## Exceptions

None.

## Configurable

The company chooses which template pages to use.

## Open questions

None.

---

⬅️ [BR-F18-18 Forms protected without tracking](br-f18-18-forms-protected-without-tracking.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-20 Search basics from public data only](br-f18-20-search-basics-from-public-data-only.md)
