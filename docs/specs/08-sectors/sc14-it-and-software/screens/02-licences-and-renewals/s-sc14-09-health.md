🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-02 Licences and renewals](README.md) › 🖥️ S-SC14-09 Health

# 🖥️ S-SC14-09 Health

**Status:** 🔄 waiting for the owner

## Personas

- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)

## Purpose

Used to follow customer health and churn risk,
[UC-SC14-09](../../use-cases/02-licences-and-renewals/uc-sc14-09-follow-customer-health-and-churn-risk.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-02 step 2, U41 | desktop | ![FL-SC14-02 step 2, U41, light](../../images/02-licences-and-renewals/u41-customer-success-manager/2-health-desktop-light.png) | ![FL-SC14-02 step 2, U41, dark](../../images/02-licences-and-renewals/u41-customer-success-manager/2-health-desktop-dark.png) |
| FL-SC14-02 step 2, U41 | phone | ![FL-SC14-02 step 2, U41, light](../../images/02-licences-and-renewals/u41-customer-success-manager/2-health-phone-light.png) | ![FL-SC14-02 step 2, U41, dark](../../images/02-licences-and-renewals/u41-customer-success-manager/2-health-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-09-health-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-09-health-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-09-health-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-09-health-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-09-health-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-09-health-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-09-health-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-09-health-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-09 Health score](../../data/e-sc14-09-health-score.md), shown as the entity pages list them, with
their examples.

## Actions

- Review scores:
  [UC-SC14-09](../../use-cases/02-licences-and-renewals/uc-sc14-09-follow-customer-health-and-churn-risk.md), step 1.
- Act on risks:
  [UC-SC14-09](../../use-cases/02-licences-and-renewals/uc-sc14-09-follow-customer-health-and-churn-risk.md), step 2.
- Record outcomes:
  [UC-SC14-09](../../use-cases/02-licences-and-renewals/uc-sc14-09-follow-customer-health-and-churn-risk.md), step 3.
- Follow: [UC-SC14-09](../../use-cases/02-licences-and-renewals/uc-sc14-09-follow-customer-health-and-churn-risk.md),
  step 4.

## States

- Normal: customers with score and factors.
- Empty: "No score yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a score drop: the manager is alerted.
- Read-only: sales read only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-09 Health score](../../data/e-sc14-09-health-score.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-09 Health score | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U41 | `u41-customer-success-manager/s-sc14-09-health-e-sc14-09-health-score-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-02 Licences and renewals](../../flows/fl-sc14-02-licences-and-renewals.md)

## Open questions

None.

---

⬅️ [S-SC14-08 Release notes](../04-product-delivery/s-sc14-08-release-notes.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-10 Renewals](s-sc14-10-renewals.md)
