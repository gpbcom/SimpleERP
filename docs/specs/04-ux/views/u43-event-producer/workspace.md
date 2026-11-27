🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🎬 [Event producer: app shell and home](README.md) › 🧰 U43 Event producer: workspace

# 🧰 U43 Event producer: workspace

**Status:** ✅ specified

## Purpose

The views [U43 Event producer](../../../01-users/personas/u43-event-producer.md) works with, embedded on their
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
| [S-F2-L05 Record types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l05-record-types.md) | No-code configuration | Needs attention | UC-F2-18 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Needs attention | UC-F2-18 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-SC16-02, UC-SC16-11 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F5-L07 Registration events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l07-registration-events.md) | Social media and marketing | Needs attention | UC-F5-17, UC-SC16-01 |
| [S-F5-L11 Ticket type and seat maps](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l11-ticket-type-and-seat-maps.md) | Social media and marketing | Needs attention | UC-F5-17, UC-F5-18 |
| [S-F5-L12 Event tickets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l12-event-tickets.md) | Social media and marketing | All | UC-F5-18 |
| [S-F5-L20 Waiting lists](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l20-waiting-lists.md) | Social media and marketing | All | UC-F5-17 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC16-24 |
| [S-F8-L06 Tax returns](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l06-tax-returns.md) | Accounting | Open: Prepared, Validated, Filed | UC-SC16-22, UC-SC16-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F13-L09 Social declarations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l09-social-declarations.md) | Payroll (plugin) | Needs attention | UC-F13-24 |
| [S-F13-L18 Special pay regimes](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l18-special-pay-regimes.md) | Payroll (plugin) | Open: Active, Changed | UC-F13-24 |
| [S-SC16-L01 Shows](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l01-shows.md) | Events and culture | Open: OnSale, Approved, Held | UC-SC16-01, UC-SC16-18, UC-SC16-20 |
| [S-SC16-L02 Event budgets](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l02-event-budgets.md) | Events and culture | Needs attention | UC-SC16-01, UC-SC16-18 |
| [S-SC16-L03 Venue rooms](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l03-venue-rooms.md) | Events and culture | All | UC-SC16-02 |
| [S-SC16-L04 Artist contracts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l04-artist-contracts.md) | Events and culture | All | UC-SC16-03 |
| [S-SC16-L05 Rider items](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l05-rider-items.md) | Events and culture | Open: Checked | UC-SC16-03 |
| [S-SC16-L06 Performer declarations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l06-performer-declarations.md) | Events and culture | All | UC-SC16-04 |
| [S-SC16-L07 Ticket orders](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l07-ticket-orders.md) | Events and culture | Open: Refunded, Exchanged | UC-SC16-17, UC-SC16-19 |
| [S-SC16-L08 Admission tickets](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l08-admission-tickets.md) | Events and culture | Open: Sent | UC-SC16-06 |
| [S-SC16-L09 Accreditations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l09-accreditations.md) | Events and culture | All | UC-SC16-08 |
| [S-SC16-L10 Staffing posts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l10-staffing-posts.md) | Events and culture | All | UC-SC16-09, UC-SC16-20 |
| [S-SC16-L11 Sponsorships](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l11-sponsorships.md) | Events and culture | All | UC-SC16-10 |
| [S-SC16-L12 Stands](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l12-stands.md) | Events and culture | All | UC-SC16-11 |
| [S-SC16-L13 Event tills](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l13-event-tills.md) | Events and culture | All | UC-SC16-12 |
| [S-SC16-L14 Safety files](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l14-safety-files.md) | Events and culture | Needs attention | UC-SC16-13 |
| [S-SC16-L15 Show declarations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l15-show-declarations.md) | Events and culture | All | UC-SC16-14, UC-SC16-15 |
| [S-SC16-L17 Attendee messages](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l17-attendee-messages.md) | Events and culture | All | UC-SC16-19 |
| [S-SC16-L18 Ticket refunds](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l18-ticket-refunds.md) | Events and culture | All | UC-SC16-17 |
| [S-SC16-L19 Cashless accounts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l19-cashless-accounts.md) | Events and culture | All | UC-SC16-21 |
| [S-SC16-L20 Screenings](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l20-screenings.md) | Events and culture | All | UC-SC16-22 |
| [S-SC16-L21 Tour dates](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l21-tour-dates.md) | Events and culture | All | UC-SC16-23 |
| [S-SC16-L22 Galleries](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l22-galleries.md) | Events and culture | All | UC-SC16-24 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U43 | desktop | ![Workspace, U43, light](mockups/workspace-desktop-light.png) | ![Workspace, U43, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U43 | phone | ![Workspace, U43, light](mockups/workspace-phone-light.png) | ![Workspace, U43, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
