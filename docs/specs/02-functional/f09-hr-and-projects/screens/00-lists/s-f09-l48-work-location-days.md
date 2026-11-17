🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L48 Work location days

# 🗂️ S-F9-L48 Work location days

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-48 Work location day](../../data/e-f09-48-work-location-day.md) the user may see: to
find, filter, total and act on many work location days at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Work location days, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "work location days" offers this view.
- **AI assistant:** "show the work location days that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Work location days    HR and projects › Work location days   [+ New]                                         |
| [count] [Declared] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   DATE   LOCATION   ALLOWANCE   STATE                                       |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | text | yes |
| Date | date | date | yes |
| Location | location | text | yes |
| Allowance | allowance | money | yes |
| State | state | badge: Declared, Validated, Refused, Withdrawn, Passed to pay | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Declared, Validated, Refused, Withdrawn, Passed to pay | the visible rows (D488) |
| Location | each value | the visible rows (D488) |
| Employee | each value | the visible rows (D488) |
| Month | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Days of a chosen employee, or of the employees that match a filter.
- From the other side: the employees with days, or none this month.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Declared.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Open: Declared.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New work location day | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

Location: an employee changes their own declared day until it is validated.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| declared by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| validated by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-40 Work location](../15-work-location-headcount-and-learning/s-f09-40-work-location.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 work location days of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no work location day the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in the image round from this page: one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)). The files are named by the plan.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U01, view Needs attention | phone | ![Listed, U01, view Needs attention, light](../../images/lists/s-f09-l48-work-location-days-u01-employee-phone-light.png) | ![Listed, U01, view Needs attention, dark](../../images/lists/s-f09-l48-work-location-days-u01-employee-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l48-work-location-days-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l48-work-location-days-u02-manager-desktop-dark.png) |
| Listed, U01, view Mine: employee | desktop | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l48-work-location-days-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l48-work-location-days-u01-employee-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l48-work-location-days-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l48-work-location-days-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Work location days](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F9-15](../../flows/fl-f09-15-work-location-headcount-and-learning.md) |

## Open questions

None.

---

⬅️ [S-F9-L47 Outreach messages](s-f09-l47-outreach-messages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L49 Positions](s-f09-l49-positions.md)
