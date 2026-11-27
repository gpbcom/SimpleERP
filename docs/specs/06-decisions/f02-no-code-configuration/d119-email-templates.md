🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D119 Email templates

# 📜 D119 Email templates

**Status:** ✅ decided

## Context

What can be customised in emails.

## Options

- Every outgoing email.
- Company branding.
- Sender address.

## Choice

All three: the subject and body of every outgoing email per language, the company's logo, colours and signature on every
email, and the company's own sender address (such as invoices@acme.fr) with its email server settings.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Email sending settings live in F1's connections (D52).

## Related

- [UC-F2-06](../../02-functional/f02-no-code-configuration/use-cases/02-customise-documents-and-emails/uc-f02-06-edit-an-email-template.md)

---

⬅️ [D118 What a document template handles](d118-document-template-features.md) · ⬆️ [Up](README.md) ·
➡️ [D120 PNG mockups of every flow step](../ux/d120-png-mockups.md)
