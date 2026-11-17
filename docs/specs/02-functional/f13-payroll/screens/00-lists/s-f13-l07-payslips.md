🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L07 Payslips

# 🗂️ S-F13-L07 Payslips

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | as the permissions row "Payslips": ✅ all | actions as [permissions](../../permissions.md) gives them |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | as the permissions row "Payslips": own only | actions as [permissions](../../permissions.md) gives them |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-07 Payslip](../../data/e-f13-07-payslip.md) the user may see: to find, filter, total
and act on many payslips at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Payslips, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "payslips" offers this view.
- **AI assistant:** "show the payslips that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Payslips    Payroll (plugin) › Payslips   [+ New]                                                            |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATE   PERIOD                                                            |
| employee          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | link to the record | yes |
| State | state | badge: Published, Available | yes |
| Period | period | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Published, Available | the visible rows (D488) |
| Employee | each linked employee | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: payslips link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by period.

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

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New payslip | header | the personas whose roles may create it | the record's own page (Row opens) |
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

- period: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F13-08 Payslips](../02-monthly-pay-run/s-f13-08-payslips.md).

The records also show on: [S-F13-20 Payroll assistant](../06-assistant/s-f13-20-payroll-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 payslips of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no payslip the user may see yet, with the create action when allowed.
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
| Listed, U45, view Mine: employee | desktop | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l07-payslips-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l07-payslips-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Mine: employee | phone | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l07-payslips-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l07-payslips-u45-payroll-officer-phone-dark.png) |
| Listed, U01, view Mine: employee | desktop | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f13-l07-payslips-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f13-l07-payslips-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: employee | phone | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f13-l07-payslips-u01-employee-phone-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f13-l07-payslips-u01-employee-phone-dark.png) |
| Listed, U08, view All | desktop | ![Listed, U08, view All, light](../../images/lists/s-f13-l07-payslips-u08-external-accountant-desktop-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f13-l07-payslips-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view All | phone | ![Listed, U08, view All, light](../../images/lists/s-f13-l07-payslips-u08-external-accountant-phone-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f13-l07-payslips-u08-external-accountant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Payslips](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md) |
| Flows | [FL-F13-02](../../flows/fl-f13-02-monthly-pay-run.md), [FL-F13-06](../../flows/fl-f13-06-assistant.md), [FL-F13-09](../../flows/fl-f13-09-collective-agreements-by-family.md), [FL-F24-06](../../../f24-integrations-hub/flows/fl-f24-06-business-tools.md) |

## Open questions

None.

---

⬅️ [S-F13-L06 Pay runs](s-f13-l06-pay-runs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L08 Pay transfers](s-f13-l08-pay-transfers.md)
