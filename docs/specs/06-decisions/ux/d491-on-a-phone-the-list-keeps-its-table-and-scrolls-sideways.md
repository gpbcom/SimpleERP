🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D491 On a phone the list keeps its table and scrolls sideways

# 📜 D491 On a phone the list keeps its table and scrolls sideways

**Status:** 🔄 draft (GH-2 step S4, from VD-08 / D491)

## Context

How an aggregated list view shows on a phone.

## Options

- Cards and a filter sheet.
- The same as on a desktop, scrolling.
- Not on a phone.

## Choice

The same as on a desktop: the phone keeps the table, which scrolls sideways; the facet panel becomes a drawer; the KPI
strip stays.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 8).

## Consequences

- C-03 Data table: in an aggregated list view the rows no longer become cards on a phone (change of step S4).
- [C-15 Facet panel](../../04-ux/design-system/components/c-15-facet-panel.md) has a drawer variant opened by "Facets".
- The rule VR-14 of the [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md#view-rules);
  [Responsive](../../04-ux/design-system/responsive.md).

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [C-03 Data table](../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../04-ux/design-system/components/c-15-facet-panel.md)
- [Responsive](../../04-ux/design-system/responsive.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D490](d490-example-images-for-every-persona-that-can-open-a-view.md) · ⬆️ [Up](README.md) ·
➡️ [D492](d492-view-content-derived-by-rules-reviewed-per-capability.md)
