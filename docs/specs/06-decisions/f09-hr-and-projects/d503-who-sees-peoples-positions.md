🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D503 Who sees people's positions

# 📜 D503 Who sees people's positions

**Status:** 🔄 draft (GH-2 step S4b, from VD-21 / D503)

## Context

Who may see where an employee is, once maps exist
([D501](../ux/d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md)). Today a position is recorded
only at check-in and check-out, shown to the employee
[BR-F9-06](../../02-functional/f09-hr-and-projects/business-rules/br-f09-06-location-only-at-check-in.md).

## Options

- The customer (arrival time).
- Their manager.
- Their planner or dispatcher.
- The employee.

The owner ticked the first three: "The customer (arrival time), Their manager, Their planner or dispatcher". The
employee's own view is [D505](d505-the-employee-sees-their-own-position-live.md).

## Choice

Their planner or dispatcher and their manager, for planning only, and the customer, who sees only an arrival time during
the visit's window.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md), VD-21).

## Consequences

- [BR-F9-32 Who sees a person's
  position](../../02-functional/f09-hr-and-projects/business-rules/br-f09-32-who-sees-a-position.md).
- The customer sees an arrival time near their address during the visit's window, and nothing is kept
  [UC-F16-17](../../02-functional/f16-customer-support-agents/use-cases/06-take-in-every-request/uc-f16-17-follow-the-arrival-of-a-visit.md),
  [S-F16-15](../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-15-arrival-of-your-visit.md).
- (Proposed) to read: the CNIL's guidance on the geolocation of employees, in
  [CR-FR-211](../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md).

## Related

- [BR-F9-32 Who sees a person's
  position](../../02-functional/f09-hr-and-projects/business-rules/br-f09-32-who-sees-a-position.md)
- [CR-FR-211 Live geolocation of
  employees](../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md)
- [CR-FR-054 Location only when needed and
  announced](../../10-country-packs/france/data-protection/cr-fr-054-location-with-consent.md)
- [D502 Records on a map for planners and managers only](../ux/d502-records-on-a-map-for-planners-and-managers-only.md)
- [D504 Positions at check-in by default, live as a team option for drivers and
  carers](d504-positions-at-check-in-by-default-live-as-a-team-option-for-drivers-and-carers.md)
- [D505 The employee sees their own position live](d505-the-employee-sees-their-own-position-live.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md)

---

⬅️ [D502](../ux/d502-records-on-a-map-for-planners-and-managers-only.md) · ⬆️ [Up](README.md) ·
➡️ [D504](d504-positions-at-check-in-by-default-live-as-a-team-option-for-drivers-and-carers.md)
