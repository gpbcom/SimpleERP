🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L15 Supplier contracts

# 🗂️ S-F7-L15 Supplier contracts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F7-15 Supplier contract](../../data/e-f07-15-supplier-contract.md) the user may see: to
find, filter, total and act on many supplier contracts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Supplier contracts, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "supplier contracts" offers this view.
- **AI assistant:** "show the supplier contracts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Supplier contracts    Purchasing and stock › Supplier contracts   [+ New]                                    |
| [count] [total prices] [Draft] [new this month]   [chart: count by state, prices stacked]                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SUPPLIER   STATE   FILE   PRICES   VALIDITY   NOTICE   REBATE TIERS                  |
| supplier          | [ ] ...                                                  Open >                          |
| rebate tiers      | [ ] ...                                                  Open >                          |
| file              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Supplier | supplier | text | yes |
| State | state | badge: Draft, Active, Renewed, Ended | yes |
| File | file | text | yes |
| Prices | prices | amount, right-aligned | yes |
| Validity | validity | date | yes |
| Notice | notice | text | yes |
| Rebate tiers | rebate tiers | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Active, Renewed, Ended | the visible rows (D488) |
| Supplier | each value | the visible rows (D488) |
| Rebate tiers | each value | the visible rows (D488) |
| File | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Supplier contracts of a chosen file, or of the files that match a filter.
- From the other side: the files that have supplier contracts, or none.
- Supplier contracts of a chosen supplier, or of the suppliers that match a filter.
- From the other side: the suppliers that have supplier contracts, or none.

## KPI strip

- Count of the visible rows.
- Total of prices.
- Needs attention: count in the state Draft.
- New this month, by validity.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, prices stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Draft, Active, Renewed.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New supplier contract | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- validity: editable in its cell unless the record's state locks it.
- notice: editable in its cell unless the record's state locks it.
- rebate tiers: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-18 Supplier contracts](../07-supplier-agreements-and-performance/s-f07-18-supplier-contracts.md).

The records also show on: [S-F7-02 Purchase order](../01-procure/s-f07-02-purchase-order.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 supplier contracts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no supplier contract the user may see yet, with the create action when allowed.
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
| Listed, U04, view Open: Draft, Active, Renewed | desktop | ![Listed, U04, view Open: Draft, Active, Renewed, light](../../images/lists/s-f07-l15-supplier-contracts-u04-purchasing-desktop-light.png) | ![Listed, U04, view Open: Draft, Active, Renewed, dark](../../images/lists/s-f07-l15-supplier-contracts-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Open: Draft, Active, Renewed | phone | ![Listed, U04, view Open: Draft, Active, Renewed, light](../../images/lists/s-f07-l15-supplier-contracts-u04-purchasing-phone-light.png) | ![Listed, U04, view Open: Draft, Active, Renewed, dark](../../images/lists/s-f07-l15-supplier-contracts-u04-purchasing-phone-dark.png) |
| Listed, U05, view Open: Draft, Active, Renewed | desktop | ![Listed, U05, view Open: Draft, Active, Renewed, light](../../images/lists/s-f07-l15-supplier-contracts-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Draft, Active, Renewed, dark](../../images/lists/s-f07-l15-supplier-contracts-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Draft, Active, Renewed | phone | ![Listed, U05, view Open: Draft, Active, Renewed, light](../../images/lists/s-f07-l15-supplier-contracts-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Draft, Active, Renewed, dark](../../images/lists/s-f07-l15-supplier-contracts-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Supplier contracts](README.md) |
| Workspaces | [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-F7-03](../../flows/fl-f07-03-replenish.md), [FL-F7-07](../../flows/fl-f07-07-supplier-agreements-and-performance.md), [FL-F7-08](../../flows/fl-f07-08-catalogues-and-stock-levels.md) |

## Open questions

None.

---

⬅️ [S-F7-L14 Repair orders](s-f07-l14-repair-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L16 Supplier scores](s-f07-l16-supplier-scores.md)
