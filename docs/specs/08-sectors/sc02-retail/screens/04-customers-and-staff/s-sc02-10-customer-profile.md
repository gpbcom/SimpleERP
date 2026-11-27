🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-04 Customers and staff](README.md) › 🖥️ S-SC02-10 Customer profile

# 🖥️ S-SC02-10 Customer profile

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to know the customer ([UC-SC02-10](../../use-cases/04-customers-and-staff/uc-sc02-10-know-the-customer.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-04 step 1, U17 | desktop | ![FL-SC02-04 step 1, U17, light](../../images/04-customers-and-staff/u17-cashier/1-customer-profile-desktop-light.png) | ![FL-SC02-04 step 1, U17, dark](../../images/04-customers-and-staff/u17-cashier/1-customer-profile-desktop-dark.png) |
| FL-SC02-04 step 1, U17 | phone | ![FL-SC02-04 step 1, U17, light](../../images/04-customers-and-staff/u17-cashier/1-customer-profile-phone-light.png) | ![FL-SC02-04 step 1, U17, dark](../../images/04-customers-and-staff/u17-cashier/1-customer-profile-phone-dark.png) |
| FL-SC02-04 step 1, U17 | tablet | ![FL-SC02-04 step 1, U17, light](../../images/04-customers-and-staff/u17-cashier/1-customer-profile-tablet-light.png) | ![FL-SC02-04 step 1, U17, dark](../../images/04-customers-and-staff/u17-cashier/1-customer-profile-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-10-customer-profile-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-10-customer-profile-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-10-customer-profile-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-10-customer-profile-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-10-customer-profile-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-10-customer-profile-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-10-customer-profile-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-10-customer-profile-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-11 Customer profile](../../data/e-sc02-11-customer-profile.md), shown as the entity pages list
them, with their examples.

## Actions

- Find the customer: [UC-SC02-10](../../use-cases/04-customers-and-staff/uc-sc02-10-know-the-customer.md), step 1.
- See history and preferences: [UC-SC02-10](../../use-cases/04-customers-and-staff/uc-sc02-10-know-the-customer.md),
  step 2.
- Suggest: [UC-SC02-10](../../use-cases/04-customers-and-staff/uc-sc02-10-know-the-customer.md), step 3.
- Update preferences: [UC-SC02-10](../../use-cases/04-customers-and-staff/uc-sc02-10-know-the-customer.md), step 4.

## States

- Normal: the customer's purchases, and with consent sizes, preferences and suggested items.
- Empty: "No purchase yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no consent: only the purchase history shows, not sizes or
  preferences.
- Read-only: without consent, only the history.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
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

- [FL-SC02-04 Customers and staff](../../flows/fl-sc02-04-customers-and-staff.md)

## Open questions

None.

---

⬅️ [S-SC02-09 Returns](../03-sell-and-return-across-channels/s-sc02-09-returns.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-11 Targets](s-sc02-11-targets.md)
