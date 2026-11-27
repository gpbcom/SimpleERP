🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D169 Data sent to outside tools

# 📜 D169 Data sent to outside tools

**Status:** ✅ decided

## Context

Which ERP data the AI assistant may send to an outside tool.

## Options

- Only what is needed, within allowed categories.
- Only what is needed.
- Nothing personal.

## Choice

Only what the request needs; per connection, the administrator allows data categories: none, business data, personal
data; every call shows "Sent to <tool>" in the conversation, expandable.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The connection gains a data categories field (BR-F3-17, D83).

## Related

- [UC-F3-06](../../02-functional/f03-assistant/use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md)
- [D80](../f01-administration/d80-external-tools-per-role.md)
- [D81](../f01-administration/d81-confirmation-per-connection.md)

---

⬅️ [D168 Missing features become requests](d168-configuration-requests.md) · ⬆️ [Up](README.md) ·
➡️ [D170 Outside results are marked](d170-outside-results-marked.md)
