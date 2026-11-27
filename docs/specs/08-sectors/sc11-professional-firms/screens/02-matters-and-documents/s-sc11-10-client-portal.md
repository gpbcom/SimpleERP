🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-02 Matters and documents](README.md) › 🖥️ S-SC11-10 Client portal

# 🖥️ S-SC11-10 Client portal

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to exchange securely with the client in the portal,
[UC-SC11-10](../../use-cases/02-matters-and-documents/uc-sc11-10-exchange-securely-with-the-client-in-the-portal.md).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-02 step 3, U09 | phone | ![FL-SC11-02 step 3, U09, light](../../images/02-matters-and-documents/u09-customer/3-portal-phone-light.png) | ![FL-SC11-02 step 3, U09, dark](../../images/02-matters-and-documents/u09-customer/3-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc11-10-client-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc11-10-client-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc11-10-client-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc11-10-client-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc11-10-client-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc11-10-client-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-10-client-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-10-client-portal-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-10 Matter document](../../data/e-sc11-10-matter-document.md), shown as the entity pages list them,
with their examples.

## Actions

- Share:
  [UC-SC11-10](../../use-cases/02-matters-and-documents/uc-sc11-10-exchange-securely-with-the-client-in-the-portal.md),
  step 1.
- Read:
  [UC-SC11-10](../../use-cases/02-matters-and-documents/uc-sc11-10-exchange-securely-with-the-client-in-the-portal.md),
  step 2.
- Reply:
  [UC-SC11-10](../../use-cases/02-matters-and-documents/uc-sc11-10-exchange-securely-with-the-client-in-the-portal.md),
  step 3.
- Meet by video:
  [UC-SC11-10](../../use-cases/02-matters-and-documents/uc-sc11-10-exchange-securely-with-the-client-in-the-portal.md),
  step 4.

## States

- Normal: shared items, messages, bills and meetings with the client.
- Empty: "Nothing shared".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a walled matter: only its team can share.
- Read-only: the client reads their own matters.
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

- [FL-SC11-02 Matters and documents](../../flows/fl-sc11-02-matters-and-documents.md)

## Open questions

None.

---

⬅️ [S-SC11-09 Documents](s-sc11-09-documents.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-11 Client portfolio](../04-deadlines-and-filings/s-sc11-11-client-portfolio.md)
