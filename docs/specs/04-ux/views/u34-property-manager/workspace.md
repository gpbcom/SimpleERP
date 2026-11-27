🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏢 [Property manager: app shell and home](README.md) › 🧰 U34 Property manager: workspace

# 🧰 U34 Property manager: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U34 Property manager](../../../01-users/personas/u34-property-manager.md) works with, embedded on their
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
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC10-21, UC-SC10-24 |
| [S-F8-L04 Bank lines](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l04-bank-lines.md) | Accounting | All | UC-F8-21 |
| [S-F8-L17 Client money ledgers](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l17-client-money-ledgers.md) | Accounting | Needs attention | UC-F8-21, UC-SC10-12 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-SC10-L07 Leases](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l07-leases.md) | Real estate | All | UC-SC10-07, UC-SC10-09, UC-SC10-20 |
| [S-SC10-L08 Deposits](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l08-deposits.md) | Real estate | All | UC-SC10-07, UC-SC10-10 |
| [S-SC10-L09 Rent calls](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l09-rent-calls.md) | Real estate | All | UC-SC10-08, UC-SC10-14 |
| [S-SC10-L10 Charge settlements](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l10-charge-settlements.md) | Real estate | All | UC-SC10-11 |
| [S-SC10-L11 Landlord statements](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l11-landlord-statements.md) | Real estate | All | UC-SC10-12 |
| [S-SC10-L12 Diagnostics](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l12-diagnostics.md) | Real estate | All | UC-SC10-13 |
| [S-SC10-L13 Co-owners' assemblies](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l13-co-owners-assemblies.md) | Real estate | All | UC-SC10-15, UC-SC10-20 |
| [S-SC10-L14 Call for funds](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l14-call-for-funds.md) | Real estate | All | UC-SC10-16 |
| [S-SC10-L15 Works funds](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l15-works-funds.md) | Real estate | All | UC-SC10-17 |
| [S-SC10-L16 Co-ownerships](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l16-co-ownerships.md) | Real estate | All | UC-SC10-18 |
| [S-SC10-L17 Stays](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l17-stays.md) | Real estate | All | UC-SC10-21 |
| [S-SC10-L18 Commercial leases](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l18-commercial-leases.md) | Real estate | All | UC-SC10-22 |
| [S-SC10-L19 Furnished properties](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l19-furnished-properties.md) | Real estate | All | UC-SC10-23 |
| [S-SC10-L20 Memberships](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l20-memberships.md) | Real estate | All | UC-SC10-24 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Real estate](../../../08-sectors/sc10-real-estate/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U34 | desktop | ![Workspace, U34, light](mockups/workspace-desktop-light.png) | ![Workspace, U34, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U34 | phone | ![Workspace, U34, light](mockups/workspace-phone-light.png) | ![Workspace, U34, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
