🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Manufacturing menu](README.md) › 🗂️ S-SC05-L06 Label templates

# 🗂️ S-SC05-L06 Label templates

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-SC05-06 Label template](../../data/e-sc05-06-label-template.md) the user may see: to
find, filter, total and act on many label templates at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Label templates, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "label templates" offers this view.
- **AI assistant:** "show the label templates that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Label templates    Administration › Label templates   [+ New]                                                |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] LEVEL   STATE   FIELDS                                                               |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Level | level | label | yes |
| State | state | badge: Active | yes |
| Fields | fields | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: label templates link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by fields.

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
| New label template | header | U07 and the administration roles | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- fields: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC05-06 Labels](../03-packaging/s-sc05-06-labels.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 label templates of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no label template the user may see yet, with the create action when allowed.
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
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-sc05-l06-label-templates-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-sc05-l06-label-templates-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-sc05-l06-label-templates-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-sc05-l06-label-templates-u20-production-operator-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-sc05-l06-label-templates-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-sc05-l06-label-templates-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-sc05-l06-label-templates-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-sc05-l06-label-templates-u15-warehouse-operator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Label templates](README.md) |
| Workspaces | [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md) |
| Flows | [FL-SC05-03](../../flows/fl-sc05-03-packaging.md) |

## Open questions

None.

---

⬅️ [S-SC05-L05 Customer-supplied parts](s-sc05-l05-customer-supplied-parts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-L07 Controlled documents](s-sc05-l07-controlled-documents.md)
