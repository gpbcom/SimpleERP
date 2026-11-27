🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D179 Conversation retention

# 📜 D179 Conversation retention

**Status:** ✅ decided

## Context

How long conversations are kept.

## Options

- Set by the administrator, 12 months by default.
- Until the user deletes.
- A fixed 90 days.

## Choice

The administrator sets how long unused conversations are kept, 12 months after the last message by default; pinned
conversations are kept; the owner is warned a week before deletion.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Conversations do not pile up personal data forever (BR-F3-27).

## Related

- [UC-F3-08](../../02-functional/f03-assistant/use-cases/08-manage-and-share-conversations/uc-f03-08-manage-and-share-conversations.md)
- [D141](d141-shareable-conversations.md)
- [D144](d144-shared-conversations-show-everything.md)

---

⬅️ [D178 Share with chosen colleagues](d178-share-with-chosen-colleagues.md) · ⬆️ [Up](README.md) ·
➡️ [D180 Organising conversations](d180-organise-conversations.md)
