🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L17 Rollouts

# 🗂️ S-F14-L17 Rollouts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F14-17 Rollout](../../data/e-f14-17-rollout.md) the user may see: to find, filter, total
and act on many rollouts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Rollouts, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "rollouts" offers this view.
- **AI assistant:** "show the rollouts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Rollouts    Plugin store › Rollouts   [+ New]                                                                |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] VERSION   CURRENT STAGE   STATUS   CHANNEL   STAGES   FAILURE RATE                   |
| version           | [ ] ...                                                  Open >                          |
| channel           | [ ] ...                                                  Open >                          |
| stages            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Version | version | link to the record | yes |
| Current stage | current stage | badge | yes |
| Status | status | badge | yes |
| Channel | channel | text | yes |
| Stages | stages | text | yes |
| Failure rate | failure rate | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Beta, Running, Paused, Done, Stopped | the visible rows (D488) |
| Version | each linked version | the visible rows (D488) |
| Channel | each value | the visible rows (D488) |
| Stages | each value | the visible rows (D488) |
| Current stage | each value | the visible rows (D488) |
| Status | Beta, Running, Paused, Done, Stopped | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Rollouts of a chosen version, or of the versions that match a filter.
- From the other side: the versions that have rollouts, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Beta, Running, Paused.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New rollout | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- channel: editable in its cell unless the record's state locks it.
- stages: editable in its cell unless the record's state locks it.
- failure rate: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F14-23 Release channels](../06-release-channels-and-rollback/s-f14-23-release-channels.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 rollouts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no rollout the user may see yet, with the create action when allowed.
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
| Listed, U46, view Open: Beta, Running, Paused | desktop | ![Listed, U46, view Open: Beta, Running, Paused, light](../../images/lists/s-f14-l17-rollouts-u46-plugin-publisher-desktop-light.png) | ![Listed, U46, view Open: Beta, Running, Paused, dark](../../images/lists/s-f14-l17-rollouts-u46-plugin-publisher-desktop-dark.png) |
| Listed, U46, view Open: Beta, Running, Paused | phone | ![Listed, U46, view Open: Beta, Running, Paused, light](../../images/lists/s-f14-l17-rollouts-u46-plugin-publisher-phone-light.png) | ![Listed, U46, view Open: Beta, Running, Paused, dark](../../images/lists/s-f14-l17-rollouts-u46-plugin-publisher-phone-dark.png) |
| Listed, U07, view Open: Beta, Running, Paused | desktop | ![Listed, U07, view Open: Beta, Running, Paused, light](../../images/lists/s-f14-l17-rollouts-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Beta, Running, Paused, dark](../../images/lists/s-f14-l17-rollouts-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Beta, Running, Paused | phone | ![Listed, U07, view Open: Beta, Running, Paused, light](../../images/lists/s-f14-l17-rollouts-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Beta, Running, Paused, dark](../../images/lists/s-f14-l17-rollouts-u07-administrator-phone-dark.png) |
| Listed, U11, view Open: Beta, Running, Paused | desktop | ![Listed, U11, view Open: Beta, Running, Paused, light](../../images/lists/s-f14-l17-rollouts-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Open: Beta, Running, Paused, dark](../../images/lists/s-f14-l17-rollouts-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Open: Beta, Running, Paused | phone | ![Listed, U11, view Open: Beta, Running, Paused, light](../../images/lists/s-f14-l17-rollouts-u11-provider-admin-phone-light.png) | ![Listed, U11, view Open: Beta, Running, Paused, dark](../../images/lists/s-f14-l17-rollouts-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Rollouts](README.md) |
| Workspaces | [U46](../../../../04-ux/views/u46-plugin-publisher/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F14-06](../../flows/fl-f14-06-release-channels-and-rollback.md) |

## Open questions

None.

---

⬅️ [S-F14-L16 Maintainer transfers](s-f14-l16-maintainer-transfers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L18 Listing translations](s-f14-l18-listing-translations.md)
