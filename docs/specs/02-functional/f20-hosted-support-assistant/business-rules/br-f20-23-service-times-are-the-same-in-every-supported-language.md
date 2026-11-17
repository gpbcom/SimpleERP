🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-23 Service times are the same in every supported language

# 📏 BR-F20-23 Service times are the same in every supported language

**Status:** 🔄 waiting for the owner

## Statement

The response and resolution times of the support plan are the same in every supported language: a language is listed as
supported only when the engineers' rota covers it during the plan's hours, and a language that is not covered is never
listed with longer times, only answered in English with a note.

## Why

Promising a language with slower answers would make a second-class support; a language that cannot be covered must say
so. The owner asked for more support languages
([D539](../../../06-decisions/f20-hosted-support-assistant/d539-benchmark-gaps-f20-hosted-support-assistant.md)).

## Examples

| Case | Result |
|---|---|
| German listed, urgent request in German | first answer within the plan's 1 hour |
| Spanish not covered | not listed, answered in English with a note |
| A language covered only 9:00 to 17:00 | the screen shows those hours, and the same times inside them |
| An engineer who speaks the language is absent | the nearest engineer within the same time, translation marked |
| A language dropped from the list | the companies are told in advance |

## Applies to

- [UC-F20-32](../use-cases/08-engineers-sharing-and-reports/uc-f20-32-get-support-in-more-languages.md)
- [E-F20-12 Support plan](../data/e-f20-12-support-plan.md)

## Exceptions

None.

## Configurable

The supported list and its hours, by the simple-ERP team in the language catalogue.

## Open questions

None.

---

⬅️ [BR-F20-22 Reports contain no personal data](br-f20-22-reports-contain-no-personal-data.md) · ⬆️ [Up](README.md)
