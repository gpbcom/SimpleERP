🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
📒 [Accounting](README.md) › ⚖️ CR-FR-216 Leases in French GAAP

# ⚖️ CR-FR-216 Leases in French GAAP

**Status:** ✅ specified

## Statement

In the French GAAP book a lease is a rent expense with a commitment note ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf), read 2026-11-27),
while the IFRS book records a right-of-use asset and a lease liability for every lease, short-term and low-value
leases excepted (IFRS 16, adopted by Regulation (EU) 2017/1986) ([European Commission, DG FISMA, Endorsement of IFRS 16](https://finance.ec.europa.eu/system/files/2018-01/171031-study-ifrs-16_en.pdf), read 2026-11-27); each book follows its
own standard.

## Values

- Rent expense and commitment note in the French GAAP book: the lessee of a credit-bail books the rentals as
  expenses and enters the asset only when the purchase option is taken up (212-5); the notes give the rentals
  still to pay, the residual price and the theoretical depreciation (836-3, 836-4) ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf), read 2026-11-27).
- No right-of-use asset in that book: the
  consolidated PCG has no right-of-use asset and no election for one ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf), read 2026-11-27).
- SimpleERP enforces: a lease follows the standard of each book.
- Read on
  [the ANC consolidated chart of accounts](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf)
  (ANC regulation 2014-03, version at 1 January 2026), articles 212-5, 836-3 and 836-4 only; the election of another
  treatment is not read:
- Read: art. 212-5, the holder of a credit-bail contract books the sums due for the rental period as expenses; when the
  purchase option is taken up, the asset is entered on the balance sheet at the entry value set by the usual rules.
- Read: account 612 (6122 movable, 6125 property) takes the invoices for rent of leased assets; account 613 exists for
  other rentals.
- Read: art. 836-3, for assets under credit-bail the notes give the rentals still to pay and the residual purchase
  price, split between movable and property credit-bail.
- Read: art. 836-4, the notes also give the value of the assets at signature, the rentals of the year and the cumulative
  rentals of earlier years, the depreciation that would have been booked had the assets been bought (year and
  cumulative), and the rentals still to pay with the residual price, by balance-sheet item and by maturity (up to one
  year, one to five years, over five years).
- Read: off-balance-sheet accounts 8016 (80161 movable, 80165 property) record the credit-bail rentals still to run.
- Not read: a right-of-use election and plain operating leases beyond the account headings; the Legifrance version of
  the regulation was not located; each article's own date and any penalty are not on the page.

## Legal references

- Plan comptable général (ANC regulation 2014-03) art. 212-5, 836-3, 836-4, consolidated version
  of 1 January 2026 ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf)).
- IFRS 16 Leases, adopted in the EU by Regulation (EU) 2017/1986 ([European Commission, DG FISMA, Endorsement of IFRS 16](https://finance.ec.europa.eu/system/files/2018-01/171031-study-ifrs-16_en.pdf)).

## Effective dates

ANC regulation 2014-03 has no first financial year of its own: it applies from 2014-10-16, the day after the
homologating arrêté was published ([Arrêté of 8 September 2014](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029583307), [ANC regulation 2014-03, art. 1 and 2](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/2014/Reglt2014-03/Reglt%202014-03_Plan%20comptable%20general.pdf), read 2026-11-27); the consolidated version of
1 January 2026 gives no date per article ([ANC, PCG consolidated at 1 January 2026](https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/Reglements/Recueils/PCG_janvier2026/PCG--1er-janvier-2026.pdf), read 2026-11-27). IFRS 16: for annual periods beginning on or after 2019-01-01 ([European Commission, DG FISMA, Endorsement of IFRS 16](https://finance.ec.europa.eu/system/files/2018-01/171031-study-ifrs-16_en.pdf), read 2026-11-27).

## Enforced by

- [BR-F8-29 Leases follow the book's standard](../../../02-functional/f08-accounting/business-rules/br-f08-29-leases-follow-the-books-standard.md)
- [UC-F8-37 Account for leases](../../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-37-account-for-leases.md)

## When the law changes

Watched in the law corpus: Lease accounting in the French chart of accounts. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

Books kept under IFRS.

## Open questions

The law on leases in the French chart of accounts is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-215 BSPCE and free shares](../company/cr-fr-215-bspce-and-free-shares.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-217 Cash-basis books for BNC professions](cr-fr-217-cash-basis-books-for-bnc.md)
