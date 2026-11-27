🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L15 Shareholdings

# 🗂️ S-F15-L15 Shareholdings

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U50 Shareholder](../../../../01-users/personas/u50-shareholder.md) | only the records shared with them | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U31: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F15-15 Shareholding](../../data/e-f15-15-shareholding.md) the user may see: to find,
filter, total and act on many shareholdings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Shareholdings, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "shareholdings" offers this view.
- **AI assistant:** "show the shareholdings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Shareholdings    Administration > Shareholdings   [+ New]                                                    |
| [count] [Approved] [new this month]   [chart: count by state]                                                |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| class             | [ ] HOLDER   CLASS   MOVEMENT   QUANTITY   ENTRY NUMBER   STATE                          |
| movement          | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Holder | holder | text | yes |
| Class | class | text | yes |
| Movement | movement | text | yes |
| Quantity | quantity | number | yes |
| Entry number | entry number | text | yes |
| State | state | badge: Proposed, Approved, Registered, Cancelled | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Class | each value | the visible rows (D488) |
| Movement | each value | the visible rows (D488) |
| State | Proposed, Approved, Registered, Cancelled | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Shareholdings that have an equity grant.
- From the other side: the decisions that authorised a movement, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Approved.
- New this month, by registered on.

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
| New shareholding | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| holder | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| counterparty | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F15-12 Cap table](../07-equity-contracts-and-disputes/s-f15-12-cap-table.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 shareholdings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no shareholding the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f15-l15-shareholdings-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f15-l15-shareholdings-u13-owner-desktop-dark.png) |
| Listed, U50, view All | phone | ![Listed, U50, view All, light](../../images/lists/s-f15-l15-shareholdings-u50-shareholder-phone-light.png) | ![Listed, U50, view All, dark](../../images/lists/s-f15-l15-shareholdings-u50-shareholder-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f15-l15-shareholdings-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f15-l15-shareholdings-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f15-l15-shareholdings-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f15-l15-shareholdings-u01-employee-phone-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f15-l15-shareholdings-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f15-l15-shareholdings-u13-owner-phone-dark.png) |
| Listed, U50, view All | desktop | ![Listed, U50, view All, light](../../images/lists/s-f15-l15-shareholdings-u50-shareholder-desktop-light.png) | ![Listed, U50, view All, dark](../../images/lists/s-f15-l15-shareholdings-u50-shareholder-desktop-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Shareholdings](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F15-07](../../flows/fl-f15-07-equity-contracts-and-disputes.md) |

## Open questions

None.

---

⬅️ [S-F15-L14 Corporate filings](s-f15-l14-corporate-filings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L16 Equity grants](s-f15-l16-equity-grants.md)
