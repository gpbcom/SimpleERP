🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Manufacturing menu](README.md) › 🗂️ S-SC05-L10 Supplier ratings

# 🗂️ S-SC05-L10 Supplier ratings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC05-10 Supplier rating](../../data/e-sc05-10-supplier-rating.md) the user may see: to
find, filter, total and act on many supplier ratings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing › Supplier ratings, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "supplier ratings" offers this view.
- **AI assistant:** "show the supplier ratings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Supplier ratings    Manufacturing › Supplier ratings   [+ New]                                               |
| [count] [Blocked]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SUPPLIER   STATUS                                                                    |
| supplier          | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Supplier | supplier | person's name | yes |
| Status | status | badge | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Qualified, Blocked | the visible rows (D488) |
| Supplier | each person, the user first | the visible rows (D488) |
| Status | Qualified, Blocked | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: supplier ratings link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Blocked.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: supplier.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New supplier rating | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the supplier; audited |
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

Open › goes to [S-SC05-10 Supplier quality](../05-suppliers-and-customers/s-sc05-10-supplier-quality.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 supplier ratings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no supplier rating the user may see yet, with the create action when allowed.
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
| Listed, U27, view Mine: supplier | desktop | ![Listed, U27, view Mine: supplier, light](../../images/lists/s-sc05-l10-supplier-ratings-u27-quality-manager-desktop-light.png) | ![Listed, U27, view Mine: supplier, dark](../../images/lists/s-sc05-l10-supplier-ratings-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view Mine: supplier | phone | ![Listed, U27, view Mine: supplier, light](../../images/lists/s-sc05-l10-supplier-ratings-u27-quality-manager-phone-light.png) | ![Listed, U27, view Mine: supplier, dark](../../images/lists/s-sc05-l10-supplier-ratings-u27-quality-manager-phone-dark.png) |
| Listed, U04, view Mine: supplier | desktop | ![Listed, U04, view Mine: supplier, light](../../images/lists/s-sc05-l10-supplier-ratings-u04-purchasing-desktop-light.png) | ![Listed, U04, view Mine: supplier, dark](../../images/lists/s-sc05-l10-supplier-ratings-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Mine: supplier | phone | ![Listed, U04, view Mine: supplier, light](../../images/lists/s-sc05-l10-supplier-ratings-u04-purchasing-phone-light.png) | ![Listed, U04, view Mine: supplier, dark](../../images/lists/s-sc05-l10-supplier-ratings-u04-purchasing-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing › Supplier ratings](README.md) |
| Workspaces | [U27](../../../../04-ux/views/u27-quality-manager/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md) |
| Flows | [FL-SC05-05](../../flows/fl-sc05-05-suppliers-and-customers.md) |

## Open questions

None.

---

⬅️ [S-SC05-L09 Quality actions](s-sc05-l09-quality-actions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-L11 8D reports](s-sc05-l11-8d-reports.md)
