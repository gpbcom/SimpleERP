🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-02 Livestock](README.md) › 🖥️ S-SC13-05 Herd

# 🖥️ S-SC13-05 Herd

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to identify animals and keep the herd register
([UC-SC13-05](../../use-cases/02-livestock/uc-sc13-05-identify-animals-and-keep-the-herd-register.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-02 step 1, U40 | phone | ![FL-SC13-02 step 1, U40, light](../../images/02-livestock/u40-farmer/1-herd-phone-light.png) | ![FL-SC13-02 step 1, U40, dark](../../images/02-livestock/u40-farmer/1-herd-phone-dark.png) |
| FL-SC13-02 step 1, U40 | desktop | ![FL-SC13-02 step 1, U40, light](../../images/02-livestock/u40-farmer/1-herd-desktop-light.png) | ![FL-SC13-02 step 1, U40, dark](../../images/02-livestock/u40-farmer/1-herd-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-05-herd-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-05-herd-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-05-herd-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-05-herd-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-05-herd-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-05-herd-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-05-herd-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-05-herd-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-05 Animal](../../data/e-sc13-05-animal.md), shown as the entity pages list them, with their
examples.

## Actions

- Record the event:
  [UC-SC13-05](../../use-cases/02-livestock/uc-sc13-05-identify-animals-and-keep-the-herd-register.md), step 1.
- Notify: [UC-SC13-05](../../use-cases/02-livestock/uc-sc13-05-identify-animals-and-keep-the-herd-register.md), step 2.
- Update the register:
  [UC-SC13-05](../../use-cases/02-livestock/uc-sc13-05-identify-animals-and-keep-the-herd-register.md), step 3.
- Tag: [UC-SC13-05](../../use-cases/02-livestock/uc-sc13-05-identify-animals-and-keep-the-herd-register.md), step 4.

## States

- Normal: the herd with identifiers, events and notification state.
- Empty: "No animal".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a late notification: the farmer is alerted.
- Read-only: notified events are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the herd list are kept on the phone; events wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-05 Animal](../../data/e-sc13-05-animal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-05 Animal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40 | `u40-farmer/s-sc13-05-herd-e-sc13-05-animal-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-02 Livestock](../../flows/fl-sc13-02-livestock.md)

## Open questions

None.

---

⬅️ [S-SC13-04 Harvests](../01-crops/s-sc13-04-harvests.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-06 Veterinary](s-sc13-06-veterinary.md)
