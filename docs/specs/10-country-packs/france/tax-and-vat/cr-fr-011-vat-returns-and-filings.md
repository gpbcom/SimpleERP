🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧮 [Tax and VAT](README.md) › ⚖️ CR-FR-011 VAT returns and tax filings

# ⚖️ CR-FR-011 VAT returns and tax filings

**Status:** ✅ specified

## Statement

VAT returns and the other tax filings are prepared in the official forms and filed electronically, through an EDI
partner, then the period is locked.

## Values

- CA3 monthly or quarterly (normal regime), CA12 yearly (simplified regime) until 2026-12-31; from 2027-01-01 the
  simplified VAT regime is abolished and only the normal regime remains ([impots.gouv.fr, micro-entrepreneur and VAT](https://www.impots.gouv.fr/professionnel/questions/je-suis-micro-entrepreneur-ou-la-tete-dune-micro-entreprise-ai-je-des), read 2026-11-27).
- DAS2, OSS, Intrastat (DEB) and the liasse fiscale.
- Electronic filing: EDI-TVA, EDI-TDFC.

## Legal references

- [Code général des impôts](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/) art. 287 (VAT returns),
  1649 quater B quater (electronic filing), 240 (DAS2).

## Effective dates

Since 2025-06-19: art. 287 in force since 2025-01-01, art. 1649 quater B quater since 2025-06-19, art. 240 since
2016-02-01 ([CGI, art. 287](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048826856), [art. 1649 quater B quater](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051764508), [art. 240](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030751913), read 2026-11-27). For the VAT returns, until 2026-12-31, CGI art. 287 applies; from 2027-01-01, the Code des impositions sur les biens et services, Book II, the declarations (L216-24 to L216-32),
in force on that date ([Ordonnance n° 2025-1247](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053091516), [art. 49](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054587047) as amended by Ordonnance n° 2026-671, read 2026-11-27); on invoices,
contracts and acts that produce effects until 2028-06-30 (art. 46 II as
amended by Ordonnance n° 2026-671, [BOFiP, BOI-RES-TVA-000253 of 2026-10-07](https://bofip.impots.gouv.fr/bofip/14901-PGP.html/identifiant=BOI-RES-TVA-000253-20261007), read 2026-11-27), a reference to the CGI is read as one to the CIBS
article that takes it over ([Ordonnance n° 2025-1247](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053091516), [art. 46](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053091753), read 2026-11-27).
From 2027-01-01 the CGI rules on the VAT returns (art. 287), the simplified regime itself ending on that date stay
applicable until the regulatory part of the CIBS takes them over ([BOFiP, BOI-RES-TVA-000253 of 2026-10-07](https://bofip.impots.gouv.fr/bofip/14901-PGP.html/identifiant=BOI-RES-TVA-000253-20261007), 2.3 and 3.1, read 2026-11-27).

## Enforced by

- [BR-F8-04 Filings need an accountant](../../../02-functional/f08-accounting/business-rules/br-f08-04-filings-need-an-accountant.md)
- [Data](../../../02-functional/f08-accounting/data/README.md)
- [Regulatory](../../../02-functional/f08-accounting/regulatory.md)
- [UC-F8-07 Manage VAT and file returns](../../../02-functional/f08-accounting/use-cases/04-tax-assets-and-analytics/uc-f08-07-manage-vat-and-file-returns.md)

## When the law changes

Watched in the law corpus: CGI art. 287, 1649 quater B quater, 240. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

A return filed late: a surcharge of 10 % of the tax, 40 % when it is not filed within 30 days of a
formal notice, 80 % when a hidden activity is found (art. 1728), plus late-payment interest (art. 1727) ([CGI, art. 1728](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784), [art. 1727](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330), read 2026-11-27).

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-010 When VAT is due](cr-fr-010-vat-due-date.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-012 Mileage allowance scale](cr-fr-012-mileage-scale.md)
