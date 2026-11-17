🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-07 Schemes and special contracts](README.md) › 🖥️ S-F13-23 Special regimes

# 🖥️ S-F13-23 Special regimes

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md), who computes and files
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md), who records show contracts
- [U40 Farmer](../../../../01-users/personas/u40-farmer.md), who records seasonal contracts

## Purpose

Pay and declare intermittent performers and farm workers under their own regimes and bodies.

## Entry points

Payroll menu, Special regimes; the "new show contract" or "new seasonal contract" notification.

## Wireframe

```text
Special regimes                          [Performers] [Farm workers]
-------------------------------------------------------------------------------
Contract           Person          Dates             Pay       Declaration
Show 2026-05-14    A. Leroy        05-14             320.00    accepted
Show 2026-05-14    B. Nguyen       05-13 to 05-14    540.00    due 05-29
Harvest 2026       C. Dupuis       09-07 to 10-02    1.10 SMIC exempted
-------------------------------------------------------------------------------
[Contract panel] performer number, fund, collector, exemption, [Compute] [File]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-07 step 4, U45 | desktop | ![FL-F13-07 step 4, U45, light](../../images/07-schemes-and-special-contracts/u45-payroll-officer/4-special-regimes-desktop-light.png) | ![FL-F13-07 step 4, U45, dark](../../images/07-schemes-and-special-contracts/u45-payroll-officer/4-special-regimes-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-23-special-regimes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-23-special-regimes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-23-special-regimes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-23-special-regimes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-23-special-regimes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-23-special-regimes-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-23-special-regimes-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-23-special-regimes-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contract | F9 contract | name and dates | no | yes |
| Person | E-F13-18 employee | name | no | yes |
| Regime | E-F13-18 regime | performer, farm worker | yes | yes |
| Collector | E-F13-18 collector | the regime's body | no (from the regime) | yes |
| Declaration | E-F13-09 state | due date, filed, accepted, returned | no | no |
| Exemption | computed | applied or not, with the reason | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Compute | contract panel | payroll officer | payslips computed |
| File | list | payroll officer | declarations sent to the regime's body |
| Ask for the number | contract panel | payroll officer | the event producer is asked for the performer number |

## States

- Normal: contracts per regime with pay, declaration due dates and states.
- Empty: "No performer or seasonal contract": shown per tab; it says contracts come from F9.
- Loading: the frame and titles show at once with placeholder rows for the contracts of the period; within 1 second
  (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: a missing performer number, a late simplified declaration with its penalty, or a returned declaration with its
  reason.
- Read-only: the event producer and the farmer see their contracts' states, never other pay; filed declarations are
  read-only.
- Offline: not available offline: filing needs the connectors (T12). D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-18 Special pay regime](../../data/e-f13-18-special-pay-regime.md),
[E-F13-11 Contribution payment](../../data/e-f13-11-contribution-payment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-18 Special pay regime | Active | Badge "Active"; a new record starts here; next: Changed or Ended (UC-F13-22, UC-F13-24); fields editable within the role | U40, U43, U45 | `u40-farmer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-active-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-active-desktop-{light,dark}.png` |
| E-F13-18 Special pay regime | Changed | Badge "Changed"; next: Active (UC-F13-22); fields editable within the role | U40, U43, U45 | `u40-farmer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-changed-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-changed-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-changed-desktop-{light,dark}.png` |
| E-F13-18 Special pay regime | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U40, U43, U45 | `u40-farmer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-ended-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-ended-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-23-special-regimes-e-f13-18-special-pay-regime-ended-desktop-{light,dark}.png` |
| E-F13-11 Contribution payment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U40, U43, U45 | `u40-farmer/s-f13-23-special-regimes-e-f13-11-contribution-payment-active-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-f13-23-special-regimes-e-f13-11-contribution-payment-active-{desktop,phone}-{light,dark}.png`, `u45-payroll-officer/s-f13-23-special-regimes-e-f13-11-contribution-payment-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet with the panel over the list; the event producer and the farmer read the states on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F13-07 Schemes and special contracts](../../flows/fl-f13-07-schemes-and-special-contracts.md)

## Open questions

None.

---

⬅️ [S-F13-22 Special contracts](s-f13-22-special-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-24 Garnishments and advances](../08-deductions-savings-and-leave-pay/s-f13-24-garnishments-and-advances.md)
