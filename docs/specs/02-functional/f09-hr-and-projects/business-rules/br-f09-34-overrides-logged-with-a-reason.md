🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-34 Every override is logged with its reason

# 📏 BR-F9-34 Every override is logged with its reason

**Status:** 🔄 draft (GH-2 step S4b, from VD-28, VD-33 / D510, D515)

## Statement

Every time a planner departs from what the request type or the engine gives (an attribute added or relaxed on one
request, a person other than the proposed one, a proposal edited), the change is saved with who, when, what and a
reason, which is required; the log stays with the assignment proposal.

## Why

- The owner's decision VD-28
  [D510](../../../06-decisions/f09-hr-and-projects/d510-attributes-chosen-per-request-type-adjustable-per-request.md):
  the planner may add or relax an attribute on a single request, logged.
- The owner's decision VD-33
  [D515](../../../06-decisions/f09-hr-and-projects/d515-the-engine-proposes-automatic-mode-enabled-by-hand-stops-on-a-problem.md);
  the planner confirms, edits or overrides a proposal; an override carries its reason.
- A later question ("why was this person sent?") must have its answer, for the customer, the employee and an inspector.

## Examples

| Case | Result |
|---|---|
| The planner picks the second-ranked carer | Reason required, for example "The customer asked for Marie"; logged |
| The planner relaxes "Spanish" on one request | Logged with the reason |
| The planner confirms the proposal as it is | No reason asked |
| The reason is left empty | The change cannot be saved |
| The planner tries to relax a legal requirement | Refused (BR-F9-26) |
| A supervisor lets a supervised trainee sign in at a work centre | Logged with the reason (BR-F12-17) |

## Applies to

- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-35 Re-plan after a change](../use-cases/12-schedule-customer-requests/uc-f09-35-re-plan-after-a-change.md)
- [UC-F12-22](../../f12-manufacturing/use-cases/10-people-and-tools/uc-f12-22-require-operator-qualifications-per-work-centre.md)
- [E-F9-28 Assignment proposal](../data/e-f09-28-assignment-proposal.md)
- [E-F16-12 Work request](../../f16-customer-support-agents/data/e-f16-12-work-request.md)

## Exceptions

None.

## Configurable

No. (Proposed) A company may keep a list of common reasons to pick from, beside the free text.

## Open questions

None.

---

⬅️ [BR-F9-33 Automatic mode enabled by hand, stops on a problem](br-f09-33-automatic-mode-stops-on-a-problem.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-35 Default order of the scheduling objectives](br-f09-35-default-order-of-objectives.md)
