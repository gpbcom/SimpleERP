🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-06 Portal and metrics](README.md) › 🖥️ S-SC14-20 Software assistant

# 🖥️ S-SC14-20 Software assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Used to ask the AI assistant ([UC-SC14-20](../../use-cases/06-portal-and-metrics/uc-sc14-20-ask-the-assistant.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-06 step 3, U41 | desktop | ![FL-SC14-06 step 3, U41, light](../../images/06-portal-and-metrics/u41-customer-success-manager/3-assistant-desktop-light.png) | ![FL-SC14-06 step 3, U41, dark](../../images/06-portal-and-metrics/u41-customer-success-manager/3-assistant-desktop-dark.png) |
| FL-SC14-06 step 3, U41 | phone | ![FL-SC14-06 step 3, U41, light](../../images/06-portal-and-metrics/u41-customer-success-manager/3-assistant-phone-light.png) | ![FL-SC14-06 step 3, U41, dark](../../images/06-portal-and-metrics/u41-customer-success-manager/3-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-20-software-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-20-software-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-20-software-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-20-software-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-20-software-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-20-software-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-20-software-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-20-software-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-09 Health score](../../data/e-sc14-09-health-score.md),
[E-SC14-16 Tracked feature](../../data/e-sc14-16-tracked-feature.md), shown as the entity pages list them, with their
examples.

## Actions

- Ask: [UC-SC14-20](../../use-cases/06-portal-and-metrics/uc-sc14-20-ask-the-assistant.md), step 1.
- Confirm a draft: [UC-SC14-20](../../use-cases/06-portal-and-metrics/uc-sc14-20-ask-the-assistant.md), step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC14-19 Partners](../02-licences-and-renewals/s-sc14-19-partners.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-21 Features](../04-product-delivery/s-sc14-21-features.md)
