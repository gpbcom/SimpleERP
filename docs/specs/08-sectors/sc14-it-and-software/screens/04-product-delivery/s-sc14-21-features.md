🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-04 Product delivery](README.md) › 🖥️ S-SC14-21 Features

# 🖥️ S-SC14-21 Features

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)

## Purpose

Used to follow features and products in the development tool,
[UC-SC14-21](../../use-cases/04-product-delivery/uc-sc14-21-follow-features-and-products-in-the-development-tool.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-04 step 3, U16 | desktop | ![FL-SC14-04 step 3, U16, light](../../images/04-product-delivery/u16-office-worker/3-features-desktop-light.png) | ![FL-SC14-04 step 3, U16, dark](../../images/04-product-delivery/u16-office-worker/3-features-desktop-dark.png) |
| FL-SC14-04 step 3, U16 | phone | ![FL-SC14-04 step 3, U16, light](../../images/04-product-delivery/u16-office-worker/3-features-phone-light.png) | ![FL-SC14-04 step 3, U16, dark](../../images/04-product-delivery/u16-office-worker/3-features-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-21-features-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-21-features-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-21-features-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-21-features-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-21-features-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-21-features-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-21-features-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-21-features-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-16 Tracked feature](../../data/e-sc14-16-tracked-feature.md),
[E-SC14-08 Software release note](../../data/e-sc14-08-software-release-note.md), shown as the entity pages list them,
with their examples.

## Actions

- Connect the tool:
  [UC-SC14-21](../../use-cases/04-product-delivery/uc-sc14-21-follow-features-and-products-in-the-development-tool.md),
  step 1.
- Link features:
  [UC-SC14-21](../../use-cases/04-product-delivery/uc-sc14-21-follow-features-and-products-in-the-development-tool.md),
  step 2.
- Follow progress:
  [UC-SC14-21](../../use-cases/04-product-delivery/uc-sc14-21-follow-features-and-products-in-the-development-tool.md),
  step 3.
- Tell on release:
  [UC-SC14-21](../../use-cases/04-product-delivery/uc-sc14-21-follow-features-and-products-in-the-development-tool.md),
  step 4.

## States

- Normal: features with tool, key, state and linked requests.
- Empty: "No tool connected".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the connector down: it is shown and the last sync kept.
- Read-only: synced fields are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-08 Software release note](../../data/e-sc14-08-software-release-note.md),
[E-SC14-16 Tracked feature](../../data/e-sc14-16-tracked-feature.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-08 Software release note | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U16, U41 | `u16-office-worker/s-sc14-21-features-e-sc14-08-software-release-note-recorded-{desktop,phone}-{light,dark}.png`, `u41-customer-success-manager/s-sc14-21-features-e-sc14-08-software-release-note-recorded-{desktop,phone}-{light,dark}.png` |
| E-SC14-16 Tracked feature | In progress | Badge "In progress"; a new record starts here; no other state; fields editable within the role | U16, U41 | `u16-office-worker/s-sc14-21-features-e-sc14-16-tracked-feature-in-progress-{desktop,phone}-{light,dark}.png`, `u41-customer-success-manager/s-sc14-21-features-e-sc14-16-tracked-feature-in-progress-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-04 Product delivery](../../flows/fl-sc14-04-product-delivery.md)

## Open questions

None.

---

⬅️ [S-SC14-20 Software assistant](../06-portal-and-metrics/s-sc14-20-software-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-22 Hardware leasing](../07-hardware-licences-and-tax-credits/s-sc14-22-hardware-leasing.md)
