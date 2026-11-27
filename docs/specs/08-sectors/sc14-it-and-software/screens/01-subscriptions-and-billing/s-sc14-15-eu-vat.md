🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-01 Subscriptions and billing](README.md) › 🖥️ S-SC14-15 EU VAT

# 🖥️ S-SC14-15 EU VAT

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to bill digital services across the EU,
[UC-SC14-15](../../use-cases/01-subscriptions-and-billing/uc-sc14-15-bill-digital-services-across-the-eu.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-01 step 4, U05 | desktop | ![FL-SC14-01 step 4, U05, light](../../images/01-subscriptions-and-billing/u05-accounting/4-eu-vat-desktop-light.png) | ![FL-SC14-01 step 4, U05, dark](../../images/01-subscriptions-and-billing/u05-accounting/4-eu-vat-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-15-eu-vat-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-15-eu-vat-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-15-eu-vat-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-15-eu-vat-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-15-eu-vat-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-15-eu-vat-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc14-15-eu-vat-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc14-15-eu-vat-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC14-02 Customer usage record](../../data/e-sc14-02-customer-usage-record.md), shown as the entity
pages list them, with their examples.

## Actions

- Check the customer:
  [UC-SC14-15](../../use-cases/01-subscriptions-and-billing/uc-sc14-15-bill-digital-services-across-the-eu.md), step 1.
- Apply the VAT:
  [UC-SC14-15](../../use-cases/01-subscriptions-and-billing/uc-sc14-15-bill-digital-services-across-the-eu.md), step 2.
- Bill: [UC-SC14-15](../../use-cases/01-subscriptions-and-billing/uc-sc14-15-bill-digital-services-across-the-eu.md),
  step 3.
- Declare: [UC-SC14-15](../../use-cases/01-subscriptions-and-billing/uc-sc14-15-bill-digital-services-across-the-eu.md),
  step 4.

## States

- Normal: invoices with country, status, VAT and declaration.
- Empty: "No EU invoice".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the country unknown: it is asked.
- Read-only: declared ones are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC14-01 Subscriptions and billing](../../flows/fl-sc14-01-subscriptions-and-billing.md)

## Open questions

None.

---

⬅️ [S-SC14-14 Data export](../05-security-and-data-compliance/s-sc14-14-data-export.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-16 Dunning](s-sc14-16-dunning.md)
