🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Transport and logistics menu](README.md) › 🗂️ S-SC07-L02 Trips

# 🗂️ S-SC07-L02 Trips

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC07-02 Trip](../../data/e-sc07-02-trip.md) the user may see: to find, filter, total and
act on many trips at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Transport and logistics › Trips, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "trips" offers this view.
- **AI assistant:** "show the trips that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Trips    Transport and logistics › Trips   [+ New]                                                           |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] VEHICLE   STATE   DRIVER   DATE   STOPS                                              |
| driver            | [ ] ...                                                  Open >                          |
| stops             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Vehicle | vehicle | link to the record | yes |
| State | state | badge: Planned, Sent, Assigned | yes |
| Driver | driver | link to the record | yes |
| Date | date | link to the record | yes |
| Stops | stops | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Planned, Sent, Assigned | the visible rows (D488) |
| Driver | each linked driver | the visible rows (D488) |
| Stops | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: trips link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: driver.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New trip | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the driver; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- driver: editable in its cell unless the record's state locks it.
- date: editable in its cell unless the record's state locks it.
- stops: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC07-02 Trip planning](../01-orders-and-planning/s-sc07-02-trip-planning.md).

The records also show on: [S-SC07-19 International trips](../04-compliance/s-sc07-19-international-trips.md),
[S-SC07-18 Margins](../05-billing-and-performance/s-sc07-18-margins.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 trips of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no trip the user may see yet, with the create action when allowed.
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
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-sc07-l02-trips-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-sc07-l02-trips-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-sc07-l02-trips-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-sc07-l02-trips-u29-dispatcher-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-sc07-l02-trips-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc07-l02-trips-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-sc07-l02-trips-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc07-l02-trips-u13-owner-phone-dark.png) |
| Listed, U30, view Mine: driver | desktop | ![Listed, U30, view Mine: driver, light](../../images/lists/s-sc07-l02-trips-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: driver, dark](../../images/lists/s-sc07-l02-trips-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: driver | phone | ![Listed, U30, view Mine: driver, light](../../images/lists/s-sc07-l02-trips-u30-driver-phone-light.png) | ![Listed, U30, view Mine: driver, dark](../../images/lists/s-sc07-l02-trips-u30-driver-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Transport and logistics › Trips](README.md) |
| Workspaces | [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md) |
| Flows | [FL-SC07-01](../../flows/fl-sc07-01-orders-and-planning.md), [FL-SC07-03](../../flows/fl-sc07-03-on-the-road.md), [FL-SC07-04](../../flows/fl-sc07-04-compliance.md), [FL-SC07-05](../../flows/fl-sc07-05-billing-and-performance.md) |

## Open questions

None.

---

⬅️ [S-SC07-L01 Transport orders](s-sc07-l01-transport-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-L03 Fleet vehicles](s-sc07-l03-fleet-vehicles.md)
