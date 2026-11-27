🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-36 HR approves the shortlist and the sequence before the first message

# 📏 BR-F9-36 HR approves the shortlist and the sequence before the first message

**Status:** ✅ specified

## Statement

No invitation or message goes to a prospect until HR has approved, once, who is contacted and every template of the
sequence. By default each message is then prepared, waits as a task in HR's task list, and goes only when HR sends it
with one click; when the administrator turned automatic sending on, the messages go out on their own after this
approval, until a reply, a refusal or day 60. The sending mode is fixed when the sequence starts: a later change by the
administrator applies only to sequences started after it, and a sequence returned to draft because a template changed
keeps its mode when HR approves it again.

## Why

The owner's answer LS-2 ([D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)):
"The shortlist and the sequence, once (Recommended)". Ranking candidates is a high-risk AI use (EU AI Act, Annex III,
point 4(a)); this approval is the human oversight
[BR-F4-21](../../f04-meetings/business-rules/br-f04-21-candidate-scoring-is-high-risk-ai.md) asks for. Sending is
prepared by default and automatic only as the administrator's option, because LinkedIn's user agreement restricts
automated activity ([D570](../../../06-decisions/f09-hr-and-projects/d570-linkedin-sending-prepared-by-default.md)).

## Examples

| Case | Result |
|---|---|
| 12 shortlisted prospects, every template approved | passes: the day 0 invitations are prepared, each goes on HR's click |
| The same, automatic sending turned on | passes: the day 0 invitations go on their own |
| The shortlist approved, follow-up 2 without a template | fails: nothing goes |
| A prospect added after the approval | waits until HR approves that prospect |
| A template changed after the approval | the next message using it waits for approval |
| Follow-up 1 on day 7 | prepared without a new approval, goes on HR's click; on its own with automatic sending on |
| The administrator turns automatic sending on while a sequence runs in prepared mode | that sequence stays prepared until it ends; a sequence approved after the change sends on its own |
| The administrator turns automatic sending off while a sequence runs automatically | that sequence goes on sending on its own; a sequence approved after the change is prepared |
| A prepared mode sequence returned to draft after the administrator turned automatic sending on, then approved again | it stays prepared: the return to draft keeps its mode |

## Applies to

- [UC-F9-40 Search and rank LinkedIn profiles](../use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md)
- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [UC-F9-42 Turn a positive reply into an applicant](../use-cases/02-recruit/uc-f09-42-turn-a-positive-reply-into-an-applicant.md)
- [E-F9-46 Outreach sequence](../data/e-f09-46-outreach-sequence.md)

## Exceptions

None.

## Configurable

The sending mode, by the administrator, per company, when connecting Unipile: prepared (the default) or automatic; a
change applies to the sequences started after it, never to a running one
([D570](../../../06-decisions/f09-hr-and-projects/d570-linkedin-sending-prepared-by-default.md)).
The approval itself is not configurable.

## Open questions

None.

---

⬅️ [BR-F9-35 Default order of the scheduling objectives](br-f09-35-default-order-of-objectives.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F9-37](br-f09-37-outreach-stops-at-a-reply-a-refusal-or-day-60.md)
