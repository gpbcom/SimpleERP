🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L03 Purchase orders

# 🗂️ S-F7-L03 Purchase orders

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | as the permissions row "Purchase orders": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | as the permissions row "Purchase orders": read the orders of their own requests (UC-F7-01) | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Purchase orders": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | as the permissions row "Purchase orders": read, to match supplier invoices (UC-F7-04) | actions as [permissions](../../permissions.md) gives them |
| [U10 Supplier](../../../../01-users/personas/u10-supplier.md) | as the permissions row "Purchase orders": confirm | actions as [permissions](../../permissions.md) gives them |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U15: their permissions in the capability's matrix give them no access to these records.

**Not embedded for:** U54: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F7-03 Purchase order](../../data/e-f07-03-purchase-order.md) the user may see: to find,
filter, total and act on many purchase orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Purchase orders, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "purchase orders" offers this view.
- **AI assistant:** "show the purchase orders that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Purchase orders    Purchasing and stock › Purchase orders   [+ New]                                          |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| supplier          | [ ] NUMBER   STATE   SUPPLIER   EXPECTED DATE   LINES   KIND                             |
| lines             | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| State | state | badge: Draft, Sent, Confirmed, Received, Billed | yes |
| Supplier | supplier | text | yes |
| Expected date | expected date | date | yes |
| Lines | lines | text | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Supplier | each value | the visible rows (D488) |
| Lines | each value | the visible rows (D488) |
| Kind | standard, blanket, dropship | the visible rows (D488) |
| State | Draft, Sent, Confirmed, Received, Billed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Purchase orders of a chosen supplier, or of the suppliers that match a filter.
- From the other side: the suppliers that have purchase orders, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by expected date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New purchase order | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- lines: editable in its cell unless the record's state locks it.
- expected date: editable in its cell unless the record's state locks it.
- kind: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-01 Purchase request](../01-procure/s-f07-01-purchase-request.md).

The records also show on: [S-F7-02 Purchase order](../01-procure/s-f07-02-purchase-order.md),
[S-F7-04 Supplier invoice matching](../01-procure/s-f07-04-supplier-invoice-matching.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 purchase orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no purchase order the user may see yet, with the create action when allowed.
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
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l03-purchase-orders-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l03-purchase-orders-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u04-purchasing-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f07-l03-purchase-orders-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f07-l03-purchase-orders-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u01-employee-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f07-l03-purchase-orders-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f07-l03-purchase-orders-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f07-l03-purchase-orders-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f07-l03-purchase-orders-u02-manager-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f07-l03-purchase-orders-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f07-l03-purchase-orders-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u05-accounting-phone-dark.png) |
| Listed, U10, view All | desktop | ![Listed, U10, view All, light](../../images/lists/s-f07-l03-purchase-orders-u10-supplier-desktop-light.png) | ![Listed, U10, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u10-supplier-desktop-dark.png) |
| Listed, U10, view All | phone | ![Listed, U10, view All, light](../../images/lists/s-f07-l03-purchase-orders-u10-supplier-phone-light.png) | ![Listed, U10, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u10-supplier-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f07-l03-purchase-orders-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f07-l03-purchase-orders-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u09-customer-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f07-l03-purchase-orders-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f07-l03-purchase-orders-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f07-l03-purchase-orders-u23-store-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Purchase orders](README.md) |
| Workspaces | [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U10](../../../../04-ux/views/u10-supplier/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md) |
| Flows | [FL-F12-05](../../../f12-manufacturing/flows/fl-f12-05-subcontracting-and-costs.md), [FL-F7-01](../../flows/fl-f07-01-procure.md), [FL-F7-02](../../flows/fl-f07-02-receive-and-store.md), [FL-F7-03](../../flows/fl-f07-03-replenish.md), [FL-F7-07](../../flows/fl-f07-07-supplier-agreements-and-performance.md), [FL-F7-09](../../flows/fl-f07-09-compliance-and-carbon.md), [FL-SC15-02](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-02-orders.md) |

## Open questions

None.

---

⬅️ [S-F7-L02 Purchase requests](s-f07-l02-purchase-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L04 Transfers](s-f07-l04-transfers.md)
