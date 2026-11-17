🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L22 Work instruction versions

# 🗂️ S-F12-L22 Work instruction versions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U27: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F12-22 Work instruction version](../../data/e-f12-22-work-instruction-version.md) the
user may see: to find, filter, total and act on many work instruction versions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Work instruction versions, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "work instruction versions" offers this view.
- **AI assistant:** "show the work instruction versions that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Work instruction versions    Manufacturing (plugin) › Work instruction versions   [+ New]                    |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] OPERATION   STATE   VERSION   ACKNOWLEDGED BY                                        |
| operation         | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Operation | operation | text | yes |
| State | state | badge: Draft, Published, Superseded | yes |
| Version | version | date | yes |
| Acknowledged by | acknowledged by | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Superseded | the visible rows (D488) |
| Operation | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Work instruction versions of a chosen operation, or of the operations that match a filter.
- From the other side: the operations that have work instruction versions, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by version.

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
| New work instruction version | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- version: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| acknowledged by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F12-27 Work instructions](../10-people-and-tools/s-f12-27-work-instructions.md).

The records also show on: [S-F12-05 Shop-floor tablet](../03-make-the-products/s-f12-05-shop-floor-tablet.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 work instruction versions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no work instruction version the user may see yet, with the create action when allowed.
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
| Listed, U21, view Needs attention | desktop | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l22-work-instruction-versions-u21-production-planner-desktop-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l22-work-instruction-versions-u21-production-planner-desktop-dark.png) |
| Listed, U21, view Needs attention | phone | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l22-work-instruction-versions-u21-production-planner-phone-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l22-work-instruction-versions-u21-production-planner-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-f12-l22-work-instruction-versions-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f12-l22-work-instruction-versions-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-f12-l22-work-instruction-versions-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f12-l22-work-instruction-versions-u20-production-operator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Work instruction versions](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md) |
| Flows | [FL-F12-10](../../flows/fl-f12-10-people-and-tools.md) |

## Open questions

None.

---

⬅️ [S-F12-L21 Work-in-progress valuations](s-f12-l21-work-in-progress-valuations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L23 Energy readings](s-f12-l23-energy-readings.md)
