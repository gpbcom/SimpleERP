🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Agriculture and food menu](README.md) › 🗂️ S-SC13-L12 Batches

# 🗂️ S-SC13-L12 Batches

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC13-12 Batch](../../data/e-sc13-12-batch.md) the user may see: to find, filter, total
and act on many batches at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Agriculture and food › Batches, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "batches" offers this view.
- **AI assistant:** "show the batches that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Batches    Agriculture and food › Batches   [+ New]                                                          |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RECIPE   STATE                                                                       |
| recipe            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Recipe | recipe | link to the record | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Recipe | each linked recipe | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Batches of a chosen recipe, or of the recipes that match a filter.
- From the other side: the recipes that have batches, or none.

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
| New batch | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC13-13 Batches](../05-food-processing/s-sc13-13-batches.md).

The records also show on: [S-SC13-14 Traceability](../05-food-processing/s-sc13-14-traceability.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 batches of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no batch the user may see yet, with the create action when allowed.
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
| Listed, U40, view All | desktop | ![Listed, U40, view All, light](../../images/lists/s-sc13-l12-batches-u40-farmer-desktop-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-sc13-l12-batches-u40-farmer-desktop-dark.png) |
| Listed, U40, view All | phone | ![Listed, U40, view All, light](../../images/lists/s-sc13-l12-batches-u40-farmer-phone-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-sc13-l12-batches-u40-farmer-phone-dark.png) |
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-sc13-l12-batches-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-sc13-l12-batches-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-sc13-l12-batches-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-sc13-l12-batches-u21-production-planner-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-sc13-l12-batches-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-sc13-l12-batches-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-sc13-l12-batches-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-sc13-l12-batches-u20-production-operator-phone-dark.png) |
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-sc13-l12-batches-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-sc13-l12-batches-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-sc13-l12-batches-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-sc13-l12-batches-u27-quality-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Agriculture and food › Batches](README.md) |
| Workspaces | [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md) |
| Flows | [FL-SC13-05](../../flows/fl-sc13-05-food-processing.md) |

## Open questions

None.

---

⬅️ [S-SC13-L11 Organic records](s-sc13-l11-organic-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-L13 Hygiene readings](s-sc13-l13-hygiene-readings.md)
