🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-02 Licences and renewals](README.md) › 🖥️ S-SC14-10 Renewals

# 🖥️ S-SC14-10 Renewals

**Status:** ✅ specified

## Personas

- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to run renewals and expansion
([UC-SC14-10](../../use-cases/02-licences-and-renewals/uc-sc14-10-run-renewals-and-expansion.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-02 step 3, U41 | desktop | ![FL-SC14-02 step 3, U41, light](../../images/02-licences-and-renewals/u41-customer-success-manager/3-renewal-desktop-light.png) | ![FL-SC14-02 step 3, U41, dark](../../images/02-licences-and-renewals/u41-customer-success-manager/3-renewal-desktop-dark.png) |
| FL-SC14-02 step 3, U41 | phone | ![FL-SC14-02 step 3, U41, light](../../images/02-licences-and-renewals/u41-customer-success-manager/3-renewal-phone-light.png) | ![FL-SC14-02 step 3, U41, dark](../../images/02-licences-and-renewals/u41-customer-success-manager/3-renewal-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-10-renewals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-10-renewals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-10-renewals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-10-renewals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-10-renewals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-10-renewals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-10-renewals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-10-renewals-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-01 Software subscription](../../data/e-sc14-01-software-subscription.md),
[E-SC14-09 Health score](../../data/e-sc14-09-health-score.md), shown as the entity pages list them, with their
examples.

## Actions

- Open the renewal: [UC-SC14-10](../../use-cases/02-licences-and-renewals/uc-sc14-10-run-renewals-and-expansion.md),
  step 1.
- Quote: [UC-SC14-10](../../use-cases/02-licences-and-renewals/uc-sc14-10-run-renewals-and-expansion.md), step 2.
- Accept: [UC-SC14-10](../../use-cases/02-licences-and-renewals/uc-sc14-10-run-renewals-and-expansion.md), step 3.
- Close: [UC-SC14-10](../../use-cases/02-licences-and-renewals/uc-sc14-10-run-renewals-and-expansion.md), step 4.

## States

- Normal: renewals with quote, state and churn reason.
- Empty: "No renewal due".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, not renewed: churn is recorded with its reason.
- Read-only: closed ones are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-SC14-09 Health](s-sc14-09-health.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-11 Processor agreements](../05-security-and-data-compliance/s-sc14-11-processor-agreements.md)
