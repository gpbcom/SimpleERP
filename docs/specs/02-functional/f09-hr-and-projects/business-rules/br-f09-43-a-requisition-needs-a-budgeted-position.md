🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-43 A requisition needs a budgeted position

# 📏 BR-F9-43 A requisition needs a budgeted position

**Status:** ✅ specified

## Statement

A job offer or hiring request can only be made for an approved position that has a free headcount and is not frozen;
otherwise it is refused with the position and the budget shown, and the owner can approve a new position first.

## Why

Hiring without a budgeted position commits the company to a salary nobody approved. The rule keeps the recruitment
pipeline tied to the plan. The owner's answer: "Headcount planning"
([D528](../../../06-decisions/f09-hr-and-projects/d528-benchmark-gaps-f09-hr-and-projects.md)).

## Examples

| Case | Result |
|---|---|
| The sales department has 1 approved position, free | a job offer can be requested |
| The position is already Open with an offer | a second request is refused |
| The position is Frozen | refused until the owner lifts the freeze |
| No position fits the request | refused, HR may plan a position for the owner's approval |
| A leaver frees a position | it returns to Approved, available for a new offer |

## Applies to

- [UC-F9-44 Plan headcount against budget](../use-cases/15-work-location-headcount-and-learning/uc-f09-44-plan-headcount-against-budget.md)
- [UC-F9-05 Publish jobs and source candidates](../use-cases/02-recruit/uc-f09-05-publish-jobs-and-source-candidates.md)
- [UC-F9-07 Make an offer and hire](../use-cases/02-recruit/uc-f09-07-make-an-offer-and-hire.md)
- [E-F9-49 Position](../data/e-f09-49-position.md)

## Exceptions

A replacement for a leaver in the same position is a request on the freed position, not a new one.

## Configurable

Yes: a company may switch the check off for small teams; the switch is audited.

## Open questions

None.

---

⬅️ [BR-F9-42 Remote-work allowances follow the agreement](br-f09-42-remote-work-allowances-follow-the-agreement.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-44 Successor lists are seen by HR and the line](br-f09-44-successor-lists-are-seen-by-hr-and-the-line.md)
