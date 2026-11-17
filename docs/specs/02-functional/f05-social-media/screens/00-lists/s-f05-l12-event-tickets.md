🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Social media and marketing menu](README.md) › 🗂️ S-F5-L12 Event tickets

# 🗂️ S-F5-L12 Event tickets

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F5-12 Event ticket](../../data/e-f05-12-event-ticket.md) the user may see: to find,
filter, total and act on many event tickets at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Social media and marketing › Event tickets, in the capability's menu (D495).
- **Workspaces:** 6 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "event tickets" offers this view.
- **AI assistant:** "show the event tickets that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Event tickets    Social media and marketing › Event tickets   [+ New]                                        |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CODE   STATE   HOLDER   SCANNED AT   CHANNEL                                         |
| holder            | [ ] ...                                                  Open >                          |
| channel           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Code | code | text | yes |
| State | state | badge: Sold, Scanned, Refunded | yes |
| Holder | holder | person's name | yes |
| Scanned at | scanned at | date and time | yes |
| Channel | channel | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Sold, Scanned, Refunded | the visible rows (D488) |
| Holder | each person, the user first | the visible rows (D488) |
| Channel | online, box office, partner | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: event tickets link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by scanned at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: holder.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New event ticket | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the holder; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- channel: editable in its cell unless the record's state locks it.
- scanned at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| holder | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F5-18 Ticket scan](../07-events-and-ticketing/s-f05-18-ticket-scan.md).

The records also show on:
[S-SC08-12 Events](../../../../08-sectors/sc08-non-profit/screens/05-events/s-sc08-12-events.md),
[S-F10-02 Till](../../../f10-point-of-sale/screens/02-sell-at-the-counter/s-f10-02-till.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 event tickets of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no event ticket the user may see yet, with the create action when allowed.
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
| Listed, U44, view Mine: holder | desktop | ![Listed, U44, view Mine: holder, light](../../images/lists/s-f05-l12-event-tickets-u44-box-office-agent-desktop-light.png) | ![Listed, U44, view Mine: holder, dark](../../images/lists/s-f05-l12-event-tickets-u44-box-office-agent-desktop-dark.png) |
| Listed, U44, view Mine: holder | phone | ![Listed, U44, view Mine: holder, light](../../images/lists/s-f05-l12-event-tickets-u44-box-office-agent-phone-light.png) | ![Listed, U44, view Mine: holder, dark](../../images/lists/s-f05-l12-event-tickets-u44-box-office-agent-phone-dark.png) |
| Listed, U09, view Mine: holder | desktop | ![Listed, U09, view Mine: holder, light](../../images/lists/s-f05-l12-event-tickets-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: holder, dark](../../images/lists/s-f05-l12-event-tickets-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: holder | phone | ![Listed, U09, view Mine: holder, light](../../images/lists/s-f05-l12-event-tickets-u09-customer-phone-light.png) | ![Listed, U09, view Mine: holder, dark](../../images/lists/s-f05-l12-event-tickets-u09-customer-phone-dark.png) |
| Listed, U43, view All | desktop | ![Listed, U43, view All, light](../../images/lists/s-f05-l12-event-tickets-u43-event-producer-desktop-light.png) | ![Listed, U43, view All, dark](../../images/lists/s-f05-l12-event-tickets-u43-event-producer-desktop-dark.png) |
| Listed, U43, view All | phone | ![Listed, U43, view All, light](../../images/lists/s-f05-l12-event-tickets-u43-event-producer-phone-light.png) | ![Listed, U43, view All, dark](../../images/lists/s-f05-l12-event-tickets-u43-event-producer-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f05-l12-event-tickets-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f05-l12-event-tickets-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f05-l12-event-tickets-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f05-l12-event-tickets-u13-owner-phone-dark.png) |
| Listed, U32, view Mine: holder | desktop | ![Listed, U32, view Mine: holder, light](../../images/lists/s-f05-l12-event-tickets-u32-volunteer-desktop-light.png) | ![Listed, U32, view Mine: holder, dark](../../images/lists/s-f05-l12-event-tickets-u32-volunteer-desktop-dark.png) |
| Listed, U32, view Mine: holder | phone | ![Listed, U32, view Mine: holder, light](../../images/lists/s-f05-l12-event-tickets-u32-volunteer-phone-light.png) | ![Listed, U32, view Mine: holder, dark](../../images/lists/s-f05-l12-event-tickets-u32-volunteer-phone-dark.png) |
| Listed, U53, view Mine | desktop | ![Listed, U53, view Mine, light](../../images/lists/s-f05-l12-event-tickets-u53-coach-desktop-light.png) | ![Listed, U53, view Mine, dark](../../images/lists/s-f05-l12-event-tickets-u53-coach-desktop-dark.png) |
| Listed, U53, view Mine | phone | ![Listed, U53, view Mine, light](../../images/lists/s-f05-l12-event-tickets-u53-coach-phone-light.png) | ![Listed, U53, view Mine, dark](../../images/lists/s-f05-l12-event-tickets-u53-coach-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Social media and marketing › Event tickets](README.md) |
| Workspaces | [U44](../../../../04-ux/views/u44-box-office-agent/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U32](../../../../04-ux/views/u32-volunteer/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md) |
| Flows | [FL-F5-07](../../flows/fl-f05-07-events-and-ticketing.md), [FL-SC08-05](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-05-events.md), [FL-SC16-02](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-02-ticketing.md) |

## Open questions

None.

---

⬅️ [S-F5-L11 Ticket type and seat maps](s-f05-l11-ticket-type-and-seat-maps.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-L13 Landing page and forms](s-f05-l13-landing-page-and-forms.md)
