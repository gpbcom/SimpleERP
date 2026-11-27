🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-32 Cash-basis books record receipts and payments only

# 📏 BR-F8-32 Cash-basis books record receipts and payments only

**Status:** ✅ specified

## Statement

A cash-basis book records only receipts and payments, each on the date the money moved; it holds no receivable, payable,
accrual, deferral or stock entry, and an invoice or a bill creates an entry in it only when it is paid.

## Why

A cash-basis book follows the money, not the invoices; mixing accruals into it would make it neither kind of book. The
owner asked for cash-basis books ([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md));
[BR-F8-10 Several books share one source](br-f08-10-books-share-one-source.md) lets several books share one source
without sharing their treatment. The France-pack rule is
[CR-FR-217 Cash-basis books for BNC professions](../../../10-country-packs/france/accounting/cr-fr-217-cash-basis-books-for-bnc.md): a
chronological book of receipts and payments and a register of fixed assets.

## Examples

| Case | Result |
|---|---|
| An invoice issued in November and paid in January | an entry in January only |
| A bill received in December and paid in February | an entry in February only |
| A year-end accrual | refused in this book |
| A stock of goods at year end | not recorded in this book |
| A refund of a payment | a negative payment on the refund's date |

## Applies to

- [UC-F8-40](../use-cases/12-audit-leases-and-special-books/uc-f08-40-keep-cash-basis-books.md)
- [E-F8-13 Book](../data/e-f08-13-book.md)
- [E-F8-03 Journal entry](../data/e-f08-03-journal-entry.md)
- France-pack rule:
  [CR-FR-217 Cash-basis books for BNC professions](../../../10-country-packs/france/accounting/cr-fr-217-cash-basis-books-for-bnc.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-31](br-f08-31-trips-outside-the-travel-policy-need-approval.md) · ⬆️ [Up](README.md)
