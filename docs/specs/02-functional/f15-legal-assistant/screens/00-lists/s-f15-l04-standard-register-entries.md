🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L04 Standard register entries

# 🗂️ S-F15-L04 Standard register entries

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F15-04 Standard register entry](../../data/e-f15-04-standard-register-entry.md) the user
may see: to find, filter, total and act on many standard register entries at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Legal assistant › Standard register entries, in the capability's menu (D495).
- **Workspaces:** 8 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "standard register entries" offers this view.
- **AI assistant:** "show the standard register entries that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Standard register entries    Legal assistant › Standard register entries   [+ New]                           |
| [count] [Open]   [chart: count by state]                                                                     |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REFERENCE   EDITION AND STATUS                                                       |
| edition and statu | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Reference | reference | text | yes |
| Edition and status | edition and status | badge | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Open | the visible rows (D488) |
| Edition and status | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: standard register entries link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Open.

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
| New standard register entry | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F15-01 Legal answer](../01-ask-a-legal-question/s-f15-01-legal-answer.md).

The records also show on: [S-F15-02 Legal warning](../02-receive-a-legal-warning/s-f15-02-legal-warning.md),
[S-F15-03 Document check](../03-check-a-document-against-the-law/s-f15-03-document-check.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 standard register entries of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no standard register entry the user may see yet, with the create action when allowed.
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
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u13-owner-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u07-administrator-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f15-l04-standard-register-entries-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f15-l04-standard-register-entries-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f15-l04-standard-register-entries-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f15-l04-standard-register-entries-u01-employee-phone-dark.png) |
| Listed, U14, view All | desktop | ![Listed, U14, view All, light](../../images/lists/s-f15-l04-standard-register-entries-u14-field-worker-desktop-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f15-l04-standard-register-entries-u14-field-worker-desktop-dark.png) |
| Listed, U14, view All | phone | ![Listed, U14, view All, light](../../images/lists/s-f15-l04-standard-register-entries-u14-field-worker-phone-light.png) | ![Listed, U14, view All, dark](../../images/lists/s-f15-l04-standard-register-entries-u14-field-worker-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u02-manager-phone-dark.png) |
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u06-hr-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f15-l04-standard-register-entries-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f15-l04-standard-register-entries-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f15-l04-standard-register-entries-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f15-l04-standard-register-entries-u05-accounting-phone-dark.png) |
| Listed, U08, view Needs attention | desktop | ![Listed, U08, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Needs attention | phone | ![Listed, U08, view Needs attention, light](../../images/lists/s-f15-l04-standard-register-entries-u08-external-accountant-phone-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f15-l04-standard-register-entries-u08-external-accountant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Legal assistant › Standard register entries](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md) |
| Flows | [FL-F15-01](../../flows/fl-f15-01-ask-a-legal-question.md), [FL-F15-02](../../flows/fl-f15-02-receive-a-legal-warning.md), [FL-F15-03](../../flows/fl-f15-03-check-a-document-against-the-law.md), [FL-F15-04](../../flows/fl-f15-04-set-up-the-legal-assistant.md), [FL-F9-08](../../../f09-hr-and-projects/flows/fl-f09-08-hr-duties.md), [FL-SC10-01](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-01-mandates-and-listings.md), [FL-SC16-04](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-04-on-site.md) |

## Open questions

None.

---

⬅️ [S-F15-L03 Document checks](s-f15-l03-document-checks.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L05 Compliance duties](s-f15-l05-compliance-duties.md)
