🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L03 Quotes

# 🗂️ S-F6-L03 Quotes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | as the permissions row "Quotes": accept, sign | actions as [permissions](../../permissions.md) gives them |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | as the permissions row "Quotes": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Quotes": ✅ approve discounts | actions as [permissions](../../permissions.md) gives them |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Quotes": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U34 Property manager](../../../../01-users/personas/u34-property-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- The owner's review (VC-14, D519): "Add Manager, Owner, and Planner here at the very least."
- The planner personas are the ready-made planner roles of E-F1-06 Role (D517).

## Purpose

The aggregated list of every [E-F6-03 Quote](../../data/e-f06-03-quote.md) the user may see: to find, filter, total and
act on many quotes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Quotes, in the capability's menu (D495).
- **Workspaces:** 16 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "quotes" offers this view.
- **AI assistant:** "show the quotes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Quotes    Customers and sales › Quotes   [+ New]                                                             |
| [count] [total totals] [Draft] [new this month]   [chart: count by state, totals stacked]                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NUMBER   STATE   TOTALS   VALID UNTIL   VERSION                                      |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| State | state | badge: Draft, ToApprove, Sent, Accepted, Refused, Expired | yes |
| Totals | totals | amount, right-aligned | yes |
| Valid until | valid until | date | yes |
| Version | version | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, ToApprove, Sent, Accepted, Refused, Expired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: quotes link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of totals.
- Needs attention: count in the state Draft.
- New this month, by valid until.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, totals stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Draft, ToApprove, Sent.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New quote | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- version: editable in its cell unless the record's state locks it.
- valid until: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| acceptance proof | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F6-03 Quote editor](../01-lead-to-quote/s-f06-03-quote-editor.md).

The records also show on: [S-F6-04 Customer portal](../02-quote-to-order/s-f06-04-customer-portal.md),
[S-F11-11 B2B access](../../../f11-online-shop/screens/04-special-sales/s-f11-11-b2b-access.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 quotes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no quote the user may see yet, with the create action when allowed.
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
| Listed, U09, view Open: Draft, ToApprove, Sent | desktop | ![Listed, U09, view Open: Draft, ToApprove, Sent, light](../../images/lists/s-f06-l03-quotes-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, ToApprove, Sent, dark](../../images/lists/s-f06-l03-quotes-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, ToApprove, Sent | phone | ![Listed, U09, view Open: Draft, ToApprove, Sent, light](../../images/lists/s-f06-l03-quotes-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, ToApprove, Sent, dark](../../images/lists/s-f06-l03-quotes-u09-customer-phone-dark.png) |
| Listed, U03, view Open: Draft, ToApprove, Sent | desktop | ![Listed, U03, view Open: Draft, ToApprove, Sent, light](../../images/lists/s-f06-l03-quotes-u03-sales-desktop-light.png) | ![Listed, U03, view Open: Draft, ToApprove, Sent, dark](../../images/lists/s-f06-l03-quotes-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: Draft, ToApprove, Sent | phone | ![Listed, U03, view Open: Draft, ToApprove, Sent, light](../../images/lists/s-f06-l03-quotes-u03-sales-phone-light.png) | ![Listed, U03, view Open: Draft, ToApprove, Sent, dark](../../images/lists/s-f06-l03-quotes-u03-sales-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u02-manager-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u13-owner-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u29-dispatcher-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u25-care-coordinator-phone-dark.png) |
| Listed, U22, view Needs attention | desktop | ![Listed, U22, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u22-site-manager-desktop-light.png) | ![Listed, U22, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u22-site-manager-desktop-dark.png) |
| Listed, U22, view Needs attention | phone | ![Listed, U22, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u22-site-manager-phone-light.png) | ![Listed, U22, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u22-site-manager-phone-dark.png) |
| Listed, U24, view Needs attention | desktop | ![Listed, U24, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u24-engagement-manager-desktop-light.png) | ![Listed, U24, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u24-engagement-manager-desktop-dark.png) |
| Listed, U24, view Needs attention | phone | ![Listed, U24, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u24-engagement-manager-phone-light.png) | ![Listed, U24, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u24-engagement-manager-phone-dark.png) |
| Listed, U21, view Needs attention | desktop | ![Listed, U21, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u21-production-planner-desktop-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u21-production-planner-desktop-dark.png) |
| Listed, U21, view Needs attention | phone | ![Listed, U21, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u21-production-planner-phone-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u21-production-planner-phone-dark.png) |
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u23-store-manager-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u38-training-coordinator-phone-dark.png) |
| Listed, U34, view Needs attention | desktop | ![Listed, U34, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u34-property-manager-desktop-light.png) | ![Listed, U34, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u34-property-manager-desktop-dark.png) |
| Listed, U34, view Needs attention | phone | ![Listed, U34, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u34-property-manager-phone-light.png) | ![Listed, U34, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u34-property-manager-phone-dark.png) |
| Listed, U43, view Needs attention | desktop | ![Listed, U43, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u43-event-producer-desktop-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Needs attention | phone | ![Listed, U43, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u43-event-producer-phone-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u43-event-producer-phone-dark.png) |
| Listed, U28, view Needs attention | desktop | ![Listed, U28, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u28-hotel-receptionist-desktop-light.png) | ![Listed, U28, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u28-hotel-receptionist-desktop-dark.png) |
| Listed, U28, view Needs attention | phone | ![Listed, U28, view Needs attention, light](../../images/lists/s-f06-l03-quotes-u28-hotel-receptionist-phone-light.png) | ![Listed, U28, view Needs attention, dark](../../images/lists/s-f06-l03-quotes-u28-hotel-receptionist-phone-dark.png) |
| Listed, U14, view Open | desktop | ![Listed, U14, view Open, light](../../images/lists/s-f06-l03-quotes-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open, dark](../../images/lists/s-f06-l03-quotes-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open | phone | ![Listed, U14, view Open, light](../../images/lists/s-f06-l03-quotes-u14-field-worker-phone-light.png) | ![Listed, U14, view Open, dark](../../images/lists/s-f06-l03-quotes-u14-field-worker-phone-dark.png) |
| Listed, U19, view Open | desktop | ![Listed, U19, view Open, light](../../images/lists/s-f06-l03-quotes-u19-kitchen-staff-desktop-light.png) | ![Listed, U19, view Open, dark](../../images/lists/s-f06-l03-quotes-u19-kitchen-staff-desktop-dark.png) |
| Listed, U19, view Open | phone | ![Listed, U19, view Open, light](../../images/lists/s-f06-l03-quotes-u19-kitchen-staff-phone-light.png) | ![Listed, U19, view Open, dark](../../images/lists/s-f06-l03-quotes-u19-kitchen-staff-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Quotes](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U22](../../../../04-ux/views/u22-site-manager/workspace.md), [U24](../../../../04-ux/views/u24-engagement-manager/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U34](../../../../04-ux/views/u34-property-manager/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md), [U28](../../../../04-ux/views/u28-hotel-receptionist/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U19](../../../../04-ux/views/u19-kitchen-staff/workspace.md) |
| Flows | [FL-F11-09](../../../f11-online-shop/flows/fl-f11-09-pre-orders-and-b2b-buying.md), [FL-F17-05](../../../f17-competitive-analysis/flows/fl-f17-05-tender-watch.md), [FL-F19-01](../../../f19-feature-factory/flows/fl-f19-01-describe-and-order.md), [FL-F19-06](../../../f19-feature-factory/flows/fl-f19-06-delivery-and-refunds.md), [FL-F2-11](../../../f02-no-code-configuration/flows/fl-f02-11-rights-translations-and-approvals.md), [FL-F6-01](../../flows/fl-f06-01-lead-to-quote.md), [FL-F6-02](../../flows/fl-f06-02-quote-to-order.md), [FL-F6-04](../../flows/fl-f06-04-subscriptions.md), [FL-F6-05](../../flows/fl-f06-05-benchmark-additions.md), [FL-SC01-01](../../../../08-sectors/sc01-construction/flows/fl-sc01-01-win-the-work.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC12-02](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-02-enrol-and-fund.md) |

## Open questions

None.

---

⬅️ [S-F6-L02 Opportunities](s-f06-l02-opportunities.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L04 Orders](s-f06-l04-orders.md)
