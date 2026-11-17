🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L04 Payslip lines

# 🗂️ S-F13-L04 Payslip lines

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-04 Payslip line](../../data/e-f13-04-payslip-line.md) the user may see: to find,
filter, total and act on many payslip lines at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Payslip lines, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "payslip lines" offers this view.
- **AI assistant:** "show the payslip lines that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Payslip lines    Payroll (plugin) › Payslip lines   [+ New]                                                  |
| [count] [total amount]   [chart: count by state, amount stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PAYSLIP   STATE   ITEM   AMOUNT                                                      |
| payslip           | [ ] ...                                                  Open >                          |
| item              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Payslip | payslip | link to the record | yes |
| State | state | badge: Recorded | yes |
| Item | item | link to the record | yes |
| Amount | amount | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Payslip | each linked payslip | the visible rows (D488) |
| Item | each linked item | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Payslip lines of a chosen item, or of the items that match a filter.
- From the other side: the items that have payslip lines, or none.
- Payslip lines of a chosen payslip, or of the payslips that match a filter.
- From the other side: the payslips that have payslip lines, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New payslip line | header | the personas whose roles may create it | the record's own page (Row opens) |
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

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F13-04 Pay computation](../02-monthly-pay-run/s-f13-04-pay-computation.md).

The records also show on: [S-F13-05 Agreement rules](../02-monthly-pay-run/s-f13-05-agreement-rules.md),
[S-F13-16 Simulations](../04-events/s-f13-16-simulations.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 payslip lines of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no payslip line the user may see yet, with the create action when allowed.
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
| Listed, U45, view All | desktop | ![Listed, U45, view All, light](../../images/lists/s-f13-l04-payslip-lines-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f13-l04-payslip-lines-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view All | phone | ![Listed, U45, view All, light](../../images/lists/s-f13-l04-payslip-lines-u45-payroll-officer-phone-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f13-l04-payslip-lines-u45-payroll-officer-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f13-l04-payslip-lines-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f13-l04-payslip-lines-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f13-l04-payslip-lines-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f13-l04-payslip-lines-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Payslip lines](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F13-02](../../flows/fl-f13-02-monthly-pay-run.md), [FL-F13-04](../../flows/fl-f13-04-events.md), [FL-F13-08](../../flows/fl-f13-08-deductions-savings-and-leave-pay.md), [FL-F13-09](../../flows/fl-f13-09-collective-agreements-by-family.md) |

## Open questions

None.

---

⬅️ [S-F13-L03 Pay inputs](s-f13-l03-pay-inputs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L05 Withholding rates](s-f13-l05-withholding-rates.md)
