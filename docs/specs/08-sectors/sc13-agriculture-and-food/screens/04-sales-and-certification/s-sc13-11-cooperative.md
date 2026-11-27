🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-04 Sales and certification](README.md) › 🖥️ S-SC13-11 Cooperative

# 🖥️ S-SC13-11 Cooperative

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to deliver to the cooperative and follow payments,
[UC-SC13-11](../../use-cases/04-sales-and-certification/uc-sc13-11-deliver-to-the-cooperative-and-follow-payments.md).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-04 step 2, U40 | desktop | ![FL-SC13-04 step 2, U40, light](../../images/04-sales-and-certification/u40-farmer/2-cooperative-desktop-light.png) | ![FL-SC13-04 step 2, U40, dark](../../images/04-sales-and-certification/u40-farmer/2-cooperative-desktop-dark.png) |
| FL-SC13-04 step 2, U40 | phone | ![FL-SC13-04 step 2, U40, light](../../images/04-sales-and-certification/u40-farmer/2-cooperative-phone-light.png) | ![FL-SC13-04 step 2, U40, dark](../../images/04-sales-and-certification/u40-farmer/2-cooperative-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-11-cooperative-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-11-cooperative-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-11-cooperative-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-11-cooperative-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-11-cooperative-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-11-cooperative-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-11-cooperative-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-11-cooperative-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC13-10 Cooperative statement](../../data/e-sc13-10-cooperative-statement.md), shown as the entity
pages list them, with their examples.

## Actions

- Deliver:
  [UC-SC13-11](../../use-cases/04-sales-and-certification/uc-sc13-11-deliver-to-the-cooperative-and-follow-payments.md),
  step 1.
- Receive the statement:
  [UC-SC13-11](../../use-cases/04-sales-and-certification/uc-sc13-11-deliver-to-the-cooperative-and-follow-payments.md),
  step 2.
- Match:
  [UC-SC13-11](../../use-cases/04-sales-and-certification/uc-sc13-11-deliver-to-the-cooperative-and-follow-payments.md),
  step 3.
- Match payments:
  [UC-SC13-11](../../use-cases/04-sales-and-certification/uc-sc13-11-deliver-to-the-cooperative-and-follow-payments.md),
  step 4.

## States

- Normal: deliveries, statements and payments.
- Empty: "No delivery".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a difference: it is shown.
- Read-only: matched ones are read-only.
- Offline: not available offline: office work on aid, accounts and margins. Offline work is kept for the phone forms of
  the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC13-10 Cooperative statement](../../data/e-sc13-10-cooperative-statement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-10 Cooperative statement | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U40 | `u05-accounting/s-sc13-11-cooperative-e-sc13-10-cooperative-statement-active-desktop-{light,dark}.png`, `u40-farmer/s-sc13-11-cooperative-e-sc13-10-cooperative-statement-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-04 Sales and certification](../../flows/fl-sc13-04-sales-and-certification.md)

## Open questions

None.

---

⬅️ [S-SC13-10 Direct sales](s-sc13-10-direct-sales.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-12 Organic](s-sc13-12-organic.md)
