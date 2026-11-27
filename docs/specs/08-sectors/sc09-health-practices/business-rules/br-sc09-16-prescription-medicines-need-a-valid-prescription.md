🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC09-16 Prescription medicines need a valid prescription

# 📏 BR-SC09-16 Prescription medicines need a valid prescription

**Status:** ✅ specified

## Statement

A medicine on prescription is dispensed only against a valid prescription that has not ended and still has the quantity
asked. Each dispensation reduces the quantity left on the prescription, and a dispensation with no valid prescription is
refused and its reason recorded.

## Why

Handing out a medicine without a valid prescription exposes the patient and the pharmacist, and the health insurance
does not pay it. The owner asked for pharmacies
([D553](../../../06-decisions/sectors/d553-benchmark-gaps-sc09-health-practices.md)). The values come from
the France pack, written later.

## Examples

| Case | Result |
|---|---|
| 3 packs prescribed, 1 dispensed | 2 left, the next dispensation is allowed |
| Prescription ended yesterday | refused |
| Quantity asked above the quantity left | refused for the excess |
| No prescription for a medicine that needs one | refused |
| Electronic prescription number read | its content is filled in and checked |

## Applies to

- [UC-SC09-21](../use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-21-dispense-in-a-pharmacy.md)
- [E-SC09-14 Dispensation](../data/e-sc09-14-dispensation.md)
- [E-SC09-04 Prescription](../data/e-sc09-04-prescription.md)

## Exceptions

A medicine that does not need a prescription may be sold without one; the pharmacist's own advice is recorded.

## Configurable

The list of medicines that need a prescription and their validity, as data of the country pack; the days before the end
of a prescription at which a repeat is proposed, by the pharmacist.

## Open questions

None.

---

⬅️ [BR-SC09-15 Certifications kept current](br-sc09-15-certifications-kept-current.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC09-17](br-sc09-17-lenses-follow-the-prescription-and-its-validity.md)
