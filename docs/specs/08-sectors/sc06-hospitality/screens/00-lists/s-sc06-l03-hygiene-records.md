🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Restaurant and hospitality menu](README.md) › 🗂️ S-SC06-L03 Hygiene records

# 🗂️ S-SC06-L03 Hygiene records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC06-03 Hygiene record](../../data/e-sc06-03-hygiene-record.md) the user may see: to
find, filter, total and act on many hygiene records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Restaurant and hospitality › Hygiene records, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "hygiene records" offers this view.
- **AI assistant:** "show the hygiene records that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Hygiene records    Restaurant and hospitality › Hygiene records   [+ New]                                    |
| [count] [total value]   [chart: count by state, value stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] KIND   STATE   VALUE                                                                 |
| kind              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Kind | kind | link to the record | yes |
| State | state | badge: Recorded | yes |
| Value | value | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Kind | each linked kind | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: hygiene records link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of value.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, value stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** place.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the kind and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New hygiene record | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC06-03 Hygiene records](../01-menus-and-food-safety/s-sc06-03-hygiene-records.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 hygiene records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no hygiene record the user may see yet, with the create action when allowed.
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
| Listed, U19, view All | desktop | ![Listed, U19, view All, light](../../images/lists/s-sc06-l03-hygiene-records-u19-kitchen-staff-desktop-light.png) | ![Listed, U19, view All, dark](../../images/lists/s-sc06-l03-hygiene-records-u19-kitchen-staff-desktop-dark.png) |
| Listed, U19, view All | phone | ![Listed, U19, view All, light](../../images/lists/s-sc06-l03-hygiene-records-u19-kitchen-staff-phone-light.png) | ![Listed, U19, view All, dark](../../images/lists/s-sc06-l03-hygiene-records-u19-kitchen-staff-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-sc06-l03-hygiene-records-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc06-l03-hygiene-records-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-sc06-l03-hygiene-records-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc06-l03-hygiene-records-u23-store-manager-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-sc06-l03-hygiene-records-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-sc06-l03-hygiene-records-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-sc06-l03-hygiene-records-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-sc06-l03-hygiene-records-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Restaurant and hospitality › Hygiene records](README.md) |
| Workspaces | [U19](../../../../04-ux/views/u19-kitchen-staff/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-SC06-01](../../flows/fl-sc06-01-menus-and-food-safety.md), [FL-SC13-05](../../../sc13-agriculture-and-food/flows/fl-sc13-05-food-processing.md) |

## Open questions

None.

---

⬅️ [S-SC06-L02 Menu dishes](s-sc06-l02-menu-dishes.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-L04 Waste records](s-sc06-l04-waste-records.md)
