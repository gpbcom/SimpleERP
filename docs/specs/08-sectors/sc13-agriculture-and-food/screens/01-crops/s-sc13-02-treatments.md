🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-01 Crops](README.md) › 🖥️ S-SC13-02 Treatments

# 🖥️ S-SC13-02 Treatments

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Record each plant-protection treatment with its product, dose, area treated, plot and date, and the operator when known
([UC-SC13-02](../../use-cases/01-crops/uc-sc13-02-record-treatments-and-inputs.md)): the register does not require the
operator, so a treatment without one is saved; a missing dose or area is flagged.

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-01 step 2, U40 | phone | ![FL-SC13-01 step 2, U40, light](../../images/01-crops/u40-farmer/2-treatment-phone-light.png) | ![FL-SC13-01 step 2, U40, dark](../../images/01-crops/u40-farmer/2-treatment-phone-dark.png) |
| FL-SC13-01 step 2, U40 | desktop | ![FL-SC13-01 step 2, U40, light](../../images/01-crops/u40-farmer/2-treatment-desktop-light.png) | ![FL-SC13-01 step 2, U40, dark](../../images/01-crops/u40-farmer/2-treatment-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-02-treatments-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-02-treatments-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-02-treatments-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-02-treatments-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-02-treatments-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-02-treatments-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-02-treatments-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-02-treatments-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-03 Field operation](../../data/e-sc13-03-field-operation.md), shown as the entity pages list them,
with their examples.

## Actions

- Choose plot and product: [UC-SC13-02](../../use-cases/01-crops/uc-sc13-02-record-treatments-and-inputs.md), step 1.
- Record dose, area and date, and the operator if known:
  [UC-SC13-02](../../use-cases/01-crops/uc-sc13-02-record-treatments-and-inputs.md), step 2.
- Save: [UC-SC13-02](../../use-cases/01-crops/uc-sc13-02-record-treatments-and-inputs.md), step 3.
- Check the register: [UC-SC13-02](../../use-cases/01-crops/uc-sc13-02-record-treatments-and-inputs.md), step 4.

## States

- Normal: the treatment register by plot and date.
- Empty: "No treatment".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a product not allowed in organic: it is refused on organic plots.
- Read-only: synced records are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  plots and products are kept on the phone; treatments wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-03 Field operation](../../data/e-sc13-03-field-operation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-03 Field operation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U14, U40 | `u14-field-worker/s-sc13-02-treatments-e-sc13-03-field-operation-active-phone-{light,dark}.png`, `u40-farmer/s-sc13-02-treatments-e-sc13-03-field-operation-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-01 Crops](../../flows/fl-sc13-01-crops.md)

## Open questions

None.

---

⬅️ [S-SC13-01 Plots](s-sc13-01-plots.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-03 Fertilisation](s-sc13-03-fertilisation.md)
