🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Non-profit association menu](README.md) › 🗂️ S-SC08-L11 Volunteer hours

# 🗂️ S-SC08-L11 Volunteer hours

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC08-11 Volunteer hours](../../data/e-sc08-11-volunteer-hours.md) the user may see: to
find, filter, total and act on many volunteer hours at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Non-profit association › Volunteer hours, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "volunteer hours" offers this view.
- **AI assistant:** "show the volunteer hours that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Volunteer hours    Non-profit association › Volunteer hours   [+ New]                                        |
| [count] [total value]   [chart: count by state, value stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] VOLUNTEER   STATE   MISSION   VALUE                                                  |
| mission           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Volunteer | volunteer | link to the record | yes |
| State | state | badge: Active | yes |
| Mission | mission | link to the record | yes |
| Value | value | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Mission | each linked mission | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Volunteer hours of a chosen mission, or of the missions that match a filter.
- From the other side: the missions that have volunteer hours, or none.

## KPI strip

- Count of the visible rows.
- Total of value.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, value stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New volunteer hours | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC08-11 Volunteer time](../04-volunteers/s-sc08-11-volunteer-time.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 volunteer hours of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no volunteer hours the user may see yet, with the create action when allowed.
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
| Listed, U32, view All | desktop | ![Listed, U32, view All, light](../../images/lists/s-sc08-l11-volunteer-hours-u32-volunteer-desktop-light.png) | ![Listed, U32, view All, dark](../../images/lists/s-sc08-l11-volunteer-hours-u32-volunteer-desktop-dark.png) |
| Listed, U32, view All | phone | ![Listed, U32, view All, light](../../images/lists/s-sc08-l11-volunteer-hours-u32-volunteer-phone-light.png) | ![Listed, U32, view All, dark](../../images/lists/s-sc08-l11-volunteer-hours-u32-volunteer-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-sc08-l11-volunteer-hours-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-sc08-l11-volunteer-hours-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-sc08-l11-volunteer-hours-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-sc08-l11-volunteer-hours-u31-treasurer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Non-profit association › Volunteer hours](README.md) |
| Workspaces | [U32](../../../../04-ux/views/u32-volunteer/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md) |
| Flows | [FL-SC04-01](../../../sc04-home-care/flows/fl-sc04-01-take-on-a-recipient.md), [FL-SC08-04](../../flows/fl-sc08-04-volunteers.md) |

## Open questions

None.

---

⬅️ [S-SC08-L10 Missions](s-sc08-l10-missions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-L12 Association events](s-sc08-l12-association-events.md)
