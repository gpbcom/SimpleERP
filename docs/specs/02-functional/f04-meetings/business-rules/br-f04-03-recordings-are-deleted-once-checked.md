🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-03 Recordings are deleted once checked

# 📏 BR-F4-03 Recordings are deleted once checked

**Status:** ✅ specified

## Statement

Audio and video are deleted when the organiser marks the transcript checked, and at the latest after the retention
period: 7 days by default, longer if an administrator chooses. Transcript and summary stay with the meeting.

## Why

Keep the least personal data needed. See [D210](../../../06-decisions/f04-meetings/d210-recordings-deleted.md).

Legal values from the France country pack:
[CR-FR-052 Personal data kept no longer than needed](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Examples

| Case | Result |
|---|---|
| Checked on day 2 | Audio deleted on day 2 |
| Never checked | Audio deleted on day 7 |
| The administrator sets 30 days | Day 30 |

## Applies to

Every F4 use case.

- [UC-F4-23 Handle an outside speaker's objection or erasure](../use-cases/13-outside-people-and-follow-up/uc-f04-23-handle-an-outside-speakers-objection-or-erasure.md)

## Exceptions

None.

## Configurable

Yes: the retention period, by an administrator.

## Open questions

None.

---

⬅️ [BR-F4-02 No voice prints](br-f04-02-no-voice-prints.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-04 Transcripts stay with participants](br-f04-04-transcripts-stay-with-participants.md)
