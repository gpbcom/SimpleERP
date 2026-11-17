🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-09 Live answers need 70 % confidence

# 📏 BR-F4-09 Live answers need 70 % confidence

**Status:** ✅ specified

## Statement

During a meeting, participants see the live transcript by default. The AI assistant answers only when a participant
calls it ("Ask about this meeting"), and only if its confidence is 70 % or more; otherwise it says it is not sure enough
and shows the passages that may help. It never speaks in the call.

## Why

A wrong answer in a live meeting misleads everyone at once. See
[D219](../../../06-decisions/f04-meetings/d219-live-transcript-and-assistant.md).

## Examples

| Case | Result |
|---|---|
| "What did we decide on the price?", confidence 88 % | "1,240 EUR, agreed at 14:12", linked |
| Confidence 55 % | "I'm not sure enough to answer. These passages may help:" |

## Applies to

- [UC-F4-01](../use-cases/01-record-an-online-meeting/uc-f04-01-record-an-online-meeting-with-the-bot.md)
- [UC-F4-02](../use-cases/01-record-an-online-meeting/uc-f04-02-import-a-platform-s-own-transcript.md)

## Exceptions

None.

## Configurable

No: the threshold is 70 %.

## Open questions

None.

---

⬅️ [BR-F4-08 Any internal participant can start](br-f04-08-any-internal-participant-can-start.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-10 Offline recordings upload later](br-f04-10-offline-recordings-upload-later.md)
