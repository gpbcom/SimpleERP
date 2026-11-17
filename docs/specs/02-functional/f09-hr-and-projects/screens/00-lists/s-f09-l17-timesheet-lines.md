🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L17 Timesheet lines

# 🗂️ S-F9-L17 Timesheet lines

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05, U09, U13, U41: their use cases only read these records, inside a screen of the use case, so
they open them from there (D493).

## Purpose

The aggregated list of every [E-F9-17 Timesheet line](../../data/e-f09-17-timesheet-line.md) the user may see: to find,
filter, total and act on many timesheet lines at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Timesheet lines, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "timesheet lines" offers this view.
- **AI assistant:** "show the timesheet lines that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Timesheet lines    HR and projects › Timesheet lines   [+ New]                                               |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| employee          | [ ] EMPLOYEE   STATE   HOURS                                                             |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | person's name | yes |
| State | state | badge: Draft, Submitted, Validated, Billed | yes |
| Hours | hours | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Employee | each person, the user first | the visible rows (D488) |
| State | Draft, Submitted, Validated, Billed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: timesheet lines link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New timesheet line | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the employee; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- hours: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F9-16 Timesheets](../03-time/s-f09-16-timesheets.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 timesheet lines of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no timesheet line the user may see yet, with the create action when allowed.
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
| Listed, U01, view Mine: employee | desktop | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l17-timesheet-lines-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l17-timesheet-lines-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: employee | phone | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l17-timesheet-lines-u01-employee-phone-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l17-timesheet-lines-u01-employee-phone-dark.png) |
| Listed, U14, view Mine: employee | desktop | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l17-timesheet-lines-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l17-timesheet-lines-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: employee | phone | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l17-timesheet-lines-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l17-timesheet-lines-u14-field-worker-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l17-timesheet-lines-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l17-timesheet-lines-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l17-timesheet-lines-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l17-timesheet-lines-u02-manager-phone-dark.png) |
| Listed, U29, view Mine | desktop | ![Listed, U29, view Mine, light](../../images/lists/s-f09-l17-timesheet-lines-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Mine, dark](../../images/lists/s-f09-l17-timesheet-lines-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Mine | phone | ![Listed, U29, view Mine, light](../../images/lists/s-f09-l17-timesheet-lines-u29-dispatcher-phone-light.png) | ![Listed, U29, view Mine, dark](../../images/lists/s-f09-l17-timesheet-lines-u29-dispatcher-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Timesheet lines](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md) |
| Flows | [FL-F9-03](../../flows/fl-f09-03-time.md), [FL-F9-06](../../flows/fl-f09-06-plan-and-deliver-work.md), [FL-SC14-04](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-04-product-delivery.md) |

## Open questions

None.

---

⬅️ [S-F9-L16 Shifts](s-f09-l16-shifts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L18 Project and tasks](s-f09-l18-project-and-tasks.md)
