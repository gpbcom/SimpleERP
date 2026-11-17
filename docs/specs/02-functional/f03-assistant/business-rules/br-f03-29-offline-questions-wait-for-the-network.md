🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-29 Offline questions wait for the network

# 📏 BR-F3-29 Offline questions wait for the network

**Status:** ✅ specified

## Statement

Without a network, the AI assistant shows "Offline: your question will be answered when you are back online"; questions
are queued on the phone, sent when the network is back, and the answer comes with a notification; a change from a queued
question still waits for the user's confirmation.

## Why

Field workers lose the network; nothing must happen without them. See
[D182](../../../06-decisions/f03-assistant/d182-offline-assistant.md).

## Examples

| Case | Result |
|---|---|
| A question in a basement | Queued, answered at 16:05 with a notification |
| "Create a follow-up visit" offline | Queued; at 16:05 the card asks for confirmation |
| A queued question older than 24 hours | Asked again before sending |

## Applies to

- [UC-F3-09](../use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-28 Hands-free confirmations are spoken](br-f03-28-hands-free-confirmations-are-spoken.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F3-30 Photos fill records through confirmation](br-f03-30-photos-fill-records-through-confirmation.md)
