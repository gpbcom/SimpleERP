🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Public bodies menu](README.md) › 🗂️ S-SC20-L09 Hall bookings

# 🗂️ S-SC20-L09 Hall bookings

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U56 Citizen](../../../../01-users/personas/u56-citizen.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC20-09 Hall booking](../../data/e-sc20-09-hall-booking.md) the user may see: to find,
filter, total and act on many hall bookings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Public bodies › Hall bookings, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "hall bookings" offers this view.
- **AI assistant:** "show the hall bookings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Hall bookings    Public bodies > Hall bookings   [+ New]                                                     |
| [count] [Requested] [new this month]   [chart: count by state]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| resource          | [ ] RESOURCE   DATE   BOOKER   RATE   DEPOSIT   STATE                                    |
| class             | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Resource | resource | text | yes |
| Date | date | date | yes |
| Booker | booker | text | yes |
| Rate | rate | amount with currency | yes |
| Deposit | deposit | amount with currency | yes |
| State | state | badge: Requested, Confirmed, Used, Closed, Cancelled | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Resource | each value | the visible rows (D488) |
| Class | each value | the visible rows (D488) |
| State | Requested, Confirmed, Used, Closed, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Resource bookings.
- From the other side: bookings Requested with no deposit after seven days.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Requested.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New hall booking | header | the personas whose roles may create it | the record's own page (Row opens) |
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

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC20-10 Hall booking](../03-citizen-services/s-sc20-10-hall-booking.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 hall bookings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no hall booking the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Not drawn yet: step S8 draws them from this page, one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U56, view All | phone | ![Listed, U56, view All, light](../../images/lists/s-sc20-l09-hall-bookings-u56-citizen-phone-light.png) | ![Listed, U56, view All, dark](../../images/lists/s-sc20-l09-hall-bookings-u56-citizen-phone-dark.png) |
| Listed, U56, view All | desktop | ![Listed, U56, view All, light](../../images/lists/s-sc20-l09-hall-bookings-u56-citizen-desktop-light.png) | ![Listed, U56, view All, dark](../../images/lists/s-sc20-l09-hall-bookings-u56-citizen-desktop-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Public bodies › Hall bookings](README.md) |
| Flows | [FL-SC20-03](../../flows/fl-sc20-03-citizen-services.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-SC20-L08 Citizen requests](s-sc20-l08-citizen-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-L10 Council decisions](s-sc20-l10-council-decisions.md)
