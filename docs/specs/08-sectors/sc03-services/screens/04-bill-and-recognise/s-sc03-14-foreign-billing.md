🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-04 Bill and recognise](README.md) › 🖥️ S-SC03-14 Foreign billing

# 🖥️ S-SC03-14 Foreign billing

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)

## Purpose

Used to bill foreign clients ([UC-SC03-14](../../use-cases/04-bill-and-recognise/uc-sc03-14-bill-foreign-clients.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-04 step 5, U05 | desktop | ![FL-SC03-04 step 5, U05, light](../../images/04-bill-and-recognise/u05-accounting/5-margin-desktop-light.png) | ![FL-SC03-04 step 5, U05, dark](../../images/04-bill-and-recognise/u05-accounting/5-margin-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-14-foreign-billing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-14-foreign-billing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-14-foreign-billing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-14-foreign-billing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-14-foreign-billing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-14-foreign-billing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc03-14-foreign-billing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc03-14-foreign-billing-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC03-07 Billing proposal](../../data/e-sc03-07-billing-proposal.md), shown as the entity pages list
them, with their examples.

## Actions

- Check the VAT number: [UC-SC03-14](../../use-cases/04-bill-and-recognise/uc-sc03-14-bill-foreign-clients.md), step 1.
- Bill in its currency: [UC-SC03-14](../../use-cases/04-bill-and-recognise/uc-sc03-14-bill-foreign-clients.md), step 2.
- Declare: [UC-SC03-14](../../use-cases/04-bill-and-recognise/uc-sc03-14-bill-foreign-clients.md), step 3.
- Match the payment: [UC-SC03-14](../../use-cases/04-bill-and-recognise/uc-sc03-14-bill-foreign-clients.md), step 4.

## States

- Normal: the client's VAT number check, currency, mentions and the European statement lines.
- Empty: "No foreign client".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the VAT number is invalid: French VAT is applied until a valid
  number is given.
- Read-only: a sent bill is read-only.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
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

- [FL-SC03-04 Bill and recognise](../../flows/fl-sc03-04-bill-and-recognise.md)

## Open questions

None.

---

⬅️ [S-SC03-13 Skills](../05-client-and-people/s-sc03-13-skills.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-15 Engagement assistant](../03-deliver-and-record/s-sc03-15-engagement-assistant.md)
