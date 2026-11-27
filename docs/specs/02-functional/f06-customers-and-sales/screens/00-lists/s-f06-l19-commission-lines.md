🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L19 Commission lines

# 🗂️ S-F6-L19 Commission lines

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U51 Reseller partner](../../../../01-users/personas/u51-reseller-partner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F6-19 Commission line](../../data/e-f06-19-commission-line.md) the user may see: to
find, filter, total and act on many commission lines at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Commission lines, in the capability's menu (D495).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "commission lines" offers this view.
- **AI assistant:** "show the commission lines that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Commission lines    Customers and sales › Commission lines   [+ New]                                         |
| [count] [total amount] [new this month]   [chart: count by state, amount stacked]                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REP   STATE   INVOICE   AMOUNT   STATEMENT                                           |
| rep               | [ ] ...                                                  Open >                          |
| invoice           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Rep | rep | person's name | yes |
| State | state | badge: Approved, Paid | yes |
| Invoice | invoice | text | yes |
| Amount | amount | amount, right-aligned | yes |
| Statement | statement | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Approved, Paid | the visible rows (D488) |
| Rep | each person, the user first | the visible rows (D488) |
| Invoice | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Commission lines of a chosen invoice, or of the invoices that match a filter.
- From the other side: the invoices that have commission lines, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- New this month, by statement.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Mine: rep.
- Open: Approved.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New commission line | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the rep; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- statement: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| rep | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| amount | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to
[S-F6-21 Targets and commissions](../09-sell-on-the-road-and-steer-sales/s-f06-21-targets-and-commissions.md).

The records also show on:
[S-SC14-19 Partners](../../../../08-sectors/sc14-it-and-software/screens/02-licences-and-renewals/s-sc14-19-partners.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 commission lines of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no commission line the user may see yet, with the create action when allowed.
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
| Listed, U02, view Open: Approved | desktop | ![Listed, U02, view Open: Approved, light](../../images/lists/s-f06-l19-commission-lines-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Approved, dark](../../images/lists/s-f06-l19-commission-lines-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Approved | phone | ![Listed, U02, view Open: Approved, light](../../images/lists/s-f06-l19-commission-lines-u02-manager-phone-light.png) | ![Listed, U02, view Open: Approved, dark](../../images/lists/s-f06-l19-commission-lines-u02-manager-phone-dark.png) |
| Listed, U13, view Open: Approved | desktop | ![Listed, U13, view Open: Approved, light](../../images/lists/s-f06-l19-commission-lines-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Approved, dark](../../images/lists/s-f06-l19-commission-lines-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Approved | phone | ![Listed, U13, view Open: Approved, light](../../images/lists/s-f06-l19-commission-lines-u13-owner-phone-light.png) | ![Listed, U13, view Open: Approved, dark](../../images/lists/s-f06-l19-commission-lines-u13-owner-phone-dark.png) |
| Listed, U42, view Mine: rep | desktop | ![Listed, U42, view Mine: rep, light](../../images/lists/s-f06-l19-commission-lines-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Mine: rep, dark](../../images/lists/s-f06-l19-commission-lines-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Mine: rep | phone | ![Listed, U42, view Mine: rep, light](../../images/lists/s-f06-l19-commission-lines-u42-sales-representative-phone-light.png) | ![Listed, U42, view Mine: rep, dark](../../images/lists/s-f06-l19-commission-lines-u42-sales-representative-phone-dark.png) |
| Listed, U23, view Open: Approved | desktop | ![Listed, U23, view Open: Approved, light](../../images/lists/s-f06-l19-commission-lines-u23-store-manager-desktop-light.png) | ![Listed, U23, view Open: Approved, dark](../../images/lists/s-f06-l19-commission-lines-u23-store-manager-desktop-dark.png) |
| Listed, U23, view Open: Approved | phone | ![Listed, U23, view Open: Approved, light](../../images/lists/s-f06-l19-commission-lines-u23-store-manager-phone-light.png) | ![Listed, U23, view Open: Approved, dark](../../images/lists/s-f06-l19-commission-lines-u23-store-manager-phone-dark.png) |
| Listed, U03, view Mine: rep | desktop | ![Listed, U03, view Mine: rep, light](../../images/lists/s-f06-l19-commission-lines-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: rep, dark](../../images/lists/s-f06-l19-commission-lines-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: rep | phone | ![Listed, U03, view Mine: rep, light](../../images/lists/s-f06-l19-commission-lines-u03-sales-phone-light.png) | ![Listed, U03, view Mine: rep, dark](../../images/lists/s-f06-l19-commission-lines-u03-sales-phone-dark.png) |
| Listed, U05, view Mine: rep | desktop | ![Listed, U05, view Mine: rep, light](../../images/lists/s-f06-l19-commission-lines-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: rep, dark](../../images/lists/s-f06-l19-commission-lines-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: rep | phone | ![Listed, U05, view Mine: rep, light](../../images/lists/s-f06-l19-commission-lines-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: rep, dark](../../images/lists/s-f06-l19-commission-lines-u05-accounting-phone-dark.png) |
| Listed, U51, view Mine | desktop | ![Listed, U51, view Mine, light](../../images/lists/s-f06-l19-commission-lines-u51-reseller-partner-desktop-light.png) | ![Listed, U51, view Mine, dark](../../images/lists/s-f06-l19-commission-lines-u51-reseller-partner-desktop-dark.png) |
| Listed, U51, view Mine | phone | ![Listed, U51, view Mine, light](../../images/lists/s-f06-l19-commission-lines-u51-reseller-partner-phone-light.png) | ![Listed, U51, view Mine, dark](../../images/lists/s-f06-l19-commission-lines-u51-reseller-partner-phone-dark.png) |
| Listed, U52, view Mine | desktop | ![Listed, U52, view Mine, light](../../images/lists/s-f06-l19-commission-lines-u52-beautician-desktop-light.png) | ![Listed, U52, view Mine, dark](../../images/lists/s-f06-l19-commission-lines-u52-beautician-desktop-dark.png) |
| Listed, U52, view Mine | phone | ![Listed, U52, view Mine, light](../../images/lists/s-f06-l19-commission-lines-u52-beautician-phone-light.png) | ![Listed, U52, view Mine, dark](../../images/lists/s-f06-l19-commission-lines-u52-beautician-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Commission lines](README.md) |
| Workspaces | [U02](../../../../04-ux/views/u02-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U51](../../../../04-ux/views/u51-reseller-partner/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md) |
| Flows | [FL-F6-09](../../flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-SC14-02](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-02-licences-and-renewals.md) |

## Open questions

None.

---

⬅️ [S-F6-L18 Commission plan and targets](s-f06-l18-commission-plan-and-targets.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L20 Leads](s-f06-l20-leads.md)
