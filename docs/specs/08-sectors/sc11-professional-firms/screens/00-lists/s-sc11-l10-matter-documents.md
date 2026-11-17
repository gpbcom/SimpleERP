🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Professional firms menu](README.md) › 🗂️ S-SC11-L10 Matter documents

# 🗂️ S-SC11-L10 Matter documents

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC11-10 Matter document](../../data/e-sc11-10-matter-document.md) the user may see: to
find, filter, total and act on many matter documents at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Professional firms › Matter documents, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "matter documents" offers this view.
- **AI assistant:** "show the matter documents that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Matter documents    Professional firms › Matter documents   [+ New]                                          |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] MATTER   STATE   SIGNED                                                              |
| matter            | [ ] ...                                                  Open >                          |
| signed            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Matter | matter | link to the record | yes |
| State | state | badge: Draft, Signed | yes |
| Signed | signed | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Signed | the visible rows (D488) |
| Matter | each linked matter | the visible rows (D488) |
| Signed | yes, no | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Matter documents of a chosen matter, or of the matters that match a filter.
- From the other side: the matters that have matter documents, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New matter document | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- signed: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC11-09 Documents](../02-matters-and-documents/s-sc11-09-documents.md).

The records also show on: [S-SC11-10 Client portal](../02-matters-and-documents/s-sc11-10-client-portal.md),
[S-SC11-12 Filings](../04-deadlines-and-filings/s-sc11-12-filings.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 matter documents of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no matter document the user may see yet, with the create action when allowed.
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
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-sc11-l10-matter-documents-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l10-matter-documents-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-sc11-l10-matter-documents-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l10-matter-documents-u36-professional-phone-dark.png) |
| Listed, U37, view All | desktop | ![Listed, U37, view All, light](../../images/lists/s-sc11-l10-matter-documents-u37-assistant-desktop-light.png) | ![Listed, U37, view All, dark](../../images/lists/s-sc11-l10-matter-documents-u37-assistant-desktop-dark.png) |
| Listed, U37, view All | phone | ![Listed, U37, view All, light](../../images/lists/s-sc11-l10-matter-documents-u37-assistant-phone-light.png) | ![Listed, U37, view All, dark](../../images/lists/s-sc11-l10-matter-documents-u37-assistant-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-sc11-l10-matter-documents-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc11-l10-matter-documents-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-sc11-l10-matter-documents-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc11-l10-matter-documents-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Professional firms › Matter documents](README.md) |
| Workspaces | [U36](../../../../04-ux/views/u36-professional/workspace.md), [U37](../../../../04-ux/views/u37-assistant/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-SC11-02](../../flows/fl-sc11-02-matters-and-documents.md), [FL-SC11-04](../../flows/fl-sc11-04-deadlines-and-filings.md) |

## Open questions

None.

---

⬅️ [S-SC11-L09 Deadlines](s-sc11-l09-deadlines.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-L11 Filings](s-sc11-l11-filings.md)
