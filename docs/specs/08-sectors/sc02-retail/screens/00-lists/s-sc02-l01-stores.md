🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Retail menu](README.md) › 🗂️ S-SC02-L01 Stores

# 🗂️ S-SC02-L01 Stores

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC02-01 Store](../../data/e-sc02-01-store.md) the user may see: to find, filter, total
and act on many stores at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Retail › Stores, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "stores" offers this view.
- **AI assistant:** "show the stores that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Stores    Retail › Stores   [+ New]                                                                          |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Planned, Open, Closed | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Planned, Open, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: stores link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Planned, Open.
- Needs attention.
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
| New store | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC02-01 Stores](../01-set-up-the-stores/s-sc02-01-stores.md).

The records also show on: [S-SC02-07 Store count](../02-keep-stock-right/s-sc02-07-store-count.md),
[S-SC02-08 Cross-channel orders](../03-sell-and-return-across-channels/s-sc02-08-cross-channel-orders.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 stores of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no store the user may see yet, with the create action when allowed.
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
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-sc02-l01-stores-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-sc02-l01-stores-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-sc02-l01-stores-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-sc02-l01-stores-u23-store-manager-phone-dark.png) |
| Listed, U17, view Open: Planned, Open | desktop | ![Listed, U17, view Open: Planned, Open, light](../../images/lists/s-sc02-l01-stores-u17-cashier-desktop-light.png) | ![Listed, U17, view Open: Planned, Open, dark](../../images/lists/s-sc02-l01-stores-u17-cashier-desktop-dark.png) |
| Listed, U17, view Open: Planned, Open | phone | ![Listed, U17, view Open: Planned, Open, light](../../images/lists/s-sc02-l01-stores-u17-cashier-phone-light.png) | ![Listed, U17, view Open: Planned, Open, dark](../../images/lists/s-sc02-l01-stores-u17-cashier-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-sc02-l01-stores-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-sc02-l01-stores-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-sc02-l01-stores-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-sc02-l01-stores-u13-owner-phone-dark.png) |
| Listed, U09, view Open: Planned, Open | desktop | ![Listed, U09, view Open: Planned, Open, light](../../images/lists/s-sc02-l01-stores-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Planned, Open, dark](../../images/lists/s-sc02-l01-stores-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Planned, Open | phone | ![Listed, U09, view Open: Planned, Open, light](../../images/lists/s-sc02-l01-stores-u09-customer-phone-light.png) | ![Listed, U09, view Open: Planned, Open, dark](../../images/lists/s-sc02-l01-stores-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Retail › Stores](README.md) |
| Workspaces | [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-SC02-01](../../flows/fl-sc02-01-set-up-the-stores.md), [FL-SC02-02](../../flows/fl-sc02-02-keep-stock-right.md), [FL-SC02-03](../../flows/fl-sc02-03-sell-and-return-across-channels.md), [FL-SC02-04](../../flows/fl-sc02-04-customers-and-staff.md), [FL-SC02-05](../../flows/fl-sc02-05-unsold-goods-and-performance.md) |

## Open questions

None.

---

⬅️ [S-SC02-19 Franchise network](../06-books-furniture-second-hand-franchise/s-sc02-19-franchise-network.md) ·
⬆️ [Up](README.md) · ➡️ [S-SC02-L02 Assortments](s-sc02-l02-assortments.md)
