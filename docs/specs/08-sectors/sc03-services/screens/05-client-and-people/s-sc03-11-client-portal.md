🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-05 Client and people](README.md) › 🖥️ S-SC03-11 Client portal

# 🖥️ S-SC03-11 Client portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to share with the client in the portal
([UC-SC03-11](../../use-cases/05-client-and-people/uc-sc03-11-share-with-the-client-in-the-portal.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-05 step 1, U09 | phone | ![FL-SC03-05 step 1, U09, light](../../images/05-client-and-people/u09-customer/1-portal-phone-light.png) | ![FL-SC03-05 step 1, U09, dark](../../images/05-client-and-people/u09-customer/1-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc03-11-client-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc03-11-client-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc03-11-client-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc03-11-client-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc03-11-client-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc03-11-client-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-11-client-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-11-client-portal-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-12 Shared item](../../data/e-sc03-12-shared-item.md), shown as the entity pages list them, with
their examples.

## Actions

- Share a report: [UC-SC03-11](../../use-cases/05-client-and-people/uc-sc03-11-share-with-the-client-in-the-portal.md),
  step 1.
- Approve: [UC-SC03-11](../../use-cases/05-client-and-people/uc-sc03-11-share-with-the-client-in-the-portal.md), step 2.
- Record: [UC-SC03-11](../../use-cases/05-client-and-people/uc-sc03-11-share-with-the-client-in-the-portal.md), step 3.
- Approve the timesheet:
  [UC-SC03-11](../../use-cases/05-client-and-people/uc-sc03-11-share-with-the-client-in-the-portal.md), step 4.

## States

- Normal: the shared items with their approval state and comments.
- Empty: "Nothing shared yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a client trying another engagement: it is not shown,
  [BR-SC03-12](../../business-rules/br-sc03-12-client-sees-only-their-engagements.md),
  [BR-F6-03](../../../../02-functional/f06-customers-and-sales/business-rules/br-f06-03-portal-shows-only-the-customer-s-own.md).
- Read-only: the client reads only their own engagements.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
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

- [FL-SC03-05 Client and people](../../flows/fl-sc03-05-client-and-people.md)

## Open questions

None.

---

⬅️ [S-SC03-10 Engagement margin](../04-bill-and-recognise/s-sc03-10-engagement-margin.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-12 Satisfaction](s-sc03-12-satisfaction.md)
