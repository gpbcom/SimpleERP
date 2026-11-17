🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L14 Funder agreements

# 🗂️ S-F6-L14 Funder agreements

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F6-14 Funder agreement](../../data/e-f06-14-funder-agreement.md) the user may see: to
find, filter, total and act on many funder agreements at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Funder agreements, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "funder agreements" offers this view.
- **AI assistant:** "show the funder agreements that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Funder agreements    Customers and sales › Funder agreements   [+ New]                                       |
| [count] [total share] [Expired] [new this month]   [chart: count by state, share stacked]                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] BENEFICIARY   STATE   FUNDER   SHARE   CAP   PERIOD                                  |
| funder            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Beneficiary | beneficiary | text | yes |
| State | state | badge: Active, Expired | yes |
| Funder | funder | text | yes |
| Share | share | amount, right-aligned | yes |
| Cap | cap | amount, right-aligned | yes |
| Period | period | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active, Expired | the visible rows (D488) |
| Funder | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Funder agreements of a chosen funder, or of the funders that match a filter.
- From the other side: the funders that have funder agreements, or none.

## KPI strip

- Count of the visible rows.
- Total of share.
- Needs attention: count in the state Expired.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, share stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Active.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New funder agreement | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- period: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| beneficiary | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F6-17 Funders and caps](../07-special-invoicing/s-f06-17-funders-and-caps.md).

The records also show on: [S-F6-06 Invoice](../03-invoice-and-get-paid/s-f06-06-invoice.md),
[S-SC04-01 Recipient](../../../../08-sectors/sc04-home-care/screens/01-take-on-a-recipient/s-sc04-01-recipient.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 funder agreements of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no funder agreement the user may see yet, with the create action when allowed.
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
| Listed, U05, view Open: Active | desktop | ![Listed, U05, view Open: Active, light](../../images/lists/s-f06-l14-funder-agreements-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Active, dark](../../images/lists/s-f06-l14-funder-agreements-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Active | phone | ![Listed, U05, view Open: Active, light](../../images/lists/s-f06-l14-funder-agreements-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Active, dark](../../images/lists/s-f06-l14-funder-agreements-u05-accounting-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f06-l14-funder-agreements-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f06-l14-funder-agreements-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f06-l14-funder-agreements-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f06-l14-funder-agreements-u25-care-coordinator-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f06-l14-funder-agreements-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f06-l14-funder-agreements-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f06-l14-funder-agreements-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f06-l14-funder-agreements-u38-training-coordinator-phone-dark.png) |
| Listed, U09, view Open: Active | desktop | ![Listed, U09, view Open: Active, light](../../images/lists/s-f06-l14-funder-agreements-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Active, dark](../../images/lists/s-f06-l14-funder-agreements-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Active | phone | ![Listed, U09, view Open: Active, light](../../images/lists/s-f06-l14-funder-agreements-u09-customer-phone-light.png) | ![Listed, U09, view Open: Active, dark](../../images/lists/s-f06-l14-funder-agreements-u09-customer-phone-dark.png) |
| Listed, U33, view Open: Active | desktop | ![Listed, U33, view Open: Active, light](../../images/lists/s-f06-l14-funder-agreements-u33-medical-secretary-desktop-light.png) | ![Listed, U33, view Open: Active, dark](../../images/lists/s-f06-l14-funder-agreements-u33-medical-secretary-desktop-dark.png) |
| Listed, U33, view Open: Active | phone | ![Listed, U33, view Open: Active, light](../../images/lists/s-f06-l14-funder-agreements-u33-medical-secretary-phone-light.png) | ![Listed, U33, view Open: Active, dark](../../images/lists/s-f06-l14-funder-agreements-u33-medical-secretary-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Funder agreements](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U33](../../../../04-ux/views/u33-medical-secretary/workspace.md) |
| Flows | [FL-F6-07](../../flows/fl-f06-07-special-invoicing.md), [FL-SC04-01](../../../../08-sectors/sc04-home-care/flows/fl-sc04-01-take-on-a-recipient.md), [FL-SC04-04](../../../../08-sectors/sc04-home-care/flows/fl-sc04-04-bill-and-fund.md), [FL-SC09-03](../../../../08-sectors/sc09-health-practices/flows/fl-sc09-03-insurance-billing.md), [FL-SC12-02](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-02-enrol-and-fund.md) |

## Open questions

None.

---

⬅️ [S-F6-L13 Public buyer settings](s-f06-l13-public-buyer-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L15 Pro-forma invoices](s-f06-l15-pro-forma-invoices.md)
