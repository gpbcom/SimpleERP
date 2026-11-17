🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-27 Conversation retention

# 📏 BR-F3-27 Conversation retention

**Status:** ✅ specified

## Statement

A conversation unused for the retention period (set by the administrator, 12 months after its last message by default)
is deleted, unless pinned; its owner is warned a week before. A conversation is deleted with its owner's account.

## Why

Conversations hold personal data and must not pile up. See
[D179](../../../06-decisions/f03-assistant/d179-conversation-retention.md).

Legal values from the France country pack:
[CR-FR-052 Personal data kept no longer than needed](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Examples

| Case | Result |
|---|---|
| Last message 12 months ago, not pinned | Warned, then deleted a week later |
| Pinned | Kept |
| The administrator sets 6 months | Applies to all conversations from then on |

## Applies to

- [UC-F3-08](../use-cases/08-manage-and-share-conversations/uc-f03-08-manage-and-share-conversations.md)

## Exceptions

None.

## Configurable

Yes: the period, by the administrator (3, 6, 12, 24 months, never); default 12 months.

## Open questions

None.

---

⬅️ [BR-F3-26 Share only with chosen colleagues](br-f03-26-share-only-with-chosen-colleagues.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-28 Hands-free confirmations are spoken](br-f03-28-hands-free-confirmations-are-spoken.md)
