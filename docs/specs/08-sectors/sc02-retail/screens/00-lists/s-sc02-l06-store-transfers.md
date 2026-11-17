🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Retail menu](README.md) › 🗂️ S-SC02-L06 Store transfers

# 🗂️ S-SC02-L06 Store transfers

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC02-06 Store transfer](../../data/e-sc02-06-store-transfer.md) the user may see: to
find, filter, total and act on many store transfers at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Retail › Store transfers, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "store transfers" offers this view.
- **AI assistant:** "show the store transfers that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Store transfers    Retail › Store transfers   [+ New]                                                        |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FROM   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| From | from | text | yes |
| State | state | badge: Draft, Sent, InTransit, Received | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Sent, InTransit, Received | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: store transfers link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New store transfer | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC02-04 Transfers](../02-keep-stock-right/s-sc02-04-transfers.md).

The records also show on: [S-SC02-15 Store assistant](../05-unsold-goods-and-performance/s-sc02-15-store-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 store transfers of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no store transfer the user may see yet, with the create action when allowed.
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
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-sc02-l06-store-transfers-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-sc02-l06-store-transfers-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-sc02-l06-store-transfers-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-sc02-l06-store-transfers-u23-store-manager-phone-dark.png) |
| Listed, U17, view All | desktop | ![Listed, U17, view All, light](../../images/lists/s-sc02-l06-store-transfers-u17-cashier-desktop-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-sc02-l06-store-transfers-u17-cashier-desktop-dark.png) |
| Listed, U17, view All | phone | ![Listed, U17, view All, light](../../images/lists/s-sc02-l06-store-transfers-u17-cashier-phone-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-sc02-l06-store-transfers-u17-cashier-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Retail › Store transfers](README.md) |
| Workspaces | [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md) |
| Flows | [FL-SC02-02](../../flows/fl-sc02-02-keep-stock-right.md), [FL-SC02-05](../../flows/fl-sc02-05-unsold-goods-and-performance.md) |

## Open questions

None.

---

⬅️ [S-SC02-L05 Replenishment rules](s-sc02-l05-replenishment-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-L07 Shelf labels](s-sc02-l07-shelf-labels.md)
