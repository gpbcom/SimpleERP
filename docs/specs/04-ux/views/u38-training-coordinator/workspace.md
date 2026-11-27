🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧑‍🏫 [Training coordinator: app shell and home](README.md) › 🧰 U38 Training coordinator: workspace

# 🧰 U38 Training coordinator: workspace

**Status:** ✅ specified

## Purpose

The views [U38 Training coordinator](../../../01-users/personas/u38-training-coordinator.md) works with, embedded on
their [home screen](README.md)
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
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Needs attention | UC-SC12-05 |
| [S-F2-L05 Record types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l05-record-types.md) | No-code configuration | Needs attention | UC-F2-18 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Needs attention | UC-F2-18, UC-F2-19 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-F2-19, UC-SC12-02 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Needs attention | UC-F6-20 |
| [S-F6-L14 Funder agreements](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l14-funder-agreements.md) | Customers and sales | Needs attention | UC-F6-20, UC-SC12-04 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Needs attention | UC-F9-25 |
| [S-F9-L22 Training sessions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l22-training-sessions.md) | HR and projects | Open: Planned, Held | UC-F9-25 |
| [S-F9-L52 Online courses](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l52-online-courses.md) | HR and projects | Mine: learner | UC-F9-47 |
| [S-F11-L03 Online products](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l03-online-products.md) | Online shop (plugin) | All | UC-F9-47 |
| [S-SC12-L01 Courses](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l01-courses.md) | Education and training | All | UC-SC12-01 |
| [S-SC12-L02 Course sessions](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l02-course-sessions.md) | Education and training | Needs attention | UC-SC12-02, UC-SC12-20, UC-SC12-16 |
| [S-SC12-L03 Enrolments](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l03-enrolments.md) | Education and training | Open: Enrolled | UC-SC12-03, UC-SC12-05 |
| [S-SC12-L04 Training agreements](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l04-training-agreements.md) | Education and training | All | UC-SC12-03 |
| [S-SC12-L05 Training fundings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l05-training-fundings.md) | Education and training | All | UC-SC12-04 |
| [S-SC12-L06 Attendance sheets](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l06-attendance-sheets.md) | Education and training | All | UC-SC12-06, UC-SC12-20 |
| [S-SC12-L07 E-learning records](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l07-e-learning-records.md) | Education and training | All | UC-SC12-07 |
| [S-SC12-L08 Completion certificates](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l08-completion-certificates.md) | Education and training | All | UC-SC12-08 |
| [S-SC12-L09 Survey answers](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l09-survey-answers.md) | Education and training | All | UC-SC12-09, UC-SC12-14 |
| [S-SC12-L10 Training invoices](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l10-training-invoices.md) | Education and training | All | UC-SC12-10 |
| [S-SC12-L11 Trainer profiles](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l11-trainer-profiles.md) | Education and training | All | UC-SC12-11 |
| [S-SC12-L12 Quality evidences](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l12-quality-evidences.md) | Education and training | All | UC-SC12-12 |
| [S-SC12-L13 Yearly training reports](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l13-yearly-training-reports.md) | Education and training | All | UC-SC12-13 |
| [S-SC12-L14 Students](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l14-students.md) | Education and training | All | UC-SC12-15 |
| [S-SC12-L15 Classes](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l15-classes.md) | Education and training | All | UC-SC12-16 |
| [S-SC12-L16 Grades](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l16-grades.md) | Education and training | All | UC-SC12-17 |
| [S-SC12-L17 Pupil absences](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l17-pupil-absences.md) | Education and training | All | UC-SC12-18 |
| [S-SC12-L18 School fees](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l18-school-fees.md) | Education and training | All | UC-SC12-24 |
| [S-SC12-L20 Apprenticeship contracts](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l20-apprenticeship-contracts.md) | Education and training | All | UC-SC12-21 |
| [S-SC12-L21 Driving lessons](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l21-driving-lessons.md) | Education and training | All | UC-SC12-22 |
| [S-SC12-L22 Childcare places](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l22-childcare-places.md) | Education and training | All | UC-SC12-23 |
| [S-SC12-L23 Meal bookings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l23-meal-bookings.md) | Education and training | All | UC-SC12-24 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[Education and training](../../../08-sectors/sc12-education-and-training/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U38 | desktop | ![Workspace, U38, light](mockups/workspace-desktop-light.png) | ![Workspace, U38, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U38 | phone | ![Workspace, U38, light](mockups/workspace-phone-light.png) | ![Workspace, U38, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
