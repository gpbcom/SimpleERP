🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Social media and marketing menu](README.md) › 🗂️ S-F5-L08 Surveys

# 🗂️ S-F5-L08 Surveys

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F5-08 Survey](../../data/e-f05-08-survey.md) the user may see: to find, filter, total
and act on many surveys at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Social media and marketing › Surveys, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "surveys" offers this view.
- **AI assistant:** "show the surveys that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Surveys    Social media and marketing › Surveys   [+ New]                                                    |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] QUESTIONS   STATE                                                                    |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Questions | questions | text | yes |
| State | state | badge: Draft, Sent, Closed | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Sent, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: surveys link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Sent.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New survey | header | the personas whose roles may create it | the record's own page (Row opens) |
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

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F5-12 Survey](../08-pages-forms-surveys-and-whatsapp/s-f05-12-survey.md).

The records also show on:
[S-F9-25 Surveys and exit interviews](../../../f09-hr-and-projects/screens/10-listen-to-employees/s-f09-25-surveys-and-exit-interviews.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 surveys of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no survey the user may see yet, with the create action when allowed.
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
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f05-l08-surveys-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f05-l08-surveys-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f05-l08-surveys-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f05-l08-surveys-u06-hr-phone-dark.png) |
| Listed, U12, view Open: Draft, Sent | desktop | ![Listed, U12, view Open: Draft, Sent, light](../../images/lists/s-f05-l08-surveys-u12-marketing-desktop-light.png) | ![Listed, U12, view Open: Draft, Sent, dark](../../images/lists/s-f05-l08-surveys-u12-marketing-desktop-dark.png) |
| Listed, U12, view Open: Draft, Sent | phone | ![Listed, U12, view Open: Draft, Sent, light](../../images/lists/s-f05-l08-surveys-u12-marketing-phone-light.png) | ![Listed, U12, view Open: Draft, Sent, dark](../../images/lists/s-f05-l08-surveys-u12-marketing-phone-dark.png) |
| Listed, U09, view Open: Draft, Sent | desktop | ![Listed, U09, view Open: Draft, Sent, light](../../images/lists/s-f05-l08-surveys-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, Sent, dark](../../images/lists/s-f05-l08-surveys-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, Sent | phone | ![Listed, U09, view Open: Draft, Sent, light](../../images/lists/s-f05-l08-surveys-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, Sent, dark](../../images/lists/s-f05-l08-surveys-u09-customer-phone-dark.png) |
| Listed, U01, view Open: Draft, Sent | desktop | ![Listed, U01, view Open: Draft, Sent, light](../../images/lists/s-f05-l08-surveys-u01-employee-desktop-light.png) | ![Listed, U01, view Open: Draft, Sent, dark](../../images/lists/s-f05-l08-surveys-u01-employee-desktop-dark.png) |
| Listed, U01, view Open: Draft, Sent | phone | ![Listed, U01, view Open: Draft, Sent, light](../../images/lists/s-f05-l08-surveys-u01-employee-phone-light.png) | ![Listed, U01, view Open: Draft, Sent, dark](../../images/lists/s-f05-l08-surveys-u01-employee-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f05-l08-surveys-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f05-l08-surveys-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f05-l08-surveys-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f05-l08-surveys-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Social media and marketing › Surveys](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F5-08](../../flows/fl-f05-08-pages-forms-surveys-and-whatsapp.md), [FL-F9-10](../../../f09-hr-and-projects/flows/fl-f09-10-listen-to-employees.md) |

## Open questions

None.

---

⬅️ [S-F5-L07 Registration events](s-f05-l07-registration-events.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-L09 Contact segments](s-f05-l09-contact-segments.md)
