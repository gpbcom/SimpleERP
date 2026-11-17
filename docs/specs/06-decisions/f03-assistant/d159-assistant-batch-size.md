🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D159 Assistant batch size

# 📜 D159 Assistant batch size

**Status:** ✅ decided

## Context

How many records one confirmed batch may change.

## Options

- Up to 100, with the full list.
- No limit.
- Up to 20.

## Choice

100 by default, configurable, with "No limit" as one of the choices (the owner: "Default to 100. But configurable.
That's include a 'No limit' option."). Larger requests are split into batches or sent to the bulk-edit screen.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The administrator sets it in the AI assistant settings of F1 (BR-F3-09).

## Related

- [UC-F3-03](../../02-functional/f03-assistant/use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)
- [D140](d140-assistant-confirms-changes.md)

---

⬅️ [D158 Undo an AI assistant batch](d158-assistant-undo.md) · ⬆️ [Up](README.md) ·
➡️ [D160 Assistant changes are signed](d160-assistant-signature.md)
