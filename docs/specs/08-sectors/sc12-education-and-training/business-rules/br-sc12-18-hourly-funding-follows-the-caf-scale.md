🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎓 [SC12 Education and training](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC12-18 Hourly funding follows the CAF scale

# 📏 BR-SC12-18 Hourly funding follows the CAF scale

**Status:** 🔄 waiting for the owner

## Statement

The hourly rate a family pays is computed from the fund's scale for the date: the family's monthly income times the
percentage for its size, never below the floor or above the ceiling. When the income is not known, the ceiling rate is
used until it is.

## Why

The fund pays the nursery on the basis of the scale; a wrong rate means the nursery or the family is paid wrongly, and
the fund can reclaim. The owner asked for nurseries
([D556](../../../06-decisions/sectors/d556-benchmark-gaps-sc12-education-and-training.md)). The percentages,
the floor and the ceiling come from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| Income 2,400.00, 0.0615 % | 1.48 EUR an hour |
| Income above the ceiling | the ceiling rate |
| Income unknown | the ceiling rate, then corrected |
| Second child in the family | the rate for a family of three applies |
| New scale on 2027-01-01 | the rate is recomputed from that date |

## Applies to

- [UC-SC12-23](../use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-23-run-a-nursery.md)
- [E-SC12-22 Childcare place](../data/e-sc12-22-childcare-place.md)
- [E-SC12-05 Training funding](../data/e-sc12-05-training-funding.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-245 Nursery hourly funding (PSU)](../../../10-country-packs/france/education/cr-fr-245-nursery-psu.md)

## Exceptions

None.

## Configurable

The scale (percentages, floor, ceiling) by date, as data of the country pack.

## Open questions

None.

---

⬅️ [BR-SC12-17](br-sc12-17-lessons-are-taught-by-an-authorised-instructor.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC12-19 Bookings close at the cut-off time](br-sc12-19-bookings-close-at-the-cut-off-time.md)
