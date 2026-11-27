🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L05 Invoices

# 🗂️ S-F6-L05 Invoices

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | as the permissions row "Invoices, credit notes": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | as the permissions row "Invoices, credit notes": pay, download | actions as [permissions](../../permissions.md) gives them |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | as the permissions row "Invoices, credit notes": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | as the permissions row "Invoices, credit notes": read their own customers' invoices (UC-F6-24) | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Invoices, credit notes": read their team's invoices (UC-F6-26) | actions as [permissions](../../permissions.md) gives them |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Invoices, credit notes": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U34 Property manager](../../../../01-users/personas/u34-property-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U12, U51, U52: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-F6-05 Invoice](../../data/e-f06-05-invoice.md) the user may see: to find, filter, total
and act on many invoices at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Invoices, in the capability's menu (D495).
- **Workspaces:** 21 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "invoices" offers this view.
- **AI assistant:** "show the invoices that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Invoices    Customers and sales › Invoices   [+ New]                                                         |
| [count] [total retention] [Draft] [due in 7 days]   [chart: count by state, retention stacked]               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| kind              | [ ] NUMBER   E-INVOICING STATUS   STATE   RETENTION   TOTALS   DUE DATE   KIND           |
| e-invoicing statu | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| E-invoicing status | e-invoicing status | badge | yes |
| State | state | badge: Sent, Received, Paid, Draft, Issued, PartlyPaid, Overdue, Refused | yes |
| Retention | retention | amount, right-aligned | yes |
| Totals | totals | amount, right-aligned | yes |
| Due date | due date | date | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Kind | deposit, progress, final, credit note, subscription | the visible rows (D488) |
| E-invoicing status | sent, received, refused, paid | the visible rows (D488) |
| State | Sent, Received, Paid, Draft, Issued, PartlyPaid, Overdue, Refused | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: invoices link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of retention.
- Needs attention: count in the state Draft.
- Due in 7 days, by due date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, retention stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Open: Sent, Received, Draft.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New invoice | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- due date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F6-06 Invoice](../03-invoice-and-get-paid/s-f06-06-invoice.md).

The records also show on: [S-F6-04 Customer portal](../02-quote-to-order/s-f06-04-customer-portal.md),
[S-F6-08 Reminders](../03-invoice-and-get-paid/s-f06-08-reminders.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 invoices of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no invoice the user may see yet, with the create action when allowed.
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
| Listed, U05, view Open: Sent, Received, Draft | desktop | ![Listed, U05, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Sent, Received, Draft | phone | ![Listed, U05, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u05-accounting-phone-dark.png) |
| Listed, U09, view Open: Sent, Received, Draft | desktop | ![Listed, U09, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Sent, Received, Draft | phone | ![Listed, U09, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u09-customer-phone-light.png) | ![Listed, U09, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u09-customer-phone-dark.png) |
| Listed, U16, view Open: Sent, Received, Draft | desktop | ![Listed, U16, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: Sent, Received, Draft | phone | ![Listed, U16, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u16-office-worker-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u25-care-coordinator-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u38-training-coordinator-phone-dark.png) |
| Listed, U03, view Open: Sent, Received, Draft | desktop | ![Listed, U03, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Sent, Received, Draft | phone | ![Listed, U03, view Open: Sent, Received, Draft, light](../../images/lists/s-f06-l05-invoices-u03-sales-phone-light.png) | ![Listed, U03, view Open: Sent, Received, Draft, dark](../../images/lists/s-f06-l05-invoices-u03-sales-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u02-manager-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l05-invoices-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l05-invoices-u13-owner-phone-dark.png) |
| Listed, U04, view Open | desktop | ![Listed, U04, view Open, light](../../images/lists/s-f06-l05-invoices-u04-purchasing-desktop-light.png) | ![Listed, U04, view Open, dark](../../images/lists/s-f06-l05-invoices-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Open | phone | ![Listed, U04, view Open, light](../../images/lists/s-f06-l05-invoices-u04-purchasing-phone-light.png) | ![Listed, U04, view Open, dark](../../images/lists/s-f06-l05-invoices-u04-purchasing-phone-dark.png) |
| Listed, U14, view Open | desktop | ![Listed, U14, view Open, light](../../images/lists/s-f06-l05-invoices-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open, dark](../../images/lists/s-f06-l05-invoices-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open | phone | ![Listed, U14, view Open, light](../../images/lists/s-f06-l05-invoices-u14-field-worker-phone-light.png) | ![Listed, U14, view Open, dark](../../images/lists/s-f06-l05-invoices-u14-field-worker-phone-dark.png) |
| Listed, U15, view Open | desktop | ![Listed, U15, view Open, light](../../images/lists/s-f06-l05-invoices-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Open, dark](../../images/lists/s-f06-l05-invoices-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Open | phone | ![Listed, U15, view Open, light](../../images/lists/s-f06-l05-invoices-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Open, dark](../../images/lists/s-f06-l05-invoices-u15-warehouse-operator-phone-dark.png) |
| Listed, U23, view Open | desktop | ![Listed, U23, view Open, light](../../images/lists/s-f06-l05-invoices-u23-store-manager-desktop-light.png) | ![Listed, U23, view Open, dark](../../images/lists/s-f06-l05-invoices-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Open | phone | ![Listed, U23, view Open, light](../../images/lists/s-f06-l05-invoices-u23-store-manager-phone-light.png) | ![Listed, U23, view Open, dark](../../images/lists/s-f06-l05-invoices-u23-store-manager-phone-dark.png) |
| Listed, U30, view Open | desktop | ![Listed, U30, view Open, light](../../images/lists/s-f06-l05-invoices-u30-driver-desktop-light.png) | ![Listed, U30, view Open, dark](../../images/lists/s-f06-l05-invoices-u30-driver-desktop-dark.png) |
| Listed, U30, view Open | phone | ![Listed, U30, view Open, light](../../images/lists/s-f06-l05-invoices-u30-driver-phone-light.png) | ![Listed, U30, view Open, dark](../../images/lists/s-f06-l05-invoices-u30-driver-phone-dark.png) |
| Listed, U31, view Open | desktop | ![Listed, U31, view Open, light](../../images/lists/s-f06-l05-invoices-u31-treasurer-desktop-light.png) | ![Listed, U31, view Open, dark](../../images/lists/s-f06-l05-invoices-u31-treasurer-desktop-dark.png) |
| Listed, U31, view Open | phone | ![Listed, U31, view Open, light](../../images/lists/s-f06-l05-invoices-u31-treasurer-phone-light.png) | ![Listed, U31, view Open, dark](../../images/lists/s-f06-l05-invoices-u31-treasurer-phone-dark.png) |
| Listed, U34, view Open | desktop | ![Listed, U34, view Open, light](../../images/lists/s-f06-l05-invoices-u34-property-manager-desktop-light.png) | ![Listed, U34, view Open, dark](../../images/lists/s-f06-l05-invoices-u34-property-manager-desktop-dark.png) |
| Listed, U34, view Open | phone | ![Listed, U34, view Open, light](../../images/lists/s-f06-l05-invoices-u34-property-manager-phone-light.png) | ![Listed, U34, view Open, dark](../../images/lists/s-f06-l05-invoices-u34-property-manager-phone-dark.png) |
| Listed, U35, view Open | desktop | ![Listed, U35, view Open, light](../../images/lists/s-f06-l05-invoices-u35-real-estate-agent-desktop-light.png) | ![Listed, U35, view Open, dark](../../images/lists/s-f06-l05-invoices-u35-real-estate-agent-desktop-dark.png) |
| Listed, U35, view Open | phone | ![Listed, U35, view Open, light](../../images/lists/s-f06-l05-invoices-u35-real-estate-agent-phone-light.png) | ![Listed, U35, view Open, dark](../../images/lists/s-f06-l05-invoices-u35-real-estate-agent-phone-dark.png) |
| Listed, U40, view Open | desktop | ![Listed, U40, view Open, light](../../images/lists/s-f06-l05-invoices-u40-farmer-desktop-light.png) | ![Listed, U40, view Open, dark](../../images/lists/s-f06-l05-invoices-u40-farmer-desktop-dark.png) |
| Listed, U40, view Open | phone | ![Listed, U40, view Open, light](../../images/lists/s-f06-l05-invoices-u40-farmer-phone-light.png) | ![Listed, U40, view Open, dark](../../images/lists/s-f06-l05-invoices-u40-farmer-phone-dark.png) |
| Listed, U41, view Open | desktop | ![Listed, U41, view Open, light](../../images/lists/s-f06-l05-invoices-u41-customer-success-manager-desktop-light.png) | ![Listed, U41, view Open, dark](../../images/lists/s-f06-l05-invoices-u41-customer-success-manager-desktop-dark.png) |
| Listed, U41, view Open | phone | ![Listed, U41, view Open, light](../../images/lists/s-f06-l05-invoices-u41-customer-success-manager-phone-light.png) | ![Listed, U41, view Open, dark](../../images/lists/s-f06-l05-invoices-u41-customer-success-manager-phone-dark.png) |
| Listed, U42, view Open | desktop | ![Listed, U42, view Open, light](../../images/lists/s-f06-l05-invoices-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Open, dark](../../images/lists/s-f06-l05-invoices-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Open | phone | ![Listed, U42, view Open, light](../../images/lists/s-f06-l05-invoices-u42-sales-representative-phone-light.png) | ![Listed, U42, view Open, dark](../../images/lists/s-f06-l05-invoices-u42-sales-representative-phone-dark.png) |
| Listed, U43, view Open | desktop | ![Listed, U43, view Open, light](../../images/lists/s-f06-l05-invoices-u43-event-producer-desktop-light.png) | ![Listed, U43, view Open, dark](../../images/lists/s-f06-l05-invoices-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Open | phone | ![Listed, U43, view Open, light](../../images/lists/s-f06-l05-invoices-u43-event-producer-phone-light.png) | ![Listed, U43, view Open, dark](../../images/lists/s-f06-l05-invoices-u43-event-producer-phone-dark.png) |
| Listed, U54, view Open | desktop | ![Listed, U54, view Open, light](../../images/lists/s-f06-l05-invoices-u54-public-finance-officer-desktop-light.png) | ![Listed, U54, view Open, dark](../../images/lists/s-f06-l05-invoices-u54-public-finance-officer-desktop-dark.png) |
| Listed, U54, view Open | phone | ![Listed, U54, view Open, light](../../images/lists/s-f06-l05-invoices-u54-public-finance-officer-phone-light.png) | ![Listed, U54, view Open, dark](../../images/lists/s-f06-l05-invoices-u54-public-finance-officer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Invoices](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U34](../../../../04-ux/views/u34-property-manager/workspace.md), [U35](../../../../04-ux/views/u35-real-estate-agent/workspace.md), [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U41](../../../../04-ux/views/u41-customer-success-manager/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U54](../../../../04-ux/views/u54-public-finance-officer/workspace.md) |
| Flows | [FL-F1-14](../../../f01-administration/flows/fl-f01-14-close-a-company.md), [FL-F10-02](../../../f10-point-of-sale/flows/fl-f10-02-sell-at-the-counter.md), [FL-F11-02](../../../f11-online-shop/flows/fl-f11-02-shop-and-check-out.md), [FL-F21-05](../../../f21-onboarding-and-modules/flows/fl-f21-05-migration-from-another-tool.md), [FL-F6-02](../../flows/fl-f06-02-quote-to-order.md), [FL-F6-03](../../flows/fl-f06-03-invoice-and-get-paid.md), [FL-F6-04](../../flows/fl-f06-04-subscriptions.md), [FL-F6-07](../../flows/fl-f06-07-special-invoicing.md), [FL-F6-08](../../flows/fl-f06-08-collect-and-settle.md), [FL-F6-09](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-F7-09](../../../f07-purchasing-and-stock/flows/fl-f07-09-compliance-and-carbon.md), [FL-F9-03](../../../f09-hr-and-projects/flows/fl-f09-03-time.md), [FL-F9-06](../../../f09-hr-and-projects/flows/fl-f09-06-plan-and-deliver-work.md), [FL-F9-11](../../../f09-hr-and-projects/flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-SC01-01](../../../../08-sectors/sc01-construction/flows/fl-sc01-01-win-the-work.md), [FL-SC01-04](../../../../08-sectors/sc01-construction/flows/fl-sc01-04-bill-and-subcontract.md), [FL-SC10-03](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-03-lettings.md), [FL-SC15-03](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-03-warehouse.md) |

## Open questions

None.

---

⬅️ [S-F6-L04 Orders](s-f06-l04-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L06 Customer payments](s-f06-l06-customer-payments.md)
