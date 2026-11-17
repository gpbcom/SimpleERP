🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D152 Ask back, or say not found

# 📜 D152 Ask back, or say not found

**Status:** ✅ decided

## Context

What the AI assistant does when a question is ambiguous or nothing matches.

## Options

- Ask, then say not found.
- Best guess, stated.
- Say not found only.

## Choice

An ambiguous question gets one clarifying question with clickable choices (which customer, which period); when nothing
matches, it says so and shows what it searched; it never invents an answer.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No made-up answers (BR-F3-04).

## Related

- [UC-F3-01](../../02-functional/f03-assistant/use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md)

---

⬅️ [D151 Figures come from queries](d151-figures-from-queries.md) · ⬆️ [Up](README.md) ·
➡️ [D153 What the AI assistant knows of the screen](d153-screen-context.md)
