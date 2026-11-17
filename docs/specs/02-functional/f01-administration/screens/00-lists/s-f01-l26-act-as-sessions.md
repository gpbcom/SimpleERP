🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L26 Act-as sessions

# 🗂️ S-F1-L26 Act-as sessions

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U48: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F1-26 Act-as session](../../data/e-f01-26-act-as-session.md) the user may see: to find,
filter, total and act on many act-as sessions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Act-as sessions, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "act-as sessions" offers this view.
- **AI assistant:** "show the act-as sessions that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Act-as sessions    Administration › Act-as sessions   [+ New]                                                |
| [count] [Active] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TARGET USER   ADMINISTRATOR   REASON   REQUESTED AT   STATE                          |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Target user | target user | person's name | yes |
| Administrator | administrator | person's name | yes |
| Reason | reason | text | yes |
| Requested at | requested at | date and time | yes |
| State | state | badge: Requested, Granted, Refused, Active, Ended, Expired | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Requested, Granted, Refused, Active, Ended, Expired | the visible rows (D488) |
| Administrator | each person | the visible rows (D488) |
| Target user | each person | the visible rows (D488) |
| Ended by | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Sessions of a chosen administrator, or of the administrators that match a filter.
- From the other side: the administrators that have sessions, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Active.
- New this month, by requested at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: target user.
- Open: Requested, Granted, Active.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New act-as session | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: sessions are asked and ended, never edited.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| target user | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| administrator | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| reason | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F1-30 Act as a user](../15-security-and-group-data/s-f01-30-act-as-user.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 act-as sessions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no act-as session the user may see yet, with the create action when allowed.
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
| Listed, U01, view Needs attention | phone | ![Listed, U01, view Needs attention, light](../../images/lists/s-f01-l26-act-as-sessions-u01-employee-phone-light.png) | ![Listed, U01, view Needs attention, dark](../../images/lists/s-f01-l26-act-as-sessions-u01-employee-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l26-act-as-sessions-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l26-act-as-sessions-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l26-act-as-sessions-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l26-act-as-sessions-u07-administrator-phone-dark.png) |
| Listed, U01, view Mine: target user | desktop | ![Listed, U01, view Mine: target user, light](../../images/lists/s-f01-l26-act-as-sessions-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: target user, dark](../../images/lists/s-f01-l26-act-as-sessions-u01-employee-desktop-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Act-as sessions](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F1-15](../../flows/fl-f01-15-security-and-group-data.md) |

## Open questions

None.

---

⬅️ [S-F1-L25 Sharing rules](s-f01-l25-sharing-rules.md) · ⬆️ [Up](README.md)
