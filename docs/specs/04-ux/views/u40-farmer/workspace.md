🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧑‍🌾 [Farmer: app shell and home](README.md) › 🧰 U40 Farmer: workspace

# 🧰 U40 Farmer: workspace

**Status:** ✅ specified

## Purpose

The views [U40 Farmer](../../../01-users/personas/u40-farmer.md) works with, embedded on their [home screen](README.md)
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
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC13-22, UC-SC13-25 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-SC13-24 |
| [S-F8-L06 Tax returns](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l06-tax-returns.md) | Accounting | Open: Prepared, Validated, Filed | UC-SC13-21 |
| [S-F8-L07 Fixed assets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l07-fixed-assets.md) | Accounting | All | UC-F8-22 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-F8-22, UC-SC13-07 |
| [S-F8-L28 Payment runs](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l28-payment-runs.md) | Accounting | All | UC-SC13-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Open: Draft, Confirmed, InProgress | UC-F12-31 |
| [S-F12-L25 Recipes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l25-recipes.md) | Manufacturing (plugin) | All | UC-F12-31, UC-SC13-13 |
| [S-F13-L11 Contribution payments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l11-contribution-payments.md) | Payroll (plugin) | All | UC-F13-25 |
| [S-F13-L18 Special pay regimes](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l18-special-pay-regimes.md) | Payroll (plugin) | Mine: employee | UC-F13-25 |
| [S-SC13-L01 Plots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l01-plots.md) | Agriculture and food | All | UC-SC13-01, UC-SC13-07 |
| [S-SC13-L02 Crop plans](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l02-crop-plans.md) | Agriculture and food | All | UC-SC13-01, UC-SC13-18 |
| [S-SC13-L03 Field operations](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l03-field-operations.md) | Agriculture and food | All | UC-SC13-02, UC-SC13-03, UC-SC13-20 |
| [S-SC13-L04 Lots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l04-lots.md) | Agriculture and food | Open: Blocked, Refused | UC-SC13-04, UC-SC13-13, UC-SC13-14 |
| [S-SC13-L05 Animals](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l05-animals.md) | Agriculture and food | All | UC-SC13-05, UC-SC13-07, UC-SC13-20 |
| [S-SC13-L06 Veterinary treatments](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l06-veterinary-treatments.md) | Agriculture and food | All | UC-SC13-06 |
| [S-SC13-L07 Machines](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l07-machines.md) | Agriculture and food | All | UC-SC13-08, UC-SC13-18 |
| [S-SC13-L08 Seasonal contracts](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l08-seasonal-contracts.md) | Agriculture and food | All | UC-SC13-09, UC-SC13-19 |
| [S-SC13-L09 Direct sales](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l09-direct-sales.md) | Agriculture and food | All | UC-SC13-10 |
| [S-SC13-L10 Cooperative statements](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l10-cooperative-statements.md) | Agriculture and food | All | UC-SC13-11 |
| [S-SC13-L11 Organic records](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l11-organic-records.md) | Agriculture and food | All | UC-SC13-12 |
| [S-SC13-L12 Batches](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l12-batches.md) | Agriculture and food | All | UC-SC13-13, UC-SC13-14 |
| [S-SC13-L16 CAP aid declarations](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l16-cap-aid-declarations.md) | Agriculture and food | All | UC-SC13-07 |
| [S-SC13-L17 Vine plots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l17-vine-plots.md) | Agriculture and food | All | UC-SC13-21 |
| [S-SC13-L18 Field jobs](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l18-field-jobs.md) | Agriculture and food | All | UC-SC13-22 |
| [S-SC13-L19 Member deliveries](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l19-member-deliveries.md) | Agriculture and food | All | UC-SC13-23 |
| [S-SC13-L20 Basket subscriptions](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l20-basket-subscriptions.md) | Agriculture and food | All | UC-SC13-24 |
| [S-SC13-L21 Timber lots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l21-timber-lots.md) | Agriculture and food | All | UC-SC13-25 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U40 | desktop | ![Workspace, U40, light](mockups/workspace-desktop-light.png) | ![Workspace, U40, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U40 | phone | ![Workspace, U40, light](mockups/workspace-phone-light.png) | ![Workspace, U40, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
