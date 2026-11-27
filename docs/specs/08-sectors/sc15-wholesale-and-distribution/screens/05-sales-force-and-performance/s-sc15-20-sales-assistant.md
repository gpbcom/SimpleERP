🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-05 Sales force and performance](README.md) › 🖥️ S-SC15-20 Sales assistant

# 🖥️ S-SC15-20 Sales assistant

**Status:** ✅ specified

## Personas

- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to ask the AI assistant
([UC-SC15-20](../../use-cases/05-sales-force-and-performance/uc-sc15-20-ask-the-assistant.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-05 step 4, U42 | phone | ![FL-SC15-05 step 4, U42, light](../../images/05-sales-force-and-performance/u42-sales-representative/4-assistant-phone-light.png) | ![FL-SC15-05 step 4, U42, dark](../../images/05-sales-force-and-performance/u42-sales-representative/4-assistant-phone-dark.png) |
| FL-SC15-05 step 4, U42 | desktop | ![FL-SC15-05 step 4, U42, light](../../images/05-sales-force-and-performance/u42-sales-representative/4-assistant-desktop-light.png) | ![FL-SC15-05 step 4, U42, dark](../../images/05-sales-force-and-performance/u42-sales-representative/4-assistant-desktop-dark.png) |
| FL-SC15-05 step 4, U42 | tablet | ![FL-SC15-05 step 4, U42, light](../../images/05-sales-force-and-performance/u42-sales-representative/4-assistant-tablet-light.png) | ![FL-SC15-05 step 4, U42, dark](../../images/05-sales-force-and-performance/u42-sales-representative/4-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-20-sales-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-20-sales-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-20-sales-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-20-sales-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-20-sales-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-20-sales-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-20-sales-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-20-sales-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-01 Price agreement](../../data/e-sc15-01-price-agreement.md),
[E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md), shown as the entity pages list them, with their examples.

## Actions

- Ask: [UC-SC15-20](../../use-cases/05-sales-force-and-performance/uc-sc15-20-ask-the-assistant.md), step 1.
- Confirm a draft: [UC-SC15-20](../../use-cases/05-sales-force-and-performance/uc-sc15-20-ask-the-assistant.md), step 4.

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

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC15-05 Sales force and performance](../../flows/fl-sc15-05-sales-force-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC15-19 Supplier performance](../04-import-and-suppliers/s-sc15-19-supplier-performance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-21 Beverage distribution](../06-beverages-vans-weights-and-devices/s-sc15-21-beverage-distribution.md)
