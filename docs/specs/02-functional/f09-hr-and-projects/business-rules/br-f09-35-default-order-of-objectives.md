🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-35 Default order of the scheduling objectives

# 📏 BR-F9-35 Default order of the scheduling objectives

**Status:** ✅ specified

## Statement

Among the eligible people, the engine ranks by its objectives in this default order (D517): lateness, travel,
customer preferences, fair workload, cost and margin; legal and required attributes are never objectives but hard
limits, and a configurator may change the order or the weights per request type.

## Why

- The owner's decision VD-32 ([D514](../../../06-decisions/f09-hr-and-projects/d514-scheduling-objectives.md)) sets the
  objectives:
  - travel and lateness;
  - customer preferences: continuity, preferred or refused people, language;
  - fair workload: working-time rules, rest, overtime;
  - cost and margin.
- The default order was answered as proposed on 2026-11-13 (D517).
- Required and legal attributes exclude people before any ranking (BR-F9-25, BR-F9-26).

## Examples

| Case | Result |
|---|---|
| Carer A on time, 25 minutes away; carer B 10 minutes late, 10 minutes away | A first: lateness comes before travel |
| Both on time and 10 minutes away; A is the usual carer | A first: continuity |
| Both equal on lateness, travel and preferences; A has worked 6 more hours this week | B first: fair workload |
| The request type "Urgent repair" puts travel first | The nearest eligible person first |
| The customer refused carer C | C is ranked last, as a customer preference |

## Applies to

- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-34](../use-cases/12-schedule-customer-requests/uc-f09-34-run-the-automatic-scheduling.md)
- [UC-F2-30](../../f02-no-code-configuration/use-cases/12-set-up-request-types/uc-f02-30-set-up-a-request-type.md)
- [E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)
- [E-F9-28 Assignment proposal](../data/e-f09-28-assignment-proposal.md)

## Exceptions

None. The legal limits of working time and rest are hard limits, not part of the fair-workload objective
([BR-F9-09 Shifts respect people and rules](br-f09-09-shifts-respect-people-and-rules.md)).

## Configurable

Yes (D517): the order and the weights of the objectives, per request type (UC-F2-30).

## Open questions

None.

---

⬅️ [BR-F9-34 Every override is logged with its reason](br-f09-34-overrides-logged-with-a-reason.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F9-36](br-f09-36-hr-approves-before-the-first-message.md)
