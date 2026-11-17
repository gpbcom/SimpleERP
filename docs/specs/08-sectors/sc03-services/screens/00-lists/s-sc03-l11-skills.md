🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Services menu](README.md) › 🗂️ S-SC03-L11 Skills

# 🗂️ S-SC03-L11 Skills

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U36: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC03-11 Skill](../../data/e-sc03-11-skill.md) the user may see: to find, filter, total
and act on many skills at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Services › Skills, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "skills" offers this view.
- **AI assistant:** "show the skills that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Skills    Services › Skills   [+ New]                                                                        |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CONSULTANT   STATE   SKILL                                                           |
| skill             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Consultant | consultant | link to the record | yes |
| State | state | badge: New, Validated | yes |
| Skill | the record's title | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | New, Validated | the visible rows (D488) |
| Skill | each linked skill | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Skills of a chosen skill, or of the skills that match a filter.
- From the other side: the skills that have skills, or none.

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
| New skill | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC03-13 Skills](../05-client-and-people/s-sc03-13-skills.md).

The records also show on: [S-SC03-03 Staffing](../02-staff-and-plan/s-sc03-03-staffing.md),
[S-SC03-04 Resource plan](../02-staff-and-plan/s-sc03-04-resource-plan.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 skills of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no skill the user may see yet, with the create action when allowed.
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
| Listed, U24, view All | desktop | ![Listed, U24, view All, light](../../images/lists/s-sc03-l11-skills-u24-engagement-manager-desktop-light.png) | ![Listed, U24, view All, dark](../../images/lists/s-sc03-l11-skills-u24-engagement-manager-desktop-dark.png) |
| Listed, U24, view All | phone | ![Listed, U24, view All, light](../../images/lists/s-sc03-l11-skills-u24-engagement-manager-phone-light.png) | ![Listed, U24, view All, dark](../../images/lists/s-sc03-l11-skills-u24-engagement-manager-phone-dark.png) |
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-sc03-l11-skills-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-sc03-l11-skills-u16-office-worker-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-sc03-l11-skills-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-sc03-l11-skills-u16-office-worker-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-sc03-l11-skills-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-sc03-l11-skills-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-sc03-l11-skills-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-sc03-l11-skills-u06-hr-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Services › Skills](README.md) |
| Workspaces | [U24](../../../../04-ux/views/u24-engagement-manager/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md) |
| Flows | [FL-F9-04](../../../../02-functional/f09-hr-and-projects/flows/fl-f09-04-grow.md), [FL-SC03-02](../../flows/fl-sc03-02-staff-and-plan.md), [FL-SC03-05](../../flows/fl-sc03-05-client-and-people.md) |

## Open questions

None.

---

⬅️ [S-SC03-L10 Freelance contracts](s-sc03-l10-freelance-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-L12 Shared items](s-sc03-l12-shared-items.md)
