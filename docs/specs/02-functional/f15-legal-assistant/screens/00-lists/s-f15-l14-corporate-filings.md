🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L14 Corporate filings

# 🗂️ S-F15-L14 Corporate filings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U50 Shareholder](../../../../01-users/personas/u50-shareholder.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F15-14 Corporate filing](../../data/e-f15-14-corporate-filing.md) the user may see: to
find, filter, total and act on many corporate filings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Legal assistant › Corporate filings, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "corporate filings" offers this view.
- **AI assistant:** "show the corporate filings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Corporate filings    Legal assistant › Corporate filings   [+ New]                                           |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CORPORATE FI   DUTY   DECISION   FILED BY   FILED ON   RECEIPT   STATE               |
| duty              | [ ] ...                                                  Open >                          |
| decision          | [ ] ...                                                  Open >                          |
| filed by          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Corporate filing | title | text | yes |
| Duty | duty | link to the record | yes |
| Decision | decision | link to the record | yes |
| Filed by | filed by | person's name | yes |
| Filed on | filed on | date | yes |
| Receipt | receipt | file name | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Duty | each linked duty | the visible rows (D488) |
| Decision | each linked decision | the visible rows (D488) |
| Filed by | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Corporate filings of a chosen compliance duty, or of the compliance duties that match a filter.
- From the other side: the compliance duties that have corporate filings, or none.
- Corporate filings of a chosen register entry, or of the register entries that match a filter.
- From the other side: the register entries that have corporate filings, or none.

## KPI strip

- Count of the visible rows.
- New this month, by filed on.

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
| New corporate filing | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| filed by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F15-07 Compliance calendar](../05-duties-and-records/s-f15-07-compliance-calendar.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 corporate filings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no corporate filing the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f15-l14-corporate-filings-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f15-l14-corporate-filings-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u13-owner-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f15-l14-corporate-filings-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f15-l14-corporate-filings-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u06-hr-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f15-l14-corporate-filings-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f15-l14-corporate-filings-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u05-accounting-phone-dark.png) |
| Listed, U50, view All | desktop | ![Listed, U50, view All, light](../../images/lists/s-f15-l14-corporate-filings-u50-shareholder-desktop-light.png) | ![Listed, U50, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u50-shareholder-desktop-dark.png) |
| Listed, U50, view All | phone | ![Listed, U50, view All, light](../../images/lists/s-f15-l14-corporate-filings-u50-shareholder-phone-light.png) | ![Listed, U50, view All, dark](../../images/lists/s-f15-l14-corporate-filings-u50-shareholder-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Legal assistant › Corporate filings](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U50](../../../../04-ux/views/u50-shareholder/workspace.md) |
| Flows | [FL-F15-05](../../flows/fl-f15-05-duties-and-records.md) |

## Open questions

None.

---

⬅️ [S-F15-L13 Data protection impact assessments](s-f15-l13-data-protection-impact-assessments.md) ·
⬆️ [Up](README.md) · ➡️ [S-F15-L15 Shareholdings](s-f15-l15-shareholdings.md)
