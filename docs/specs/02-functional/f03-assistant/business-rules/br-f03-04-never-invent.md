🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-04 Ask or say not found, never invent

# 📏 BR-F3-04 Ask or say not found, never invent

**Status:** ✅ specified

## Statement

When a question is ambiguous, the AI assistant asks one clarifying question with clickable choices; when nothing
matches, it says so and shows what it searched; it never makes up a record, a figure or a fact.

## Why

A wrong answer said with confidence is worse than none. See
[D152](../../../06-decisions/f03-assistant/d152-ask-or-not-found.md).

## Examples

| Case | Result |
|---|---|
| "How much does Martin owe?" with 2 customers named Martin | "Which Martin?" [Martin SARL, Lyon] [Martin Plomberie, Nantes] |
| "Orders from Zeta?" with no such customer | "I found no customer named Zeta among the records you can see. I searched: customers, contacts." |

## Applies to

- [UC-F3-01](../use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md); every
  assistant answer of F3.
- [UC-F3-14 Run the quality evaluation set](../use-cases/11-trust-the-answers/uc-f03-14-run-the-quality-evaluation-set.md)
- [UC-F3-19 Turn unanswered topics into knowledge proposals](../use-cases/12-personal-cost-aware-and-learning/uc-f03-19-turn-unanswered-topics-into-knowledge-proposals.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-03 Figures come from queries, never the model](br-f03-03-figures-come-from-queries.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-05 Screen context is the user's view](br-f03-05-screen-context-is-the-user-s-view.md)
