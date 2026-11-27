🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-08 Document checks list, never rewrite

# 📏 BR-F15-08 Document checks list, never rewrite

**Status:** ✅ specified

## Statement

A document check (a contract, a document template, terms and conditions) lists each mandatory clause or mention found or
missing, and each clause that may break a rule, with its article; it never rewrites the document by itself: suggested
wording goes through the drafting and confirmation of F3 (BR-F3-12).

## Why

The document stays the company's; the AI assistant points out, the person decides.

Legal values from the France country pack:
[CR-FR-015 Mandatory invoice mentions](../../../10-country-packs/france/invoicing/cr-fr-015-invoice-mandatory-mentions.md),
[CR-FR-019 Late-payment penalties](../../../10-country-packs/france/invoicing/cr-fr-019-late-payment-penalties.md),
[CR-FR-041 Fixed-term contracts](../../../10-country-packs/france/labour/cr-fr-041-fixed-term-contracts.md).

## Examples

| Case | Result |
|---|---|
| A fixed-term contract template without its reason for recourse | "Missing: the reason for recourse (L1242-12)" |
| An invoice template without late-payment penalties | "Missing: late-payment penalty rate and the 40 EUR recovery fee (Code de commerce, L441-10)" |
| "Suggest the clause" | A draft in the template editor, not saved until the user saves |

## Applies to

- [UC-F15-01](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-03](../use-cases/03-check-a-document-against-the-law/uc-f15-03-check-a-document-against-the-law.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-07 Warnings inform, never block](br-f15-07-warnings-inform-never-block.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-09 Law packs pull official sources on their own](br-f15-09-law-packs-pull-official-sources-on-their-own.md)
