🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-01 Crops](README.md) › 🖥️ S-SC13-03 Fertilisation

# 🖥️ S-SC13-03 Fertilisation

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to record fertilisation and the nitrogen plan
([UC-SC13-03](../../use-cases/01-crops/uc-sc13-03-record-fertilisation-and-the-nitrogen-plan.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-01 step 3, U40 | desktop | ![FL-SC13-01 step 3, U40, light](../../images/01-crops/u40-farmer/3-fertilisation-desktop-light.png) | ![FL-SC13-01 step 3, U40, dark](../../images/01-crops/u40-farmer/3-fertilisation-desktop-dark.png) |
| FL-SC13-01 step 3, U40 | phone | ![FL-SC13-01 step 3, U40, light](../../images/01-crops/u40-farmer/3-fertilisation-phone-light.png) | ![FL-SC13-01 step 3, U40, dark](../../images/01-crops/u40-farmer/3-fertilisation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-03-fertilisation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-03-fertilisation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-03-fertilisation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-03-fertilisation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-03-fertilisation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-03-fertilisation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-03-fertilisation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-03-fertilisation-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-03 Field operation](../../data/e-sc13-03-field-operation.md), shown as the entity pages list them,
with their examples.

## Actions

- Plan: [UC-SC13-03](../../use-cases/01-crops/uc-sc13-03-record-fertilisation-and-the-nitrogen-plan.md), step 1.
- Record: [UC-SC13-03](../../use-cases/01-crops/uc-sc13-03-record-fertilisation-and-the-nitrogen-plan.md), step 2.
- Compare: [UC-SC13-03](../../use-cases/01-crops/uc-sc13-03-record-fertilisation-and-the-nitrogen-plan.md), step 3.
- Close the season: [UC-SC13-03](../../use-cases/01-crops/uc-sc13-03-record-fertilisation-and-the-nitrogen-plan.md),
  step 4.

## States

- Normal: the nitrogen plan and inputs per plot.
- Empty: "No plan".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over the plan: the farmer is warned.
- Read-only: closed seasons are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the plan are kept on the phone; inputs wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-03 Field operation](../../data/e-sc13-03-field-operation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-03 Field operation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40 | `u40-farmer/s-sc13-03-fertilisation-e-sc13-03-field-operation-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC13-02 Treatments](s-sc13-02-treatments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-04 Harvests](s-sc13-04-harvests.md)
