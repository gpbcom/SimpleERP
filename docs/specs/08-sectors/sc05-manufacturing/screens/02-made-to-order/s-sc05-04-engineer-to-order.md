🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-02 Made to order](README.md) › 🖥️ S-SC05-04 Engineer to order

# 🖥️ S-SC05-04 Engineer to order

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to engineer to order ([UC-SC05-04](../../use-cases/02-made-to-order/uc-sc05-04-engineer-to-order.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-02 step 2, U21 | desktop | ![FL-SC05-02 step 2, U21, light](../../images/02-made-to-order/u21-production-planner/2-engineer-to-order-desktop-light.png) | ![FL-SC05-02 step 2, U21, dark](../../images/02-made-to-order/u21-production-planner/2-engineer-to-order-desktop-dark.png) |
| FL-SC05-02 step 2, U21 | phone | ![FL-SC05-02 step 2, U21, light](../../images/02-made-to-order/u21-production-planner/2-engineer-to-order-phone-light.png) | ![FL-SC05-02 step 2, U21, dark](../../images/02-made-to-order/u21-production-planner/2-engineer-to-order-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-04-engineer-to-order-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-04-engineer-to-order-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-04-engineer-to-order-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-04-engineer-to-order-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-04-engineer-to-order-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-04-engineer-to-order-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-04-engineer-to-order-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-04-engineer-to-order-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC05-04 Engineered design](../../data/e-sc05-04-engineered-design.md), shown as the entity pages list
them, with their examples.

## Actions

- Design: [UC-SC05-04](../../use-cases/02-made-to-order/uc-sc05-04-engineer-to-order.md), step 1.
- Approve: [UC-SC05-04](../../use-cases/02-made-to-order/uc-sc05-04-engineer-to-order.md), step 2.
- Release: [UC-SC05-04](../../use-cases/02-made-to-order/uc-sc05-04-engineer-to-order.md), step 3.
- Cost the project: [UC-SC05-04](../../use-cases/02-made-to-order/uc-sc05-04-engineer-to-order.md), step 4.

## States

- Normal: the project's design versions, bill of materials, routing and approval.
- Empty: "No design yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the design is not approved: release is blocked.
- Read-only: an approved version is read-only.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC05-04 Engineered design](../../data/e-sc05-04-engineered-design.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-04 Engineered design | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U21, U27 | `u21-production-planner/s-sc05-04-engineer-to-order-e-sc05-04-engineered-design-active-{desktop,phone}-{light,dark}.png`, `u27-quality-manager/s-sc05-04-engineer-to-order-e-sc05-04-engineered-design-active-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC05-03 Configurator](s-sc05-03-configurator.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-05 Customer parts](s-sc05-05-customer-parts.md)
