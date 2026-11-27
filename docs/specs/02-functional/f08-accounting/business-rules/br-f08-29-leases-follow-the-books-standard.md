🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-29 Leases follow the book's standard

# 📏 BR-F8-29 Leases follow the book's standard

**Status:** ✅ specified

## Statement

A lease is accounted for in each book by that book's standard: as a right-of-use asset and a lease liability in a book
that follows the IFRS lease standard, and as rent in the period (with the commitment disclosed) in a book that follows
French GAAP; the same lease record feeds every book and no book is derived from another.

## Why

Books of one company follow different standards and the lease must not be accounted for twice in the same way
([CR-FR-064](../../../10-country-packs/france/accounting/cr-fr-064-accounting-frameworks.md)). The owner asked for lease
accounting ([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md));
[BR-F8-10 Several books share one source](br-f08-10-books-share-one-source.md) makes books share one source.
In the French GAAP book a lease is a rent expense with a commitment note, with no right-of-use asset: the consolidated
PCG has none and no election for one, and a credit-bail asset enters that book only when the purchase option is taken
up ([CR-FR-216 Leases in French GAAP](../../../10-country-packs/france/accounting/cr-fr-216-leases-in-french-gaap.md)).

## Examples

| Case | Result |
|---|---|
| A 5-year lease in an IFRS book | a liability and a right-of-use asset, interest and depreciation |
| The same lease in the French GAAP book | rent each period, the commitment in the notes |
| An indexation after one year | the IFRS liability is remeasured, the French GAAP rent changes |
| A short-term lease the IFRS book chose to expense | payments expensed in both books |
| A lease with no book standard set | stays Draft |

## Applies to

- [UC-F8-37](../use-cases/12-audit-leases-and-special-books/uc-f08-37-account-for-leases.md)
- [E-F8-41 Lease](../data/e-f08-41-lease.md)
- [E-F8-13 Book](../data/e-f08-13-book.md)
- [E-F8-07 Fixed asset](../data/e-f08-07-fixed-asset.md)
- France-pack rule:
  [CR-FR-216 Leases in French GAAP](../../../10-country-packs/france/accounting/cr-fr-216-leases-in-french-gaap.md)

## Exceptions

A short-term lease or a low-value asset may be expensed in an IFRS book if its settings say so.

## Configurable

Yes: per book, the standard and the exemptions for short-term and low-value leases.

## Open questions

None.

---

⬅️ [BR-F8-28](br-f08-28-the-auditor-reads-only-and-every-view-is-logged.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-30](br-f08-30-peppol-serves-only-flows-outside-the-french-platforms.md)
