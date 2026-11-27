🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-07 Scheduling engine

# 📌 REQ-T13-07 Scheduling engine

**Status:** 🔄 draft (GH-2 step S4b, from VD-27 to VD-33 / D509 to D515)

## Statement

The platform must schedule every work request: exclude the people missing a required attribute (verified and
current), rank the others by the preferred attributes and the objectives with the request type's weights, propose the
best with the next ones and the excluded with their reasons, apply it alone only in automatic mode, stop and notify the
planner at the first problem, and re-plan after a change.

Decided (D517): An open-source constraint solver run on the company's servers.

## Why

Every customer request becomes one work request that feeds scheduling (VD-30, VD-31); attributes count as required or
preferred with weights, legal ones always required (VD-27 to VD-29); objectives are travel and lateness, customer
preferences, fair workload, cost and margin (VD-32); the engine proposes, and automatic mode is enabled by hand and
stops on a problem (VD-33). It replaces the nine domain rules' separate checks with one mechanism.

Decided by the owner on 2026-11-13 (VD-27 to VD-33). The solver named is decided (D517).

## Acceptance criteria

1. A person missing a required attribute, or holding it unverified or expired, is never proposed
   [BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md),
   [BR-F9-27](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-27-unverified-attributes-do-not-count.md).
2. A legal requirement cannot be relaxed, by the planner or by a weight
   [BR-F9-26](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md).
3. Each proposal lists its candidates with scores and reasons, and the excluded with eligibility labels only
   [BR-F9-29](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-29-planners-see-eligibility-only.md).
4. With no eligible person, the work request is "Blocked" with the reasons listed.
5. In automatic mode, any of the problems (no eligible person, legal conflict, window missed, over the cost limit,
   overlap) stops the assignment and notifies the planner
   [BR-F9-33](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-33-automatic-mode-stops-on-a-problem.md).
6. Working-time and rest rules of the country pack are never broken by a proposal.
7. After an absence, a delay, an urgent request or a cancellation, the affected work requests are proposed again.
8. Every override is logged with its reason
   [BR-F9-34](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-34-overrides-logged-with-a-reason.md).

## Measure

Decided (D517): One work request proposed within 3 seconds for a team of 200 people; a day of 2,000 work requests
re-planned within 60 seconds. Proposals breaking a required or legal attribute: 0.

## Priority

Must (Proposed)

## Capabilities served

F9, F16, F2, F6, F7, F12; sectors SC01, SC03, SC04, SC06, SC07, SC09, SC10, SC12, SC13, SC15, SC16.

## Tests

Unit tests per rule on small teams with known answers (each branch of the eligibility check fires on real values);
load tests on a generated team; a test per stopping problem in automatic mode.

## Open questions

None.

---

⬅️ [REQ-T13-06 Map queries respect permissions](req-t13-06-map-queries-respect-permissions.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T13-08 Floor and venue plans](req-t13-08-floor-and-venue-plans.md)
