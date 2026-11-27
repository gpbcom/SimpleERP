🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-05 Sales force and performance](README.md) › 🖥️ S-SC15-15 Margins

# 🖥️ S-SC15-15 Margins

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to follow margins per customer, product and rep,
[UC-SC15-15](../../use-cases/05-sales-force-and-performance/uc-sc15-15-follow-margins-per-customer-product-and-rep.md).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-05 step 2, U13 | desktop | ![FL-SC15-05 step 2, U13, light](../../images/05-sales-force-and-performance/u13-owner/2-margins-desktop-light.png) | ![FL-SC15-05 step 2, U13, dark](../../images/05-sales-force-and-performance/u13-owner/2-margins-desktop-dark.png) |
| FL-SC15-05 step 2, U13 | phone | ![FL-SC15-05 step 2, U13, light](../../images/05-sales-force-and-performance/u13-owner/2-margins-phone-light.png) | ![FL-SC15-05 step 2, U13, dark](../../images/05-sales-force-and-performance/u13-owner/2-margins-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-15-margins-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-15-margins-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-15-margins-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-15-margins-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-15-margins-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-15-margins-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-15-margins-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-15-margins-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-02 Rebate rule](../../data/e-sc15-02-rebate-rule.md),
[E-SC15-04 Sales order](../../data/e-sc15-04-sales-order.md), shown as the entity pages list them, with their examples.

## Actions

- Open:
  [UC-SC15-15](../../use-cases/05-sales-force-and-performance/uc-sc15-15-follow-margins-per-customer-product-and-rep.md),
  step 1.
- Compare:
  [UC-SC15-15](../../use-cases/05-sales-force-and-performance/uc-sc15-15-follow-margins-per-customer-product-and-rep.md),
  step 2.
- Drill:
  [UC-SC15-15](../../use-cases/05-sales-force-and-performance/uc-sc15-15-follow-margins-per-customer-product-and-rep.md),
  step 3.
- Act:
  [UC-SC15-15](../../use-cases/05-sales-force-and-performance/uc-sc15-15-follow-margins-per-customer-product-and-rep.md),
  step 4.

## States

- Normal: margins per customer, product and rep net of rebates.
- Empty: "No sale".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, costs missing: they are shown.
- Read-only: reps see their own.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC15-05 Sales force and performance](../../flows/fl-sc15-05-sales-force-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC15-14 Visits](s-sc15-14-visits.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-16 Credit limits](s-sc15-16-credit-limits.md)
