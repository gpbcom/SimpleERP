🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-01 Crops](README.md) › 🖥️ S-SC13-04 Harvests

# 🖥️ S-SC13-04 Harvests

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to record harvests, yields and lots
([UC-SC13-04](../../use-cases/01-crops/uc-sc13-04-record-harvests-yields-and-lots.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-01 step 4, U40 | phone | ![FL-SC13-01 step 4, U40, light](../../images/01-crops/u40-farmer/4-harvest-phone-light.png) | ![FL-SC13-01 step 4, U40, dark](../../images/01-crops/u40-farmer/4-harvest-phone-dark.png) |
| FL-SC13-01 step 4, U40 | desktop | ![FL-SC13-01 step 4, U40, light](../../images/01-crops/u40-farmer/4-harvest-desktop-light.png) | ![FL-SC13-01 step 4, U40, dark](../../images/01-crops/u40-farmer/4-harvest-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-04-harvests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-04-harvests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-04-harvests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-04-harvests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-04-harvests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-04-harvests-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-04-harvests-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-04-harvests-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-04 Lot](../../data/e-sc13-04-lot.md), shown as the entity pages list them, with their examples.

## Actions

- Record the harvest: [UC-SC13-04](../../use-cases/01-crops/uc-sc13-04-record-harvests-yields-and-lots.md), step 1.
- Create the lot: [UC-SC13-04](../../use-cases/01-crops/uc-sc13-04-record-harvests-yields-and-lots.md), step 2.
- Store: [UC-SC13-04](../../use-cases/01-crops/uc-sc13-04-record-harvests-yields-and-lots.md), step 3.
- See the yield: [UC-SC13-04](../../use-cases/01-crops/uc-sc13-04-record-harvests-yields-and-lots.md), step 4.

## States

- Normal: harvests, lots and yields.
- Empty: "No harvest".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a plot unknown: it is refused.
- Read-only: stored lots are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  plots are kept on the phone; harvest weights wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-04 Lot](../../data/e-sc13-04-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-04 Lot | Blocked | Badge "Blocked"; a new record starts here; next: Expired or Refused (UC-SC13-17, UC-SC13-04); fields editable within the role | U40 | `u40-farmer/s-sc13-04-harvests-e-sc13-04-lot-blocked-{desktop,phone}-{light,dark}.png` |
| E-SC13-04 Lot | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U40 | `u40-farmer/s-sc13-04-harvests-e-sc13-04-lot-refused-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC13-03 Fertilisation](s-sc13-03-fertilisation.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-05 Herd](../02-livestock/s-sc13-05-herd.md)
