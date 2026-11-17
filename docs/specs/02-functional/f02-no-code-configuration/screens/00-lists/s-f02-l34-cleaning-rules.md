🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L34 Cleaning rules

# 🗂️ S-F2-L34 Cleaning rules

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F2-34 Cleaning rule](../../data/e-f02-34-cleaning-rule.md) the user may see: to find,
filter, total and act on many cleaning rules at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Cleaning rules, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "cleaning rules" offers this view.
- **AI assistant:** "show the cleaning rules that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Cleaning rules    No-code configuration › Cleaning rules   [+ New]                                           |
| [count] [Paused] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   RECORD TYPE   KIND   LAST SCAN   STATE                                        |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Record type | record type | text | yes |
| Kind | kind | text | yes |
| Last scan | last scan | date | yes |
| State | state | badge: Draft, Active, Paused | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Active, Paused | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Record type | each value | the visible rows (D488) |
| Action | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Rules of a chosen record type, or of the record types that match a filter.
- From the other side: the record types that have a rule, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Paused.
- New this month, by last scan.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: none, the rules belong to the company.
- Open: Draft, Active, Paused.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New cleaning rule | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- schedule: editable in its cell unless the record's state locks it.

## Hidden fields

None: no field of this list is personal data.

## Row opens

Open › goes to [S-F2-35 Data cleaning](../13-low-code-bulk-and-cleaning/s-f02-35-data-cleaning.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 cleaning rules of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no cleaning rule the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l34-cleaning-rules-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l34-cleaning-rules-u07-administrator-desktop-dark.png) |
| Listed, U16, view Needs attention | desktop | ![Listed, U16, view Needs attention, light](../../images/lists/s-f02-l34-cleaning-rules-u16-office-worker-desktop-light.png) | ![Listed, U16, view Needs attention, dark](../../images/lists/s-f02-l34-cleaning-rules-u16-office-worker-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l34-cleaning-rules-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l34-cleaning-rules-u07-administrator-phone-dark.png) |
| Listed, U16, view Mine: none, the rules belong to the company | phone | ![Listed, U16, view Mine: none, the rules belong to the company, light](../../images/lists/s-f02-l34-cleaning-rules-u16-office-worker-phone-light.png) | ![Listed, U16, view Mine: none, the rules belong to the company, dark](../../images/lists/s-f02-l34-cleaning-rules-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Cleaning rules](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F2-13](../../flows/fl-f02-13-low-code-bulk-and-cleaning.md) |

## Open questions

None.

---

⬅️ [S-F2-L33 Translation entries](s-f02-l33-translation-entries.md) · ⬆️ [Up](README.md)
