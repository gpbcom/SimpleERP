🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-33 Automatic mode enabled by hand, stops on a problem

# 📏 BR-F9-33 Automatic mode enabled by hand, stops on a problem

**Status:** 🔄 draft (GH-2 step S4b, from VD-33 / D515)

## Statement

By default the scheduling engine proposes and a planner confirms; the automatic mode, in which the engine assigns and
re-plans on its own, runs only for the teams and request types where a person switched it on by hand, and at the first
problem (no eligible candidate, a legal conflict, a window missed, over the cost limit, an overlap) it stops, leaves the
work request as a proposal and notifies the planner.

## Why

The owner's decision VD-33
[D515](../../../06-decisions/f09-hr-and-projects/d515-the-engine-proposes-automatic-mode-enabled-by-hand-stops-on-a-problem.md),
word for word: "Proposes, planners confirms (by default) and a fully autonatic mode that stops and send a notification
to the planner if problem (it MUST be enabled manually)."

## Examples

| Case | Result |
|---|---|
| A new team; nobody switched the automatic mode on | Proposals only; the planner confirms each one |
| Switched on for the home-care team and the request type "Weekly visit"; a carer falls ill | The engine re-plans and assigns; the planner sees it in the log |
| Automatic mode; no eligible carer for one visit | It stops; the planner is notified; the visit waits as Blocked |
| Automatic mode; the only plan goes over the cost limit | It stops; the planner is notified and gets the proposal |
| Same team, request type "Urgent repair" not switched on | A proposal for the planner |
| A sector pack is installed | The automatic mode stays off |

## Applies to

- [UC-F9-34](../use-cases/12-schedule-customer-requests/uc-f09-34-run-the-automatic-scheduling.md)
- [UC-F9-35 Re-plan after a change](../use-cases/12-schedule-customer-requests/uc-f09-35-re-plan-after-a-change.md)
- [E-F9-33 Automatic scheduling setting](../data/e-f09-33-automatic-scheduling-setting.md)
- [E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)
- [E-F9-28 Assignment proposal](../data/e-f09-28-assignment-proposal.md)

## Exceptions

None: the automatic mode is never on by default, and never switched on by a template, a pack or the engine itself.

## Configurable

Yes:
- per team and per request type, switched on by hand; the request type says whether the automatic mode is allowed;
- by the administrator or the planners' manager (D517);
- who is notified when it stops;
- (Proposed) the cost limit, per request type.

When it stops on one work request, it goes on for the others (D517).

## Open questions

None.

---

⬅️ [BR-F9-32 Who sees a person's position](br-f09-32-who-sees-a-position.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-34 Every override is logged with its reason](br-f09-34-overrides-logged-with-a-reason.md)
