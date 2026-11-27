🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-16 KPI strip

# 🧩 C-16 KPI strip

**Status:** ✅ specified

## Purpose

Shows 2 to 4 totals and one default chart of the filtered visible rows above an [aggregated list
view](../patterns/aggregated-list-view.md)'s table
([D487](../../../06-decisions/ux/d487-kpi-strip-default-chart-and-the-chart-button.md)).

## Anatomy

```text
+------------------------------------------------------------------------------------+
| [ 42      ] [ 1,284,300 EUR ] [ 9            ] [ 6              ] | count by stage   |
| [ open    ] [ pipeline      ] [ due in 7 days] [ won this month ] | ##### ### ## #   |
|                                                                   |          [Hide ^]|
+------------------------------------------------------------------------------------+
```

1. **Tiles:** a figure and its label, from the view card (rule VR-7 of the plan (the owner's interview notes of 2026-11
   for the specifications, not kept in the repository)): the count, the total of the first amount, a "needs attention"
   count and a dated count ("due in 7 days" or "new this month").
2. **Default chart:** a small [C-09 Chart](c-09-chart.md), rule VR-8: count by state (stacked by amount when there is
   one), else by month of the first date, else by the first facet.
3. **Hide:** collapses the strip to one line of figures; the choice is kept per user and view.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-16-kpi-strip-desktop-light.png) | ![Variants and states, dark](../images/c-16-kpi-strip-desktop-dark.png) |

## Variants

- **With chart:** the default, on a desktop.
- **Figures only:** collapsed, or on a view card with no chart.
- **Phone:** the tiles in one row that scrolls sideways; the chart below them, collapsed by default
  ([D491](../../../06-decisions/ux/d491-on-a-phone-the-list-keeps-its-table-and-scrolls-sideways.md)).
- **Tile as a filter:** a "needs attention" or dated tile adds its filter as a chip when pressed.

## States

| State | Look |
|---|---|
| Loading | Skeleton figures; within 1 second on 100,000 records |
| Normal | The figures of the filtered visible rows |
| Recomputing | Figures dim while the filters change |
| Zero | "0" with its label, never hidden |
| Collapsed | One line of figures, "Show ˅" |
| Error | A dash in place of each figure and a retry link ([error message pattern](../patterns/error-messages.md)) |

## Tokens

Figures in the dashboard face, as the figure variant of [C-09](c-09-chart.md)
([Typography](../../visual-identity/typography.md)), with tabular figures; labels in `font-caption` and
`color-text-muted`; tiles on `color-surface` with `elevation-1` and `color-border` ([Tokens](../tokens.md),
[Colours](../../visual-identity/colours.md)); `color-warning` only for the "needs attention" tile, with its word.

## Accessibility

- The strip is a region named "Totals of this list"; each tile reads as one sentence ("42 open opportunities").
- New figures are announced politely after a filter change, once, not tile by tile.
- The chart has its table and summary, as every [C-09 Chart](c-09-chart.md).
- Hide and Show are buttons that state whether the strip is expanded.

## Do and don't

- Do compute every figure on the visible rows only, with the same filters as the table
  [D488](../../../06-decisions/ux/d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md).
- Do show money with its currency.
- Don't show more than 4 tiles.
- Don't hint that hidden records exist, such as "42 of 60".

## Used in

The [aggregated list view pattern](../patterns/aggregated-list-view.md), and so every list page; for example
[S-F16-14](../../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## Open questions

None.

---

⬅️ [Facet panel](c-15-facet-panel.md) · ⬆️ [Up](README.md) · ➡️ [Map](c-17-map.md)

