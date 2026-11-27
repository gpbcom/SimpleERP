🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧮 [Payroll officer: app shell and home](README.md) › 🧰 U45 Payroll officer: workspace

# 🧰 U45 Payroll officer: workspace

**Status:** ✅ specified

## Purpose

The views [U45 Payroll officer](../../../01-users/personas/u45-payroll-officer.md) works with, embedded on their
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
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | Mine: manager | UC-F9-20, UC-F9-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L05 HR duties](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l05-hr-duties.md) | HR and projects | Mine: employee | UC-F9-23 |
| [S-F9-L20 Equality indexes](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l20-equality-indexes.md) | HR and projects | All | UC-F9-20 |
| [S-F13-L01 Payroll establishments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l01-payroll-establishments.md) | Payroll (plugin) | All | UC-F13-01 |
| [S-F13-L02 Employee pay profiles](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l02-employee-pay-profiles.md) | Payroll (plugin) | Mine: employee | UC-F13-02, UC-F13-17, UC-F13-21, UC-F13-22 |
| [S-F13-L03 Pay inputs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l03-pay-inputs.md) | Payroll (plugin) | Mine: employee | UC-F13-03, UC-F13-14, UC-F13-31, UC-F13-33 |
| [S-F13-L04 Payslip lines](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l04-payslip-lines.md) | Payroll (plugin) | All | UC-F13-04, UC-F13-05, UC-F13-16, UC-F13-29 and more |
| [S-F13-L05 Withholding rates](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l05-withholding-rates.md) | Payroll (plugin) | Mine: employee | UC-F13-06 |
| [S-F13-L06 Pay runs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l06-pay-runs.md) | Payroll (plugin) | All | UC-F13-07, UC-F13-34 |
| [S-F13-L07 Payslips](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l07-payslips.md) | Payroll (plugin) | Mine: employee | UC-F13-08, UC-F13-20 |
| [S-F13-L08 Pay transfers](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l08-pay-transfers.md) | Payroll (plugin) | Mine: employee | UC-F13-09, UC-F13-26, UC-F13-27 |
| [S-F13-L09 Social declarations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l09-social-declarations.md) | Payroll (plugin) | Open: Accepted, Filed, Returned | UC-F13-10, UC-F13-24 |
| [S-F13-L10 Corrections](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l10-corrections.md) | Payroll (plugin) | Mine: employee | UC-F13-11 |
| [S-F13-L11 Contribution payments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l11-contribution-payments.md) | Payroll (plugin) | All | UC-F13-12, UC-F13-25 |
| [S-F13-L12 Payroll entries](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l12-payroll-entries.md) | Payroll (plugin) | All | UC-F13-13, UC-F13-28 |
| [S-F13-L13 Sick leaves](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l13-sick-leaves.md) | Payroll (plugin) | Mine: employee | UC-F13-14 |
| [S-F13-L14 End-of-contract files](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l14-end-of-contract-files.md) | Payroll (plugin) | Mine: employee | UC-F13-15 |
| [S-F13-L15 Yearly payroll reports](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l15-yearly-payroll-reports.md) | Payroll (plugin) | All | UC-F13-18 |
| [S-F13-L16 Rate sets](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l16-rate-sets.md) | Payroll (plugin) | All | UC-F13-19 |
| [S-F13-L17 Scheme memberships](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l17-scheme-memberships.md) | Payroll (plugin) | Mine: employee | UC-F13-21 |
| [S-F13-L18 Special pay regimes](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l18-special-pay-regimes.md) | Payroll (plugin) | Mine: employee | UC-F13-22, UC-F13-23, UC-F13-24, UC-F13-25 |
| [S-F13-L19 Garnishments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l19-garnishments.md) | Payroll (plugin) | Mine: employee | UC-F13-09, UC-F13-26 |
| [S-F13-L20 Pay advances](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l20-pay-advances.md) | Payroll (plugin) | Mine: employee | UC-F13-09, UC-F13-27 |
| [S-F13-L21 Profit-sharing years](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l21-profit-sharing-years.md) | Payroll (plugin) | All | UC-F13-28 |
| [S-F13-L22 Leave pay valuations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l22-leave-pay-valuations.md) | Payroll (plugin) | Mine: employee | UC-F13-29 |
| [S-F13-L23 Agreement families](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l23-agreement-families.md) | Payroll (plugin) | All | UC-F13-01, UC-F13-05, UC-F13-19, UC-F13-30 and more |
| [S-F13-L24 Payroll cost allocations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l24-payroll-cost-allocations.md) | Payroll (plugin) | Mine: employee | UC-F13-13, UC-F13-34 |
| [S-F13-L25 Analytic axis](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l25-analytic-axis.md) | Payroll (plugin) | All | UC-F13-34 |
| [S-F13-L26 Employee benefits](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l26-employee-benefits.md) | Payroll (plugin) | All | UC-F13-17 |
| [S-F13-L27 Pay simulations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l27-pay-simulations.md) | Payroll (plugin) | All | UC-F13-16 |
| [S-F13-L28 Postings](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l28-postings.md) | Payroll (plugin) | All | UC-F13-35 |
| [S-F13-L29 Days packages](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l29-days-packages.md) | Payroll (plugin) | All | UC-F13-36 |
| [S-F13-L30 Payroll handovers](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l30-payroll-handovers.md) | Payroll (plugin) | All | UC-F13-37 |
| [S-F13-L31 Delegation hours](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l31-delegation-hours.md) | Payroll (plugin) | All | UC-F13-38 |
| [S-F21-L21 Parallel runs](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l21-parallel-runs.md) | Onboarding and module activation | All | UC-F21-28 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U45 | desktop | ![Workspace, U45, light](mockups/workspace-desktop-light.png) | ![Workspace, U45, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U45 | phone | ![Workspace, U45, light](mockups/workspace-phone-light.png) | ![Workspace, U45, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
