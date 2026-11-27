🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L30 CAD documents

# 🗂️ S-F12-L30 CAD documents

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F12-30 CAD document](../../data/e-f12-30-cad-document.md) the user may see: to find,
filter, total and act on many cad documents at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing › CAD documents, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "cad documents" offers this view.
- **AI assistant:** "show the cad documents that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| CAD documents    Manufacturing › CAD documents   [+ New]                                                     |
| [count] [In review] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REFERENCE   REVISION   FORMAT   LINKED TO   STATE                                    |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Reference | reference | text | yes |
| Revision | revision | text | yes |
| Format | format | text | yes |
| Linked to | linked to | text | yes |
| State | state | badge: Draft, In review, Released, Superseded, Withdrawn | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, In review, Released, Superseded, Withdrawn | the visible rows (D488) |
| Format | each value | the visible rows (D488) |
| Linked to | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Documents of a chosen product, or of the products that match a filter.
- From the other side: the products with a released drawing, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state In review.
- New this month, by released at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: reviewer.
- Open: Released.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New CAD document | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: revisions change state by action, never by editing.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| released by, at | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F12-31 CAD link](../14-cad-kanban-mps-and-tools/s-f12-31-cad-link.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 cad documents of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no CAD document the user may see yet, with the create action when allowed.
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
| Listed, U21, view Needs attention | desktop | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l30-cad-documents-u21-production-planner-desktop-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l30-cad-documents-u21-production-planner-desktop-dark.png) |
| Listed, U27, view Needs attention | desktop | ![Listed, U27, view Needs attention, light](../../images/lists/s-f12-l30-cad-documents-u27-quality-manager-desktop-light.png) | ![Listed, U27, view Needs attention, dark](../../images/lists/s-f12-l30-cad-documents-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view Mine: reviewer | phone | ![Listed, U27, view Mine: reviewer, light](../../images/lists/s-f12-l30-cad-documents-u27-quality-manager-phone-light.png) | ![Listed, U27, view Mine: reviewer, dark](../../images/lists/s-f12-l30-cad-documents-u27-quality-manager-phone-dark.png) |
| Listed, U21, view Mine: reviewer | phone | ![Listed, U21, view Mine: reviewer, light](../../images/lists/s-f12-l30-cad-documents-u21-production-planner-phone-light.png) | ![Listed, U21, view Mine: reviewer, dark](../../images/lists/s-f12-l30-cad-documents-u21-production-planner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing › CAD documents](README.md) |
| Workspaces | [U27](../../../../04-ux/views/u27-quality-manager/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md) |
| Flows | [FL-F12-14](../../flows/fl-f12-14-cad-kanban-mps-and-tools.md) |

## Open questions

None.

---

⬅️ [S-F12-L29 Unbuild orders](s-f12-l29-unbuild-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L31 Kanban cards](s-f12-l31-kanban-cards.md)
