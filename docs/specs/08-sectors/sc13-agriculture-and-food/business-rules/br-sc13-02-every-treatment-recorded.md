🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC13-02 Every treatment recorded

# 📏 BR-SC13-02 Every treatment recorded

**Status:** ✅ specified

## Statement

Each plant-protection treatment is recorded in the establishment's electronic register with product, dose, area
treated, crop, plot and date; the operator may be recorded but is not required; in France:
[CR-FR-161 Register of plant-protection treatments](../../../10-country-packs/france/agriculture/cr-fr-161-plant-protection-register.md).

## Why

Until 2025-12-31 the register of the arrêté du 16 juin 2009 could be kept on any medium. From 2026-01-01 it is
electronic and machine-readable, kept per establishment (SIRET), with the product's trade name and authorisation
number, the date, the dose, the area or quantity treated, the crop and the location; the operator's name is not
required, and the register is kept at least 5 years (CR-FR-161, arrêté du 24 décembre 2025).

## Examples

| Case | Result |
|---|---|
| Treatment without operator | Line complete, the operator left empty |
| Treatment without its dose or area | Line incomplete, flagged |

## Applies to

Every SC13 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC13-01 Agriculture follows the country pack](br-sc13-01-agriculture-follows-the-country-pack.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC13-03 Animals notified on time](br-sc13-03-animals-notified-on-time.md)
