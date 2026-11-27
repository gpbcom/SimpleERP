🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-04 Sales and certification](README.md) › 🖥️ S-SC13-12 Organic

# 🖥️ S-SC13-12 Organic

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to keep organic certification records,
[UC-SC13-12](../../use-cases/04-sales-and-certification/uc-sc13-12-keep-organic-certification-records.md).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-04 step 3, U40 | desktop | ![FL-SC13-04 step 3, U40, light](../../images/04-sales-and-certification/u40-farmer/3-organic-desktop-light.png) | ![FL-SC13-04 step 3, U40, dark](../../images/04-sales-and-certification/u40-farmer/3-organic-desktop-dark.png) |
| FL-SC13-04 step 3, U40 | phone | ![FL-SC13-04 step 3, U40, light](../../images/04-sales-and-certification/u40-farmer/3-organic-phone-light.png) | ![FL-SC13-04 step 3, U40, dark](../../images/04-sales-and-certification/u40-farmer/3-organic-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-12-organic-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-12-organic-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-12-organic-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-12-organic-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-12-organic-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-12-organic-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-12-organic-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-12-organic-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-11 Organic record](../../data/e-sc13-11-organic-record.md), shown as the entity pages list them,
with their examples.

## Actions

- Keep records:
  [UC-SC13-12](../../use-cases/04-sales-and-certification/uc-sc13-12-keep-organic-certification-records.md), step 1.
- Prepare the control:
  [UC-SC13-12](../../use-cases/04-sales-and-certification/uc-sc13-12-keep-organic-certification-records.md), step 2.
- Record the result:
  [UC-SC13-12](../../use-cases/04-sales-and-certification/uc-sc13-12-keep-organic-certification-records.md), step 3.
- Act: [UC-SC13-12](../../use-cases/04-sales-and-certification/uc-sc13-12-keep-organic-certification-records.md), step
  4.

## States

- Normal: organic records and control results.
- Empty: "No record".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a mixed lot: it is refused.
- Read-only: past controls are read-only.
- Offline: not available offline: office work on aid, accounts and margins. Offline work is kept for the phone forms of
  the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC13-11 Organic record](../../data/e-sc13-11-organic-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-11 Organic record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U27, U40 | `u27-quality-manager/s-sc13-12-organic-e-sc13-11-organic-record-recorded-{desktop,tablet}-{light,dark}.png`, `u40-farmer/s-sc13-12-organic-e-sc13-11-organic-record-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-04 Sales and certification](../../flows/fl-sc13-04-sales-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC13-11 Cooperative](s-sc13-11-cooperative.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-13 Batches](../05-food-processing/s-sc13-13-batches.md)
