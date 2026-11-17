🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L04 Transfers

# 🗂️ S-F7-L04 Transfers

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F7-04 Transfer](../../data/e-f07-04-transfer.md) the user may see: to find, filter,
total and act on many transfers at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Transfers, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "transfers" offers this view.
- **AI assistant:** "show the transfers that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Transfers    Purchasing and stock › Transfers   [+ New]                                                      |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] KIND   STATE                                                                         |
| kind              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Kind | kind | label | yes |
| State | state | badge: Sent, Received, Reserved, Flagged, Lost | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Sent, Received, Reserved, Flagged, Lost | the visible rows (D488) |
| Kind | receipt, internal, delivery, return | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: transfers link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Sent, Received, Reserved.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New transfer | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
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

Open › goes to [S-F7-03 Receipt](../02-receive-and-store/s-f07-03-receipt.md).

The records also show on:
[S-F10-25 Store stock and transfers](../../../f10-point-of-sale/screens/10-clienteling-transfers-and-tax-free/s-f10-25-store-stock-and-transfers.md),
[S-F11-27 Store fulfilment](../../../f11-online-shop/screens/10-fulfil-from-stores-and-report/s-f11-27-store-fulfilment.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 transfers of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no transfer the user may see yet, with the create action when allowed.
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
| Listed, U15, view Open: Sent, Received, Reserved | desktop | ![Listed, U15, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Open: Sent, Received, Reserved | phone | ![Listed, U15, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u15-warehouse-operator-phone-dark.png) |
| Listed, U17, view Open: Sent, Received, Reserved | desktop | ![Listed, U17, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u17-cashier-desktop-light.png) | ![Listed, U17, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u17-cashier-desktop-dark.png) |
| Listed, U17, view Open: Sent, Received, Reserved | phone | ![Listed, U17, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u17-cashier-phone-light.png) | ![Listed, U17, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u17-cashier-phone-dark.png) |
| Listed, U23, view Open: Sent, Received, Reserved | desktop | ![Listed, U23, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u23-store-manager-desktop-light.png) | ![Listed, U23, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Open: Sent, Received, Reserved | phone | ![Listed, U23, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u23-store-manager-phone-light.png) | ![Listed, U23, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u23-store-manager-phone-dark.png) |
| Listed, U04, view Open: Sent, Received, Reserved | desktop | ![Listed, U04, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u04-purchasing-desktop-light.png) | ![Listed, U04, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Open: Sent, Received, Reserved | phone | ![Listed, U04, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u04-purchasing-phone-light.png) | ![Listed, U04, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u04-purchasing-phone-dark.png) |
| Listed, U02, view Open: Sent, Received, Reserved | desktop | ![Listed, U02, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Sent, Received, Reserved | phone | ![Listed, U02, view Open: Sent, Received, Reserved, light](../../images/lists/s-f07-l04-transfers-u02-manager-phone-light.png) | ![Listed, U02, view Open: Sent, Received, Reserved, dark](../../images/lists/s-f07-l04-transfers-u02-manager-phone-dark.png) |
| Listed, U20, view Open | desktop | ![Listed, U20, view Open, light](../../images/lists/s-f07-l04-transfers-u20-production-operator-desktop-light.png) | ![Listed, U20, view Open, dark](../../images/lists/s-f07-l04-transfers-u20-production-operator-desktop-dark.png) |
| Listed, U20, view Open | phone | ![Listed, U20, view Open, light](../../images/lists/s-f07-l04-transfers-u20-production-operator-phone-light.png) | ![Listed, U20, view Open, dark](../../images/lists/s-f07-l04-transfers-u20-production-operator-phone-dark.png) |
| Listed, U21, view Open | desktop | ![Listed, U21, view Open, light](../../images/lists/s-f07-l04-transfers-u21-production-planner-desktop-light.png) | ![Listed, U21, view Open, dark](../../images/lists/s-f07-l04-transfers-u21-production-planner-desktop-dark.png) |
| Listed, U21, view Open | phone | ![Listed, U21, view Open, light](../../images/lists/s-f07-l04-transfers-u21-production-planner-phone-light.png) | ![Listed, U21, view Open, dark](../../images/lists/s-f07-l04-transfers-u21-production-planner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Transfers](README.md) |
| Workspaces | [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md) |
| Flows | [FL-F10-10](../../../f10-point-of-sale/flows/fl-f10-10-clienteling-transfers-and-tax-free.md), [FL-F11-10](../../../f11-online-shop/flows/fl-f11-10-fulfil-from-stores-and-report.md), [FL-F12-05](../../../f12-manufacturing/flows/fl-f12-05-subcontracting-and-costs.md), [FL-F12-07](../../../f12-manufacturing/flows/fl-f12-07-compliance-and-safety.md), [FL-F6-02](../../../f06-customers-and-sales/flows/fl-f06-02-quote-to-order.md), [FL-F7-02](../../flows/fl-f07-02-receive-and-store.md), [FL-F7-03](../../flows/fl-f07-03-replenish.md), [FL-F7-04](../../flows/fl-f07-04-pick-pack-and-ship.md), [FL-F7-05](../../flows/fl-f07-05-count-trace-and-analyse.md), [FL-F7-07](../../flows/fl-f07-07-supplier-agreements-and-performance.md), [FL-F7-09](../../flows/fl-f07-09-compliance-and-carbon.md), [FL-SC07-03](../../../../08-sectors/sc07-transport/flows/fl-sc07-03-on-the-road.md), [FL-SC15-04](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-04-import-and-suppliers.md) |

## Open questions

None.

---

⬅️ [S-F7-L03 Purchase orders](s-f07-l03-purchase-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L05 Supplier invoices](s-f07-l05-supplier-invoices.md)
