🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-02 Sales](README.md) › 🖥️ S-SC10-06 Agency fees

# 🖥️ S-SC10-06 Agency fees

**Status:** ✅ specified

## Personas

- [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to bill and display agency fees
([UC-SC10-06](../../use-cases/02-sales/uc-sc10-06-bill-and-display-agency-fees.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-02 step 4, U35 | desktop | ![FL-SC10-02 step 4, U35, light](../../images/02-sales/u35-real-estate-agent/4-fees-desktop-light.png) | ![FL-SC10-02 step 4, U35, dark](../../images/02-sales/u35-real-estate-agent/4-fees-desktop-dark.png) |
| FL-SC10-02 step 4, U35 | phone | ![FL-SC10-02 step 4, U35, light](../../images/02-sales/u35-real-estate-agent/4-fees-phone-light.png) | ![FL-SC10-02 step 4, U35, dark](../../images/02-sales/u35-real-estate-agent/4-fees-phone-dark.png) |
| FL-SC10-02 step 4, U35 | tablet | ![FL-SC10-02 step 4, U35, light](../../images/02-sales/u35-real-estate-agent/4-fees-tablet-light.png) | ![FL-SC10-02 step 4, U35, dark](../../images/02-sales/u35-real-estate-agent/4-fees-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-06-agency-fees-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-06-agency-fees-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-06-agency-fees-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-06-agency-fees-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-06-agency-fees-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-06-agency-fees-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc10-06-agency-fees-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc10-06-agency-fees-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC10-06 Fee scale](../../data/e-sc10-06-fee-scale.md), shown as the entity pages list them, with their
examples.

## Actions

- Apply the scale: [UC-SC10-06](../../use-cases/02-sales/uc-sc10-06-bill-and-display-agency-fees.md), step 1.
- Show on the listing: [UC-SC10-06](../../use-cases/02-sales/uc-sc10-06-bill-and-display-agency-fees.md), step 2.
- Bill: [UC-SC10-06](../../use-cases/02-sales/uc-sc10-06-bill-and-display-agency-fees.md), step 3.
- Collect: [UC-SC10-06](../../use-cases/02-sales/uc-sc10-06-bill-and-display-agency-fees.md), step 4.

## States

- Normal: the fee scale and fees per sale.
- Empty: "No scale".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the scale missing: it is asked.
- Read-only: agents read the scale.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-06 Fee scale](../../data/e-sc10-06-fee-scale.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-06 Fee scale | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U35 | `u05-accounting/s-sc10-06-agency-fees-e-sc10-06-fee-scale-active-desktop-{light,dark}.png`, `u35-real-estate-agent/s-sc10-06-agency-fees-e-sc10-06-fee-scale-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC10-02 Sales](../../flows/fl-sc10-02-sales.md)

## Open questions

None.

---

⬅️ [S-SC10-05 Client funds](s-sc10-05-client-funds.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-07 Letting](../03-lettings/s-sc10-07-letting.md)
