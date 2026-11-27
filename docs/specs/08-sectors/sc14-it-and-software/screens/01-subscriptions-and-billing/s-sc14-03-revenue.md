🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-01 Subscriptions and billing](README.md) › 🖥️ S-SC14-03 Revenue

# 🖥️ S-SC14-03 Revenue

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to recognise subscription revenue
([UC-SC14-03](../../use-cases/01-subscriptions-and-billing/uc-sc14-03-recognise-subscription-revenue.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-01 step 3, U05 | desktop | ![FL-SC14-01 step 3, U05, light](../../images/01-subscriptions-and-billing/u05-accounting/3-revenue-desktop-light.png) | ![FL-SC14-01 step 3, U05, dark](../../images/01-subscriptions-and-billing/u05-accounting/3-revenue-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-03-revenue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-03-revenue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-03-revenue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-03-revenue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-03-revenue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-03-revenue-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc14-03-revenue-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc14-03-revenue-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-F8-14 Revenue schedule](../../../../02-functional/f08-accounting/data/e-f08-14-revenue-schedule.md),
shown as the entity pages list them, with their examples.

## Actions

- Compute: [UC-SC14-03](../../use-cases/01-subscriptions-and-billing/uc-sc14-03-recognise-subscription-revenue.md), step
  1.
- Review: [UC-SC14-03](../../use-cases/01-subscriptions-and-billing/uc-sc14-03-recognise-subscription-revenue.md), step
  2.
- Post: [UC-SC14-03](../../use-cases/01-subscriptions-and-billing/uc-sc14-03-recognise-subscription-revenue.md), step 3.
- Report: [UC-SC14-03](../../use-cases/01-subscriptions-and-billing/uc-sc14-03-recognise-subscription-revenue.md), step
  4.

## States

- Normal: schedules with recognised and deferred revenue.
- Empty: "No schedule".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a plan change mid-period: the schedule is recomputed.
- Read-only: posted months are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15):
[E-F8-14 Revenue schedule](../../../../02-functional/f08-accounting/data/e-f08-14-revenue-schedule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-14 Revenue schedule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-sc14-03-revenue-e-f08-14-revenue-schedule-active-desktop-{light,dark}.png` |

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

- [FL-SC14-01 Subscriptions and billing](../../flows/fl-sc14-01-subscriptions-and-billing.md)

## Open questions

None.

---

⬅️ [S-SC14-02 Usage](s-sc14-02-usage.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-04 Licences](../02-licences-and-renewals/s-sc14-04-licences.md)
