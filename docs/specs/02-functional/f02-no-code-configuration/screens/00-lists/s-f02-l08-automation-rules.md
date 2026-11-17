🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L08 Automation rules

# 🗂️ S-F2-L08 Automation rules

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F2-08 Automation rule](../../data/e-f02-08-automation-rule.md) the user may see: to
find, filter, total and act on many automation rules at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Automation rules, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "automation rules" offers this view.
- **AI assistant:** "show the automation rules that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Automation rules    Administration › Automation rules   [+ New]                                              |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATUS   AUTHOR   TRIGGER   CONDITIONS   ACTIONS                              |
| conditions        | [ ] ...                                                  Open >                          |
| actions           | [ ] ...                                                  Open >                          |
| author            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Status | status | badge | yes |
| Author | author | person's name | yes |
| Trigger | trigger | date | yes |
| Conditions | conditions | text | yes |
| Actions | actions | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Paused | the visible rows (D488) |
| Conditions | each value | the visible rows (D488) |
| Actions | each value | the visible rows (D488) |
| Author | each person, the user first | the visible rows (D488) |
| Status | Draft, Published, Paused | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: automation rules link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by trigger.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: author.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New automation rule | header | U07 and the administration roles | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the author; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- trigger: editable in its cell unless the record's state locks it.
- conditions: editable in its cell unless the record's state locks it.
- actions: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| author | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F2-08 Rule editor](../03-automate-with-a-rule/s-f02-08-rule-editor.md).

The records also show on: [S-F2-23 Test cases](../10-change-safely/s-f02-23-test-cases.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 automation rules of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no automation rule the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l08-automation-rules-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l08-automation-rules-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l08-automation-rules-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l08-automation-rules-u07-administrator-phone-dark.png) |
| Listed, U11, view Needs attention | desktop | ![Listed, U11, view Needs attention, light](../../images/lists/s-f02-l08-automation-rules-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f02-l08-automation-rules-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Needs attention | phone | ![Listed, U11, view Needs attention, light](../../images/lists/s-f02-l08-automation-rules-u11-provider-admin-phone-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f02-l08-automation-rules-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Automation rules](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F2-03](../../flows/fl-f02-03-automate-with-a-rule.md), [FL-F2-06](../../flows/fl-f02-06-share-a-configuration.md), [FL-F2-10](../../flows/fl-f02-10-change-safely.md) |

## Open questions

None.

---

⬅️ [S-F2-L07 Email templates](s-f02-l07-email-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L09 Workflows](s-f02-l09-workflows.md)
