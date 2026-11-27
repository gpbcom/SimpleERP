🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-11 Drafts follow the company style

# 📏 BR-F3-11 Drafts follow the company style

**Status:** ✅ specified

## Statement

A draft uses the company's document template when one fits the request (F2), the company writing style, and the user's
signature; it is written in the recipient's language when the record gives it, otherwise in the user's.

## Why

Every text should sound like the company. See [D161](../../../06-decisions/f03-assistant/d161-summaries-and-drafts.md)
and [D162](../../../06-decisions/f03-assistant/d162-company-writing-style.md).

## Examples

| Case | Result |
|---|---|
| A reminder to a German customer, style "formal, Sie" | A formal German email with the user's signature |
| "Write the quote text" with a quote template | The template's sections, filled |
| A word to avoid, "cheap" | Never used; "affordable" instead |

## Applies to

- [UC-F3-04](../use-cases/04-summarise-or-draft/uc-f03-04-summarise-and-draft.md)

## Exceptions

None.

## Configurable

Yes: the company writing style, by an administrator; each user's signature.

## Open questions

None.

---

⬅️ [BR-F3-10 Changes signed through the AI assistant](br-f03-10-changes-signed-through-the-assistant.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-12 Drafts go to their editor, never out](br-f03-12-drafts-go-to-their-editor.md)
