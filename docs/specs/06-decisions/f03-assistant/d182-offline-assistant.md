🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D182 The AI assistant offline

# 📜 D182 The AI assistant offline

**Status:** ✅ decided

## Context

What happens without a network.

## Options

- Queue, with a clear notice.
- Unavailable offline.
- A small on-device model.

## Choice

The AI assistant says it is offline; questions are queued and answered when the network is back, with a notification;
changes still need confirmation then. Offline task screens work as usual (D38).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No model on the phone (BR-F3-29).

## Related

- [UC-F3-09](../../02-functional/f03-assistant/use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)
- [D34](../ux/d34-phone-experience.md)
- [D38](../ux/d38-offline-field-tasks.md)

---

⬅️ [D181 Voice first on the phone](d181-phone-voice-first.md) · ⬆️ [Up](README.md) ·
➡️ [D183 Ask about a photo](d183-photo-questions.md)
