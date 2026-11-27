🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Purchasing and stock menu](README.md) › 🗂️ S-F7-L06 Items

# 🗂️ S-F7-L06 Items

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U17 Cashier](../../../../01-users/personas/u17-cashier.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09, U14, U20, U21, U42, U53: their use cases only read these records, inside a screen of the use
case, so they open them from there (D493).

## Purpose

The aggregated list of every [E-F7-06 Item](../../data/e-f07-06-item.md) the user may see: to find, filter, total and
act on many items at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Purchasing and stock › Items, in the capability's menu (D495).
- **Workspaces:** 10 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "items" offers this view.
- **AI assistant:** "show the items that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Items    Purchasing and stock › Items   [+ New]                                                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   KIND   CATEGORY                                                       |
| kind              | [ ] ...                                                  Open >                          |
| category          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Active | yes |
| Kind | kind | label | yes |
| Category | category | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Kind | stocked, consumable, service, kit | the visible rows (D488) |
| Category | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: items link to no other record type in their fields.

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
| New item | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- category: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F7-03 Receipt](../02-receive-and-store/s-f07-03-receipt.md).

The records also show on: [S-F7-05 Replenishment](../03-replenish/s-f07-05-replenishment.md),
[S-F7-06 Pick, pack and ship](../04-pick-pack-and-ship/s-f07-06-pick-pack-and-ship.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 items of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no item the user may see yet, with the create action when allowed.
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
| Listed, U04, view All | desktop | ![Listed, U04, view All, light](../../images/lists/s-f07-l06-items-u04-purchasing-desktop-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l06-items-u04-purchasing-desktop-dark.png) |
| Listed, U04, view All | phone | ![Listed, U04, view All, light](../../images/lists/s-f07-l06-items-u04-purchasing-phone-light.png) | ![Listed, U04, view All, dark](../../images/lists/s-f07-l06-items-u04-purchasing-phone-dark.png) |
| Listed, U15, view All | desktop | ![Listed, U15, view All, light](../../images/lists/s-f07-l06-items-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l06-items-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view All | phone | ![Listed, U15, view All, light](../../images/lists/s-f07-l06-items-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view All, dark](../../images/lists/s-f07-l06-items-u15-warehouse-operator-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f07-l06-items-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l06-items-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f07-l06-items-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f07-l06-items-u05-accounting-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f07-l06-items-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l06-items-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f07-l06-items-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f07-l06-items-u02-manager-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f07-l06-items-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l06-items-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f07-l06-items-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f07-l06-items-u13-owner-phone-dark.png) |
| Listed, U17, view All | desktop | ![Listed, U17, view All, light](../../images/lists/s-f07-l06-items-u17-cashier-desktop-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f07-l06-items-u17-cashier-desktop-dark.png) |
| Listed, U17, view All | phone | ![Listed, U17, view All, light](../../images/lists/s-f07-l06-items-u17-cashier-phone-light.png) | ![Listed, U17, view All, dark](../../images/lists/s-f07-l06-items-u17-cashier-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f07-l06-items-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f07-l06-items-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f07-l06-items-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f07-l06-items-u23-store-manager-phone-dark.png) |
| Listed, U33, view All | desktop | ![Listed, U33, view All, light](../../images/lists/s-f07-l06-items-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view All, dark](../../images/lists/s-f07-l06-items-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view All | phone | ![Listed, U33, view All, light](../../images/lists/s-f07-l06-items-u33-medical-secretary-phone-light.png) | ![Listed, U33, view All, dark](../../images/lists/s-f07-l06-items-u33-medical-secretary-phone-dark.png) |
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-f07-l06-items-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-f07-l06-items-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-f07-l06-items-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-f07-l06-items-u36-professional-phone-dark.png) |
| Listed, U52, view All | desktop | ![Listed, U52, view All, light](../../images/lists/s-f07-l06-items-u52-beautician-desktop-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-f07-l06-items-u52-beautician-desktop-dark.png) |
| Listed, U52, view All | phone | ![Listed, U52, view All, light](../../images/lists/s-f07-l06-items-u52-beautician-phone-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-f07-l06-items-u52-beautician-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Purchasing and stock › Items](README.md) |
| Workspaces | [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U17](../../../../04-ux/views/u17-cashier/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md) |
| Flows | [FL-F1-02](../../../f01-administration/flows/fl-f01-02-manage-sites.md), [FL-F10-08](../../../f10-point-of-sale/flows/fl-f10-08-vouchers-and-age-checks.md), [FL-F10-10](../../../f10-point-of-sale/flows/fl-f10-10-clienteling-transfers-and-tax-free.md), [FL-F10-11](../../../f10-point-of-sale/flows/fl-f10-11-store-reports.md), [FL-F11-06](../../../f11-online-shop/flows/fl-f11-06-channels-and-legal.md), [FL-F11-08](../../../f11-online-shop/flows/fl-f11-08-product-content-and-listings.md), [FL-F11-09](../../../f11-online-shop/flows/fl-f11-09-pre-orders-and-b2b-buying.md), [FL-F11-10](../../../f11-online-shop/flows/fl-f11-10-fulfil-from-stores-and-report.md), [FL-F12-05](../../../f12-manufacturing/flows/fl-f12-05-subcontracting-and-costs.md), [FL-F12-08](../../../f12-manufacturing/flows/fl-f12-08-report-and-assist.md), [FL-F12-09](../../../f12-manufacturing/flows/fl-f12-09-recipes-and-batches.md), [FL-F12-12](../../../f12-manufacturing/flows/fl-f12-12-quality-engineering.md), [FL-F12-13](../../../f12-manufacturing/flows/fl-f12-13-energy-passport-and-work-in-progress.md), [FL-F21-05](../../../f21-onboarding-and-modules/flows/fl-f21-05-migration-from-another-tool.md), [FL-F6-05](../../../f06-customers-and-sales/flows/fl-f06-05-benchmark-additions.md), [FL-F6-09](../../../f06-customers-and-sales/flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-F7-02](../../flows/fl-f07-02-receive-and-store.md), [FL-F7-03](../../flows/fl-f07-03-replenish.md), [FL-F7-04](../../flows/fl-f07-04-pick-pack-and-ship.md), [FL-F7-05](../../flows/fl-f07-05-count-trace-and-analyse.md), [FL-F7-06](../../flows/fl-f07-06-benchmark-additions.md), [FL-F7-08](../../flows/fl-f07-08-catalogues-and-stock-levels.md), [FL-F7-09](../../flows/fl-f07-09-compliance-and-carbon.md), [FL-SC02-01](../../../../08-sectors/sc02-retail/flows/fl-sc02-01-set-up-the-stores.md), [FL-SC02-02](../../../../08-sectors/sc02-retail/flows/fl-sc02-02-keep-stock-right.md), [FL-SC02-03](../../../../08-sectors/sc02-retail/flows/fl-sc02-03-sell-and-return-across-channels.md), [FL-SC05-02](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-02-made-to-order.md), [FL-SC05-03](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-03-packaging.md), [FL-SC05-05](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-05-suppliers-and-customers.md), [FL-SC06-01](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-01-menus-and-food-safety.md), [FL-SC06-02](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-02-kitchen-stock-and-staff.md), [FL-SC07-06](../../../../08-sectors/sc07-transport/flows/fl-sc07-06-logistics-for-clients.md), [FL-SC09-05](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-05-practice-organisation.md), [FL-SC13-01](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-01-crops.md), [FL-SC13-02](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-02-livestock.md), [FL-SC13-03](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-03-farm-business.md), [FL-SC13-04](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-04-sales-and-certification.md), [FL-SC13-05](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-05-food-processing.md), [FL-SC14-04](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-04-product-delivery.md), [FL-SC15-02](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-02-orders.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md) |

## Open questions

None.

---

⬅️ [S-F7-L05 Supplier invoices](s-f07-l05-supplier-invoices.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L07 Locations](s-f07-l07-locations.md)
