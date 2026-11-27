🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Social media and marketing menu](README.md) › 🗂️ S-F5-L11 Ticket type and seat maps

# 🗂️ S-F5-L11 Ticket type and seat maps

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F5-11 Ticket type and seat map](../../data/e-f05-11-ticket-type-and-seat-map.md) the
user may see: to find, filter, total and act on many ticket type and seat maps at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Social media and marketing › Ticket type and seat maps, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "ticket type and seat maps" offers this view.
- **AI assistant:** "show the ticket type and seat maps that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Ticket type and seat maps    Social media and marketing › Ticket type and seat maps   [+ New]                |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EVENT   STATE   SESSIONS                                                             |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Event | event | text | yes |
| State | state | badge: Draft, Closed | yes |
| Sessions | sessions | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: ticket type and seat maps link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by sessions.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New ticket type and seat map | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- sessions: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F5-17 Ticketing setup](../07-events-and-ticketing/s-f05-17-ticketing-setup.md).

The records also show on: [S-F5-11 Event](../07-events-and-ticketing/s-f05-11-event.md),
[S-F10-02 Till](../../../f10-point-of-sale/screens/02-sell-at-the-counter/s-f10-02-till.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 ticket type and seat maps of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no ticket type and seat map the user may see yet, with the create action when allowed.
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
| Listed, U43, view Needs attention | desktop | ![Listed, U43, view Needs attention, light](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u43-event-producer-desktop-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Needs attention | phone | ![Listed, U43, view Needs attention, light](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u43-event-producer-phone-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u43-event-producer-phone-dark.png) |
| Listed, U12, view Open: Draft | desktop | ![Listed, U12, view Open: Draft, light](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u12-marketing-desktop-light.png) | ![Listed, U12, view Open: Draft, dark](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u12-marketing-desktop-dark.png) |
| Listed, U12, view Open: Draft | phone | ![Listed, U12, view Open: Draft, light](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u12-marketing-phone-light.png) | ![Listed, U12, view Open: Draft, dark](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u12-marketing-phone-dark.png) |
| Listed, U44, view Open: Draft | desktop | ![Listed, U44, view Open: Draft, light](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u44-box-office-agent-desktop-light.png) | ![Listed, U44, view Open: Draft, dark](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u44-box-office-agent-desktop-dark.png) |
| Listed, U44, view Open: Draft | phone | ![Listed, U44, view Open: Draft, light](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u44-box-office-agent-phone-light.png) | ![Listed, U44, view Open: Draft, dark](../../images/lists/s-f05-l11-ticket-type-and-seat-maps-u44-box-office-agent-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Social media and marketing › Ticket type and seat maps](README.md) |
| Workspaces | [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U44](../../../../04-ux/views/u44-box-office-agent/workspace.md) |
| Flows | [FL-F5-07](../../flows/fl-f05-07-events-and-ticketing.md), [FL-SC16-02](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-02-ticketing.md) |

## Open questions

None.

---

⬅️ [S-F5-L10 Consent and suppression records](s-f05-l10-consent-and-suppression-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-L12 Event tickets](s-f05-l12-event-tickets.md)
