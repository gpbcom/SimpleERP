🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-22 Loan interest is accrued each period

# 📏 BR-F8-22 Loan interest is accrued each period

**Status:** 🔄 waiting for the owner

## Statement

The interest of a loan is accrued in every accounting period for the days elapsed since the last instalment, whether or
not the instalment has been paid, and the accrual is reversed when the instalment is posted.

## Why

Interest belongs to the period in which it accrues
([CR-FR-064](../../../10-country-packs/france/accounting/cr-fr-064-accounting-frameworks.md)); leaving it to the payment
date misstates two periods. The owner asked for loans and borrowings
([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md)).

## Examples

| Case | Result |
|---|---|
| 25 days of interest between the last instalment and the period end | 25 days of interest are accrued |
| The instalment paid on the 5th of the next month | the accrual is reversed and the real interest posted |
| A loan repaid early in the period | interest is accrued up to the repayment date |
| A period already locked | the accrual goes to the next open period, flagged |
| A loan with a grace period | interest is accrued, no principal falls due |

## Applies to

- [UC-F8-30](../use-cases/11-treasury-and-payment-means/uc-f08-30-manage-loans-and-borrowings.md)
- [E-F8-34 Loan](../data/e-f08-34-loan.md)
- [E-F8-03 Journal entry](../data/e-f08-03-journal-entry.md)
- [E-F8-10 Fiscal period](../data/e-f08-10-fiscal-period.md)

## Exceptions

None.

## Configurable

No; the day-count convention of the contract is stored on the loan.

## Open questions

None.

---

⬅️ [BR-F8-21 Open questions are listed at closing](br-f08-21-open-questions-are-listed-at-closing.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-23](br-f08-23-a-cheque-or-lcr-is-posted-when-the-bank-credits-it.md)
