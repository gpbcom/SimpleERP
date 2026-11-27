🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-02 Sales](README.md) › 🖥️ S-SC10-03 Viewings

# 🖥️ S-SC10-03 Viewings

**Status:** ✅ specified

## Personas

- [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to organise viewings ([UC-SC10-03](../../use-cases/02-sales/uc-sc10-03-organise-viewings.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-02 step 1, U35 | phone | ![FL-SC10-02 step 1, U35, light](../../images/02-sales/u35-real-estate-agent/1-viewings-phone-light.png) | ![FL-SC10-02 step 1, U35, dark](../../images/02-sales/u35-real-estate-agent/1-viewings-phone-dark.png) |
| FL-SC10-02 step 1, U35 | desktop | ![FL-SC10-02 step 1, U35, light](../../images/02-sales/u35-real-estate-agent/1-viewings-desktop-light.png) | ![FL-SC10-02 step 1, U35, dark](../../images/02-sales/u35-real-estate-agent/1-viewings-desktop-dark.png) |
| FL-SC10-02 step 1, U35 | tablet | ![FL-SC10-02 step 1, U35, light](../../images/02-sales/u35-real-estate-agent/1-viewings-tablet-light.png) | ![FL-SC10-02 step 1, U35, dark](../../images/02-sales/u35-real-estate-agent/1-viewings-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-03-viewings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-03-viewings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-03-viewings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-03-viewings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-03-viewings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-03-viewings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc10-03-viewings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc10-03-viewings-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC10-03 Viewing](../../data/e-sc10-03-viewing.md), shown as the entity pages list them, with their
examples.

## Actions

- Ask to visit: [UC-SC10-03](../../use-cases/02-sales/uc-sc10-03-organise-viewings.md), step 1.
- Confirm: [UC-SC10-03](../../use-cases/02-sales/uc-sc10-03-organise-viewings.md), step 2.
- Visit: [UC-SC10-03](../../use-cases/02-sales/uc-sc10-03-organise-viewings.md), step 3.
- Record feedback: [UC-SC10-03](../../use-cases/02-sales/uc-sc10-03-organise-viewings.md), step 4.

## States

- Normal: viewings with prospect, slot and feedback.
- Empty: "No viewing".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the owner unavailable: the viewing is rescheduled.
- Read-only: owners read the feedback.
- Offline: the day's viewings stay readable on the phone; feedback typed offline syncs later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC10-03 Viewing](../../data/e-sc10-03-viewing.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-03 Viewing | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U35 | `u09-customer/s-sc10-03-viewings-e-sc10-03-viewing-active-phone-{light,dark}.png`, `u35-real-estate-agent/s-sc10-03-viewings-e-sc10-03-viewing-active-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC10-02 Listings](../01-mandates-and-listings/s-sc10-02-listings.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-04 Offers](s-sc10-04-offers.md)
