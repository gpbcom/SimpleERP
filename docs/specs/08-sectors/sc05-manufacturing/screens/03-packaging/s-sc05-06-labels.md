🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-03 Packaging](README.md) › 🖥️ S-SC05-06 Labels

# 🖥️ S-SC05-06 Labels

**Status:** ✅ specified

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to package and label ([UC-SC05-06](../../use-cases/03-packaging/uc-sc05-06-package-and-label.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-03 step 1, U20 | tablet | ![FL-SC05-03 step 1, U20, light](../../images/03-packaging/u20-production-operator/1-labels-tablet-light.png) | ![FL-SC05-03 step 1, U20, dark](../../images/03-packaging/u20-production-operator/1-labels-tablet-dark.png) |
| Error E1, U20 | tablet | ![Error E1, U20, light](../../images/03-packaging/u20-production-operator/e1-no-lot-tablet-light.png) | ![Error E1, U20, dark](../../images/03-packaging/u20-production-operator/e1-no-lot-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-sc05-06-labels-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-sc05-06-labels-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-sc05-06-labels-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-sc05-06-labels-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-sc05-06-labels-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-sc05-06-labels-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-06-labels-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-06-labels-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-06 Label template](../../data/e-sc05-06-label-template.md), shown as the entity pages list them,
with their examples.

## Actions

- Pack: [UC-SC05-06](../../use-cases/03-packaging/uc-sc05-06-package-and-label.md), step 1.
- Print labels: [UC-SC05-06](../../use-cases/03-packaging/uc-sc05-06-package-and-label.md), step 2.
- Close the pallet: [UC-SC05-06](../../use-cases/03-packaging/uc-sc05-06-package-and-label.md), step 3.
- Ship: [UC-SC05-06](../../use-cases/03-packaging/uc-sc05-06-package-and-label.md), step 4.

## States

- Normal: the order's packages, labels to print and the pallet.
- Empty: "Nothing to pack".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a lot missing: printing is refused.
- Read-only: a closed pallet is read-only.
- Offline: the shop-floor tablet keeps working without the network,
  [UC-F12-26](../../../../02-functional/f12-manufacturing/use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md),
  packages and labels printed locally sync in order when it is back,
  [BR-F12-21](../../../../02-functional/f12-manufacturing/business-rules/br-f12-21-tablet-records-sync-in-order.md).

Shown entities (VD-15): [E-SC05-06 Label template](../../data/e-sc05-06-label-template.md),
[E-SC15-14 Pallet](../../../sc15-wholesale-and-distribution/data/e-sc15-14-pallet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-06 Label template | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15, U20 | `u15-warehouse-operator/s-sc05-06-labels-e-sc05-06-label-template-active-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-sc05-06-labels-e-sc05-06-label-template-active-tablet-{light,dark}.png` |
| E-SC15-14 Pallet | Open | Badge "Open"; a new record starts here; next: Closed (UC-SC05-06, BR-SC15-09); fields editable within the role | U15, U20 | `u15-warehouse-operator/s-sc05-06-labels-e-sc15-14-pallet-open-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-sc05-06-labels-e-sc15-14-pallet-open-tablet-{light,dark}.png` |
| E-SC15-14 Pallet | Closed | Badge "Closed"; next: Loaded (UC-SC15-09); fields editable within the role | U15, U20 | `u15-warehouse-operator/s-sc05-06-labels-e-sc15-14-pallet-closed-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-sc05-06-labels-e-sc15-14-pallet-closed-tablet-{light,dark}.png` |
| E-SC15-14 Pallet | Loaded | Badge "Loaded"; final: read-only, no next state; the history shows how it got here | U15, U20 | `u15-warehouse-operator/s-sc05-06-labels-e-sc15-14-pallet-loaded-{phone,tablet}-{light,dark}.png`, `u20-production-operator/s-sc05-06-labels-e-sc15-14-pallet-loaded-tablet-{light,dark}.png` |

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

- [FL-SC05-03 Packaging](../../flows/fl-sc05-03-packaging.md)

## Open questions

None.

---

⬅️ [S-SC05-05 Customer parts](../02-made-to-order/s-sc05-05-customer-parts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-07 Documents](../04-quality-system/s-sc05-07-documents.md)
