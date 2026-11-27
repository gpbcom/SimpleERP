🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-06 Portal and metrics](README.md) › 🖥️ S-SC14-17 Customer portal

# 🖥️ S-SC14-17 Customer portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to give customers their portal
([UC-SC14-17](../../use-cases/06-portal-and-metrics/uc-sc14-17-give-customers-their-portal.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-06 step 1, U09 | phone | ![FL-SC14-06 step 1, U09, light](../../images/06-portal-and-metrics/u09-customer/1-portal-phone-light.png) | ![FL-SC14-06 step 1, U09, dark](../../images/06-portal-and-metrics/u09-customer/1-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc14-17-customer-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc14-17-customer-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc14-17-customer-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc14-17-customer-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc14-17-customer-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc14-17-customer-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-17-customer-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-17-customer-portal-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-01 Software subscription](../../data/e-sc14-01-software-subscription.md),
[E-SC14-02 Customer usage record](../../data/e-sc14-02-customer-usage-record.md), shown as the entity pages list them,
with their examples.

## Actions

- Sign in: [UC-SC14-17](../../use-cases/06-portal-and-metrics/uc-sc14-17-give-customers-their-portal.md), step 1.
- See: [UC-SC14-17](../../use-cases/06-portal-and-metrics/uc-sc14-17-give-customers-their-portal.md), step 2.
- Change: [UC-SC14-17](../../use-cases/06-portal-and-metrics/uc-sc14-17-give-customers-their-portal.md), step 3.
- Pay or ask: [UC-SC14-17](../../use-cases/06-portal-and-metrics/uc-sc14-17-give-customers-their-portal.md), step 4.

## States

- Normal: the customer's subscriptions, invoices, usage, tickets and exports.
- Empty: "No subscription".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, another company's data: it is never shown,
  [BR-F6-03](../../../../02-functional/f06-customers-and-sales/business-rules/br-f06-03-portal-shows-only-the-customer-s-own.md).
- Read-only: users see less than admins.
- Offline: not available offline: a portal page for customers.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC14-06 Portal and metrics](../../flows/fl-sc14-06-portal-and-metrics.md)

## Open questions

None.

---

⬅️ [S-SC14-16 Dunning](../01-subscriptions-and-billing/s-sc14-16-dunning.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-18 SaaS metrics](s-sc14-18-saas-metrics.md)
