🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Competitive analysis menu](README.md) › 🗂️ S-F17-L16 Tender opportunities

# 🗂️ S-F17-L16 Tender opportunities

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F17-16 Tender opportunity](../../data/e-f17-16-tender-opportunity.md) the user may see:
to find, filter, total and act on many tender opportunities at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Competitive analysis › Tender opportunities, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "tender opportunities" offers this view.
- **AI assistant:** "show the tender opportunities that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Tender opportunities    Competitive analysis › Tender opportunities   [+ New]                                |
| [count] [total estimated amount] [due in 7 days]   [chart: count by state, estimated amount stacked]         |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   STATE   SOURCE   ESTIMATED AMOUNT   DEADLINE   CODES   DECISION              |
| codes             | [ ] ...                                                  Open >                          |
| source            | [ ] ...                                                  Open >                          |
| decision          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| State | state | badge: New, Answering, Skipped, Missed, Awarded | yes |
| Source | source | link to the record | yes |
| Estimated amount | estimated amount | amount, right-aligned | yes |
| Deadline | deadline | date and time | yes |
| Codes | codes | text | yes |
| Decision | decision | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | New, Answering, Skipped, Missed, Awarded | the visible rows (D488) |
| Codes | each value | the visible rows (D488) |
| Source | each linked source | the visible rows (D488) |
| Decision | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Tender opportunities of a chosen source, or of the sources that match a filter.
- From the other side: the sources that have tender opportunities, or none.

## KPI strip

- Count of the visible rows.
- Total of estimated amount.
- Due in 7 days, by deadline.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, estimated amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin
to their home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New tender opportunity | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- codes: editable in its cell unless the record's state locks it.
- deadline: editable in its cell unless the record's state locks it.
- decision: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F17-05 Tenders won](../02-collect-signals/s-f17-05-tenders-won.md).

The records also show on: [S-F17-21 Tender watch](../05-tender-watch/s-f17-21-tender-watch.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 tender opportunities of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no tender opportunity the user may see yet, with the create action when allowed.
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
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f17-l16-tender-opportunities-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f17-l16-tender-opportunities-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f17-l16-tender-opportunities-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f17-l16-tender-opportunities-u03-sales-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f17-l16-tender-opportunities-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f17-l16-tender-opportunities-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f17-l16-tender-opportunities-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f17-l16-tender-opportunities-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Competitive analysis › Tender opportunities](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F17-02](../../flows/fl-f17-02-collect-signals.md), [FL-F17-05](../../flows/fl-f17-05-tender-watch.md) |

## Open questions

None.

---

⬅️ [S-F17-L15 Collection rules](s-f17-l15-collection-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-L17 Price indexes](s-f17-l17-price-indexes.md)
