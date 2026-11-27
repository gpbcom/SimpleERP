🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-02 Donations and receipts](README.md) › 🖥️ S-SC08-04 Donations

# 🖥️ S-SC08-04 Donations

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to collect donations online and offline,
[UC-SC08-04](../../use-cases/02-donations-and-receipts/uc-sc08-04-collect-donations-online-and-offline.md).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-02 step 1, U31 | desktop | ![FL-SC08-02 step 1, U31, light](../../images/02-donations-and-receipts/u31-treasurer/1-gifts-desktop-light.png) | ![FL-SC08-02 step 1, U31, dark](../../images/02-donations-and-receipts/u31-treasurer/1-gifts-desktop-dark.png) |
| FL-SC08-02 step 1, U31 | phone | ![FL-SC08-02 step 1, U31, light](../../images/02-donations-and-receipts/u31-treasurer/1-gifts-phone-light.png) | ![FL-SC08-02 step 1, U31, dark](../../images/02-donations-and-receipts/u31-treasurer/1-gifts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-04-donations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-04-donations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-04-donations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-04-donations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-04-donations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-04-donations-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-04-donations-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-04-donations-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-04 Gift](../../data/e-sc08-04-gift.md), shown as the entity pages list them, with their examples.

## Actions

- Give: [UC-SC08-04](../../use-cases/02-donations-and-receipts/uc-sc08-04-collect-donations-online-and-offline.md), step
  1.
- Match the donor:
  [UC-SC08-04](../../use-cases/02-donations-and-receipts/uc-sc08-04-collect-donations-online-and-offline.md), step 2.
- Record purpose:
  [UC-SC08-04](../../use-cases/02-donations-and-receipts/uc-sc08-04-collect-donations-online-and-offline.md), step 3.
- Thank: [UC-SC08-04](../../use-cases/02-donations-and-receipts/uc-sc08-04-collect-donations-online-and-offline.md),
  step 4.

## States

- Normal: gifts with donor, amount, method, campaign and purpose.
- Empty: "No gift yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an unknown donor: a donor record is created.
- Read-only: posted gifts are read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC08-04 Gift](../../data/e-sc08-04-gift.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-04 Gift | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U31 | `u09-customer/s-sc08-04-donations-e-sc08-04-gift-active-phone-{light,dark}.png`, `u31-treasurer/s-sc08-04-donations-e-sc08-04-gift-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC08-02 Donations and receipts](../../flows/fl-sc08-02-donations-and-receipts.md)

## Open questions

None.

---

⬅️ [S-SC08-03 Board](../01-members-and-governance/s-sc08-03-board.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-05 Campaigns](s-sc08-05-campaigns.md)
