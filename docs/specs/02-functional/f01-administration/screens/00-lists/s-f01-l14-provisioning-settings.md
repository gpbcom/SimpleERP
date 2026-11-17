🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L14 Provisioning settings

# 🗂️ S-F1-L14 Provisioning settings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F1-14 Provisioning setting](../../data/e-f01-14-provisioning-setting.md) the user may
see: to find, filter, total and act on many provisioning settings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Provisioning settings, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "provisioning settings" offers this view.
- **AI assistant:** "show the provisioning settings that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Provisioning settings    Administration › Provisioning settings   [+ New]                                    |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] STATUS   LAST SYNC                                                                   |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Status | status | badge | yes |
| Last sync | last sync | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Off, Tested, On | the visible rows (D488) |
| Status | Off, Tested, On | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: provisioning settings link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by last sync.

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
| New provisioning setting | header | U07 and the administration roles | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- last sync: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| token | secret | nobody | everyone (VR-4) |

## Row opens

Open › goes to [S-F1-13 Automatic provisioning](../10-bring-users-in-at-scale/s-f01-13-automatic-provisioning.md).

The records also show on: [S-F1-04 User page](../03-user-lifecycle/s-f01-04-user-page.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 provisioning settings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no provisioning setting the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f01-l14-provisioning-settings-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l14-provisioning-settings-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f01-l14-provisioning-settings-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l14-provisioning-settings-u07-administrator-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f01-l14-provisioning-settings-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l14-provisioning-settings-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f01-l14-provisioning-settings-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l14-provisioning-settings-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Provisioning settings](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F1-10](../../flows/fl-f01-10-bring-users-in-at-scale.md) |

## Open questions

None.

---

⬅️ [S-F1-L13 Approval delegations](s-f01-l13-approval-delegations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L15 Bulk invitation batches](s-f01-l15-bulk-invitation-batches.md)
