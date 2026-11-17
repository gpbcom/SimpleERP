🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Agriculture and food menu](README.md) › 🗂️ S-SC13-L01 Plots

# 🗂️ S-SC13-L01 Plots

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC13-01 Plot](../../data/e-sc13-01-plot.md) the user may see: to find, filter, total and
act on many plots at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Agriculture and food › Plots, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "plots" offers this view.
- **AI assistant:** "show the plots that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Plots    Agriculture and food › Plots   [+ New]                                                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   LOCATION                                                              |
| location          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | link to the record | yes |
| State | state | badge: New, Refused | yes |
| Location | location | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | New, Refused | the visible rows (D488) |
| Location | each linked location | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Plots of a chosen location, or of the locations that match a filter.
- From the other side: the locations that have plots, or none.

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

- **Place:** area, location.
- **Layout:** a plan, [C-18](../../../../04-ux/design-system/components/c-18-plan.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New plot | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC13-01 Plots](../01-crops/s-sc13-01-plots.md).

The records also show on: [S-SC13-07 Aid declaration](../03-farm-business/s-sc13-07-aid-declaration.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 plots of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no plot the user may see yet, with the create action when allowed.
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
| Listed, U40, view All | desktop | ![Listed, U40, view All, light](../../images/lists/s-sc13-l01-plots-u40-farmer-desktop-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-sc13-l01-plots-u40-farmer-desktop-dark.png) |
| Listed, U40, view All | phone | ![Listed, U40, view All, light](../../images/lists/s-sc13-l01-plots-u40-farmer-phone-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-sc13-l01-plots-u40-farmer-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-sc13-l01-plots-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc13-l01-plots-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-sc13-l01-plots-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc13-l01-plots-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-18 Plan](../../../../04-ux/design-system/components/c-18-plan.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Agriculture and food › Plots](README.md) |
| Workspaces | [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-SC13-01](../../flows/fl-sc13-01-crops.md), [FL-SC13-03](../../flows/fl-sc13-03-farm-business.md), [FL-SC13-05](../../flows/fl-sc13-05-food-processing.md) |

## Open questions

None.

---

⬅️ [S-SC13-25 Forestry](../06-vineyards-contractors-and-cooperatives/s-sc13-25-forestry.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-L02 Crop plans](s-sc13-l02-crop-plans.md)
