🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-02 Donations and receipts](README.md) › 🖥️ S-SC08-07 Regular gifts

# 🖥️ S-SC08-07 Regular gifts

**Status:** 🔄 waiting for the owner

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to manage regular donors
([UC-SC08-07](../../use-cases/02-donations-and-receipts/uc-sc08-07-manage-regular-donors.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-02 step 4, U31 | desktop | ![FL-SC08-02 step 4, U31, light](../../images/02-donations-and-receipts/u31-treasurer/4-regular-gifts-desktop-light.png) | ![FL-SC08-02 step 4, U31, dark](../../images/02-donations-and-receipts/u31-treasurer/4-regular-gifts-desktop-dark.png) |
| FL-SC08-02 step 4, U31 | phone | ![FL-SC08-02 step 4, U31, light](../../images/02-donations-and-receipts/u31-treasurer/4-regular-gifts-phone-light.png) | ![FL-SC08-02 step 4, U31, dark](../../images/02-donations-and-receipts/u31-treasurer/4-regular-gifts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-07-regular-gifts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-07-regular-gifts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-07-regular-gifts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-07-regular-gifts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-07-regular-gifts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-07-regular-gifts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-07-regular-gifts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-07-regular-gifts-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-04 Gift](../../data/e-sc08-04-gift.md),
[E-SC08-07 Debit mandate](../../data/e-sc08-07-debit-mandate.md), shown as the entity pages list them, with their
examples.

## Actions

- Sign the mandate: [UC-SC08-07](../../use-cases/02-donations-and-receipts/uc-sc08-07-manage-regular-donors.md), step 1.
- Collect monthly: [UC-SC08-07](../../use-cases/02-donations-and-receipts/uc-sc08-07-manage-regular-donors.md), step 2.
- Match: [UC-SC08-07](../../use-cases/02-donations-and-receipts/uc-sc08-07-manage-regular-donors.md), step 3.
- Yearly receipt: [UC-SC08-07](../../use-cases/02-donations-and-receipts/uc-sc08-07-manage-regular-donors.md), step 4.

## States

- Normal: mandates with amount, frequency and debits.
- Empty: "No regular donor".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a debit rejected: the donor is told.
- Read-only: a revoked mandate is read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC08-04 Gift](../../data/e-sc08-04-gift.md),
[E-SC08-07 Debit mandate](../../data/e-sc08-07-debit-mandate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-04 Gift | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U31 | `u09-customer/s-sc08-07-regular-gifts-e-sc08-04-gift-active-phone-{light,dark}.png`, `u31-treasurer/s-sc08-07-regular-gifts-e-sc08-04-gift-active-{desktop,phone}-{light,dark}.png` |
| E-SC08-07 Debit mandate | Signed | Badge "Signed"; a new record starts here; next: Suspended or Revoked (UC-SC08-07, BR-SC08-12); fields editable within the role | U09, U31 | `u09-customer/s-sc08-07-regular-gifts-e-sc08-07-debit-mandate-signed-phone-{light,dark}.png`, `u31-treasurer/s-sc08-07-regular-gifts-e-sc08-07-debit-mandate-signed-{desktop,phone}-{light,dark}.png` |
| E-SC08-07 Debit mandate | Suspended | Badge "Suspended"; next: Signed (UC-SC08-07); fields editable within the role | U09, U31 | `u09-customer/s-sc08-07-regular-gifts-e-sc08-07-debit-mandate-suspended-phone-{light,dark}.png`, `u31-treasurer/s-sc08-07-regular-gifts-e-sc08-07-debit-mandate-suspended-{desktop,phone}-{light,dark}.png` |
| E-SC08-07 Debit mandate | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U09, U31 | `u09-customer/s-sc08-07-regular-gifts-e-sc08-07-debit-mandate-revoked-phone-{light,dark}.png`, `u31-treasurer/s-sc08-07-regular-gifts-e-sc08-07-debit-mandate-revoked-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC08-06 Tax receipts](s-sc08-06-tax-receipts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-08 Grants](../03-grants/s-sc08-08-grants.md)
