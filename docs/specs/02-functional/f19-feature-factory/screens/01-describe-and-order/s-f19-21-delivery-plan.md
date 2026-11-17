🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-01 Describe and order](README.md) › 🖥️ S-F19-21 Delivery plan

# 🖥️ S-F19-21 Delivery plan

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Purpose

Show each ordered feature's committed delivery date, its delays and its state.

## Entry points

Feature factory, my features; the delay notification.

## Wireframe

```text
Delivery plan
-------------------------------------------------------------------------------
Feature        Committed    Now          State      Reason
Gate booking   2026-12-03   2026-12-10   delayed    tests failing
Vat reminder   2026-11-28   -            on time
-------------------------------------------------------------------------------
[Announce delay] (engineer)   [Cancel order] (owner, when late)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-01 step 4, U13 | desktop | ![FL-F19-01 step 4, U13, light](../../images/01-describe-and-order/u13-owner/4-delivery-plan-desktop-light.png) | ![FL-F19-01 step 4, U13, dark](../../images/01-describe-and-order/u13-owner/4-delivery-plan-desktop-dark.png) |
| FL-F19-01 step 4, U13 | phone | ![FL-F19-01 step 4, U13, light](../../images/01-describe-and-order/u13-owner/4-delivery-plan-phone-light.png) | ![FL-F19-01 step 4, U13, dark](../../images/01-describe-and-order/u13-owner/4-delivery-plan-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/06-delivery-and-refunds/u13-owner/e1-delivery-plan-refused-desktop-light.png) | ![Error E1, U13, dark](../../images/06-delivery-and-refunds/u13-owner/e1-delivery-plan-refused-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/06-delivery-and-refunds/u13-owner/e1-delivery-plan-refused-phone-light.png) | ![Error E1, U13, dark](../../images/06-delivery-and-refunds/u13-owner/e1-delivery-plan-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-21-delivery-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-21-delivery-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-21-delivery-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-21-delivery-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-21-delivery-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-21-delivery-plan-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-21-delivery-plan-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-21-delivery-plan-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Feature | E-F19-11 feature request | name | no | yes |
| Committed | E-F19-11 committed | date | no | yes |
| Now | E-F19-11 delays | date | yes (engineer) | no |
| State | E-F19-11 state | list | no | yes |
| Reason | E-F19-11 delays | text | yes (engineer) | if delayed |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Announce delay | row | hosting engineer | owner told |
| Cancel order | row | owner | closed without charge when late |

## States

- Normal: ordered features with dates and states.
- Empty: "No feature ordered".
- Loading: the frame and titles show at once with placeholder rows for the orders; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a delay after the date, counted as missed.
- Read-only: the owner reads dates; only the engineer announces delays.
- Offline: The plan last loaded stays visible with its date. Nothing else is queued: D38 keeps only today's schedule,
  time and intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F19-11 Delivery commitment](../../data/e-f19-11-delivery-commitment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-11 Delivery commitment | On time | Badge "On time"; a new record starts here; next: Delayed or Delivered (UC-F19-21, UC-F19-03); fields editable within the role | U13, U48 | `u13-owner/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-on-time-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-on-time-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Delayed | Badge "Delayed"; next: Late or Delivered (UC-F19-19, UC-F19-03); fields editable within the role | U13, U48 | `u13-owner/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-delayed-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-delayed-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U13, U48 | `u13-owner/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-delivered-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-delivered-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Late | Badge "Late"; next: Delivered or Cancelled (UC-F19-03, UC-F19-21); fields editable within the role | U13, U48 | `u13-owner/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-late-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-late-{desktop,phone}-{light,dark}.png` |
| E-F19-11 Delivery commitment | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U48 | `u13-owner/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-cancelled-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f19-21-delivery-plan-e-f19-11-delivery-commitment-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the owner reads on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F19-06 Delivery and refunds](../../flows/fl-f19-06-delivery-and-refunds.md)

## Open questions

None.

---

⬅️ [S-F19-20 Promotion terms](../04-promote/s-f19-20-promotion-terms.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-22 Refunds](../06-delivery-and-refunds/s-f19-22-refunds.md)
