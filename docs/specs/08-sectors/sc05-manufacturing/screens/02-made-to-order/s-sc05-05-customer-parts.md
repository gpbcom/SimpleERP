🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-02 Made to order](README.md) › 🖥️ S-SC05-05 Customer parts

# 🖥️ S-SC05-05 Customer parts

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Used to handle customer-supplied parts
([UC-SC05-05](../../use-cases/02-made-to-order/uc-sc05-05-handle-customer-supplied-parts.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-02 step 3, U15 | phone | ![FL-SC05-02 step 3, U15, light](../../images/02-made-to-order/u15-warehouse-operator/3-customer-parts-phone-light.png) | ![FL-SC05-02 step 3, U15, dark](../../images/02-made-to-order/u15-warehouse-operator/3-customer-parts-phone-dark.png) |
| FL-SC05-02 step 3, U15 | tablet | ![FL-SC05-02 step 3, U15, light](../../images/02-made-to-order/u15-warehouse-operator/3-customer-parts-tablet-light.png) | ![FL-SC05-02 step 3, U15, dark](../../images/02-made-to-order/u15-warehouse-operator/3-customer-parts-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc05-05-customer-parts-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc05-05-customer-parts-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc05-05-customer-parts-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc05-05-customer-parts-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc05-05-customer-parts-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc05-05-customer-parts-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-05-customer-parts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-05-customer-parts-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC05-05 Customer-supplied part](../../data/e-sc05-05-customer-supplied-part.md), shown as the entity
pages list them, with their examples.

## Actions

- Receive: [UC-SC05-05](../../use-cases/02-made-to-order/uc-sc05-05-handle-customer-supplied-parts.md), step 1.
- Consume for that customer:
  [UC-SC05-05](../../use-cases/02-made-to-order/uc-sc05-05-handle-customer-supplied-parts.md), step 2.
- Return the rest: [UC-SC05-05](../../use-cases/02-made-to-order/uc-sc05-05-handle-customer-supplied-parts.md), step 3.
- Report to the customer: [UC-SC05-05](../../use-cases/02-made-to-order/uc-sc05-05-handle-customer-supplied-parts.md),
  step 4.

## States

- Normal: the customer's parts received, consumed and returned.
- Empty: "No customer part".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, used for another customer: it is refused.
- Read-only: consumed parts are read-only.
- Offline: receipt scans are kept on the phone and sync when the network is back,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC05-05 Customer-supplied part](../../data/e-sc05-05-customer-supplied-part.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-05 Customer-supplied part | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15, U21 | `u15-warehouse-operator/s-sc05-05-customer-parts-e-sc05-05-customer-supplied-part-active-{phone,tablet}-{light,dark}.png`, `u21-production-planner/s-sc05-05-customer-parts-e-sc05-05-customer-supplied-part-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC05-04 Engineer to order](s-sc05-04-engineer-to-order.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-06 Labels](../03-packaging/s-sc05-06-labels.md)
