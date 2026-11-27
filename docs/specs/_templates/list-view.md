🏠 [Specs](../README.md) › 🧱 [Templates](README.md) › 🖥️ List view template

# 🖥️ List view template

**Status:** 🔄 draft (GH-2 step S4, from VD-01 to VD-12, VD-18 to VD-20 / D484 to D495, D501, D502)

Copy this file for a new page of this kind: the aggregated list view of one record type, named "S-<capability>-L<nn>
<View>" (Proposed: in a `screens/00-lists/` folder of its capability). It follows the
[aggregated list view pattern](../04-ux/design-system/patterns/aggregated-list-view.md); its content comes from the
entity's view card, derived by the [view rules](../../tickets/GH-2/resources/flowcharts-screens/PLAN.md#view-rules) VR-1
to VR-15 and reviewed with the owner
([D492](../06-decisions/ux/d492-view-content-derived-by-rules-reviewed-per-capability.md)). Keep every section, in this
order; write "None" or link a question in `07-questions/` rather than leave one blank.

## Personas

_Links to the personas whose use cases list the record type, most frequent first (VR-3), and what each one sees
differently: rows (their record rules), columns (their field rules), actions. An admin list adds U07, and U48 for
hosting records (D494)._

## Purpose

_What the list is for, in one sentence._

## Entry points

_The capability's menu path, "<capability> › <view>" or "Administration › <view>" (VR-1, D495); the workspaces that
embed it, with their default saved view (D493); the global search; the AI assistant._

## Wireframe

_A text wireframe in a code block, from the pattern's anatomy: header, KPI strip, toolbar, chips, facet panel, bulk bar,
table, permission note._

## Columns

_A table: label, field, format, sortable. The identifying field, then the state, people, links, amounts, dates,
categories and numbers; 7 at most; secrets never (VR-4)._

## Facets

_A table: facet, values, counted on. State, category, people and link fields, 8 at most (VR-5, D486). Add the "Eligible
for" facet when the record type is people who can be scheduled, or work to schedule (D511): the request types or
operations, and the reason categories a planner may see (BR-F9-29). Otherwise "None" for that facet._

## Related-record filters

_The filters on linked records, both ways ("customers with an overdue invoice", "invoices of a customer in Lyon"),
VR-6._

## KPI strip

_The 2 to 4 tiles: count, total of the first amount, "needs attention" count, dated count (VR-7, D487, C-16)._

## Default chart

_Count by state (stacked by amount when there is one), else by month of the first date, else by the first facet (VR-8)._

## Saved views

_All; Mine; Open; By state; Needs attention; Recently changed (VR-9, D109); and each persona's default._

## Map layout

_For a record type that holds a place: the place field, the map ([C-17](../04-ux/design-system/components/c-17-map.md))
or the plan ([C-18](../04-ux/design-system/components/c-18-plan.md)), the marker's label and state, the layers, and the
roles that hold the map right and so see the switch (D501, D502, BR-F1-32). Otherwise "None: no place."_

## Actions

_A table: action, where (header, toolbar, bulk bar, row), who may use it, result. Bulk actions: change state (allowed
transitions only), assign, tag, export, delete when the rules allow, each within the role and audited (VR-10, D489);
export as CSV or XLSX; "Ask about this list"._

## Inline edit

_The fields editable in a cell: category, date, person and number fields that are neither identifying, personal data nor
locked by the record's state (VR-11)._

## Hidden fields

_The fields some personas may not read, and for whom (VR-12, D488): they are never a column, a facet, a filter, a chart
axis or a plain-words filter target._

## Row opens

_The record's own screen that "Open ›" goes to (VR-13); none yet → step S7 draws one._

## States

_The states of the view (Loading, Listed, Filtered, No result, Empty, Selected, Error) from the pattern, and what each
shows; for a map layout, the count of rows without a place._

## Responsive behaviour

_On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer, the KPI strip stays
(VR-14, D491); the map takes the full width._

## Accessibility

_Landmarks, the announced result count, the named chips, the facet drawer's focus, and the table that holds the same
rows as the map._

## Example images

_A table: shows, device, light, dark; one row per persona and device, for each state that has images (D490, D500)._

## Components

_Links to the design-system components it uses: [C-03](../04-ux/design-system/components/c-03-data-table.md),
[C-15](../04-ux/design-system/components/c-15-facet-panel.md),
[C-16](../04-ux/design-system/components/c-16-kpi-strip.md), [C-09](../04-ux/design-system/components/c-09-chart.md),
and [C-17](../04-ux/design-system/components/c-17-map.md) or [C-18](../04-ux/design-system/components/c-18-plan.md) for
a map layout._

## Shown in

_Links to the workspaces, flows and journeys that show it._

## Open questions

_Links to open questions, or "None"._

---

⬅️ [Screen template](screen.md) · ⬆️ [Up](README.md) · ➡️ [Journey template](journey.md)

