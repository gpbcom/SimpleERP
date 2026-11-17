🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L10 Attendances

# 🗂️ S-F9-L10 Attendances

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-10 Attendance](../../data/e-f09-10-attendance.md) the user may see: to find, filter,
total and act on many attendances at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Attendances, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "attendances" offers this view.
- **AI assistant:** "show the attendances that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Attendances    HR and projects › Attendances   [+ New]                                                       |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATE                                                                     |
| employee          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | person's name | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Employee | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: attendances link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** position.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the employee and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New attendance | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the employee; audited |
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
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| position | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-10 Attendance](../03-time/s-f09-10-attendance.md).

The records also show on: [S-F9-33 Planning map](../12-schedule-customer-requests/s-f09-33-planning-map.md),
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 attendances of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no attendance the user may see yet, with the create action when allowed.
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
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f09-l10-attendances-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l10-attendances-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f09-l10-attendances-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l10-attendances-u02-manager-phone-dark.png) |
| Listed, U01, view Mine: employee | desktop | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l10-attendances-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l10-attendances-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: employee | phone | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l10-attendances-u01-employee-phone-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l10-attendances-u01-employee-phone-dark.png) |
| Listed, U14, view Mine: employee | desktop | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l10-attendances-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l10-attendances-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: employee | phone | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l10-attendances-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l10-attendances-u14-field-worker-phone-dark.png) |
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-f09-l10-attendances-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f09-l10-attendances-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-f09-l10-attendances-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f09-l10-attendances-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-f09-l10-attendances-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f09-l10-attendances-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-f09-l10-attendances-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f09-l10-attendances-u29-dispatcher-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Attendances](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md) |
| Flows | [FL-F9-03](../../flows/fl-f09-03-time.md), [FL-F9-09](../../flows/fl-f09-09-train-and-protect.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md) |

## Open questions

None.

---

⬅️ [S-F9-L09 Time-off requests](s-f09-l09-time-off-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L11 Appraisals](s-f09-l11-appraisals.md)
