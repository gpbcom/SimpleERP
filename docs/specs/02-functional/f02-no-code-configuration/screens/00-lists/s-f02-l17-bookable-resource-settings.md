🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L17 Bookable resource settings

# 🗂️ S-F2-L17 Bookable resource settings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | an admin list (D494): settings and technical records |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F2-17 Bookable resource setting](../../data/e-f02-17-bookable-resource-setting.md) the
user may see: to find, filter, total and act on many bookable resource settings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Bookable resource settings, in the Administration menu (D494).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "bookable resource settings" offers this view.
- **AI assistant:** "show the bookable resource settings that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Bookable resource settings    Administration › Bookable resource settings   [+ New]                          |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RECORD TYPE   STATE   RULES   CAPACITY                                               |
| record type       | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Record type | record type | text | yes |
| State | state | badge: Draft, Published, Archived | yes |
| Rules | rules | date and time | yes |
| Capacity | capacity | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Archived | the visible rows (D488) |
| Record type | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Bookable resource settings of a chosen record type, or of the record types that match a filter.
- From the other side: the record types that have bookable resource settings, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by rules.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New bookable resource setting | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- capacity: editable in its cell unless the record's state locks it.
- rules: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F2-18 Booking settings](../08-views-and-bookings/s-f02-18-booking-settings.md).

The records also show on: [S-F2-19 Booking calendar](../08-views-and-bookings/s-f02-19-booking-calendar.md),
[S-F4-19 Room booking](../../../f04-meetings/screens/12-rooms-and-client-video/s-f04-19-room-booking.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 bookable resource settings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no bookable resource setting the user may see yet, with the create action when allowed.
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
| Listed, U28, view Needs attention | desktop | ![Listed, U28, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view Needs attention | phone | ![Listed, U28, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u28-hotel-receptionist-phone-dark.png) |
| Listed, U33, view Open: Draft, Published | desktop | ![Listed, U33, view Open: Draft, Published, light](../../images/lists/s-f02-l17-bookable-resource-settings-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view Open: Draft, Published, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view Open: Draft, Published | phone | ![Listed, U33, view Open: Draft, Published, light](../../images/lists/s-f02-l17-bookable-resource-settings-u33-medical-secretary-phone-light.png) | ![Listed, U33, view Open: Draft, Published, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u33-medical-secretary-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u38-training-coordinator-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u07-administrator-phone-dark.png) |
| Listed, U43, view Needs attention | desktop | ![Listed, U43, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u43-event-producer-desktop-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Needs attention | phone | ![Listed, U43, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u43-event-producer-phone-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u43-event-producer-phone-dark.png) |
| Listed, U09, view Open: Draft, Published | desktop | ![Listed, U09, view Open: Draft, Published, light](../../images/lists/s-f02-l17-bookable-resource-settings-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, Published, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, Published | phone | ![Listed, U09, view Open: Draft, Published, light](../../images/lists/s-f02-l17-bookable-resource-settings-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, Published, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u09-customer-phone-dark.png) |
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u23-store-manager-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f02-l17-bookable-resource-settings-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f02-l17-bookable-resource-settings-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Bookable resource settings](README.md) |
| Workspaces | [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F2-08](../../flows/fl-f02-08-views-and-bookings.md), [FL-F4-12](../../../f04-meetings/flows/fl-f04-12-rooms-and-client-video.md), [FL-SC03-02](../../../../08-sectors/sc03-services/flows/fl-sc03-02-staff-and-plan.md), [FL-SC06-03](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC09-05](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-05-practice-organisation.md), [FL-SC12-01](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-01-offer-and-sessions.md) |

## Open questions

None.

---

⬅️ [S-F2-L16 Visual views](s-f02-l16-visual-views.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L18 Resource bookings](s-f02-l18-resource-bookings.md)
