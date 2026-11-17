🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
📒 [Accounting](README.md) › ⚖️ CR-FR-216 Leases in French GAAP

# ⚖️ CR-FR-216 Leases in French GAAP

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) In the French GAAP book a lease is a rent expense with a commitment note, while the IFRS book records a
right-of-use asset and a lease liability; each book follows its own standard.

## Values

- (Proposed) Rent expense and commitment note in the French GAAP book.
- (Proposed) No right-of-use asset in that book unless the entity elects another treatment, to read.
- (Proposed) simple-ERP enforces: a lease follows the standard of each book.
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

- Law to read: leases in the French chart of accounts (not read yet).

## Effective dates

(Proposed) To read.

## Enforced by

- [BR-F8-29 Leases follow the book's standard](../../../02-functional/f08-accounting/business-rules/br-f08-29-leases-follow-the-books-standard.md)
- [UC-F8-37 Account for leases](../../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-37-account-for-leases.md)

## When the law changes

Watched in the law corpus: Lease accounting in the French chart of accounts. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

(Proposed) Books kept under IFRS.

## Open questions

The law on leases in the French chart of accounts is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-215 BSPCE and free shares](../company/cr-fr-215-bspce-and-free-shares.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-217 Cash-basis books for BNC professions](cr-fr-217-cash-basis-books-for-bnc.md)
