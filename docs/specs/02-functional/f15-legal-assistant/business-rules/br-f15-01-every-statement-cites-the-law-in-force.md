🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-01 Every statement cites the law in force

# 📏 BR-F15-01 Every statement cites the law in force

**Status:** ✅ specified

## Statement

Each statement of a legal answer cites its source: the article (or agreement clause, guidance page, decision), the
version in force and the date it took effect, linked to the official text. By default the answer uses the law in force
today; the user can ask "as of" a past date and the answer uses the versions then in force, saying so at the top. Case
law is labelled as case law.

## Why

A legal answer is only as good as its source and date. See
[D194](../../../06-decisions/f15-legal-assistant/d194-legal-citations.md).

## Examples

| Case | Result |
|---|---|
| "How many days of paid leave?" | "2.5 working days per month worked (Code du travail, L3141-3, version in force since 22 April 2024)", linked |
| "What was the notice for my dismissal in March 2025?" | "As of 15 March 2025:" then the versions in force that day |
| A Cour de cassation decision used | "Case law: Cass. soc., <date>, n° <number>" |

## Applies to

Every answer of the legal assistant.

- [UC-F15-07 Keep the compliance calendar](../use-cases/05-duties-and-records/uc-f15-07-keep-the-compliance-calendar.md)
- [UC-F15-13 Answer a client's tax question with their data](../use-cases/01-ask-a-legal-question/uc-f15-13-answer-a-clients-tax-question-with-their-data.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F15-02 Information, not advice](br-f15-02-information-not-advice.md)
