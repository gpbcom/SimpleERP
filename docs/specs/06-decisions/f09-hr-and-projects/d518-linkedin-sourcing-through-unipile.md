🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D518 LinkedIn sourcing through Unipile

# 📜 D518 LinkedIn sourcing through Unipile

**Status:** ✅ decided

## Context

The owner asked on 2026-11-13 at 10:27: "check is the HR use cases has a sourcing use case : browse LinkedIn profiles
(Unipile) and searching with a rich set of creterias & AI which candidates are the best choices, then send them messages
and check periodically the response (mot mode than 2 months). If the candidate answer positively schedule a meeting."
The specifications had one step in
[UC-F9-05](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-05-publish-jobs-and-source-candidates.md)
and [D235](../f04-meetings/d235-recruitment-split.md)'s note that sourcing and campaigns are F9 use cases. Four
questions were asked, each with a recommended answer.

## Options

- LS-1, where it goes: new use cases in F9 Recruit, or a step of UC-F9-05 only.
- LS-2, what HR confirms: the shortlist and the sequence once, or every message.
- LS-3, follow-ups and the reply check: an invitation then 2 follow-ups, or other rhythms; always within two months.
- LS-4, the meeting on a positive answer: three slots proposed by the AI assistant in the thread, or the booking link of
  the applicant pipeline.
- The [interview record](../../../tickets/GH-2/interviews/2026-11-13-wording-and-views.md) keeps the owner's answers,
  not every option.

## Choice

LinkedIn sourcing is a set of F9 Recruit use cases on Unipile, an F24 connector; HR approves the shortlist and the
templates once, an invitation and two follow-ups go within 60 days, and a positive answer becomes an applicant with the
booking link.

| # | Point | Decision | The owner's answer |
|---|---|---|---|
| LS-1 | Where it goes | New use cases in F9 Recruit with a flow, entities, screens and rules; Unipile is an F24 connector, its API key in the secret store | "New use cases in F9 Recruit (Recommended)" |
| LS-2 | What HR confirms before sending | HR approves who is contacted and the message templates once; follow-ups then go out on their own until a reply, a refusal or day 60 | "The shortlist and the sequence, once (Recommended)" |
| LS-3 | Follow-ups and reply check | A connection request with a note on day 0 (a direct message when already connected), follow-ups on days 7 and 21 by default (adjustable), replies checked every few hours, everything stops at a reply, a refusal or day 60 | "Invite, then 2 follow-ups (Recommended)" |
| LS-4 | The meeting on a yes | The candidate gets the self-scheduling link the applicant pipeline uses; the prospect becomes an applicant, source "sourcing" | "Send a booking link" |

## Decided by

The owner, on 2026-11-13 at 10:30, in the GH-2 interview round on the wording and the views
([interview record](../../../tickets/GH-2/interviews/2026-11-13-wording-and-views.md), section "LinkedIn sourcing
through Unipile").

## Consequences

- Use cases
  [UC-F9-40 Search and rank LinkedIn profiles](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md),
  [UC-F9-41 Run a LinkedIn outreach sequence](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
  and
  [UC-F9-42 Turn a positive reply into an applicant](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-42-turn-a-positive-reply-into-an-applicant.md),
  drawn in
  [FL-F9-14 Source candidates on LinkedIn](../../02-functional/f09-hr-and-projects/flows/fl-f09-14-source-candidates-on-linkedin.md);
  the sourcing branch is added to [FL-F9-02 Recruit](../../02-functional/f09-hr-and-projects/flows/fl-f09-02-recruit.md)
  and step 3 of
  [UC-F9-05](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-05-publish-jobs-and-source-candidates.md)
  links them.
- Entities [E-F9-44 Sourcing search](../../02-functional/f09-hr-and-projects/data/e-f09-44-sourcing-search.md),
  [E-F9-45 Prospect](../../02-functional/f09-hr-and-projects/data/e-f09-45-prospect.md),
  [E-F9-46 Outreach sequence](../../02-functional/f09-hr-and-projects/data/e-f09-46-outreach-sequence.md) and
  [E-F9-47 Outreach message](../../02-functional/f09-hr-and-projects/data/e-f09-47-outreach-message.md); the LinkedIn
  account linked through Unipile is a
  [E-F24-02 Tool connection](../../02-functional/f24-integrations-hub/data/e-f24-02-tool-connection.md), not a new
  entity.
- Rules
  [BR-F9-36 HR approves the shortlist and the sequence before the first message](../../02-functional/f09-hr-and-projects/business-rules/br-f09-36-hr-approves-before-the-first-message.md),
  [BR-F9-37 An outreach sequence stops at a reply, a refusal or day 60](../../02-functional/f09-hr-and-projects/business-rules/br-f09-37-outreach-stops-at-a-reply-a-refusal-or-day-60.md),
  [BR-F9-38 A sourced person is told at the first contact at the latest](../../02-functional/f09-hr-and-projects/business-rules/br-f09-38-sourced-people-told-at-the-first-contact.md),
  [BR-F9-39 Prospects are kept only as long as the sequence needs them](../../02-functional/f09-hr-and-projects/business-rules/br-f09-39-prospects-kept-only-as-long-as-needed.md),
  [BR-F9-40 No search criterion the law forbids in hiring](../../02-functional/f09-hr-and-projects/business-rules/br-f09-40-no-criterion-the-law-forbids-in-hiring.md)
  and
  [BR-F9-41 The LinkedIn account's limits are respected](../../02-functional/f09-hr-and-projects/business-rules/br-f09-41-linkedin-account-limits-respected.md).
- Screens
  [S-F9-37 LinkedIn sourcing search](../../02-functional/f09-hr-and-projects/screens/02-recruit/s-f09-37-linkedin-sourcing-search.md),
  [S-F9-38 Outreach sequence](../../02-functional/f09-hr-and-projects/screens/02-recruit/s-f09-38-outreach-sequence.md)
  and
  [S-F9-39 Prospect conversations](../../02-functional/f09-hr-and-projects/screens/02-recruit/s-f09-39-prospect-conversations.md).
- Unipile is a connector of the F24 catalogue (UC-F24-02, BR-F24-12): its API key in the secret store, never in
  configuration or logs (BR-F24-08); each HR user links their own LinkedIn account on Unipile's hosted sign-in page, so
  simple-ERP never sees the LinkedIn password.
- Ranking candidates is a high-risk AI use (EU AI Act, Annex III, point 4(a)):
  [BR-F4-21 Candidate scoring is high-risk AI](../../02-functional/f04-meetings/business-rules/br-f04-21-candidate-scoring-is-high-risk-ai.md)
  applies, and LS-2's approval is the human oversight.
- Open:
  [Q18 LinkedIn automation and its user agreement](../../07-questions/q18-linkedin-automation-and-its-user-agreement.md)
  and [Q19 Which LinkedIn search sourcing uses](../../07-questions/q19-which-linkedin-search-sourcing-uses.md).

## Related

- [D235 Recruitment: interviews here, the rest in F9](../f04-meetings/d235-recruitment-split.md)
- [D234 Scoring calls and candidates](../f04-meetings/d234-scoring-calls-and-candidates.md)
- [BR-F4-21 Candidate scoring is high-risk AI](../../02-functional/f04-meetings/business-rules/br-f04-21-candidate-scoring-is-high-risk-ai.md)
- [Q18 LinkedIn automation and its user agreement](../../07-questions/q18-linkedin-automation-and-its-user-agreement.md)
- [Q19 Which LinkedIn search sourcing uses](../../07-questions/q19-which-linkedin-search-sourcing-uses.md)
- [UC-F24-02 Connect a tool in the fewest steps](../../02-functional/f24-integrations-hub/use-cases/01-find-and-connect/uc-f24-02-connect-a-tool-in-the-fewest-steps.md)
- [BR-F24-12 The catalogue covers every business category](../../02-functional/f24-integrations-hub/business-rules/br-f24-12-the-catalogue-covers-every-business-category.md)
- [BR-F24-08 Credentials in the vault](../../02-functional/f24-integrations-hub/business-rules/br-f24-08-credentials-in-the-vault.md)
- [AI governance](../../05-non-functional/ai-governance.md)
- [Interview record](../../../tickets/GH-2/interviews/2026-11-13-wording-and-views.md)

---

⬅️ [D517](../foundations/d517-the-drafts-open-points-answered-on-2026-11-13.md) · ⬆️ [Up](README.md) ·
➡️ [D519 View cards reviewed: list pages and workspaces](../ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)
