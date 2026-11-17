🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L23 Work accidents

# 🗂️ S-F9-L23 Work accidents

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-23 Work accident](../../data/e-f09-23-work-accident.md) the user may see: to find,
filter, total and act on many work accidents at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Work accidents, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "work accidents" offers this view.
- **AI assistant:** "show the work accidents that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Work accidents    HR and projects › Work accidents   [+ New]                                                 |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATE   DECLARED   LEAVE                                                  |
| employee          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | person's name | yes |
| State | state | badge: Active, Closed | yes |
| Declared | declared | date and time | yes |
| Leave | leave | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active, Closed | the visible rows (D488) |
| Employee | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: work accidents link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by declared.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Open: Active.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New work accident | header | the personas whose roles may create it | the record's own page (Row opens) |
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

- declared: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| what happened | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| leave | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-23 Work accident](../09-train-and-protect/s-f09-23-work-accident.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 work accidents of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no work accident the user may see yet, with the create action when allowed.
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
| Listed, U02, view Open: Active | desktop | ![Listed, U02, view Open: Active, light](../../images/lists/s-f09-l23-work-accidents-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Active, dark](../../images/lists/s-f09-l23-work-accidents-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Active | phone | ![Listed, U02, view Open: Active, light](../../images/lists/s-f09-l23-work-accidents-u02-manager-phone-light.png) | ![Listed, U02, view Open: Active, dark](../../images/lists/s-f09-l23-work-accidents-u02-manager-phone-dark.png) |
| Listed, U06, view Open: Active | desktop | ![Listed, U06, view Open: Active, light](../../images/lists/s-f09-l23-work-accidents-u06-hr-desktop-light.png) | ![Listed, U06, view Open: Active, dark](../../images/lists/s-f09-l23-work-accidents-u06-hr-desktop-dark.png) |
| Listed, U06, view Open: Active | phone | ![Listed, U06, view Open: Active, light](../../images/lists/s-f09-l23-work-accidents-u06-hr-phone-light.png) | ![Listed, U06, view Open: Active, dark](../../images/lists/s-f09-l23-work-accidents-u06-hr-phone-dark.png) |
| Listed, U14, view Mine: employee | desktop | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l23-work-accidents-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l23-work-accidents-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: employee | phone | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l23-work-accidents-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l23-work-accidents-u14-field-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Work accidents](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-F9-09](../../flows/fl-f09-09-train-and-protect.md) |

## Open questions

None.

---

⬅️ [S-F9-L22 Training sessions](s-f09-l22-training-sessions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L24 Risk assessment lines](s-f09-l24-risk-assessment-lines.md)
