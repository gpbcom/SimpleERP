🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-04 Health exchanges](README.md) › 🖥️ S-SC09-09 Health exchanges

# 🖥️ S-SC09-09 Health exchanges

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to share with the national health record and secure messaging,
[UC-SC09-09](../../use-cases/04-health-exchanges/uc-sc09-09-share-with-the-national-health-record-and-secure-messaging.md).

## Entry points

Health practices in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-04 step 1, U13 | desktop | ![FL-SC09-04 step 1, U13, light](../../images/04-health-exchanges/u13-owner/1-national-record-desktop-light.png) | ![FL-SC09-04 step 1, U13, dark](../../images/04-health-exchanges/u13-owner/1-national-record-desktop-dark.png) |
| FL-SC09-04 step 1, U13 | phone | ![FL-SC09-04 step 1, U13, light](../../images/04-health-exchanges/u13-owner/1-national-record-phone-light.png) | ![FL-SC09-04 step 1, U13, dark](../../images/04-health-exchanges/u13-owner/1-national-record-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-09-health-exchanges-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-09-health-exchanges-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-09-health-exchanges-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-09-health-exchanges-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-09-health-exchanges-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-09-health-exchanges-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc09-09-health-exchanges-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc09-09-health-exchanges-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC09-03 Clinical record entry](../../data/e-sc09-03-clinical-record-entry.md),
[E-SC09-08 Health exchange](../../data/e-sc09-08-health-exchange.md), shown as the entity pages list them, with their
examples.

## Actions

- File the document:
  [UC-SC09-09](../../use-cases/04-health-exchanges/uc-sc09-09-share-with-the-national-health-record-and-secure-messaging.md),
  step 1.
- Message a colleague:
  [UC-SC09-09](../../use-cases/04-health-exchanges/uc-sc09-09-share-with-the-national-health-record-and-secure-messaging.md),
  step 3.
- See the state:
  [UC-SC09-09](../../use-cases/04-health-exchanges/uc-sc09-09-share-with-the-national-health-record-and-secure-messaging.md),
  step 4.

## States

- Normal: documents with their national record and messaging state.
- Empty: "No document".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the service down: it is retried.
- Read-only: sent documents are read-only.
- Offline: not available offline: work on health data that stays on certified hosting. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC09-08 Health exchange](../../data/e-sc09-08-health-exchange.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-08 Health exchange | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-sc09-09-health-exchanges-e-sc09-08-health-exchange-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC09-04 Health exchanges](../../flows/fl-sc09-04-health-exchanges.md)

## Open questions

None.

---

⬅️ [S-SC09-08 Patient billing](../03-insurance-billing/s-sc09-08-patient-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-10 Results](s-sc09-10-results.md)
