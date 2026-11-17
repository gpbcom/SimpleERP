🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-07 Invoice numbers never break

# 📏 BR-F6-07 Invoice numbers never break

**Status:** ✅ specified

## Statement

Invoices and credit notes are numbered in a continuous sequence per company, never reused or deleted; an issued invoice
can no longer change: mistakes are corrected by a credit note.

## Why

See [D251](../../../06-decisions/f06-customers-and-sales/d251-sales-cycle.md).

Legal values from the France country pack:
[CR-FR-014 Invoice numbering](../../../10-country-packs/france/invoicing/cr-fr-014-invoice-numbering.md).

## Examples

| Case | Result |
|---|---|
| An issued invoice with a wrong price | A credit note, then a new invoice |
| A draft deleted | Its number was never given |

## Applies to

Every F6 use case concerned.

- [UC-F6-19 Invoice a public buyer through Chorus Pro](../use-cases/07-special-invoicing/uc-f06-19-invoice-a-public-buyer-through-chorus-pro.md)

- [UC-F6-20 Invoice several payers with funders and caps](../use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F6-06 Progress invoices and retention](br-f06-06-progress-invoices-and-retention.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-08 VAT is shown wherever it matters](br-f06-08-vat-is-shown-wherever-it-matters.md)
