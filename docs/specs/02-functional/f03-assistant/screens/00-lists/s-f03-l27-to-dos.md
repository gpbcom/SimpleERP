🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L27 To-dos

# 🗂️ S-F3-L27 To-dos

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F3-27 To-do](../../data/e-f03-27-to-do.md) the user may see: to find, filter, total and
act on many to-dos at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Assistant › To-dos, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "to-dos" offers this view.
- **AI assistant:** "show the to-dos that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| To-dos    Assistant › To-dos   [+ New]                                                                       |
| [count] [Open] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   DUE   LINKED RECORD   SHARED WITH   STATE                                    |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| Due | due date | date | yes |
| Linked record | linked record | text | yes |
| Shared with | shared with | list of people | yes |
| State | state | badge: Open, Done, Dropped | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open, Done, Dropped | the visible rows (D488) |
| Source | each value | the visible rows (D488) |
| Due | each value | the visible rows (D488) |
| Shared with | each person | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- To-dos of a chosen record, or of the records that match a filter.
- From the other side: the records that have to-dos of mine, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count of open to-dos due today or overdue.
- New this month, by due date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: owner, the only view: to-dos are private.
- Open: Open.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New to-do | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- due date: editable in its cell unless the record's state locks it.
- title: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| note | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| done by, at | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| title | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| shared with | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F3-28 My to-dos](../13-voice-agents-and-briefings/s-f03-28-my-to-dos.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 to-dos of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no to-do the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in the image round from this page: one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)). The files are named by the plan.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U01, view Needs attention | phone | ![Listed, U01, view Needs attention, light](../../images/lists/s-f03-l27-to-dos-u01-employee-phone-light.png) | ![Listed, U01, view Needs attention, dark](../../images/lists/s-f03-l27-to-dos-u01-employee-phone-dark.png) |
| Listed, U16, view Needs attention | desktop | ![Listed, U16, view Needs attention, light](../../images/lists/s-f03-l27-to-dos-u16-office-worker-desktop-light.png) | ![Listed, U16, view Needs attention, dark](../../images/lists/s-f03-l27-to-dos-u16-office-worker-desktop-dark.png) |
| Listed, U01, view Mine: owner, the only view: to-dos are private | desktop | ![Listed, U01, view Mine: owner, the only view: to-dos are private, light](../../images/lists/s-f03-l27-to-dos-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: owner, the only view: to-dos are private, dark](../../images/lists/s-f03-l27-to-dos-u01-employee-desktop-dark.png) |
| Listed, U16, view Mine: owner, the only view: to-dos are private | phone | ![Listed, U16, view Mine: owner, the only view: to-dos are private, light](../../images/lists/s-f03-l27-to-dos-u16-office-worker-phone-light.png) | ![Listed, U16, view Mine: owner, the only view: to-dos are private, dark](../../images/lists/s-f03-l27-to-dos-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Assistant › To-dos](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F3-13](../../flows/fl-f03-13-voice-agents-and-briefings.md) |

## Open questions

None.

---

⬅️ [S-F3-L26 Briefings](s-f03-l26-briefings.md) · ⬆️ [Up](README.md)
