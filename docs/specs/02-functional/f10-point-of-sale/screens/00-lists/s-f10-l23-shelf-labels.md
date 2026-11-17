🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Point of sale (plugin) menu](README.md) › 🗂️ S-F10-L23 Shelf labels

# 🗂️ S-F10-L23 Shelf labels

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F10-23 Shelf label](../../data/e-f10-23-shelf-label.md) the user may see: to find,
filter, total and act on many shelf labels at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Point of sale › Shelf labels, in the capability's menu (D495).
- **Workspaces:** 1 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "shelf labels" offers this view.
- **AI assistant:** "show the shelf labels that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Shelf labels    Point of sale › Shelf labels   [+ New]                                                       |
| [count] [Mismatch] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] LABEL   PRODUCT   SHELF   PRICE SHOWN   STATE                                        |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Label | code | text | yes |
| Product | product | text | yes |
| Shelf | shelf position | text | yes |
| Price shown | price shown | money | yes |
| State | state | badge: Registered, Linked, Updating, Up to date, Mismatch, Faulty, Retired | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Registered, Linked, Updating, Up to date, Mismatch, Faulty, Retired | the visible rows (D488) |
| Shelf | each value | the visible rows (D488) |
| Battery | low, normal | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Labels of a chosen product, or of the products that match a filter.
- From the other side: the products with a label, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Mismatch.
- New this month, by last confirmed at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: shop.
- Open: Linked.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New shelf label | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

Shelf position: the store manager edits it in place.

## Hidden fields

None: no field of this list is personal data.

## Row opens

Open › goes to [S-F10-30 Shelf labels](../12-takeaway-softpos-and-labels/s-f10-30-shelf-labels.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 shelf labels of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no shelf label the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in the image round from this page: one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)). The files are named by the plan.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f10-l23-shelf-labels-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f10-l23-shelf-labels-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Mine: shop | phone | ![Listed, U23, view Mine: shop, light](../../images/lists/s-f10-l23-shelf-labels-u23-store-manager-phone-light.png) | ![Listed, U23, view Mine: shop, dark](../../images/lists/s-f10-l23-shelf-labels-u23-store-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Point of sale › Shelf labels](README.md) |
| Workspaces | [U23](../../../../04-ux/views/u23-store-manager/workspace.md) |
| Flows | [FL-F10-12](../../flows/fl-f10-12-takeaway-softpos-and-labels.md) |

## Open questions

None.

---

⬅️ [S-F10-L22 Takeaway orders](s-f10-l22-takeaway-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-L24 Layaways](s-f10-l24-layaways.md)
