🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-05 Document numbering

# 📏 BR-F1-05 Document numbering

**Status:** ✅ specified

## Statement

A company numbers its invoices either with one company-wide sequence or with one series per site; each sequence is
continuous, with no gap and no duplicate.

## Why

French invoicing rules require unique, continuous numbering; series are allowed when each is continuous. See
[D66](../../../06-decisions/f01-administration/d66-site-documents-and-numbering.md).

Legal values from the France country pack:
[CR-FR-014 Invoice numbering](../../../10-country-packs/france/invoicing/cr-fr-014-invoice-numbering.md).

## Examples

| Setting | Invoices |
|---|---|
| Company-wide | INV-2026-0001, INV-2026-0002 whatever the site |
| Per site | LYO-2026-0001 and PAR-2026-0001, each series continuous |

## Applies to

- [UC-F1-02 Add or change a site](../use-cases/02-manage-sites/uc-f01-02-add-or-change-a-site.md); the invoices of F6.

## Exceptions

⬜ To be specified with F6 (credit notes, quotes and delivery notes).

## Configurable

Yes: the company's choice, set by the administrator. It cannot change once an invoice exists in the fiscal
year.

## Open questions

None.

---

⬅️ [BR-F1-04 Empty a site before closing it](br-f01-04-empty-a-site-before-closing-it.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-06 Invitation link valid 48 hours](br-f01-06-invitation-link-valid-48-hours.md)
