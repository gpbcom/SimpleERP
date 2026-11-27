🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-04 Filings need an accountant

# 📏 BR-F8-04 Filings need an accountant

**Status:** ✅ specified

## Statement

A tax return or filing (CA3/CA12, DAS2, liasse fiscale, OSS, FEC sent to the administration) is prepared by SimpleERP,
validated by an accountant, then filed through the EDI partner; the tax period is then locked; the filing receipt is
kept.

## Why

See [D278](../../../06-decisions/f08-accounting/d278-french-filings.md).

Legal values from the France country pack:
[CR-FR-011 VAT returns and tax filings](../../../10-country-packs/france/tax-and-vat/cr-fr-011-vat-returns-and-filings.md).

## Examples

| Case | Result |
|---|---|
| CA3 of October prepared | Waits for the accountant |
| Validated | Filed; the receipt kept; October tax-locked |

## Applies to

Every F8 use case concerned.

- [UC-F8-24 Compute and pay corporate tax and local business taxes](../use-cases/08-year-end-duties/uc-f08-24-compute-and-pay-corporate-tax-and-local-business-taxes.md)

- [UC-F8-25 Approve and file the annual accounts](../use-cases/08-year-end-duties/uc-f08-25-approve-and-file-the-annual-accounts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-03 Every bank line is reconciled](br-f08-03-every-bank-line-is-reconciled.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-05 Expenses need a receipt and an approval](br-f08-05-expenses-need-a-receipt-and-an-approval.md)
