🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎙️ [Decisions: F4 Meetings](README.md) ›
📜 D219 Live transcript and assistant

# 📜 D219 Live transcript and assistant

**Status:** ✅ decided

## Context

What participants see during the meeting.

## Options

- A live transcript.
- Nothing until after.
- Live transcript and assistant.

## Choice

The owner: "Live transcript by default. The assistant can be triggerred explicitely, it answers only if confidence rate
is superior or equal 70%."

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F4-09; the confidence is the model's own estimate, checked against the transcript passages it cites.

## Related

- [UC-F4-01](../../02-functional/f04-meetings/use-cases/01-record-an-online-meeting/uc-f04-01-record-an-online-meeting-with-the-bot.md)
- [UC-F4-02](../../02-functional/f04-meetings/use-cases/01-record-an-online-meeting/uc-f04-02-import-a-platform-s-own-transcript.md)

---

⬅️ [D218 Who starts a recording](d218-any-participant-starts.md) · ⬆️ [Up](README.md) ·
➡️ [D220 Offline recording](d220-offline-recording.md)
