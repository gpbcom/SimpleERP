🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L33 Automatic scheduling settings

# 🗂️ S-F9-L33 Automatic scheduling settings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F9-33 Automatic scheduling setting](../../data/e-f09-33-automatic-scheduling-setting.md)
the user may see: to find, filter, total and act on many automatic scheduling settings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Automatic scheduling settings, in the Administration menu (D494).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "automatic scheduling settings" offers this view.
- **AI assistant:** "show the automatic scheduling settings that need attention" opens it with the filter as editable
  chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Automatic scheduling settings    Administration › Automatic scheduling settings   [+ New]                    |
| [count] [total cost limit] [new this month]   [chart: count by state, cost limit stacked]                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| team              | [ ] TEAM   STATE   SWITCHED BY   PLANNERS NOTIFIED   COST LIMIT   SWITCHED AT   STOPPING |
| state             | [ ] ...                                                  Open >                          |
| switched by       | [ ] ...                                                  Open >                          |
| stopping problems | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Team | team | text | yes |
| State | state | badge: Off, On | yes |
| Switched by | switched by | person's name | yes |
| Planners notified | planners notified | person's name | yes |
| Cost limit | cost limit | amount, right-aligned | yes |
| Switched at | switched at | date and time | yes |
| Stopping problems | stopping problems | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Team | each value | the visible rows (D488) |
| State | Off, On | the visible rows (D488) |
| Switched by | each person, the user first | the visible rows (D488) |
| Stopping problems | each value | the visible rows (D488) |
| Planners notified | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Automatic scheduling settings of a chosen team, or of the teams that match a filter.
- From the other side: the teams that have automatic scheduling settings, or none.

## KPI strip

- Count of the visible rows.
- Total of cost limit.
- New this month, by switched at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, cost limit stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Mine: switched by.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New automatic scheduling setting | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the switched by; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- switched at: editable in its cell unless the record's state locks it.
- stopping problems: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| switched by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| planners notified | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-30 Scheduling board](../12-schedule-customer-requests/s-f09-30-scheduling-board.md).

The records also show on:
[S-F9-32 Automatic scheduling settings](../12-schedule-customer-requests/s-f09-32-automatic-scheduling-settings.md),
[S-F9-31 Proposal review](../12-schedule-customer-requests/s-f09-31-proposal-review.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 automatic scheduling settings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no automatic scheduling setting the user may see yet, with the create action when allowed.
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
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u02-manager-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u07-administrator-phone-dark.png) |
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u29-dispatcher-phone-dark.png) |
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-f09-l33-automatic-scheduling-settings-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f09-l33-automatic-scheduling-settings-u25-care-coordinator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Automatic scheduling settings](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md) |
| Flows | [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md) |

## Open questions

None.

---

⬅️ [S-F9-L32 Live positions](s-f09-l32-live-positions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L34 Attendance kiosks](s-f09-l34-attendance-kiosks.md)
