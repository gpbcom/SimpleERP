🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧮 [Tax and VAT](README.md) › ⚖️ CR-FR-011 VAT returns and tax filings

# ⚖️ CR-FR-011 VAT returns and tax filings

**Status:** ✅ specified

## Statement

VAT returns and the other tax filings are prepared in the official forms and filed electronically, through an EDI
partner, then the period is locked.

## Values

- CA3 monthly or quarterly (normal regime), CA12 yearly (simplified regime).
- DAS2, OSS, Intrastat (DEB) and the liasse fiscale.
- Electronic filing: EDI-TVA, EDI-TDFC.

## Legal references

- [Code général des impôts](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/) art. 287 (VAT returns),
  1649 quater B quater (electronic filing), 240 (DAS2).

## Effective dates

Start date to read in the official source; in force when read on 2026-11-11, the date of this specification.

## Enforced by

- [BR-F8-04 Filings need an accountant](../../../02-functional/f08-accounting/business-rules/br-f08-04-filings-need-an-accountant.md)
- [Data](../../../02-functional/f08-accounting/data/README.md)
- [Regulatory](../../../02-functional/f08-accounting/regulatory.md)
- [UC-F8-07 Manage VAT and file returns](../../../02-functional/f08-accounting/use-cases/04-tax-assets-and-analytics/uc-f08-07-manage-vat-and-file-returns.md)

## When the law changes

Watched in the law corpus: CGI art. 287, 1649 quater B quater, 240. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-010 When VAT is due](cr-fr-010-vat-due-date.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-012 Mileage allowance scale](cr-fr-012-mileage-scale.md)
