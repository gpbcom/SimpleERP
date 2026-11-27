🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-02 Livestock](README.md) › 🖥️ S-SC13-06 Veterinary

# 🖥️ S-SC13-06 Veterinary

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Record each veterinary treatment of a food animal in the herd's health register with its withdrawal period, even when it
is nil, kept at least 5 years after the year of the last entry, and block the animal's products until the period ends
([UC-SC13-06](../../use-cases/02-livestock/uc-sc13-06-record-veterinary-treatments.md),
[CR-FR-163](../../../../10-country-packs/france/agriculture/cr-fr-163-livestock-health-register.md)). The block is
SimpleERP's way to keep food from being obtained before the period ends: the texts state no sales ban as such.

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-02 step 2, U40 | phone | ![FL-SC13-02 step 2, U40, light](../../images/02-livestock/u40-farmer/2-vet-phone-light.png) | ![FL-SC13-02 step 2, U40, dark](../../images/02-livestock/u40-farmer/2-vet-phone-dark.png) |
| FL-SC13-02 step 2, U40 | desktop | ![FL-SC13-02 step 2, U40, light](../../images/02-livestock/u40-farmer/2-vet-desktop-light.png) | ![FL-SC13-02 step 2, U40, dark](../../images/02-livestock/u40-farmer/2-vet-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-06-veterinary-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-06-veterinary-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-06-veterinary-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-06-veterinary-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-06-veterinary-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-06-veterinary-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-06-veterinary-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-06-veterinary-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-06 Veterinary treatment](../../data/e-sc13-06-veterinary-treatment.md), shown as the entity pages
list them, with their examples.

## Actions

- Record: [UC-SC13-06](../../use-cases/02-livestock/uc-sc13-06-record-veterinary-treatments.md), step 1.
- Set the withdrawal: [UC-SC13-06](../../use-cases/02-livestock/uc-sc13-06-record-veterinary-treatments.md), step 2.
- Block products: [UC-SC13-06](../../use-cases/02-livestock/uc-sc13-06-record-veterinary-treatments.md), step 3.
- Release: [UC-SC13-06](../../use-cases/02-livestock/uc-sc13-06-record-veterinary-treatments.md), step 4.

## States

- Normal: treatments with withdrawal ends and blocks.
- Empty: "No treatment".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a product sold during withdrawal: it is refused.
- Read-only: past treatments are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the herd are kept on the phone; treatments wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-06 Veterinary treatment](../../data/e-sc13-06-veterinary-treatment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-06 Veterinary treatment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40 | `u40-farmer/s-sc13-06-veterinary-e-sc13-06-veterinary-treatment-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-02 Livestock](../../flows/fl-sc13-02-livestock.md)

## Open questions

None.

---

⬅️ [S-SC13-05 Herd](s-sc13-05-herd.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-07 Aid declaration](../03-farm-business/s-sc13-07-aid-declaration.md)
