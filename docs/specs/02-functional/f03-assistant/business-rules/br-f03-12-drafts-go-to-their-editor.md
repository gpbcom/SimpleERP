🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-12 Drafts go to their editor, never out

# 📏 BR-F3-12 Drafts go to their editor, never out

**Status:** ✅ specified

## Statement

"Use this draft" puts the draft in the editor it belongs to (email composer, a field, a new document) as a draft; the
user edits and sends or saves it; "Copy" is always offered. The AI assistant never sends a draft itself (BR-F3-07).

## Why

Sending is a person's act. See [D163](../../../06-decisions/f03-assistant/d163-draft-output.md).

## Examples

| Case | Result |
|---|---|
| An email draft | The composer opens with it, To filled, not sent |
| A quote text | Put in the quote's text field, the quote unsaved until the user saves |
| A summary | Copy, or add as a note to the record |

## Applies to

- [UC-F3-04](../use-cases/04-summarise-or-draft/uc-f03-04-summarise-and-draft.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-11 Drafts follow the company style](br-f03-11-drafts-follow-the-company-style.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-13 Drafted texts are traced](br-f03-13-drafted-texts-are-traced.md)
