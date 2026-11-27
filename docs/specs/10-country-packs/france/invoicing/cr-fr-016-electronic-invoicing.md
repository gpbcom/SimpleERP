🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧾 [Invoicing](README.md) › ⚖️ CR-FR-016 Electronic invoicing

# ⚖️ CR-FR-016 Electronic invoicing

**Status:** ✅ specified

## Statement

Invoices between French companies are exchanged as structured e-invoices through a registered platform: every company
receives them from 1 September 2026 and issues them from its size's date.

## Values

- Reception: every company from 2026-09-01.
- Issuing: large and mid-size companies from 2026-09-01, small and micro companies from 2027-09-01.
- Formats: Factur-X, UBL or CII, from the same data as the PDF.
- Through a registered platform (PA) chosen by the company; public buyers through Chorus Pro.

## Legal references

- [Code général des impôts](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/) art. 289 bis.
- [DGFiP e-invoicing reform](https://www.impots.gouv.fr/professionnel/facturation-electronique).

## Effective dates

2026-09-01 and 2027-09-01, by company size. Until 2026-12-31, CGI art. 289 bis applies; from 2027-01-01, the Code des impositions sur les biens et services, Book II, the invoices (L216-33 to L216-46) and the reliability of tax data (L216-47 to L216-56),
in force on that date ([Ordonnance n° 2025-1247](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053091516), [art. 49](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054587047) as amended by Ordonnance n° 2026-671, read 2026-11-27); on invoices,
contracts and acts that produce effects until 2028-06-30 (art. 46 II as
amended by Ordonnance n° 2026-671, [BOFiP, BOI-RES-TVA-000253 of 2026-10-07](https://bofip.impots.gouv.fr/bofip/14901-PGP.html/identifiant=BOI-RES-TVA-000253-20261007), read 2026-11-27), a reference to the CGI is read as one to the CIBS
article that takes it over ([Ordonnance n° 2025-1247](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053091516), [art. 46](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053091753), read 2026-11-27).
From 2027-01-01 the CGI rules on the invoice format and its electronic transmission (art. 289 bis) stay
applicable until the regulatory part of the CIBS takes them over ([BOFiP, BOI-RES-TVA-000253 of 2026-10-07](https://bofip.impots.gouv.fr/bofip/14901-PGP.html/identifiant=BOI-RES-TVA-000253-20261007), 2.3 and 3.1, read 2026-11-27).

## Enforced by

- [BR-F2-11 Electronic formats with the PDF](../../../02-functional/f02-no-code-configuration/business-rules/br-f02-11-electronic-formats-with-the-pdf.md)
- [Regulatory](../../../02-functional/f06-customers-and-sales/regulatory.md)
- [Regulatory](../../../02-functional/f07-purchasing-and-stock/regulatory.md)
- [E-invoicing platforms](../../../05-non-functional/e-invoicing-platforms.md)
- [Legal rules in France](../../../05-non-functional/legal-france.md)
- [Q8 E-invoicing dates](../../../07-questions/q08-e-invoicing-dates.md)
- [Q13 E-invoicing platforms](../../../07-questions/q13-e-invoicing-platforms.md)

## When the law changes

Watched in the law corpus: CGI art. 289 bis. A change flags this rule and warns the administrators; the corrected rule
ships in a pack update (D294).

## Penalty

50 EUR per invoice not issued electronically, at most 15 000 EUR a calendar year, for invoices issued from
2026-09-01; not applied to a first breach corrected within 30 days (CGI 1737 III, V) ([CGI, art. 1737](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546686), read 2026-11-27).
From 2027-01-01, the same fines, the e-invoicing duties now in the Code des impositions sur les
biens et services ([CGI, art. 1737, version of 2027-01-01](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546686/2027-01-02), read 2026-11-27).

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-015 Mandatory invoice mentions](cr-fr-015-invoice-mandatory-mentions.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-017 E-reporting of sales to consumers and abroad](cr-fr-017-e-reporting.md)
