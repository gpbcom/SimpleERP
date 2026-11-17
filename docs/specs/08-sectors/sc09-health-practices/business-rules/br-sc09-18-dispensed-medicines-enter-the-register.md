🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🩺 [SC09 Health practices](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC09-18 Dispensed medicines enter the register

# 📏 BR-SC09-18 Dispensed medicines enter the register

**Status:** 🔄 waiting for the owner

## Statement

A medicine given or sold to an animal is written in the practice's register with the animal, the medicine, the lot, the
quantity, the date and the vet before the act is saved. A medicine with no lot or no vet cannot be given in the system.

## Why

The register shows where each medicine went and allows a recall; a missing line is an offence and hides a possible
misuse. The owner asked for veterinary practices
([D553](../../../06-decisions/sectors/d553-benchmark-gaps-sc09-health-practices.md)). (Proposed) The France-pack rule is
written later.

## Examples

| Case | Result |
|---|---|
| Antibiotic, lot A-771, 14 tablets, dog Milo | register line written |
| Medicine with no lot | refused |
| Medicine only prescribed | no register line, the prescription is kept |
| Lot recalled | the register lists the animals concerned |
| Register line corrected | a new line, the old one stays in the history |

## Applies to

- [UC-SC09-23](../use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-23-run-a-veterinary-practice.md)
- [E-SC09-16 Animal](../data/e-sc09-16-animal.md)
- [E-SC09-03 Clinical record entry](../data/e-sc09-03-clinical-record-entry.md)

## Exceptions

None.

## Configurable

The years the register is kept, as data of the country pack.

## Open questions

None.

---

⬅️ [BR-SC09-17](br-sc09-17-lenses-follow-the-prescription-and-its-validity.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC09-19](br-sc09-19-prosthetics-need-the-regulated-quote-before-care.md)
