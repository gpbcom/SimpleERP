🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-04 Compliance](README.md) › 🖥️ S-SC07-19 International trips

# 🖥️ S-SC07-19 International trips

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Used to follow cabotage and international trips
([UC-SC07-19](../../use-cases/04-compliance/uc-sc07-19-follow-cabotage-and-international-trips.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-04 step 3, U29 | desktop | ![FL-SC07-04 step 3, U29, light](../../images/04-compliance/u29-dispatcher/3-cabotage-desktop-light.png) | ![FL-SC07-04 step 3, U29, dark](../../images/04-compliance/u29-dispatcher/3-cabotage-desktop-dark.png) |
| FL-SC07-04 step 3, U29 | phone | ![FL-SC07-04 step 3, U29, light](../../images/04-compliance/u29-dispatcher/3-cabotage-phone-light.png) | ![FL-SC07-04 step 3, U29, dark](../../images/04-compliance/u29-dispatcher/3-cabotage-phone-dark.png) |
| Error E1, U29 | desktop | ![Error E1, U29, light](../../images/04-compliance/u29-dispatcher/e1-cabotage-limit-desktop-light.png) | ![Error E1, U29, dark](../../images/04-compliance/u29-dispatcher/e1-cabotage-limit-desktop-dark.png) |
| Error E1, U29 | phone | ![Error E1, U29, light](../../images/04-compliance/u29-dispatcher/e1-cabotage-limit-phone-light.png) | ![Error E1, U29, dark](../../images/04-compliance/u29-dispatcher/e1-cabotage-limit-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-19-international-trips-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-19-international-trips-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-19-international-trips-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-19-international-trips-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-19-international-trips-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-19-international-trips-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-19-international-trips-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-19-international-trips-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-02 Trip](../../data/e-sc07-02-trip.md),
[E-SC07-15 Cabotage operation](../../data/e-sc07-15-cabotage-operation.md), shown as the entity pages list them, with
their examples.

## Actions

- Plan abroad: [UC-SC07-19](../../use-cases/04-compliance/uc-sc07-19-follow-cabotage-and-international-trips.md), step
  1.
- Count cabotage: [UC-SC07-19](../../use-cases/04-compliance/uc-sc07-19-follow-cabotage-and-international-trips.md),
  step 2.
- Declare postings: [UC-SC07-19](../../use-cases/04-compliance/uc-sc07-19-follow-cabotage-and-international-trips.md),
  step 3.
- Close: [UC-SC07-19](../../use-cases/04-compliance/uc-sc07-19-follow-cabotage-and-international-trips.md), step 4.

## States

- Normal: trips abroad with cabotage counts and declarations.
- Empty: "No trip abroad".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the limit reached: the operation is refused.
- Read-only: past operations are read-only.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-02 Trip](../../data/e-sc07-02-trip.md),
[E-SC07-15 Cabotage operation](../../data/e-sc07-15-cabotage-operation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-02 Trip | Planned | Badge "Planned"; a new record starts here; next: Sent (UC-SC07-02); fields editable within the role | U29 | `u29-dispatcher/s-sc07-19-international-trips-e-sc07-02-trip-planned-{desktop,phone}-{light,dark}.png` |
| E-SC07-02 Trip | Sent | Badge "Sent"; next: Assigned (BR-SC07-03); fields editable within the role | U29 | `u29-dispatcher/s-sc07-19-international-trips-e-sc07-02-trip-sent-{desktop,phone}-{light,dark}.png` |
| E-SC07-02 Trip | Assigned | Badge "Assigned"; final: read-only, no next state; the history shows how it got here | U29 | `u29-dispatcher/s-sc07-19-international-trips-e-sc07-02-trip-assigned-{desktop,phone}-{light,dark}.png` |
| E-SC07-15 Cabotage operation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U29 | `u29-dispatcher/s-sc07-19-international-trips-e-sc07-15-cabotage-operation-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC07-04 Compliance](../../flows/fl-sc07-04-compliance.md)

## Open questions

None.

---

⬅️ [S-SC07-18 Margins](../05-billing-and-performance/s-sc07-18-margins.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-20 Fleet assistant](../01-orders-and-planning/s-sc07-20-fleet-assistant.md)
