🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🔑 [Real-estate agent: app shell and home](README.md) › 🧰 U35 Real-estate agent: workspace

# 🧰 U35 Real-estate agent: workspace

**Status:** ✅ specified

## Purpose

The views [U35 Real-estate agent](../../../01-users/personas/u35-real-estate-agent.md) works with, embedded on their
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
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC01-17 |
| [S-F8-L17 Client money ledgers](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l17-client-money-ledgers.md) | Accounting | Open: Open | UC-SC10-05 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-SC01-L16 Off-plan lots](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l16-off-plan-lots.md) | Construction | All | UC-SC01-17 |
| [S-SC10-L01 Mandates](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l01-mandates.md) | Real estate | Mine: owner | UC-SC10-01 |
| [S-SC10-L02 Property listings](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l02-property-listings.md) | Real estate | All | UC-SC10-02 |
| [S-SC10-L03 Viewings](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l03-viewings.md) | Real estate | All | UC-SC10-03 |
| [S-SC10-L04 Offers](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l04-offers.md) | Real estate | All | UC-SC10-04 |
| [S-SC10-L05 Client funds](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l05-client-funds.md) | Real estate | All | UC-SC10-05 |
| [S-SC10-L06 Fee scales](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l06-fee-scales.md) | Real estate | All | UC-SC10-06 |
| [S-SC10-L07 Leases](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l07-leases.md) | Real estate | All | UC-SC10-20 |
| [S-SC10-L12 Diagnostics](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l12-diagnostics.md) | Real estate | All | UC-SC10-02 |
| [S-SC10-L13 Co-owners' assemblies](../../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l13-co-owners-assemblies.md) | Real estate | Mine: co-ownership | UC-SC10-20 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Real estate](../../../08-sectors/sc10-real-estate/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U35 | desktop | ![Workspace, U35, light](mockups/workspace-desktop-light.png) | ![Workspace, U35, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U35 | phone | ![Workspace, U35, light](mockups/workspace-phone-light.png) | ![Workspace, U35, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
