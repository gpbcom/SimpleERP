🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D158 Undo an AI assistant batch

# 📜 D158 Undo an AI assistant batch

**Status:** ✅ decided

## Context

Whether the user can undo what the AI assistant did.

## Options

- Undo the whole batch.
- History only.
- Undo for 10 minutes.

## Choice

An "Undo" on the confirmation message reverts the whole batch, as long as no one has changed those records since;
otherwise each record's history shows what to restore.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Undo never overwrites someone else's change (BR-F3-08).

## Related

- [UC-F3-03](../../02-functional/f03-assistant/use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)
- [D140](d140-assistant-confirms-changes.md)

---

⬅️ [D157 What the AI assistant may do](d157-assistant-actions.md) · ⬆️ [Up](README.md) ·
➡️ [D159 Assistant batch size](d159-assistant-batch-size.md)
