🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L02 Work centres

# 🗂️ S-F12-L02 Work centres

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | as the permissions row "Bills of materials, routings, work centres": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | as the permissions row "Bills of materials, routings, work centres": read work centres, for costing (UC-F12-12) | actions as [permissions](../../permissions.md) gives them |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | as the permissions row "Bills of materials, routings, work centres": read work centres, to connect machines (UC-F12-14) | actions as [permissions](../../permissions.md) gives them |

**Not embedded for:** U20, U27: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F12-02 Work centre](../../data/e-f12-02-work-centre.md) the user may see: to find,
filter, total and act on many work centres at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Work centres, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "work centres" offers this view.
- **AI assistant:** "show the work centres that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Work centres    Manufacturing (plugin) › Work centres   [+ New]                                              |
| [count] [total cost per hour]   [chart: count by state, cost per hour stacked]                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   EQUIPMENT   COST PER HOUR   SITE                                      |
| site              | [ ] ...                                                  Open >                          |
| equipment         | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | label | yes |
| State | state | badge: Active | yes |
| Equipment | equipment | text | yes |
| Cost per hour | cost per hour | amount, right-aligned | yes |
| Site | site | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Site | text, site | the visible rows (D488) |
| Equipment | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Work centres of a chosen equipment, or of the equipments that match a filter.
- From the other side: the equipments that have work centres, or none.

## KPI strip

- Count of the visible rows.
- Total of cost per hour.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, cost per hour stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** site.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New work centre | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F12-02 Routing](../01-define-the-products/s-f12-02-routing.md).

The records also show on:
[S-F12-12 Production cost variance](../05-subcontracting-and-costs/s-f12-12-production-cost-variance.md),
[S-F12-14 Machine connections](../06-machines-and-oee/s-f12-14-machine-connections.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 work centres of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no work centre the user may see yet, with the create action when allowed.
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
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f12-l02-work-centres-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l02-work-centres-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f12-l02-work-centres-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l02-work-centres-u21-production-planner-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f12-l02-work-centres-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f12-l02-work-centres-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f12-l02-work-centres-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f12-l02-work-centres-u05-accounting-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f12-l02-work-centres-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f12-l02-work-centres-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f12-l02-work-centres-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f12-l02-work-centres-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Work centres](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F12-01](../../flows/fl-f12-01-define-the-products.md), [FL-F12-05](../../flows/fl-f12-05-subcontracting-and-costs.md), [FL-F12-06](../../flows/fl-f12-06-machines-and-oee.md), [FL-F12-10](../../flows/fl-f12-10-people-and-tools.md), [FL-F12-11](../../flows/fl-f12-11-finite-schedule-and-the-tablet.md) |

## Open questions

None.

---

⬅️ [S-F12-L01 Bill of materials](s-f12-l01-bill-of-materials.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L03 Routing operations](s-f12-l03-routing-operations.md)
