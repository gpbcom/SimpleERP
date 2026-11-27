🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-10 Offline recordings upload later

# 📏 BR-F4-10 Offline recordings upload later

**Status:** ✅ specified

## Statement

Without a network, the phone app records, stores the audio encrypted on the phone, and uploads it as soon as the network
is back; the audio is then removed from the phone and transcribed on the server. A recording not uploaded
after 7 days is flagged to the user.

## Why

Sites and basements have no network. See [D220](../../../06-decisions/f04-meetings/d220-offline-recording.md).

## Examples

| Case | Result |
|---|---|
| A site meeting in a basement | Recorded, uploaded at 16:05 |
| The phone is lost before upload | The audio is encrypted; nothing readable |

## Applies to

- [UC-F4-03](../use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-09 Live answers need 70 % confidence](br-f04-09-live-answers-need-70-confidence.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-11 Business calls recorded only when switched on](br-f04-11-business-calls-are-recorded.md)
