🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC03-01 Win and price](README.md) › 🖥️ S-SC03-02 Rate cards

# 🖥️ S-SC03-02 Rate cards

**Status:** 🔄 waiting for the owner

## Personas

- [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to set rate cards and pricing models
([UC-SC03-02](../../use-cases/01-win-and-price/uc-sc03-02-set-rate-cards-and-pricing-models.md)).

## Entry points

Services in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC03-01 step 2, U24 | desktop | ![FL-SC03-01 step 2, U24, light](../../images/01-win-and-price/u24-engagement-manager/2-rate-card-desktop-light.png) | ![FL-SC03-01 step 2, U24, dark](../../images/01-win-and-price/u24-engagement-manager/2-rate-card-desktop-dark.png) |
| FL-SC03-01 step 2, U24 | phone | ![FL-SC03-01 step 2, U24, light](../../images/01-win-and-price/u24-engagement-manager/2-rate-card-phone-light.png) | ![FL-SC03-01 step 2, U24, dark](../../images/01-win-and-price/u24-engagement-manager/2-rate-card-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc03-02-rate-cards-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc03-02-rate-cards-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc03-02-rate-cards-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc03-02-rate-cards-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc03-02-rate-cards-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc03-02-rate-cards-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc03-02-rate-cards-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc03-02-rate-cards-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC03-03 Rate card](../../data/e-sc03-03-rate-card.md), shown as the entity pages list them, with their
examples.

## Actions

- Set standard rates: [UC-SC03-02](../../use-cases/01-win-and-price/uc-sc03-02-set-rate-cards-and-pricing-models.md),
  step 1.
- Agree client rates: [UC-SC03-02](../../use-cases/01-win-and-price/uc-sc03-02-set-rate-cards-and-pricing-models.md),
  step 2.
- Choose the model: [UC-SC03-02](../../use-cases/01-win-and-price/uc-sc03-02-set-rate-cards-and-pricing-models.md), step
  3.
- Check the engagement's price:
  [UC-SC03-02](../../use-cases/01-win-and-price/uc-sc03-02-set-rate-cards-and-pricing-models.md), step 4.

## States

- Normal: standard and client rates per role, discounts and the engagements' models.
- Empty: "No rate card", with New rate card.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a role on the engagement without a rate: the engagement manager
  is warned and billing of that role waits.
- Read-only: consultants read rates only for their engagements.
- Offline: not available offline: office work at a desk on shared engagement figures. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC03-03 Rate card](../../data/e-sc03-03-rate-card.md),
[E-SC03-14 Pricing model](../../data/e-sc03-14-pricing-model.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC03-03 Rate card | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U24 | `u13-owner/s-sc03-02-rate-cards-e-sc03-03-rate-card-active-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-02-rate-cards-e-sc03-03-rate-card-active-{desktop,phone}-{light,dark}.png` |
| E-SC03-14 Pricing model | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U24 | `u13-owner/s-sc03-02-rate-cards-e-sc03-14-pricing-model-active-{desktop,phone}-{light,dark}.png`, `u24-engagement-manager/s-sc03-02-rate-cards-e-sc03-14-pricing-model-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC03-01 Win and price](../../flows/fl-sc03-01-win-and-price.md)

## Open questions

None.

---

⬅️ [S-SC03-01 Statement of work](s-sc03-01-statement-of-work.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC03-03 Staffing](../02-staff-and-plan/s-sc03-03-staffing.md)
