🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-03 On the road](README.md) › 🖥️ S-SC07-06 Driver app

# 🖥️ S-SC07-06 Driver app

**Status:** ✅ specified

## Personas

- [U30 Driver](../../../../01-users/personas/u30-driver.md)

## Purpose

Used to drive with the phone ([UC-SC07-06](../../use-cases/03-on-the-road/uc-sc07-06-drive-with-the-phone.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-03 step 2, U30 | phone | ![FL-SC07-03 step 2, U30, light](../../images/03-on-the-road/u30-driver/2-trip-phone-light.png) | ![FL-SC07-03 step 2, U30, dark](../../images/03-on-the-road/u30-driver/2-trip-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc07-06-driver-app-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc07-06-driver-app-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc07-06-driver-app-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc07-06-driver-app-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc07-06-driver-app-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc07-06-driver-app-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-06-driver-app-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-06-driver-app-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-06 Stop](../../data/e-sc07-06-stop.md), shown as the entity pages list them, with their examples.

## Actions

- Start the trip: [UC-SC07-06](../../use-cases/03-on-the-road/uc-sc07-06-drive-with-the-phone.md), step 1.
- Check in at the stop: [UC-SC07-06](../../use-cases/03-on-the-road/uc-sc07-06-drive-with-the-phone.md), step 2.
- Scan: [UC-SC07-06](../../use-cases/03-on-the-road/uc-sc07-06-drive-with-the-phone.md), step 3.
- Check out and go: [UC-SC07-06](../../use-cases/03-on-the-road/uc-sc07-06-drive-with-the-phone.md), step 4.

## States

- Normal: the trip's stops in order, navigation, check-in and scans.
- Empty: "No trip today".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no network: check-ins and scans are kept and synced in order,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).
- Read-only: done stops are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the day's trip and stops are kept on the phone; check-ins, scans and positions wait and sync in order when the network
  is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC07-06 Stop](../../data/e-sc07-06-stop.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-06 Stop | New | Badge "New"; a new record starts here; next: Open (UC-SC07-07); fields editable within the role | U30 | `u30-driver/s-sc07-06-driver-app-e-sc07-06-stop-new-phone-{light,dark}.png` |
| E-SC07-06 Stop | Open | Badge "Open"; next: Done (UC-SC07-06); fields editable within the role | U30 | `u30-driver/s-sc07-06-driver-app-e-sc07-06-stop-open-phone-{light,dark}.png` |
| E-SC07-06 Stop | Done | Badge "Done"; next: Closed (UC-SC07-07); fields editable within the role | U30 | `u30-driver/s-sc07-06-driver-app-e-sc07-06-stop-done-phone-{light,dark}.png` |
| E-SC07-06 Stop | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U30 | `u30-driver/s-sc07-06-driver-app-e-sc07-06-stop-closed-phone-{light,dark}.png` |

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

⬅️ [S-SC07-05 Consignment notes](s-sc07-05-consignment-notes.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-07 Proof of delivery](s-sc07-07-proof-of-delivery.md)
