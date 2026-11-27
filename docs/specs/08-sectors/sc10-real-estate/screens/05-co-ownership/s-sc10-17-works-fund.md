🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-05 Co-ownership](README.md) › 🖥️ S-SC10-17 Works fund

# 🖥️ S-SC10-17 Works fund

**Status:** ✅ specified

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)

## Purpose

Used to manage the works fund and works
([UC-SC10-17](../../use-cases/05-co-ownership/uc-sc10-17-manage-the-works-fund-and-works.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-05 step 3, U34 | desktop | ![FL-SC10-05 step 3, U34, light](../../images/05-co-ownership/u34-property-manager/3-works-fund-desktop-light.png) | ![FL-SC10-05 step 3, U34, dark](../../images/05-co-ownership/u34-property-manager/3-works-fund-desktop-dark.png) |
| FL-SC10-05 step 3, U34 | tablet | ![FL-SC10-05 step 3, U34, light](../../images/05-co-ownership/u34-property-manager/3-works-fund-tablet-light.png) | ![FL-SC10-05 step 3, U34, dark](../../images/05-co-ownership/u34-property-manager/3-works-fund-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-17-works-fund-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-17-works-fund-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-17-works-fund-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-17-works-fund-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-17-works-fund-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-17-works-fund-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-17-works-fund-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-17-works-fund-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-15 Works fund](../../data/e-sc10-15-works-fund.md), shown as the entity pages list them, with
their examples.

## Actions

- Set the contribution: [UC-SC10-17](../../use-cases/05-co-ownership/uc-sc10-17-manage-the-works-fund-and-works.md),
  step 1.
- Vote works: [UC-SC10-17](../../use-cases/05-co-ownership/uc-sc10-17-manage-the-works-fund-and-works.md), step 2.
- Order works: [UC-SC10-17](../../use-cases/05-co-ownership/uc-sc10-17-manage-the-works-fund-and-works.md), step 3.
- Pay from the fund: [UC-SC10-17](../../use-cases/05-co-ownership/uc-sc10-17-manage-the-works-fund-and-works.md), step
  4.

## States

- Normal: the fund's contributions, balance and works.
- Empty: "No works".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, under the minimum: it is refused.
- Read-only: paid works are read-only.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-15 Works fund](../../data/e-sc10-15-works-fund.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-15 Works fund | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U34 | `u34-property-manager/s-sc10-17-works-fund-e-sc10-15-works-fund-active-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC10-05 Co-ownership](../../flows/fl-sc10-05-co-ownership.md)

## Open questions

None.

---

⬅️ [S-SC10-16 Budget and calls](s-sc10-16-budget-and-calls.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-18 Co-ownership accounts](s-sc10-18-co-ownership-accounts.md)
