🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L18 Resource bookings

# 🗂️ S-F2-L18 Resource bookings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U56 Citizen](../../../../01-users/personas/u56-citizen.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F2-18 Resource booking](../../data/e-f02-18-resource-booking.md) the user may see: to
find, filter, total and act on many resource bookings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Resource bookings, in the capability's menu (D495).
- **Workspaces:** 12 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "resource bookings" offers this view.
- **AI assistant:** "show the resource bookings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Resource bookings    No-code configuration › Resource bookings   [+ New]                                     |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RESOURCES   STATUS                                                                   |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Resources | resources | text | yes |
| Status | status | badge | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Requested, Confirmed, Cancelled, Done, NoShow | the visible rows (D488) |
| Status | Requested, Confirmed, Cancelled, Done, NoShow | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: resource bookings link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Requested, Confirmed, NoShow.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New resource booking | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
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
| booked for | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F2-19 Booking calendar](../08-views-and-bookings/s-f02-19-booking-calendar.md).

The records also show on:
[S-F4-19 Room booking](../../../f04-meetings/screens/12-rooms-and-client-video/s-f04-19-room-booking.md),
[S-SC06-08 Bookings](../../../../08-sectors/sc06-hospitality/screens/03-rooms-and-bookings/s-sc06-08-bookings.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 resource bookings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no resource booking the user may see yet, with the create action when allowed.
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
| Listed, U09, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U09, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U09, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u09-customer-phone-light.png) | ![Listed, U09, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u09-customer-phone-dark.png) |
| Listed, U28, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U28, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U28, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u28-hotel-receptionist-phone-dark.png) |
| Listed, U33, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U33, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U33, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u33-medical-secretary-phone-light.png) | ![Listed, U33, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u33-medical-secretary-phone-dark.png) |
| Listed, U38, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U38, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U38, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u38-training-coordinator-phone-dark.png) |
| Listed, U43, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U43, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u43-event-producer-desktop-light.png) | ![Listed, U43, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U43, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u43-event-producer-phone-light.png) | ![Listed, U43, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u43-event-producer-phone-dark.png) |
| Listed, U01, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U01, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u01-employee-desktop-light.png) | ![Listed, U01, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u01-employee-desktop-dark.png) |
| Listed, U01, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U01, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u01-employee-phone-light.png) | ![Listed, U01, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u01-employee-phone-dark.png) |
| Listed, U02, view Open: Requested, Confirmed, NoShow | desktop | ![Listed, U02, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Requested, Confirmed, NoShow | phone | ![Listed, U02, view Open: Requested, Confirmed, NoShow, light](../../images/lists/s-f02-l18-resource-bookings-u02-manager-phone-light.png) | ![Listed, U02, view Open: Requested, Confirmed, NoShow, dark](../../images/lists/s-f02-l18-resource-bookings-u02-manager-phone-dark.png) |
| Listed, U13, view Open | desktop | ![Listed, U13, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u13-owner-desktop-light.png) | ![Listed, U13, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u13-owner-desktop-dark.png) |
| Listed, U13, view Open | phone | ![Listed, U13, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u13-owner-phone-light.png) | ![Listed, U13, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u13-owner-phone-dark.png) |
| Listed, U23, view Open | desktop | ![Listed, U23, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u23-store-manager-desktop-light.png) | ![Listed, U23, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Open | phone | ![Listed, U23, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u23-store-manager-phone-light.png) | ![Listed, U23, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u23-store-manager-phone-dark.png) |
| Listed, U52, view Open | desktop | ![Listed, U52, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u52-beautician-desktop-light.png) | ![Listed, U52, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u52-beautician-desktop-dark.png) |
| Listed, U52, view Open | phone | ![Listed, U52, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u52-beautician-phone-light.png) | ![Listed, U52, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u52-beautician-phone-dark.png) |
| Listed, U53, view Open | desktop | ![Listed, U53, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u53-coach-desktop-light.png) | ![Listed, U53, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u53-coach-desktop-dark.png) |
| Listed, U53, view Open | phone | ![Listed, U53, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u53-coach-phone-light.png) | ![Listed, U53, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u53-coach-phone-dark.png) |
| Listed, U56, view Open | desktop | ![Listed, U56, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u56-citizen-desktop-light.png) | ![Listed, U56, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u56-citizen-desktop-dark.png) |
| Listed, U56, view Open | phone | ![Listed, U56, view Open, light](../../images/lists/s-f02-l18-resource-bookings-u56-citizen-phone-light.png) | ![Listed, U56, view Open, dark](../../images/lists/s-f02-l18-resource-bookings-u56-citizen-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Resource bookings](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md), [U56](../../../../04-ux/views/u56-citizen/workspace.md) |
| Flows | [FL-F2-08](../../flows/fl-f02-08-views-and-bookings.md), [FL-F4-10](../../../f04-meetings/flows/fl-f04-10-benchmark-additions.md), [FL-F4-12](../../../f04-meetings/flows/fl-f04-12-rooms-and-client-video.md), [FL-SC06-03](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC09-01](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-01-appointments.md), [FL-SC12-01](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-01-offer-and-sessions.md), [FL-SC16-01](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-01-plan-and-book.md), [FL-SC16-03](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-03-people-and-partners.md) |

## Open questions

None.

---

⬅️ [S-F2-L17 Bookable resource settings](s-f02-l17-bookable-resource-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L19 Portal exposures](s-f02-l19-portal-exposures.md)
