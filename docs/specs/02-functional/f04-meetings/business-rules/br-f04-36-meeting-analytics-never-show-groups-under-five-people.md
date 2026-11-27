🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-36 Meeting analytics never show groups under five people

# 📏 BR-F4-36 Meeting analytics never show groups under five people

**Status:** ✅ specified

## Statement

Meeting time analytics show a group (a team, a site, a kind of meeting with its attendees) only when it has at least
five people; smaller groups are added to Other groups or left out, no filter selects one person, and nothing ranks
people.

## Why

Time spent in meetings of a group of two or three reveals what one person does. The owner's answer: "Meeting-time
analytics" ([D523](../../../06-decisions/f04-meetings/d523-benchmark-gaps-f04-meetings.md)); the same minimum applies to
trends across calls in [BR-F4-24](br-f04-24-trends-count-only-what-the-reader-may-see-quoted.md).

## Examples

| Case | Result |
|---|---|
| Sales, 11 people | shown |
| Finance, 3 people | added to Other groups |
| A filter on Claire P. | not offered |
| Every group under five | only the company total is shown, with the reason |
| A person reading their own hours | shown only in their own calendar, not here |

## Applies to

- [UC-F4-31 Analyse time spent in meetings](../use-cases/14-video-messages-and-webinars/uc-f04-31-analyse-time-spent-in-meetings.md)
- [S-F4-28 Meeting time analytics](../screens/14-video-messages-and-webinars/s-f04-28-meeting-time-analytics.md)
- [UC-F4-20 Analyse topics and trends across calls](../use-cases/11-insights-and-accessibility/uc-f04-20-analyse-topics-and-trends-across-calls.md)

## Exceptions

None.

## Configurable

No: five is the minimum; a company may raise it to 10 but not lower it.

## Open questions

None.

---

⬅️ [BR-F4-35](br-f04-35-ai-filled-template-fields-stay-drafts-until-reviewed.md) · ⬆️ [Up](README.md)
