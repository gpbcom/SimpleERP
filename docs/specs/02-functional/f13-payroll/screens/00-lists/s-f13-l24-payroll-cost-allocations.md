🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L24 Payroll cost allocations

# 🗂️ S-F13-L24 Payroll cost allocations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-24 Payroll cost allocation](../../data/e-f13-24-payroll-cost-allocation.md) the user
may see: to find, filter, total and act on many payroll cost allocations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Payroll cost allocations, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "payroll cost allocations" offers this view.
- **AI assistant:** "show the payroll cost allocations that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Payroll cost allocations    Payroll (plugin) › Payroll cost allocations   [+ New]                            |
| [count] [total value]   [chart: count by state, value stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PAY RUN   STATE   EMPLOYEE   VALUE   COST   SHARE                                    |
| pay run           | [ ] ...                                                  Open >                          |
| employee          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Pay run | pay run | link to the record | yes |
| State | state | badge: Computed, Posted | yes |
| Employee | employee | link to the record | yes |
| Value | value | text | yes |
| Cost | cost | amount, right-aligned | yes |
| Share | share | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Computed, Posted | the visible rows (D488) |
| Pay run | each linked pay run | the visible rows (D488) |
| Employee | each linked employee | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Payroll cost allocations of a chosen pay run, or of the pay runs that match a filter.
- From the other side: the pay runs that have payroll cost allocations, or none.

## KPI strip

- Count of the visible rows.
- Total of value.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, value stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Mine: employee.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New payroll cost allocation | header | the personas whose roles may create it | the record's own page (Row opens) |
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

- share: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| cost | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F13-13 Payroll entries](../03-declarations-and-payments/s-f13-13-payroll-entries.md).

The records also show on: [S-F13-27 Payroll analytics](../05-reports-and-rules/s-f13-27-payroll-analytics.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 payroll cost allocations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no payroll cost allocation the user may see yet, with the create action when allowed.
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
| Listed, U05, view Mine: employee | desktop | ![Listed, U05, view Mine: employee, light](../../images/lists/s-f13-l24-payroll-cost-allocations-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: employee, dark](../../images/lists/s-f13-l24-payroll-cost-allocations-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: employee | phone | ![Listed, U05, view Mine: employee, light](../../images/lists/s-f13-l24-payroll-cost-allocations-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: employee, dark](../../images/lists/s-f13-l24-payroll-cost-allocations-u05-accounting-phone-dark.png) |
| Listed, U45, view Mine: employee | desktop | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l24-payroll-cost-allocations-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l24-payroll-cost-allocations-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Mine: employee | phone | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l24-payroll-cost-allocations-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l24-payroll-cost-allocations-u45-payroll-officer-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f13-l24-payroll-cost-allocations-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f13-l24-payroll-cost-allocations-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f13-l24-payroll-cost-allocations-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f13-l24-payroll-cost-allocations-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Payroll cost allocations](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F13-03](../../flows/fl-f13-03-declarations-and-payments.md), [FL-F13-05](../../flows/fl-f13-05-reports-and-rules.md) |

## Open questions

None.

---

⬅️ [S-F13-L23 Agreement families](s-f13-l23-agreement-families.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L25 Analytic axis](s-f13-l25-analytic-axis.md)
