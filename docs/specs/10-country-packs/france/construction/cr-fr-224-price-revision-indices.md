🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🏗️ [Construction](README.md) › ⚖️ CR-FR-224 Price revision with BT and TP indices

# ⚖️ CR-FR-224 Price revision with BT and TP indices

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) A works contract may carry a clause that revises the price with the monthly building (BT) or public works
(TP) index published by the national statistics office; the clause names the index, the base month and the formula.
Public works contracts above a certain length must carry such a clause.

## Values

- (Proposed) Index, base month and formula named in the contract.
- (Proposed) Provisional revision when the index is not yet published, corrected when it is.
- (Proposed) simple-ERP enforces: revisions use the index of the contract's month.
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

- Law to read: price revision indices in works contracts (not read yet).

## Effective dates

(Proposed) To read.

## Enforced by

- [BR-SC01-16 Revisions use the index of the contract's month](../../../08-sectors/sc01-construction/business-rules/br-sc01-16-revisions-use-the-index-of-the-contracts-month.md)
- [UC-SC01-16 Revise prices with the BT and TP indices](../../../08-sectors/sc01-construction/use-cases/06-revision-developers-bim-and-grants/uc-sc01-16-revise-prices-with-the-bt-and-tp-indices.md)

## When the law changes

Watched in the law corpus: Price revision in works contracts. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

(Proposed) Contracts with a firm price.

## Open questions

The law on price revision indices in works contracts is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-223 Legal conformity guarantee](../consumer/cr-fr-223-legal-conformity-guarantee.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-225 Off-plan sales (VEFA) calls for funds](../real-estate/cr-fr-225-off-plan-sales.md)
