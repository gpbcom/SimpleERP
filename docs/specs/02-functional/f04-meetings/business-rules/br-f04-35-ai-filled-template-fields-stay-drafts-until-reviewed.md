🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-35 AI-filled template fields stay drafts until reviewed

# 📏 BR-F4-35 AI-filled template fields stay drafts until reviewed

**Status:** ✅ specified

## Statement

A note template field filled by the AI assistant is marked Draft with its source in the transcript and is not copied to
any record until a person confirms or edits it; a meeting published without review shows its fields as Not checked, and
an empty value is shown as Not said in the meeting, never guessed.

## Why

A wrong amount in an opportunity or a wrong name in a file does harm that a wrong sentence in a summary does not. The
owner's answer: "Note templates" ([D523](../../../06-decisions/f04-meetings/d523-benchmark-gaps-f04-meetings.md)); it
extends [BR-F4-15](br-f04-15-unreviewed-meetings-publish-as-not-checked.md) and
[BR-F4-20](br-f04-20-scores-come-with-their-evidence.md) to structured fields.

## Examples

| Case | Result |
|---|---|
| Budget filled as 40,000 EUR | Draft, source shown, copied only after the reviewer confirms |
| The meeting is published without review | the fields show Not checked |
| The customer never spoke of a budget | the field says Not said in the meeting |
| The reviewer edits the budget to 45,000 | the edited value is confirmed and may be copied |

## Applies to

- [UC-F4-30 Choose a note template per meeting type](../use-cases/14-video-messages-and-webinars/uc-f04-30-choose-a-note-template-per-meeting-type.md)
- [E-F4-29 Note template](../data/e-f04-29-note-template.md)
- [UC-F4-05 Review a meeting](../use-cases/03-review-a-meeting/uc-f04-05-review-a-meeting.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-34](br-f04-34-webinar-attendees-become-leads-only-with-consent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-36](br-f04-36-meeting-analytics-never-show-groups-under-five-people.md)
