🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L14 Product compliance files

# 🗂️ S-F12-L14 Product compliance files

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F12-14 Product compliance file](../../data/e-f12-14-product-compliance-file.md) the user
may see: to find, filter, total and act on many product compliance files at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Product compliance files, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "product compliance files" offers this view.
- **AI assistant:** "show the product compliance files that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Product compliance files    Manufacturing (plugin) › Product compliance files   [+ New]                      |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| product           | [ ] PRODUCT   STATE                                                                      |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | text | yes |
| State | state | badge: Complete, Incomplete | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Product | each value | the visible rows (D488) |
| State | Complete, Incomplete | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Product compliance files of a chosen product, or of the products that match a filter.
- From the other side: the products that have product compliance files, or none.

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
| New product compliance file | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F12-16 Compliance file](../07-compliance-and-safety/s-f12-16-compliance-file.md).

The records also show on:
[S-F12-29 Product passport](../13-energy-passport-and-work-in-progress/s-f12-29-product-passport.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 product compliance files of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no product compliance file the user may see yet, with the create action when allowed.
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
| Listed, U21, view All | desktop | ![Listed, U21, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u21-production-planner-desktop-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u21-production-planner-desktop-dark.png) |
| Listed, U21, view All | phone | ![Listed, U21, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u21-production-planner-phone-light.png) | ![Listed, U21, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u21-production-planner-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u07-administrator-phone-dark.png) |
| Listed, U27, view All | desktop | ![Listed, U27, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u27-quality-manager-desktop-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u27-quality-manager-desktop-dark.png) |
| Listed, U27, view All | phone | ![Listed, U27, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u27-quality-manager-phone-light.png) | ![Listed, U27, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u27-quality-manager-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f12-l14-product-compliance-files-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f12-l14-product-compliance-files-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Product compliance files](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U27](../../../../04-ux/views/u27-quality-manager/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F12-07](../../flows/fl-f12-07-compliance-and-safety.md), [FL-F12-13](../../flows/fl-f12-13-energy-passport-and-work-in-progress.md) |

## Open questions

None.

---

⬅️ [S-F12-L13 Machine signals](s-f12-l13-machine-signals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L15 Waste register lines](s-f12-l15-waste-register-lines.md)
