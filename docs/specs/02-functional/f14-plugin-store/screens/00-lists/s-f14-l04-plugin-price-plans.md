🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L04 Plugin price plans

# 🗂️ S-F14-L04 Plugin price plans

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F14-04 Plugin price plan](../../data/e-f14-04-plugin-price-plan.md) the user may see: to
find, filter, total and act on many plugin price plans at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Plugin price plans, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "plugin price plans" offers this view.
- **AI assistant:** "show the plugin price plans that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Plugin price plans    Plugin store › Plugin price plans   [+ New]                                            |
| [count] [total price]   [chart: count by state, price stacked]                                               |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PLUGIN   STATE   PRICE                                                               |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Plugin | plugin | link to the record | yes |
| State | state | badge: Published, Paid | yes |
| Price | price | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Published, Paid | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: plugin price plans link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of price.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, price stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Published.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New plugin price plan | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F14-05 Purchase](../02-buy-and-licence/s-f14-05-purchase.md).

The records also show on: [S-F14-12 Pricing](../04-money-and-taxes/s-f14-12-pricing.md),
[S-F14-25 Support terms](../02-buy-and-licence/s-f14-25-support-terms.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 plugin price plans of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no plugin price plan the user may see yet, with the create action when allowed.
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
| Listed, U07, view Open: Published | desktop | ![Listed, U07, view Open: Published, light](../../images/lists/s-f14-l04-plugin-price-plans-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Published, dark](../../images/lists/s-f14-l04-plugin-price-plans-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Published | phone | ![Listed, U07, view Open: Published, light](../../images/lists/s-f14-l04-plugin-price-plans-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Published, dark](../../images/lists/s-f14-l04-plugin-price-plans-u07-administrator-phone-dark.png) |
| Listed, U46, view Open: Published | desktop | ![Listed, U46, view Open: Published, light](../../images/lists/s-f14-l04-plugin-price-plans-u46-plugin-publisher-desktop-light.png) | ![Listed, U46, view Open: Published, dark](../../images/lists/s-f14-l04-plugin-price-plans-u46-plugin-publisher-desktop-dark.png) |
| Listed, U46, view Open: Published | phone | ![Listed, U46, view Open: Published, light](../../images/lists/s-f14-l04-plugin-price-plans-u46-plugin-publisher-phone-light.png) | ![Listed, U46, view Open: Published, dark](../../images/lists/s-f14-l04-plugin-price-plans-u46-plugin-publisher-phone-dark.png) |
| Listed, U13, view Open: Published | desktop | ![Listed, U13, view Open: Published, light](../../images/lists/s-f14-l04-plugin-price-plans-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Published, dark](../../images/lists/s-f14-l04-plugin-price-plans-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Published | phone | ![Listed, U13, view Open: Published, light](../../images/lists/s-f14-l04-plugin-price-plans-u13-owner-phone-light.png) | ![Listed, U13, view Open: Published, dark](../../images/lists/s-f14-l04-plugin-price-plans-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Plugin price plans](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U46](../../../../04-ux/views/u46-plugin-publisher/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F14-02](../../flows/fl-f14-02-buy-and-licence.md), [FL-F14-04](../../flows/fl-f14-04-money-and-taxes.md) |

## Open questions

None.

---

⬅️ [S-F14-L03 Plugin versions](s-f14-l03-plugin-versions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L05 Plugin licences](s-f14-l05-plugin-licences.md)
