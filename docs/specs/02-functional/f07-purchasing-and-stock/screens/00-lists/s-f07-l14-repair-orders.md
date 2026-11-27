🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L14 Repair orders

# 🗂️ S-F7-L14 Repair orders

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F7-14 Repair order](../../data/e-f07-14-repair-order.md) the user may see: to find,
filter, total and act on many repair orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Repair orders, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "repair orders" offers this view.
- **AI assistant:** "show the repair orders that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Repair orders    Purchasing and stock › Repair orders   [+ New]                                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| under warranty    | [ ] PRODUCT   STATE   UNDER WARRANTY                                                     |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | link to the record | yes |
| State | state | badge: ToDo, InRepair, Done, Invoiced | yes |
| Under warranty | under warranty | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Under warranty | yes, no | the visible rows (D488) |
| State | ToDo, InRepair, Done, Invoiced | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: repair orders link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: ToDo, InRepair, Invoiced.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New repair order | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- under warranty: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-17 Repairs](../06-benchmark-additions/s-f07-17-repairs.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 repair orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no repair order the user may see yet, with the create action when allowed.
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
| Listed, U15, view Open: ToDo, InRepair, Invoiced | desktop | ![Listed, U15, view Open: ToDo, InRepair, Invoiced, light](../../images/lists/s-f07-l14-repair-orders-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Open: ToDo, InRepair, Invoiced, dark](../../images/lists/s-f07-l14-repair-orders-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Open: ToDo, InRepair, Invoiced | phone | ![Listed, U15, view Open: ToDo, InRepair, Invoiced, light](../../images/lists/s-f07-l14-repair-orders-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Open: ToDo, InRepair, Invoiced, dark](../../images/lists/s-f07-l14-repair-orders-u15-warehouse-operator-phone-dark.png) |
| Listed, U09, view Open: ToDo, InRepair, Invoiced | desktop | ![Listed, U09, view Open: ToDo, InRepair, Invoiced, light](../../images/lists/s-f07-l14-repair-orders-u09-customer-desktop-light.png) | ![Listed, U09, view Open: ToDo, InRepair, Invoiced, dark](../../images/lists/s-f07-l14-repair-orders-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: ToDo, InRepair, Invoiced | phone | ![Listed, U09, view Open: ToDo, InRepair, Invoiced, light](../../images/lists/s-f07-l14-repair-orders-u09-customer-phone-light.png) | ![Listed, U09, view Open: ToDo, InRepair, Invoiced, dark](../../images/lists/s-f07-l14-repair-orders-u09-customer-phone-dark.png) |
| Listed, U16, view Open | desktop | ![Listed, U16, view Open, light](../../images/lists/s-f07-l14-repair-orders-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open, dark](../../images/lists/s-f07-l14-repair-orders-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open | phone | ![Listed, U16, view Open, light](../../images/lists/s-f07-l14-repair-orders-u16-office-worker-phone-light.png) | ![Listed, U16, view Open, dark](../../images/lists/s-f07-l14-repair-orders-u16-office-worker-phone-dark.png) |
| Listed, U53, view Open | desktop | ![Listed, U53, view Open, light](../../images/lists/s-f07-l14-repair-orders-u53-coach-desktop-light.png) | ![Listed, U53, view Open, dark](../../images/lists/s-f07-l14-repair-orders-u53-coach-desktop-dark.png) |
| Listed, U53, view Open | phone | ![Listed, U53, view Open, light](../../images/lists/s-f07-l14-repair-orders-u53-coach-phone-light.png) | ![Listed, U53, view Open, dark](../../images/lists/s-f07-l14-repair-orders-u53-coach-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Repair orders](README.md) |
| Workspaces | [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md) |
| Flows | [FL-F12-03](../../../f12-manufacturing/flows/fl-f12-03-make-the-products.md), [FL-F7-06](../../flows/fl-f07-06-benchmark-additions.md) |

## Open questions

None.

---

⬅️ [S-F7-L13 Call for tenders](s-f07-l13-call-for-tenders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L15 Supplier contracts](s-f07-l15-supplier-contracts.md)
