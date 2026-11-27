🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-02 Made to order](README.md) › 🖥️ S-SC05-03 Configurator

# 🖥️ S-SC05-03 Configurator

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Used to configure a product to order
([UC-SC05-03](../../use-cases/02-made-to-order/uc-sc05-03-configure-a-product-to-order.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-02 step 1, U03 | desktop | ![FL-SC05-02 step 1, U03, light](../../images/02-made-to-order/u03-sales/1-configurator-desktop-light.png) | ![FL-SC05-02 step 1, U03, dark](../../images/02-made-to-order/u03-sales/1-configurator-desktop-dark.png) |
| FL-SC05-02 step 1, U03 | phone | ![FL-SC05-02 step 1, U03, light](../../images/02-made-to-order/u03-sales/1-configurator-phone-light.png) | ![FL-SC05-02 step 1, U03, dark](../../images/02-made-to-order/u03-sales/1-configurator-phone-dark.png) |
| FL-SC05-02 step 1, U03 | tablet | ![FL-SC05-02 step 1, U03, light](../../images/02-made-to-order/u03-sales/1-configurator-tablet-light.png) | ![FL-SC05-02 step 1, U03, dark](../../images/02-made-to-order/u03-sales/1-configurator-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-03-configurator-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-03-configurator-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-03-configurator-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-03-configurator-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-03-configurator-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-03-configurator-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-03-configurator-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-03-configurator-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC05-03 Configuration rule](../../data/e-sc05-03-configuration-rule.md), shown as the entity pages list
them, with their examples.

## Actions

- Choose options: [UC-SC05-03](../../use-cases/02-made-to-order/uc-sc05-03-configure-a-product-to-order.md), step 1.
- Quote: [UC-SC05-03](../../use-cases/02-made-to-order/uc-sc05-03-configure-a-product-to-order.md), step 2.
- Order creates the build: [UC-SC05-03](../../use-cases/02-made-to-order/uc-sc05-03-configure-a-product-to-order.md),
  step 3.
- Launch the build: [UC-SC05-03](../../use-cases/02-made-to-order/uc-sc05-03-configure-a-product-to-order.md), step 4.

## States

- Normal: options, allowed combinations, price and the built bill of materials.
- Empty: "No configurable product".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a forbidden combination: it is not offered, with the rule shown.
- Read-only: a sent quote is read-only.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC05-03 Configuration rule](../../data/e-sc05-03-configuration-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-03 Configuration rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U21 | `u03-sales/s-sc05-03-configurator-e-sc05-03-configuration-rule-active-{desktop,phone,tablet}-{light,dark}.png`, `u21-production-planner/s-sc05-03-configurator-e-sc05-03-configuration-rule-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC05-02 Made to order](../../flows/fl-sc05-02-made-to-order.md)

## Open questions

None.

---

⬅️ [S-SC05-02 Recipes](../01-production-setups/s-sc05-02-recipes.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-04 Engineer to order](s-sc05-04-engineer-to-order.md)
