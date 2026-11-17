🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: What-if simulation and impact menu](README.md) › 🗂️ S-F23-L03 Scenario changes

# 🗂️ S-F23-L03 Scenario changes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F23-03 Scenario change](../../data/e-f23-03-scenario-change.md) the user may see: to
find, filter, total and act on many scenario changes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** What-if simulation and impact › Scenario changes, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "scenario changes" offers this view.
- **AI assistant:** "show the scenario changes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Scenario changes    What-if simulation and impact › Scenario changes   [+ New]                               |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SCENARIO   STATE                                                                     |
| scenario          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Scenario | scenario | link to the record | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Scenario | each linked scenario | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Scenario changes of a chosen scenario, or of the scenarios that match a filter.
- From the other side: the scenarios that have scenario changes, or none.

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
| New scenario change | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F23-03 Changes](../01-build-a-scenario/s-f23-03-changes.md).

The records also show on: [S-F23-04 Ranges](../01-build-a-scenario/s-f23-04-ranges.md),
[S-F23-13 Platform costs impact](../03-see-the-impact/s-f23-13-platform-costs-impact.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 scenario changes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no scenario change the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f23-l03-scenario-changes-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f23-l03-scenario-changes-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u13-owner-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f23-l03-scenario-changes-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f23-l03-scenario-changes-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u02-manager-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f23-l03-scenario-changes-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f23-l03-scenario-changes-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u05-accounting-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-f23-l03-scenario-changes-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-f23-l03-scenario-changes-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f23-l03-scenario-changes-u31-treasurer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [What-if simulation and impact › Scenario changes](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md) |
| Flows | [FL-F23-01](../../flows/fl-f23-01-build-a-scenario.md), [FL-F23-03](../../flows/fl-f23-03-see-the-impact.md), [FL-F23-06](../../flows/fl-f23-06-goals-and-financing.md), [FL-F23-07](../../flows/fl-f23-07-accuracy-and-drivers.md) |

## Open questions

None.

---

⬅️ [S-F23-L02 Scenarios](s-f23-l02-scenarios.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-L04 Simulation runs](s-f23-l04-simulation-runs.md)
