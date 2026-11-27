🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-03 Farm business](README.md) › 🖥️ S-SC13-08 Machinery

# 🖥️ S-SC13-08 Machinery

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)

## Purpose

Used to manage machinery, fuel and maintenance
([UC-SC13-08](../../use-cases/03-farm-business/uc-sc13-08-manage-machinery-fuel-and-maintenance.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-03 step 2, U40 | desktop | ![FL-SC13-03 step 2, U40, light](../../images/03-farm-business/u40-farmer/2-machinery-desktop-light.png) | ![FL-SC13-03 step 2, U40, dark](../../images/03-farm-business/u40-farmer/2-machinery-desktop-dark.png) |
| FL-SC13-03 step 2, U40 | phone | ![FL-SC13-03 step 2, U40, light](../../images/03-farm-business/u40-farmer/2-machinery-phone-light.png) | ![FL-SC13-03 step 2, U40, dark](../../images/03-farm-business/u40-farmer/2-machinery-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-08-machinery-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-08-machinery-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-08-machinery-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-08-machinery-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-08-machinery-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-08-machinery-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-08-machinery-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-08-machinery-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-07 Machine](../../data/e-sc13-07-machine.md), shown as the entity pages list them, with their
examples.

## Actions

- Record use: [UC-SC13-08](../../use-cases/03-farm-business/uc-sc13-08-manage-machinery-fuel-and-maintenance.md), step
  1.
- Plan maintenance: [UC-SC13-08](../../use-cases/03-farm-business/uc-sc13-08-manage-machinery-fuel-and-maintenance.md),
  step 2.
- Charge costs: [UC-SC13-08](../../use-cases/03-farm-business/uc-sc13-08-manage-machinery-fuel-and-maintenance.md), step
  3.
- Repair: [UC-SC13-08](../../use-cases/03-farm-business/uc-sc13-08-manage-machinery-fuel-and-maintenance.md), step 4.

## States

- Normal: machines with hours, fuel, maintenance and costs.
- Empty: "No machine".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, overdue: the machine is flagged.
- Read-only: repairs are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  machines are kept on the phone; hours and fuel wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-07 Machine](../../data/e-sc13-07-machine.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-07 Machine | Overdue | Badge "Overdue"; a new record starts here; next: Flagged (UC-SC13-08); fields editable within the role | U40 | `u40-farmer/s-sc13-08-machinery-e-sc13-07-machine-overdue-{desktop,phone}-{light,dark}.png` |
| E-SC13-07 Machine | Flagged | Badge "Flagged"; next: Overdue (UC-SC13-08); fields editable within the role | U40 | `u40-farmer/s-sc13-08-machinery-e-sc13-07-machine-flagged-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-03 Farm business](../../flows/fl-sc13-03-farm-business.md)

## Open questions

None.

---

⬅️ [S-SC13-07 Aid declaration](s-sc13-07-aid-declaration.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-09 Seasonal work](s-sc13-09-seasonal-work.md)
