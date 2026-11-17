🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L15 Waste register lines

# 🗂️ S-F12-L15 Waste register lines

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F12-15 Waste register line](../../data/e-f12-15-waste-register-line.md) the user may
see: to find, filter, total and act on many waste register lines at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Waste register lines, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "waste register lines" offers this view.
- **AI assistant:** "show the waste register lines that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Waste register lines    Manufacturing (plugin) › Waste register lines   [+ New]                              |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] DATE   STATE   SITE                                                                  |
| site              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Date | date | date | yes |
| State | state | badge: Recorded | yes |
| Site | site | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Site | date, site | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: waste register lines link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** site.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the date and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New waste register line | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- site: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F12-18 Waste register](../07-compliance-and-safety/s-f12-18-waste-register.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 waste register lines of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no waste register line the user may see yet, with the create action when allowed.
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
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f12-l15-waste-register-lines-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l15-waste-register-lines-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f12-l15-waste-register-lines-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l15-waste-register-lines-u21-production-planner-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f12-l15-waste-register-lines-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f12-l15-waste-register-lines-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f12-l15-waste-register-lines-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f12-l15-waste-register-lines-u15-warehouse-operator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Waste register lines](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md) |
| Flows | [FL-F12-07](../../flows/fl-f12-07-compliance-and-safety.md) |

## Open questions

None.

---

⬅️ [S-F12-L14 Product compliance files](s-f12-l14-product-compliance-files.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L16 Calibrations](s-f12-l16-calibrations.md)
