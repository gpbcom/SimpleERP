🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D487 KPI strip, default chart and the Chart button

# 📜 D487 KPI strip, default chart and the Chart button

**Status:** ✅ decided

## Context

Which charts an aggregated list view shows.

## Options

- A KPI strip and a chart.
- Charts on demand.
- Both.
- None.

## Choice

Both: a KPI strip of 2 to 4 totals and one default chart above the table, which the user can collapse; and a "Chart"
button that turns the filtered list into a [C-09 Chart](../../04-ux/design-system/components/c-09-chart.md) the user can
pin to their home screen.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), answer 4).

## Consequences

- New component [C-16 KPI strip](../../04-ux/design-system/components/c-16-kpi-strip.md).
- C-09 Chart gains "chart from a list" and "pin to home" (change of step S4).
- The rules VR-7 and VR-8 of the plan (the owner's interview notes of 2026-11 for the specifications, not kept in the repository) derive
  each view's totals and default chart.
- The first page and the KPI strip show within 1 second on 100,000 records
  ([Performance](../../05-non-functional/performance.md)).

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [C-16 KPI strip](../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../04-ux/design-system/components/c-09-chart.md)
- [D488 Totals, facets, charts, AI answers and exports on visible rows
  only](d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D486](d486-plain-words-filter-facets-with-counts-related-record-filters.md) · ⬆️ [Up](README.md) ·
➡️ [D488](d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md)
