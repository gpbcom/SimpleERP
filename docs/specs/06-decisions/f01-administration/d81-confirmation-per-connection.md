🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D81 Confirmation per connection

# 📜 D81 Confirmation per connection

**Status:** ✅ decided

## Context

What happens before the AI assistant calls an external tool that changes something outside.

## Options

- The user confirms each call.
- Configurable per connection.
- Never ask.

## Choice

Configurable per connection: the administrator chooses "always ask" or "trusted". Read-only calls never ask.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Each connection carries its own setting.

## Related

- [UC-F1-07](../../02-functional/f01-administration/use-cases/05-connect-an-external-tool/uc-f01-07-connect-an-external-mcp-server-or-a2a-agent.md)
- [BR-F1-14](../../02-functional/f01-administration/business-rules/br-f01-14-confirming-outside-changes.md)

---

⬅️ [D80 External tools per role](d80-external-tools-per-role.md) · ⬆️ [Up](README.md) ·
➡️ [D82 AI provider per feature](d82-ai-provider-per-feature.md)
