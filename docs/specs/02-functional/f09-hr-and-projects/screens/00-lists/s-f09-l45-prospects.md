🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L45 Prospects

# 🗂️ S-F9-L45 Prospects

**Status:** 🔄 waiting for the owner

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-45 Prospect](../../data/e-f09-45-prospect.md) the user may see: to find, filter,
total and act on many prospects at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Prospects, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "prospects" offers this view.
- **AI assistant:** "show the prospects that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Prospects    HR and projects › Prospects   [+ New]                                                           |
| [count] [WaitingForHR] [new this month]   [chart: count by state]                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| sourcing search   | [ ] SOURCING SEARCH   STATE   LOCATION   APPLICANT   AT   KEPT UNTIL   CRITERIA MET AND  |
| location          | [ ] ...                                                  Open >                          |
| criteria met and  | [ ] ...                                                  Open >                          |
| already connected | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Sourcing search | sourcing search | text | yes |
| State | state | badge: Found, Shortlisted, Discarded, Invited, Connected, WaitingForHR, Applicant, Declined, NoAnswer, Erased | yes |
| Location | location | text | yes |
| Applicant | applicant | text | yes |
| At | at | date and time | yes |
| Kept until | kept until | date | yes |
| Criteria met and missed | criteria met and missed | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Sourcing search | each value | the visible rows (D488) |
| Location | each value | the visible rows (D488) |
| Criteria met and missed | each value | the visible rows (D488) |
| Already connected | each value | the visible rows (D488) |
| State | Found, Shortlisted, Discarded, Invited, Connected, WaitingForHR, Applicant, Declined, NoAnswer, Erased | the visible rows (D488) |
| Applicant | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Prospects of a chosen applicant, or of the applicants that match a filter.
- From the other side: the applicants that have prospects, or none.
- Prospects of a chosen location, or of the locations that match a filter.
- From the other side: the locations that have prospects, or none.
- Prospects of a chosen sourcing search, or of the sourcing searches that match a filter.
- From the other side: the sourcing searches that have prospects, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state WaitingForHR.
- New this month, by at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** current position, location.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the sourcing search and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New prospect | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- at: editable in its cell unless the record's state locks it.
- kept until: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| linkedin profile id | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| name | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| profile snapshot | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| score | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| reason | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| criteria met and missed | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| already connected | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| applicant | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-06 Applicant pipeline](../02-recruit/s-f09-06-applicant-pipeline.md).

The records also show on: [S-F9-37 LinkedIn sourcing search](../02-recruit/s-f09-37-linkedin-sourcing-search.md),
[S-F9-38 Outreach sequence](../02-recruit/s-f09-38-outreach-sequence.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 prospects of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no prospect the user may see yet, with the create action when allowed.
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
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f09-l45-prospects-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f09-l45-prospects-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f09-l45-prospects-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f09-l45-prospects-u06-hr-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f09-l45-prospects-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f09-l45-prospects-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f09-l45-prospects-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f09-l45-prospects-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Prospects](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F9-02](../../flows/fl-f09-02-recruit.md), [FL-F9-14](../../flows/fl-f09-14-source-candidates-on-linkedin.md) |

## Open questions

(Proposed) This list waits for the owner's confirmation: its entity was created after the review of 2026-11-13.

---

⬅️ [S-F9-L44 Sourcing searches](s-f09-l44-sourcing-searches.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L46 Outreach sequences](s-f09-l46-outreach-sequences.md)
