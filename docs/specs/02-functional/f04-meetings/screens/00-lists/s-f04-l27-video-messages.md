🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Meetings menu](README.md) › 🗂️ S-F4-L27 Video messages

# 🗂️ S-F4-L27 Video messages

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F4-27 Video message](../../data/e-f04-27-video-message.md) the user may see: to find,
filter, total and act on many video messages at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Meetings › Video messages, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "video messages" offers this view.
- **AI assistant:** "show the video messages that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Video messages    Meetings › Video messages   [+ New]                                                        |
| [count] [Expired] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] AUTHOR   SOURCE   LINKED RECORD   LINK ENDS   STATE                                  |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Author | author | person's name | yes |
| Source | source | text | yes |
| Linked record | linked record | text | yes |
| Link ends | link ends | date | yes |
| State | state | badge: Recording, Uploaded, Shared, Expired, Deleted | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Recording, Uploaded, Shared, Expired, Deleted | the visible rows (D488) |
| Author | each person | the visible rows (D488) |
| Source | each value | the visible rows (D488) |
| Link ends | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Messages of a chosen record, or of the records that match a filter.
- From the other side: the records that have messages, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.
- New this month, by recorded at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: author.
- Open: Uploaded, Shared.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New video message | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- link ends: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| author | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| recording | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| transcript | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| shared with | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| views | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F4-25 Video message](../14-video-messages-and-webinars/s-f04-25-video-message.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 video messages of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no video message the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in the image round from this page: one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)). The files are named by the plan.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U01, view Needs attention | phone | ![Listed, U01, view Needs attention, light](../../images/lists/s-f04-l27-video-messages-u01-employee-phone-light.png) | ![Listed, U01, view Needs attention, dark](../../images/lists/s-f04-l27-video-messages-u01-employee-phone-dark.png) |
| Listed, U03, view Needs attention | desktop | ![Listed, U03, view Needs attention, light](../../images/lists/s-f04-l27-video-messages-u03-sales-desktop-light.png) | ![Listed, U03, view Needs attention, dark](../../images/lists/s-f04-l27-video-messages-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: author | phone | ![Listed, U03, view Mine: author, light](../../images/lists/s-f04-l27-video-messages-u03-sales-phone-light.png) | ![Listed, U03, view Mine: author, dark](../../images/lists/s-f04-l27-video-messages-u03-sales-phone-dark.png) |
| Listed, U01, view Mine: author | desktop | ![Listed, U01, view Mine: author, light](../../images/lists/s-f04-l27-video-messages-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: author, dark](../../images/lists/s-f04-l27-video-messages-u01-employee-desktop-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Meetings › Video messages](README.md) |
| Workspaces | [U03](../../../../04-ux/views/u03-sales/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F4-14](../../flows/fl-f04-14-video-messages-and-webinars.md) |

## Open questions

None.

---

⬅️ [S-F4-L26 Employee calendars](s-f04-l26-employee-calendars.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-L28 Webinars](s-f04-l28-webinars.md)
