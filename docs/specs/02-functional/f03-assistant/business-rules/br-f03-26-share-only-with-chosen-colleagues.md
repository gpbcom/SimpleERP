🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-26 Share only with chosen colleagues

# 📏 BR-F3-26 Share only with chosen colleagues

**Status:** ✅ specified

## Statement

A conversation is shared with named colleagues of the same company, or a team; its link opens only for them, signed in;
the author sees who it is shared with and can stop sharing at any time, which closes it for them (their copies stay).

## Why

Sharing must stay inside chosen people. See
[D178](../../../06-decisions/f03-assistant/d178-share-with-chosen-colleagues.md).

## Examples

| Case | Result |
|---|---|
| Shared with Paul; Lea opens the link | "This conversation is not shared with you" |
| Shared with team Sales | Every member of Sales can open it |
| Sharing stopped | Paul can no longer open it |

## Applies to

- [UC-F3-08](../use-cases/08-manage-and-share-conversations/uc-f03-08-manage-and-share-conversations.md)

## Exceptions

None.

## Configurable

An administrator can turn sharing off.

## Open questions

None.

---

⬅️ [BR-F3-25 Shared conversations continue as a copy](br-f03-25-shared-conversations-continue-as-a-copy.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-27 Conversation retention](br-f03-27-conversation-retention.md)
