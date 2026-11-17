🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: DevOps agents (hosted edition) menu](README.md) › 🗂️ S-F25-L14 Votes

# 🗂️ S-F25-L14 Votes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F25-14 Vote](../../data/e-f25-14-vote.md) the user may see: to find, filter, total and
act on many votes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** DevOps agents (hosted edition) › Votes, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "votes" offers this view.
- **AI assistant:** "show the votes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Votes    DevOps agents (hosted edition) › Votes   [+ New]                                                    |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REQUEST   STATE   COMPANY   DATE                                                     |
| request           | [ ] ...                                                  Open >                          |
| company           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Request | request | link to the record | yes |
| State | state | badge: Counted, Withdrawn | yes |
| Company | company | link to the record | yes |
| Date | date | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Counted, Withdrawn | the visible rows (D488) |
| Request | each linked request | the visible rows (D488) |
| Company | each linked company | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Votes of a chosen company, or of the companies that match a filter.
- From the other side: the companies that have votes, or none.
- Votes of a chosen request, or of the requests that match a filter.
- From the other side: the requests that have votes, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Counted.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New vote | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- date: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F25-12 Approvals](../04-approve-and-govern/s-f25-12-approvals.md).

The records also show on: [S-F25-20 Requests assistant](../05-tell-the-customer/s-f25-20-requests-assistant.md),
[S-F25-24 Public requests](../05-tell-the-customer/s-f25-24-public-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 votes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no vote the user may see yet, with the create action when allowed.
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
| Listed, U13, view Open: Counted | desktop | ![Listed, U13, view Open: Counted, light](../../images/lists/s-f25-l14-votes-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Counted, dark](../../images/lists/s-f25-l14-votes-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Counted | phone | ![Listed, U13, view Open: Counted, light](../../images/lists/s-f25-l14-votes-u13-owner-phone-light.png) | ![Listed, U13, view Open: Counted, dark](../../images/lists/s-f25-l14-votes-u13-owner-phone-dark.png) |
| Listed, U07, view Open: Counted | desktop | ![Listed, U07, view Open: Counted, light](../../images/lists/s-f25-l14-votes-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Counted, dark](../../images/lists/s-f25-l14-votes-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Counted | phone | ![Listed, U07, view Open: Counted, light](../../images/lists/s-f25-l14-votes-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Counted, dark](../../images/lists/s-f25-l14-votes-u07-administrator-phone-dark.png) |
| Listed, U47, view Open: Counted | desktop | ![Listed, U47, view Open: Counted, light](../../images/lists/s-f25-l14-votes-u47-simple-erp-maintainer-desktop-light.png) | ![Listed, U47, view Open: Counted, dark](../../images/lists/s-f25-l14-votes-u47-simple-erp-maintainer-desktop-dark.png) |
| Listed, U47, view Open: Counted | phone | ![Listed, U47, view Open: Counted, light](../../images/lists/s-f25-l14-votes-u47-simple-erp-maintainer-phone-light.png) | ![Listed, U47, view Open: Counted, dark](../../images/lists/s-f25-l14-votes-u47-simple-erp-maintainer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [DevOps agents (hosted edition) › Votes](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U47](../../../../04-ux/views/u47-simple-erp-maintainer/workspace.md) |
| Flows | [FL-F25-04](../../flows/fl-f25-04-approve-and-govern.md), [FL-F25-05](../../flows/fl-f25-05-tell-the-customer.md), [FL-SC10-05](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-05-co-ownership.md) |

## Open questions

None.

---

⬅️ [S-F25-L13 Spec check reports](s-f25-l13-spec-check-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-L15 SPECS features](s-f25-l15-specs-features.md)
