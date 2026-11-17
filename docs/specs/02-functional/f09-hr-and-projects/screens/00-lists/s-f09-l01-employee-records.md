🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L01 Employee records

# 🗂️ S-F9-L01 Employee records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U23, U33, U40: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-F9-01 Employee record](../../data/e-f09-01-employee-record.md) the user may see: to
find, filter, total and act on many employee records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Employee records, in the capability's menu (D495).
- **Workspaces:** 10 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "employee records" offers this view.
- **AI assistant:** "show the employee records that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Employee records    HR and projects › Employee records   [+ New]                                             |
| [count] [total cost rate] [new this month]   [chart: count by state, cost rate stacked]                      |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   MANAGER   DEPARTMENT   RESUME   COST RATE   BIRTH DATE                |
| department        | [ ] ...                                                  Open >                          |
| manager           | [ ] ...                                                  Open >                          |
| resume            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Active | yes |
| Manager | manager | link to the record | yes |
| Department | department | link to the record | yes |
| Resume | resume | text | yes |
| Cost rate | cost rate | amount, right-aligned | yes |
| Birth date | birth date | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Department | each linked department | the visible rows (D488) |
| Manager | each linked manager | the visible rows (D488) |
| Resume | each value | the visible rows (D488) |
| Eligible for (request type, D509 to D511) | each request type or operation with required attributes (D509 to D511); reasons as categories only for planners (BR-F9-29) | the visible rows (D488) |

## Related-record filters

- Employee records of a chosen department, or of the departments that match a filter.
- From the other side: the departments that have employee records, or none.
- Employee records of a chosen resume, or of the resumes that match a filter.
- From the other side: the resumes that have employee records, or none.

## KPI strip

- Count of the visible rows.
- Total of cost rate.
- New this month, by birth date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, cost rate stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Mine: manager.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** address.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New employee record | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the manager; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- manager: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| name | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| private data | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| skills | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| languages | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| resume | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| birth date | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| medical fitness | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| home base | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| cost rate | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-01 Employee](../01-people/s-f09-01-employee.md).

The records also show on: [S-F9-02 Activity plan](../01-people/s-f09-02-activity-plan.md),
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 employee records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no employee record the user may see yet, with the create action when allowed.
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
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f09-l01-employee-records-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f09-l01-employee-records-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f09-l01-employee-records-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f09-l01-employee-records-u06-hr-phone-dark.png) |
| Listed, U01, view Mine: manager | desktop | ![Listed, U01, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: manager | phone | ![Listed, U01, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u01-employee-phone-light.png) | ![Listed, U01, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u01-employee-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f09-l01-employee-records-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l01-employee-records-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f09-l01-employee-records-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l01-employee-records-u02-manager-phone-dark.png) |
| Listed, U14, view Mine: manager | desktop | ![Listed, U14, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: manager | phone | ![Listed, U14, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u14-field-worker-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f09-l01-employee-records-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f09-l01-employee-records-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f09-l01-employee-records-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f09-l01-employee-records-u13-owner-phone-dark.png) |
| Listed, U45, view Mine: manager | desktop | ![Listed, U45, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Mine: manager | phone | ![Listed, U45, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u45-payroll-officer-phone-dark.png) |
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-f09-l01-employee-records-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f09-l01-employee-records-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-f09-l01-employee-records-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f09-l01-employee-records-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-f09-l01-employee-records-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f09-l01-employee-records-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-f09-l01-employee-records-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f09-l01-employee-records-u29-dispatcher-phone-dark.png) |
| Listed, U26, view Mine: manager | desktop | ![Listed, U26, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: manager | phone | ![Listed, U26, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u26-carer-phone-light.png) | ![Listed, U26, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: manager | desktop | ![Listed, U30, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: manager | phone | ![Listed, U30, view Mine: manager, light](../../images/lists/s-f09-l01-employee-records-u30-driver-phone-light.png) | ![Listed, U30, view Mine: manager, dark](../../images/lists/s-f09-l01-employee-records-u30-driver-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Employee records](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md) |
| Flows | [FL-F1-03](../../../f01-administration/flows/fl-f01-03-user-lifecycle.md), [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F24-06](../../../f24-integrations-hub/flows/fl-f24-06-business-tools.md), [FL-F9-01](../../flows/fl-f09-01-people.md), [FL-F9-02](../../flows/fl-f09-02-recruit.md), [FL-F9-07](../../flows/fl-f09-07-fair-pay-and-speaking-up.md), [FL-F9-08](../../flows/fl-f09-08-hr-duties.md), [FL-F9-09](../../flows/fl-f09-09-train-and-protect.md), [FL-F9-10](../../flows/fl-f09-10-listen-to-employees.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../flows/fl-f09-13-keep-qualifications.md) |

## Open questions

None.

---

⬅️ [S-F9-44 Online courses](../15-work-location-headcount-and-learning/s-f09-44-online-courses.md) ·
⬆️ [Up](README.md) · ➡️ [S-F9-L02 Contracts](s-f09-l02-contracts.md)
