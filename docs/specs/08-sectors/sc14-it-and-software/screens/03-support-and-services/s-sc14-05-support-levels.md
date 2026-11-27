🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-03 Support and services](README.md) › 🖥️ S-SC14-05 Support levels

# 🖥️ S-SC14-05 Support levels

**Status:** 🔄 waiting for the owner

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)

## Purpose

Used to run support with service levels
([UC-SC14-05](../../use-cases/03-support-and-services/uc-sc14-05-run-support-with-service-levels.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-03 step 1, U09 | phone | ![FL-SC14-03 step 1, U09, light](../../images/03-support-and-services/u09-customer/1-service-levels-phone-light.png) | ![FL-SC14-03 step 1, U09, dark](../../images/03-support-and-services/u09-customer/1-service-levels-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc14-05-support-levels-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc14-05-support-levels-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc14-05-support-levels-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc14-05-support-levels-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc14-05-support-levels-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc14-05-support-levels-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-05-support-levels-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-05-support-levels-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-05 Service level](../../data/e-sc14-05-service-level.md), shown as the entity pages list them,
with their examples.

## Actions

- Open: [UC-SC14-05](../../use-cases/03-support-and-services/uc-sc14-05-run-support-with-service-levels.md), step 1.
- Answer: [UC-SC14-05](../../use-cases/03-support-and-services/uc-sc14-05-run-support-with-service-levels.md), step 2.
- Resolve: [UC-SC14-05](../../use-cases/03-support-and-services/uc-sc14-05-run-support-with-service-levels.md), step 3.
- Link: [UC-SC14-05](../../use-cases/03-support-and-services/uc-sc14-05-run-support-with-service-levels.md), step 4.

## States

- Normal: tickets with priority, times against the level and credits.
- Empty: "No ticket".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a breach: a credit is proposed.
- Read-only: customers read their own.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-05 Service level](../../data/e-sc14-05-service-level.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-05 Service level | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U41 | `u09-customer/s-sc14-05-support-levels-e-sc14-05-service-level-active-phone-{light,dark}.png`, `u41-customer-success-manager/s-sc14-05-support-levels-e-sc14-05-service-level-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-03 Support and services](../../flows/fl-sc14-03-support-and-services.md)

## Open questions

None.

---

⬅️ [S-SC14-04 Licences](../02-licences-and-renewals/s-sc14-04-licences.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-06 Managed services](s-sc14-06-managed-services.md)
