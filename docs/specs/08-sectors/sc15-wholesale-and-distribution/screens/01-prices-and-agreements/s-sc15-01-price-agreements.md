🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-01 Prices and agreements](README.md) › 🖥️ S-SC15-01 Price agreements

# 🖥️ S-SC15-01 Price agreements

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md)

## Purpose

Used to agree customer prices and tiers
([UC-SC15-01](../../use-cases/01-prices-and-agreements/uc-sc15-01-agree-customer-prices-and-tiers.md)).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-01 step 1, U03 | desktop | ![FL-SC15-01 step 1, U03, light](../../images/01-prices-and-agreements/u03-sales/1-price-agreement-desktop-light.png) | ![FL-SC15-01 step 1, U03, dark](../../images/01-prices-and-agreements/u03-sales/1-price-agreement-desktop-dark.png) |
| FL-SC15-01 step 1, U03 | phone | ![FL-SC15-01 step 1, U03, light](../../images/01-prices-and-agreements/u03-sales/1-price-agreement-phone-light.png) | ![FL-SC15-01 step 1, U03, dark](../../images/01-prices-and-agreements/u03-sales/1-price-agreement-phone-dark.png) |
| FL-SC15-01 step 1, U03 | tablet | ![FL-SC15-01 step 1, U03, light](../../images/01-prices-and-agreements/u03-sales/1-price-agreement-tablet-light.png) | ![FL-SC15-01 step 1, U03, dark](../../images/01-prices-and-agreements/u03-sales/1-price-agreement-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-01-price-agreements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-01-price-agreements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-01-price-agreements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-01-price-agreements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-01-price-agreements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-01-price-agreements-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-01-price-agreements-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-01-price-agreements-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-01 Price agreement](../../data/e-sc15-01-price-agreement.md), shown as the entity pages list them,
with their examples.

## Actions

- Agree: [UC-SC15-01](../../use-cases/01-prices-and-agreements/uc-sc15-01-agree-customer-prices-and-tiers.md), step 1.
- Set validity: [UC-SC15-01](../../use-cases/01-prices-and-agreements/uc-sc15-01-agree-customer-prices-and-tiers.md),
  step 2.
- Check margins: [UC-SC15-01](../../use-cases/01-prices-and-agreements/uc-sc15-01-agree-customer-prices-and-tiers.md),
  step 3.
- Publish to reps: [UC-SC15-01](../../use-cases/01-prices-and-agreements/uc-sc15-01-agree-customer-prices-and-tiers.md),
  step 4.

## States

- Normal: agreements with lines, tiers, validity and margins.
- Empty: "No agreement".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a price below cost: approval is asked.
- Read-only: reps read prices only.
- Offline: the agreed prices are kept on the rep's tablet,
  [UC-F6-21](../../../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md).

Shown entities (VD-15): [E-SC15-01 Price agreement](../../data/e-sc15-01-price-agreement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-01 Price agreement | Active | Badge "Active"; a new record starts here; next: Expired (BR-SC15-02); fields editable within the role | U03, U42 | `u03-sales/s-sc15-01-price-agreements-e-sc15-01-price-agreement-active-{desktop,phone,tablet}-{light,dark}.png`, `u42-sales-representative/s-sc15-01-price-agreements-e-sc15-01-price-agreement-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC15-01 Price agreement | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03, U42 | `u03-sales/s-sc15-01-price-agreements-e-sc15-01-price-agreement-expired-{desktop,phone,tablet}-{light,dark}.png`, `u42-sales-representative/s-sc15-01-price-agreements-e-sc15-01-price-agreement-expired-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC15-01 Prices and agreements](../../flows/fl-sc15-01-prices-and-agreements.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC15-02 Rebates](s-sc15-02-rebates.md)
