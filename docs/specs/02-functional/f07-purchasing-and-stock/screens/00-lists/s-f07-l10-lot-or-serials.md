🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L10 Lot or serials

# 🗂️ S-F7-L10 Lot or serials

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05, U40, U52: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-F7-10 Lot or serial](../../data/e-f07-10-lot-or-serial.md) the user may see: to find,
filter, total and act on many lot or serials at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Lot or serials, in the capability's menu (D495).
- **Workspaces:** 9 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "lot or serials" offers this view.
- **AI assistant:** "show the lot or serials that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Lot or serials    Purchasing and stock › Lot or serials   [+ New]                                            |
| [count] [due in 7 days]   [chart: count by state]                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NUMBER   STATE   ITEM   EXPIRY                                                       |
| item              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | text | yes |
| State | state | badge: Active | yes |
| Item | item | text | yes |
| Expiry | expiry | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Item | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Lot or serials of a chosen item, or of the items that match a filter.
- From the other side: the items that have lot or serials, or none.

## KPI strip

- Count of the visible rows.
- Due in 7 days, by expiry.

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
| New lot or serial | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- expiry: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-03 Receipt](../02-receive-and-store/s-f07-03-receipt.md).

The records also show on: [S-F7-06 Pick, pack and ship](../04-pick-pack-and-ship/s-f07-06-pick-pack-and-ship.md),
[S-F7-08 Traceability](../05-count-trace-and-analyse/s-f07-08-traceability.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 lot or serials of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no lot or serial the user may see yet, with the create action when allowed.
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
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u15-warehouse-operator-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u04-purchasing-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u02-manager-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u03-sales-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u14-field-worker-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u20-production-operator-phone-dark.png) |
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u21-production-planner-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u23-store-manager-phone-dark.png) |
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-f07-l10-lot-or-serials-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l10-lot-or-serials-u27-quality-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Lot or serials](README.md) |
| Workspaces | [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md) |
| Flows | [FL-F12-09](../../../f12-manufacturing/flows/fl-f12-09-recipes-and-batches.md), [FL-F7-02](../../flows/fl-f07-02-receive-and-store.md), [FL-F7-04](../../flows/fl-f07-04-pick-pack-and-ship.md), [FL-F7-05](../../flows/fl-f07-05-count-trace-and-analyse.md), [FL-SC05-01](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-01-production-setups.md), [FL-SC05-03](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-03-packaging.md) |

## Open questions

None.

---

⬅️ [S-F7-L09 Reordering rules](s-f07-l09-reordering-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L11 Stock counts](s-f07-l11-stock-counts.md)
