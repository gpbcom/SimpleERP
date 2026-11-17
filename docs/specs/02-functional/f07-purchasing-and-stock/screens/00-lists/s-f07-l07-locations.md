🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L07 Locations

# 🗂️ S-F7-L07 Locations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U14, U23: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F7-07 Location](../../data/e-f07-07-location.md) the user may see: to find, filter,
total and act on many locations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Locations, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "locations" offers this view.
- **AI assistant:** "show the locations that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Locations    Purchasing and stock › Locations   [+ New]                                                      |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] WAREHOUSE   STATE   STORAGE CATEGORY                                                 |
| storage category  | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Warehouse | warehouse | text | yes |
| State | state | badge: Active | yes |
| Storage category | storage category | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Storage category | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: locations link to no other record type in their fields.

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

- **Place:** warehouse.
- **Layout:** a plan, [C-18](../../../../04-ux/design-system/components/c-18-plan.md).
- **Marker:** the warehouse and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New location | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- storage category: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-03 Receipt](../02-receive-and-store/s-f07-03-receipt.md).

The records also show on: [S-F7-06 Pick, pack and ship](../04-pick-pack-and-ship/s-f07-06-pick-pack-and-ship.md),
[S-F7-07 Stock count](../05-count-trace-and-analyse/s-f07-07-stock-count.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 locations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no location the user may see yet, with the create action when allowed.
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
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f07-l07-locations-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l07-locations-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f07-l07-locations-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l07-locations-u15-warehouse-operator-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f07-l07-locations-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l07-locations-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f07-l07-locations-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l07-locations-u02-manager-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f07-l07-locations-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f07-l07-locations-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f07-l07-locations-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f07-l07-locations-u07-administrator-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l07-locations-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l07-locations-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l07-locations-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l07-locations-u04-purchasing-phone-dark.png) |
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-f07-l07-locations-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l07-locations-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-f07-l07-locations-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l07-locations-u27-quality-manager-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-f07-l07-locations-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f07-l07-locations-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-f07-l07-locations-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f07-l07-locations-u20-production-operator-phone-dark.png) |
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f07-l07-locations-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f07-l07-locations-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f07-l07-locations-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f07-l07-locations-u21-production-planner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-18 Plan](../../../../04-ux/design-system/components/c-18-plan.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Locations](README.md) |
| Workspaces | [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md) |
| Flows | [FL-F11-10](../../../f11-online-shop/flows/fl-f11-10-fulfil-from-stores-and-report.md), [FL-F7-02](../../flows/fl-f07-02-receive-and-store.md), [FL-F7-03](../../flows/fl-f07-03-replenish.md), [FL-F7-04](../../flows/fl-f07-04-pick-pack-and-ship.md), [FL-F7-05](../../flows/fl-f07-05-count-trace-and-analyse.md), [FL-F7-09](../../flows/fl-f07-09-compliance-and-carbon.md), [FL-SC02-02](../../../../08-sectors/sc02-retail/flows/fl-sc02-02-keep-stock-right.md), [FL-SC07-06](../../../../08-sectors/sc07-transport/flows/fl-sc07-06-logistics-for-clients.md) |

## Open questions

None.

---

⬅️ [S-F7-L06 Items](s-f07-l06-items.md) · ⬆️ [Up](README.md) · ➡️ [S-F7-L08 Routes](s-f07-l08-routes.md)
