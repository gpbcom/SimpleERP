🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-06 Logistics for clients](README.md) › 🖥️ S-SC07-16 Client portal

# 🖥️ S-SC07-16 Client portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Used to give clients tracking and documents in the portal,
[UC-SC07-16](../../use-cases/06-logistics-for-clients/uc-sc07-16-give-clients-tracking-and-documents-in-the-portal.md).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-06 step 3, U09 | phone | ![FL-SC07-06 step 3, U09, light](../../images/06-logistics-for-clients/u09-customer/3-portal-phone-light.png) | ![FL-SC07-06 step 3, U09, dark](../../images/06-logistics-for-clients/u09-customer/3-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc07-16-client-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc07-16-client-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc07-16-client-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc07-16-client-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc07-16-client-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc07-16-client-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-16-client-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-16-client-portal-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-06 Stop](../../data/e-sc07-06-stop.md),
[E-SC07-05 Consignment note](../../data/e-sc07-05-consignment-note.md), shown as the entity pages list them, with their
examples.

## Actions

- Sign in:
  [UC-SC07-16](../../use-cases/06-logistics-for-clients/uc-sc07-16-give-clients-tracking-and-documents-in-the-portal.md),
  step 1.
- Follow shipments:
  [UC-SC07-16](../../use-cases/06-logistics-for-clients/uc-sc07-16-give-clients-tracking-and-documents-in-the-portal.md),
  step 2.
- Download proofs:
  [UC-SC07-16](../../use-cases/06-logistics-for-clients/uc-sc07-16-give-clients-tracking-and-documents-in-the-portal.md),
  step 3.
- Answer a question:
  [UC-SC07-16](../../use-cases/06-logistics-for-clients/uc-sc07-16-give-clients-tracking-and-documents-in-the-portal.md),
  step 4.

## States

- Normal: the client's shipments with status, ETA, proofs and invoices.
- Empty: "No shipment".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, another client's shipment: it is never shown,
  [BR-F6-03](../../../../02-functional/f06-customers-and-sales/business-rules/br-f06-03-portal-shows-only-the-customer-s-own.md).
- Read-only: the client reads only their own.
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

- [FL-SC07-06 Logistics for clients](../../flows/fl-sc07-06-logistics-for-clients.md)

## Open questions

None.

---

⬅️ [S-SC07-15 Storage billing](s-sc07-15-storage-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-17 CO2 information](../05-billing-and-performance/s-sc07-17-co2-information.md)
