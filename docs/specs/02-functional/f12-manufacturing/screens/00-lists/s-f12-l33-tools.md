🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L33 Tools

# 🗂️ S-F12-L33 Tools

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F12-33 Tool](../../data/e-f12-33-tool.md) the user may see: to find, filter, total and
act on many tools at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing › Tools, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "tools" offers this view.
- **AI assistant:** "show the tools that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Tools    Manufacturing › Tools   [+ New]                                                                     |
| [count] [Blocked] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TOOL   KIND   COUNT   LIMIT   STATE                                                  |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Tool | reference | text | yes |
| Kind | kind | text | yes |
| Count | count | number | yes |
| Limit | life limit | number | yes |
| State | state | badge: Available, In use, Blocked, In maintenance, Retired | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Available, In use, Blocked, In maintenance, Retired | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Mounted on | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Tools mounted on a chosen work centre, or on the centres that match a filter.
- From the other side: the work centres with a tool, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Blocked.
- New this month, by last refurbished.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: work centre.
- Open: In use.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New tool | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: counts change by production, never by editing.

## Hidden fields

None: no field of this list is personal data.

## Row opens

Open › goes to [S-F12-34 Tools and moulds](../14-cad-kanban-mps-and-tools/s-f12-34-tools-and-moulds.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 tools of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no tool the user may see yet, with the create action when allowed.
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
| Listed, U27, view Needs attention | desktop | ![Listed, U27, view Needs attention, light](../../images/lists/s-f12-l33-tools-u27-quality-manager-desktop-light.png) | ![Listed, U27, view Needs attention, dark](../../images/lists/s-f12-l33-tools-u27-quality-manager-desktop-dark.png) |
| Listed, U20, view Mine: work centre | desktop | ![Listed, U20, view Mine: work centre, light](../../images/lists/s-f12-l33-tools-u20-production-operator-desktop-light.png) | ![Listed, U20, view Mine: work centre, dark](../../images/lists/s-f12-l33-tools-u20-production-operator-desktop-dark.png) |
| Listed, U20, view Mine: work centre | phone | ![Listed, U20, view Mine: work centre, light](../../images/lists/s-f12-l33-tools-u20-production-operator-phone-light.png) | ![Listed, U20, view Mine: work centre, dark](../../images/lists/s-f12-l33-tools-u20-production-operator-phone-dark.png) |
| Listed, U27, view Mine: work centre | phone | ![Listed, U27, view Mine: work centre, light](../../images/lists/s-f12-l33-tools-u27-quality-manager-phone-light.png) | ![Listed, U27, view Mine: work centre, dark](../../images/lists/s-f12-l33-tools-u27-quality-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing › Tools](README.md) |
| Workspaces | [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md) |
| Flows | [FL-F12-14](../../flows/fl-f12-14-cad-kanban-mps-and-tools.md) |

## Open questions

None.

---

⬅️ [S-F12-L32 MPS lines](s-f12-l32-mps-lines.md) · ⬆️ [Up](README.md)
