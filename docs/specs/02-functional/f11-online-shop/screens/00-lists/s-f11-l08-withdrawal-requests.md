🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Online shop (plugin) menu](README.md) › 🗂️ S-F11-L08 Withdrawal requests

# 🗂️ S-F11-L08 Withdrawal requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U14: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F11-08 Withdrawal request](../../data/e-f11-08-withdrawal-request.md) the user may see:
to find, filter, total and act on many withdrawal requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Online shop (plugin) › Withdrawal requests, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "withdrawal requests" offers this view.
- **AI assistant:** "show the withdrawal requests that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Withdrawal requests    Online shop (plugin) › Withdrawal requests   [+ New]                                  |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| order             | [ ] ORDER   STATE   RECEIVED                                                             |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Order | order | text | yes |
| State | state | badge: Received, Acknowledged, Returned, Refunded | yes |
| Received | received | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Order | each value | the visible rows (D488) |
| State | Received, Acknowledged, Returned, Refunded | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Withdrawal requests of a chosen order, or of the orders that match a filter.
- From the other side: the orders that have withdrawal requests, or none.

## KPI strip

- Count of the visible rows.
- New this month, by received.

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
| New withdrawal request | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- received: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F11-09 Withdrawal](../03-after-the-order/s-f11-09-withdrawal.md).

The records also show on: [S-F11-28 Shop reports](../10-fulfil-from-stores-and-report/s-f11-28-shop-reports.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 withdrawal requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no withdrawal request the user may see yet, with the create action when allowed.
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
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u09-customer-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u03-sales-phone-dark.png) |
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u12-marketing-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f11-l08-withdrawal-requests-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f11-l08-withdrawal-requests-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Online shop (plugin) › Withdrawal requests](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F11-03](../../flows/fl-f11-03-after-the-order.md), [FL-F11-10](../../flows/fl-f11-10-fulfil-from-stores-and-report.md), [FL-SC02-03](../../../../08-sectors/sc02-retail/flows/fl-sc02-03-sell-and-return-across-channels.md) |

## Open questions

None.

---

⬅️ [S-F11-L07 Delivery methods](s-f11-l07-delivery-methods.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-L09 Customer accounts](s-f11-l09-customer-accounts.md)
