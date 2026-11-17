🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customer support agents menu](README.md) › 🗂️ S-F16-L05 Service-level policies

# 🗂️ S-F16-L05 Service-level policies

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F16-05 Service-level policy](../../data/e-f16-05-service-level-policy.md) the user may
see: to find, filter, total and act on many service-level policies at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Service-level policies, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "service-level policies" offers this view.
- **AI assistant:** "show the service-level policies that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Service-level policies    Administration › Service-level policies   [+ New]                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   PRIORITY   FIRST RESPONSE   RESOLUTION                                |
| priority          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Active, Changed, Retired | yes |
| Priority | priority | text | yes |
| First response | first response | number, right-aligned | yes |
| Resolution | resolution | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active, Changed, Retired | the visible rows (D488) |
| Priority | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: service-level policies link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Active, Changed.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New service-level policy | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- priority: editable in its cell unless the record's state locks it.
- first response: editable in its cell unless the record's state locks it.
- resolution: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F16-05 Support dashboard](../03-review-and-monitor/s-f16-05-support-dashboard.md).

The records also show on: [S-F16-07 Service levels](../04-human-agent-workspace/s-f16-07-service-levels.md),
[S-F16-08 Agent workspace](../04-human-agent-workspace/s-f16-08-agent-workspace.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 service-level policies of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no service-level policy the user may see yet, with the create action when allowed.
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
| Listed, U02, view Open: Active, Changed | desktop | ![Listed, U02, view Open: Active, Changed, light](../../images/lists/s-f16-l05-service-level-policies-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Active, Changed, dark](../../images/lists/s-f16-l05-service-level-policies-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Active, Changed | phone | ![Listed, U02, view Open: Active, Changed, light](../../images/lists/s-f16-l05-service-level-policies-u02-manager-phone-light.png) | ![Listed, U02, view Open: Active, Changed, dark](../../images/lists/s-f16-l05-service-level-policies-u02-manager-phone-dark.png) |
| Listed, U13, view Open: Active, Changed | desktop | ![Listed, U13, view Open: Active, Changed, light](../../images/lists/s-f16-l05-service-level-policies-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Active, Changed, dark](../../images/lists/s-f16-l05-service-level-policies-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Active, Changed | phone | ![Listed, U13, view Open: Active, Changed, light](../../images/lists/s-f16-l05-service-level-policies-u13-owner-phone-light.png) | ![Listed, U13, view Open: Active, Changed, dark](../../images/lists/s-f16-l05-service-level-policies-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Service-level policies](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F16-03](../../flows/fl-f16-03-review-and-monitor.md), [FL-F16-04](../../flows/fl-f16-04-human-agent-workspace.md) |

## Open questions

None.

---

⬅️ [S-F16-L04 Helpdesk connections](s-f16-l04-helpdesk-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-L06 Queues](s-f16-l06-queues.md)
