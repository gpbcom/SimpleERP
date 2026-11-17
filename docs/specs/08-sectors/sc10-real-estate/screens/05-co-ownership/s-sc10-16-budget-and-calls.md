🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-05 Co-ownership](README.md) › 🖥️ S-SC10-16 Budget and calls

# 🖥️ S-SC10-16 Budget and calls

**Status:** 🔄 waiting for the owner

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to vote the co-ownership budget and call funds
([UC-SC10-16](../../use-cases/05-co-ownership/uc-sc10-16-vote-the-co-ownership-budget-and-call-funds.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-05 step 2, U34 | desktop | ![FL-SC10-05 step 2, U34, light](../../images/05-co-ownership/u34-property-manager/2-calls-desktop-light.png) | ![FL-SC10-05 step 2, U34, dark](../../images/05-co-ownership/u34-property-manager/2-calls-desktop-dark.png) |
| FL-SC10-05 step 2, U34 | tablet | ![FL-SC10-05 step 2, U34, light](../../images/05-co-ownership/u34-property-manager/2-calls-tablet-light.png) | ![FL-SC10-05 step 2, U34, dark](../../images/05-co-ownership/u34-property-manager/2-calls-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-16-budget-and-calls-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-16-budget-and-calls-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-16-budget-and-calls-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-16-budget-and-calls-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-16-budget-and-calls-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-16-budget-and-calls-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-16-budget-and-calls-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-16-budget-and-calls-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-14 Call for funds](../../data/e-sc10-14-call-for-funds.md), shown as the entity pages list them,
with their examples.

## Actions

- Vote the budget:
  [UC-SC10-16](../../use-cases/05-co-ownership/uc-sc10-16-vote-the-co-ownership-budget-and-call-funds.md), step 1.
- Call funds by shares:
  [UC-SC10-16](../../use-cases/05-co-ownership/uc-sc10-16-vote-the-co-ownership-budget-and-call-funds.md), step 2.
- Pay: [UC-SC10-16](../../use-cases/05-co-ownership/uc-sc10-16-vote-the-co-ownership-budget-and-call-funds.md), step 3.
- Follow payments:
  [UC-SC10-16](../../use-cases/05-co-ownership/uc-sc10-16-vote-the-co-ownership-budget-and-call-funds.md), step 4.

## States

- Normal: budget, calls by lot and payments.
- Empty: "No call".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a co-owner late: a reminder goes out.
- Read-only: co-owners read their own.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-14 Call for funds](../../data/e-sc10-14-call-for-funds.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-14 Call for funds | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09, U34 | `u09-customer/s-sc10-16-budget-and-calls-e-sc10-14-call-for-funds-recorded-phone-{light,dark}.png`, `u34-property-manager/s-sc10-16-budget-and-calls-e-sc10-14-call-for-funds-recorded-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC10-05 Co-ownership](../../flows/fl-sc10-05-co-ownership.md)

## Open questions

None.

---

⬅️ [S-SC10-15 Assemblies](s-sc10-15-assemblies.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-17 Works fund](s-sc10-17-works-fund.md)
