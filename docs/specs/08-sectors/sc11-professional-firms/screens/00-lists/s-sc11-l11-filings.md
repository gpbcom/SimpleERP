🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Professional firms menu](README.md) › 🗂️ S-SC11-L11 Filings

# 🗂️ S-SC11-L11 Filings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC11-11 Filing](../../data/e-sc11-11-filing.md) the user may see: to find, filter, total
and act on many filings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Professional firms › Filings, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "filings" offers this view.
- **AI assistant:** "show the filings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Filings    Professional firms › Filings   [+ New]                                                            |
| [count] [due in 7 days]   [chart: count by state]                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| kind              | [ ] CLIENT   STATE   DUE   KIND                                                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Client | client | link to the record | yes |
| State | state | badge: ToDo, Filed | yes |
| Due | due | link to the record | yes |
| Kind | kind | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Kind | each linked kind | the visible rows (D488) |
| State | ToDo, Filed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: filings link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Due in 7 days, by due.

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
| New filing | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- due: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC11-12 Filings](../04-deadlines-and-filings/s-sc11-12-filings.md).

The records also show on: [S-SC11-11 Client portfolio](../04-deadlines-and-filings/s-sc11-11-client-portfolio.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 filings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no filing the user may see yet, with the create action when allowed.
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
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-sc11-l11-filings-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l11-filings-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-sc11-l11-filings-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l11-filings-u36-professional-phone-dark.png) |
| Listed, U37, view All | desktop | ![Listed, U37, view All, light](../../images/lists/s-sc11-l11-filings-u37-assistant-desktop-light.png) | ![Listed, U37, view All, dark](../../images/lists/s-sc11-l11-filings-u37-assistant-desktop-dark.png) |
| Listed, U37, view All | phone | ![Listed, U37, view All, light](../../images/lists/s-sc11-l11-filings-u37-assistant-phone-light.png) | ![Listed, U37, view All, dark](../../images/lists/s-sc11-l11-filings-u37-assistant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Professional firms › Filings](README.md) |
| Workspaces | [U36](../../../../04-ux/views/u36-professional/workspace.md), [U37](../../../../04-ux/views/u37-assistant/workspace.md) |
| Flows | [FL-SC11-04](../../flows/fl-sc11-04-deadlines-and-filings.md) |

## Open questions

None.

---

⬅️ [S-SC11-L10 Matter documents](s-sc11-l10-matter-documents.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-L12 Vigilance records](s-sc11-l12-vigilance-records.md)
