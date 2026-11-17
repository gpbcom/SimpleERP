🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-07 The organiser picks the source

# 📏 BR-F4-07 The organiser picks the source

**Status:** ✅ specified

## Statement

For each meeting, the organiser chooses the source: the platform's own transcript, imported after the meeting, or the
bot; the default is the platform's transcript when the connection allows it, otherwise the bot.

## Why

Some platforms transcribe well, others not at all. See
[D217](../../../06-decisions/f04-meetings/d217-organiser-picks-source.md).

## Examples

| Case | Result |
|---|---|
| Teams with transcription on | Imported after the meeting |
| Zoom without transcription | The bot joins |
| The organiser picks the bot | The bot joins |

## Applies to

- [UC-F4-01](../use-cases/01-record-an-online-meeting/uc-f04-01-record-an-online-meeting-with-the-bot.md)
- [UC-F4-02](../use-cases/01-record-an-online-meeting/uc-f04-02-import-a-platform-s-own-transcript.md)

## Exceptions

None.

## Configurable

Yes: per meeting, by its organiser.

## Open questions

None.

---

⬅️ [BR-F4-06 The bot joins calendar meetings by default](br-f04-06-the-bot-joins-calendar-meetings-by-default.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F4-08 Any internal participant can start](br-f04-08-any-internal-participant-can-start.md)
