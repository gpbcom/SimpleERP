🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L01 Store listings

# 🗂️ S-F14-L01 Store listings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U12: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F14-01 Store listing](../../data/e-f14-01-store-listing.md) the user may see: to find,
filter, total and act on many store listings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Store listings, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "store listings" offers this view.
- **AI assistant:** "show the store listings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Store listings    Plugin store › Store listings   [+ New]                                                    |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   RATING   CATEGORY                                                     |
| category          | [ ] ...                                                  Open >                          |
| rating            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | link to the record | yes |
| State | state | badge: New, Paid, Complete, Refused | yes |
| Rating | rating | text | yes |
| Category | category | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | New, Paid, Complete, Refused | the visible rows (D488) |
| Category | each linked category | the visible rows (D488) |
| Rating | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Store listings of a chosen rating, or of the ratings that match a filter.
- From the other side: the ratings that have store listings, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: New, Complete, Refused.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New store listing | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- category: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F14-01 Store](../01-find-and-install/s-f14-01-store.md).

The records also show on: [S-F14-02 Install](../01-find-and-install/s-f14-02-install.md),
[S-F14-08 Submission](../03-publish/s-f14-08-submission.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 store listings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no store listing the user may see yet, with the create action when allowed.
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
| Listed, U07, view Open: New, Complete, Refused | desktop | ![Listed, U07, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: New, Complete, Refused | phone | ![Listed, U07, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u07-administrator-phone-light.png) | ![Listed, U07, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u07-administrator-phone-dark.png) |
| Listed, U46, view Open: New, Complete, Refused | desktop | ![Listed, U46, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u46-plugin-publisher-desktop-light.png) | ![Listed, U46, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u46-plugin-publisher-desktop-dark.png) |
| Listed, U46, view Open: New, Complete, Refused | phone | ![Listed, U46, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u46-plugin-publisher-phone-light.png) | ![Listed, U46, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u46-plugin-publisher-phone-dark.png) |
| Listed, U13, view Open: New, Complete, Refused | desktop | ![Listed, U13, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u13-owner-desktop-light.png) | ![Listed, U13, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: New, Complete, Refused | phone | ![Listed, U13, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u13-owner-phone-light.png) | ![Listed, U13, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u13-owner-phone-dark.png) |
| Listed, U11, view Open: New, Complete, Refused | desktop | ![Listed, U11, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Open: New, Complete, Refused | phone | ![Listed, U11, view Open: New, Complete, Refused, light](../../images/lists/s-f14-l01-store-listings-u11-provider-admin-phone-light.png) | ![Listed, U11, view Open: New, Complete, Refused, dark](../../images/lists/s-f14-l01-store-listings-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Store listings](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U46](../../../../04-ux/views/u46-plugin-publisher/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F14-01](../../flows/fl-f14-01-find-and-install.md), [FL-F14-03](../../flows/fl-f14-03-publish.md), [FL-F14-05](../../flows/fl-f14-05-store-operations.md), [FL-F14-07](../../flows/fl-f14-07-plugin-end-of-life.md), [FL-F19-04](../../../f19-feature-factory/flows/fl-f19-04-promote.md) |

## Open questions

None.

---

⬅️ [S-F14-30 Website themes](../08-trials-instances-and-partners/s-f14-30-website-themes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L02 Plugin installations](s-f14-l02-plugin-installations.md)
