🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-36 HR approves the shortlist and the sequence before the first message

# 📏 BR-F9-36 HR approves the shortlist and the sequence before the first message

**Status:** 🔄 waiting for the owner

## Statement

No invitation or message goes to a prospect until HR has approved, once, who is contacted and every template of the
sequence; the follow-ups then go out on their own until a reply, a refusal or day 60.

## Why

The owner's answer LS-2 ([D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)):
"The shortlist and the sequence, once (Recommended)". Ranking candidates is a high-risk AI use (EU AI Act, Annex III,
point 4(a)); this approval is the human oversight
[BR-F4-21](../../f04-meetings/business-rules/br-f04-21-candidate-scoring-is-high-risk-ai.md) asks for.

## Examples

| Case | Result |
|---|---|
| 12 shortlisted prospects, every template approved | passes: the day 0 invitations go |
| The shortlist approved, follow-up 2 without a template | fails: nothing goes |
| A prospect added after the approval | waits until HR approves that prospect |
| (Proposed) A template changed after the approval | the next message using it waits for approval |
| Follow-up 1 on day 7 | goes without a new approval |

## Applies to

- [UC-F9-40 Search and rank LinkedIn profiles](../use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md)
- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [UC-F9-42 Turn a positive reply into an applicant](../use-cases/02-recruit/uc-f09-42-turn-a-positive-reply-into-an-applicant.md)
- [E-F9-46 Outreach sequence](../data/e-f09-46-outreach-sequence.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F9-35 Default order of the scheduling objectives](br-f09-35-default-order-of-objectives.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F9-37](br-f09-37-outreach-stops-at-a-reply-a-refusal-or-day-60.md)
