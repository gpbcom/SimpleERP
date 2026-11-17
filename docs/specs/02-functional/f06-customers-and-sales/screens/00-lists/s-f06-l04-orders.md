🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L04 Orders

# 🗂️ S-F6-L04 Orders

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | as the permissions row "Orders": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | as the permissions row "Orders": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | as the permissions row "Orders": read, to release held orders (UC-F6-18) | actions as [permissions](../../permissions.md) gives them |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Orders": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U12, U21: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F6-04 Order](../../data/e-f06-04-order.md) the user may see: to find, filter, total and
act on many orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Orders, in the capability's menu (D495).
- **Workspaces:** 10 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "orders" offers this view.
- **AI assistant:** "show the orders that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Orders    Customers and sales › Orders   [+ New]                                                             |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| quote             | [ ] NUMBER   STATE   QUOTE   PROGRESS                                                    |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| State | state | badge: Open, InProgress, Done, Cancelled | yes |
| Quote | quote | text | yes |
| Progress | progress | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Quote | each value | the visible rows (D488) |
| State | Open, InProgress, Done, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Orders of a chosen quote, or of the quotes that match a filter.
- From the other side: the quotes that have orders, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Open, InProgress.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New order | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- progress: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F6-05 Order](../02-quote-to-order/s-f06-05-order.md).

The records also show on: [S-F6-18 Phone order](../09-sell-on-the-road-and-steer-sales/s-f06-18-phone-order.md),
[S-F6-16 Credit control](../06-accounts-and-credit/s-f06-16-credit-control.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no order the user may see yet, with the create action when allowed.
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
| Listed, U03, view Open: Open, InProgress | desktop | ![Listed, U03, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Open, InProgress | phone | ![Listed, U03, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u03-sales-phone-light.png) | ![Listed, U03, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u03-sales-phone-dark.png) |
| Listed, U16, view Open: Open, InProgress | desktop | ![Listed, U16, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: Open, InProgress | phone | ![Listed, U16, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u16-office-worker-phone-dark.png) |
| Listed, U05, view Open: Open, InProgress | desktop | ![Listed, U05, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Open, InProgress | phone | ![Listed, U05, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u05-accounting-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l04-orders-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l04-orders-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l04-orders-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l04-orders-u13-owner-phone-dark.png) |
| Listed, U42, view Open: Open, InProgress | desktop | ![Listed, U42, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Open: Open, InProgress | phone | ![Listed, U42, view Open: Open, InProgress, light](../../images/lists/s-f06-l04-orders-u42-sales-representative-phone-light.png) | ![Listed, U42, view Open: Open, InProgress, dark](../../images/lists/s-f06-l04-orders-u42-sales-representative-phone-dark.png) |
| Listed, U04, view Open | desktop | ![Listed, U04, view Open, light](../../images/lists/s-f06-l04-orders-u04-purchasing-desktop-light.png) | ![Listed, U04, view Open, dark](../../images/lists/s-f06-l04-orders-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Open | phone | ![Listed, U04, view Open, light](../../images/lists/s-f06-l04-orders-u04-purchasing-phone-light.png) | ![Listed, U04, view Open, dark](../../images/lists/s-f06-l04-orders-u04-purchasing-phone-dark.png) |
| Listed, U09, view Open | desktop | ![Listed, U09, view Open, light](../../images/lists/s-f06-l04-orders-u09-customer-desktop-light.png) | ![Listed, U09, view Open, dark](../../images/lists/s-f06-l04-orders-u09-customer-desktop-dark.png) |
| Listed, U09, view Open | phone | ![Listed, U09, view Open, light](../../images/lists/s-f06-l04-orders-u09-customer-phone-light.png) | ![Listed, U09, view Open, dark](../../images/lists/s-f06-l04-orders-u09-customer-phone-dark.png) |
| Listed, U15, view Open | desktop | ![Listed, U15, view Open, light](../../images/lists/s-f06-l04-orders-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Open, dark](../../images/lists/s-f06-l04-orders-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Open | phone | ![Listed, U15, view Open, light](../../images/lists/s-f06-l04-orders-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Open, dark](../../images/lists/s-f06-l04-orders-u15-warehouse-operator-phone-dark.png) |
| Listed, U23, view Open | desktop | ![Listed, U23, view Open, light](../../images/lists/s-f06-l04-orders-u23-store-manager-desktop-light.png) | ![Listed, U23, view Open, dark](../../images/lists/s-f06-l04-orders-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Open | phone | ![Listed, U23, view Open, light](../../images/lists/s-f06-l04-orders-u23-store-manager-phone-light.png) | ![Listed, U23, view Open, dark](../../images/lists/s-f06-l04-orders-u23-store-manager-phone-dark.png) |
| Listed, U28, view Open | desktop | ![Listed, U28, view Open, light](../../images/lists/s-f06-l04-orders-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view Open, dark](../../images/lists/s-f06-l04-orders-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view Open | phone | ![Listed, U28, view Open, light](../../images/lists/s-f06-l04-orders-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view Open, dark](../../images/lists/s-f06-l04-orders-u28-hotel-receptionist-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Orders](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md) |
| Flows | [FL-F11-04](../../../f11-online-shop/flows/fl-f11-04-special-sales.md), [FL-F11-06](../../../f11-online-shop/flows/fl-f11-06-channels-and-legal.md), [FL-F11-07](../../../f11-online-shop/flows/fl-f11-07-payment-risk.md), [FL-F11-10](../../../f11-online-shop/flows/fl-f11-10-fulfil-from-stores-and-report.md), [FL-F12-02](../../../f12-manufacturing/flows/fl-f12-02-plan-production.md), [FL-F6-02](../../flows/fl-f06-02-quote-to-order.md), [FL-F6-03](../../flows/fl-f06-03-invoice-and-get-paid.md), [FL-F6-06](../../flows/fl-f06-06-accounts-and-credit.md), [FL-F6-07](../../flows/fl-f06-07-special-invoicing.md), [FL-F6-09](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-F7-03](../../../f07-purchasing-and-stock/flows/fl-f07-03-replenish.md), [FL-F7-04](../../../f07-purchasing-and-stock/flows/fl-f07-04-pick-pack-and-ship.md), [FL-SC02-03](../../../../08-sectors/sc02-retail/flows/fl-sc02-03-sell-and-return-across-channels.md), [FL-SC05-02](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-02-made-to-order.md) |

## Open questions

None.

---

⬅️ [S-F6-L03 Quotes](s-f06-l03-quotes.md) · ⬆️ [Up](README.md) · ➡️ [S-F6-L05 Invoices](s-f06-l05-invoices.md)
