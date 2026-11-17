🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-01 See and set up](README.md) › 🖥️ S-F22-21 Currencies

# 🖥️ S-F22-21 Currencies

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Set a provider's currency and see the rates used.

## Entry points

Providers, a provider's prices.

## Wireframe

```text
Provider A, currency [USD v]          Rate source: ECB
-------------------------------------------------------------------------------
Date         Rate     Flag
2026-11-12   0.9200
2026-11-11   0.9188   holiday, previous rate
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-01 step 6, U07 | desktop | ![FL-F22-01 step 6, U07, light](../../images/01-see-and-set-up/u07-administrator/6-currencies-desktop-light.png) | ![FL-F22-01 step 6, U07, dark](../../images/01-see-and-set-up/u07-administrator/6-currencies-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-21-currencies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-21-currencies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-21-currencies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-21-currencies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-21-currencies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-21-currencies-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-21-currencies-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-21-currencies-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Currency | E-F22-04 | ISO code | yes | yes |
| Date, rate | E-F22-14 | date, number | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Set currency | header | administrator | saved |

## States

- Normal: the currency and rates used.
- Empty: "Euro": no conversion.
- Loading: the frame and titles show at once with placeholder rows for the rates; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a price without currency, refused.
- Read-only: accounting reads.
- Offline: not available offline: rates are read online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F22-04 Paid provider](../../data/e-f22-04-paid-provider.md),
[E-F22-03 Provider price list](../../data/e-f22-03-provider-price-list.md),
[E-F22-14 Exchange rate](../../data/e-f22-14-exchange-rate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-04 Paid provider | New | Badge "New"; a new record starts here; next: Paid (UC-F22-04); fields editable within the role | U05, U07 | `u05-accounting/s-f22-21-currencies-e-f22-04-paid-provider-new-desktop-{light,dark}.png`, `u07-administrator/s-f22-21-currencies-e-f22-04-paid-provider-new-desktop-{light,dark}.png` |
| E-F22-03 Provider price list | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U07 | `u05-accounting/s-f22-21-currencies-e-f22-03-provider-price-list-active-desktop-{light,dark}.png`, `u07-administrator/s-f22-21-currencies-e-f22-03-provider-price-list-active-desktop-{light,dark}.png` |
| E-F22-14 Exchange rate | Published | Badge "Published"; a new record starts here; no other state; fields editable within the role | U05, U07 | `u05-accounting/s-f22-21-currencies-e-f22-14-exchange-rate-published-desktop-{light,dark}.png`, `u07-administrator/s-f22-21-currencies-e-f22-14-exchange-rate-published-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-01 See and set up](../../flows/fl-f22-01-see-and-set-up.md)

## Open questions

None.

---

⬅️ [S-F22-20 Cost assistant](s-f22-20-cost-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-22 Self-hosted compute](s-f22-22-self-hosted-compute.md)
