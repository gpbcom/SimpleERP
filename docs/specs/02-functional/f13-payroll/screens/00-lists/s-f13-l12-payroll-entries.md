🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L12 Payroll entries

# 🗂️ S-F13-L12 Payroll entries

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | as the permissions row "Payroll entries, transfers": prepare | actions as [permissions](../../permissions.md) gives them |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | as the permissions row "Payroll entries, transfers": ✅ post, send | actions as [permissions](../../permissions.md) gives them |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Payroll entries, transfers": approve | actions as [permissions](../../permissions.md) gives them |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | as the permissions row "Payroll entries, transfers": read their own entries only (UC-F13-28) | actions as [permissions](../../permissions.md) gives them |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-12 Payroll entry](../../data/e-f13-12-payroll-entry.md) the user may see: to find,
filter, total and act on many payroll entries at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Payroll entries, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "payroll entries" offers this view.
- **AI assistant:** "show the payroll entries that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Payroll entries    Payroll (plugin) › Payroll entries   [+ New]                                              |
| [count] [total amount]   [chart: count by state, amount stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RUN   STATE   ACCOUNT   AMOUNT                                                       |
| account           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Run | run | link to the record | yes |
| State | state | badge: Recorded | yes |
| Account | account | link to the record | yes |
| Amount | amount | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Account | each linked account | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Payroll entries of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have payroll entries, or none.

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
| New payroll entry | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F13-13 Payroll entries](../03-declarations-and-payments/s-f13-13-payroll-entries.md).

The records also show on: [S-F13-25 Profit-sharing](../08-deductions-savings-and-leave-pay/s-f13-25-profit-sharing.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 payroll entries of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no payroll entry the user may see yet, with the create action when allowed.
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
| Listed, U45, view All | desktop | ![Listed, U45, view All, light](../../images/lists/s-f13-l12-payroll-entries-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view All | phone | ![Listed, U45, view All, light](../../images/lists/s-f13-l12-payroll-entries-u45-payroll-officer-phone-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u45-payroll-officer-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f13-l12-payroll-entries-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f13-l12-payroll-entries-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f13-l12-payroll-entries-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f13-l12-payroll-entries-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u13-owner-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f13-l12-payroll-entries-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f13-l12-payroll-entries-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u01-employee-phone-dark.png) |
| Listed, U08, view All | desktop | ![Listed, U08, view All, light](../../images/lists/s-f13-l12-payroll-entries-u08-external-accountant-desktop-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view All | phone | ![Listed, U08, view All, light](../../images/lists/s-f13-l12-payroll-entries-u08-external-accountant-phone-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f13-l12-payroll-entries-u08-external-accountant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Payroll entries](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md) |
| Flows | [FL-F13-03](../../flows/fl-f13-03-declarations-and-payments.md), [FL-F13-08](../../flows/fl-f13-08-deductions-savings-and-leave-pay.md) |

## Open questions

None.

---

⬅️ [S-F13-L11 Contribution payments](s-f13-l11-contribution-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L13 Sick leaves](s-f13-l13-sick-leaves.md)
