🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-20 Identifiers are checked per scheme

# 📏 BR-F6-20 Identifiers are checked per scheme

**Status:** ✅ specified

## Statement

Every identifier is stored with its scheme and checked by that scheme's rule when it is entered and again when it is
used on a document; an identifier that fails its check is never printed on an invoice, a filing or an exchange.

## Why

Schemes differ in length, characters and check digit, and a wrong number makes an invoice rejected by the buyer or the
platform. The owner asked for several identifiers per company
([D525](../../../06-decisions/f06-customers-and-sales/d525-benchmark-gaps-f06-customers-and-sales.md)); company
identifiers are in [CR-FR-001](../../../10-country-packs/france/company/cr-fr-001-company-identifiers.md).

## Examples

| Case | Result |
|---|---|
| A SIREN of 9 digits with a valid check digit | Valid |
| A SIRET of 14 digits whose first 9 digits differ from the company's SIREN | refused: the establishment does not belong to the company |
| A VAT number the register reports inactive | Invalid, invoices held |
| An identifier of a scheme the country pack does not know | refused with the list of known schemes |
| A VAT number checked 400 days ago, used on a new invoice | checked again first |

## Applies to

- [UC-F6-28](../use-cases/10-partners-contracts-and-warranties/uc-f06-28-keep-several-identifiers-per-company.md)
- [E-F6-24 Company identifier](../data/e-f06-24-company-identifier.md)
- [E-F6-01 Customer record](../data/e-f06-01-customer-record.md)
- [E-F6-05 Invoice](../data/e-f06-05-invoice.md)

## Exceptions

A scheme with no public check (some foreign registers) is saved as Entered, marked unchecked, and never blocks a
document.

## Configurable

Yes: the schemes and their rules, by the country packs.

## Open questions

None.

---

⬅️ [BR-F6-19 Forwarded leads leave their owner's pipeline](br-f06-19-forwarded-leads-leave-their-owners-pipeline.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F6-21](br-f06-21-call-offs-never-exceed-the-balance-without-approval.md)
