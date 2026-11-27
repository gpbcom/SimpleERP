🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Online shop (plugin) menu](README.md) › 🗂️ S-F11-L10 Product reviews

# 🗂️ S-F11-L10 Product reviews

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F11-10 Product review](../../data/e-f11-10-product-review.md) the user may see: to find,
filter, total and act on many product reviews at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Online shop (plugin) › Product reviews, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "product reviews" offers this view.
- **AI assistant:** "show the product reviews that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Product reviews    Online shop (plugin) › Product reviews   [+ New]                                          |
| [count] [Rejected] [new this month]   [chart: count by state]                                                |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| product           | [ ] PRODUCT   STATE   RATING   DATE                                                      |
| rating            | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | text | yes |
| State | state | badge: ToCheck, Published, Rejected | yes |
| Rating | rating | label | yes |
| Date | date | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Product | each value | the visible rows (D488) |
| Rating | 1 to 5, text | the visible rows (D488) |
| State | ToCheck, Published, Rejected | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Product reviews of a chosen product, or of the products that match a filter.
- From the other side: the products that have product reviews, or none.
- Product reviews of a chosen rating, or of the ratings that match a filter.
- From the other side: the ratings that have product reviews, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Rejected.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: ToCheck, Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New product review | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F11-15 Reviews](../05-grow-the-shop/s-f11-15-reviews.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 product reviews of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no product review the user may see yet, with the create action when allowed.
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
| Listed, U12, view Open: ToCheck, Published | desktop | ![Listed, U12, view Open: ToCheck, Published, light](../../images/lists/s-f11-l10-product-reviews-u12-marketing-desktop-light.png) | ![Listed, U12, view Open: ToCheck, Published, dark](../../images/lists/s-f11-l10-product-reviews-u12-marketing-desktop-dark.png) |
| Listed, U12, view Open: ToCheck, Published | phone | ![Listed, U12, view Open: ToCheck, Published, light](../../images/lists/s-f11-l10-product-reviews-u12-marketing-phone-light.png) | ![Listed, U12, view Open: ToCheck, Published, dark](../../images/lists/s-f11-l10-product-reviews-u12-marketing-phone-dark.png) |
| Listed, U09, view Open: ToCheck, Published | desktop | ![Listed, U09, view Open: ToCheck, Published, light](../../images/lists/s-f11-l10-product-reviews-u09-customer-desktop-light.png) | ![Listed, U09, view Open: ToCheck, Published, dark](../../images/lists/s-f11-l10-product-reviews-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: ToCheck, Published | phone | ![Listed, U09, view Open: ToCheck, Published, light](../../images/lists/s-f11-l10-product-reviews-u09-customer-phone-light.png) | ![Listed, U09, view Open: ToCheck, Published, dark](../../images/lists/s-f11-l10-product-reviews-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Online shop (plugin) › Product reviews](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F11-05](../../flows/fl-f11-05-grow-the-shop.md) |

## Open questions

None.

---

⬅️ [S-F11-L09 Customer accounts](s-f11-l09-customer-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-L11 Online promotion codes](s-f11-l11-online-promotion-codes.md)
