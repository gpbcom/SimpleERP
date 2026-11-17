🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D150 Answers never hint at hidden records

# 📜 D150 Answers never hint at hidden records

**Status:** ✅ decided

## Context

What the AI assistant says when the answer depends on records the user may not see.

## Options

- Silent, with a generic notice.
- Say that data was left out.
- Refuse the question.

## Choice

It answers only from what the user may see and never hints that anything else exists; a fixed sentence under every
figure says it covers "the records you can see".

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The AI assistant cannot be used to probe for hidden records (BR-F3-02, D12).

## Related

- [UC-F3-01](../../02-functional/f03-assistant/use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md)
- [D12](../foundations/d12-permissions-model.md)

---

⬅️ [D149 How answers show their sources](d149-answer-sources.md) · ⬆️ [Up](README.md) ·
➡️ [D151 Figures come from queries](d151-figures-from-queries.md)
