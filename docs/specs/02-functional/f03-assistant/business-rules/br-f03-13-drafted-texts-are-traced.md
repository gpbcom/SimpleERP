🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-13 Drafted texts are traced

# 📏 BR-F3-13 Drafted texts are traced

**Status:** ✅ specified

## Statement

A text drafted with the AI assistant and then saved or sent is noted "drafted with the assistant" in the record history.
A visible "written with AI help" mention for recipients is a company setting, off by default; for content published to
social media (F5) it is on.

## Why

Transparency, without burdening every email. See
[D164](../../../06-decisions/f03-assistant/d164-drafted-with-ai-label.md).

Legal values from the France country pack:
[CR-FR-056 People know they deal with an AI](../../../10-country-packs/france/ai-and-recording/cr-fr-056-people-know-they-deal-with-an-ai.md).

## Examples

| Case | Result |
|---|---|
| An email drafted, then sent | History: "Email sent by Marie Dupont, drafted with the assistant" |
| Setting on | The email ends with "Written with AI help" |
| A social media post (F5) | The mention is on |

## Applies to

- [UC-F3-04](../use-cases/04-summarise-or-draft/uc-f03-04-summarise-and-draft.md)

## Exceptions

None.

## Configurable

Yes: the visible mention, by an administrator, except for F5 where it is on.

## Open questions

None.

---

⬅️ [BR-F3-12 Drafts go to their editor, never out](br-f03-12-drafts-go-to-their-editor.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-14 One match opens, several are listed](br-f03-14-one-match-opens-several-are-listed.md)
