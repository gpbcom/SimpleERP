🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-01 Crops](README.md) › 🖥️ S-SC13-01 Plots

# 🖥️ S-SC13-01 Plots

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to map plots and plan crops ([UC-SC13-01](../../use-cases/01-crops/uc-sc13-01-map-plots-and-plan-crops.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-01 step 1, U40 | desktop | ![FL-SC13-01 step 1, U40, light](../../images/01-crops/u40-farmer/1-plots-desktop-light.png) | ![FL-SC13-01 step 1, U40, dark](../../images/01-crops/u40-farmer/1-plots-desktop-dark.png) |
| FL-SC13-01 step 1, U40 | phone | ![FL-SC13-01 step 1, U40, light](../../images/01-crops/u40-farmer/1-plots-phone-light.png) | ![FL-SC13-01 step 1, U40, dark](../../images/01-crops/u40-farmer/1-plots-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-01-plots-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-01-plots-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-01-plots-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-01-plots-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-01-plots-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-01-plots-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-01-plots-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-01-plots-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-01 Plot](../../data/e-sc13-01-plot.md), [E-SC13-02 Crop plan](../../data/e-sc13-02-crop-plan.md),
shown as the entity pages list them, with their examples.

## Actions

- Draw or import plots: [UC-SC13-01](../../use-cases/01-crops/uc-sc13-01-map-plots-and-plan-crops.md), step 1.
- Mark organic: [UC-SC13-01](../../use-cases/01-crops/uc-sc13-01-map-plots-and-plan-crops.md), step 2.
- Plan crops: [UC-SC13-01](../../use-cases/01-crops/uc-sc13-01-map-plots-and-plan-crops.md), step 3.
- Follow the rotation: [UC-SC13-01](../../use-cases/01-crops/uc-sc13-01-map-plots-and-plan-crops.md), step 4.

## States

- Normal: plots on a map with area, organic status and crops by season.
- Empty: "No plot", with Draw a plot.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, overlapping plots: the plot is refused.
- Read-only: field workers read the map.
- Offline: the farm map stays readable on the phone; drawing waits.

Shown entities (VD-15): [E-SC13-02 Crop plan](../../data/e-sc13-02-crop-plan.md),
[E-SC13-01 Plot](../../data/e-sc13-01-plot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-02 Crop plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40 | `u40-farmer/s-sc13-01-plots-e-sc13-02-crop-plan-active-{desktop,phone}-{light,dark}.png` |
| E-SC13-01 Plot | New | Badge "New"; a new record starts here; next: Refused (UC-SC13-01); fields editable within the role | U40 | `u40-farmer/s-sc13-01-plots-e-sc13-01-plot-new-{desktop,phone}-{light,dark}.png` |
| E-SC13-01 Plot | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U40 | `u40-farmer/s-sc13-01-plots-e-sc13-01-plot-refused-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-01 Crops](../../flows/fl-sc13-01-crops.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC13-02 Treatments](s-sc13-02-treatments.md)
