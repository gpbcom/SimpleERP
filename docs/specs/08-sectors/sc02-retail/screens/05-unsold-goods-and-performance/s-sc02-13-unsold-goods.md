🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-05 Unsold goods and performance](README.md) ›
🖥️ S-SC02-13 Unsold goods

# 🖥️ S-SC02-13 Unsold goods

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to handle unsold goods
([UC-SC02-13](../../use-cases/05-unsold-goods-and-performance/uc-sc02-13-handle-unsold-goods.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-05 step 1, U23 | phone | ![FL-SC02-05 step 1, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/1-unsold-phone-light.png) | ![FL-SC02-05 step 1, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/1-unsold-phone-dark.png) |
| FL-SC02-05 step 1, U23 | desktop | ![FL-SC02-05 step 1, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/1-unsold-desktop-light.png) | ![FL-SC02-05 step 1, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/1-unsold-desktop-dark.png) |
| FL-SC02-05 step 1, U23 | tablet | ![FL-SC02-05 step 1, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/1-unsold-tablet-light.png) | ![FL-SC02-05 step 1, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/1-unsold-tablet-dark.png) |
| Error E1, U23 | phone | ![Error E1, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/e1-no-partner-phone-light.png) | ![Error E1, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/e1-no-partner-phone-dark.png) |
| Error E1, U23 | desktop | ![Error E1, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/e1-no-partner-desktop-light.png) | ![Error E1, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/e1-no-partner-desktop-dark.png) |
| Error E1, U23 | tablet | ![Error E1, U23, light](../../images/05-unsold-goods-and-performance/u23-store-manager/e1-no-partner-tablet-light.png) | ![Error E1, U23, dark](../../images/05-unsold-goods-and-performance/u23-store-manager/e1-no-partner-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-13-unsold-goods-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-13-unsold-goods-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-13-unsold-goods-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-13-unsold-goods-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-13-unsold-goods-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-13-unsold-goods-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-13-unsold-goods-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-13-unsold-goods-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-10 Unsold goods donation](../../data/e-sc02-10-unsold-goods-donation.md), shown as the entity
pages list them, with their examples.

## Actions

- List unsold goods: [UC-SC02-13](../../use-cases/05-unsold-goods-and-performance/uc-sc02-13-handle-unsold-goods.md),
  step 1.
- Choose the outlet: [UC-SC02-13](../../use-cases/05-unsold-goods-and-performance/uc-sc02-13-handle-unsold-goods.md),
  step 2.
- Hand over: [UC-SC02-13](../../use-cases/05-unsold-goods-and-performance/uc-sc02-13-handle-unsold-goods.md), step 3.
- Record the slip: [UC-SC02-13](../../use-cases/05-unsold-goods-and-performance/uc-sc02-13-handle-unsold-goods.md), step
  4.

## States

- Normal: unsold lines with quantity, value, outlet, partner and slip.
- Empty: "No unsold goods".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no partner set: the store manager is asked to set one.
- Read-only: a recorded donation is read-only.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC02-10 Unsold goods donation](../../data/e-sc02-10-unsold-goods-donation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-10 Unsold goods donation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15, U23 | `u15-warehouse-operator/s-sc02-13-unsold-goods-e-sc02-10-unsold-goods-donation-active-{phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-13-unsold-goods-e-sc02-10-unsold-goods-donation-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC02-12 Schedules](../04-customers-and-staff/s-sc02-12-schedules.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-14 Store performance](s-sc02-14-store-performance.md)
