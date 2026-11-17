🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 👥 [HR and projects](README.md) › 🤖 AI

# 🤖 AI

**Status:** ✅ specified

## What the AI assistant can do

Every action of this capability can be triggered from the AI assistant, within the user's roles; changes are confirmed,
irreversible acts prepared for the user
([BR-F3-34](../f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md)).

Read CVs, pre-screen candidates by voice (BR-F9-12), draft job descriptions and contracts, check contract templates
continuously (BR-F9-13), suggest shifts, draft timesheets from the employee's own activity when they opted in
(BR-F9-07), answer employees' HR questions with the legal assistant (F15).

Rank LinkedIn profiles against a job position's criteria, with a short reason per score, and classify the replies to an
outreach sequence as positive, negative, question or unclear
([UC-F9-40](use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md),
[UC-F9-41](use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md),
[D518](../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)). Ranking candidates is a
high-risk AI use (EU AI Act, Annex III, point 4(a), [AI governance](../../05-non-functional/ai-governance.md)); HR
approves the shortlist ([BR-F9-36](business-rules/br-f09-36-hr-approves-before-the-first-message.md)) and the AI
assistant never contacts or rejects anyone on its own.

## Permissions

The user's roles; HR data rules (BR-F9-02).

## Models

"CV reading", "Voice pre-screening" and "Planning suggestions" AI feature settings in F1 (D82), local by default.

(Proposed) "Profile ranking" and "Reply classification" AI feature settings in F1 for LinkedIn sourcing.

## Open questions

None.

---

⬅️ [Integrations](integrations.md) · ⬆️ [Up](README.md) · ➡️ [Regulatory](regulatory.md)
