🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L14 Software bill of materials

# 🗂️ S-F14-L14 Software bill of materials

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F14-14 Software bill of materials](../../data/e-f14-14-software-bill-of-materials.md)
the user may see: to find, filter, total and act on many software bill of materials at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Software bill of materials, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "software bill of materials" offers this view.
- **AI assistant:** "show the software bill of materials that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Software bill of materials    Plugin store › Software bill of materials   [+ New]                            |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] VERSION   STATE   COMPONENT   COMPATIBLE   VULNERABILITIES   FORMAT                  |
| version           | [ ] ...                                                  Open >                          |
| component         | [ ] ...                                                  Open >                          |
| compatible        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Version | version | link to the record | yes |
| State | state | badge: Generated, Checked, Published, Rescanned | yes |
| Component | component | text | yes |
| Compatible | compatible | yes or no | yes |
| Vulnerabilities | vulnerabilities | text | yes |
| Format | format | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Generated, Checked, Published, Rescanned | the visible rows (D488) |
| Version | each linked version | the visible rows (D488) |
| Component | each value | the visible rows (D488) |
| Compatible | each value | the visible rows (D488) |
| Vulnerabilities | each value | the visible rows (D488) |
| Format | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Software bill of materials of a chosen component, or of the components that match a filter.
- From the other side: the components that have software bill of materials, or none.
- Software bill of materials of a chosen version, or of the versions that match a filter.
- From the other side: the versions that have software bill of materials, or none.

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
| New software bill of materials | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- compatible: editable in its cell unless the record's state locks it.
- vulnerabilities: editable in its cell unless the record's state locks it.
- format: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F14-21 Dependency report](../03-publish/s-f14-21-dependency-report.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 software bill of materials of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no software bill of materials the user may see yet, with the create action when allowed.
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
| Listed, U46, view All | desktop | ![Listed, U46, view All, light](../../images/lists/s-f14-l14-software-bill-of-materials-u46-plugin-publisher-desktop-light.png) | ![Listed, U46, view All, dark](../../images/lists/s-f14-l14-software-bill-of-materials-u46-plugin-publisher-desktop-dark.png) |
| Listed, U46, view All | phone | ![Listed, U46, view All, light](../../images/lists/s-f14-l14-software-bill-of-materials-u46-plugin-publisher-phone-light.png) | ![Listed, U46, view All, dark](../../images/lists/s-f14-l14-software-bill-of-materials-u46-plugin-publisher-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f14-l14-software-bill-of-materials-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f14-l14-software-bill-of-materials-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f14-l14-software-bill-of-materials-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f14-l14-software-bill-of-materials-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Software bill of materials](README.md) |
| Workspaces | [U46](../../../../04-ux/views/u46-plugin-publisher/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F14-03](../../flows/fl-f14-03-publish.md), [FL-SC14-05](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-05-security-and-data-compliance.md) |

## Open questions

None.

---

⬅️ [S-F14-L13 Usage metrics](s-f14-l13-usage-metrics.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L15 End-of-life notices](s-f14-l15-end-of-life-notices.md)
