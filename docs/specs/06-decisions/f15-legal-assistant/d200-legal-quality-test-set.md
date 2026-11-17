🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D200 Legal answer quality

# 📜 D200 Legal answer quality

**Status:** 🚫 withdrawn

## Context

How the quality of legal answers is measured.

## Options

- A test set and feedback.
- Feedback only.
- Manual review.

## Choice

Each law pack has a test set of questions with the articles expected; it runs after every corpus refresh and every model
change; a drop blocks the update; users' thumbs (D186) feed new test questions.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

🚫 Withdrawn on 2026-11-10 by [D206](d206-unattended-pulls-without-test-gate.md): the owner chose unattended pulls (D205)
over this gate.

## Related

- [UC-F15-01](../../02-functional/f15-legal-assistant/use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)

---

⬅️ [D199 Law packs](d199-law-packs.md) · ⬆️ [Up](README.md) ·
➡️ [D201 Whose law applies](d201-legal-country-of-an-answer.md)
