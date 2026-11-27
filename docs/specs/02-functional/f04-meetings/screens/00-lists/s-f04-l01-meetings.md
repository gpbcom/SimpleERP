🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Meetings menu](README.md) › 🗂️ S-F4-L01 Meetings

# 🗂️ S-F4-L01 Meetings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F4-01 Meeting](../../data/e-f04-01-meeting.md) the user may see: to find, filter, total
and act on many meetings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Meetings › Meetings, in the capability's menu (D495).
- **Workspaces:** 10 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "meetings" offers this view.
- **AI assistant:** "show the meetings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Meetings    Meetings › Meetings   [+ New]                                                                    |
| [count] [WaitingForReview] [new this month]   [chart: count by state]                                        |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   STATUS   STARTS   KIND                                                       |
| kind              | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| Status | status | badge | yes |
| Starts | starts | date and time | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Planned, Live, Ended, WaitingForReview, Checked | the visible rows (D488) |
| Kind | ordinary, HR | the visible rows (D488) |
| Status | Planned, Live, Ended, WaitingForReview, Checked | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: meetings link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state WaitingForReview.
- New this month, by starts.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Planned, Live, WaitingForReview.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New meeting | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- starts: editable in its cell unless the record's state locks it.
- kind: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| participants | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F4-01 Meeting](../01-record-an-online-meeting/s-f04-01-meeting.md).

The records also show on: [S-F4-02 Live transcript](../01-record-an-online-meeting/s-f04-02-live-transcript.md),
[S-F2-19 Booking calendar](../../../f02-no-code-configuration/screens/08-views-and-bookings/s-f02-19-booking-calendar.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 meetings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no meeting the user may see yet, with the create action when allowed.
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
| Listed, U03, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U03, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U03, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u03-sales-phone-light.png) | ![Listed, U03, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u03-sales-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f04-l01-meetings-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f04-l01-meetings-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f04-l01-meetings-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f04-l01-meetings-u02-manager-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f04-l01-meetings-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f04-l01-meetings-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f04-l01-meetings-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f04-l01-meetings-u13-owner-phone-dark.png) |
| Listed, U14, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U14, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U14, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u14-field-worker-phone-light.png) | ![Listed, U14, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u14-field-worker-phone-dark.png) |
| Listed, U01, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U01, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u01-employee-desktop-light.png) | ![Listed, U01, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u01-employee-desktop-dark.png) |
| Listed, U01, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U01, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u01-employee-phone-light.png) | ![Listed, U01, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u01-employee-phone-dark.png) |
| Listed, U09, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U09, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U09, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u09-customer-phone-light.png) | ![Listed, U09, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u09-customer-phone-dark.png) |
| Listed, U04, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U04, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u04-purchasing-desktop-light.png) | ![Listed, U04, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U04, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u04-purchasing-phone-light.png) | ![Listed, U04, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u04-purchasing-phone-dark.png) |
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f04-l01-meetings-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f04-l01-meetings-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f04-l01-meetings-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f04-l01-meetings-u06-hr-phone-dark.png) |
| Listed, U36, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U36, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u36-professional-desktop-light.png) | ![Listed, U36, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u36-professional-desktop-dark.png) |
| Listed, U36, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U36, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u36-professional-phone-light.png) | ![Listed, U36, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u36-professional-phone-dark.png) |
| Listed, U33, view Open: Planned, Live, WaitingForReview | desktop | ![Listed, U33, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view Open: Planned, Live, WaitingForReview | phone | ![Listed, U33, view Open: Planned, Live, WaitingForReview, light](../../images/lists/s-f04-l01-meetings-u33-medical-secretary-phone-light.png) | ![Listed, U33, view Open: Planned, Live, WaitingForReview, dark](../../images/lists/s-f04-l01-meetings-u33-medical-secretary-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Meetings › Meetings](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md) |
| Flows | [FL-F17-07](../../../f17-competitive-analysis/flows/fl-f17-07-sales-enablement.md), [FL-F24-02](../../../f24-integrations-hub/flows/fl-f24-02-office-suites.md), [FL-F4-01](../../flows/fl-f04-01-record-an-online-meeting.md), [FL-F4-02](../../flows/fl-f04-02-record-in-person-or-by-phone.md), [FL-F4-03](../../flows/fl-f04-03-review-a-meeting.md), [FL-F4-04](../../flows/fl-f04-04-find-and-reuse-meetings.md), [FL-F4-05](../../flows/fl-f04-05-hr-meeting.md), [FL-F4-07](../../flows/fl-f04-07-prepare-and-capture-anywhere.md), [FL-F4-08](../../flows/fl-f04-08-share-and-reuse-outside.md), [FL-F4-09](../../flows/fl-f04-09-score-calls-and-interviews.md), [FL-F4-10](../../flows/fl-f04-10-benchmark-additions.md), [FL-F4-11](../../flows/fl-f04-11-insights-and-accessibility.md), [FL-F4-12](../../flows/fl-f04-12-rooms-and-client-video.md), [FL-F4-13](../../flows/fl-f04-13-outside-people-and-follow-up.md), [FL-F6-06](../../../f06-customers-and-sales/flows/fl-f06-06-accounts-and-credit.md), [FL-F9-02](../../../f09-hr-and-projects/flows/fl-f09-02-recruit.md), [FL-F9-10](../../../f09-hr-and-projects/flows/fl-f09-10-listen-to-employees.md) |

## Open questions

None.

---

⬅️ [S-F4-28 Meeting time analytics](../14-video-messages-and-webinars/s-f04-28-meeting-time-analytics.md) ·
⬆️ [Up](README.md) · ➡️ [S-F4-L02 Transcripts](s-f04-l02-transcripts.md)
