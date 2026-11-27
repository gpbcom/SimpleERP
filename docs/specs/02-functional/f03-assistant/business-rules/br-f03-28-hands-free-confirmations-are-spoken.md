🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-28 Hands-free confirmations are spoken

# 📏 BR-F3-28 Hands-free confirmations are spoken

**Status:** ✅ specified

## Statement

In hands-free mode, the AI assistant reads its answers aloud and reads each change aloud before it is made, ending with
"Say yes to confirm"; only a clear "yes" confirms; anything else cancels. A batch over 5 records is not
confirmed by voice: the card is shown on screen.

## Why

Voice must not make confirmation weaker (D140). See
[D181](../../../06-decisions/f03-assistant/d181-phone-voice-first.md).

## Examples

| Case | Result |
|---|---|
| "Mark this visit done" | "I will set visit V-212 to Done. Say yes to confirm." "Yes" | Done |
| "Hmm, wait" | Cancelled |
| "Move my 12 visits" | "Please check the list on screen" |

## Applies to

- [UC-F3-09](../use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)

## Exceptions

None.

## Configurable

Yes: hands-free mode on or off, by each user.

## Open questions

None.

---

⬅️ [BR-F3-27 Conversation retention](br-f03-27-conversation-retention.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-29 Offline questions wait for the network](br-f03-29-offline-questions-wait-for-the-network.md)
