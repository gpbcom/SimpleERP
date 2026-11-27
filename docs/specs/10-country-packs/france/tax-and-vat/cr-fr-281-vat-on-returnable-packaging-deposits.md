🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧮 [Tax and VAT](README.md) › ⚖️ CR-FR-281 VAT on deposits for returnable packaging

# ⚖️ CR-FR-281 VAT on deposits for returnable packaging

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

The sums charged as a deposit on returnable packaging may be left out of the VAT base on condition that no VAT is
invoiced on them; they enter the base when the packaging is not returned within the time usual in the trade
([Code général des impôts, art. 267, III](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042910064), read
2026-11-27). Packaging costs charged to the customer are otherwise part of the base
([art. 267, I, 2°](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042910064), read 2026-11-27).

## Values

- Deposit on returnable packaging: outside the VAT base, invoiced without VAT, while the packaging can still be
  returned (267, III).
- Packaging not returned within the time usual in the trade: the deposit enters the VAT base (267, III).
- Packaging costs that are not a refundable deposit: in the VAT base (267, I, 2°).
- (⚖️ lawyer review before launch, D574) The "time usual in the trade" is not a figure of the law: it is set per trade
  by the company; and from 2027-01-01 CGI art. 267 is repealed and taken over by the Code des impositions sur les biens
  et services (ordonnance n° 2025-1247, art. 9), whose article is not read.
- SimpleERP enforces: a deposit line carries no VAT; when the return period of the trade ends without a return, the
  deposit is invoiced with VAT.

## Legal references

- [Code général des impôts, art. 267](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042910064), version in
  force since 2020-12-31, repealed from 2027-01-01 by ordonnance n° 2025-1247, read 2026-11-27.

## Effective dates

Art. 267 in its version since 2020-12-31 (loi n° 2020-1721), until 2026-12-31
([CGI, art. 267](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042910064), read 2026-11-27).

## Enforced by

- [UC-F7-28 Track returnable packaging and deposits](../../../02-functional/f07-purchasing-and-stock/use-cases/10-consignment-scanning-and-edi/uc-f07-28-track-returnable-packaging-and-deposits.md)

## When the law changes

Watched in the law corpus: CGI art. 267 and the CIBS article that takes it over. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

None stated in the article read.

## Exceptions

None stated.

## Open questions

None: the law was read on 2026-11-27; the return period and the CIBS article are a lawyer item above.

---

⬅️ [CR-FR-280 Personal data shared inside a group](../data-protection/cr-fr-280-personal-data-shared-inside-a-group.md) · ⬆️ [Up](README.md) · ➡️ [CR-FR-282 Police form for foreign guests](../hospitality/cr-fr-282-police-form-for-foreign-guests.md)
