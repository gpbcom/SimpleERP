🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D502 Records on a map for planners and managers only

# 📜 D502 Records on a map for planners and managers only

**Status:** ✅ decided

## Context

Who sees records on a map ([D501](d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md)).

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

Planners and managers only: a "map" right held by the planner and manager roles. Everyone else sees the same records as
lists and addresses, never on a map. Customer-facing maps, the F11 store locator and the arrival time, are the
exceptions by nature.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-20).

## Consequences

- [E-F1-06 Role](../../02-functional/f01-administration/data/e-f01-06-role.md) holds the map right (change note);
  [BR-F1-32 Records on a map only for roles with the map
  right](../../02-functional/f01-administration/business-rules/br-f01-32-map-right-for-planners-and-managers.md).
- Map queries obey the same record and field rules as lists
  [REQ-T13-06](../../03-technical/t13-maps-and-geodata/requirements/req-t13-06-map-queries-respect-permissions.md),
  [D12](../foundations/d12-permissions-model.md).
- The [aggregated list view](../../04-ux/design-system/patterns/aggregated-list-view.md) offers its map layout only to
  those roles.
- Answered on 2026-11-13 ([D517](../foundations/d517-the-drafts-open-points-answered-on-2026-11-13.md)): field workers
  have no map, and an address on their phone shows a "Directions" button that opens their own navigation app;
  plans inside operational screens follow that screen's own rights; the planner roles are U29 Dispatcher, U25 Care
  coordinator, U22 Site manager, U24 Engagement manager, U21 Production
  planner, U23 Store manager, U38 Training coordinator, U34 Property manager, U43 Event producer and U28 Hotel
  receptionist, and the managers U02 and U13.

## Related

- [BR-F1-32 Records on a map only for roles with the map
  right](../../02-functional/f01-administration/business-rules/br-f01-32-map-right-for-planners-and-managers.md)
- [E-F1-06 Role](../../02-functional/f01-administration/data/e-f01-06-role.md)
- [Roles](../../01-users/roles.md)
- [REQ-T13-06 Map queries respect
  permissions](../../03-technical/t13-maps-and-geodata/requirements/req-t13-06-map-queries-respect-permissions.md)
- [D501 Maps: planning, list views, record pages, dashboards, in four
  domains](d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md)
- [D503 Who sees people's positions](../f09-hr-and-projects/d503-who-sees-peoples-positions.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D501](d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md) · ⬆️ [Up](README.md) ·
➡️ [D503 Who sees people's positions](../f09-hr-and-projects/d503-who-sees-peoples-positions.md)
