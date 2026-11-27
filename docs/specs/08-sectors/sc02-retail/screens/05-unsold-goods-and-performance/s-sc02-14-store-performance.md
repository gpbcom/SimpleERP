🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-05 Unsold goods and performance](README.md) ›
🖥️ S-SC02-14 Store performance

# 🖥️ S-SC02-14 Store performance

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to follow store performance
([UC-SC02-14](../../use-cases/05-unsold-goods-and-performance/uc-sc02-14-follow-store-performance.md)).

## Entry points

Retail in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-05 step 2, U13 | desktop | ![FL-SC02-05 step 2, U13, light](../../images/05-unsold-goods-and-performance/u13-owner/2-performance-desktop-light.png) | ![FL-SC02-05 step 2, U13, dark](../../images/05-unsold-goods-and-performance/u13-owner/2-performance-desktop-dark.png) |
| FL-SC02-05 step 2, U13 | phone | ![FL-SC02-05 step 2, U13, light](../../images/05-unsold-goods-and-performance/u13-owner/2-performance-phone-light.png) | ![FL-SC02-05 step 2, U13, dark](../../images/05-unsold-goods-and-performance/u13-owner/2-performance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-14-store-performance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-14-store-performance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-14-store-performance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-14-store-performance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-14-store-performance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-14-store-performance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-14-store-performance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-14-store-performance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC02-12 Footfall count](../../data/e-sc02-12-footfall-count.md),
[E-SC02-01 Store](../../data/e-sc02-01-store.md), shown as the entity pages list them, with their examples.

## Actions

- Open the dashboard:
  [UC-SC02-14](../../use-cases/05-unsold-goods-and-performance/uc-sc02-14-follow-store-performance.md), step 1.
- Compare stores: [UC-SC02-14](../../use-cases/05-unsold-goods-and-performance/uc-sc02-14-follow-store-performance.md),
  step 2.
- Drill into a store:
  [UC-SC02-14](../../use-cases/05-unsold-goods-and-performance/uc-sc02-14-follow-store-performance.md), step 3.
- Export: [UC-SC02-14](../../use-cases/05-unsold-goods-and-performance/uc-sc02-14-follow-store-performance.md), step 4.

## States

- Normal: per store: sales per m2, footfall, conversion, basket, stock cover, with comparisons.
- Empty: "No sale in this period".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no counter in a store: conversion is not shown for that store.
- Read-only: store managers see their own store.
- Offline: not available offline: back-office work on stock and sales shared by all stores. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC02-05 Unsold goods and performance](../../flows/fl-sc02-05-unsold-goods-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC02-13 Unsold goods](s-sc02-13-unsold-goods.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-15 Store assistant](s-sc02-15-store-assistant.md)
