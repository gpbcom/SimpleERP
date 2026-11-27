🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-03 Legal questions stay private

# 📏 BR-F15-03 Legal questions stay private

**Status:** ✅ specified

## Statement

A legal conversation is visible only to its asker, unless the asker shares it (BR-F3-26). Managers, HR and
administrators never see it. Reports show counts only; the audit trail records that a legal question was asked, by whom
and when, never its content or topic; questions on sensitive topics (harassment, discrimination, health) are never
counted per team or site.

## Why

An employee must be able to ask about their rights without their employer knowing. See
[D196](../../../06-decisions/f15-legal-assistant/d196-legal-privacy.md).

## Examples

| Case | Result |
|---|---|
| An employee asks about resignation | HR sees nothing |
| The owner opens the usage dashboard | "Legal questions: 46 this month", no topics per team |
| An employee shares a conversation with HR | HR sees that conversation only |

## Applies to

Every answer of the legal assistant.

- [UC-F15-12 Hand a question over to a lawyer](../use-cases/01-ask-a-legal-question/uc-f15-12-hand-a-question-over-to-a-lawyer.md)

## Exceptions

None, administrators included.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F15-02 Information, not advice](br-f15-02-information-not-advice.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F15-04 The user's language, the law's words](br-f15-04-the-user-s-language-the-law-s-words.md)
