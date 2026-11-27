🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🎓 [Education](README.md) › ⚖️ CR-FR-245 Nursery hourly funding (PSU)

# ⚖️ CR-FR-245 Nursery hourly funding (PSU)

**Status:** ✅ specified

## Statement

A nursery funded by the family allowance fund applies the fund's scale: the family pays an hourly rate that is a
percentage of its monthly income, lower for larger families, within a floor and a ceiling, and the fund pays 66 % of the
cost price, within a ceiling price, for the hours billed to families, minus the families' share, times the share of
families in the general scheme ([CNAF PSU
guide](https://www.caf.fr/sites/default/files/medias/671/Guide%20PSU%2012-2025_2.pdf), September 2025, section 1.4, read
2026-11-27). The nursery reports the hours to the fund.

## Values

- Percentages, floor and ceiling by date, kept as data: the 2024 and 2025 scales are dated (2025: floor 801.00 EUR a
  month, ceiling 7 000 EUR then 8 500 EUR from the September 2025 billing) ([CNAF PSU guide](https://www.caf.fr/sites/default/files/medias/671/Guide%20PSU%2012-2025_2.pdf), annex 6, read 2026-11-27).
- Hours reported to the fund: the nursery keeps an attendance list to count the hours done, declared to the fund, and
  records the hours done and billed to justify its declarations ([CNAF PSU guide](https://www.caf.fr/sites/default/files/medias/671/Guide%20PSU%2012-2025_2.pdf), sections 1.3 and 2, read 2026-11-27).
- SimpleERP enforces: hourly funding follows the family allowance scale.
- Read in the
  [CNAF Prestation de Service Unique guide](https://www.caf.fr/sites/default/files/medias/671/Guide%20PSU%2012-2025_2.pdf)
  (September 2025), scale of 2025; the 2026 scale, the ceiling price of 2025 and the legal references are not read:
- Read: hourly effort rate for collective care and micro-nurseries: 1 child 0.0619 %; 2 children 0.0516 %; 3 children
  0.0413 %; 4 to 7 children 0.0310 %; 8 to 10 children 0.0206 %.
- Read: family or parental care column: 0.0516 %, 0.0413 %, 0.0310 %, 0.0310 %, 0.0310 %, 0.0206 % and 0.0206 % beyond.
- Read: formula (annual income used / 12) x hourly effort rate x reserved hours; the income is the N-2 household income;
  only alimony paid is deductible.
- Read: floor income 801.00 EUR a month; ceiling income 7 000 EUR a month from the September 2024 billing and 8 500 EUR
  a month from the September 2025 billing; the manager may go beyond with the fund's agreement.
- Read: a child with a disability allowance in the family brings the next lower rate; the PSU is 66 % of the cost price,
  within a ceiling price set each year by CNAF.

## Legal references

- CNAF PSU guide (September 2025) and CNAF circulars 2014-009 and 2019-005; Code de la santé publique R2324-17,
  R2324-46.

## Effective dates

2025 scale applied from 2025-01-01 to 2025-12-31; the 2026 scale is not read ([CNAF PSU guide](https://www.caf.fr/sites/default/files/medias/671/Guide%20PSU%2012-2025_2.pdf), annex 6,
read 2026-11-27).

## Enforced by

- [BR-SC12-18 Hourly funding follows the CAF scale](../../../08-sectors/sc12-education-and-training/business-rules/br-sc12-18-hourly-funding-follows-the-caf-scale.md)
- [UC-SC12-23 Run a nursery](../../../08-sectors/sc12-education-and-training/use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-23-run-a-nursery.md)

## When the law changes

Watched in the law corpus: Nursery funding. A change flags this rule and warns the administrators; the corrected rule
ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None stated.

## Open questions

The law on the hourly funding of nurseries is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-244 Apprenticeship funding by the OPCO](cr-fr-244-apprenticeship-funding.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-246 Research and innovation tax credits](../tax-and-vat/cr-fr-246-research-tax-credit.md)
