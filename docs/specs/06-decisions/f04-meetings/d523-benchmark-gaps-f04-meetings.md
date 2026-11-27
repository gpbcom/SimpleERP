🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎙️ [Decisions: F4 Meetings](README.md) ›
📜 D523 Benchmark gaps of F4 Meetings

# 📜 D523 Benchmark gaps of F4 Meetings

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the recorder, event and analytics features of
the benchmarked suites and offered each gap as an option
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F4 Meetings").

## Options

- Take each gap as a use case of F4 in a new flow, or leave it out.
- Meeting analytics is a use case with a business rule and no entity, since it computes from meetings and calendars that
  already exist.

## Choice

The owner selected all four gaps; each becomes a use case of F4, drawn in
[FL-F4-14 Video messages, webinars and templates](../../02-functional/f04-meetings/flows/fl-f04-14-video-messages-and-webinars.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G39 | [UC-F4-28 Record and share a video message](../../02-functional/f04-meetings/use-cases/14-video-messages-and-webinars/uc-f04-28-record-and-share-a-video-message.md) | "Video messages" |
| G40 | [UC-F4-29 Host a webinar](../../02-functional/f04-meetings/use-cases/14-video-messages-and-webinars/uc-f04-29-host-a-webinar.md) | "Webinars" |
| G41 | [UC-F4-30 Choose a note template per meeting type](../../02-functional/f04-meetings/use-cases/14-video-messages-and-webinars/uc-f04-30-choose-a-note-template-per-meeting-type.md) | "Note templates" |
| G42 | [UC-F4-31 Analyse time spent in meetings](../../02-functional/f04-meetings/use-cases/14-video-messages-and-webinars/uc-f04-31-analyse-time-spent-in-meetings.md) | "Meeting-time analytics" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "Block by block").

## Consequences

- Use cases
  [UC-F4-28 Record and share a video message](../../02-functional/f04-meetings/use-cases/14-video-messages-and-webinars/uc-f04-28-record-and-share-a-video-message.md)
  to
  [UC-F4-31 Analyse time spent in meetings](../../02-functional/f04-meetings/use-cases/14-video-messages-and-webinars/uc-f04-31-analyse-time-spent-in-meetings.md),
  screens
  [S-F4-25 Video message](../../02-functional/f04-meetings/screens/14-video-messages-and-webinars/s-f04-25-video-message.md)
  to
  [S-F4-28 Meeting time analytics](../../02-functional/f04-meetings/screens/14-video-messages-and-webinars/s-f04-28-meeting-time-analytics.md),
  rules
  [BR-F4-33 Video messages follow meeting retention](../../02-functional/f04-meetings/business-rules/br-f04-33-video-messages-follow-meeting-retention.md)
  to
  [BR-F4-36 Meeting analytics never show groups under five people](../../02-functional/f04-meetings/business-rules/br-f04-36-meeting-analytics-never-show-groups-under-five-people.md),
  entities [E-F4-27 Video message](../../02-functional/f04-meetings/data/e-f04-27-video-message.md) to
  [E-F4-29 Note template](../../02-functional/f04-meetings/data/e-f04-29-note-template.md) and their lists
  [S-F4-L27 Video messages](../../02-functional/f04-meetings/screens/00-lists/s-f04-l27-video-messages.md) to
  [S-F4-L29 Note templates](../../02-functional/f04-meetings/screens/00-lists/s-f04-l29-note-templates.md).
- Recording keeps the announcements of
  [BR-F4-01 Every recording is announced](../../02-functional/f04-meetings/business-rules/br-f04-01-every-recording-is-announced.md)
  and the retention of
  [E-F4-25 Meeting recording setting](../../02-functional/f04-meetings/data/e-f04-25-meeting-recording-setting.md).
- Workplace monitoring needs a France pack rule, written later.

## Related

- [FL-F4-14 Video messages, webinars and templates](../../02-functional/f04-meetings/flows/fl-f04-14-video-messages-and-webinars.md)
- [D461 F4 Meetings: gaps and improvements](d461-f04-gaps-and-improvements.md)
- Interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)

---

⬅️ [D522 Benchmark gaps of F3 Assistant](../f03-assistant/d522-benchmark-gaps-f03-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [D524 Benchmark gaps of F5 Social media and marketing](../f05-social-media/d524-benchmark-gaps-f05-social-media.md)
