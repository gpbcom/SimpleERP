🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-01 Mandates and listings](README.md) › 🖥️ S-SC10-02 Listings

# 🖥️ S-SC10-02 Listings

**Status:** 🔄 waiting for the owner

## Personas

- [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md)

## Purpose

Used to publish listings on portals
([UC-SC10-02](../../use-cases/01-mandates-and-listings/uc-sc10-02-publish-listings-on-portals.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-01 step 2, U35 | desktop | ![FL-SC10-01 step 2, U35, light](../../images/01-mandates-and-listings/u35-real-estate-agent/2-listing-desktop-light.png) | ![FL-SC10-01 step 2, U35, dark](../../images/01-mandates-and-listings/u35-real-estate-agent/2-listing-desktop-dark.png) |
| FL-SC10-01 step 2, U35 | phone | ![FL-SC10-01 step 2, U35, light](../../images/01-mandates-and-listings/u35-real-estate-agent/2-listing-phone-light.png) | ![FL-SC10-01 step 2, U35, dark](../../images/01-mandates-and-listings/u35-real-estate-agent/2-listing-phone-dark.png) |
| FL-SC10-01 step 2, U35 | tablet | ![FL-SC10-01 step 2, U35, light](../../images/01-mandates-and-listings/u35-real-estate-agent/2-listing-tablet-light.png) | ![FL-SC10-01 step 2, U35, dark](../../images/01-mandates-and-listings/u35-real-estate-agent/2-listing-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-02-listings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-02-listings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-02-listings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-02-listings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-02-listings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-02-listings-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc10-02-listings-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc10-02-listings-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC10-02 Property listing](../../data/e-sc10-02-property-listing.md),
[E-SC10-12 Diagnostic](../../data/e-sc10-12-diagnostic.md), shown as the entity pages list them, with their examples.

## Actions

- Write the listing: [UC-SC10-02](../../use-cases/01-mandates-and-listings/uc-sc10-02-publish-listings-on-portals.md),
  step 1.
- Check diagnostics: [UC-SC10-02](../../use-cases/01-mandates-and-listings/uc-sc10-02-publish-listings-on-portals.md),
  step 2.
- Show fees and energy:
  [UC-SC10-02](../../use-cases/01-mandates-and-listings/uc-sc10-02-publish-listings-on-portals.md), step 3.
- Publish: [UC-SC10-02](../../use-cases/01-mandates-and-listings/uc-sc10-02-publish-listings-on-portals.md), step 4.

## States

- Normal: listings with text, photos, rating, fees and portals.
- Empty: "No listing".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, diagnostics missing: publication is blocked.
- Read-only: a withdrawn listing is read-only.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-02 Property listing](../../data/e-sc10-02-property-listing.md),
[E-SC10-12 Diagnostic](../../data/e-sc10-12-diagnostic.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-02 Property listing | Live | Badge "Live"; a new record starts here; next: Blocked (BR-SC10-08); fields editable within the role | U35 | `u35-real-estate-agent/s-sc10-02-listings-e-sc10-02-property-listing-live-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC10-02 Property listing | Blocked | Badge "Blocked"; next: Live (UC-SC10-02); fields editable within the role | U35 | `u35-real-estate-agent/s-sc10-02-listings-e-sc10-02-property-listing-blocked-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC10-12 Diagnostic | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U35 | `u35-real-estate-agent/s-sc10-02-listings-e-sc10-12-diagnostic-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC10-01 Mandates and listings](../../flows/fl-sc10-01-mandates-and-listings.md)

## Open questions

None.

---

⬅️ [S-SC10-01 Mandates](s-sc10-01-mandates.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-03 Viewings](../02-sales/s-sc10-03-viewings.md)
