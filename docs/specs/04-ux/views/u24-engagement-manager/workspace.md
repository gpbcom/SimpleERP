🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧭 [Engagement manager: app shell and home](README.md) › 🧰 U24 Engagement manager: workspace

# 🧰 U24 Engagement manager: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U24 Engagement manager](../../../01-users/personas/u24-engagement-manager.md) works with, embedded on their
[home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. (Proposed) The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F9-L02 Contracts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l02-contracts.md) | HR and projects | Open: Draft, Running | UC-SC03-16 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-29, UC-F9-31, UC-F9-32 |
| [S-F9-L25 Resource allocations](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l25-resource-allocations.md) | HR and projects | Open: Planned | UC-F9-29 |
| [S-F9-L27 Subcontractor assignments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l27-subcontractor-assignments.md) | HR and projects | Open: Proposed, Active | UC-F9-32 |
| [S-F9-L51 Change requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l51-change-requests.md) | HR and projects | Mine: project | UC-F9-46 |
| [S-SC03-L01 Engagements](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l01-engagements.md) | Services | Open: PreSales, Running | UC-SC03-01, UC-SC03-15, UC-SC03-10 |
| [S-SC03-L02 Statement of works](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l02-statement-of-works.md) | Services | All | UC-SC03-01 |
| [S-SC03-L03 Rate cards](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l03-rate-cards.md) | Services | All | UC-SC03-02 |
| [S-SC03-L04 Staffing assignments](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l04-staffing-assignments.md) | Services | All | UC-SC03-03, UC-SC03-04 |
| [S-SC03-L05 Timesheets](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l05-timesheets.md) | Services | Needs attention | UC-SC03-05, UC-SC03-15 |
| [S-SC03-L06 Rebillable costs](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l06-rebillable-costs.md) | Services | All | UC-SC03-05 |
| [S-SC03-L07 Billing proposals](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l07-billing-proposals.md) | Services | All | UC-SC03-06, UC-SC03-07, UC-SC03-14 |
| [S-SC03-L08 Milestones](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l08-milestones.md) | Services | All | UC-SC03-07 |
| [S-SC03-L09 Revenue positions](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l09-revenue-positions.md) | Services | All | UC-SC03-08 |
| [S-SC03-L10 Freelance contracts](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l10-freelance-contracts.md) | Services | All | UC-SC03-09 |
| [S-SC03-L11 Skills](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l11-skills.md) | Services | All | UC-SC03-03, UC-SC03-13 |
| [S-SC03-L12 Shared items](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l12-shared-items.md) | Services | All | UC-SC03-11 |
| [S-SC03-L13 Satisfaction surveys](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l13-satisfaction-surveys.md) | Services | Open: Sent | UC-SC03-12 |
| [S-SC03-L14 Pricing models](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l14-pricing-models.md) | Services | All | UC-SC03-02 |
| [S-SC03-L15 Resource plans](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l15-resource-plans.md) | Services | All | UC-SC03-03 |
| [S-SC03-L16 Staffing needs](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l16-staffing-needs.md) | Services | All | UC-SC03-03 |
| [S-SC03-L17 Assignment contracts](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l17-assignment-contracts.md) | Services | All | UC-SC03-16 |
| [S-SC03-L18 Creative proofs](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l18-creative-proofs.md) | Services | All | UC-SC03-17 |
| [S-SC03-L19 Certificates](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l19-certificates.md) | Services | All | UC-SC03-18 |
| [S-SC03-L20 Answers](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l20-answers.md) | Services | All | UC-SC03-19 |
| [S-SC14-L07 Sprints](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l07-sprints.md) | IT and software | All | UC-SC14-07 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U24 | desktop | ![Workspace, U24, light](mockups/workspace-desktop-light.png) | ![Workspace, U24, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U24 | phone | ![Workspace, U24, light](mockups/workspace-phone-light.png) | ![Workspace, U24, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
