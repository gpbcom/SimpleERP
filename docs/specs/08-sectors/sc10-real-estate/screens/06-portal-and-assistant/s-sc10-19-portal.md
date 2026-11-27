🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-06 Portal and assistant](README.md) › 🖥️ S-SC10-19 Portal

# 🖥️ S-SC10-19 Portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to give landlords, tenants and co-owners their portal,
[UC-SC10-19](../../use-cases/06-portal-and-assistant/uc-sc10-19-give-landlords-tenants-and-co-owners-their-portal.md).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-06 step 1, U09 | phone | ![FL-SC10-06 step 1, U09, light](../../images/06-portal-and-assistant/u09-customer/1-portal-phone-light.png) | ![FL-SC10-06 step 1, U09, dark](../../images/06-portal-and-assistant/u09-customer/1-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc10-19-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc10-19-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc10-19-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc10-19-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc10-19-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc10-19-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc10-19-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc10-19-portal-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC10-09 Rent call](../../data/e-sc10-09-rent-call.md),
[E-SC10-11 Landlord statement](../../data/e-sc10-11-landlord-statement.md),
[E-SC10-16 Co-ownership](../../data/e-sc10-16-co-ownership.md), shown as the entity pages list them, with their
examples.

## Actions

- Sign in:
  [UC-SC10-19](../../use-cases/06-portal-and-assistant/uc-sc10-19-give-landlords-tenants-and-co-owners-their-portal.md),
  step 1.
- See documents and balances:
  [UC-SC10-19](../../use-cases/06-portal-and-assistant/uc-sc10-19-give-landlords-tenants-and-co-owners-their-portal.md),
  step 2.
- Pay:
  [UC-SC10-19](../../use-cases/06-portal-and-assistant/uc-sc10-19-give-landlords-tenants-and-co-owners-their-portal.md),
  step 3.
- Ask:
  [UC-SC10-19](../../use-cases/06-portal-and-assistant/uc-sc10-19-give-landlords-tenants-and-co-owners-their-portal.md),
  step 4.

## States

- Normal: the client's documents, balances, payments and requests.
- Empty: "No document yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, another's data: it is never shown.
- Read-only: clients read their own records.
- Offline: not available offline: a portal page for clients.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC10-06 Portal and assistant](../../flows/fl-sc10-06-portal-and-assistant.md)

## Open questions

None.

---

⬅️ [S-SC10-18 Co-ownership accounts](../05-co-ownership/s-sc10-18-co-ownership-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-20 Portfolio assistant](s-sc10-20-portfolio-assistant.md)
