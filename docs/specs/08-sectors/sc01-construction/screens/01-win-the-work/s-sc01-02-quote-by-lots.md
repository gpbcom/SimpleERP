🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-01 Win the work](README.md) › 🖥️ S-SC01-02 Quote by lots

# 🖥️ S-SC01-02 Quote by lots

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)

## Purpose

Used to open a site ([UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md)); to quote by lots and
unit-price schedules
([UC-SC01-02](../../use-cases/01-win-the-work/uc-sc01-02-quote-by-lots-and-unit-price-schedules.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-01 step 1, U03 | desktop | ![FL-SC01-01 step 1, U03, light](../../images/01-win-the-work/u03-sales/1-quote-by-lots-desktop-light.png) | ![FL-SC01-01 step 1, U03, dark](../../images/01-win-the-work/u03-sales/1-quote-by-lots-desktop-dark.png) |
| FL-SC01-01 step 1, U03 | phone | ![FL-SC01-01 step 1, U03, light](../../images/01-win-the-work/u03-sales/1-quote-by-lots-phone-light.png) | ![FL-SC01-01 step 1, U03, dark](../../images/01-win-the-work/u03-sales/1-quote-by-lots-phone-dark.png) |
| FL-SC01-01 step 1, U03 | tablet | ![FL-SC01-01 step 1, U03, light](../../images/01-win-the-work/u03-sales/1-quote-by-lots-tablet-light.png) | ![FL-SC01-01 step 1, U03, dark](../../images/01-win-the-work/u03-sales/1-quote-by-lots-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-02-quote-by-lots-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-02-quote-by-lots-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-02-quote-by-lots-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-02-quote-by-lots-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-02-quote-by-lots-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-02-quote-by-lots-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-02-quote-by-lots-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-02-quote-by-lots-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md),
[E-SC01-02 Quote lot](../../data/e-sc01-02-quote-lot.md), shown as the entity pages list them, with their examples.

## Actions

- Mark quote Q-221 signed: [UC-SC01-01](../../use-cases/01-win-the-work/uc-sc01-01-open-a-site.md), step 1.
- Create the quote and its lots:
  [UC-SC01-02](../../use-cases/01-win-the-work/uc-sc01-02-quote-by-lots-and-unit-price-schedules.md), step 1.
- Price each lot: [UC-SC01-02](../../use-cases/01-win-the-work/uc-sc01-02-quote-by-lots-and-unit-price-schedules.md),
  step 2.
- Check margin and VAT:
  [UC-SC01-02](../../use-cases/01-win-the-work/uc-sc01-02-quote-by-lots-and-unit-price-schedules.md), step 3.
- Send for signature:
  [UC-SC01-02](../../use-cases/01-win-the-work/uc-sc01-02-quote-by-lots-and-unit-price-schedules.md), step 4.
- Sign the quote: [UC-SC01-02](../../use-cases/01-win-the-work/uc-sc01-02-quote-by-lots-and-unit-price-schedules.md),
  step 5.

## States

- Normal: the quote's lots, each with its lines, quantities, unit prices and total, the VAT per line, the margin per lot
  and the certificate.
- Empty: "No lot yet", with Add a lot.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the address is not found by the map lookup: the site manager
  types it by hand or places a pin; the site is not opened without an address.
- Read-only: a sent or signed quote is read-only; a change makes a new version.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC01-02 Quote lot](../../data/e-sc01-02-quote-lot.md),
[E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-02 Quote lot | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U09, U22 | `u03-sales/s-sc01-02-quote-by-lots-e-sc01-02-quote-lot-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-02-quote-by-lots-e-sc01-02-quote-lot-active-phone-{light,dark}.png`, `u22-site-manager/s-sc01-02-quote-by-lots-e-sc01-02-quote-lot-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Planned | Badge "Planned"; a new record starts here; next: Running (UC-SC01-01); fields editable within the role | U03, U09, U22 | `u03-sales/s-sc01-02-quote-by-lots-e-sc01-01-construction-site-planned-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-02-quote-by-lots-e-sc01-01-construction-site-planned-phone-{light,dark}.png`, `u22-site-manager/s-sc01-02-quote-by-lots-e-sc01-01-construction-site-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Running | Badge "Running"; next: Accepted (UC-SC01-01); fields editable within the role | U03, U09, U22 | `u03-sales/s-sc01-02-quote-by-lots-e-sc01-01-construction-site-running-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-02-quote-by-lots-e-sc01-01-construction-site-running-phone-{light,dark}.png`, `u22-site-manager/s-sc01-02-quote-by-lots-e-sc01-01-construction-site-running-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-01 Win the work](../../flows/fl-sc01-01-win-the-work.md)

## Open questions

None.

---

⬅️ [S-SC01-01 Site](s-sc01-01-site.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-03 Site planning](../02-prepare-the-site/s-sc01-03-site-planning.md)
