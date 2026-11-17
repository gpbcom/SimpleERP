🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: What-if simulation and impact menu](README.md) › 🗂️ S-F23-L02 Scenarios

# 🗂️ S-F23-L02 Scenarios

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U31: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F23-02 Scenario](../../data/e-f23-02-scenario.md) the user may see: to find, filter,
total and act on many scenarios at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** What-if simulation and impact › Scenarios, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "scenarios" offers this view.
- **AI assistant:** "show the scenarios that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Scenarios    What-if simulation and impact › Scenarios   [+ New]                                             |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   OWNER                                                                 |
| owner             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | link to the record | yes |
| State | state | badge: Active | yes |
| Owner | owner | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Owner | each linked owner | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: scenarios link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: owner.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New scenario | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the owner; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- owner: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F23-02 New scenario](../01-build-a-scenario/s-f23-02-new-scenario.md).

The records also show on: [S-F23-15 Comparison](../04-decide/s-f23-15-comparison.md),
[S-F23-19 Sharing](../04-decide/s-f23-19-sharing.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 scenarios of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no scenario the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f23-l02-scenarios-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f23-l02-scenarios-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f23-l02-scenarios-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f23-l02-scenarios-u13-owner-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f23-l02-scenarios-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f23-l02-scenarios-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f23-l02-scenarios-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f23-l02-scenarios-u02-manager-phone-dark.png) |
| Listed, U08, view All | desktop | ![Listed, U08, view All, light](../../images/lists/s-f23-l02-scenarios-u08-external-accountant-desktop-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f23-l02-scenarios-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view All | phone | ![Listed, U08, view All, light](../../images/lists/s-f23-l02-scenarios-u08-external-accountant-phone-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f23-l02-scenarios-u08-external-accountant-phone-dark.png) |
| Listed, U05, view Mine: owner | desktop | ![Listed, U05, view Mine: owner, light](../../images/lists/s-f23-l02-scenarios-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: owner, dark](../../images/lists/s-f23-l02-scenarios-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: owner | phone | ![Listed, U05, view Mine: owner, light](../../images/lists/s-f23-l02-scenarios-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: owner, dark](../../images/lists/s-f23-l02-scenarios-u05-accounting-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [What-if simulation and impact › Scenarios](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md) |
| Flows | [FL-F23-01](../../flows/fl-f23-01-build-a-scenario.md), [FL-F23-02](../../flows/fl-f23-02-run.md), [FL-F23-04](../../flows/fl-f23-04-decide.md), [FL-F23-05](../../flows/fl-f23-05-act-and-watch.md), [FL-F23-06](../../flows/fl-f23-06-goals-and-financing.md), [FL-F23-07](../../flows/fl-f23-07-accuracy-and-drivers.md) |

## Open questions

None.

---

⬅️ [S-F23-L01 Baseline forecasts](s-f23-l01-baseline-forecasts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-L03 Scenario changes](s-f23-l03-scenario-changes.md)
