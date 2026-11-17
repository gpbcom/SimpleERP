🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L03 Point of sale orders

# 🗂️ S-F10-L03 Point of sale orders

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U18 Waiter](../../../../01-users/personas/u18-waiter.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U28: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md) the user may
see: to find, filter, total and act on many point of sale orders at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Point of sale orders, in the capability's menu (D495).
- **Workspaces:** 11 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "point of sale orders" offers this view.
- **AI assistant:** "show the point of sale orders that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Point of sale orders    Point of sale (plugin) › Point of sale orders   [+ New]                              |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| channel           | [ ] NUMBER   STATE   CUSTOMER   CHANNEL                                                  |
| customer          | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| State | state | badge: Draft, Paid, Invoiced, Refunded | yes |
| Customer | customer | person's name | yes |
| Channel | channel | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Channel | till, table, QR, kiosk, mobile, delivery | the visible rows (D488) |
| Customer | each person, the user first | the visible rows (D488) |
| State | Draft, Paid, Invoiced, Refunded | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: point of sale orders link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: customer.
- Open: Draft, Invoiced, Refunded.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New point of sale order | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the customer; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- channel: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| customer | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F10-02 Till](../02-sell-at-the-counter/s-f10-02-till.md).

The records also show on: [S-F10-03 Payment](../02-sell-at-the-counter/s-f10-03-payment.md),
[S-F10-04 Refund](../03-after-sales/s-f10-04-refund.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 point of sale orders of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no point of sale order the user may see yet, with the create action when allowed.
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
| Listed, U17, view Mine: customer | desktop | ![Listed, U17, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u17-cashier-desktop-light.png) | ![Listed, U17, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u17-cashier-desktop-dark.png) |
| Listed, U17, view Mine: customer | phone | ![Listed, U17, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u17-cashier-phone-light.png) | ![Listed, U17, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u17-cashier-phone-dark.png) |
| Listed, U09, view Mine: customer | desktop | ![Listed, U09, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: customer | phone | ![Listed, U09, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u09-customer-phone-light.png) | ![Listed, U09, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u09-customer-phone-dark.png) |
| Listed, U18, view Mine: customer | desktop | ![Listed, U18, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u18-waiter-desktop-light.png) | ![Listed, U18, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u18-waiter-desktop-dark.png) |
| Listed, U18, view Mine: customer | phone | ![Listed, U18, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u18-waiter-phone-light.png) | ![Listed, U18, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u18-waiter-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f10-l03-point-of-sale-orders-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f10-l03-point-of-sale-orders-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u02-manager-phone-dark.png) |
| Listed, U19, view Mine: customer | desktop | ![Listed, U19, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u19-kitchen-staff-desktop-light.png) | ![Listed, U19, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u19-kitchen-staff-desktop-dark.png) |
| Listed, U19, view Mine: customer | phone | ![Listed, U19, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u19-kitchen-staff-phone-light.png) | ![Listed, U19, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u19-kitchen-staff-phone-dark.png) |
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f10-l03-point-of-sale-orders-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-f10-l03-point-of-sale-orders-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u23-store-manager-phone-dark.png) |
| Listed, U14, view Mine: customer | desktop | ![Listed, U14, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: customer | phone | ![Listed, U14, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u14-field-worker-phone-dark.png) |
| Listed, U15, view Mine: customer | desktop | ![Listed, U15, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Mine: customer | phone | ![Listed, U15, view Mine: customer, light](../../images/lists/s-f10-l03-point-of-sale-orders-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Mine: customer, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u15-warehouse-operator-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f10-l03-point-of-sale-orders-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f10-l03-point-of-sale-orders-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u13-owner-phone-dark.png) |
| Listed, U52, view Mine | desktop | ![Listed, U52, view Mine, light](../../images/lists/s-f10-l03-point-of-sale-orders-u52-beautician-desktop-light.png) | ![Listed, U52, view Mine, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u52-beautician-desktop-dark.png) |
| Listed, U52, view Mine | phone | ![Listed, U52, view Mine, light](../../images/lists/s-f10-l03-point-of-sale-orders-u52-beautician-phone-light.png) | ![Listed, U52, view Mine, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u52-beautician-phone-dark.png) |
| Listed, U53, view Mine | desktop | ![Listed, U53, view Mine, light](../../images/lists/s-f10-l03-point-of-sale-orders-u53-coach-desktop-light.png) | ![Listed, U53, view Mine, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u53-coach-desktop-dark.png) |
| Listed, U53, view Mine | phone | ![Listed, U53, view Mine, light](../../images/lists/s-f10-l03-point-of-sale-orders-u53-coach-phone-light.png) | ![Listed, U53, view Mine, dark](../../images/lists/s-f10-l03-point-of-sale-orders-u53-coach-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Point of sale orders](README.md) |
| Workspaces | [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U18](../../../../04-ux/views/u18-waiter/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U19](../../../../04-ux/views/u19-kitchen-staff/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md) |
| Flows | [FL-F10-02](../../flows/fl-f10-02-sell-at-the-counter.md), [FL-F10-03](../../flows/fl-f10-03-after-sales.md), [FL-F10-04](../../flows/fl-f10-04-restaurant-service.md), [FL-F10-05](../../flows/fl-f10-05-self-order-and-kiosk.md), [FL-F10-06](../../flows/fl-f10-06-mobile-and-delivery.md), [FL-F10-07](../../flows/fl-f10-07-set-up-and-report.md), [FL-F10-08](../../flows/fl-f10-08-vouchers-and-age-checks.md), [FL-F10-10](../../flows/fl-f10-10-clienteling-transfers-and-tax-free.md), [FL-F10-11](../../flows/fl-f10-11-store-reports.md), [FL-SC02-04](../../../../08-sectors/sc02-retail/flows/fl-sc02-04-customers-and-staff.md), [FL-SC11-02](../../../../08-sectors/sc11-professional-firms/flows/fl-sc11-02-matters-and-documents.md), [FL-SC16-04](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-04-on-site.md) |

## Open questions

None.

---

⬅️ [S-F10-L02 Till sessions](s-f10-l02-till-sessions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L04 Till payments](s-f10-l04-till-payments.md)
