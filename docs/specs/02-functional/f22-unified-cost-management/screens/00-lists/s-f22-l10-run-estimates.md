🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Unified platform cost management menu](README.md) › 🗂️ S-F22-L10 Run estimates

# 🗂️ S-F22-L10 Run estimates

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F22-10 Run estimate](../../data/e-f22-10-run-estimate.md) the user may see: to find,
filter, total and act on many run estimates at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Unified platform cost management › Run estimates, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "run estimates" offers this view.
- **AI assistant:** "show the run estimates that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Run estimates    Unified platform cost management › Run estimates   [+ New]                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RUN   STATE                                                                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Run | run | link to the record | yes |
| State | state | badge: Running, Done | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Running, Done | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: run estimates link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Running.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New run estimate | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F22-10 Estimate](../03-runs/s-f22-10-estimate.md).

The records also show on: [S-F22-11 Live run](../03-runs/s-f22-11-live-run.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 run estimates of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no run estimate the user may see yet, with the create action when allowed.
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
| Listed, U07, view Open: Running | desktop | ![Listed, U07, view Open: Running, light](../../images/lists/s-f22-l10-run-estimates-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Running, dark](../../images/lists/s-f22-l10-run-estimates-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Running | phone | ![Listed, U07, view Open: Running, light](../../images/lists/s-f22-l10-run-estimates-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Running, dark](../../images/lists/s-f22-l10-run-estimates-u07-administrator-phone-dark.png) |
| Listed, U02, view Open: Running | desktop | ![Listed, U02, view Open: Running, light](../../images/lists/s-f22-l10-run-estimates-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Running, dark](../../images/lists/s-f22-l10-run-estimates-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Running | phone | ![Listed, U02, view Open: Running, light](../../images/lists/s-f22-l10-run-estimates-u02-manager-phone-light.png) | ![Listed, U02, view Open: Running, dark](../../images/lists/s-f22-l10-run-estimates-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Unified platform cost management › Run estimates](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F22-03](../../flows/fl-f22-03-runs.md), [FL-F3-12](../../../f03-assistant/flows/fl-f03-12-personal-cost-aware-and-learning.md) |

## Open questions

None.

---

⬅️ [S-F22-L09 Allocation rules](s-f22-l09-allocation-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-L11 Forecasts](s-f22-l11-forecasts.md)
