🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: DevOps agents (hosted edition) menu](README.md) › 🗂️ S-F25-L05 Agent pull requests

# 🗂️ S-F25-L05 Agent pull requests

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U48: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F25-05 Agent pull request](../../data/e-f25-05-agent-pull-request.md) the user may see:
to find, filter, total and act on many agent pull requests at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** DevOps agents (hosted edition) › Agent pull requests, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "agent pull requests" offers this view.
- **AI assistant:** "show the agent pull requests that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Agent pull requests    DevOps agents (hosted edition) › Agent pull requests   [+ New]                        |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| kind              | [ ] REPOSITORY   STATE   KIND                                                            |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Repository | repository | link to the record | yes |
| State | state | badge: InReview, Proposed, Checked, Open, Waiting, Declined | yes |
| Kind | kind | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Kind | each linked kind | the visible rows (D488) |
| State | InReview, Proposed, Checked, Open, Waiting, Declined | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: agent pull requests link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

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
| New agent pull request | header | the personas whose roles may create it | the record's own page (Row opens) |
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

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F25-06 Spec pull request](../02-feature-requests/s-f25-06-spec-pull-request.md).

The records also show on: [S-F25-10 Fix pull request](../03-bugs/s-f25-10-fix-pull-request.md),
[S-F25-13 Revisions](../04-approve-and-govern/s-f25-13-revisions.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 agent pull requests of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no agent pull request the user may see yet, with the create action when allowed.
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
| Listed, U47, view All | desktop | ![Listed, U47, view All, light](../../images/lists/s-f25-l05-agent-pull-requests-u47-simpleerp-maintainer-desktop-light.png) | ![Listed, U47, view All, dark](../../images/lists/s-f25-l05-agent-pull-requests-u47-simpleerp-maintainer-desktop-dark.png) |
| Listed, U47, view All | phone | ![Listed, U47, view All, light](../../images/lists/s-f25-l05-agent-pull-requests-u47-simpleerp-maintainer-phone-light.png) | ![Listed, U47, view All, dark](../../images/lists/s-f25-l05-agent-pull-requests-u47-simpleerp-maintainer-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f25-l05-agent-pull-requests-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f25-l05-agent-pull-requests-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f25-l05-agent-pull-requests-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f25-l05-agent-pull-requests-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [DevOps agents (hosted edition) › Agent pull requests](README.md) |
| Workspaces | [U47](../../../../04-ux/views/u47-simpleerp-maintainer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F25-02](../../flows/fl-f25-02-feature-requests.md), [FL-F25-03](../../flows/fl-f25-03-bugs.md), [FL-F25-04](../../flows/fl-f25-04-approve-and-govern.md), [FL-F25-06](../../flows/fl-f25-06-vulnerability-handling.md) |

## Open questions

None.

---

⬅️ [S-F25-L04 Study notes](s-f25-l04-study-notes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-L06 Agent tickets](s-f25-l06-agent-tickets.md)
