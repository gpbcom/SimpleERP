🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L19 Dedicated funds

# 🗂️ S-F8-L19 Dedicated funds

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09, U12: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F8-19 Dedicated fund](../../data/e-f08-19-dedicated-fund.md) the user may see: to find,
filter, total and act on many dedicated funds at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Dedicated funds, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "dedicated funds" offers this view.
- **AI assistant:** "show the dedicated funds that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Dedicated funds    Accounting › Dedicated funds   [+ New]                                                    |
| [count] [total balance] [Open]   [chart: count by state, balance stacked]                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PURPOSE   STATE   BALANCE                                                            |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Purpose | purpose | text | yes |
| State | state | badge: Open, Closed | yes |
| Balance | balance | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: dedicated funds link to no other record type in their fields.

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
| New dedicated fund | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F8-23 Non-profit accounts](../07-client-money-grants-and-non-profits/s-f08-23-non-profit-accounts.md).

The records also show on:
[S-SC08-14 Association accounts](../../../../08-sectors/sc08-non-profit/screens/06-accounts-and-data/s-sc08-14-association-accounts.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 dedicated funds of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no dedicated fund the user may see yet, with the create action when allowed.
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
| Listed, U31, view Open: Open | desktop | ![Listed, U31, view Open: Open, light](../../images/lists/s-f08-l19-dedicated-funds-u31-treasurer-desktop-light.png) | ![Listed, U31, view Open: Open, dark](../../images/lists/s-f08-l19-dedicated-funds-u31-treasurer-desktop-dark.png) |
| Listed, U31, view Open: Open | phone | ![Listed, U31, view Open: Open, light](../../images/lists/s-f08-l19-dedicated-funds-u31-treasurer-phone-light.png) | ![Listed, U31, view Open: Open, dark](../../images/lists/s-f08-l19-dedicated-funds-u31-treasurer-phone-dark.png) |
| Listed, U05, view Open: Open | desktop | ![Listed, U05, view Open: Open, light](../../images/lists/s-f08-l19-dedicated-funds-u05-accounting-desktop-light.png) | ![Listed, U05, view Open: Open, dark](../../images/lists/s-f08-l19-dedicated-funds-u05-accounting-desktop-dark.png) |
| Listed, U05, view Open: Open | phone | ![Listed, U05, view Open: Open, light](../../images/lists/s-f08-l19-dedicated-funds-u05-accounting-phone-light.png) | ![Listed, U05, view Open: Open, dark](../../images/lists/s-f08-l19-dedicated-funds-u05-accounting-phone-dark.png) |
| Listed, U08, view Needs attention | desktop | ![Listed, U08, view Needs attention, light](../../images/lists/s-f08-l19-dedicated-funds-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f08-l19-dedicated-funds-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Needs attention | phone | ![Listed, U08, view Needs attention, light](../../images/lists/s-f08-l19-dedicated-funds-u08-external-accountant-phone-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f08-l19-dedicated-funds-u08-external-accountant-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f08-l19-dedicated-funds-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f08-l19-dedicated-funds-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f08-l19-dedicated-funds-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f08-l19-dedicated-funds-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Dedicated funds](README.md) |
| Workspaces | [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F8-07](../../flows/fl-f08-07-client-money-grants-and-non-profits.md), [FL-SC08-06](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-06-accounts-and-data.md) |

## Open questions

None.

---

⬅️ [S-F8-L18 Grants](s-f08-l18-grants.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L20 Volunteer contributions](s-f08-l20-volunteer-contributions.md)
