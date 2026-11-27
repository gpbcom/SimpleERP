🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-04 Bill and recognise](README.md) › 🖥️ S-SC03-07 Milestones

# 🖥️ S-SC03-07 Milestones

**Status:** ✅ specified

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to bill fixed price by milestones and retainers,
[UC-SC03-07](../../use-cases/04-bill-and-recognise/uc-sc03-07-bill-fixed-price-by-milestones-and-retainers.md).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-04 step 2, U24 | desktop | ![FL-SC03-04 step 2, U24, light](../../images/04-bill-and-recognise/u24-engagement-manager/2-milestone-desktop-light.png) | ![FL-SC03-04 step 2, U24, dark](../../images/04-bill-and-recognise/u24-engagement-manager/2-milestone-desktop-dark.png) |
| FL-SC03-04 step 2, U24 | phone | ![FL-SC03-04 step 2, U24, light](../../images/04-bill-and-recognise/u24-engagement-manager/2-milestone-phone-light.png) | ![FL-SC03-04 step 2, U24, dark](../../images/04-bill-and-recognise/u24-engagement-manager/2-milestone-phone-dark.png) |
| Error E1, U24 | desktop | ![Error E1, U24, light](../../images/04-bill-and-recognise/u24-engagement-manager/e1-milestone-not-accepted-desktop-light.png) | ![Error E1, U24, dark](../../images/04-bill-and-recognise/u24-engagement-manager/e1-milestone-not-accepted-desktop-dark.png) |
| Error E1, U24 | phone | ![Error E1, U24, light](../../images/04-bill-and-recognise/u24-engagement-manager/e1-milestone-not-accepted-phone-light.png) | ![Error E1, U24, dark](../../images/04-bill-and-recognise/u24-engagement-manager/e1-milestone-not-accepted-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-07-milestones-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-07-milestones-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-07-milestones-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-07-milestones-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-07-milestones-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-07-milestones-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-07-milestones-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-07-milestones-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-08 Milestone](../../data/e-sc03-08-milestone.md),
[E-SC03-07 Billing proposal](../../data/e-sc03-07-billing-proposal.md), shown as the entity pages list them, with their
examples.

## Actions

- Mark the milestone accepted:
  [UC-SC03-07](../../use-cases/04-bill-and-recognise/uc-sc03-07-bill-fixed-price-by-milestones-and-retainers.md), step
  1.
- Bill its share:
  [UC-SC03-07](../../use-cases/04-bill-and-recognise/uc-sc03-07-bill-fixed-price-by-milestones-and-retainers.md), step
  2.
- Track the balance:
  [UC-SC03-07](../../use-cases/04-bill-and-recognise/uc-sc03-07-bill-fixed-price-by-milestones-and-retainers.md), step
  3.
- Plan the next milestone:
  [UC-SC03-07](../../use-cases/04-bill-and-recognise/uc-sc03-07-bill-fixed-price-by-milestones-and-retainers.md), step
  4.

## States

- Normal: milestones with share, acceptance and billing state; retainers with balance.
- Empty: "No milestone", with Add a milestone.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the milestone is not accepted: it is not billed.
- Read-only: a billed milestone is read-only.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-08 Milestone](../../data/e-sc03-08-milestone.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-08 Milestone | Planned | Badge "Planned"; a new record starts here; next: Accepted (UC-SC03-07); fields editable within the role | U05, U24 | `u05-accounting/s-sc03-07-milestones-e-sc03-08-milestone-planned-desktop-{light,dark}.png`, `u24-engagement-manager/s-sc03-07-milestones-e-sc03-08-milestone-planned-{desktop,phone}-{light,dark}.png` |
| E-SC03-08 Milestone | Accepted | Badge "Accepted"; next: Billed (UC-SC03-07); fields editable within the role | U05, U24 | `u05-accounting/s-sc03-07-milestones-e-sc03-08-milestone-accepted-desktop-{light,dark}.png`, `u24-engagement-manager/s-sc03-07-milestones-e-sc03-08-milestone-accepted-{desktop,phone}-{light,dark}.png` |
| E-SC03-08 Milestone | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U05, U24 | `u05-accounting/s-sc03-07-milestones-e-sc03-08-milestone-billed-desktop-{light,dark}.png`, `u24-engagement-manager/s-sc03-07-milestones-e-sc03-08-milestone-billed-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-04 Bill and recognise](../../flows/fl-sc03-04-bill-and-recognise.md)

## Open questions

None.

---

⬅️ [S-SC03-06 T&M billing](s-sc03-06-t-m-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-08 Revenue](s-sc03-08-revenue.md)
