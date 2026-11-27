🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L01 Conversations

# 🗂️ S-F3-L01 Conversations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U55 Elected official](../../../../01-users/personas/u55-elected-official.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- Every AI assistant user sees their own records, as the F3 use cases list them (D519).

## Purpose

The aggregated list of every [E-F3-01 Conversation](../../data/e-f03-01-conversation.md) the user may see: to find,
filter, total and act on many conversations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Assistant › Conversations, in the capability's menu (D495).
- **Workspaces:** 14 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "conversations" offers this view.
- **AI assistant:** "show the conversations that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Conversations    Assistant › Conversations   [+ New]                                                         |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   STATE   OWNER   COPIED FROM   FOLDER   STARTED   LAST MESSAGE   TAGS         |
| owner             | [ ] ...                                                  Open >                          |
| copied from       | [ ] ...                                                  Open >                          |
| folder            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| State | state | badge: Private, Shared, Deleted | yes |
| Owner | owner | person's name | yes |
| Copied from | copied from | text | yes |
| Folder | folder | text | yes |
| Started | started | date and time | yes |
| Last message | last message | date and time | yes |
| Tags | tags | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Private, Shared, Deleted | the visible rows (D488) |
| Owner | each person, the user first | the visible rows (D488) |
| Copied from | each value | the visible rows (D488) |
| Folder | each value | the visible rows (D488) |
| Tags | each value | the visible rows (D488) |
| Pinned | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Conversations of a chosen copied from, or of the copied froms that match a filter.
- From the other side: the copied froms that have conversations, or none.
- Conversations of a chosen folder, or of the folders that match a filter.
- From the other side: the folders that have conversations, or none.

## KPI strip

- Count of the visible rows.
- New this month, by started.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: owner.
- Open: Private, Shared.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New conversation | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the owner; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- tags: editable in its cell unless the record's state locks it.
- pinned: editable in its cell unless the record's state locks it.
- started: editable in its cell unless the record's state locks it.
- last message: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| shared with | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to
[S-F15-01 Legal answer](../../../f15-legal-assistant/screens/01-ask-a-legal-question/s-f15-01-legal-answer.md).

The records also show on:
[S-F15-02 Legal warning](../../../f15-legal-assistant/screens/02-receive-a-legal-warning/s-f15-02-legal-warning.md),
[S-F15-03 Document check](../../../f15-legal-assistant/screens/03-check-a-document-against-the-law/s-f15-03-document-check.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 conversations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no conversation the user may see yet, with the create action when allowed.
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
| Listed, U01, view Mine: owner | desktop | ![Listed, U01, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: owner | phone | ![Listed, U01, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u01-employee-phone-light.png) | ![Listed, U01, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u01-employee-phone-dark.png) |
| Listed, U14, view Mine: owner | desktop | ![Listed, U14, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: owner | phone | ![Listed, U14, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u14-field-worker-phone-dark.png) |
| Listed, U02, view Open: Private, Shared | desktop | ![Listed, U02, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Private, Shared | phone | ![Listed, U02, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u02-manager-phone-light.png) | ![Listed, U02, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u02-manager-phone-dark.png) |
| Listed, U06, view Open: Private, Shared | desktop | ![Listed, U06, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u06-hr-desktop-light.png) | ![Listed, U06, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u06-hr-desktop-dark.png) |
| Listed, U06, view Open: Private, Shared | phone | ![Listed, U06, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u06-hr-phone-light.png) | ![Listed, U06, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u06-hr-phone-dark.png) |
| Listed, U13, view Open: Private, Shared | desktop | ![Listed, U13, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u13-owner-desktop-light.png) | ![Listed, U13, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: Private, Shared | phone | ![Listed, U13, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u13-owner-phone-light.png) | ![Listed, U13, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u13-owner-phone-dark.png) |
| Listed, U05, view Mine: owner | desktop | ![Listed, U05, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: owner | phone | ![Listed, U05, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u05-accounting-phone-dark.png) |
| Listed, U08, view Open: Private, Shared | desktop | ![Listed, U08, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Open: Private, Shared | phone | ![Listed, U08, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u08-external-accountant-phone-light.png) | ![Listed, U08, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u08-external-accountant-phone-dark.png) |
| Listed, U07, view Open: Private, Shared | desktop | ![Listed, U07, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Private, Shared | phone | ![Listed, U07, view Open: Private, Shared, light](../../images/lists/s-f03-l01-conversations-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Private, Shared, dark](../../images/lists/s-f03-l01-conversations-u07-administrator-phone-dark.png) |
| Listed, U03, view Mine: owner | desktop | ![Listed, U03, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: owner | phone | ![Listed, U03, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u03-sales-phone-light.png) | ![Listed, U03, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u03-sales-phone-dark.png) |
| Listed, U04, view Mine: owner | desktop | ![Listed, U04, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u04-purchasing-desktop-light.png) | ![Listed, U04, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Mine: owner | phone | ![Listed, U04, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u04-purchasing-phone-light.png) | ![Listed, U04, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u04-purchasing-phone-dark.png) |
| Listed, U12, view Mine: owner | desktop | ![Listed, U12, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u12-marketing-desktop-light.png) | ![Listed, U12, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u12-marketing-desktop-dark.png) |
| Listed, U12, view Mine: owner | phone | ![Listed, U12, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u12-marketing-phone-light.png) | ![Listed, U12, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u12-marketing-phone-dark.png) |
| Listed, U15, view Mine: owner | desktop | ![Listed, U15, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Mine: owner | phone | ![Listed, U15, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u15-warehouse-operator-phone-dark.png) |
| Listed, U16, view Mine: owner | desktop | ![Listed, U16, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u16-office-worker-desktop-light.png) | ![Listed, U16, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Mine: owner | phone | ![Listed, U16, view Mine: owner, light](../../images/lists/s-f03-l01-conversations-u16-office-worker-phone-light.png) | ![Listed, U16, view Mine: owner, dark](../../images/lists/s-f03-l01-conversations-u16-office-worker-phone-dark.png) |
| Listed, U55, view Open | desktop | ![Listed, U55, view Open, light](../../images/lists/s-f03-l01-conversations-u55-elected-official-desktop-light.png) | ![Listed, U55, view Open, dark](../../images/lists/s-f03-l01-conversations-u55-elected-official-desktop-dark.png) |
| Listed, U55, view Open | phone | ![Listed, U55, view Open, light](../../images/lists/s-f03-l01-conversations-u55-elected-official-phone-light.png) | ![Listed, U55, view Open, dark](../../images/lists/s-f03-l01-conversations-u55-elected-official-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Assistant › Conversations](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U55](../../../../04-ux/views/u55-elected-official/workspace.md) |
| Flows | [FL-F15-01](../../../f15-legal-assistant/flows/fl-f15-01-ask-a-legal-question.md), [FL-F15-02](../../../f15-legal-assistant/flows/fl-f15-02-receive-a-legal-warning.md), [FL-F15-03](../../../f15-legal-assistant/flows/fl-f15-03-check-a-document-against-the-law.md), [FL-F15-04](../../../f15-legal-assistant/flows/fl-f15-04-set-up-the-legal-assistant.md), [FL-F3-01](../../flows/fl-f03-01-ask-the-assistant.md), [FL-F3-08](../../flows/fl-f03-08-manage-and-share-conversations.md), [FL-F3-09](../../flows/fl-f03-09-assistant-on-a-phone.md) |

## Open questions

None.

---

⬅️ [S-F3-28 My to-dos](../13-voice-agents-and-briefings/s-f03-28-my-to-dos.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L02 Assistant answers](s-f03-l02-assistant-answers.md)
