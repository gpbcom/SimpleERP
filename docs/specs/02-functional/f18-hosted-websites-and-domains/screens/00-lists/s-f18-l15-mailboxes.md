🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Hosted websites and domains (hosted edition) menu](README.md) › 🗂️ S-F18-L15 Mailboxes

# 🗂️ S-F18-L15 Mailboxes

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F18-15 Mailbox](../../data/e-f18-15-mailbox.md) the user may see: to find, filter, total
and act on many mailboxes at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Hosted websites and domains (hosted edition) › Mailboxes, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "mailboxes" offers this view.
- **AI assistant:** "show the mailboxes that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Mailboxes    Hosted websites and domains (hosted edition) › Mailboxes   [+ New]                              |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] ADDRESS   STATUS   OWNER   KIND   SIZE                                               |
| owner             | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Address | address | text | yes |
| Status | status | badge | yes |
| Owner | owner | link to the record | yes |
| Kind | kind | text | yes |
| Size | size | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active, Forwarding, Closed | the visible rows (D488) |
| Owner | each linked owner | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Status | Active, Forwarding, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: mailboxes link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: owner.
- Open: Active, Forwarding.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New mailbox | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the owner; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- size: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| address | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F18-23 Mailboxes](../03-domain-and-dns/s-f18-23-mailboxes.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 mailboxes of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no mailbox the user may see yet, with the create action when allowed.
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
| Listed, U07, view Open: Active, Forwarding | desktop | ![Listed, U07, view Open: Active, Forwarding, light](../../images/lists/s-f18-l15-mailboxes-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Active, Forwarding, dark](../../images/lists/s-f18-l15-mailboxes-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Active, Forwarding | phone | ![Listed, U07, view Open: Active, Forwarding, light](../../images/lists/s-f18-l15-mailboxes-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Active, Forwarding, dark](../../images/lists/s-f18-l15-mailboxes-u07-administrator-phone-dark.png) |
| Listed, U01, view Mine: owner | desktop | ![Listed, U01, view Mine: owner, light](../../images/lists/s-f18-l15-mailboxes-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: owner, dark](../../images/lists/s-f18-l15-mailboxes-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: owner | phone | ![Listed, U01, view Mine: owner, light](../../images/lists/s-f18-l15-mailboxes-u01-employee-phone-light.png) | ![Listed, U01, view Mine: owner, dark](../../images/lists/s-f18-l15-mailboxes-u01-employee-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Hosted websites and domains (hosted edition) › Mailboxes](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F18-03](../../flows/fl-f18-03-domain-and-dns.md) |

## Open questions

None.

---

⬅️ [S-F18-L14 Redirects](s-f18-l14-redirects.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-L16 Spam holds](s-f18-l16-spam-holds.md)
