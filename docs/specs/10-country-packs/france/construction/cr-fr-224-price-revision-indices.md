🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏗️ [Construction](README.md) › ⚖️ CR-FR-224 Price revision with BT and TP indices

# ⚖️ CR-FR-224 Price revision with BT and TP indices

**Status:** ✅ specified

## Statement

A works contract may carry a clause that revises the price with the monthly building (BT) or public works (TP) index
published by the national statistics office; the clause names the index, the base month and the formula. In public
contracts, a price is revisable when the parties face major hazards from foreseeable economic changes; a revision clause
with an official index is mandatory for contracts of more than 3 months with a large share of supplies priced on world
markets (R2112-13, R2112-14); a fixed-price works contract carries an actualisation clause (R2112-10) ([Code de la
commande publique, art. R2112-7 to R2112-14](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000037730977), read
2026-11-27).

## Values

- Index, base month and formula named in the contract: the clauses set the date of the initial price, the way the
  revision is computed (a reference index, a cost formula with a possible fixed term, or both) and how often it
  applies ([Code de la commande publique, art. R2112-13](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000037730977), since 2019-04-01, read 2026-11-27); private contracts not read.
- Provisional revision when the index is not yet published, corrected when it is: in a public works contract under
  the CCAG-Travaux 2021, an interim statement uses the last coefficients calculated and says so (art. 12.2.1), interim
  amounts do not bind the parties (art. 12.2.3), and the revision of the balance is notified within ten days of the
  index's publication (art. 12.4.2) ([arrêté du 30 mars 2021, CCAG-Travaux](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043310463), published 2021-04-01, read 2026-11-27); private
  contracts follow their own clause.
- SimpleERP enforces: revisions use the index of the contract's month.
- Read on [Service-public F23387](https://entreprendre.service-public.gouv.fr/vosdroits/F23387) (verified 1 January
  2025), public works contracts only; private works are not read:
- Read: actualisation applies when more than 3 months pass between price-fixing and start of performance; mandatory in
  public works; applied only once per contract; without a clause, the CCAG-Travaux 9.4.3 formula, initial price times
  (index at start minus 3 months) over the index at the price-fixing date.
- Read: works prices are fixed unless the contract documents give a revision formula (in the CCAP); default indices
  BTP01 for mainly building works and TP01 for mainly civil engineering works.
- Read: index publication lags by 3 months (December index published end of March); the initial index is at the offer
  date (final offer date after negotiation), the final index no later than the scheduled or actual execution date
  (CCAG-Travaux 9.4.4).
- Read: Code de la commande publique L2112-6, R2112-9 to R2112-12 (fixed price), R2112-13 (revisable price).

## Legal references

- Code de la commande publique L2112-6, R2112-7 to R2112-14; CCAG-Travaux (arrêté du 30 mars 2021), art. 12.

## Effective dates

R2112-10 to R2112-14 since 2019-04-01 ([Code de la commande publique](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000037730977), read 2026-11-27).

## Enforced by

- [BR-SC01-16 Revisions use the index of the contract's month](../../../08-sectors/sc01-construction/business-rules/br-sc01-16-revisions-use-the-index-of-the-contracts-month.md)
- [UC-SC01-16 Revise prices with the BT and TP indices](../../../08-sectors/sc01-construction/use-cases/06-revision-developers-bim-and-grants/uc-sc01-16-revise-prices-with-the-bt-and-tp-indices.md)

## When the law changes

Watched in the law corpus: Price revision in works contracts. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

Contracts with a firm price: a firm price does not change during the contract (R2112-9), apart from its
actualisation (R2112-10, R2112-11) ([Code de la commande publique](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000037730977), since 2019-04-01, read 2026-11-27).

## Open questions

None, read on 2026-11-27.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-223 Legal conformity guarantee](../consumer/cr-fr-223-legal-conformity-guarantee.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-225 Off-plan sales (VEFA) calls for funds](../real-estate/cr-fr-225-off-plan-sales.md)
