🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: DevOps agents (hosted edition) menu](README.md) › 🗂️ S-F25-L13 Spec check reports

# 🗂️ S-F25-L13 Spec check reports

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F25-13 Spec check report](../../data/e-f25-13-spec-check-report.md) the user may see: to
find, filter, total and act on many spec check reports at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** DevOps agents (hosted edition) › Spec check reports, in the capability's menu (D495).
- **Workspaces:** 1 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "spec check reports" offers this view.
- **AI assistant:** "show the spec check reports that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Spec check reports    DevOps agents (hosted edition) › Spec check reports   [+ New]                          |
| [count] [Failed]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PULL REQUEST   STATE   UNSOURCED   CONTRADICTIONS   TOOL CHECKS   RESULT             |
| pull request      | [ ] ...                                                  Open >                          |
| unsourced         | [ ] ...                                                  Open >                          |
| contradictions    | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Pull request | pull request | link to the record | yes |
| State | state | badge: Run, Passed, Failed | yes |
| Unsourced | unsourced | text | yes |
| Contradictions | contradictions | text | yes |
| Tool checks | tool checks | text | yes |
| Result | result | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Run, Passed, Failed | the visible rows (D488) |
| Pull request | each linked pull request | the visible rows (D488) |
| Unsourced | each value | the visible rows (D488) |
| Contradictions | each value | the visible rows (D488) |
| Tool checks | each value | the visible rows (D488) |
| Result | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Spec check reports of a chosen pull request, or of the pull requests that match a filter.
- From the other side: the pull requests that have spec check reports, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Failed.

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
| New spec check report | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- unsourced: editable in its cell unless the record's state locks it.
- contradictions: editable in its cell unless the record's state locks it.
- tool checks: editable in its cell unless the record's state locks it.
- result: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F25-06 Spec pull request](../02-feature-requests/s-f25-06-spec-pull-request.md).

The records also show on: [S-F25-23 Spec checks](../02-feature-requests/s-f25-23-spec-checks.md),
[S-F25-19 Agent quality](../04-approve-and-govern/s-f25-19-agent-quality.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 spec check reports of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no spec check report the user may see yet, with the create action when allowed.
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
| Listed, U47, view All | desktop | ![Listed, U47, view All, light](../../images/lists/s-f25-l13-spec-check-reports-u47-simple-erp-maintainer-desktop-light.png) | ![Listed, U47, view All, dark](../../images/lists/s-f25-l13-spec-check-reports-u47-simple-erp-maintainer-desktop-dark.png) |
| Listed, U47, view All | phone | ![Listed, U47, view All, light](../../images/lists/s-f25-l13-spec-check-reports-u47-simple-erp-maintainer-phone-light.png) | ![Listed, U47, view All, dark](../../images/lists/s-f25-l13-spec-check-reports-u47-simple-erp-maintainer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [DevOps agents (hosted edition) › Spec check reports](README.md) |
| Workspaces | [U47](../../../../04-ux/views/u47-simple-erp-maintainer/workspace.md) |
| Flows | [FL-F25-02](../../flows/fl-f25-02-feature-requests.md), [FL-F25-04](../../flows/fl-f25-04-approve-and-govern.md) |

## Open questions

None.

---

⬅️ [S-F25-L12 Vulnerability cases](s-f25-l12-vulnerability-cases.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-L14 Votes](s-f25-l14-votes.md)
