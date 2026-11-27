🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Manufacturing (plugin) menu](README.md) › 🗂️ S-F12-L25 Recipes

# 🗂️ S-F12-L25 Recipes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F12-25 Recipe](../../data/e-f12-25-recipe.md) the user may see: to find, filter, total
and act on many recipes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Manufacturing (plugin) › Recipes, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "recipes" offers this view.
- **AI assistant:** "show the recipes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Recipes    Manufacturing (plugin) › Recipes   [+ New]                                                        |
| [count] [total cost] [Draft] [new this month]   [chart: count by state, cost stacked]                        |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PRODUCT   STATE   COST   STEPS                                                       |
| product           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | text | yes |
| State | state | badge: Draft, Approved, Superseded | yes |
| Cost | cost | amount, right-aligned | yes |
| Steps | steps | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Approved, Superseded | the visible rows (D488) |
| Product | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Recipes of a chosen product, or of the products that match a filter.
- From the other side: the products that have recipes, or none.

## KPI strip

- Count of the visible rows.
- Total of cost.
- Needs attention: count in the state Draft.
- New this month, by steps.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, cost stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New recipe | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- steps: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F12-30 Recipe and batch](../09-recipes-and-batches/s-f12-30-recipe-and-batch.md).

The records also show on: [S-F12-05 Shop-floor tablet](../03-make-the-products/s-f12-05-shop-floor-tablet.md),
[S-F12-06 Consumption](../03-make-the-products/s-f12-06-consumption.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 recipes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no recipe the user may see yet, with the create action when allowed.
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
| Listed, U21, view Needs attention | desktop | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l25-recipes-u21-production-planner-desktop-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l25-recipes-u21-production-planner-desktop-dark.png) |
| Listed, U21, view Needs attention | phone | ![Listed, U21, view Needs attention, light](../../images/lists/s-f12-l25-recipes-u21-production-planner-phone-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f12-l25-recipes-u21-production-planner-phone-dark.png) |
| Listed, U20, view All | desktop | ![Listed, U20, view All, light](../../images/lists/s-f12-l25-recipes-u20-production-operator-desktop-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f12-l25-recipes-u20-production-operator-desktop-dark.png) |
| Listed, U20, view All | phone | ![Listed, U20, view All, light](../../images/lists/s-f12-l25-recipes-u20-production-operator-phone-light.png) | ![Listed, U20, view All, dark](../../images/lists/s-f12-l25-recipes-u20-production-operator-phone-dark.png) |
| Listed, U19, view All | desktop | ![Listed, U19, view All, light](../../images/lists/s-f12-l25-recipes-u19-kitchen-staff-desktop-light.png) | ![Listed, U19, view All, dark](../../images/lists/s-f12-l25-recipes-u19-kitchen-staff-desktop-dark.png) |
| Listed, U19, view All | phone | ![Listed, U19, view All, light](../../images/lists/s-f12-l25-recipes-u19-kitchen-staff-phone-light.png) | ![Listed, U19, view All, dark](../../images/lists/s-f12-l25-recipes-u19-kitchen-staff-phone-dark.png) |
| Listed, U40, view All | desktop | ![Listed, U40, view All, light](../../images/lists/s-f12-l25-recipes-u40-farmer-desktop-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-f12-l25-recipes-u40-farmer-desktop-dark.png) |
| Listed, U40, view All | phone | ![Listed, U40, view All, light](../../images/lists/s-f12-l25-recipes-u40-farmer-phone-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-f12-l25-recipes-u40-farmer-phone-dark.png) |
| Listed, U23, view Needs attention | desktop | ![Listed, U23, view Needs attention, light](../../images/lists/s-f12-l25-recipes-u23-store-manager-desktop-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f12-l25-recipes-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Needs attention | phone | ![Listed, U23, view Needs attention, light](../../images/lists/s-f12-l25-recipes-u23-store-manager-phone-light.png) | ![Listed, U23, view Needs attention, dark](../../images/lists/s-f12-l25-recipes-u23-store-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Manufacturing (plugin) › Recipes](README.md) |
| Workspaces | [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U19](../../../../04-ux/views/u19-kitchen-staff/workspace.md), [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md) |
| Flows | [FL-F12-09](../../flows/fl-f12-09-recipes-and-batches.md), [FL-SC05-01](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-01-production-setups.md), [FL-SC06-01](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-01-menus-and-food-safety.md), [FL-SC13-05](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-05-food-processing.md) |

## Open questions

None.

---

⬅️ [S-F12-L24 Product passports](s-f12-l24-product-passports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-L26 Risk assessments](s-f12-l26-risk-assessments.md)
