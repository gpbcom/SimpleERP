🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏢 [Company identity](README.md) › ⚖️ CR-FR-001 Company identifiers

# ⚖️ CR-FR-001 Company identifiers

**Status:** ✅ specified

## Statement

A French company is identified by its SIREN, each establishment by its SIRET, and its VAT number is derived from the
SIREN.

## Values

- SIREN: 9 digits with a Luhn check digit.
- SIRET: 14 digits, SIREN plus a 5-digit establishment number (NIC).
- Intra-EU VAT number: `FR` + a 2-digit key + SIREN, key = (12 + 3 × (SIREN mod 97)) mod 97.

## Legal references

- SIRENE register, INSEE.
- [Code général des impôts](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/) art. 286 ter (VAT
  identification number).

## Effective dates

Since 2025-01-01: CGI 286 ter ([CGI, art. 286 ter](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048826954), read 2026-11-27); the SIRENE
numbering rules not read for their date.

## Enforced by

- [Data](../../../02-functional/f01-administration/data/README.md)
- [Regulatory](../../../02-functional/f01-administration/regulatory.md)
- [UC-F1-01 Set up a new company](../../../02-functional/f01-administration/use-cases/01-guided-setup/uc-f01-01-set-up-a-new-company.md)
- [Data](../../../02-functional/f06-customers-and-sales/data/README.md)
- [Regulatory](../../../02-functional/f06-customers-and-sales/regulatory.md)
- [Q11 Establishment SIRET](../../../07-questions/q11-establishment-siret.md)

## When the law changes

Watched in the law corpus: CGI art. 286 ter. A change flags this rule and warns the administrators; the corrected rule
ships in a pack update (D294).

## Penalty

None stated in the sources read.

## Exceptions

Companies outside France use their own country pack's identifiers.

## Open questions

[Q11 Establishment SIRET](../../../07-questions/q11-establishment-siret.md).
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬆️ [Up](README.md) ·
➡️ [CR-FR-002 Accounting records kept 10 years](../accounting/cr-fr-002-accounting-records-kept-ten-years.md)
