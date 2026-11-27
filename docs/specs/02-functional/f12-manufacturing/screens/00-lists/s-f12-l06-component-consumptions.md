🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L06 Component consumptions

# 🗂️ S-F12-L06 Component consumptions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F12-06 Component consumption](../../data/e-f12-06-component-consumption.md) the user may
see: to find, filter, total and act on many component consumptions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Component consumptions, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "component consumptions" offers this view.
- **AI assistant:** "show the component consumptions that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Component consumptions    Manufacturing (plugin) › Component consumptions   [+ New]                          |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ORDER   STATE   COMPONENT   LOT   FINISHED LOT   QUANTITY                            |
| order             | [ ] ...                                                  Open >                          |
| component         | [ ] ...                                                  Open >                          |
| lot               | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Order | order | text | yes |
| State | state | badge: Active | yes |
| Component | component | label | yes |
| Lot | lot | label | yes |
| Finished lot | finished lot | text | yes |
| Quantity | quantity | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Order | each value | the visible rows (D488) |
| Component | product, lot | the visible rows (D488) |
| Lot | product, lot | the visible rows (D488) |
| Finished lot | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Component consumptions of a chosen component, or of the components that match a filter.
- From the other side: the components that have component consumptions, or none.
- Component consumptions of a chosen finished lot, or of the finished lots that match a filter.
- From the other side: the finished lots that have component consumptions, or none.
- Component consumptions of a chosen lot, or of the lots that match a filter.
- From the other side: the lots that have component consumptions, or none.
- Component consumptions of a chosen order, or of the orders that match a filter.
- From the other side: the orders that have component consumptions, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New component consumption | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- quantity: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F12-06 Consumption](../03-make-the-products/s-f12-06-consumption.md).

The records also show on: [S-F12-05 Shop-floor tablet](../03-make-the-products/s-f12-05-shop-floor-tablet.md),
[S-F12-15 Pick for production](../02-plan-production/s-f12-15-pick-for-production.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 component consumptions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no component consumption the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-f12-l06-component-consumptions-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f12-l06-component-consumptions-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-f12-l06-component-consumptions-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f12-l06-component-consumptions-u20-production-operator-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f12-l06-component-consumptions-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f12-l06-component-consumptions-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f12-l06-component-consumptions-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f12-l06-component-consumptions-u15-warehouse-operator-phone-dark.png) |
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f12-l06-component-consumptions-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l06-component-consumptions-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f12-l06-component-consumptions-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l06-component-consumptions-u21-production-planner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Component consumptions](README.md) |
| Workspaces | [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md) |
| Flows | [FL-F12-02](../../flows/fl-f12-02-plan-production.md), [FL-F12-03](../../flows/fl-f12-03-make-the-products.md), [FL-F12-11](../../flows/fl-f12-11-finite-schedule-and-the-tablet.md), [FL-SC05-01](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-01-production-setups.md) |

## Open questions

None.

---

⬅️ [S-F12-L05 Work orders](s-f12-l05-work-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L07 Quality control points](s-f12-l07-quality-control-points.md)
