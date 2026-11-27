🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L21 Plugin security reviews

# 🗂️ S-F14-L21 Plugin security reviews

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F14-21 Plugin security review](../../data/e-f14-21-plugin-security-review.md) the user
may see: to find, filter, total and act on many plugin security reviews at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Plugin security reviews, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "plugin security reviews" offers this view.
- **AI assistant:** "show the plugin security reviews that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Plugin security reviews    Plugin store › Plugin security reviews   [+ New]                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PLUGIN SECURITY REVIEW   STATE                                                       |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Plugin security review | the record's title | text | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: plugin security reviews link to no other record type in their fields.

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
| New plugin security review | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F14-10 Security review](../03-publish/s-f14-10-security-review.md).

The records also show on: [S-F14-22 Plugin lifecycle](../07-plugin-end-of-life/s-f14-22-plugin-lifecycle.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 plugin security reviews of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no plugin security review the user may see yet, with the create action when allowed.
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
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f14-l21-plugin-security-reviews-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f14-l21-plugin-security-reviews-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f14-l21-plugin-security-reviews-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f14-l21-plugin-security-reviews-u11-provider-admin-phone-dark.png) |
| Listed, U46, view All | desktop | ![Listed, U46, view All, light](../../images/lists/s-f14-l21-plugin-security-reviews-u46-plugin-publisher-desktop-light.png) | ![Listed, U46, view All, dark](../../images/lists/s-f14-l21-plugin-security-reviews-u46-plugin-publisher-desktop-dark.png) |
| Listed, U46, view All | phone | ![Listed, U46, view All, light](../../images/lists/s-f14-l21-plugin-security-reviews-u46-plugin-publisher-phone-light.png) | ![Listed, U46, view All, dark](../../images/lists/s-f14-l21-plugin-security-reviews-u46-plugin-publisher-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f14-l21-plugin-security-reviews-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f14-l21-plugin-security-reviews-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f14-l21-plugin-security-reviews-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f14-l21-plugin-security-reviews-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Plugin security reviews](README.md) |
| Workspaces | [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U46](../../../../04-ux/views/u46-plugin-publisher/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F14-03](../../flows/fl-f14-03-publish.md), [FL-F14-07](../../flows/fl-f14-07-plugin-end-of-life.md) |

## Open questions

None.

---

⬅️ [S-F14-L20 Rollback points](s-f14-l20-rollback-points.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L22 Test instances](s-f14-l22-test-instances.md)
