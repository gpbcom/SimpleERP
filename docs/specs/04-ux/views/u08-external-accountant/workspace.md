🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
📊 [External accountant: app shell and home](README.md) › 🧰 U08 External accountant: workspace

# 🧰 U08 External accountant: workspace

**Status:** ✅ specified

## Purpose

The views [U08 External accountant](../../../01-users/personas/u08-external-accountant.md) works with, embedded on their
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
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Needs attention | UC-F21-23 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Open: Private, Shared | UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-16 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F8-L01 Accounts](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l01-accounts.md) | Accounting | All | UC-F8-01, UC-F8-11 |
| [S-F8-L02 Journals](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l02-journals.md) | Accounting | All | UC-F8-01, UC-F8-14 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | Needs attention | UC-F8-02, UC-F8-14, UC-F8-11, UC-F8-26 and more |
| [S-F8-L06 Tax returns](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l06-tax-returns.md) | Accounting | Needs attention | UC-F8-07, UC-F8-24 |
| [S-F8-L07 Fixed assets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l07-fixed-assets.md) | Accounting | All | UC-F8-37 |
| [S-F8-L10 Fiscal periods](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l10-fiscal-periods.md) | Accounting | All | UC-F8-01, UC-F8-10, UC-F8-25 |
| [S-F8-L11 Consolidation groups](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l11-consolidation-groups.md) | Accounting | All | UC-F8-13 |
| [S-F8-L12 Filing partners](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l12-filing-partners.md) | Accounting | All | UC-F8-07 |
| [S-F8-L13 Books](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l13-books.md) | Accounting | Open: Refused | UC-F8-15 |
| [S-F8-L19 Dedicated funds](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l19-dedicated-funds.md) | Accounting | Needs attention | UC-F8-23 |
| [S-F8-L20 Volunteer contributions](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l20-volunteer-contributions.md) | Accounting | All | UC-F8-23 |
| [S-F8-L21 Corporate tax computations](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l21-corporate-tax-computations.md) | Accounting | Needs attention | UC-F8-24 |
| [S-F8-L22 Annual accounts files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l22-annual-accounts-files.md) | Accounting | Needs attention | UC-F8-25 |
| [S-F8-L23 Doubtful debt provisions](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l23-doubtful-debt-provisions.md) | Accounting | All | UC-F8-26 |
| [S-F8-L24 Variance comments](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l24-variance-comments.md) | Accounting | Needs attention | UC-F8-27 |
| [S-F8-L26 Accountant requests](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l26-accountant-requests.md) | Accounting | Needs attention | UC-F8-29 |
| [S-F8-L27 FEC files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l27-fec-files.md) | Accounting | All | UC-F8-01, UC-F8-10, UC-F21-22 |
| [S-F8-L29 Entry annotations](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l29-entry-annotations.md) | Accounting | All | UC-F8-01, UC-F8-10 |
| [S-F8-L31 Closing checklists](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l31-closing-checklists.md) | Accounting | All | UC-F8-10 |
| [S-F8-L33 Tax rates](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l33-tax-rates.md) | Accounting | All | UC-F8-01 |
| [S-F8-L41 Leases](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l41-leases.md) | Accounting | Needs attention | UC-F8-37 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F13-L07 Payslips](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l07-payslips.md) | Payroll (plugin) | All | UC-F13-37 |
| [S-F13-L12 Payroll entries](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l12-payroll-entries.md) | Payroll (plugin) | All | UC-F13-37 |
| [S-F13-L30 Payroll handovers](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l30-payroll-handovers.md) | Payroll (plugin) | Needs attention | UC-F13-37 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01, UC-F15-13 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | Needs attention | UC-F15-01 |
| [S-F15-L05 Compliance duties](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l05-compliance-duties.md) | Legal assistant | Needs attention | UC-F15-09 |
| [S-F15-L07 Corporate decisions](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l07-corporate-decisions.md) | Legal assistant | All | UC-F15-09 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | Needs attention | UC-F15-01 |
| [S-F21-L01 Onboarding progresses](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l01-onboarding-progresses.md) | Onboarding and module activation | All | UC-F21-27 |
| [S-F21-L07 Import jobs](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l07-import-jobs.md) | Onboarding and module activation | All | UC-F21-21 |
| [S-F21-L14 Migration sources](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l14-migration-sources.md) | Onboarding and module activation | Needs attention | UC-F21-21 |
| [S-F21-L15 Opening balance checks](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l15-opening-balance-checks.md) | Onboarding and module activation | All | UC-F21-22 |
| [S-F21-L17 Migration guides](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l17-migration-guides.md) | Onboarding and module activation | All | UC-F21-21 |
| [S-F21-L20 Cutover plans](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l20-cutover-plans.md) | Onboarding and module activation | Needs attention | UC-F21-27 |
| [S-F23-L02 Scenarios](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l02-scenarios.md) | What-if simulation and impact | All | UC-F23-19 |
| [S-F23-L10 Scenario comments](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l10-scenario-comments.md) | What-if simulation and impact | All | UC-F23-19, UC-F23-29 |
| [S-F23-L12 Financing options](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l12-financing-options.md) | What-if simulation and impact | Needs attention | UC-F23-29 |
| [S-F24-L06 Sync jobs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l06-sync-jobs.md) | Integrations hub | All | UC-F24-31 |
| [S-F24-L19 Firm syncs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l19-firm-syncs.md) | Integrations hub | Needs attention | UC-F24-31 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U08 | desktop | ![Workspace, U08, light](mockups/workspace-desktop-light.png) | ![Workspace, U08, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U08 | phone | ![Workspace, U08, light](mockups/workspace-phone-light.png) | ![Workspace, U08, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
