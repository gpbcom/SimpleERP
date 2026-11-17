🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L04 Bank lines

# 🗂️ S-F8-L04 Bank lines

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U34 Property manager](../../../../01-users/personas/u34-property-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U31: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F8-04 Bank line](../../data/e-f08-04-bank-line.md) the user may see: to find, filter,
total and act on many bank lines at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Bank lines, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "bank lines" offers this view.
- **AI assistant:** "show the bank lines that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Bank lines    Accounting › Bank lines   [+ New]                                                              |
| [count] [total amount] [new this month]   [chart: count by state, amount stacked]                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| account           | [ ] ACCOUNT   STATE   AMOUNT   DATE                                                      |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Account | account | text | yes |
| State | state | badge: ToReconcile, Reconciled, InSuspense | yes |
| Amount | amount | amount, right-aligned | yes |
| Date | date | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Account | each value | the visible rows (D488) |
| State | ToReconcile, Reconciled, InSuspense | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Bank lines of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have bank lines, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- New this month, by date.

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
| New bank line | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F8-06 Bank reconciliation](../03-bank-and-collect/s-f08-06-bank-reconciliation.md).

The records also show on: [S-F8-04 Supplier payments](../02-purchase-to-pay/s-f08-04-supplier-payments.md),
[S-F8-05 Customer payments](../03-bank-and-collect/s-f08-05-customer-payments.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 bank lines of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no bank line the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f08-l04-bank-lines-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l04-bank-lines-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f08-l04-bank-lines-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l04-bank-lines-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f08-l04-bank-lines-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f08-l04-bank-lines-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f08-l04-bank-lines-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f08-l04-bank-lines-u13-owner-phone-dark.png) |
| Listed, U34, view All | desktop | ![Listed, U34, view All, light](../../images/lists/s-f08-l04-bank-lines-u34-property-manager-desktop-light.png) | ![Listed, U34, view All, dark](../../images/lists/s-f08-l04-bank-lines-u34-property-manager-desktop-dark.png) |
| Listed, U34, view All | phone | ![Listed, U34, view All, light](../../images/lists/s-f08-l04-bank-lines-u34-property-manager-phone-light.png) | ![Listed, U34, view All, dark](../../images/lists/s-f08-l04-bank-lines-u34-property-manager-phone-dark.png) |
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-f08-l04-bank-lines-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-f08-l04-bank-lines-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-f08-l04-bank-lines-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-f08-l04-bank-lines-u36-professional-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Bank lines](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U34](../../../../04-ux/views/u34-property-manager/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md) |
| Flows | [FL-F10-09](../../../f10-point-of-sale/flows/fl-f10-09-cash-and-settlements.md), [FL-F8-01](../../flows/fl-f08-01-set-up-and-post.md), [FL-F8-02](../../flows/fl-f08-02-purchase-to-pay.md), [FL-F8-03](../../flows/fl-f08-03-bank-and-collect.md), [FL-F8-07](../../flows/fl-f08-07-client-money-grants-and-non-profits.md), [FL-F8-09](../../flows/fl-f08-09-pay-analyse-and-report.md) |

## Open questions

None.

---

⬅️ [S-F8-L03 Journal entries](s-f08-l03-journal-entries.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L05 Reconciliation models](s-f08-l05-reconciliation-models.md)
