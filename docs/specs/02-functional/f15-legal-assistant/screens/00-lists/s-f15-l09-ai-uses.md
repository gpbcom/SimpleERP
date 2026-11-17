🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L09 AI uses

# 🗂️ S-F15-L09 AI uses

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F15-09 AI use](../../data/e-f15-09-ai-use.md) the user may see: to find, filter, total
and act on many ai uses at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Legal assistant › AI uses, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "ai uses" offers this view.
- **AI assistant:** "show the ai uses that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| AI uses    Legal assistant › AI uses   [+ New]                                                               |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FEATURE   STATUS   DATA USED   RISK CLASS                                            |
| feature           | [ ] ...                                                  Open >                          |
| data used         | [ ] ...                                                  Open >                          |
| risk class        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Feature | feature | link to the record | yes |
| Status | status | badge | yes |
| Data used | data used | text | yes |
| Risk class | risk class | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Listed, Assessed, On, Off | the visible rows (D488) |
| Feature | each linked feature | the visible rows (D488) |
| Data used | each value | the visible rows (D488) |
| Risk class | each value | the visible rows (D488) |
| Status | Listed, Assessed, On, Off | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- AI uses of a chosen feature, or of the features that match a filter.
- From the other side: the features that have ai uses, or none.

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
| New ai use | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- data used: editable in its cell unless the record's state locks it.
- risk class: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F15-10 Privacy and AI register](../06-privacy-and-ai-duties/s-f15-10-privacy-and-ai-register.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 ai uses of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no ai use the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f15-l09-ai-uses-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f15-l09-ai-uses-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f15-l09-ai-uses-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f15-l09-ai-uses-u07-administrator-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f15-l09-ai-uses-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f15-l09-ai-uses-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f15-l09-ai-uses-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f15-l09-ai-uses-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Legal assistant › AI uses](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F15-06](../../flows/fl-f15-06-privacy-and-ai-duties.md), [FL-F4-09](../../../f04-meetings/flows/fl-f04-09-score-calls-and-interviews.md) |

## Open questions

None.

---

⬅️ [S-F15-L08 Data-subject requests](s-f15-l08-data-subject-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L10 Lawyer hand-offs](s-f15-l10-lawyer-hand-offs.md)
