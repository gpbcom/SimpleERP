🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L28 Assignment proposals

# 🗂️ S-F9-L28 Assignment proposals

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-28 Assignment proposal](../../data/e-f09-28-assignment-proposal.md) the user may see:
to find, filter, total and act on many assignment proposals at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Assignment proposals, in the capability's menu (D495).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "assignment proposals" offers this view.
- **AI assistant:** "show the assignment proposals that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Assignment proposals    HR and projects › Assignment proposals   [+ New]                                     |
| [count] [Waiting] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| work request      | [ ] WORK REQUEST   STATE   CHOSEN   NOTIFIED   ROUTE   COMPUTED AT   PROBLEM             |
| chosen            | [ ] ...                                                  Open >                          |
| route             | [ ] ...                                                  Open >                          |
| problem           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Work request | work request | link to the record | yes |
| State | state | badge: Waiting, NoCandidate, Applied, Stopped, Confirmed, Overridden, Superseded | yes |
| Chosen | chosen | person's name | yes |
| Notified | notified | person's name | yes |
| Route | route | link to the record | yes |
| Computed at | computed at | date and time | yes |
| Problem | problem | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Work request | each linked work request | the visible rows (D488) |
| Chosen | each person, the user first | the visible rows (D488) |
| Route | each linked route | the visible rows (D488) |
| Problem | each value | the visible rows (D488) |
| State | Waiting, NoCandidate, Applied, Stopped, Confirmed, Overridden, Superseded | the visible rows (D488) |
| Notified | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Assignment proposals of a chosen route, or of the routes that match a filter.
- From the other side: the routes that have assignment proposals, or none.
- Assignment proposals of a chosen work request, or of the work requests that match a filter.
- From the other side: the work requests that have assignment proposals, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Waiting.
- New this month, by computed at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: chosen.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** route.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the work request and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New assignment proposal | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the chosen; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- computed at: editable in its cell unless the record's state locks it.
- problem: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| candidates | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| excluded | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| chosen | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| decided by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| override reason | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| notified | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-27 Rounds](../11-capacity-rounds-and-partners/s-f09-27-rounds.md).

The records also show on: [S-F9-30 Scheduling board](../12-schedule-customer-requests/s-f09-30-scheduling-board.md),
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 assignment proposals of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no assignment proposal the user may see yet, with the create action when allowed.
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
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u29-dispatcher-phone-dark.png) |
| Listed, U26, view Mine: chosen | desktop | ![Listed, U26, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: chosen | phone | ![Listed, U26, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u26-carer-phone-light.png) | ![Listed, U26, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: chosen | desktop | ![Listed, U30, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: chosen | phone | ![Listed, U30, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u30-driver-phone-light.png) | ![Listed, U30, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u30-driver-phone-dark.png) |
| Listed, U14, view Mine: chosen | desktop | ![Listed, U14, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: chosen | phone | ![Listed, U14, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u14-field-worker-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u02-manager-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f09-l28-assignment-proposals-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f09-l28-assignment-proposals-u07-administrator-phone-dark.png) |
| Listed, U09, view Mine: chosen | desktop | ![Listed, U09, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: chosen | phone | ![Listed, U09, view Mine: chosen, light](../../images/lists/s-f09-l28-assignment-proposals-u09-customer-phone-light.png) | ![Listed, U09, view Mine: chosen, dark](../../images/lists/s-f09-l28-assignment-proposals-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Assignment proposals](README.md) |
| Workspaces | [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../flows/fl-f09-13-keep-qualifications.md) |

## Open questions

None.

---

⬅️ [S-F9-L27 Subcontractor assignments](s-f09-l27-subcontractor-assignments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L29 Degrees](s-f09-l29-degrees.md)
