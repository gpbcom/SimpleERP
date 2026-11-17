🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L30 Script steps

# 🗂️ S-F2-L30 Script steps

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F2-30 Script step](../../data/e-f02-30-script-step.md) the user may see: to find,
filter, total and act on many script steps at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Script steps, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "script steps" offers this view.
- **AI assistant:** "show the script steps that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Script steps    No-code configuration › Script steps   [+ New]                                               |
| [count] [Failed] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   WORKFLOW   VERSION   STATE   AUTHOR                                           |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Workflow | workflow or rule | text | yes |
| Version | version | number | yes |
| State | state | badge: Draft, Tested, Published, Failed, Retired | yes |
| Author | author | person's name | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Tested, Published, Failed, Retired | the visible rows (D488) |
| Workflow | each value | the visible rows (D488) |
| Author | each person | the visible rows (D488) |
| Over limit | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Scripts of a chosen workflow, or of the workflows that match a filter.
- From the other side: the workflows that have scripts, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Failed.
- New this month, by last run.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: author.
- Open: Draft, Tested, Published, Failed.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New script step | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: a script is edited in its editor and published, never in a cell.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| author | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F2-31 Script step editor](../13-low-code-bulk-and-cleaning/s-f02-31-script-step-editor.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 script steps of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no script step the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l30-script-steps-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l30-script-steps-u07-administrator-desktop-dark.png) |
| Listed, U11, view Needs attention | desktop | ![Listed, U11, view Needs attention, light](../../images/lists/s-f02-l30-script-steps-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f02-l30-script-steps-u11-provider-admin-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l30-script-steps-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l30-script-steps-u07-administrator-phone-dark.png) |
| Listed, U11, view Needs attention | phone | ![Listed, U11, view Needs attention, light](../../images/lists/s-f02-l30-script-steps-u11-provider-admin-phone-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f02-l30-script-steps-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Script steps](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F2-13](../../flows/fl-f02-13-low-code-bulk-and-cleaning.md) |

## Open questions

None.

---

⬅️ [S-F2-L29 Workflow templates](s-f02-l29-workflow-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L31 Bulk operations](s-f02-l31-bulk-operations.md)
