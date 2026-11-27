🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-05 Unsold goods and performance](README.md) ›
🖥️ S-SC02-15 Store assistant

# 🖥️ S-SC02-15 Store assistant

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)

## Purpose

Used to ask the AI assistant about a store,
[UC-SC02-15](../../use-cases/05-unsold-goods-and-performance/uc-sc02-15-ask-the-assistant-about-a-store.md).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-05 step 3, U23 | phone | ![FL-SC02-05 step 3, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/3-assistant-phone-light.png) | ![FL-SC02-05 step 3, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/3-assistant-phone-dark.png) |
| FL-SC02-05 step 3, U23 | desktop | ![FL-SC02-05 step 3, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/3-assistant-desktop-light.png) | ![FL-SC02-05 step 3, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/3-assistant-desktop-dark.png) |
| FL-SC02-05 step 3, U23 | tablet | ![FL-SC02-05 step 3, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/3-assistant-tablet-light.png) | ![FL-SC02-05 step 3, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/3-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-15-store-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-15-store-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-15-store-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-15-store-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-15-store-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-15-store-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-15-store-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-15-store-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-01 Store](../../data/e-sc02-01-store.md),
[E-SC02-06 Store transfer](../../data/e-sc02-06-store-transfer.md), shown as the entity pages list them, with their
examples.

## Actions

- Ask for a size:
  [UC-SC02-15](../../use-cases/05-unsold-goods-and-performance/uc-sc02-15-ask-the-assistant-about-a-store.md), step 1.
- Confirm a transfer:
  [UC-SC02-15](../../use-cases/05-unsold-goods-and-performance/uc-sc02-15-ask-the-assistant-about-a-store.md), step 4.

## States

- Normal: the conversation with answers, links and prepared actions to confirm.
- Empty: suggested questions about the store.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses and
  says which role can do it.
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

- [FL-SC02-05 Unsold goods and performance](../../flows/fl-sc02-05-unsold-goods-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC02-14 Store performance](s-sc02-14-store-performance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-16 Book trade](../06-books-furniture-second-hand-franchise/s-sc02-16-book-trade.md)
