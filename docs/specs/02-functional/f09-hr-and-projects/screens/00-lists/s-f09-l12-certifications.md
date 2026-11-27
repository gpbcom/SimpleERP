🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L12 Certifications

# 🗂️ S-F9-L12 Certifications

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U21 Production planner](../../../../01-users/personas/u21-production-planner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U20 Production operator](../../../../01-users/personas/u20-production-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U09, U13, U52, U53: their use cases only read these records, inside a screen of the use case, so
they open them from there (D493).

## Purpose

The aggregated list of every [E-F9-12 Qualification](../../data/e-f09-12-certification.md) the user may see: to find,
filter, total and act on many certifications at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Certifications, in the capability's menu (D495).
- **Workspaces:** 11 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "certifications" offers this view.
- **AI assistant:** "show the certifications that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Certifications    HR and projects › Certifications   [+ New]                                                 |
| [count] [Rejected] [new this month]   [chart: count by state]                                                |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATUS   PROOF   ISSUED   EXPIRES   VERIFIED AT   TYPE                    |
| employee          | [ ] ...                                                  Open >                          |
| type              | [ ] ...                                                  Open >                          |
| proof             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | person's name | yes |
| Status | status | badge | yes |
| Proof | proof | text | yes |
| Issued | issued | date | yes |
| Expires | expires | date | yes |
| Verified at | verified at | date and time | yes |
| Type | type | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | ToVerify, Verified, Rejected, Expired | the visible rows (D488) |
| Employee | each person, the user first | the visible rows (D488) |
| Type | each value | the visible rows (D488) |
| Proof | each value | the visible rows (D488) |
| Status | ToVerify, Verified, Rejected, Expired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Certifications of a chosen proof, or of the proofs that match a filter.
- From the other side: the proofs that have certifications, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Rejected.
- New this month, by issued.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: employee.
- Open: ToVerify, Verified.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New qualification | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the employee; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- type: editable in its cell unless the record's state locks it.
- issued: editable in its cell unless the record's state locks it.
- expires: editable in its cell unless the record's state locks it.
- verified at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| proof | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F9-04 My HR](../01-people/s-f09-04-my-hr.md).

The records also show on:
[S-F12-22 Qualifications matrix](../../../f12-manufacturing/screens/10-people-and-tools/s-f12-22-qualifications-matrix.md),
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 certifications of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no qualification the user may see yet, with the create action when allowed.
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
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u06-hr-phone-dark.png) |
| Listed, U01, view Mine: employee | desktop | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: employee | phone | ![Listed, U01, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u01-employee-phone-light.png) | ![Listed, U01, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u01-employee-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u02-manager-phone-dark.png) |
| Listed, U21, view Needs attention | desktop | ![Listed, U21, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u21-production-planner-desktop-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u21-production-planner-desktop-dark.png) |
| Listed, U21, view Needs attention | phone | ![Listed, U21, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u21-production-planner-phone-light.png) | ![Listed, U21, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u21-production-planner-phone-dark.png) |
| Listed, U20, view Mine: employee | desktop | ![Listed, U20, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u20-production-operator-desktop-light.png) | ![Listed, U20, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u20-production-operator-desktop-dark.png) |
| Listed, U20, view Mine: employee | phone | ![Listed, U20, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u20-production-operator-phone-light.png) | ![Listed, U20, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u20-production-operator-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u38-training-coordinator-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l12-certifications-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l12-certifications-u29-dispatcher-phone-dark.png) |
| Listed, U26, view Mine: employee | desktop | ![Listed, U26, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: employee | phone | ![Listed, U26, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u26-carer-phone-light.png) | ![Listed, U26, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: employee | desktop | ![Listed, U30, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: employee | phone | ![Listed, U30, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u30-driver-phone-light.png) | ![Listed, U30, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u30-driver-phone-dark.png) |
| Listed, U14, view Mine: employee | desktop | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: employee | phone | ![Listed, U14, view Mine: employee, light](../../images/lists/s-f09-l12-certifications-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: employee, dark](../../images/lists/s-f09-l12-certifications-u14-field-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Certifications](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U21](../../../../04-ux/views/u21-production-planner/workspace.md), [U20](../../../../04-ux/views/u20-production-operator/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-F12-10](../../../f12-manufacturing/flows/fl-f12-10-people-and-tools.md), [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F9-04](../../flows/fl-f09-04-grow.md), [FL-F9-09](../../flows/fl-f09-09-train-and-protect.md), [FL-F9-11](../../flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../flows/fl-f09-13-keep-qualifications.md), [FL-SC03-05](../../../../08-sectors/sc03-services/flows/fl-sc03-05-client-and-people.md), [FL-SC13-04](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-04-sales-and-certification.md) |

## Open questions

None.

---

⬅️ [S-F9-L11 Appraisals](s-f09-l11-appraisals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L13 Company vehicles](s-f09-l13-company-vehicles.md)
