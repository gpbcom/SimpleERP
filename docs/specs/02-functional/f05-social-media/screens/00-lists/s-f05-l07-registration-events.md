🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Social media and marketing menu](README.md) › 🗂️ S-F5-L07 Registration events

# 🗂️ S-F5-L07 Registration events

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F5-07 Registration event](../../data/e-f05-07-registration-event.md) the user may see:
to find, filter, total and act on many registration events at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Social media and marketing › Registration events, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "registration events" offers this view.
- **AI assistant:** "show the registration events that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Registration events    Social media and marketing › Registration events   [+ New]                            |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Draft, Planned, Published, Approved, Cancelled | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Planned, Published, Approved, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: registration events link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Planned, Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** place.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New registration event | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| attendees | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F5-11 Event](../07-events-and-ticketing/s-f05-11-event.md).

The records also show on: [S-F5-17 Ticketing setup](../07-events-and-ticketing/s-f05-17-ticketing-setup.md),
[S-SC08-12 Events](../../../../08-sectors/sc08-non-profit/screens/05-events/s-sc08-12-events.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 registration events of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no registration event the user may see yet, with the create action when allowed.
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
| Listed, U12, view Open: Draft, Planned, Published | desktop | ![Listed, U12, view Open: Draft, Planned, Published, light](../../images/lists/s-f05-l07-registration-events-u12-marketing-desktop-light.png) | ![Listed, U12, view Open: Draft, Planned, Published, dark](../../images/lists/s-f05-l07-registration-events-u12-marketing-desktop-dark.png) |
| Listed, U12, view Open: Draft, Planned, Published | phone | ![Listed, U12, view Open: Draft, Planned, Published, light](../../images/lists/s-f05-l07-registration-events-u12-marketing-phone-light.png) | ![Listed, U12, view Open: Draft, Planned, Published, dark](../../images/lists/s-f05-l07-registration-events-u12-marketing-phone-dark.png) |
| Listed, U09, view Open: Draft, Planned, Published | desktop | ![Listed, U09, view Open: Draft, Planned, Published, light](../../images/lists/s-f05-l07-registration-events-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, Planned, Published, dark](../../images/lists/s-f05-l07-registration-events-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, Planned, Published | phone | ![Listed, U09, view Open: Draft, Planned, Published, light](../../images/lists/s-f05-l07-registration-events-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, Planned, Published, dark](../../images/lists/s-f05-l07-registration-events-u09-customer-phone-dark.png) |
| Listed, U43, view Needs attention | desktop | ![Listed, U43, view Needs attention, light](../../images/lists/s-f05-l07-registration-events-u43-event-producer-desktop-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f05-l07-registration-events-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Needs attention | phone | ![Listed, U43, view Needs attention, light](../../images/lists/s-f05-l07-registration-events-u43-event-producer-phone-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f05-l07-registration-events-u43-event-producer-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f05-l07-registration-events-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f05-l07-registration-events-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f05-l07-registration-events-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f05-l07-registration-events-u13-owner-phone-dark.png) |
| Listed, U32, view Open: Draft, Planned, Published | desktop | ![Listed, U32, view Open: Draft, Planned, Published, light](../../images/lists/s-f05-l07-registration-events-u32-volunteer-desktop-light.png) | ![Listed, U32, view Open: Draft, Planned, Published, dark](../../images/lists/s-f05-l07-registration-events-u32-volunteer-desktop-dark.png) |
| Listed, U32, view Open: Draft, Planned, Published | phone | ![Listed, U32, view Open: Draft, Planned, Published, light](../../images/lists/s-f05-l07-registration-events-u32-volunteer-phone-light.png) | ![Listed, U32, view Open: Draft, Planned, Published, dark](../../images/lists/s-f05-l07-registration-events-u32-volunteer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Social media and marketing › Registration events](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U32](../../../../04-ux/views/u32-volunteer/workspace.md) |
| Flows | [FL-F5-07](../../flows/fl-f05-07-events-and-ticketing.md), [FL-SC08-05](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-05-events.md), [FL-SC16-01](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-01-plan-and-book.md) |

## Open questions

None.

---

⬅️ [S-F5-L06 Journeys](s-f05-l06-journeys.md) · ⬆️ [Up](README.md) · ➡️ [S-F5-L08 Surveys](s-f05-l08-surveys.md)
