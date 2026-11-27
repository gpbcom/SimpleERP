🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🎤 [Trainer: app shell and home](README.md) › 🧰 U39 Trainer: workspace

# 🧰 U39 Trainer: workspace

**Status:** ✅ specified

## Purpose

The views [U39 Trainer](../../../01-users/personas/u39-trainer.md) works with, embedded on their
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
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-SC12-L02 Course sessions](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l02-course-sessions.md) | Education and training | Mine: trainer | UC-SC12-20 |
| [S-SC12-L05 Training fundings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l05-training-fundings.md) | Education and training | All | UC-SC12-22 |
| [S-SC12-L06 Attendance sheets](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l06-attendance-sheets.md) | Education and training | All | UC-SC12-06, UC-SC12-20 |
| [S-SC12-L08 Completion certificates](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l08-completion-certificates.md) | Education and training | All | UC-SC12-08 |
| [S-SC12-L16 Grades](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l16-grades.md) | Education and training | All | UC-SC12-17 |
| [S-SC12-L17 Pupil absences](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l17-pupil-absences.md) | Education and training | All | UC-SC12-18 |
| [S-SC12-L21 Driving lessons](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l21-driving-lessons.md) | Education and training | All | UC-SC12-22 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Education and training](../../../08-sectors/sc12-education-and-training/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U39 | desktop | ![Workspace, U39, light](mockups/workspace-desktop-light.png) | ![Workspace, U39, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U39 | phone | ![Workspace, U39, light](mockups/workspace-phone-light.png) | ![Workspace, U39, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
