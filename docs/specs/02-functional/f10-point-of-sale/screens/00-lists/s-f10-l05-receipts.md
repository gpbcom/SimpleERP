🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L05 Receipts

# 🗂️ S-F10-L05 Receipts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F10-05 Receipt](../../data/e-f10-05-receipt.md) the user may see: to find, filter, total
and act on many receipts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Receipts, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "receipts" offers this view.
- **AI assistant:** "show the receipts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Receipts    Point of sale (plugin) › Receipts   [+ New]                                                      |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ORDER   STATE   REPRINTS                                                             |
| order             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Order | order | link to the record | yes |
| State | state | badge: Recorded | yes |
| Reprints | reprints | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Order | each linked order | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Receipts of a chosen order, or of the orders that match a filter.
- From the other side: the orders that have receipts, or none.

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
| New receipt | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- reprints: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| signature | secret | nobody | everyone (VR-4) |

## Row opens

Open › goes to [S-F10-05 Receipt](../02-sell-at-the-counter/s-f10-05-receipt.md).

The records also show on: [S-F10-04 Refund](../03-after-sales/s-f10-04-refund.md),
[S-F10-26 Tax-free](../10-clienteling-transfers-and-tax-free/s-f10-26-tax-free.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 receipts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no receipt the user may see yet, with the create action when allowed.
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
| Listed, U17, view All | desktop | ![Listed, U17, view All, light](../../images/lists/s-f10-l05-receipts-u17-cashier-desktop-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f10-l05-receipts-u17-cashier-desktop-dark.png) |
| Listed, U17, view All | phone | ![Listed, U17, view All, light](../../images/lists/s-f10-l05-receipts-u17-cashier-phone-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f10-l05-receipts-u17-cashier-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f10-l05-receipts-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l05-receipts-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f10-l05-receipts-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l05-receipts-u02-manager-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f10-l05-receipts-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f10-l05-receipts-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f10-l05-receipts-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f10-l05-receipts-u09-customer-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f10-l05-receipts-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f10-l05-receipts-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f10-l05-receipts-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f10-l05-receipts-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Receipts](README.md) |
| Workspaces | [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-F10-02](../../flows/fl-f10-02-sell-at-the-counter.md), [FL-F10-03](../../flows/fl-f10-03-after-sales.md), [FL-F10-10](../../flows/fl-f10-10-clienteling-transfers-and-tax-free.md) |

## Open questions

None.

---

⬅️ [S-F10-L04 Till payments](s-f10-l04-till-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L06 Closures](s-f10-l06-closures.md)
