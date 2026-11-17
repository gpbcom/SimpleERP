🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L09 Expense claims

# 🗂️ S-F8-L09 Expense claims

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F8-09 Expense claim](../../data/e-f08-09-expense-claim.md) the user may see: to find,
filter, total and act on many expense claims at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Expense claims, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "expense claims" offers this view.
- **AI assistant:** "show the expense claims that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Expense claims    Accounting › Expense claims   [+ New]                                                      |
| [count] [total amount] [Draft]   [chart: count by state, amount stacked]                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| employee          | [ ] EMPLOYEE   STATE   RECEIPT   AMOUNT   CATEGORY                                       |
| category          | [ ] ...                                                  Open >                          |
| receipt           | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | person's name | yes |
| State | state | badge: Draft, Submitted, Approved, Reimbursed, Refused | yes |
| Receipt | receipt | file name | no |
| Amount | amount | amount, right-aligned | yes |
| Category | category | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Employee | each person, the user first | the visible rows (D488) |
| Category | each value | the visible rows (D488) |
| Receipt | each value | the visible rows (D488) |
| State | Draft, Submitted, Approved, Reimbursed, Refused | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Expense claims of a chosen receipt, or of the receipts that match a filter.
- From the other side: the receipts that have expense claims, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

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
| New expense claim | header | the personas whose roles may create it | the record's own page (Row opens) |
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

- category: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| receipt | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F8-12 Expenses](../02-purchase-to-pay/s-f08-12-expenses.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 expense claims of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no expense claim the user may see yet, with the create action when allowed.
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
| Listed, U01, view Mine: employee | desktop | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f08-l09-expense-claims-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f08-l09-expense-claims-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: employee | phone | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f08-l09-expense-claims-u01-employee-phone-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f08-l09-expense-claims-u01-employee-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f08-l09-expense-claims-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f08-l09-expense-claims-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f08-l09-expense-claims-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f08-l09-expense-claims-u02-manager-phone-dark.png) |
| Listed, U05, view Mine: employee | desktop | ![Listed, U05, view Mine: employee, light](../../images/lists/s-f08-l09-expense-claims-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: employee, dark](../../images/lists/s-f08-l09-expense-claims-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: employee | phone | ![Listed, U05, view Mine: employee, light](../../images/lists/s-f08-l09-expense-claims-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: employee, dark](../../images/lists/s-f08-l09-expense-claims-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Expense claims](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-F2-11](../../../f02-no-code-configuration/flows/fl-f02-11-rights-translations-and-approvals.md), [FL-F8-02](../../flows/fl-f08-02-purchase-to-pay.md) |

## Open questions

None.

---

⬅️ [S-F8-L08 Accounting budgets](s-f08-l08-accounting-budgets.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L10 Fiscal periods](s-f08-l10-fiscal-periods.md)
