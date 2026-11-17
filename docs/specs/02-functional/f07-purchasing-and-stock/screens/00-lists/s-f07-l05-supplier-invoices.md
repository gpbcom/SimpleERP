🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L05 Supplier invoices

# 🗂️ S-F7-L05 Supplier invoices

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | as the permissions row "Supplier invoices": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Supplier invoices": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | as the permissions row "Supplier invoices": ✅ view | actions as [permissions](../../permissions.md) gives them |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U54: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F7-05 Supplier invoice](../../data/e-f07-05-supplier-invoice.md) the user may see: to
find, filter, total and act on many supplier invoices at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Supplier invoices, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "supplier invoices" offers this view.
- **AI assistant:** "show the supplier invoices that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Supplier invoices    Purchasing and stock › Supplier invoices   [+ New]                                      |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| differences       | [ ] SOURCE   STATE   DIFFERENCES                                                         |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Source | source | link to the record | yes |
| State | state | badge: Received, Matched, SentToAccounting, Held | yes |
| Differences | differences | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Differences | each value | the visible rows (D488) |
| State | Received, Matched, SentToAccounting, Held | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: supplier invoices link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

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
| New supplier invoice | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- differences: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-04 Supplier invoice matching](../01-procure/s-f07-04-supplier-invoice-matching.md).

The records also show on: [S-F7-24 Purchase carbon](../09-compliance-and-carbon/s-f07-24-purchase-carbon.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 supplier invoices of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no supplier invoice the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u13-owner-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u04-purchasing-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u31-treasurer-phone-dark.png) |
| Listed, U41, view All | desktop | ![Listed, U41, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u41-customer-success-manager-desktop-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u41-customer-success-manager-desktop-dark.png) |
| Listed, U41, view All | phone | ![Listed, U41, view All, light](../../images/lists/s-f07-l05-supplier-invoices-u41-customer-success-manager-phone-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f07-l05-supplier-invoices-u41-customer-success-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Supplier invoices](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U41](../../../../04-ux/views/u41-customer-success-manager/workspace.md) |
| Flows | [FL-F12-05](../../../f12-manufacturing/flows/fl-f12-05-subcontracting-and-costs.md), [FL-F7-01](../../flows/fl-f07-01-procure.md), [FL-F7-07](../../flows/fl-f07-07-supplier-agreements-and-performance.md), [FL-F7-09](../../flows/fl-f07-09-compliance-and-carbon.md), [FL-F8-02](../../../f08-accounting/flows/fl-f08-02-purchase-to-pay.md) |

## Open questions

None.

---

⬅️ [S-F7-L04 Transfers](s-f07-l04-transfers.md) · ⬆️ [Up](README.md) · ➡️ [S-F7-L06 Items](s-f07-l06-items.md)
