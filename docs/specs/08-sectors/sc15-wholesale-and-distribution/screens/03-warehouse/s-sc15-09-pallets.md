🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-03 Warehouse](README.md) › 🖥️ S-SC15-09 Pallets

# 🖥️ S-SC15-09 Pallets

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Used to build pallets and GS1 labels
([UC-SC15-09](../../use-cases/03-warehouse/uc-sc15-09-build-pallets-and-gs1-labels.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-03 step 2, U15 | phone | ![FL-SC15-03 step 2, U15, light](../../images/03-warehouse/u15-warehouse-operator/2-pallets-phone-light.png) | ![FL-SC15-03 step 2, U15, dark](../../images/03-warehouse/u15-warehouse-operator/2-pallets-phone-dark.png) |
| FL-SC15-03 step 2, U15 | tablet | ![FL-SC15-03 step 2, U15, light](../../images/03-warehouse/u15-warehouse-operator/2-pallets-tablet-light.png) | ![FL-SC15-03 step 2, U15, dark](../../images/03-warehouse/u15-warehouse-operator/2-pallets-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc15-09-pallets-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc15-09-pallets-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc15-09-pallets-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc15-09-pallets-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc15-09-pallets-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc15-09-pallets-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-09-pallets-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-09-pallets-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-05 Pick wave](../../data/e-sc15-05-pick-wave.md), shown as the entity pages list them, with their
examples.

## Actions

- Build: [UC-SC15-09](../../use-cases/03-warehouse/uc-sc15-09-build-pallets-and-gs1-labels.md), step 1.
- Label: [UC-SC15-09](../../use-cases/03-warehouse/uc-sc15-09-build-pallets-and-gs1-labels.md), step 2.
- Load: [UC-SC15-09](../../use-cases/03-warehouse/uc-sc15-09-build-pallets-and-gs1-labels.md), step 3.
- Send the advice: [UC-SC15-09](../../use-cases/03-warehouse/uc-sc15-09-build-pallets-and-gs1-labels.md), step 4.

## States

- Normal: pallets with contents and labels.
- Empty: "No pallet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a label missing: loading is blocked.
- Read-only: loaded pallets are read-only.
- Offline: labels print on the local network; loading scans sync later.

Shown entities (VD-15): [E-SC15-05 Pick wave](../../data/e-sc15-05-pick-wave.md),
[E-SC15-14 Pallet](../../data/e-sc15-14-pallet.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-05 Pick wave | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U15 | `u15-warehouse-operator/s-sc15-09-pallets-e-sc15-05-pick-wave-active-{phone,tablet}-{light,dark}.png` |
| E-SC15-14 Pallet | Open | Badge "Open"; a new record starts here; next: Closed (UC-SC05-06, BR-SC15-09); fields editable within the role | U15 | `u15-warehouse-operator/s-sc15-09-pallets-e-sc15-14-pallet-open-{phone,tablet}-{light,dark}.png` |
| E-SC15-14 Pallet | Closed | Badge "Closed"; next: Loaded (UC-SC15-09); fields editable within the role | U15 | `u15-warehouse-operator/s-sc15-09-pallets-e-sc15-14-pallet-closed-{phone,tablet}-{light,dark}.png` |
| E-SC15-14 Pallet | Loaded | Badge "Loaded"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-sc15-09-pallets-e-sc15-14-pallet-loaded-{phone,tablet}-{light,dark}.png` |

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

- [FL-SC15-03 Warehouse](../../flows/fl-sc15-03-warehouse.md)

## Open questions

None.

---

⬅️ [S-SC15-08 Waves](../02-orders/s-sc15-08-waves.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-10 Returns](s-sc15-10-returns.md)
