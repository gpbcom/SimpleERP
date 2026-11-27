🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customer support agents menu](README.md) › 🗂️ S-F16-L12 Work requests

# 🗂️ S-F16-L12 Work requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F16-12 Work request](../../data/e-f16-12-work-request.md) the user may see: to find,
filter, total and act on many work requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customer support agents › Work requests, in the capability's menu (D495).
- **Workspaces:** 9 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "work requests" offers this view.
- **AI assistant:** "show the work requests that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Work requests    Customer support agents › Work requests   [+ New]                                           |
| [count] [Drafted]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| channel           | [ ] NUMBER   STATE   CONFIRMED BY   CUSTOMER   REQUEST TYPE   CHANNEL   ATTRIBUTE CHANGE |
| customer          | [ ] ...                                                  Open >                          |
| request type      | [ ] ...                                                  Open >                          |
| attribute changes | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| State | state | badge: Drafted, ToConfirm, Ready, Proposed, Blocked, Scheduled, InProgress, Done, Cancelled | yes |
| Confirmed by | confirmed by | person's name | yes |
| Customer | customer | text | yes |
| Request type | request type | link to the record | yes |
| Channel | channel | text | yes |
| Attribute changes | attribute changes | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Channel | each value | the visible rows (D488) |
| Customer | each value | the visible rows (D488) |
| Request type | each linked request type | the visible rows (D488) |
| Attribute changes | each value | the visible rows (D488) |
| Confirmed by | each person, the user first | the visible rows (D488) |
| State | Drafted, ToConfirm, Ready, Proposed, Blocked, Scheduled, InProgress, Done, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Work requests of a chosen customer, or of the customers that match a filter.
- From the other side: the customers that have work requests, or none.
- Work requests of a chosen request type, or of the request types that match a filter.
- From the other side: the request types that have work requests, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Drafted.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: confirmed by.
- Open: Drafted, ToConfirm, Ready.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** place.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the number and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New work request | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the confirmed by; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- channel: editable in its cell unless the record's state locks it.
- attribute changes: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| customer | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| place | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| needs | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| source | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| confirmed by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| assigned to | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| cancel reason | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F16-11 My requests](../05-customer-side/s-f16-11-my-requests.md).

The records also show on: [S-F16-14 Work requests](../06-take-in-every-request/s-f16-14-work-requests.md),
[S-F16-15 Arrival of your visit](../06-take-in-every-request/s-f16-15-arrival-of-your-visit.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 work requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no work request the user may see yet, with the create action when allowed.
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
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u29-dispatcher-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u25-care-coordinator-phone-dark.png) |
| Listed, U09, view Mine: confirmed by | desktop | ![Listed, U09, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: confirmed by | phone | ![Listed, U09, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u09-customer-phone-light.png) | ![Listed, U09, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u09-customer-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u02-manager-phone-dark.png) |
| Listed, U26, view Mine: confirmed by | desktop | ![Listed, U26, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: confirmed by | phone | ![Listed, U26, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u26-carer-phone-light.png) | ![Listed, U26, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: confirmed by | desktop | ![Listed, U30, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: confirmed by | phone | ![Listed, U30, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u30-driver-phone-light.png) | ![Listed, U30, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u30-driver-phone-dark.png) |
| Listed, U16, view Mine: confirmed by | desktop | ![Listed, U16, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u16-office-worker-desktop-light.png) | ![Listed, U16, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Mine: confirmed by | phone | ![Listed, U16, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u16-office-worker-phone-light.png) | ![Listed, U16, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u16-office-worker-phone-dark.png) |
| Listed, U14, view Mine: confirmed by | desktop | ![Listed, U14, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: confirmed by | phone | ![Listed, U14, view Mine: confirmed by, light](../../images/lists/s-f16-l12-work-requests-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: confirmed by, dark](../../images/lists/s-f16-l12-work-requests-u14-field-worker-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f16-l12-work-requests-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f16-l12-work-requests-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customer support agents › Work requests](README.md) |
| Workspaces | [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F16-06](../../flows/fl-f16-06-take-in-every-request.md), [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F9-12](../../../f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../../f09-hr-and-projects/flows/fl-f09-13-keep-qualifications.md) |

## Open questions

None.

---

⬅️ [S-F16-L11 Fraud signals](s-f16-l11-fraud-signals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-L13 Forum posts](s-f16-l13-forum-posts.md)
