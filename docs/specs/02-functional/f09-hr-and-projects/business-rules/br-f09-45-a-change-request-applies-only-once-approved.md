🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-45 A change request applies only once approved

# 📏 BR-F9-45 A change request applies only once approved

**Status:** ✅ specified

## Statement

A change to a project's scope, budget, days or dates is applied only from an approved change request: approved by the
customer when the work is billed to a customer, and by the owner when it is internal; a request that is Draft,
Submitted, Rejected or Withdrawn changes nothing.

## Why

Unapproved changes are the usual cause of disputes over price and dates. The rule keeps one written, dated decision
behind each change. The owner's answer: "Project risks and changes"
([D528](../../../06-decisions/f09-hr-and-projects/d528-benchmark-gaps-f09-hr-and-projects.md)).

## Examples

| Case | Result |
|---|---|
| The customer approves 12 days and 9000 euros | the project is changed and a quote line is created |
| The request is still Submitted | nothing changes |
| The customer rejects | the scope and price stay, the request is kept |
| An internal change of 2 days | the owner approves, the plan changes |
| The customer approves a lower amount | a new request is written for the accepted part |

## Applies to

- [UC-F9-46 Log project risks and change requests](../use-cases/15-work-location-headcount-and-learning/uc-f09-46-log-project-risks-and-change-requests.md)
- [E-F9-51 Change request](../data/e-f09-51-change-request.md)
- [UC-F9-17 Manage projects and tasks](../use-cases/06-plan-and-deliver-work/uc-f09-17-manage-projects-and-tasks.md)

## Exceptions

A change under the amount the owner sets as a tolerance may be approved by the engagement manager alone.

## Configurable

Yes: the tolerance amount and who approves internal changes are set per company.

## Open questions

None.

---

⬅️ [BR-F9-44 Successor lists are seen by HR and the line](br-f09-44-successor-lists-are-seen-by-hr-and-the-line.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-46 Certificates follow a passed assessment](br-f09-46-certificates-follow-a-passed-assessment.md)
