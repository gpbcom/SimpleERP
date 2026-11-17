🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customers and sales menu](README.md) › 🗂️ S-F6-L11 Timeline entries

# 🗂️ S-F6-L11 Timeline entries

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F6-11 Timeline entry](../../data/e-f06-11-timeline-entry.md) the user may see: to find,
filter, total and act on many timeline entries at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customers and sales › Timeline entries, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "timeline entries" offers this view.
- **AI assistant:** "show the timeline entries that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Timeline entries    Customers and sales › Timeline entries   [+ New]                                         |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ACCOUNT   STATE   LINK   DATE   KIND                                                 |
| account           | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| link              | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Account | account | text | yes |
| State | state | badge: Recorded | yes |
| Link | link | link to the record | yes |
| Date | date | date and time | yes |
| Kind | kind | label | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recorded | the visible rows (D488) |
| Account | each value | the visible rows (D488) |
| Kind | email, call, meeting, quote, order, invoice, payment, request | the visible rows (D488) |
| Link | each linked link | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Timeline entries of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have timeline entries, or none.
- Timeline entries of a chosen link, or of the links that match a filter.
- From the other side: the links that have timeline entries, or none.

## KPI strip

- Count of the visible rows.
- New this month, by date.

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
| New timeline entry | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- date: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| summary | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F6-15 Account](../06-accounts-and-credit/s-f06-15-account.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 timeline entries of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no timeline entry the user may see yet, with the create action when allowed.
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
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f06-l11-timeline-entries-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f06-l11-timeline-entries-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u03-sales-phone-dark.png) |
| Listed, U41, view All | desktop | ![Listed, U41, view All, light](../../images/lists/s-f06-l11-timeline-entries-u41-customer-success-manager-desktop-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u41-customer-success-manager-desktop-dark.png) |
| Listed, U41, view All | phone | ![Listed, U41, view All, light](../../images/lists/s-f06-l11-timeline-entries-u41-customer-success-manager-phone-light.png) | ![Listed, U41, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u41-customer-success-manager-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f06-l11-timeline-entries-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f06-l11-timeline-entries-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u02-manager-phone-dark.png) |
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f06-l11-timeline-entries-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f06-l11-timeline-entries-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f06-l11-timeline-entries-u12-marketing-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customers and sales › Timeline entries](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U41](../../../../04-ux/views/u41-customer-success-manager/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md) |
| Flows | [FL-F6-06](../../flows/fl-f06-06-accounts-and-credit.md) |

## Open questions

None.

---

⬅️ [S-F6-L10 Rate plan and meters](s-f06-l10-rate-plan-and-meters.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-L12 Credit limits](s-f06-l12-credit-limits.md)
