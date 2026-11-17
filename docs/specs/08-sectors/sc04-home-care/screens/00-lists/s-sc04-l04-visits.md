🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Home care menu](README.md) › 🗂️ S-SC04-L04 Visits

# 🗂️ S-SC04-L04 Visits

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC04-04 Visit](../../data/e-sc04-04-visit.md) the user may see: to find, filter, total
and act on many visits at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Home care › Visits, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "visits" offers this view.
- **AI assistant:** "show the visits that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Visits    Home care › Visits   [+ New]                                                                       |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| carer             | [ ] RECIPIENT   STATE   CARER                                                            |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Recipient | recipient | link to the record | yes |
| State | state | badge: Planned, Done, Missed, Cancelled | yes |
| Carer | carer | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Carer | each linked carer | the visible rows (D488) |
| State | Planned, Done, Missed, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: visits link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: carer.
- Open: Planned, Missed.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New visit | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the carer; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- carer: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC04-04 Visit](../02-plan-the-rounds/s-sc04-04-visit.md).

The records also show on: [S-SC04-03 Rounds](../02-plan-the-rounds/s-sc04-03-rounds.md),
[S-SC04-06 Replacements](../02-plan-the-rounds/s-sc04-06-replacements.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 visits of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no visit the user may see yet, with the create action when allowed.
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
| Listed, U25, view Open: Planned, Missed | desktop | ![Listed, U25, view Open: Planned, Missed, light](../../images/lists/s-sc04-l04-visits-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Open: Planned, Missed, dark](../../images/lists/s-sc04-l04-visits-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Open: Planned, Missed | phone | ![Listed, U25, view Open: Planned, Missed, light](../../images/lists/s-sc04-l04-visits-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Open: Planned, Missed, dark](../../images/lists/s-sc04-l04-visits-u25-care-coordinator-phone-dark.png) |
| Listed, U26, view Mine: carer | desktop | ![Listed, U26, view Mine: carer, light](../../images/lists/s-sc04-l04-visits-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: carer, dark](../../images/lists/s-sc04-l04-visits-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: carer | phone | ![Listed, U26, view Mine: carer, light](../../images/lists/s-sc04-l04-visits-u26-carer-phone-light.png) | ![Listed, U26, view Mine: carer, dark](../../images/lists/s-sc04-l04-visits-u26-carer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Home care › Visits](README.md) |
| Workspaces | [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md) |
| Flows | [FL-SC04-02](../../flows/fl-sc04-02-plan-the-rounds.md), [FL-SC04-03](../../flows/fl-sc04-03-visit.md) |

## Open questions

None.

---

⬅️ [S-SC04-L03 Care plans](s-sc04-l03-care-plans.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-L06 Care log entries](s-sc04-l06-care-log-entries.md)
