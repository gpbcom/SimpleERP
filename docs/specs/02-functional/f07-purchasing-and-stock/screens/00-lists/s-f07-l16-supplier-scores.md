🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L16 Supplier scores

# 🗂️ S-F7-L16 Supplier scores

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F7-16 Supplier score](../../data/e-f07-16-supplier-score.md) the user may see: to find,
filter, total and act on many supplier scores at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Supplier scores, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "supplier scores" offers this view.
- **AI assistant:** "show the supplier scores that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Supplier scores    Purchasing and stock › Supplier scores   [+ New]                                          |
| [count] [total price variance] [new this month]   [chart: count by state, price variance stacked]            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SUPPLIER   STATE   PRICE VARIANCE   PERIOD   ON TIME IN FULL   SCORE                 |
| supplier          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Supplier | supplier | text | yes |
| State | state | badge: Recorded | yes |
| Price variance | price variance | amount, right-aligned | yes |
| Period | period | date | yes |
| On time in full | on time in full | number, right-aligned | yes |
| Score | score | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Supplier | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Supplier scores of a chosen supplier, or of the suppliers that match a filter.
- From the other side: the suppliers that have supplier scores, or none.

## KPI strip

- Count of the visible rows.
- Total of price variance.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price variance stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New supplier score | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- period: editable in its cell unless the record's state locks it.
- on time in full: editable in its cell unless the record's state locks it.
- score: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F7-19 Supplier performance](../07-supplier-agreements-and-performance/s-f07-19-supplier-performance.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 supplier scores of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no supplier score the user may see yet, with the create action when allowed.
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
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l16-supplier-scores-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l16-supplier-scores-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l16-supplier-scores-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l16-supplier-scores-u04-purchasing-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f07-l16-supplier-scores-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l16-supplier-scores-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f07-l16-supplier-scores-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l16-supplier-scores-u13-owner-phone-dark.png) |
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-f07-l16-supplier-scores-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l16-supplier-scores-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-f07-l16-supplier-scores-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f07-l16-supplier-scores-u27-quality-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Supplier scores](README.md) |
| Workspaces | [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md) |
| Flows | [FL-F7-07](../../flows/fl-f07-07-supplier-agreements-and-performance.md) |

## Open questions

None.

---

⬅️ [S-F7-L15 Supplier contracts](s-f07-l15-supplier-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L17 Approved catalogues](s-f07-l17-approved-catalogues.md)
