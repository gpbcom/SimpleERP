🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-03 Trips within driving times

# 📏 BR-SC07-03 Trips within driving times

**Status:** ✅ specified

## Statement

A trip is assigned to a driver only if it fits their remaining driving and rest times. Trips are built by the
shared rounds optimiser, which respects working time,
[BR-F9-22 Rounds respect travel, skills, continuity and working time](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-22-rounds-respect-travel-skills-continuity-and-working-time.md);
transport adds the driving and rest times of the country pack; in France:
[CR-FR-117 Driving and rest times](../../../10-country-packs/france/transport/cr-fr-117-driving-and-rest-times.md).

## Why

The limits are those of [CR-FR-117](../../../10-country-packs/france/transport/cr-fr-117-driving-and-rest-times.md): 9 hours of driving a day (10 hours
twice a week), 56 hours a week and 90 hours over two weeks; a 45-minute break after 4 h 30 of driving; a daily rest of
11 hours and a weekly rest of 45 hours, with the reductions the regulation allows.

## Examples

| Case | Result |
|---|---|
| 3 h left, trip 4 h | Refused, relay proposed |

## Applies to

Every SC07 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC07-02 Vehicles within the licence](br-sc07-02-vehicles-within-the-licence.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-04 Documents on board complete](br-sc07-04-documents-on-board-complete.md)
