🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D157 What the AI assistant may do

# 📜 D157 What the AI assistant may do

**Status:** ✅ decided

## Context

Which kinds of actions the AI assistant carries out once the user confirms.

## Options

- All but irreversible acts.
- Everything the user may do.
- Create and change only.

## Choice

It creates, changes and moves statuses within the user's rights; it never deletes, and never does irreversible or
outward acts itself (validate an invoice, send to a customer, pay): it prepares them and opens the screen where the user
finishes.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Irreversible and legal acts stay a person's own click (BR-F3-07).

Revised by D439 on 2026-11-12: this is the AI assistant tier: it always asks before writing; agents and automations act
alone only within a procedure switched to automatic, never for payments, legal sendings, deletions or decisions about a
person.

## Related

- [UC-F3-03](../../02-functional/f03-assistant/use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)
- [D140](d140-assistant-confirms-changes.md)

---

⬅️ [D156 The AI assistant explains the screen](d156-explain-the-screen.md) · ⬆️ [Up](README.md) ·
➡️ [D158 Undo an AI assistant batch](d158-assistant-undo.md)
