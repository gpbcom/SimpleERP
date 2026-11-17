🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L12 Provider sessions

# 🗂️ S-F1-L12 Provider sessions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F1-12 Provider session](../../data/e-f01-12-provider-session.md) the user may see: to
find, filter, total and act on many provider sessions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Provider sessions, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "provider sessions" offers this view.
- **AI assistant:** "show the provider sessions that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Provider sessions    Administration › Provider sessions   [+ New]                                            |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PROVIDER USER   STATE   STARTED   ENDED   ACTIONS                                    |
| provider user     | [ ] ...                                                  Open >                          |
| actions           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Provider user | provider user | text | yes |
| State | state | badge: Live, Closed | yes |
| Started | started | date and time | yes |
| Ended | ended | date and time | yes |
| Actions | actions | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Live, Closed | the visible rows (D488) |
| Provider user | each value | the visible rows (D488) |
| Actions | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: provider sessions link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by started.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: provider user.
- Open: Live.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New provider session | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the provider user; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- started: editable in its cell unless the record's state locks it.
- ended: editable in its cell unless the record's state locks it.
- actions: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| provider user | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F1-11 Provider access log](../08-provider-and-client-companies/s-f01-11-provider-access-log.md).

The records also show on: [S-F1-10 Client companies](../08-provider-and-client-companies/s-f01-10-client-companies.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 provider sessions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no provider session the user may see yet, with the create action when allowed.
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
| Listed, U11, view Open: Live | desktop | ![Listed, U11, view Open: Live, light](../../images/lists/s-f01-l12-provider-sessions-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Open: Live, dark](../../images/lists/s-f01-l12-provider-sessions-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Open: Live | phone | ![Listed, U11, view Open: Live, light](../../images/lists/s-f01-l12-provider-sessions-u11-provider-admin-phone-light.png) | ![Listed, U11, view Open: Live, dark](../../images/lists/s-f01-l12-provider-sessions-u11-provider-admin-phone-dark.png) |
| Listed, U07, view Open: Live | desktop | ![Listed, U07, view Open: Live, light](../../images/lists/s-f01-l12-provider-sessions-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Live, dark](../../images/lists/s-f01-l12-provider-sessions-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Live | phone | ![Listed, U07, view Open: Live, light](../../images/lists/s-f01-l12-provider-sessions-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Live, dark](../../images/lists/s-f01-l12-provider-sessions-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Provider sessions](README.md) |
| Workspaces | [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F1-08](../../flows/fl-f01-08-provider-and-client-companies.md), [FL-F1-09](../../flows/fl-f01-09-administration-reports.md) |

## Open questions

None.

---

⬅️ [S-F1-L11 Company templates](s-f01-l11-company-templates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L13 Approval delegations](s-f01-l13-approval-delegations.md)
