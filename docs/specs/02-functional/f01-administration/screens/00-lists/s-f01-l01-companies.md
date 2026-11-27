🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L01 Companies

# 🗂️ S-F1-L01 Companies

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F1-01 Company](../../data/e-f01-01-company.md) the user may see: to find, filter, total
and act on many companies at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Companies, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "companies" offers this view.
- **AI assistant:** "show the companies that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Companies    Administration › Companies   [+ New]                                                            |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   FISCAL YEAR START   LEGAL FORM   CURRENCY   VAT REGIME   SECTOR PACK  |
| legal form        | [ ] ...                                                  Open >                          |
| currency          | [ ] ...                                                  Open >                          |
| VAT regime        | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: InSetup, Active | yes |
| Fiscal year start | fiscal year start | date | yes |
| Legal form | legal form | text | yes |
| Currency | currency | text | yes |
| VAT regime | vat regime | text | yes |
| Sector pack | sector pack | text | yes |
| Setup step | setup step | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | InSetup, Active | the visible rows (D488) |
| Legal form | each value | the visible rows (D488) |
| Currency | each value | the visible rows (D488) |
| VAT regime | each value | the visible rows (D488) |
| Sector pack | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: companies link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by fiscal year start.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

- **Place:** address.
- **Layout:** a map, [C-17](../../../../04-ux/design-system/components/c-17-map.md).
- **Marker:** the name and the state.
- **Layers:** by state.
- **Who sees the switch:** the roles with the map right, the planner roles and U02 and U13 (BR-F1-32, D502); the others
  see the table with the place as a column.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New company | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- legal form: editable in its cell unless the record's state locks it.
- currency: editable in its cell unless the record's state locks it.
- fiscal year start: editable in its cell unless the record's state locks it.
- VAT regime: editable in its cell unless the record's state locks it.
- sector pack: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F1-23 Close the company](../14-close-a-company/s-f01-23-close-the-company.md).

The records also show on: [S-F1-01 Setup wizard](../01-guided-setup/s-f01-01-setup-wizard.md),
[S-F1-10 Client companies](../08-provider-and-client-companies/s-f01-10-client-companies.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 companies of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no company the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

On the map layout, Listed also shows the count of rows without a place.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491); the map takes the full width.

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button. The table holds the
same rows as the map.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f01-l01-companies-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l01-companies-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f01-l01-companies-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l01-companies-u07-administrator-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f01-l01-companies-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f01-l01-companies-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f01-l01-companies-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f01-l01-companies-u13-owner-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f01-l01-companies-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l01-companies-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f01-l01-companies-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l01-companies-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md),
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Companies](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F1-01](../../flows/fl-f01-01-guided-setup.md), [FL-F1-08](../../flows/fl-f01-08-provider-and-client-companies.md), [FL-F1-14](../../flows/fl-f01-14-close-a-company.md), [FL-F15-01](../../../f15-legal-assistant/flows/fl-f15-01-ask-a-legal-question.md), [FL-F21-01](../../../f21-onboarding-and-modules/flows/fl-f21-01-first-run.md), [FL-F22-07](../../../f22-unified-cost-management/flows/fl-f22-07-it-provider-re-billing.md), [FL-F7-06](../../../f07-purchasing-and-stock/flows/fl-f07-06-benchmark-additions.md), [FL-F8-07](../../../f08-accounting/flows/fl-f08-07-client-money-grants-and-non-profits.md), [FL-F9-09](../../../f09-hr-and-projects/flows/fl-f09-09-train-and-protect.md), [FL-SC08-02](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-02-donations-and-receipts.md), [FL-SC08-06](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-06-accounts-and-data.md), [FL-SC14-06](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-06-portal-and-metrics.md) |

## Open questions

None.

---

⬅️ [S-F1-30 Act as a user](../15-security-and-group-data/s-f01-30-act-as-user.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L02 Company sites](s-f01-l02-company-sites.md)
