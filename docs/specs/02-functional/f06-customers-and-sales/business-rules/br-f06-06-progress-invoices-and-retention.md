🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-06 Progress invoices and retention

# 📏 BR-F6-06 Progress invoices and retention

**Status:** ✅ specified

## Statement

Deposits and progress invoices (by percentage or by line) are deducted from the final invoice; when the contract sets a
retention guarantee (5 % in French construction), it is deducted from each invoice and released after the guarantee
period (one year from acceptance of the works) or against a bank guarantee.

## Why

See [D258](../../../06-decisions/f06-customers-and-sales/d258-invoicing-schemes.md).

Legal values from the France country pack:
[CR-FR-021 Construction retention guarantee](../../../10-country-packs/france/invoicing/cr-fr-021-construction-retention-guarantee.md).

## Examples

| Case | Result |
|---|---|
| 30 % deposit, 2 progress invoices, final | Final deducts all three |
| Retention 5 % | Deducted, released after one year |

## Applies to

Every F6 use case concerned.

- [UC-F6-19 Invoice a public buyer through Chorus Pro](../use-cases/07-special-invoicing/uc-f06-19-invoice-a-public-buyer-through-chorus-pro.md)

## Exceptions

None.

## Configurable

Yes: per contract.

## Open questions

None.

---

⬅️ [BR-F6-05 Reminders run on their own](br-f06-05-reminders-run-on-their-own.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-07 Invoice numbers never break](br-f06-07-invoice-numbers-never-break.md)
