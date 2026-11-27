🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-01 Mandates and listings](README.md) › 🖥️ S-SC10-01 Mandates

# 🖥️ S-SC10-01 Mandates

**Status:** ✅ specified

## Personas

- [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md)

## Purpose

Used to take a mandate and record it in the register,
[UC-SC10-01](../../use-cases/01-mandates-and-listings/uc-sc10-01-take-a-mandate-and-record-it-in-the-register.md).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-01 step 1, U35 | desktop | ![FL-SC10-01 step 1, U35, light](../../images/01-mandates-and-listings/u35-real-estate-agent/1-mandate-desktop-light.png) | ![FL-SC10-01 step 1, U35, dark](../../images/01-mandates-and-listings/u35-real-estate-agent/1-mandate-desktop-dark.png) |
| FL-SC10-01 step 1, U35 | phone | ![FL-SC10-01 step 1, U35, light](../../images/01-mandates-and-listings/u35-real-estate-agent/1-mandate-phone-light.png) | ![FL-SC10-01 step 1, U35, dark](../../images/01-mandates-and-listings/u35-real-estate-agent/1-mandate-phone-dark.png) |
| FL-SC10-01 step 1, U35 | tablet | ![FL-SC10-01 step 1, U35, light](../../images/01-mandates-and-listings/u35-real-estate-agent/1-mandate-tablet-light.png) | ![FL-SC10-01 step 1, U35, dark](../../images/01-mandates-and-listings/u35-real-estate-agent/1-mandate-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-01-mandates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-01-mandates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-01-mandates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-01-mandates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-01-mandates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-01-mandates-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc10-01-mandates-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc10-01-mandates-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC10-01 Mandate](../../data/e-sc10-01-mandate.md), shown as the entity pages list them, with their
examples.

## Actions

- Agree the mandate:
  [UC-SC10-01](../../use-cases/01-mandates-and-listings/uc-sc10-01-take-a-mandate-and-record-it-in-the-register.md),
  step 1.
- Number it:
  [UC-SC10-01](../../use-cases/01-mandates-and-listings/uc-sc10-01-take-a-mandate-and-record-it-in-the-register.md),
  step 2.
- Sign:
  [UC-SC10-01](../../use-cases/01-mandates-and-listings/uc-sc10-01-take-a-mandate-and-record-it-in-the-register.md),
  step 3.
- Activate:
  [UC-SC10-01](../../use-cases/01-mandates-and-listings/uc-sc10-01-take-a-mandate-and-record-it-in-the-register.md),
  step 4.

## States

- Normal: the mandates register with number, kind, owner, property, price and end.
- Empty: "No mandate".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the card for the activity missing: the mandate is blocked.
- Read-only: a signed mandate is read-only.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-01 Mandate](../../data/e-sc10-01-mandate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-01 Mandate | Signed | Badge "Signed"; a new record starts here; next: Active or Cancelled (UC-SC10-01); fields editable within the role | U35 | `u35-real-estate-agent/s-sc10-01-mandates-e-sc10-01-mandate-signed-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC10-01 Mandate | Active | Badge "Active"; next: Blocked (UC-SC10-01); fields editable within the role | U35 | `u35-real-estate-agent/s-sc10-01-mandates-e-sc10-01-mandate-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC10-01 Mandate | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U35 | `u35-real-estate-agent/s-sc10-01-mandates-e-sc10-01-mandate-cancelled-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC10-01 Mandate | Blocked | Badge "Blocked"; next: Active (UC-SC10-01); fields editable within the role | U35 | `u35-real-estate-agent/s-sc10-01-mandates-e-sc10-01-mandate-blocked-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC10-01 Mandates and listings](../../flows/fl-sc10-01-mandates-and-listings.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC10-02 Listings](s-sc10-02-listings.md)
