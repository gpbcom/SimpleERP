🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Social media and marketing menu](README.md) › 🗂️ S-F5-L02 Social accounts

# 🗂️ S-F5-L02 Social accounts

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U13: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F5-02 Social account](../../data/e-f05-02-social-account.md) the user may see: to find,
filter, total and act on many social accounts at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Social media and marketing › Social accounts, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "social accounts" offers this view.
- **AI assistant:** "show the social accounts that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Social accounts    Social media and marketing › Social accounts   [+ New]                                    |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NETWORK   STATE   PAGE   APPROVAL                                                    |
| page              | [ ] ...                                                  Open >                          |
| approval          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Network | network | text | yes |
| State | state | badge: Active | yes |
| Page | page | text | yes |
| Approval | approval | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Page | each value | the visible rows (D488) |
| Approval | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Social accounts of a chosen approval, or of the approvals that match a filter.
- From the other side: the approvals that have social accounts, or none.
- Social accounts of a chosen page, or of the pages that match a filter.
- From the other side: the pages that have social accounts, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New social account | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| credential | secret | nobody | everyone (VR-4) |

## Row opens

Open › goes to [S-F5-07 Social accounts](../04-connect-accounts/s-f05-07-social-accounts.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 social accounts of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no social account the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f05-l02-social-accounts-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f05-l02-social-accounts-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f05-l02-social-accounts-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f05-l02-social-accounts-u07-administrator-phone-dark.png) |
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f05-l02-social-accounts-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f05-l02-social-accounts-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f05-l02-social-accounts-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f05-l02-social-accounts-u12-marketing-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Social media and marketing › Social accounts](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md) |
| Flows | [FL-F5-01](../../flows/fl-f05-01-publish-a-post.md), [FL-F5-04](../../flows/fl-f05-04-connect-accounts.md), [FL-F5-08](../../flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md) |

## Open questions

None.

---

⬅️ [S-F5-L01 Posts](s-f05-l01-posts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-L03 Automatic post rules](s-f05-l03-automatic-post-rules.md)
