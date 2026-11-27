🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L07 Subscription contracts

# 🗂️ S-F6-L07 Subscription contracts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U14, U40: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F6-07 Subscription contract](../../data/e-f06-07-subscription-contract.md) the user may
see: to find, filter, total and act on many subscription contracts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Subscription contracts, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "subscription contracts" offers this view.
- **AI assistant:** "show the subscription contracts that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Subscription contracts    Customers and sales › Subscription contracts   [+ New]                             |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CUSTOMER   STATE   PERIOD   LINES                                                    |
| customer          | [ ] ...                                                  Open >                          |
| lines             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Customer | customer | text | yes |
| State | state | badge: Active | yes |
| Period | period | label | yes |
| Lines | lines | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Customer | each value | the visible rows (D488) |
| Lines | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Subscription contracts of a chosen customer, or of the customers that match a filter.
- From the other side: the customers that have subscription contracts, or none.

## KPI strip

- Count of the visible rows.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New subscription contract | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- lines: editable in its cell unless the record's state locks it.
- period: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F6-09 Subscriptions](../04-subscriptions/s-f06-09-subscriptions.md).

The records also show on: [S-F6-04 Customer portal](../02-quote-to-order/s-f06-04-customer-portal.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 subscription contracts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no subscription contract the user may see yet, with the create action when allowed.
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
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u03-sales-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u05-accounting-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u09-customer-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u13-owner-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u23-store-manager-phone-dark.png) |
| Listed, U41, view All | desktop | ![Listed, U41, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u41-customer-success-manager-desktop-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u41-customer-success-manager-desktop-dark.png) |
| Listed, U41, view All | phone | ![Listed, U41, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u41-customer-success-manager-phone-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u41-customer-success-manager-phone-dark.png) |
| Listed, U52, view All | desktop | ![Listed, U52, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u52-beautician-desktop-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u52-beautician-desktop-dark.png) |
| Listed, U52, view All | phone | ![Listed, U52, view All, light](../../images/lists/s-f06-l07-subscription-contracts-u52-beautician-phone-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-f06-l07-subscription-contracts-u52-beautician-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Subscription contracts](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U41](../../../../04-ux/views/u41-customer-success-manager/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md) |
| Flows | [FL-F1-14](../../../f01-administration/flows/fl-f01-14-close-a-company.md), [FL-F11-04](../../../f11-online-shop/flows/fl-f11-04-special-sales.md), [FL-F6-02](../../flows/fl-f06-02-quote-to-order.md), [FL-F6-03](../../flows/fl-f06-03-invoice-and-get-paid.md), [FL-F6-04](../../flows/fl-f06-04-subscriptions.md), [FL-SC14-03](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-03-support-and-services.md) |

## Open questions

None.

---

⬅️ [S-F6-L06 Customer payments](s-f06-l06-customer-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L08 Sales price lists](s-f06-l08-sales-price-lists.md)
