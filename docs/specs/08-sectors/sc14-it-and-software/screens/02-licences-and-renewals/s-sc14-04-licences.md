🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-02 Licences and renewals](README.md) › 🖥️ S-SC14-04 Licences

# 🖥️ S-SC14-04 Licences

**Status:** ✅ specified

## Personas

- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to manage licences, keys and renewals
([UC-SC14-04](../../use-cases/02-licences-and-renewals/uc-sc14-04-manage-licences-keys-and-renewals.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-02 step 1, U41 | desktop | ![FL-SC14-02 step 1, U41, light](../../images/02-licences-and-renewals/u41-customer-success-manager/1-licences-desktop-light.png) | ![FL-SC14-02 step 1, U41, dark](../../images/02-licences-and-renewals/u41-customer-success-manager/1-licences-desktop-dark.png) |
| FL-SC14-02 step 1, U41 | phone | ![FL-SC14-02 step 1, U41, light](../../images/02-licences-and-renewals/u41-customer-success-manager/1-licences-phone-light.png) | ![FL-SC14-02 step 1, U41, dark](../../images/02-licences-and-renewals/u41-customer-success-manager/1-licences-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-04-licences-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-04-licences-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-04-licences-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-04-licences-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-04-licences-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-04-licences-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-04-licences-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-04-licences-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-04 Software licence](../../data/e-sc14-04-software-licence.md), shown as the entity pages list
them, with their examples.

## Actions

- Issue the key: [UC-SC14-04](../../use-cases/02-licences-and-renewals/uc-sc14-04-manage-licences-keys-and-renewals.md),
  step 1.
- Track the term:
  [UC-SC14-04](../../use-cases/02-licences-and-renewals/uc-sc14-04-manage-licences-keys-and-renewals.md), step 2.
- Prepare the renewal:
  [UC-SC14-04](../../use-cases/02-licences-and-renewals/uc-sc14-04-manage-licences-keys-and-renewals.md), step 3.
- Renew: [UC-SC14-04](../../use-cases/02-licences-and-renewals/uc-sc14-04-manage-licences-keys-and-renewals.md), step 4.

## States

- Normal: licences with key, product and term.
- Empty: "No licence".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, expired: the key is disabled.
- Read-only: expired ones are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-04 Software licence](../../data/e-sc14-04-software-licence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-04 Software licence | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U41 | `u03-sales/s-sc14-04-licences-e-sc14-04-software-licence-active-{desktop,phone,tablet}-{light,dark}.png`, `u41-customer-success-manager/s-sc14-04-licences-e-sc14-04-software-licence-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-02 Licences and renewals](../../flows/fl-sc14-02-licences-and-renewals.md)

## Open questions

None.

---

⬅️ [S-SC14-03 Revenue](../01-subscriptions-and-billing/s-sc14-03-revenue.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-05 Support levels](../03-support-and-services/s-sc14-05-support-levels.md)
