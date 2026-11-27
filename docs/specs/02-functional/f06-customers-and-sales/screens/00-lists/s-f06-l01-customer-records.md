🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L01 Customer records

# 🗂️ S-F6-L01 Customer records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U18 Waiter](../../../../01-users/personas/u18-waiter.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U01, U04, U12, U16, U22, U24, U27, U29, U33, U34, U35, U36: their use cases only read these
records, inside a screen of the use case, so they open them from there (D493).

**Not embedded for:** U38, U39, U43, U53: their use cases only read these records, inside a screen of the use case, so
they open them from there (D493).

## Purpose

The aggregated list of every [E-F6-01 Customer record](../../data/e-f06-01-customer-record.md) the user may see: to
find, filter, total and act on many customer records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Customer records, in the capability's menu (D495).
- **Workspaces:** 11 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "customer records" offers this view.
- **AI assistant:** "show the customer records that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Customer records    Customers and sales › Customer records   [+ New]                                         |
| [count] [total price list]   [chart: count by state, price list stacked]                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   PRICE LIST   KIND                                                     |
| kind              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Accepted, Active | yes |
| Price list | price list | amount, right-aligned | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Accepted, Active | the visible rows (D488) |
| Kind | company, person | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: customer records link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price list.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price list stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** address.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New customer record | header | the personas whose roles may create it | the record's own page (Row opens) |
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

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| name | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| contacts | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F6-04 Customer portal](../02-quote-to-order/s-f06-04-customer-portal.md).

The records also show on: [S-F6-02 Lead](../01-lead-to-quote/s-f06-02-lead.md),
[S-F10-24 Clienteling](../../../f10-point-of-sale/screens/10-clienteling-transfers-and-tax-free/s-f10-24-clienteling.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 customer records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no customer record the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

On the map layout, Listed also shows the count of rows without a place.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491); the map takes the full width.

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button. The table holds the
same rows as the map.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f06-l01-customer-records-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l01-customer-records-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f06-l01-customer-records-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f06-l01-customer-records-u09-customer-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f06-l01-customer-records-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l01-customer-records-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f06-l01-customer-records-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l01-customer-records-u03-sales-phone-dark.png) |
| Listed, U17, view All | desktop | ![Listed, U17, view All, light](../../images/lists/s-f06-l01-customer-records-u17-cashier-desktop-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f06-l01-customer-records-u17-cashier-desktop-dark.png) |
| Listed, U17, view All | phone | ![Listed, U17, view All, light](../../images/lists/s-f06-l01-customer-records-u17-cashier-phone-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f06-l01-customer-records-u17-cashier-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f06-l01-customer-records-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f06-l01-customer-records-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f06-l01-customer-records-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f06-l01-customer-records-u23-store-manager-phone-dark.png) |
| Listed, U41, view All | desktop | ![Listed, U41, view All, light](../../images/lists/s-f06-l01-customer-records-u41-customer-success-manager-desktop-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f06-l01-customer-records-u41-customer-success-manager-desktop-dark.png) |
| Listed, U41, view All | phone | ![Listed, U41, view All, light](../../images/lists/s-f06-l01-customer-records-u41-customer-success-manager-phone-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f06-l01-customer-records-u41-customer-success-manager-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f06-l01-customer-records-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l01-customer-records-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f06-l01-customer-records-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l01-customer-records-u02-manager-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f06-l01-customer-records-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f06-l01-customer-records-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f06-l01-customer-records-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f06-l01-customer-records-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f06-l01-customer-records-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l01-customer-records-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f06-l01-customer-records-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f06-l01-customer-records-u13-owner-phone-dark.png) |
| Listed, U18, view All | desktop | ![Listed, U18, view All, light](../../images/lists/s-f06-l01-customer-records-u18-waiter-desktop-light.png) | ![Listed, U18, view All, dark](../../images/lists/s-f06-l01-customer-records-u18-waiter-desktop-dark.png) |
| Listed, U18, view All | phone | ![Listed, U18, view All, light](../../images/lists/s-f06-l01-customer-records-u18-waiter-phone-light.png) | ![Listed, U18, view All, dark](../../images/lists/s-f06-l01-customer-records-u18-waiter-phone-dark.png) |
| Listed, U28, view All | desktop | ![Listed, U28, view All, light](../../images/lists/s-f06-l01-customer-records-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view All, dark](../../images/lists/s-f06-l01-customer-records-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view All | phone | ![Listed, U28, view All, light](../../images/lists/s-f06-l01-customer-records-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view All, dark](../../images/lists/s-f06-l01-customer-records-u28-hotel-receptionist-phone-dark.png) |
| Listed, U52, view All | desktop | ![Listed, U52, view All, light](../../images/lists/s-f06-l01-customer-records-u52-beautician-desktop-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-f06-l01-customer-records-u52-beautician-desktop-dark.png) |
| Listed, U52, view All | phone | ![Listed, U52, view All, light](../../images/lists/s-f06-l01-customer-records-u52-beautician-phone-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-f06-l01-customer-records-u52-beautician-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Customer records](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U41](../../../../04-ux/views/u41-customer-success-manager/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U18](../../../../04-ux/views/u18-waiter/workspace.md), [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md) |
| Flows | [FL-F1-12](../../../f01-administration/flows/fl-f01-12-portal-accounts-and-integrations.md), [FL-F10-10](../../../f10-point-of-sale/flows/fl-f10-10-clienteling-transfers-and-tax-free.md), [FL-F21-05](../../../f21-onboarding-and-modules/flows/fl-f21-05-migration-from-another-tool.md), [FL-F6-01](../../flows/fl-f06-01-lead-to-quote.md), [FL-F6-02](../../flows/fl-f06-02-quote-to-order.md), [FL-F6-04](../../flows/fl-f06-04-subscriptions.md), [FL-F6-06](../../flows/fl-f06-06-accounts-and-credit.md) |

## Open questions

None.

---

⬅️ [S-F6-28 Warranty claims](../10-partners-contracts-and-warranties/s-f06-28-warranty-claims.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L02 Opportunities](s-f06-l02-opportunities.md)
