🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧮 [Tax and VAT](README.md) › ⚖️ CR-FR-272 VAT on advance payments for services

# ⚖️ CR-FR-272 VAT on advance payments for services

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

For a service, VAT becomes chargeable when the advance payment, the price or the fee is collected, or on the supplier's
option when it is invoiced; for a service on which the business customer accounts for the VAT (reverse charge), it is
chargeable when the service is done or when an advance is collected
([Code général des impôts, art. 269, 2, b bis and
c](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827), read 2026-11-27). A pledge collected towards a
co-funded feature is therefore taxed when it is collected, at the rate and place of the service it pays for
([CR-FR-100](cr-fr-100-vat-on-services-abroad.md)); an invoice follows
[CR-FR-015](../invoicing/cr-fr-015-invoice-mandatory-mentions.md) and a refund is a credit note
([CR-FR-200](../invoicing/cr-fr-200-credit-notes.md)).

## Values

- Chargeability of a service: on collection of each advance, of the price or of the fee, to the amount collected, or on
  the debits on the supplier's option (269, 2, c) ([CGI, art.
  269](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827), read 2026-11-27).
- Reverse-charged service (283, 2): chargeable at the taxable event (the service done) or on collection of an advance
  (269, 2, b bis); for a continuous reverse-charged service of more than a year without accounts or payments, at the end
  of each calendar year (269, 1, a quater) ([CGI, art.
  269](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827), read 2026-11-27).
- A pledge charged only when the goal is met is collected, and so taxed, only at that date; a pledge never collected
  bears no VAT.
- (⚖️ lawyer review before launch, D574) Whether a pledge that gives the pledger no right of its own (the feature
  ships to every user) is still the consideration for a service: the texts read do not say. SimpleERP takes the
  conservative reading and taxes each collected pledge as the price of a service.
- (⚖️ lawyer review before launch, D574) From 2027-01-01, CGI art. 269 is repealed and taken over by the Code des
  impositions sur les biens et services (ordonnance n° 2025-1247, art. 9 and 49, read in
  [CR-FR-181](cr-fr-181-ticket-vat-rates.md)); the CIBS articles that take it over are not read.
- SimpleERP enforces: each pledge collected gets its VAT by the pledger's country and status, and each refund a credit
  note.

## Legal references

- [Code général des impôts, art. 269](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827), version in
  force since 2023-01-01, repealed from 2027-01-01 by ordonnance n° 2025-1247, read 2026-11-27.

## Effective dates

Art. 269 in its version since 2023-01-01 (loi n° 2021-1900), for advances collected from that date; repealed from
2027-01-01, except the first and last paragraphs of 2, c, kept until the CIBS regulatory measures of L234-15 take them
over ([CGI, art. 269](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827), read 2026-11-27).

## Enforced by

- [UC-F19-29 Co-fund a feature](../../../02-functional/f19-feature-factory/use-cases/07-catalogue-and-co-funding/uc-f19-29-co-fund-a-feature.md)

## When the law changes

Watched in the law corpus: CGI art. 269 and the CIBS articles that take it over. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

None stated in the article read.

## Exceptions

Building contractors may opt to pay VAT on delivery for the works a decree sets (269, 2, c).

## Open questions

None: the law was read on 2026-11-27; the nature of a pledge and the CIBS articles are lawyer items above.

---

⬅️ [CR-FR-271 General terms and prices for business buyers](../trade/cr-fr-271-terms-and-prices-for-businesses.md) · ⬆️ [Up](README.md) · ➡️ [CR-FR-273 Valuations the law requires](../company/cr-fr-273-valuations-required-by-law.md)
