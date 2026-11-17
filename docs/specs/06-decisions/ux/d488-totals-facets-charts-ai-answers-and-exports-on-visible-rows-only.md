🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D488 Totals, facets, charts, AI answers and exports on visible rows only

# 📜 D488 Totals, facets, charts, AI answers and exports on visible rows only

**Status:** 🔄 draft (GH-2 step S4, from VD-05 / D488)

## Context

What the totals of a list count when the user may not see every record, and whether hidden records may be hinted at.

## Options

- Visible rows only.
- Visible rows, and a hint that other records exist.
- Managers see the totals of every record.

## Choice

Visible rows only: every count, total, facet, chart, AI answer and export uses only the rows and fields the user may
see; nothing hints that other records exist; a field the user may not read never appears as a column, a filter or a
facet.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 5).

## Consequences

- The list shows one fixed sentence ("Counts, totals, facets and the chart use only the records you may see"), never a
  count of hidden records.
- The plain-words filter refuses a hidden field: "You cannot filter on that field."
- (Proposed) T2 applies the record and field rules to lists, aggregates, facets and exports; the server checks bulk
  actions and inline edits again ([T2](../../03-technical/t02-identity-and-access/README.md)).
- It applies [D12](../foundations/d12-permissions-model.md) to every part of the list.

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [D12 Permissions model](../foundations/d12-permissions-model.md)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [D486 Plain-words filter, facets with counts, related-record
  filters](d486-plain-words-filter-facets-with-counts-related-record-filters.md)
- [D489 List actions: bulk, export, inline edit, ask about the list, open the
  record](d489-list-actions-bulk-export-inline-edit-ask-about-the-list-open-the-record.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D487 KPI strip, default chart and the Chart button](d487-kpi-strip-default-chart-and-the-chart-button.md) ·
⬆️ [Up](README.md) · ➡️ [D489](d489-list-actions-bulk-export-inline-edit-ask-about-the-list-open-the-record.md)
