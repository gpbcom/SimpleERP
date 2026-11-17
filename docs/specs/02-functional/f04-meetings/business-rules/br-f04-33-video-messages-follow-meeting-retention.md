🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-33 Video messages follow meeting retention

# 📏 BR-F4-33 Video messages follow meeting retention

**Status:** ✅ specified

## Statement

A video message is kept for the same period as the company's meeting recordings
([E-F4-25 Meeting recording setting](../data/e-f04-25-meeting-recording-setting.md)) and deleted at its end, with its
transcript, unless the user deletes it sooner or the message is attached to a record the law requires to keep; a shared
link never outlives the message.

## Why

A video message is a recording of people: it must follow the retention the company already set for recordings, not a
second, forgotten one. The owner's answer: "Video messages"
([D523](../../../06-decisions/f04-meetings/d523-benchmark-gaps-f04-meetings.md)); recording rules are
[BR-F4-01](br-f04-01-every-recording-is-announced.md) and [BR-F4-03](br-f04-03-recordings-are-deleted-once-checked.md).

## Examples

| Case | Result |
|---|---|
| Company retention 90 days, message recorded today | deleted on day 91 with its transcript |
| The user deletes the message on day 10 | deleted at once, the link stops |
| A link ending in 30 days, retention ending in 10 | the link ends in 10 days |
| A message attached to a signed quote | kept with the quote for its legal period |

## Applies to

- [UC-F4-28 Record and share a video message](../use-cases/14-video-messages-and-webinars/uc-f04-28-record-and-share-a-video-message.md)
- [E-F4-27 Video message](../data/e-f04-27-video-message.md)
- [E-F4-25 Meeting recording setting](../data/e-f04-25-meeting-recording-setting.md)

## Exceptions

A message attached to a record the law requires to keep follows that record's period.

## Configurable

Yes, through the meeting recording setting
([E-F4-25 Meeting recording setting](../data/e-f04-25-meeting-recording-setting.md)).

## Open questions

None.

---

⬅️ [BR-F4-32 Who sees a colleague's calendar](br-f04-32-who-sees-a-colleagues-calendar.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-34](br-f04-34-webinar-attendees-become-leads-only-with-consent.md)
