🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎓 [SC12 Education and training](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC12-16 Funding follows the contract's support level

# 📏 BR-SC12-16 Funding follows the contract's support level

**Status:** ✅ specified

## Statement

The funding claimed from the OPCO for an apprenticeship contract follows the support level set for its diploma: a
yearly amount counted pro rata of the days done under the contract and paid in instalments. For a contract of more
than one year, 40 % within 30 days of the centre's invoice, 30 % in the seventh month, 20 % in the tenth month, and the
balance with the next year's advance or the final invoice, which is lost if not sent within four months of the end; a
contract under one year gets one 50 % advance. After a break, while the apprentice stays in the centre to find a new
employer, the funding goes on pro rata of the days for up to six months or until the new contract. A contract with no
support level, or days after the funding's end, are not claimed.

## Why

The OPCO pays what the level and the days done allow, and a claim above it is reclaimed. The owner asked for
apprentice training centres ([D556](../../../06-decisions/sectors/d556-benchmark-gaps-sc12-education-and-training.md)).
The levels come from the France pack and the branches, and the instalments and the break rule from the Code du travail
R6332-25 for contracts from 2025-07-01 (CR-FR-244).

## Examples

| Case | Result |
|---|---|
| Level 7,500.00 a year, two-year contract, first invoice | 3,000.00 EUR (40 %) |
| Break on 2026-12-15, the apprentice stays in the centre | claims go on pro rata of the days, at most to 2027-06-15 |
| Break on 2026-12-15, a new contract on 2027-02-01 | no claim for the old contract after 2027-01-31 |
| Diploma with no level | no claim, the level is requested |
| OPCO corrects the level | the claims are recomputed |
| Apprentice changes employer | a new contract for the rest |

## Applies to

- [UC-SC12-21](../use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-21-run-an-apprentice-training-centre.md)
- [E-SC12-20 Apprenticeship contract](../data/e-sc12-20-apprenticeship-contract.md)
- [E-SC12-05 Training funding](../data/e-sc12-05-training-funding.md)
- France-pack rule:
  [CR-FR-244 Apprenticeship funding by the OPCO](../../../10-country-packs/france/education/cr-fr-244-apprenticeship-funding.md)

## Exceptions

None.

## Configurable

The support levels by diploma and branch, as data of the country pack.

## Open questions

None.

---

⬅️ [BR-SC12-15 E-learning tracked](br-sc12-15-e-learning-tracked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC12-17](br-sc12-17-lessons-are-taught-by-an-authorised-instructor.md)
