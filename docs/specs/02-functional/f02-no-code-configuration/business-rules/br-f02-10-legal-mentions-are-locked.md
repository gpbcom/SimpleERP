🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-10 Legal mentions are locked

# 📏 BR-F2-10 Legal mentions are locked

**Status:** ✅ specified

## Statement

simple-ERP adds the mentions French law requires on each document type, and a template cannot remove or hide them; it
can only place and style them.

## Why

An invoice missing a mandatory mention is not compliant. See
[D118](../../../06-decisions/f02-no-code-configuration/d118-document-template-features.md).

Legal values from the France country pack:
[CR-FR-015 Mandatory invoice mentions](../../../10-country-packs/france/invoicing/cr-fr-015-invoice-mandatory-mentions.md).

## Examples

On an invoice: number, date, seller and buyer identities and addresses, SIREN, VAT numbers, the date of the
sale or service, quantities, unit prices and VAT rates, totals, the payment due date, the late-payment penalty rate and
the fixed recovery indemnity; with e-invoicing, the buyer's SIREN and the nature of the operation. The exact list per
document type is to be checked with its sources in F6 and F8.

| Case | Result |
|---|---|
| Delete the "late-payment penalties" block | Refused: the block is locked |
| Move it to the footer, in small type | Allowed, down to the minimum legible size |

## Applies to

- [UC-F2-05](../use-cases/02-customise-documents-and-emails/uc-f02-05-edit-a-document-template.md); F6, F7, F8.
- [UC-F2-25 Merge a sector pack upgrade with local changes](../use-cases/10-change-safely/uc-f02-25-merge-a-sector-pack-upgrade-with-local-changes.md)

## Exceptions

None.

## Configurable

Their place and style only.

## Open questions

None.

---

⬅️ [BR-F2-09 New record types start closed](br-f02-09-new-record-types-start-closed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-11 Electronic formats with the PDF](br-f02-11-electronic-formats-with-the-pdf.md)
