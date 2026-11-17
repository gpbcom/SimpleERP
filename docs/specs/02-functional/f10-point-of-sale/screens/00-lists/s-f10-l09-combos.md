🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L09 Combos

# 🗂️ S-F10-L09 Combos

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F10-09 Combo](../../data/e-f10-09-combo.md) the user may see: to find, filter, total and
act on many combos at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale (plugin) › Combos, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "combos" offers this view.
- **AI assistant:** "show the combos that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Combos    Point of sale (plugin) › Combos   [+ New]                                                          |
| [count] [total price]   [chart: count by state, price stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   PRICE                                                                 |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Active | yes |
| Price | price | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: combos link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
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
| New combo | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F10-06 Prices and promotions](../02-sell-at-the-counter/s-f10-06-prices-and-promotions.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 combos of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no combo the user may see yet, with the create action when allowed.
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
| Listed, U17, view All | desktop | ![Listed, U17, view All, light](../../images/lists/s-f10-l09-combos-u17-cashier-desktop-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f10-l09-combos-u17-cashier-desktop-dark.png) |
| Listed, U17, view All | phone | ![Listed, U17, view All, light](../../images/lists/s-f10-l09-combos-u17-cashier-phone-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f10-l09-combos-u17-cashier-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f10-l09-combos-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l09-combos-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f10-l09-combos-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f10-l09-combos-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale (plugin) › Combos](README.md) |
| Workspaces | [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F10-02](../../flows/fl-f10-02-sell-at-the-counter.md), [FL-F10-11](../../flows/fl-f10-11-store-reports.md) |

## Open questions

None.

---

⬅️ [S-F10-L08 Price promotions](s-f10-l08-price-promotions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L10 Loyalty card and gift cards](s-f10-l10-loyalty-card-and-gift-cards.md)
