🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-03 On the road](README.md) › 🖥️ S-SC07-05 Consignment notes

# 🖥️ S-SC07-05 Consignment notes

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)
- [U30 Driver](../../../../01-users/personas/u30-driver.md)

## Purpose

Used to issue consignment notes, paper or e-CMR
([UC-SC07-05](../../use-cases/03-on-the-road/uc-sc07-05-issue-consignment-notes-paper-or-e-cmr.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-03 step 1, U29 | desktop | ![FL-SC07-03 step 1, U29, light](../../images/03-on-the-road/u29-dispatcher/1-consignment-note-desktop-light.png) | ![FL-SC07-03 step 1, U29, dark](../../images/03-on-the-road/u29-dispatcher/1-consignment-note-desktop-dark.png) |
| FL-SC07-03 step 1, U29 | phone | ![FL-SC07-03 step 1, U29, light](../../images/03-on-the-road/u29-dispatcher/1-consignment-note-phone-light.png) | ![FL-SC07-03 step 1, U29, dark](../../images/03-on-the-road/u29-dispatcher/1-consignment-note-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-05-consignment-notes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-05-consignment-notes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-05-consignment-notes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-05-consignment-notes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-05-consignment-notes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-05-consignment-notes-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-05-consignment-notes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-05-consignment-notes-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-05 Consignment note](../../data/e-sc07-05-consignment-note.md), shown as the entity pages list
them, with their examples.

## Actions

- Generate: [UC-SC07-05](../../use-cases/03-on-the-road/uc-sc07-05-issue-consignment-notes-paper-or-e-cmr.md), step 1.
- Sign at loading: [UC-SC07-05](../../use-cases/03-on-the-road/uc-sc07-05-issue-consignment-notes-paper-or-e-cmr.md),
  step 2.
- Sign at delivery: [UC-SC07-05](../../use-cases/03-on-the-road/uc-sc07-05-issue-consignment-notes-paper-or-e-cmr.md),
  step 3.
- Keep: [UC-SC07-05](../../use-cases/03-on-the-road/uc-sc07-05-issue-consignment-notes-paper-or-e-cmr.md), step 4.

## States

- Normal: notes per shipment with signatures and reservations.
- Empty: "No note".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the note missing: the trip cannot start.
- Read-only: a signed note is read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the trip's notes are kept on the phone; signatures and reservations wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC07-05 Consignment note](../../data/e-sc07-05-consignment-note.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-05 Consignment note | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-05-consignment-notes-e-sc07-05-consignment-note-recorded-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-05-consignment-notes-e-sc07-05-consignment-note-recorded-phone-{light,dark}.png` |

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

- [FL-SC07-03 On the road](../../flows/fl-sc07-03-on-the-road.md)

## Open questions

None.

---

⬅️ [S-SC07-04 Drivers](../02-fleet-and-drivers/s-sc07-04-drivers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-06 Driver app](s-sc07-06-driver-app.md)
