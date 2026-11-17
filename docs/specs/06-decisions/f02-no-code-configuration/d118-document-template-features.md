🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D118 What a document template handles

# 📜 D118 What a document template handles

**Status:** ✅ decided

## Context

What a document template must handle.

## Options

- Mandatory legal mentions.
- One template per language.
- Several templates per type.
- Electronic invoice formats.

## Choice

All four: the legal mentions French law requires are added and locked; a template per language; several templates per
document type, chosen per document or per customer; and the structured e-invoicing formats (Factur-X, UBL, CII)
generated with the PDF. The owner also asked for a benchmark of the platforms whose APIs submit invoices automatically.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The benchmark is [Q13](../../07-questions/q13-e-invoicing-platforms.md), research in progress.

## Related

- [UC-F2-05](../../02-functional/f02-no-code-configuration/use-cases/02-customise-documents-and-emails/uc-f02-05-edit-a-document-template.md)
- [BR-F2-10](../../02-functional/f02-no-code-configuration/business-rules/br-f02-10-legal-mentions-are-locked.md)
- [BR-F2-11](../../02-functional/f02-no-code-configuration/business-rules/br-f02-11-electronic-formats-with-the-pdf.md)

---

⬅️ [D117 Document template editors](d117-document-template-editors.md) · ⬆️ [Up](README.md) ·
➡️ [D119 Email templates](d119-email-templates.md)
