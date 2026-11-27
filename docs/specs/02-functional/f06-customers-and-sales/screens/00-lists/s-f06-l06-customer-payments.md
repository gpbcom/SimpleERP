🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L06 Customer payments

# 🗂️ S-F6-L06 Customer payments

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U53 Coach](../../../../01-users/personas/u53-coach.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U12, U23, U56: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-F6-06 Customer payment](../../data/e-f06-06-customer-payment.md) the user may see: to
find, filter, total and act on many customer payments at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Customer payments, in the capability's menu (D495).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "customer payments" offers this view.
- **AI assistant:** "show the customer payments that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Customer payments    Customers and sales › Customer payments   [+ New]                                       |
| [count] [total amount]   [chart: count by state, amount stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] AMOUNT   STATE                                                                       |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Amount | amount | amount, right-aligned | yes |
| State | state | badge: Matched, Refused | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Matched, Refused | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: customer payments link to no other record type in their fields.

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
| New customer payment | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to
[S-F6-07 Payments and reconciliation](../03-invoice-and-get-paid/s-f06-07-payments-and-reconciliation.md).

The records also show on: [S-F6-06 Invoice](../03-invoice-and-get-paid/s-f06-06-invoice.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 customer payments of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no customer payment the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f06-l06-customer-payments-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f06-l06-customer-payments-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f06-l06-customer-payments-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f06-l06-customer-payments-u05-accounting-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f06-l06-customer-payments-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l06-customer-payments-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f06-l06-customer-payments-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l06-customer-payments-u09-customer-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f06-l06-customer-payments-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f06-l06-customer-payments-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f06-l06-customer-payments-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f06-l06-customer-payments-u04-purchasing-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f06-l06-customer-payments-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l06-customer-payments-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f06-l06-customer-payments-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l06-customer-payments-u13-owner-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-f06-l06-customer-payments-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f06-l06-customer-payments-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-f06-l06-customer-payments-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f06-l06-customer-payments-u31-treasurer-phone-dark.png) |
| Listed, U40, view All | desktop | ![Listed, U40, view All, light](../../images/lists/s-f06-l06-customer-payments-u40-farmer-desktop-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-f06-l06-customer-payments-u40-farmer-desktop-dark.png) |
| Listed, U40, view All | phone | ![Listed, U40, view All, light](../../images/lists/s-f06-l06-customer-payments-u40-farmer-phone-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-f06-l06-customer-payments-u40-farmer-phone-dark.png) |
| Listed, U42, view All | desktop | ![Listed, U42, view All, light](../../images/lists/s-f06-l06-customer-payments-u42-sales-representative-desktop-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-f06-l06-customer-payments-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view All | phone | ![Listed, U42, view All, light](../../images/lists/s-f06-l06-customer-payments-u42-sales-representative-phone-light.png) | ![Listed, U42, view All, dark](../../images/lists/s-f06-l06-customer-payments-u42-sales-representative-phone-dark.png) |
| Listed, U53, view All | desktop | ![Listed, U53, view All, light](../../images/lists/s-f06-l06-customer-payments-u53-coach-desktop-light.png) | ![Listed, U53, view All, dark](../../images/lists/s-f06-l06-customer-payments-u53-coach-desktop-dark.png) |
| Listed, U53, view All | phone | ![Listed, U53, view All, light](../../images/lists/s-f06-l06-customer-payments-u53-coach-phone-light.png) | ![Listed, U53, view All, dark](../../images/lists/s-f06-l06-customer-payments-u53-coach-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Customer payments](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U53](../../../../04-ux/views/u53-coach/workspace.md) |
| Flows | [FL-F11-03](../../../f11-online-shop/flows/fl-f11-03-after-the-order.md), [FL-F19-05](../../../f19-feature-factory/flows/fl-f19-05-bill-and-credit.md), [FL-F24-06](../../../f24-integrations-hub/flows/fl-f24-06-business-tools.md), [FL-F6-03](../../flows/fl-f06-03-invoice-and-get-paid.md), [FL-F6-04](../../flows/fl-f06-04-subscriptions.md), [FL-F6-06](../../flows/fl-f06-06-accounts-and-credit.md), [FL-F8-03](../../../f08-accounting/flows/fl-f08-03-bank-and-collect.md), [FL-SC01-04](../../../../08-sectors/sc01-construction/flows/fl-sc01-04-bill-and-subcontract.md), [FL-SC06-05](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-05-taxes-and-performance.md), [FL-SC09-03](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-03-insurance-billing.md), [FL-SC09-05](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-05-practice-organisation.md), [FL-SC10-04](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-04-rents-and-landlords.md), [FL-SC13-04](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-04-sales-and-certification.md), [FL-SC14-01](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-01-subscriptions-and-billing.md), [FL-SC16-02](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-02-ticketing.md) |

## Open questions

None.

---

⬅️ [S-F6-L05 Invoices](s-f06-l05-invoices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L07 Subscription contracts](s-f06-l07-subscription-contracts.md)
