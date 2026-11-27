🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D172 Outside call caps

# 📜 D172 Outside call caps

**Status:** ✅ decided

## Context

Whether paid outside tools have usage limits.

## Options

- A cap per connection and per user.
- No limits.
- A cap per user only.

## Choice

The administrator sets an optional monthly call cap per connection, and per user; administrators are warned at 80 %; at
100 % calls stop until next month or a raise.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Costs of outside tools stay under control (BR-F3-20).

## Related

- [UC-F3-06](../../02-functional/f03-assistant/use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md)
- [D80](../f01-administration/d80-external-tools-per-role.md)
- [D81](../f01-administration/d81-confirmation-per-connection.md)

---

⬅️ [D171 Personal connections](d171-personal-connections.md) · ⬆️ [Up](README.md) ·
➡️ [D173 Knowledge base content](d173-knowledge-content.md)
