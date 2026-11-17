🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D144 Shared conversations show everything

# 📜 D144 Shared conversations show everything

**Status:** ✅ decided

## Context

What a colleague with fewer rights sees in a shared conversation.

## Options

- Only what they may see.
- Everything, as the author saw it.

## Choice

Everything, as the author saw it: sharing is the author's responsibility.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

- **An exception to D12:** through a shared conversation, a colleague can read data their own role would not show (for
  example salaries quoted in an answer).
- Before sharing, the author is warned when the conversation quotes data the colleagues may not see, naming
  that data; the share is recorded in the audit trail.
- Follow-up questions by the colleague are answered under the colleague's own rights.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [D12](../foundations/d12-permissions-model.md)

---

⬅️ [D143 Outside APIs from their OpenAPI description](d143-outside-api-from-openapi.md) · ⬆️ [Up](README.md) ·
➡️ [D145 Voice in and out](d145-assistant-voice.md)
