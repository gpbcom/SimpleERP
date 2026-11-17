🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Restaurant and hospitality menu](README.md) › 🗂️ S-SC06-L06 Hotel rooms

# 🗂️ S-SC06-L06 Hotel rooms

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U13: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC06-06 Hotel room](../../data/e-sc06-06-hotel-room.md) the user may see: to find,
filter, total and act on many hotel rooms at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Restaurant and hospitality › Hotel rooms, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "hotel rooms" offers this view.
- **AI assistant:** "show the hotel rooms that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Hotel rooms    Restaurant and hospitality › Hotel rooms   [+ New]                                            |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NUMBER   STATUS   TYPE                                                               |
| type              | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| Status | status | badge | yes |
| Type | type | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Dirty, Clean, Inspected, OutOfOrder | the visible rows (D488) |
| Type | each value | the visible rows (D488) |
| Status | Dirty, Clean, Inspected, OutOfOrder | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: hotel rooms link to no other record type in their fields.

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
| New hotel room | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- type: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC06-07 Rooms and rates](../03-rooms-and-bookings/s-sc06-07-rooms-and-rates.md).

The records also show on: [S-SC06-10 Housekeeping](../04-stay-and-folio/s-sc06-10-housekeeping.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 hotel rooms of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no hotel room the user may see yet, with the create action when allowed.
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
| Listed, U28, view All | desktop | ![Listed, U28, view All, light](../../images/lists/s-sc06-l06-hotel-rooms-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view All, dark](../../images/lists/s-sc06-l06-hotel-rooms-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view All | phone | ![Listed, U28, view All, light](../../images/lists/s-sc06-l06-hotel-rooms-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view All, dark](../../images/lists/s-sc06-l06-hotel-rooms-u28-hotel-receptionist-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-sc06-l06-hotel-rooms-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc06-l06-hotel-rooms-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-sc06-l06-hotel-rooms-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc06-l06-hotel-rooms-u23-store-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Restaurant and hospitality › Hotel rooms](README.md) |
| Workspaces | [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md) |
| Flows | [FL-SC06-03](../../flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC06-04](../../flows/fl-sc06-04-stay-and-folio.md) |

## Open questions

None.

---

⬅️ [S-SC06-L05 Staff benefits](s-sc06-l05-staff-benefits.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-L07 Rate plans](s-sc06-l07-rate-plans.md)
