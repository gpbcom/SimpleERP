🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-05 The law of the contract or the site

# 📏 BR-F15-05 The law of the contract or the site

**Status:** ✅ specified

## Statement

An employee's question is answered under the law of their contract, or else of their place of work; a company question
under the law of the site concerned, or else of the head office. The answer's first line names the country ("Under
French law"), with a switch to another enabled country.

## Why

The right law depends on the person and the site. See
[D201](../../../06-decisions/f15-legal-assistant/d201-legal-country-of-an-answer.md).

## Examples

| Case | Result |
|---|---|
| An employee of the Barcelona site, Spanish contract | Spanish law, if its law pack is installed |
| No law pack for that country | "I don't know: the law of Spain is not in my sources." (BR-F15-02) |
| The owner asks about the Lyon site | French law |

## Applies to

- [UC-F15-01](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-03](../use-cases/03-check-a-document-against-the-law/uc-f15-03-check-a-document-against-the-law.md)
- [UC-F15-04](../use-cases/04-set-up-the-legal-assistant/uc-f15-04-set-up-the-legal-assistant.md)
- [UC-F15-13 Answer a client's tax question with their data](../use-cases/01-ask-a-legal-question/uc-f15-13-answer-a-clients-tax-question-with-their-data.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-04 The user's language, the law's words](br-f15-04-the-user-s-language-the-law-s-words.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F15-06 A quality drop blocks the update](br-f15-06-a-quality-drop-blocks-the-update.md)
