🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-05 Declarations and reports](README.md) › 🖥️ S-SC16-16 Memberships

# 🖥️ S-SC16-16 Memberships

**Status:** ✅ specified

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to run museum memberships and passes,
[UC-SC16-16](../../use-cases/05-declarations-and-reports/uc-sc16-16-run-museum-memberships-and-passes.md).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-05 step 3, U44 | desktop | ![FL-SC16-05 step 3, U44, light](../../images/05-declarations-and-reports/u44-box-office-agent/3-memberships-desktop-light.png) | ![FL-SC16-05 step 3, U44, dark](../../images/05-declarations-and-reports/u44-box-office-agent/3-memberships-desktop-dark.png) |
| FL-SC16-05 step 3, U44 | phone | ![FL-SC16-05 step 3, U44, light](../../images/05-declarations-and-reports/u44-box-office-agent/3-memberships-phone-light.png) | ![FL-SC16-05 step 3, U44, dark](../../images/05-declarations-and-reports/u44-box-office-agent/3-memberships-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-16-memberships-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-16-memberships-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-16-memberships-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-16-memberships-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-16-memberships-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-16-memberships-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-16-memberships-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-16-memberships-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-16 Membership](../../data/e-sc16-16-membership.md), shown as the entity pages list them, with
their examples.

## Actions

- Sell: [UC-SC16-16](../../use-cases/05-declarations-and-reports/uc-sc16-16-run-museum-memberships-and-passes.md), step
  1.
- Book a slot:
  [UC-SC16-16](../../use-cases/05-declarations-and-reports/uc-sc16-16-run-museum-memberships-and-passes.md), step 2.
- Scan: [UC-SC16-16](../../use-cases/05-declarations-and-reports/uc-sc16-16-run-museum-memberships-and-passes.md), step
  3.
- Renew: [UC-SC16-16](../../use-cases/05-declarations-and-reports/uc-sc16-16-run-museum-memberships-and-passes.md), step
  4.

## States

- Normal: memberships, passes and timed entries.
- Empty: "No membership".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, expired: renewal is offered.
- Read-only: members read their own.
- Offline: scans at the entrance work like the gates; sales need the network.

Shown entities (VD-15): [E-SC16-16 Membership](../../data/e-sc16-16-membership.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-16 Membership | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U44 | `u09-customer/s-sc16-16-memberships-e-sc16-16-membership-active-phone-{light,dark}.png`, `u44-box-office-agent/s-sc16-16-memberships-e-sc16-16-membership-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC16-05 Declarations and reports](../../flows/fl-sc16-05-declarations-and-reports.md)

## Open questions

None.

---

⬅️ [S-SC16-15 Ticket tax](s-sc16-15-ticket-tax.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-17 Refunds](../02-ticketing/s-sc16-17-refunds.md)
