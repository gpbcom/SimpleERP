🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L11 Stock counts

# 🗂️ S-F7-L11 Stock counts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F7-11 Stock count](../../data/e-f07-11-stock-count.md) the user may see: to find,
filter, total and act on many stock counts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Stock counts, in the capability's menu (D495).
- **Workspaces:** 6 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "stock counts" offers this view.
- **AI assistant:** "show the stock counts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Stock counts    Purchasing and stock › Stock counts   [+ New]                                                |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| location          | [ ] LOCATION   STATE                                                                     |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Location | location | text | yes |
| State | state | badge: ToCount, Counted, ToApprove, Applied | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Location | each value | the visible rows (D488) |
| State | ToCount, Counted, ToApprove, Applied | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Stock counts of a chosen location, or of the locations that match a filter.
- From the other side: the locations that have stock counts, or none.

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

- **Place:** location.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the location and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New stock count | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: no field is editable in a cell.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-07 Stock count](../05-count-trace-and-analyse/s-f07-07-stock-count.md).

The records also show on: [S-F7-11 Stock analytics](../05-count-trace-and-analyse/s-f07-11-stock-analytics.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 stock counts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no stock count the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

On the map layout, Listed also shows the count of rows without a place.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491); the map takes the full width.

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button. The table holds the
same rows as the map.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f07-l11-stock-counts-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l11-stock-counts-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f07-l11-stock-counts-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l11-stock-counts-u02-manager-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f07-l11-stock-counts-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l11-stock-counts-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f07-l11-stock-counts-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l11-stock-counts-u15-warehouse-operator-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f07-l11-stock-counts-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l11-stock-counts-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f07-l11-stock-counts-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l11-stock-counts-u13-owner-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l11-stock-counts-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l11-stock-counts-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l11-stock-counts-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l11-stock-counts-u04-purchasing-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-f07-l11-stock-counts-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f07-l11-stock-counts-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-f07-l11-stock-counts-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f07-l11-stock-counts-u14-field-worker-phone-dark.png) |
| Listed, U42, view All | desktop | ![Listed, U42, view All, light](../../images/lists/s-f07-l11-stock-counts-u42-sales-representative-desktop-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-f07-l11-stock-counts-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view All | phone | ![Listed, U42, view All, light](../../images/lists/s-f07-l11-stock-counts-u42-sales-representative-phone-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-f07-l11-stock-counts-u42-sales-representative-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Stock counts](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md) |
| Flows | [FL-F7-05](../../flows/fl-f07-05-count-trace-and-analyse.md) |

## Open questions

None.

---

⬅️ [S-F7-L10 Lot or serials](s-f07-l10-lot-or-serials.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L12 Landed costs](s-f07-l12-landed-costs.md)
