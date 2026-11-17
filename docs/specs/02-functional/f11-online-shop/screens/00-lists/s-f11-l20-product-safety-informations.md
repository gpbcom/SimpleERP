🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Online shop (plugin) menu](README.md) › 🗂️ S-F11-L20 Product safety informations

# 🗂️ S-F11-L20 Product safety informations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F11-20 Product safety information](../../data/e-f11-20-product-safety-information.md)
the user may see: to find, filter, total and act on many product safety informations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Online shop (plugin) › Product safety informations, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "product safety informations" offers this view.
- **AI assistant:** "show the product safety informations that need attention" opens it with the filter as editable
  chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Product safety informations    Online shop (plugin) › Product safety informations   [+ New]                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] MANUFACTURER   STATE                                                                 |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Manufacturer | manufacturer | label | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: product safety informations link to no other record type in their fields.

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
| New product safety information | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F11-25 Product safety](../08-product-content-and-listings/s-f11-25-product-safety.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 product safety informations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no product safety information the user may see yet, with the create action when allowed.
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
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f11-l20-product-safety-informations-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f11-l20-product-safety-informations-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f11-l20-product-safety-informations-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f11-l20-product-safety-informations-u12-marketing-phone-dark.png) |
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f11-l20-product-safety-informations-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f11-l20-product-safety-informations-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f11-l20-product-safety-informations-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f11-l20-product-safety-informations-u04-purchasing-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Online shop (plugin) › Product safety informations](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md) |
| Flows | [FL-F11-08](../../flows/fl-f11-08-product-content-and-listings.md) |

## Open questions

None.

---

⬅️ [S-F11-L19 Product feeds](s-f11-l19-product-feeds.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-L21 Pre-order and reservations](s-f11-l21-pre-order-and-reservations.md)
