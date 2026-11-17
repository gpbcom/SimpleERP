🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Customer support agents menu](README.md) › 🗂️ S-F16-L13 Forum posts

# 🗂️ S-F16-L13 Forum posts

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only the records shared with them | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F16-13 Forum post](../../data/e-f16-13-forum-post.md) the user may see: to find, filter,
total and act on many forum posts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Customer support agents › Forum posts, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "forum posts" offers this view.
- **AI assistant:** "show the forum posts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Forum posts    Customer support agents > Forum posts   [+ New]                                               |
| [count] [Flagged] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| category          | [ ] TITLE   CATEGORY   KIND   AUTHOR   VOTES   STATE                                     |
| kind              | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| Category | category | text | yes |
| Kind | kind | text | yes |
| Author | author | number | yes |
| Votes | votes | number | yes |
| State | state | badge: Submitted, Published, Flagged, Removed, Hidden | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Category | each value | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| State | Submitted, Published, Flagged, Removed, Hidden | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Posts linked to a help-centre article.
- From the other side: the articles that have forum posts, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Flagged.
- New this month, by votes.

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
| New forum post | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
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
| author | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| body | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F16-16 Forum](../07-live-chat-voice-and-contracts/s-f16-16-forum.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 forum posts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no forum post the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Not drawn yet: step S8 draws them from this page, one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-f16-l13-forum-posts-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f16-l13-forum-posts-u09-customer-phone-dark.png) |
| Listed, U16, view All | desktop | ![Listed, U16, view All, light](../../images/lists/s-f16-l13-forum-posts-u16-office-worker-desktop-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f16-l13-forum-posts-u16-office-worker-desktop-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-f16-l13-forum-posts-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-f16-l13-forum-posts-u09-customer-desktop-dark.png) |
| Listed, U16, view All | phone | ![Listed, U16, view All, light](../../images/lists/s-f16-l13-forum-posts-u16-office-worker-phone-light.png) | ![Listed, U16, view All, dark](../../images/lists/s-f16-l13-forum-posts-u16-office-worker-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Customer support agents › Forum posts](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F16-07](../../flows/fl-f16-07-live-chat-voice-and-contracts.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-F16-L12 Work requests](s-f16-l12-work-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-L14 Chat sessions](s-f16-l14-chat-sessions.md)
