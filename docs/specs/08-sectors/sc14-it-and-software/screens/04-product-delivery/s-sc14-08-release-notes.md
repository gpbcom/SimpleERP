🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-04 Product delivery](README.md) › 🖥️ S-SC14-08 Release notes

# 🖥️ S-SC14-08 Release notes

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)

## Purpose

Used to publish release notes to customers
([UC-SC14-08](../../use-cases/04-product-delivery/uc-sc14-08-publish-release-notes-to-customers.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-04 step 2, U16 | desktop | ![FL-SC14-04 step 2, U16, light](../../images/04-product-delivery/u16-office-worker/2-release-notes-desktop-light.png) | ![FL-SC14-04 step 2, U16, dark](../../images/04-product-delivery/u16-office-worker/2-release-notes-desktop-dark.png) |
| FL-SC14-04 step 2, U16 | phone | ![FL-SC14-04 step 2, U16, light](../../images/04-product-delivery/u16-office-worker/2-release-notes-phone-light.png) | ![FL-SC14-04 step 2, U16, dark](../../images/04-product-delivery/u16-office-worker/2-release-notes-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-08-release-notes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-08-release-notes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-08-release-notes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-08-release-notes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-08-release-notes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-08-release-notes-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-08-release-notes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-08-release-notes-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-08 Software release note](../../data/e-sc14-08-software-release-note.md), shown as the entity
pages list them, with their examples.

## Actions

- Draft: [UC-SC14-08](../../use-cases/04-product-delivery/uc-sc14-08-publish-release-notes-to-customers.md), step 1.
- Review: [UC-SC14-08](../../use-cases/04-product-delivery/uc-sc14-08-publish-release-notes-to-customers.md), step 2.
- Publish: [UC-SC14-08](../../use-cases/04-product-delivery/uc-sc14-08-publish-release-notes-to-customers.md), step 3.
- Tell requesters: [UC-SC14-08](../../use-cases/04-product-delivery/uc-sc14-08-publish-release-notes-to-customers.md),
  step 4.

## States

- Normal: release notes with features and state.
- Empty: "No release note".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a feature not done: it is left out.
- Read-only: published ones are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-08 Software release note](../../data/e-sc14-08-software-release-note.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-08 Software release note | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U16, U41 | `u16-office-worker/s-sc14-08-release-notes-e-sc14-08-software-release-note-recorded-{desktop,phone}-{light,dark}.png`, `u41-customer-success-manager/s-sc14-08-release-notes-e-sc14-08-software-release-note-recorded-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC14-07 Sprints](s-sc14-07-sprints.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-09 Health](../02-licences-and-renewals/s-sc14-09-health.md)
