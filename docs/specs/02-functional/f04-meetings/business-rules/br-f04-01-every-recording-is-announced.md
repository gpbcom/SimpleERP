🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-01 Every recording is announced

# 📏 BR-F4-01 Every recording is announced

**Status:** ✅ specified

## Statement

Every recording is announced to everyone in it, and anyone can stop it: online, the bot joins as "simple-ERP recorder"
and posts a notice (D23); in person, the app shows "Recording" and the organiser confirms everyone was told before it
starts; on the phone, a spoken message opens the call. A platform's own transcript is imported only if that platform
announced its recording.

## Why

People must know they are recorded. See [D213](../../../06-decisions/f04-meetings/d213-recording-notice-without-bot.md).

Legal values from the France country pack:
[CR-FR-059 Recordings are announced](../../../10-country-packs/france/ai-and-recording/cr-fr-059-recordings-are-announced.md).

## Examples

| Case | Result |
|---|---|
| A site meeting on the phone app | "Did you tell everyone present they are recorded?" Yes, then recording |
| A customer call | "This call is recorded and transcribed" plays first |
| A participant says "stop recording" | It stops; the transcript ends there |

## Applies to

Every F4 use case.

- [UC-F4-25 Hold a client video meeting](../use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md)

## Exceptions

None.

## Configurable

The spoken message's words, per language.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F4-02 No voice prints](br-f04-02-no-voice-prints.md)
