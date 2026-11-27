🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
💰 [Treasurer: app shell and home](README.md) › 🧰 U31 Treasurer: workspace

# 🧰 U31 Treasurer: workspace

**Status:** ✅ specified

## Purpose

The views [U31 Treasurer](../../../01-users/personas/u31-treasurer.md) works with, embedded on their
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
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F8-31, UC-F8-33, UC-SC08-23, UC-SC18-02 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-F8-31, UC-SC18-02 |
| [S-F7-L05 Supplier invoices](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l05-supplier-invoices.md) | Purchasing and stock | All | UC-F8-33, UC-F8-34 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | All | UC-F8-30, UC-F8-31 |
| [S-F8-L07 Fixed assets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l07-fixed-assets.md) | Accounting | All | UC-F8-22 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-F8-22, UC-SC08-20, UC-SC08-08, UC-SC08-09 and more |
| [S-F8-L19 Dedicated funds](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l19-dedicated-funds.md) | Accounting | Open: Open | UC-F8-23, UC-SC08-14 |
| [S-F8-L20 Volunteer contributions](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l20-volunteer-contributions.md) | Accounting | All | UC-F8-23, UC-SC08-11 |
| [S-F8-L28 Payment runs](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l28-payment-runs.md) | Accounting | All | UC-F8-34, UC-SC13-23 |
| [S-F8-L34 Loans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l34-loans.md) | Accounting | All | UC-F8-30 |
| [S-F8-L35 Remittance slips](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l35-remittance-slips.md) | Accounting | All | UC-F8-31 |
| [S-F8-L37 Cash forecasts](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l37-cash-forecasts.md) | Accounting | All | UC-F8-33 |
| [S-F8-L38 Payment orders](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l38-payment-orders.md) | Accounting | All | UC-F8-34 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F15-L17 Funding rounds](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l17-funding-rounds.md) | Legal assistant | All | UC-F15-16, UC-F23-34 |
| [S-F23-L03 Scenario changes](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l03-scenario-changes.md) | What-if simulation and impact | All | UC-F23-04 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-07, UC-F23-23 |
| [S-F23-L09 Change warnings](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l09-change-warnings.md) | What-if simulation and impact | All | UC-F23-18 |
| [S-F23-L12 Financing options](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l12-financing-options.md) | What-if simulation and impact | All | UC-F23-23 |
| [S-F23-L17 Valuations](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l17-valuations.md) | What-if simulation and impact | All | UC-F23-34 |
| [S-SC08-L01 Members](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l01-members.md) | Non-profit association | Mine: contact | UC-SC08-01, UC-SC08-18, UC-SC08-19 |
| [S-SC08-L02 Dues payments](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l02-dues-payments.md) | Non-profit association | All | UC-SC08-01 |
| [S-SC08-L03 Assembly or board meetings](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l03-assembly-or-board-meetings.md) | Non-profit association | All | UC-SC08-02, UC-SC08-03 |
| [S-SC08-L04 Gifts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l04-gifts.md) | Non-profit association | All | UC-SC08-04, UC-SC08-07, UC-SC08-20, UC-SC08-19 |
| [S-SC08-L05 Fundraising campaigns](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l05-fundraising-campaigns.md) | Non-profit association | All | UC-SC08-05 |
| [S-SC08-L06 Tax receipts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l06-tax-receipts.md) | Non-profit association | All | UC-SC08-06 |
| [S-SC08-L07 Debit mandates](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l07-debit-mandates.md) | Non-profit association | Open: Signed, Revoked | UC-SC08-07 |
| [S-SC08-L09 Grant reports](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l09-grant-reports.md) | Non-profit association | All | UC-SC08-09, UC-SC08-14, UC-SC08-15 |
| [S-SC08-L11 Volunteer hours](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l11-volunteer-hours.md) | Non-profit association | All | UC-SC08-11 |
| [S-SC08-L13 Temporary bars](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l13-temporary-bars.md) | Non-profit association | Mine: authorisation | UC-SC08-13 |
| [S-SC08-L15 Gift in kinds](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l15-gift-in-kinds.md) | Non-profit association | All | UC-SC08-16 |
| [S-SC08-L16 Grant applications](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l16-grant-applications.md) | Non-profit association | All | UC-SC08-21 |
| [S-SC08-L18 Member organisations](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l18-member-organisations.md) | Non-profit association | All | UC-SC08-23 |
| [S-SC13-L10 Cooperative statements](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l10-cooperative-statements.md) | Agriculture and food | All | UC-SC13-23 |
| [S-SC13-L19 Member deliveries](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l19-member-deliveries.md) | Agriculture and food | All | UC-SC13-23 |
| [S-SC18-L02 Dues mandates](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l02-dues-mandates.md) | Sports and fitness | All | UC-SC18-02 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Sports and fitness](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U31 | desktop | ![Workspace, U31, light](mockups/workspace-desktop-light.png) | ![Workspace, U31, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U31 | phone | ![Workspace, U31, light](mockups/workspace-phone-light.png) | ![Workspace, U31, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
