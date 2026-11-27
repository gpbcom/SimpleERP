🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-32 Records on a map only for roles with the map right

# 📏 BR-F1-32 Records on a map only for roles with the map right

**Status:** ✅ specified

## Statement

Records appear on a map (the map layout of a list view, a planning map, the mini-map of a record page, an area map on a
dashboard) only for a user who holds a role with the map right; every other user sees the same records as a list, with
their addresses, never on a map.

## Why

- The owner's decision VD-20 ([D502](../../../06-decisions/ux/d502-records-on-a-map-for-planners-and-managers-only.md),
  with [D501](../../../06-decisions/ux/d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md) for
  where maps appear): maps show where customers live and where people work, so only those who plan the work need them,
  the planners and the managers.
- The map right is one more right of a role (D12): it never widens what the user may see. A map shows only the records
  and fields the user may see, as every list does (D488,
  [REQ-T13-06](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-06-map-queries-respect-permissions.md)).
- Legal values from the France country pack:
  [CR-FR-050](../../../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md).

## Examples

| Case | Result |
|---|---|
| U29 Dispatcher, role with the map right, opens the trips | The list and its map layout |
| U03 Sales, role without the map right, opens the customers | The list only; the map layout is not offered |
| A manager with the map right and the record rule "own site" | The map shows the records of the site only |
| U30 Driver opens a stop on their phone | The address and a "Directions" button that opens the phone's own navigation app (D517) |
| A customer follows the arrival of their visit | The arrival time near their address: an exception by nature (BR-F9-32) |
| A visitor of the online shop looks for a store | The store locator: an exception by nature |

## Applies to

- [E-F1-06 Role](../data/e-f01-06-role.md)
- [E-F2-04 List view](../../f02-no-code-configuration/data/e-f02-04-list-view.md)
- [UC-F1-06 Edit a role and its record rules](../use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md)
- [UC-F2-17](../../f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-17-add-a-kanban-calendar-map-gantt-or-timeline-view.md)
- [UC-F9-36](../../f09-hr-and-projects/use-cases/12-schedule-customer-requests/uc-f09-36-see-work-and-places-on-a-map.md)
- [UC-F16-17](../../f16-customer-support-agents/use-cases/06-take-in-every-request/uc-f16-17-follow-the-arrival-of-a-visit.md)
  (an exception)
- [C-17 Map](../../../04-ux/design-system/components/c-17-map.md)

## Exceptions

Two customer-facing maps, by their nature (D502):
- the store locator of the online shop (F11), which shows only public places: stores and pickup points;
- the arrival time of a visit, which the customer sees near their address during the visit's window only (BR-F9-32).

Nobody may override the rule otherwise.

## Configurable

Yes, within limits:
- the map right is a right of a role like the others (D12): an administrator gives it to the company's own planner and
  manager roles (UC-F1-06);
- the ready-made planner and manager roles hold it (D517: U29 Dispatcher, U25 Care coordinator, U22 Site manager,
  U24 Engagement manager, U21 Production planner, U23 Store manager, U38 Training coordinator, U34 Property manager,
  U43 Event producer, U28 Hotel receptionist; the managers U02 and U13);
- giving the map right to a role that is neither a planner nor a manager role shows a warning first.

The two customer-facing exceptions cannot be changed.

## Open questions

None. Answered on 2026-11-13 (D517): field workers have no map, and an address on their phone
shows a "Directions" button that opens their own navigation app; the planner roles are those above; plans
inside operational screens follow that screen's own rights, not the map right.

---

⬅️ [BR-F1-31 Exports are complete and in open formats](br-f01-31-exports-are-complete-and-in-open-formats.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F1-33 Sessions end on role change or revocation](br-f01-33-sessions-end-on-role-change-or-revocation.md)
