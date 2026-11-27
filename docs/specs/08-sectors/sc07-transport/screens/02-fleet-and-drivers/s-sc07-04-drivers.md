🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-02 Fleet and drivers](README.md) › 🖥️ S-SC07-04 Drivers

# 🖥️ S-SC07-04 Drivers

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Keep each driver's documents and their expiries; HR is reminded of each document 60 days before it expires, a default
the company may change ([D575](../../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md),
[UC-SC07-04](../../use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-02 step 2, U29 | desktop | ![FL-SC07-02 step 2, U29, light](../../images/02-fleet-and-drivers/u29-dispatcher/2-drivers-desktop-light.png) | ![FL-SC07-02 step 2, U29, dark](../../images/02-fleet-and-drivers/u29-dispatcher/2-drivers-desktop-dark.png) |
| FL-SC07-02 step 2, U29 | phone | ![FL-SC07-02 step 2, U29, light](../../images/02-fleet-and-drivers/u29-dispatcher/2-drivers-phone-light.png) | ![FL-SC07-02 step 2, U29, dark](../../images/02-fleet-and-drivers/u29-dispatcher/2-drivers-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-04-drivers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-04-drivers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-04-drivers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-04-drivers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-04-drivers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-04-drivers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-04-drivers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-04-drivers-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-04 Driver document](../../data/e-sc07-04-driver-document.md), shown as the entity pages list them,
with their examples.

## Actions

- Record documents: [UC-SC07-04](../../use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md),
  step 1.
- Follow expiries: [UC-SC07-04](../../use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md),
  step 2.
- Remind and plan: [UC-SC07-04](../../use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md),
  step 3.
- Use in planning: [UC-SC07-04](../../use-cases/02-fleet-and-drivers/uc-sc07-04-manage-drivers-and-their-documents.md),
  step 4.

## States

- Normal: drivers with documents and expiries; a document within the reminder delay (60 days by default, a company
  setting) is marked, and HR has been reminded.
- Empty: "No driver".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an expired document: the driver is blocked from trips.
- Read-only: drivers read their own.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-04 Driver document](../../data/e-sc07-04-driver-document.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-04 Driver document | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06, U29 | `u06-hr/s-sc07-04-drivers-e-sc07-04-driver-document-active-desktop-{light,dark}.png`, `u29-dispatcher/s-sc07-04-drivers-e-sc07-04-driver-document-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC07-02 Fleet and drivers](../../flows/fl-sc07-02-fleet-and-drivers.md)

## Open questions

None.

---

⬅️ [S-SC07-03 Fleet](s-sc07-03-fleet.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-05 Consignment notes](../03-on-the-road/s-sc07-05-consignment-notes.md)
