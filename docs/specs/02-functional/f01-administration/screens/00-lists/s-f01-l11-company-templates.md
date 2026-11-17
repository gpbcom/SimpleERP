🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L11 Company templates

# 🗂️ S-F1-L11 Company templates

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F1-11 Company template](../../data/e-f01-11-company-template.md) the user may see: to
find, filter, total and act on many company templates at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Company templates, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "company templates" offers this view.
- **AI assistant:** "show the company templates that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Company templates    Administration › Company templates   [+ New]                                            |
| [count] [Template]   [chart: count by state]                                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   SOURCE COMPANY   COPIES                                               |
| source company    | [ ] ...                                                  Open >                          |
| copies            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Template | yes |
| Source company | source company | text | yes |
| Copies | copies | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Template | the visible rows (D488) |
| Source company | each value | the visible rows (D488) |
| Copies | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Company templates of a chosen source company, or of the source companies that match a filter.
- From the other side: the source companies that have company templates, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Template.

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

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New company template | header | U07 and the administration roles | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- copies: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F1-10 Client companies](../08-provider-and-client-companies/s-f01-10-client-companies.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 company templates of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no company template the user may see yet, with the create action when allowed.
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
| Listed, U11, view Needs attention | desktop | ![Listed, U11, view Needs attention, light](../../images/lists/s-f01-l11-company-templates-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f01-l11-company-templates-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Needs attention | phone | ![Listed, U11, view Needs attention, light](../../images/lists/s-f01-l11-company-templates-u11-provider-admin-phone-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f01-l11-company-templates-u11-provider-admin-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l11-company-templates-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l11-company-templates-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l11-company-templates-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l11-company-templates-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Company templates](README.md) |
| Workspaces | [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F1-08](../../flows/fl-f01-08-provider-and-client-companies.md) |

## Open questions

None.

---

⬅️ [S-F1-L10 Single sign-on settings](s-f01-l10-single-sign-on-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L12 Provider sessions](s-f01-l12-provider-sessions.md)
