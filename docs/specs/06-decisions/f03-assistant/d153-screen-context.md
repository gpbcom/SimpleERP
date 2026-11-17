🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D153 What the AI assistant knows of the screen

# 📜 D153 What the AI assistant knows of the screen

**Status:** ✅ decided

## Context

What the AI assistant knows about the screen the user is on.

## Options

- The record, its linked records, or the list with its filters.
- Only what is displayed.
- The record only.

## Choice

On a record: that record and its linked records (a customer's quotes, invoices and history). On a list: the list with
its current filters and sort. Always within the user's rights.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

"This customer" or "these invoices" need no more words (BR-F3-05).

## Related

- [UC-F3-02](../../02-functional/f03-assistant/use-cases/02-ask-about-the-screen/uc-f03-02-ask-about-what-is-on-screen.md)

---

⬅️ [D152 Ask back, or say not found](d152-ask-or-not-found.md) · ⬆️ [Up](README.md) ·
➡️ [D154 Suggested questions per record type](d154-suggested-questions.md)
