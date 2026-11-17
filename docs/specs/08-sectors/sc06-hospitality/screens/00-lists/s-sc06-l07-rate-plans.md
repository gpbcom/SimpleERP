🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Restaurant and hospitality menu](README.md) › 🗂️ S-SC06-L07 Rate plans

# 🗂️ S-SC06-L07 Rate plans

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC06-07 Rate plan](../../data/e-sc06-07-rate-plan.md) the user may see: to find, filter,
total and act on many rate plans at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Restaurant and hospitality › Rate plans, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "rate plans" offers this view.
- **AI assistant:** "show the rate plans that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Rate plans    Restaurant and hospitality › Rate plans   [+ New]                                              |
| [count] [total price] [new this month]   [chart: count by state, price stacked]                              |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TYPE   STATE   PRICE   DATE                                                          |
| type              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Type | type | link to the record | yes |
| State | state | badge: Active | yes |
| Price | price | amount, right-aligned | yes |
| Date | date | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Type | each linked type | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: rate plans link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New rate plan | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC06-07 Rooms and rates](../03-rooms-and-bookings/s-sc06-07-rooms-and-rates.md).

The records also show on: [S-SC06-14 Performance](../05-taxes-and-performance/s-sc06-14-performance.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 rate plans of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no rate plan the user may see yet, with the create action when allowed.
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
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-sc06-l07-rate-plans-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc06-l07-rate-plans-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-sc06-l07-rate-plans-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc06-l07-rate-plans-u23-store-manager-phone-dark.png) |
| Listed, U28, view All | desktop | ![Listed, U28, view All, light](../../images/lists/s-sc06-l07-rate-plans-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view All, dark](../../images/lists/s-sc06-l07-rate-plans-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view All | phone | ![Listed, U28, view All, light](../../images/lists/s-sc06-l07-rate-plans-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view All, dark](../../images/lists/s-sc06-l07-rate-plans-u28-hotel-receptionist-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-sc06-l07-rate-plans-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc06-l07-rate-plans-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-sc06-l07-rate-plans-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc06-l07-rate-plans-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Restaurant and hospitality › Rate plans](README.md) |
| Workspaces | [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-SC06-03](../../flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC06-05](../../flows/fl-sc06-05-taxes-and-performance.md) |

## Open questions

None.

---

⬅️ [S-SC06-L06 Hotel rooms](s-sc06-l06-hotel-rooms.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-L08 Room reservations](s-sc06-l08-room-reservations.md)
