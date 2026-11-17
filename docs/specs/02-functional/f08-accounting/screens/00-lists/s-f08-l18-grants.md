🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L18 Grants

# 🗂️ S-F8-L18 Grants

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U54: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F8-18 Grant](../../data/e-f08-18-grant.md) the user may see: to find, filter, total and
act on many grants at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Grants, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "grants" offers this view.
- **AI assistant:** "show the grants that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Grants    Accounting › Grants   [+ New]                                                                      |
| [count] [total amount] [new this month]   [chart: count by state, amount stacked]                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] FUNDER   STATE   AMOUNT   CONDITIONS AND PERIOD   REPORT DUE                         |
| funder            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Funder | funder | text | yes |
| State | state | badge: Granted, Received, Closed | yes |
| Amount | amount | amount, right-aligned | yes |
| Conditions and period | conditions and period | date | yes |
| Report due | report due | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Granted, Received, Closed | the visible rows (D488) |
| Funder | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Grants of a chosen funder, or of the funders that match a filter.
- From the other side: the funders that have grants, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- New this month, by conditions and period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Granted, Received.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New grant | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- conditions and period: editable in its cell unless the record's state locks it.
- report due: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F8-22 Grants](../07-client-money-grants-and-non-profits/s-f08-22-grants.md).

The records also show on:
[S-SC08-08 Grants](../../../../08-sectors/sc08-non-profit/screens/03-grants/s-sc08-08-grants.md),
[S-SC04-14 Activity reports](../../../../08-sectors/sc04-home-care/screens/05-people-and-quality/s-sc04-14-activity-reports.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 grants of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no grant the user may see yet, with the create action when allowed.
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
| Listed, U31, view Open: Granted, Received | desktop | ![Listed, U31, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u31-treasurer-desktop-light.png) | ![Listed, U31, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u31-treasurer-desktop-dark.png) |
| Listed, U31, view Open: Granted, Received | phone | ![Listed, U31, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u31-treasurer-phone-light.png) | ![Listed, U31, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u31-treasurer-phone-dark.png) |
| Listed, U13, view Open: Granted, Received | desktop | ![Listed, U13, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Granted, Received | phone | ![Listed, U13, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u13-owner-phone-light.png) | ![Listed, U13, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u13-owner-phone-dark.png) |
| Listed, U05, view Open: Granted, Received | desktop | ![Listed, U05, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Granted, Received | phone | ![Listed, U05, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u05-accounting-phone-dark.png) |
| Listed, U40, view Open: Granted, Received | desktop | ![Listed, U40, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u40-farmer-desktop-light.png) | ![Listed, U40, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u40-farmer-desktop-dark.png) |
| Listed, U40, view Open: Granted, Received | phone | ![Listed, U40, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u40-farmer-phone-light.png) | ![Listed, U40, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u40-farmer-phone-dark.png) |
| Listed, U25, view Open: Granted, Received | desktop | ![Listed, U25, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Open: Granted, Received | phone | ![Listed, U25, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u25-care-coordinator-phone-dark.png) |
| Listed, U09, view Open: Granted, Received | desktop | ![Listed, U09, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Granted, Received | phone | ![Listed, U09, view Open: Granted, Received, light](../../images/lists/s-f08-l18-grants-u09-customer-phone-light.png) | ![Listed, U09, view Open: Granted, Received, dark](../../images/lists/s-f08-l18-grants-u09-customer-phone-dark.png) |
| Listed, U22, view Open | desktop | ![Listed, U22, view Open, light](../../images/lists/s-f08-l18-grants-u22-site-manager-desktop-light.png) | ![Listed, U22, view Open, dark](../../images/lists/s-f08-l18-grants-u22-site-manager-desktop-dark.png) |
| Listed, U22, view Open | phone | ![Listed, U22, view Open, light](../../images/lists/s-f08-l18-grants-u22-site-manager-phone-light.png) | ![Listed, U22, view Open, dark](../../images/lists/s-f08-l18-grants-u22-site-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Grants](README.md) |
| Workspaces | [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U22](../../../../04-ux/views/u22-site-manager/workspace.md) |
| Flows | [FL-F8-07](../../flows/fl-f08-07-client-money-grants-and-non-profits.md), [FL-SC04-05](../../../../08-sectors/sc04-home-care/flows/fl-sc04-05-people-and-quality.md), [FL-SC08-02](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-02-donations-and-receipts.md), [FL-SC08-03](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-03-grants.md), [FL-SC08-06](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-06-accounts-and-data.md), [FL-SC12-05](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-05-private-school.md), [FL-SC13-03](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-03-farm-business.md) |

## Open questions

None.

---

⬅️ [S-F8-L17 Client money ledgers](s-f08-l17-client-money-ledgers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L19 Dedicated funds](s-f08-l19-dedicated-funds.md)
