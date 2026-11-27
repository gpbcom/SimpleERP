🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Professional firms menu](README.md) › 🗂️ S-SC11-L08 Trust movements

# 🗂️ S-SC11-L08 Trust movements

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC11-08 Trust movement](../../data/e-sc11-08-trust-movement.md) the user may see: to
find, filter, total and act on many trust movements at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Professional firms › Trust movements, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "trust movements" offers this view.
- **AI assistant:** "show the trust movements that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Trust movements    Professional firms › Trust movements   [+ New]                                            |
| [count] [total amount]   [chart: count by state, amount stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CLIENT   STATE   MATTER   ACCOUNT   AMOUNT                                           |
| matter            | [ ] ...                                                  Open >                          |
| account           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Client | client | link to the record | yes |
| State | state | badge: Active | yes |
| Matter | matter | link to the record | yes |
| Account | account | text | yes |
| Amount | amount | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Matter | each linked matter | the visible rows (D488) |
| Account | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Trust movements of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have trust movements, or none.
- Trust movements of a chosen matter, or of the matters that match a filter.
- From the other side: the matters that have trust movements, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.

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
| New trust movement | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-SC11-07 Client funds](../03-time-and-billing/s-sc11-07-client-funds.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 trust movements of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no trust movement the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-sc11-l08-trust-movements-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc11-l08-trust-movements-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-sc11-l08-trust-movements-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc11-l08-trust-movements-u05-accounting-phone-dark.png) |
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-sc11-l08-trust-movements-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l08-trust-movements-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-sc11-l08-trust-movements-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l08-trust-movements-u36-professional-phone-dark.png) |
| Listed, U37, view All | desktop | ![Listed, U37, view All, light](../../images/lists/s-sc11-l08-trust-movements-u37-assistant-desktop-light.png) | ![Listed, U37, view All, dark](../../images/lists/s-sc11-l08-trust-movements-u37-assistant-desktop-dark.png) |
| Listed, U37, view All | phone | ![Listed, U37, view All, light](../../images/lists/s-sc11-l08-trust-movements-u37-assistant-phone-light.png) | ![Listed, U37, view All, dark](../../images/lists/s-sc11-l08-trust-movements-u37-assistant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Professional firms › Trust movements](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U36](../../../../04-ux/views/u36-professional/workspace.md), [U37](../../../../04-ux/views/u37-assistant/workspace.md) |
| Flows | [FL-SC11-03](../../flows/fl-sc11-03-time-and-billing.md) |

## Open questions

None.

---

⬅️ [S-SC11-L07 Fee bills](s-sc11-l07-fee-bills.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-L09 Deadlines](s-sc11-l09-deadlines.md)
