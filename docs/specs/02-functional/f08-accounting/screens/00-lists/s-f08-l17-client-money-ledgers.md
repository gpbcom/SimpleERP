🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L17 Client money ledgers

# 🗂️ S-F8-L17 Client money ledgers

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U34 Property manager](../../../../01-users/personas/u34-property-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F8-17 Client money ledger](../../data/e-f08-17-client-money-ledger.md) the user may see:
to find, filter, total and act on many client money ledgers at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Client money ledgers, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "client money ledgers" offers this view.
- **AI assistant:** "show the client money ledgers that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Client money ledgers    Accounting › Client money ledgers   [+ New]                                          |
| [count] [total balance] [Open]   [chart: count by state, balance stacked]                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CLIENT   STATE   MATTER OR MANDATE   ACCOUNT   BALANCE                               |
| client            | [ ] ...                                                  Open >                          |
| matter or mandate | [ ] ...                                                  Open >                          |
| account           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Client | client | text | yes |
| State | state | badge: Open, Closed | yes |
| Matter or mandate | matter or mandate | link to the record | yes |
| Account | account | text | yes |
| Balance | balance | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open, Closed | the visible rows (D488) |
| Client | each value | the visible rows (D488) |
| Matter or mandate | each linked matter or mandate | the visible rows (D488) |
| Account | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Client money ledgers of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have client money ledgers, or none.
- Client money ledgers of a chosen client, or of the clients that match a filter.
- From the other side: the clients that have client money ledgers, or none.
- Client money ledgers of a chosen matter or mandate, or of the matter or mandates that match a filter.
- From the other side: the matter or mandates that have client money ledgers, or none.

## KPI strip

- Count of the visible rows.
- Total of balance.
- Needs attention: count in the state Open.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, balance stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Open.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New client money ledger | header | the personas whose roles may create it | the record's own page (Row opens) |
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

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| client | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F8-21 Client money](../07-client-money-grants-and-non-profits/s-f08-21-client-money.md).

The records also show on: [S-F8-06 Bank reconciliation](../03-bank-and-collect/s-f08-06-bank-reconciliation.md),
[S-SC10-05 Client funds](../../../../08-sectors/sc10-real-estate/screens/02-sales/s-sc10-05-client-funds.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 client money ledgers of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no client money ledger the user may see yet, with the create action when allowed.
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
| Listed, U05, view Open: Open | desktop | ![Listed, U05, view Open: Open, light](../../images/lists/s-f08-l17-client-money-ledgers-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Open, dark](../../images/lists/s-f08-l17-client-money-ledgers-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Open | phone | ![Listed, U05, view Open: Open, light](../../images/lists/s-f08-l17-client-money-ledgers-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Open, dark](../../images/lists/s-f08-l17-client-money-ledgers-u05-accounting-phone-dark.png) |
| Listed, U34, view Needs attention | desktop | ![Listed, U34, view Needs attention, light](../../images/lists/s-f08-l17-client-money-ledgers-u34-property-manager-desktop-light.png) | ![Listed, U34, view Needs attention, dark](../../images/lists/s-f08-l17-client-money-ledgers-u34-property-manager-desktop-dark.png) |
| Listed, U34, view Needs attention | phone | ![Listed, U34, view Needs attention, light](../../images/lists/s-f08-l17-client-money-ledgers-u34-property-manager-phone-light.png) | ![Listed, U34, view Needs attention, dark](../../images/lists/s-f08-l17-client-money-ledgers-u34-property-manager-phone-dark.png) |
| Listed, U36, view Open: Open | desktop | ![Listed, U36, view Open: Open, light](../../images/lists/s-f08-l17-client-money-ledgers-u36-professional-desktop-light.png) | ![Listed, U36, view Open: Open, dark](../../images/lists/s-f08-l17-client-money-ledgers-u36-professional-desktop-dark.png) |
| Listed, U36, view Open: Open | phone | ![Listed, U36, view Open: Open, light](../../images/lists/s-f08-l17-client-money-ledgers-u36-professional-phone-light.png) | ![Listed, U36, view Open: Open, dark](../../images/lists/s-f08-l17-client-money-ledgers-u36-professional-phone-dark.png) |
| Listed, U35, view Open: Open | desktop | ![Listed, U35, view Open: Open, light](../../images/lists/s-f08-l17-client-money-ledgers-u35-real-estate-agent-desktop-light.png) | ![Listed, U35, view Open: Open, dark](../../images/lists/s-f08-l17-client-money-ledgers-u35-real-estate-agent-desktop-dark.png) |
| Listed, U35, view Open: Open | phone | ![Listed, U35, view Open: Open, light](../../images/lists/s-f08-l17-client-money-ledgers-u35-real-estate-agent-phone-light.png) | ![Listed, U35, view Open: Open, dark](../../images/lists/s-f08-l17-client-money-ledgers-u35-real-estate-agent-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Client money ledgers](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U34](../../../../04-ux/views/u34-property-manager/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md), [U35](../../../../04-ux/views/u35-real-estate-agent/workspace.md) |
| Flows | [FL-F8-07](../../flows/fl-f08-07-client-money-grants-and-non-profits.md), [FL-SC10-02](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-02-sales.md), [FL-SC10-03](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-03-lettings.md), [FL-SC10-04](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-04-rents-and-landlords.md), [FL-SC11-03](../../../../08-sectors/sc11-professional-firms/flows/fl-sc11-03-time-and-billing.md) |

## Open questions

None.

---

⬅️ [S-F8-L16 Budget plans](s-f08-l16-budget-plans.md) · ⬆️ [Up](README.md) · ➡️ [S-F8-L18 Grants](s-f08-l18-grants.md)
