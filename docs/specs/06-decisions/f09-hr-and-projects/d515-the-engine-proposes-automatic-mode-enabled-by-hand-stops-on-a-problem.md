🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D515 The engine proposes; automatic mode enabled by hand, stops on a problem

# 📜 D515 The engine proposes; automatic mode enabled by hand, stops on a problem

**Status:** ✅ decided

## Context

How much the scheduling engine decides on its own.

## Options

The owner's answer: "Proposes, planners confirms (by default) and a fully autonatic mode that stops and send a
notification to the planner if problem (it MUST be enabled manually)."

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

By default the engine proposes and the planner confirms. A fully automatic mode must be enabled by hand; in it the
engine assigns and re-plans on its own, and stops and notifies the planner at the first problem.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-33).

## Consequences

- New entity [E-F9-33 Automatic scheduling
  setting](../../02-functional/f09-hr-and-projects/data/e-f09-33-automatic-scheduling-setting.md), set on
  [S-F9-32](../../02-functional/f09-hr-and-projects/screens/12-schedule-customer-requests/s-f09-32-automatic-scheduling-settings.md).
- [BR-F9-33 Automatic mode enabled by hand, stops on a
  problem](../../02-functional/f09-hr-and-projects/business-rules/br-f09-33-automatic-mode-stops-on-a-problem.md): no
  candidate, a legal conflict, a window missed, over a cost limit, an overlap.
- [S-F9-31 Proposal
  review](../../02-functional/f09-hr-and-projects/screens/12-schedule-customer-requests/s-f09-31-proposal-review.md),
  [UC-F9-34](../../02-functional/f09-hr-and-projects/use-cases/12-schedule-customer-requests/uc-f09-34-run-the-automatic-scheduling.md).
- The administrator or the planners' manager switches it on, per team and request type (D517).

## Related

- [E-F9-33 Automatic scheduling
  setting](../../02-functional/f09-hr-and-projects/data/e-f09-33-automatic-scheduling-setting.md)
- [BR-F9-33 Automatic mode enabled by hand, stops on a
  problem](../../02-functional/f09-hr-and-projects/business-rules/br-f09-33-automatic-mode-stops-on-a-problem.md)
- [S-F9-31 Proposal
  review](../../02-functional/f09-hr-and-projects/screens/12-schedule-customer-requests/s-f09-31-proposal-review.md)
- [D514 Scheduling objectives](d514-scheduling-objectives.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D514 Scheduling objectives](d514-scheduling-objectives.md) · ⬆️ [Up](README.md) ·
➡️ [D516](../foundations/d516-naming-rules-and-the-seven-classes-of-names.md)
