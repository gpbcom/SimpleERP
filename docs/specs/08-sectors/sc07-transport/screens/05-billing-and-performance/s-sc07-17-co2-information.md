🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-05 Billing and performance](README.md) › 🖥️ S-SC07-17 CO2 information

# 🖥️ S-SC07-17 CO2 information

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to inform clients of CO2 per transport,
[UC-SC07-17](../../use-cases/05-billing-and-performance/uc-sc07-17-inform-clients-of-co2-per-transport.md).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-05 step 3, U29 | desktop | ![FL-SC07-05 step 3, U29, light](../../images/05-billing-and-performance/u29-dispatcher/3-co2-desktop-light.png) | ![FL-SC07-05 step 3, U29, dark](../../images/05-billing-and-performance/u29-dispatcher/3-co2-desktop-dark.png) |
| FL-SC07-05 step 3, U29 | phone | ![FL-SC07-05 step 3, U29, light](../../images/05-billing-and-performance/u29-dispatcher/3-co2-phone-light.png) | ![FL-SC07-05 step 3, U29, dark](../../images/05-billing-and-performance/u29-dispatcher/3-co2-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-17-co2-information-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-17-co2-information-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-17-co2-information-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-17-co2-information-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-17-co2-information-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-17-co2-information-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-17-co2-information-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-17-co2-information-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC07-13 Transport invoice line](../../data/e-sc07-13-transport-invoice-line.md), shown as the entity
pages list them, with their examples.

## Actions

- Compute: [UC-SC07-17](../../use-cases/05-billing-and-performance/uc-sc07-17-inform-clients-of-co2-per-transport.md),
  step 1.
- Show on the invoice:
  [UC-SC07-17](../../use-cases/05-billing-and-performance/uc-sc07-17-inform-clients-of-co2-per-transport.md), step 2.
- Report yearly:
  [UC-SC07-17](../../use-cases/05-billing-and-performance/uc-sc07-17-inform-clients-of-co2-per-transport.md), step 3.
- Feed sustainability:
  [UC-SC07-17](../../use-cases/05-billing-and-performance/uc-sc07-17-inform-clients-of-co2-per-transport.md), step 4.

## States

- Normal: emissions per transport and the yearly report per client.
- Empty: "No transport this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, data missing: default values are used and flagged.
- Read-only: reported years are read-only.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC07-17 Transport CO2 statement](../../data/e-sc07-17-transport-co2-statement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-17 Transport CO2 statement | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U29 | `u05-accounting/s-sc07-17-co2-information-e-sc07-17-transport-co2-statement-active-desktop-{light,dark}.png`, `u29-dispatcher/s-sc07-17-co2-information-e-sc07-17-transport-co2-statement-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC07-05 Billing and performance](../../flows/fl-sc07-05-billing-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC07-16 Client portal](../06-logistics-for-clients/s-sc07-16-client-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-18 Margins](s-sc07-18-margins.md)
