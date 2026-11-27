🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧾 [Invoicing](README.md) › ⚖️ CR-FR-015 Mandatory invoice mentions

# ⚖️ CR-FR-015 Mandatory invoice mentions

**Status:** ✅ specified

## Statement

Every invoice carries the mentions the law requires; templates may place and style them but never remove them.

## Values

- Number, date, seller and buyer identities and addresses, SIREN, VAT numbers, date of sale or service.
- Quantities, unit prices, VAT rate per line, totals excluding VAT, VAT per rate, total including VAT.
- Due date, late-payment penalty rate and the 40 EUR recovery indemnity (business customers).
- With e-invoicing: the buyer's SIREN, the delivery address if different, the nature of the operation (goods, services
  or both), and the option for VAT on debits.

## Legal references

- CGI annex II art. 242 nonies A.
- [Code de commerce](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000005634379/) art. L441-9.
- [DGFiP e-invoicing reform](https://www.impots.gouv.fr/professionnel/facturation-electronique).

## Effective dates

Start date to read in the official source; in force when read on 2026-11-11, the date of this specification.

## Enforced by

- [BR-F2-10 Legal mentions are locked](../../../02-functional/f02-no-code-configuration/business-rules/br-f02-10-legal-mentions-are-locked.md)
- [Regulatory](../../../02-functional/f02-no-code-configuration/regulatory.md)
- [UC-F2-05 Edit a document template](../../../02-functional/f02-no-code-configuration/use-cases/02-customise-documents-and-emails/uc-f02-05-edit-a-document-template.md)
- [BR-F15-08 Document checks list, never rewrite](../../../02-functional/f15-legal-assistant/business-rules/br-f15-08-document-checks-list-never-rewrite.md)

## When the law changes

Watched in the law corpus: CGI annex II 242 nonies A; CCom L441-9. A change flags this rule and warns the
administrators; the corrected rule ships in a pack update (D294).

## Penalty

Not read yet (CGI art. 1737 sets fines for missing mentions).

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-014 Invoice numbering](cr-fr-014-invoice-numbering.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-016 Electronic invoicing](cr-fr-016-electronic-invoicing.md)
