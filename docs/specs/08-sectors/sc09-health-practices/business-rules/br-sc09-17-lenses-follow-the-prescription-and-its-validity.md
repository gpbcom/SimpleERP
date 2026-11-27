🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC09-17 Lenses follow the prescription and its validity

# 📏 BR-SC09-17 Lenses follow the prescription and its validity

**Status:** ✅ specified

## Statement

Lenses are ordered only to the correction of a prescription that is valid for the wearer on the day of the order, or
adapted by the optician within the rules, and only after the patient has signed the quote. A prescription past its
validity blocks the order.

## Why

Lenses made to an old or wrong correction harm the wearer, and the health insurance and the complementary cover pay only
a valid prescription. The owner asked for opticians
([D553](../../../06-decisions/sectors/d553-benchmark-gaps-sc09-health-practices.md)). The validity values
come from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| Adult wearer, prescription of 2025-09-10 | valid, the order may go on |
| Prescription past its validity, adaptation not allowed | no lens ordered |
| Adaptation by the optician within the rules | recorded with the optician's name |
| Quote not signed | the lab order is not sent |
| Child wearer | a shorter validity from the pack |

## Applies to

- [UC-SC09-22](../use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-22-sell-eyewear-to-a-prescription.md)
- [E-SC09-15 Eyewear order](../data/e-sc09-15-eyewear-order.md)
- [E-SC09-04 Prescription](../data/e-sc09-04-prescription.md)

## Exceptions

None.

## Configurable

The validity by age band, as data of the country pack; the delay of the renewal reminder, by the optician.

## Open questions

None.

---

⬅️ [BR-SC09-16](br-sc09-16-prescription-medicines-need-a-valid-prescription.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC09-18 Dispensed medicines enter the register](br-sc09-18-dispensed-medicines-enter-the-register.md)
