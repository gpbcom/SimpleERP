🏠 [Specs](../../../../README.md) › ⚙️ [Technical capabilities](../../../README.md) ›
🚀 [T9 Install, backups and updates](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Install, backups and updates menu](README.md) › 🗂️ S-T09-L02 Restore points

# 🗂️ S-T09-L02 Restore points

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-T09-02 Restore point](../../data/e-t09-02-restore-point.md) the user may see: to find,
filter, total and act on many restore points at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Restore points, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "restore points" offers this view.
- **AI assistant:** "show the restore points that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Restore points    Administration › Restore points   [+ New]                                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] COMPANY   STATE   LOCATION                                                           |
| company           | [ ] ...                                                  Open >                          |
| location          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Company | company | link to the record | yes |
| State | state | badge: Active | yes |
| Location | location | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Company | each linked company | the visible rows (D488) |
| Location | each linked location | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Restore points of a chosen company, or of the companies that match a filter.
- From the other side: the companies that have restore points, or none.
- Restore points of a chosen location, or of the locations that match a filter.
- From the other side: the locations that have restore points, or none.

## KPI strip

- Count of the visible rows.

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
| New restore point | header | U07 and the administration roles | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: no field is editable in a cell.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-T09-02 Restore point](../s-t09-02-restore-point.md), drawn in step 36j.

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 restore points of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no restore point the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-t09-l02-restore-points-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-t09-l02-restore-points-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-t09-l02-restore-points-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-t09-l02-restore-points-u07-administrator-phone-dark.png) |
| Listed, U48, view All | desktop | ![Listed, U48, view All, light](../../images/lists/s-t09-l02-restore-points-u48-hosting-engineer-desktop-light.png) | ![Listed, U48, view All, dark](../../images/lists/s-t09-l02-restore-points-u48-hosting-engineer-desktop-dark.png) |
| Listed, U48, view All | phone | ![Listed, U48, view All, light](../../images/lists/s-t09-l02-restore-points-u48-hosting-engineer-phone-light.png) | ![Listed, U48, view All, dark](../../images/lists/s-t09-l02-restore-points-u48-hosting-engineer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Restore points](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U48](../../../../04-ux/views/u48-hosting-engineer/workspace.md) |
| Flows | None |

## Open questions

None.

---

⬅️ [S-T09-L01 Server installations](s-t09-l01-server-installations.md) · ⬆️ [Up](README.md) ·
➡️ [S-T09-L03 Upgrade runs](s-t09-l03-upgrade-runs.md)
