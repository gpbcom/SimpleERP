🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🗂️ [Assistant: app shell and home](README.md) › 🧰 U37 Professional's assistant: workspace

# 🧰 U37 Professional's assistant: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U37 Professional's assistant](../../../01-users/personas/u37-assistant.md) works with, embedded on their
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
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-SC11-L01 Client identities](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l01-client-identities.md) | Professional firms | All | UC-SC11-01 |
| [S-SC11-L02 Beneficial owners](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l02-beneficial-owners.md) | Professional firms | All | UC-SC11-01 |
| [S-SC11-L03 Conflict checks](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l03-conflict-checks.md) | Professional firms | All | UC-SC11-02 |
| [S-SC11-L05 Matters](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l05-matters.md) | Professional firms | Open: Open | UC-SC11-04, UC-SC11-20 |
| [S-SC11-L07 Fee bills](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l07-fee-bills.md) | Professional firms | All | UC-SC11-06 |
| [S-SC11-L08 Trust movements](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l08-trust-movements.md) | Professional firms | All | UC-SC11-21 |
| [S-SC11-L09 Deadlines](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l09-deadlines.md) | Professional firms | Mine: owner | UC-SC11-20, UC-SC11-08 |
| [S-SC11-L10 Matter documents](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l10-matter-documents.md) | Professional firms | All | UC-SC11-09 |
| [S-SC11-L11 Filings](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l11-filings.md) | Professional firms | All | UC-SC11-11 |
| [S-SC11-L16 Deeds](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l16-deeds.md) | Professional firms | All | UC-SC11-21 |
| [S-SC11-L18 Service acts](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l18-service-acts.md) | Professional firms | All | UC-SC11-23 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Professional firms](../../../08-sectors/sc11-professional-firms/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U37 | desktop | ![Workspace, U37, light](mockups/workspace-desktop-light.png) | ![Workspace, U37, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U37 | phone | ![Workspace, U37, light](mockups/workspace-phone-light.png) | ![Workspace, U37, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
