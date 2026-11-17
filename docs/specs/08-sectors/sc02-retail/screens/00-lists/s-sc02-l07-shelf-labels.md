🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Retail menu](README.md) › 🗂️ S-SC02-L07 Shelf labels

# 🗂️ S-SC02-L07 Shelf labels

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC02-07 Shelf label](../../data/e-sc02-07-shelf-label.md) the user may see: to find,
filter, total and act on many shelf labels at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Retail › Shelf labels, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "shelf labels" offers this view.
- **AI assistant:** "show the shelf labels that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Shelf labels    Retail › Shelf labels   [+ New]                                                              |
| [count] [total price]   [chart: count by state, price stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| store             | [ ] PRODUCT   STATE   STORE   PRICE   UNIT PRICE                                         |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | link to the record | yes |
| State | state | badge: ToPrint, Done | yes |
| Store | store | link to the record | yes |
| Price | price | amount, right-aligned | yes |
| Unit price | unit price | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Store | each linked store | the visible rows (D488) |
| State | ToPrint, Done | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Shelf labels of a chosen store, or of the stores that match a filter.
- From the other side: the stores that have shelf labels, or none.

## KPI strip

- Count of the visible rows.
- Total of price.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: ToPrint.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** store.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the product and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New shelf label | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
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

Open › goes to [S-SC02-05 Labels](../01-set-up-the-stores/s-sc02-05-labels.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 shelf labels of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no shelf label the user may see yet, with the create action when allowed.
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
| Listed, U23, view Open: ToPrint | desktop | ![Listed, U23, view Open: ToPrint, light](../../images/lists/s-sc02-l07-shelf-labels-u23-store-manager-desktop-light.png) | ![Listed, U23, view Open: ToPrint, dark](../../images/lists/s-sc02-l07-shelf-labels-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Open: ToPrint | phone | ![Listed, U23, view Open: ToPrint, light](../../images/lists/s-sc02-l07-shelf-labels-u23-store-manager-phone-light.png) | ![Listed, U23, view Open: ToPrint, dark](../../images/lists/s-sc02-l07-shelf-labels-u23-store-manager-phone-dark.png) |
| Listed, U17, view Open: ToPrint | desktop | ![Listed, U17, view Open: ToPrint, light](../../images/lists/s-sc02-l07-shelf-labels-u17-cashier-desktop-light.png) | ![Listed, U17, view Open: ToPrint, dark](../../images/lists/s-sc02-l07-shelf-labels-u17-cashier-desktop-dark.png) |
| Listed, U17, view Open: ToPrint | phone | ![Listed, U17, view Open: ToPrint, light](../../images/lists/s-sc02-l07-shelf-labels-u17-cashier-phone-light.png) | ![Listed, U17, view Open: ToPrint, dark](../../images/lists/s-sc02-l07-shelf-labels-u17-cashier-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Retail › Shelf labels](README.md) |
| Workspaces | [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md) |
| Flows | [FL-SC02-01](../../flows/fl-sc02-01-set-up-the-stores.md) |

## Open questions

None.

---

⬅️ [S-SC02-L06 Store transfers](s-sc02-l06-store-transfers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-L08 Markdowns](s-sc02-l08-markdowns.md)
