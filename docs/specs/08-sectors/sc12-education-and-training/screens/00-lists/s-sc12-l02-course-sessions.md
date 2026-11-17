🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Education and training menu](README.md) › 🗂️ S-SC12-L02 Course sessions

# 🗂️ S-SC12-L02 Course sessions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U39 Trainer](../../../../01-users/personas/u39-trainer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC12-02 Course session](../../data/e-sc12-02-course-session.md) the user may see: to
find, filter, total and act on many course sessions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Education and training › Course sessions, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "course sessions" offers this view.
- **AI assistant:** "show the course sessions that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Course sessions    Education and training › Course sessions   [+ New]                                        |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] COURSE   STATE   TRAINER                                                             |
| course            | [ ] ...                                                  Open >                          |
| trainer           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Course | course | link to the record | yes |
| State | state | badge: Planned, Open | yes |
| Trainer | trainer | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Planned, Open | the visible rows (D488) |
| Course | each linked course | the visible rows (D488) |
| Trainer | each linked trainer | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Course sessions of a chosen course, or of the courses that match a filter.
- From the other side: the courses that have course sessions, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: trainer.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** place, room.
- **Layout:** a plan, [C-18](../../../../04-ux/design-system/components/c-18-plan.md).
- **Marker:** the course and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New course session | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the trainer; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- trainer: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC12-02 Sessions](../01-offer-and-sessions/s-sc12-02-sessions.md).

The records also show on: [S-SC12-16 Timetables](../05-private-school/s-sc12-16-timetables.md),
[S-SC12-20 Training assistant](../03-deliver-and-assess/s-sc12-20-training-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 course sessions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no course session the user may see yet, with the create action when allowed.
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
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-sc12-l02-course-sessions-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-sc12-l02-course-sessions-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-sc12-l02-course-sessions-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-sc12-l02-course-sessions-u38-training-coordinator-phone-dark.png) |
| Listed, U39, view Mine: trainer | desktop | ![Listed, U39, view Mine: trainer, light](../../images/lists/s-sc12-l02-course-sessions-u39-trainer-desktop-light.png) | ![Listed, U39, view Mine: trainer, dark](../../images/lists/s-sc12-l02-course-sessions-u39-trainer-desktop-dark.png) |
| Listed, U39, view Mine: trainer | phone | ![Listed, U39, view Mine: trainer, light](../../images/lists/s-sc12-l02-course-sessions-u39-trainer-phone-light.png) | ![Listed, U39, view Mine: trainer, dark](../../images/lists/s-sc12-l02-course-sessions-u39-trainer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-18 Plan](../../../../04-ux/design-system/components/c-18-plan.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Education and training › Course sessions](README.md) |
| Workspaces | [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U39](../../../../04-ux/views/u39-trainer/workspace.md) |
| Flows | [FL-SC12-01](../../flows/fl-sc12-01-offer-and-sessions.md), [FL-SC12-02](../../flows/fl-sc12-02-enrol-and-fund.md), [FL-SC12-03](../../flows/fl-sc12-03-deliver-and-assess.md), [FL-SC12-05](../../flows/fl-sc12-05-private-school.md) |

## Open questions

None.

---

⬅️ [S-SC12-L01 Courses](s-sc12-l01-courses.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-L03 Enrolments](s-sc12-l03-enrolments.md)
