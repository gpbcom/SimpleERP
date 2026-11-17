🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Meetings menu](README.md) › 🗂️ S-F4-L28 Webinars

# 🗂️ S-F4-L28 Webinars

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F4-28 Webinar](../../data/e-f04-28-webinar.md) the user may see: to find, filter, total
and act on many webinars at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Meetings › Webinars, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "webinars" offers this view.
- **AI assistant:** "show the webinars that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Webinars    Meetings › Webinars   [+ New]                                                                    |
| [count] [Live] [new this month]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TITLE   STARTS AT   REGISTERED   ATTENDED   STATE                                    |
| [ ] ...                                                                       Open >                         |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Title | title | text | yes |
| Starts at | starts at | date and time | yes |
| Registered | registrations | number | yes |
| Attended | attendance | number | yes |
| State | state | badge: Draft, Scheduled, Live, Ended, Replay published, Cancelled | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Scheduled, Live, Ended, Replay published, Cancelled | the visible rows (D488) |
| Host | each person | the visible rows (D488) |
| Starts at | each value | the visible rows (D488) |
| Replay | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Webinars of a chosen host, or of the hosts that match a filter.
- From the other side: the hosts that have webinars, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Live.
- New this month, by starts at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: host.
- Open: Draft, Scheduled, Live.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New webinar | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only, audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows, audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted, audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns, audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- title: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| registrations | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| attendance | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| questions | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F4-26 Webinar](../14-video-messages-and-webinars/s-f04-26-webinar.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 webinars of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no webinar the user may see yet, with the create action when allowed.
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
| Listed, U09, view Needs attention | phone | ![Listed, U09, view Needs attention, light](../../images/lists/s-f04-l28-webinars-u09-customer-phone-light.png) | ![Listed, U09, view Needs attention, dark](../../images/lists/s-f04-l28-webinars-u09-customer-phone-dark.png) |
| Listed, U12, view Needs attention | desktop | ![Listed, U12, view Needs attention, light](../../images/lists/s-f04-l28-webinars-u12-marketing-desktop-light.png) | ![Listed, U12, view Needs attention, dark](../../images/lists/s-f04-l28-webinars-u12-marketing-desktop-dark.png) |
| Listed, U12, view Mine: host | phone | ![Listed, U12, view Mine: host, light](../../images/lists/s-f04-l28-webinars-u12-marketing-phone-light.png) | ![Listed, U12, view Mine: host, dark](../../images/lists/s-f04-l28-webinars-u12-marketing-phone-dark.png) |
| Listed, U09, view Mine: host | desktop | ![Listed, U09, view Mine: host, light](../../images/lists/s-f04-l28-webinars-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: host, dark](../../images/lists/s-f04-l28-webinars-u09-customer-desktop-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Meetings › Webinars](README.md) |
| Workspaces | [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F4-14](../../flows/fl-f04-14-video-messages-and-webinars.md) |

## Open questions

None.

---

⬅️ [S-F4-L27 Video messages](s-f04-l27-video-messages.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-L29 Note templates](s-f04-l29-note-templates.md)
