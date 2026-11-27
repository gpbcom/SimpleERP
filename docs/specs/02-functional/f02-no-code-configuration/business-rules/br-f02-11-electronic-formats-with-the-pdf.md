🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-11 Electronic formats with the PDF

# 📏 BR-F2-11 Electronic formats with the PDF

**Status:** ✅ specified

## Statement

Each invoice is generated in the structured e-invoicing formats (Factur-X, UBL, CII) alongside its PDF, from the same
data, whatever the template's look.

## Why

French e-invoicing requires structured invoices; the template only changes the look. See
[D118](../../../06-decisions/f02-no-code-configuration/d118-document-template-features.md).

Legal values from the France country pack:
[CR-FR-016 Electronic invoicing](../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md).

## Examples

| Template | Output |
|---|---|
| "Detailed quote" | PDF only (quotes are not invoices) |
| "Short invoice", English | PDF in English, and the structured invoice with the same amounts |
| A Factur-X invoice | One PDF/A-3 file carrying the structured data |

## Applies to

- [UC-F2-05](../use-cases/02-customise-documents-and-emails/uc-f02-05-edit-a-document-template.md); F6, F7; submission
  through the platform of [Q13](../../../07-questions/q13-e-invoicing-platforms.md).

## Exceptions

None.

## Configurable

The default format per customer, among those the platform accepts.

## Open questions

- [Q13 E-invoicing platforms](../../../07-questions/q13-e-invoicing-platforms.md)

---

⬅️ [BR-F2-10 Legal mentions are locked](br-f02-10-legal-mentions-are-locked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-12 Rule accounts never exceed their author](br-f02-12-rule-accounts-never-exceed-their-author.md)
