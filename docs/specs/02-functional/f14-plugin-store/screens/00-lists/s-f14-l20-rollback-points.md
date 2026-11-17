🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L20 Rollback points

# 🗂️ S-F14-L20 Rollback points

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F14-20 Rollback point](../../data/e-f14-20-rollback-point.md) the user may see: to find,
filter, total and act on many rollback points at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Rollback points, in the capability's menu (D495).
- **Workspaces:** 1 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "rollback points" offers this view.
- **AI assistant:** "show the rollback points that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Rollback points    Plugin store › Rollback points   [+ New]                                                  |
| [count] [Expired]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] INSTALLATION   STATE                                                                 |
| installation      | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Installation | installation | link to the record | yes |
| State | state | badge: Kept, Restored, Expired | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Kept, Restored, Expired | the visible rows (D488) |
| Installation | each linked installation | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Rollback points of a chosen installation, or of the installations that match a filter.
- From the other side: the installations that have rollback points, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Kept, Restored.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New rollback point | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
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

Open › goes to [S-F14-03 Updates](../01-find-and-install/s-f14-03-updates.md).

The records also show on: [S-F14-26 Version history](../06-release-channels-and-rollback/s-f14-26-version-history.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 rollback points of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no rollback point the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f14-l20-rollback-points-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f14-l20-rollback-points-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f14-l20-rollback-points-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f14-l20-rollback-points-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Rollback points](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F14-01](../../flows/fl-f14-01-find-and-install.md), [FL-F14-06](../../flows/fl-f14-06-release-channels-and-rollback.md), [FL-SC09-06](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-06-compliance-and-certification.md) |

## Open questions

None.

---

⬅️ [S-F14-L19 Support terms](s-f14-l19-support-terms.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L21 Plugin security reviews](s-f14-l21-plugin-security-reviews.md)
