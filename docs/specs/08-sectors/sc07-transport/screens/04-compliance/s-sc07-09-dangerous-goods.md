🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-04 Compliance](README.md) › 🖥️ S-SC07-09 Dangerous goods

# 🖥️ S-SC07-09 Dangerous goods

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)
- [U30 Driver](../../../../01-users/personas/u30-driver.md)

## Purpose

Used to handle dangerous goods ([UC-SC07-09](../../use-cases/04-compliance/uc-sc07-09-handle-dangerous-goods.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-04 step 2, U29 | desktop | ![FL-SC07-04 step 2, U29, light](../../images/04-compliance/u29-dispatcher/2-dangerous-goods-desktop-light.png) | ![FL-SC07-04 step 2, U29, dark](../../images/04-compliance/u29-dispatcher/2-dangerous-goods-desktop-dark.png) |
| FL-SC07-04 step 2, U29 | phone | ![FL-SC07-04 step 2, U29, light](../../images/04-compliance/u29-dispatcher/2-dangerous-goods-phone-light.png) | ![FL-SC07-04 step 2, U29, dark](../../images/04-compliance/u29-dispatcher/2-dangerous-goods-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-09-dangerous-goods-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-09-dangerous-goods-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-09-dangerous-goods-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-09-dangerous-goods-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-09-dangerous-goods-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-09-dangerous-goods-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-09-dangerous-goods-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-09-dangerous-goods-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-09 Dangerous goods declaration](../../data/e-sc07-09-dangerous-goods-declaration.md), shown as the
entity pages list them, with their examples.

## Actions

- Mark the load: [UC-SC07-09](../../use-cases/04-compliance/uc-sc07-09-handle-dangerous-goods.md), step 1.
- Check driver and vehicle: [UC-SC07-09](../../use-cases/04-compliance/uc-sc07-09-handle-dangerous-goods.md), step 2.
- Issue documents: [UC-SC07-09](../../use-cases/04-compliance/uc-sc07-09-handle-dangerous-goods.md), step 3.
- Carry on board: [UC-SC07-09](../../use-cases/04-compliance/uc-sc07-09-handle-dangerous-goods.md), step 4.

## States

- Normal: loads of dangerous goods with class, quantity, driver and vehicle checks.
- Empty: "No dangerous goods".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the driver not certified: the assignment is refused.
- Read-only: issued documents are read-only.
- Offline: the issued declaration is kept on the driver's phone.

Shown entities (VD-15): [E-SC07-09 Dangerous goods declaration](../../data/e-sc07-09-dangerous-goods-declaration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-09 Dangerous goods declaration | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-09-dangerous-goods-e-sc07-09-dangerous-goods-declaration-active-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-09-dangerous-goods-e-sc07-09-dangerous-goods-declaration-active-phone-{light,dark}.png` |

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

- [FL-SC07-04 Compliance](../../flows/fl-sc07-04-compliance.md)

## Open questions

None.

---

⬅️ [S-SC07-08 Tachograph](s-sc07-08-tachograph.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-10 Fuel and tolls](../05-billing-and-performance/s-sc07-10-fuel-and-tolls.md)
