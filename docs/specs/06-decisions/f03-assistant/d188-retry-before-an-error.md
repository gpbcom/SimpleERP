🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D188 Retry before an error

# 📜 D188 Retry before an error

**Status:** ✅ decided

## Context

When a call fails (the model, an outside tool, a sync), when the user sees an error.

## Options

- Retry with exponential backoff, then the error.
- The error at once.

## Choice

Retry: the owner, asked about F3's proposed details: "Add a retry mechanism (3 attempts with exponential backoff) before
sending an error." A failing call is retried up to 3 times, each wait twice the previous one; only then is the error
shown.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The waits are 1, 2 and 4 seconds for the user's own questions; the same mechanism is proposed for T5 and T6
at their interviews (BR-F3-32). The other proposed details of F3 stay waiting.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)

---

⬅️ [D187 Where the AI assistant settings live](d187-assistant-settings-page.md) · ⬆️ [Up](README.md) ·
➡️ [D189 Step 19c becomes Storage](../technical/d189-storage-topic.md)
