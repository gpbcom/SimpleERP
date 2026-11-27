🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-01 Take on a recipient](README.md) › 🖥️ S-SC04-01 Recipient

# 🖥️ S-SC04-01 Recipient

**Status:** 🔄 waiting for the owner

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to register a care recipient and their funding,
[UC-SC04-01](../../use-cases/01-take-on-a-recipient/uc-sc04-01-register-a-care-recipient-and-their-funding.md).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-01 step 1, U25 | desktop | ![FL-SC04-01 step 1, U25, light](../../images/01-take-on-a-recipient/u25-care-coordinator/1-recipient-desktop-light.png) | ![FL-SC04-01 step 1, U25, dark](../../images/01-take-on-a-recipient/u25-care-coordinator/1-recipient-desktop-dark.png) |
| FL-SC04-01 step 1, U25 | phone | ![FL-SC04-01 step 1, U25, light](../../images/01-take-on-a-recipient/u25-care-coordinator/1-recipient-phone-light.png) | ![FL-SC04-01 step 1, U25, dark](../../images/01-take-on-a-recipient/u25-care-coordinator/1-recipient-phone-dark.png) |
| Error E1, U25 | desktop | ![Error E1, U25, light](../../images/01-take-on-a-recipient/u25-care-coordinator/e1-not-authorised-desktop-light.png) | ![Error E1, U25, dark](../../images/01-take-on-a-recipient/u25-care-coordinator/e1-not-authorised-desktop-dark.png) |
| Error E1, U25 | phone | ![Error E1, U25, light](../../images/01-take-on-a-recipient/u25-care-coordinator/e1-not-authorised-phone-light.png) | ![Error E1, U25, dark](../../images/01-take-on-a-recipient/u25-care-coordinator/e1-not-authorised-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-01-recipient-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-01-recipient-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-01-recipient-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-01-recipient-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-01-recipient-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-01-recipient-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-01-recipient-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-01-recipient-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-01 Care recipient](../../data/e-sc04-01-care-recipient.md),
[E-SC04-02 Care funding](../../data/e-sc04-02-care-funding.md),
[E-F6-14 Funder agreement](../../../../02-functional/f06-customers-and-sales/data/e-f06-14-funder-agreement.md), shown
as the entity pages list them, with their examples.

## Actions

- Create the recipient:
  [UC-SC04-01](../../use-cases/01-take-on-a-recipient/uc-sc04-01-register-a-care-recipient-and-their-funding.md), step
  1.
- Check the activity is covered:
  [UC-SC04-01](../../use-cases/01-take-on-a-recipient/uc-sc04-01-register-a-care-recipient-and-their-funding.md), step
  2.
- Add funding:
  [UC-SC04-01](../../use-cases/01-take-on-a-recipient/uc-sc04-01-register-a-care-recipient-and-their-funding.md), step
  3.
- Record consents:
  [UC-SC04-01](../../use-cases/01-take-on-a-recipient/uc-sc04-01-register-a-care-recipient-and-their-funding.md), step
  4.

## States

- Normal: the recipient with address, access code, contacts, funders and shares, consents and state.
- Empty: "No recipient yet", with New recipient.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the activity is not covered: the registration is refused with the
  missing approval ([BR-SC04-02](../../business-rules/br-sc04-02-activities-need-their-registration.md)).
- Read-only: carers see only what their visits need.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-01 Care recipient](../../data/e-sc04-01-care-recipient.md),
[E-SC04-02 Care funding](../../data/e-sc04-02-care-funding.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-01 Care recipient | Assessed | Badge "Assessed"; a new record starts here; next: Served (UC-SC04-01); fields editable within the role | U09, U25 | `u09-customer/s-sc04-01-recipient-e-sc04-01-care-recipient-assessed-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-01-recipient-e-sc04-01-care-recipient-assessed-{desktop,phone}-{light,dark}.png` |
| E-SC04-01 Care recipient | Served | Badge "Served"; next: Left or Paused (BR-SC04-10); fields editable within the role | U09, U25 | `u09-customer/s-sc04-01-recipient-e-sc04-01-care-recipient-served-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-01-recipient-e-sc04-01-care-recipient-served-{desktop,phone}-{light,dark}.png` |
| E-SC04-01 Care recipient | Left | Badge "Left"; final: read-only, no next state; the history shows how it got here | U09, U25 | `u09-customer/s-sc04-01-recipient-e-sc04-01-care-recipient-left-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-01-recipient-e-sc04-01-care-recipient-left-{desktop,phone}-{light,dark}.png` |
| E-SC04-01 Care recipient | Paused | Badge "Paused"; next: Left (BR-SC04-10); fields editable within the role | U09, U25 | `u09-customer/s-sc04-01-recipient-e-sc04-01-care-recipient-paused-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-01-recipient-e-sc04-01-care-recipient-paused-{desktop,phone}-{light,dark}.png` |
| E-SC04-02 Care funding | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U25 | `u09-customer/s-sc04-01-recipient-e-sc04-02-care-funding-active-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-01-recipient-e-sc04-02-care-funding-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC04-01 Take on a recipient](../../flows/fl-sc04-01-take-on-a-recipient.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC04-02 Care plan](s-sc04-02-care-plan.md)
