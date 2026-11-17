🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L09 Reordering rules

# 🗂️ S-F7-L09 Reordering rules

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

**Not embedded for:** U20, U21, U23: their use cases only read these records, inside a screen of the use case, so they
open them from there (D493).

## Purpose

The aggregated list of every [E-F7-09 Reordering rule](../../data/e-f07-09-reordering-rule.md) the user may see: to
find, filter, total and act on many reordering rules at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Reordering rules, in the Administration menu (D494).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "reordering rules" offers this view.
- **AI assistant:** "show the reordering rules that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Reordering rules    Administration › Reordering rules   [+ New]                                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ITEM   STATE   LOCATION   VISIBILITY DAYS                                            |
| item              | [ ] ...                                                  Open >                          |
| location          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Item | item | text | yes |
| State | state | badge: Active | yes |
| Location | location | text | yes |
| Visibility days | visibility days | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Item | each value | the visible rows (D488) |
| Location | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Reordering rules of a chosen item, or of the items that match a filter.
- From the other side: the items that have reordering rules, or none.
- Reordering rules of a chosen location, or of the locations that match a filter.
- From the other side: the locations that have reordering rules, or none.

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
| New reordering rule | header | U07 and the administration roles | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- visibility days: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-05 Replenishment](../03-replenish/s-f07-05-replenishment.md).

The records also show on: [S-F7-13 Warehouse setup](../03-replenish/s-f07-13-warehouse-setup.md),
[S-F7-21 Stock levels](../03-replenish/s-f07-21-stock-levels.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 reordering rules of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no reordering rule the user may see yet, with the create action when allowed.
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
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l09-reordering-rules-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l09-reordering-rules-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l09-reordering-rules-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l09-reordering-rules-u04-purchasing-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f07-l09-reordering-rules-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l09-reordering-rules-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f07-l09-reordering-rules-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l09-reordering-rules-u02-manager-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f07-l09-reordering-rules-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f07-l09-reordering-rules-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f07-l09-reordering-rules-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f07-l09-reordering-rules-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Reordering rules](README.md) |
| Workspaces | [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F7-03](../../flows/fl-f07-03-replenish.md), [FL-F7-08](../../flows/fl-f07-08-catalogues-and-stock-levels.md) |

## Open questions

None.

---

⬅️ [S-F7-L08 Routes](s-f07-l08-routes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L10 Lot or serials](s-f07-l10-lot-or-serials.md)
