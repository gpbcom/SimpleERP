🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-28 A client video link works for one meeting

# 📏 BR-F4-28 A client video link works for one meeting

**Status:** ✅ specified

## Statement

A client's video link works only for its meeting, from shortly before its start until it ends, and passes through a
waiting room.

## Why

A forwarded link must not open another client's meeting.

## Examples

| Case | Result |
|---|---|
| Link of 12-02 10:00 opened at 09:55 | Waiting room |
| Same link the next day | Refused |

## Applies to

- [UC-F4-25 Hold a client video meeting](../use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-27](br-f04-27-accuracy-is-measured-on-reviewers-corrections.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-29 Customers see only the actions sent to them](br-f04-29-customers-see-only-the-actions-sent-to-them.md)
