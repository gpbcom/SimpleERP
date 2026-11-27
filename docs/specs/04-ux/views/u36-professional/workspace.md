🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
⚖️ [Professional: app shell and home](README.md) › 🧰 U36 Professional: workspace

# 🧰 U36 Professional: workspace

**Status:** ✅ specified

## Purpose

The views [U36 Professional](../../../01-users/personas/u36-professional.md) works with, embedded on their
[home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-25 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | UC-F4-25 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-SC09-21, UC-SC09-22, UC-SC09-23 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | All | UC-F8-40, UC-F15-19, UC-F15-20 |
| [S-F8-L04 Bank lines](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l04-bank-lines.md) | Accounting | All | UC-F8-21 |
| [S-F8-L17 Client money ledgers](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l17-client-money-ledgers.md) | Accounting | Open: Open | UC-F8-21, UC-SC11-07 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F15-L05 Compliance duties](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l05-compliance-duties.md) | Legal assistant | Mine: owner | UC-F15-19, UC-F15-20 |
| [S-F15-L06 Contract records](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l06-contract-records.md) | Legal assistant | Open: Active, NoticeGiven, Renewed | UC-F15-17 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | All | UC-F15-17 |
| [S-F15-L18 Clauses](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l18-clauses.md) | Legal assistant | All | UC-F15-17 |
| [S-F15-L20 IP rights](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l20-ip-rights.md) | Legal assistant | All | UC-F15-19 |
| [S-F15-L21 Disputes](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l21-disputes.md) | Legal assistant | All | UC-F15-20 |
| [S-SC03-L04 Staffing assignments](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l04-staffing-assignments.md) | Services | All | UC-SC03-18 |
| [S-SC03-L19 Certificates](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l19-certificates.md) | Services | All | UC-SC03-18 |
| [S-SC09-L03 Clinical record entries](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l03-clinical-record-entries.md) | Health practices | Mine: author | UC-SC09-23, UC-SC09-24 |
| [S-SC09-L04 Prescriptions](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l04-prescriptions.md) | Health practices | All | UC-SC09-21, UC-SC09-22 |
| [S-SC09-L07 Patient invoices](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l07-patient-invoices.md) | Health practices | All | UC-SC09-22, UC-SC09-24 |
| [S-SC09-L14 Dispensations](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l14-dispensations.md) | Health practices | All | UC-SC09-21 |
| [S-SC09-L15 Eyewear orders](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l15-eyewear-orders.md) | Health practices | All | UC-SC09-22 |
| [S-SC09-L16 Animals](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l16-animals.md) | Health practices | All | UC-SC09-23 |
| [S-SC09-L17 Dental quotes](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l17-dental-quotes.md) | Health practices | All | UC-SC09-24 |
| [S-SC09-L19 Funding indicators](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l19-aci-indicators.md) | Health practices | All | UC-SC09-26 |
| [S-SC11-L01 Client identities](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l01-client-identities.md) | Professional firms | All | UC-SC11-01, UC-SC11-15 |
| [S-SC11-L02 Beneficial owners](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l02-beneficial-owners.md) | Professional firms | All | UC-SC11-01 |
| [S-SC11-L03 Conflict checks](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l03-conflict-checks.md) | Professional firms | All | UC-SC11-02 |
| [S-SC11-L04 Engagement letters](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l04-engagement-letters.md) | Professional firms | All | UC-SC11-03 |
| [S-SC11-L05 Matters](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l05-matters.md) | Professional firms | Open: Open | UC-SC11-04, UC-SC11-13, UC-SC11-20 |
| [S-SC11-L06 Time entries](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l06-time-entries.md) | Professional firms | All | UC-SC11-05, UC-SC11-14 |
| [S-SC11-L07 Fee bills](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l07-fee-bills.md) | Professional firms | All | UC-SC11-13, UC-SC11-06, UC-SC11-14 |
| [S-SC11-L08 Trust movements](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l08-trust-movements.md) | Professional firms | All | UC-SC11-07 |
| [S-SC11-L09 Deadlines](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l09-deadlines.md) | Professional firms | Mine: owner | UC-SC11-20, UC-SC11-08 |
| [S-SC11-L10 Matter documents](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l10-matter-documents.md) | Professional firms | All | UC-SC11-09, UC-SC11-10, UC-SC11-12 |
| [S-SC11-L11 Filings](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l11-filings.md) | Professional firms | All | UC-SC11-11, UC-SC11-12 |
| [S-SC11-L12 Vigilance records](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l12-vigilance-records.md) | Professional firms | All | UC-SC11-15 |
| [S-SC11-L13 Access walls](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l13-access-walls.md) | Professional firms | All | UC-SC11-16 |
| [S-SC11-L15 Training records](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l15-training-records.md) | Professional firms | All | UC-SC11-18 |
| [S-SC11-L16 Deeds](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l16-deeds.md) | Professional firms | All | UC-SC11-21 |
| [S-SC11-L17 Policies](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l17-policies.md) | Professional firms | All | UC-SC11-22 |
| [S-SC11-L18 Service acts](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l18-service-acts.md) | Professional firms | All | UC-SC11-23 |
| [S-SC11-L19 Audit engagements](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l19-audit-engagements.md) | Professional firms | All | UC-SC11-24 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Professional firms](../../../08-sectors/sc11-professional-firms/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U36 | desktop | ![Workspace, U36, light](mockups/workspace-desktop-light.png) | ![Workspace, U36, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U36 | phone | ![Workspace, U36, light](mockups/workspace-phone-light.png) | ![Workspace, U36, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
