🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L08 Accounting budgets

# 🗂️ S-F8-L08 Accounting budgets

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U54, U55: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F8-08 Accounting budget](../../data/e-f08-08-accounting-budget.md) the user may see: to
find, filter, total and act on many accounting budgets at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Accounting budgets, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "accounting budgets" offers this view.
- **AI assistant:** "show the accounting budgets that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Accounting budgets    Accounting › Accounting budgets   [+ New]                                              |
| [count] [total lines]   [chart: count by state, lines stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PLAN   STATE   LINES   REVISION                                                      |
| plan              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Plan | plan | text | yes |
| State | state | badge: Active | yes |
| Lines | lines | amount, right-aligned | yes |
| Revision | revision | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Plan | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Accounting budgets of a chosen plan, or of the plans that match a filter.
- From the other side: the plans that have accounting budgets, or none.

## KPI strip

- Count of the visible rows.
- Total of lines.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, lines stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
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
| New accounting budget | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- revision: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F8-09 Analytics and budgets](../04-tax-assets-and-analytics/s-f08-09-analytics-and-budgets.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 accounting budgets of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no accounting budget the user may see yet, with the create action when allowed.
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
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f08-l08-accounting-budgets-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f08-l08-accounting-budgets-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f08-l08-accounting-budgets-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f08-l08-accounting-budgets-u02-manager-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f08-l08-accounting-budgets-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f08-l08-accounting-budgets-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f08-l08-accounting-budgets-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f08-l08-accounting-budgets-u13-owner-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f08-l08-accounting-budgets-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l08-accounting-budgets-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f08-l08-accounting-budgets-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l08-accounting-budgets-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Accounting budgets](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-F7-01](../../../f07-purchasing-and-stock/flows/fl-f07-01-procure.md), [FL-F8-04](../../flows/fl-f08-04-tax-assets-and-analytics.md), [FL-SC03-04](../../../../08-sectors/sc03-services/flows/fl-sc03-04-bill-and-recognise.md), [FL-SC10-05](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-05-co-ownership.md), [FL-SC14-04](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-04-product-delivery.md) |

## Open questions

None.

---

⬅️ [S-F8-L07 Fixed assets](s-f08-l07-fixed-assets.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L09 Expense claims](s-f08-l09-expense-claims.md)
