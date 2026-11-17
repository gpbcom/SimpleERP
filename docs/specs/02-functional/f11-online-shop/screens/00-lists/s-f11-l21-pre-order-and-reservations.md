🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Online shop (plugin) menu](README.md) › 🗂️ S-F11-L21 Pre-order and reservations

# 🗂️ S-F11-L21 Pre-order and reservations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F11-21 Pre-order and reservation](../../data/e-f11-21-pre-order-and-reservation.md) the
user may see: to find, filter, total and act on many pre-order and reservations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Online shop (plugin) › Pre-order and reservations, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "pre-order and reservations" offers this view.
- **AI assistant:** "show the pre-order and reservations that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Pre-order and reservations    Online shop (plugin) › Pre-order and reservations   [+ New]                    |
| [count] [Open] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] KIND   STATUS   PRODUCT   DATE AND PAYMENT                                           |
| kind              | [ ] ...                                                  Open >                          |
| product           | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Kind | kind | label | yes |
| Status | status | badge | yes |
| Product | product | text | yes |
| Date and payment | date and payment | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open, Shipped, Released, Held, Cancelled | the visible rows (D488) |
| Kind | pre-order, reservation | the visible rows (D488) |
| Product | each value | the visible rows (D488) |
| Status | Open, Shipped, Released, Held, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Pre-order and reservations of a chosen product, or of the products that match a filter.
- From the other side: the products that have pre-order and reservations, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.
- New this month, by date and payment.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Open, Shipped, Released.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New pre-order and reservation | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date and payment: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| shopper | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F11-26 Pre-order](../09-pre-orders-and-b2b-buying/s-f11-26-pre-order.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 pre-order and reservations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no pre-order and reservation the user may see yet, with the create action when allowed.
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
| Listed, U09, view Open: Open, Shipped, Released | desktop | ![Listed, U09, view Open: Open, Shipped, Released, light](../../images/lists/s-f11-l21-pre-order-and-reservations-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Open, Shipped, Released, dark](../../images/lists/s-f11-l21-pre-order-and-reservations-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Open, Shipped, Released | phone | ![Listed, U09, view Open: Open, Shipped, Released, light](../../images/lists/s-f11-l21-pre-order-and-reservations-u09-customer-phone-light.png) | ![Listed, U09, view Open: Open, Shipped, Released, dark](../../images/lists/s-f11-l21-pre-order-and-reservations-u09-customer-phone-dark.png) |
| Listed, U12, view Open: Open, Shipped, Released | desktop | ![Listed, U12, view Open: Open, Shipped, Released, light](../../images/lists/s-f11-l21-pre-order-and-reservations-u12-marketing-desktop-light.png) | ![Listed, U12, view Open: Open, Shipped, Released, dark](../../images/lists/s-f11-l21-pre-order-and-reservations-u12-marketing-desktop-dark.png) |
| Listed, U12, view Open: Open, Shipped, Released | phone | ![Listed, U12, view Open: Open, Shipped, Released, light](../../images/lists/s-f11-l21-pre-order-and-reservations-u12-marketing-phone-light.png) | ![Listed, U12, view Open: Open, Shipped, Released, dark](../../images/lists/s-f11-l21-pre-order-and-reservations-u12-marketing-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Online shop (plugin) › Pre-order and reservations](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md) |
| Flows | [FL-F11-09](../../flows/fl-f11-09-pre-orders-and-b2b-buying.md) |

## Open questions

None.

---

⬅️ [S-F11-L20 Product safety informations](s-f11-l20-product-safety-informations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-L22 Punch-out sessions](s-f11-l22-punch-out-sessions.md)
