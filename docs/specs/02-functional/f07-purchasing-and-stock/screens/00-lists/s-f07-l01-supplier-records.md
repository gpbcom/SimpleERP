🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L01 Supplier records

# 🗂️ S-F7-L01 Supplier records

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U10 Supplier](../../../../01-users/personas/u10-supplier.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U08, U15, U23, U31, U40, U54, U55: their use cases only read these records, inside a screen of the
use case, so they open them from there (D493).

## Purpose

The aggregated list of every [E-F7-01 Supplier record](../../data/e-f07-01-supplier-record.md) the user may see: to
find, filter, total and act on many supplier records at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Supplier records, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "supplier records" offers this view.
- **AI assistant:** "show the supplier records that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Supplier records    Purchasing and stock › Supplier records   [+ New]                                        |
| [count] [total price lists]   [chart: count by state, price lists stacked]                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   PRICE LISTS                                                           |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Active | yes |
| Price lists | price lists | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: supplier records link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price lists.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price lists stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
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
| New supplier record | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F7-12 Supplier portal](../01-procure/s-f07-12-supplier-portal.md).

The records also show on:
[S-F7-18 Supplier contracts](../07-supplier-agreements-and-performance/s-f07-18-supplier-contracts.md),
[S-F7-02 Purchase order](../01-procure/s-f07-02-purchase-order.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 supplier records of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no supplier record the user may see yet, with the create action when allowed.
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
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l01-supplier-records-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l01-supplier-records-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l01-supplier-records-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l01-supplier-records-u04-purchasing-phone-dark.png) |
| Listed, U10, view All | desktop | ![Listed, U10, view All, light](../../images/lists/s-f07-l01-supplier-records-u10-supplier-desktop-light.png) | ![Listed, U10, view All, dark](../../images/lists/s-f07-l01-supplier-records-u10-supplier-desktop-dark.png) |
| Listed, U10, view All | phone | ![Listed, U10, view All, light](../../images/lists/s-f07-l01-supplier-records-u10-supplier-phone-light.png) | ![Listed, U10, view All, dark](../../images/lists/s-f07-l01-supplier-records-u10-supplier-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f07-l01-supplier-records-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l01-supplier-records-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f07-l01-supplier-records-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l01-supplier-records-u05-accounting-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f07-l01-supplier-records-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l01-supplier-records-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f07-l01-supplier-records-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l01-supplier-records-u13-owner-phone-dark.png) |
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-f07-l01-supplier-records-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l01-supplier-records-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-f07-l01-supplier-records-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l01-supplier-records-u27-quality-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Supplier records](README.md) |
| Workspaces | [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U10](../../../../04-ux/views/u10-supplier/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md) |
| Flows | [FL-F7-01](../../flows/fl-f07-01-procure.md), [FL-F7-07](../../flows/fl-f07-07-supplier-agreements-and-performance.md) |

## Open questions

None.

---

⬅️ [S-F7-30 Slotting](../10-consignment-scanning-and-edi/s-f07-30-slotting.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L02 Purchase requests](s-f07-l02-purchase-requests.md)
