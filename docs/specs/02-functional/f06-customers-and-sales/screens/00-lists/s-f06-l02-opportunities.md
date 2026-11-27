🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L02 Opportunities

# 🗂️ S-F6-L02 Opportunities

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U51 Reseller partner](../../../../01-users/personas/u51-reseller-partner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F6-02 Opportunity](../../data/e-f06-02-opportunity.md) the user may see: to find,
filter, total and act on many opportunities at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Opportunities, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "opportunities" offers this view.
- **AI assistant:** "show the opportunities that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Opportunities    Customers and sales › Opportunities   [+ New]                                               |
| [count] [total amount] [due in 7 days]   [chart: count by state, amount stacked]                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CUSTOMER   STAGE   AMOUNT   NEXT ACTIVITY                                            |
| customer          | [ ] ...                                                  Open >                          |
| stage             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Customer | customer | text | yes |
| Stage | stage | badge | yes |
| Amount | amount | amount, right-aligned | yes |
| Next activity | next activity | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Customer | each value | the visible rows (D488) |
| Stage | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Opportunities of a chosen customer, or of the customers that match a filter.
- From the other side: the customers that have opportunities, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- Due in 7 days, by next activity.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New opportunity | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change stage | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- next activity: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F6-01 Pipeline](../01-lead-to-quote/s-f06-01-pipeline.md).

The records also show on: [S-F6-02 Lead](../01-lead-to-quote/s-f06-02-lead.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 opportunities of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no opportunity the user may see yet, with the create action when allowed.
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
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f06-l02-opportunities-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l02-opportunities-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f06-l02-opportunities-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l02-opportunities-u03-sales-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f06-l02-opportunities-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l02-opportunities-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f06-l02-opportunities-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l02-opportunities-u02-manager-phone-dark.png) |
| Listed, U51, view All | desktop | ![Listed, U51, view All, light](../../images/lists/s-f06-l02-opportunities-u51-reseller-partner-desktop-light.png) | ![Listed, U51, view All, dark](../../images/lists/s-f06-l02-opportunities-u51-reseller-partner-desktop-dark.png) |
| Listed, U51, view All | phone | ![Listed, U51, view All, light](../../images/lists/s-f06-l02-opportunities-u51-reseller-partner-phone-light.png) | ![Listed, U51, view All, dark](../../images/lists/s-f06-l02-opportunities-u51-reseller-partner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Opportunities](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U51](../../../../04-ux/views/u51-reseller-partner/workspace.md) |
| Flows | [FL-F17-07](../../../f17-competitive-analysis/flows/fl-f17-07-sales-enablement.md), [FL-F23-03](../../../f23-what-if-simulation/flows/fl-f23-03-see-the-impact.md), [FL-F4-09](../../../f04-meetings/flows/fl-f04-09-score-calls-and-interviews.md), [FL-F6-01](../../flows/fl-f06-01-lead-to-quote.md) |

## Open questions

None.

---

⬅️ [S-F6-L01 Customer records](s-f06-l01-customer-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L03 Quotes](s-f06-l03-quotes.md)
