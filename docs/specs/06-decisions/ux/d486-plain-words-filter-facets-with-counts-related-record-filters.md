🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D486 Plain-words filter, facets with counts, related-record filters

# 📜 D486 Plain-words filter, facets with counts, related-record filters

**Status:** ✅ decided

## Context

How users filter an aggregated list view beyond the field filters and saved views of
[D109](../f02-no-code-configuration/d109-list-views.md).

## Options

- A facet sidebar with counts.
- A plain-words filter, turned into filters by the AI assistant.
- Related-record filters ("customers with an overdue invoice").
- Other layouts: board, calendar, map, timeline.

## Choice

The first three, on every aggregated list view: the plain-words filter, the facet panel with counts and the
related-record filters. Board, calendar and timeline layouts are not part of it.

Amended on 2026-11-13 by [D501](d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md) and
[D502](d502-records-on-a-map-for-planners-and-managers-only.md): the views of record types that hold a place offer a map
layout to the roles that hold the map right.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), answer 3). Amended by the owner on 2026-11-13
(VD-18, VD-20).

## Consequences

- New component [C-15 Facet panel](../../04-ux/design-system/components/c-15-facet-panel.md): values with counts,
  related-record filters, a drawer on a phone.
- The AI assistant turns plain words into filter chips the user sees and can edit; it refuses a field the user may not
  read ([D488](d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md)).
- Related-record filters work both ways ("customers with an overdue invoice", "invoices of a customer in Lyon").
- A pipeline or a delivery round stays a table in its aggregated view; an existing board screen, such as [S-F6-01
  Pipeline](../../02-functional/f06-customers-and-sales/screens/01-lead-to-quote/s-f06-01-pipeline.md), stays the record
  type's own screen.
- [E-F2-04 List view](../../02-functional/f02-no-code-configuration/data/e-f02-04-list-view.md) saves the layout (table
  or map) of a view (change note).
- Amended by D501 and D502: a record type that has a place gets a map layout on its view, for the roles that
  hold the map right. Board, calendar and timeline layouts stay out.

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [C-15 Facet panel](../../04-ux/design-system/components/c-15-facet-panel.md)
- [D109 Shared and personal list views](../f02-no-code-configuration/d109-list-views.md)
- [E-F2-04 List view](../../02-functional/f02-no-code-configuration/data/e-f02-04-list-view.md)
- [D501 Maps: planning, list views, record pages, dashboards, in four
  domains](d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md)
- [D502 Records on a map for planners and managers only](d502-records-on-a-map-for-planners-and-managers-only.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D485 Every entity has an aggregated view](d485-every-entity-has-an-aggregated-view.md) · ⬆️ [Up](README.md) ·
➡️ [D487 KPI strip, default chart and the Chart button](d487-kpi-strip-default-chart-and-the-chart-button.md)
