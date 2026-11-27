🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-06 After an incident](README.md) › 🖥️ S-F20-24 Service credits

# 🖥️ S-F20-24 Service credits

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Show each month's targets, measures and credits.

## Entry points

Support plan; the credit notification.

## Wireframe

```text
Service credits, November 2026
-------------------------------------------------------------------------------
Target                Measured    Met    Credit
Availability 99.5 %   99.4 %      no     10 %
Urgent answer 1 h     52 min      yes    -
-------------------------------------------------------------------------------
Credit 42.00 EUR on the December invoice     [Dispute]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-06 step 2, U13 | desktop | ![FL-F20-06 step 2, U13, light](../../images/06-after-an-incident/u13-owner/2-service-credits-desktop-light.png) | ![FL-F20-06 step 2, U13, dark](../../images/06-after-an-incident/u13-owner/2-service-credits-desktop-dark.png) |
| FL-F20-06 step 2, U13 | phone | ![FL-F20-06 step 2, U13, light](../../images/06-after-an-incident/u13-owner/2-service-credits-phone-light.png) | ![FL-F20-06 step 2, U13, dark](../../images/06-after-an-incident/u13-owner/2-service-credits-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-24-service-credits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-24-service-credits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-24-service-credits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-24-service-credits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-24-service-credits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-24-service-credits-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-24-service-credits-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-24-service-credits-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Target | E-F20-12 | text | no | yes |
| Measured | E-F20-16 | number | no | yes |
| Credit | E-F20-16 percent, amount | percent, EUR | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Dispute | footer | owner | engineer checks |

## States

- Normal: targets, measures and the credit.
- Empty: "All targets met this month".
- Loading: the frame and titles show at once with placeholder rows for the targets; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a dispute without reason, refused.
- Read-only: accounting reads.
- Offline: Figures last loaded stay visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F20-12 Support plan](../../data/e-f20-12-support-plan.md),
[E-F20-16 Service credit](../../data/e-f20-16-service-credit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-12 Support plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f20-24-service-credits-e-f20-12-support-plan-active-desktop-{light,dark}.png`, `u13-owner/s-f20-24-service-credits-e-f20-12-support-plan-active-{desktop,phone}-{light,dark}.png` |
| E-F20-16 Service credit | Computed | Badge "Computed"; a new record starts here; next: Issued or Disputed (UC-F20-24); fields editable within the role | U05, U13 | `u05-accounting/s-f20-24-service-credits-e-f20-16-service-credit-computed-desktop-{light,dark}.png`, `u13-owner/s-f20-24-service-credits-e-f20-16-service-credit-computed-{desktop,phone}-{light,dark}.png` |
| E-F20-16 Service credit | Disputed | Badge "Disputed"; next: Issued (UC-F20-24); fields editable within the role | U05, U13 | `u05-accounting/s-f20-24-service-credits-e-f20-16-service-credit-disputed-desktop-{light,dark}.png`, `u13-owner/s-f20-24-service-credits-e-f20-16-service-credit-disputed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-06 After an incident](../../flows/fl-f20-06-after-an-incident.md)

## Open questions

None.

---

⬅️ [S-F20-23 Incident report](s-f20-23-incident-report.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-25 NIS2 facts](s-f20-25-nis2-facts.md)
