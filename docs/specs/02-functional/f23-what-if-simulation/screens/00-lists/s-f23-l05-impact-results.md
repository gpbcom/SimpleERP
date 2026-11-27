🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: What-if simulation and impact menu](README.md) › 🗂️ S-F23-L05 Impact results

# 🗂️ S-F23-L05 Impact results

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F23-05 Impact result](../../data/e-f23-05-impact-result.md) the user may see: to find,
filter, total and act on many impact results at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** What-if simulation and impact › Impact results, in the capability's menu (D495).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "impact results" offers this view.
- **AI assistant:** "show the impact results that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Impact results    What-if simulation and impact › Impact results   [+ New]                                   |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RUN   STATE   SCENARIO                                                               |
| scenario          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Run | run | link to the record | yes |
| State | state | badge: Recorded | yes |
| Scenario | scenario | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Scenario | each linked scenario | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Impact results of a chosen scenario, or of the scenarios that match a filter.
- From the other side: the scenarios that have impact results, or none.

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

- **Place:** area.
- **Layout:** a plan, [C-18](../../../../04-ux/design-system/components/c-18-plan.md).
- **Marker:** the run and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New impact result | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F23-06 Sales impact](../03-see-the-impact/s-f23-06-sales-impact.md).

The records also show on: [S-F23-07 Cash impact](../03-see-the-impact/s-f23-07-cash-impact.md),
[S-F23-08 Statements impact](../03-see-the-impact/s-f23-08-statements-impact.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 impact results of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no impact result the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f23-l05-impact-results-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f23-l05-impact-results-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f23-l05-impact-results-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f23-l05-impact-results-u13-owner-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f23-l05-impact-results-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f23-l05-impact-results-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f23-l05-impact-results-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f23-l05-impact-results-u05-accounting-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-f23-l05-impact-results-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f23-l05-impact-results-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-f23-l05-impact-results-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f23-l05-impact-results-u31-treasurer-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f23-l05-impact-results-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f23-l05-impact-results-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f23-l05-impact-results-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f23-l05-impact-results-u03-sales-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f23-l05-impact-results-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f23-l05-impact-results-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f23-l05-impact-results-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f23-l05-impact-results-u04-purchasing-phone-dark.png) |
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f23-l05-impact-results-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f23-l05-impact-results-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f23-l05-impact-results-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f23-l05-impact-results-u21-production-planner-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f23-l05-impact-results-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f23-l05-impact-results-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f23-l05-impact-results-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f23-l05-impact-results-u06-hr-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f23-l05-impact-results-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f23-l05-impact-results-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f23-l05-impact-results-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f23-l05-impact-results-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-18 Plan](../../../../04-ux/design-system/components/c-18-plan.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [What-if simulation and impact › Impact results](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F23-02](../../flows/fl-f23-02-run.md), [FL-F23-03](../../flows/fl-f23-03-see-the-impact.md), [FL-F23-06](../../flows/fl-f23-06-goals-and-financing.md) |

## Open questions

None.

---

⬅️ [S-F23-L04 Simulation runs](s-f23-l04-simulation-runs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-L06 Sensitivities](s-f23-l06-sensitivities.md)
