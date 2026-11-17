🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Non-profit association menu](README.md) ›
🗂️ S-SC08-L03 Assembly or board meetings

# 🗂️ S-SC08-L03 Assembly or board meetings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC08-03 Assembly or board meeting](../../data/e-sc08-03-assembly-or-board-meeting.md)
the user may see: to find, filter, total and act on many assembly or board meetings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Non-profit association › Assembly or board meetings, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "assembly or board meetings" offers this view.
- **AI assistant:** "show the assembly or board meetings that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Assembly or board meetings    Non-profit association › Assembly or board meetings   [+ New]                  |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] KIND   STATE   ATTENDANCE   DATE                                                     |
| kind              | [ ] ...                                                  Open >                          |
| attendance        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Kind | kind | link to the record | yes |
| State | state | badge: Active | yes |
| Attendance | attendance | text | yes |
| Date | date | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Kind | each linked kind | the visible rows (D488) |
| Attendance | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Assembly or board meetings of a chosen attendance, or of the attendances that match a filter.
- From the other side: the attendances that have assembly or board meetings, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

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
| New assembly or board meeting | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC08-02 General assembly](../01-members-and-governance/s-sc08-02-general-assembly.md).

The records also show on: [S-SC08-03 Board](../01-members-and-governance/s-sc08-03-board.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 assembly or board meetings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no assembly or board meeting the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u13-owner-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-sc08-l03-assembly-or-board-meetings-u31-treasurer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Non-profit association › Assembly or board meetings](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md) |
| Flows | [FL-SC08-01](../../flows/fl-sc08-01-members-and-governance.md) |

## Open questions

None.

---

⬅️ [S-SC08-L02 Dues payments](s-sc08-l02-dues-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-L04 Gifts](s-sc08-l04-gifts.md)
