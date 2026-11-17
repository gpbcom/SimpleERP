🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-05 Benchmark additions](README.md) › 🖥️ S-F6-14 Usage billing

# 🖥️ S-F6-14 Usage billing

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Bill usage, commitments and milestones.

## Entry points

Customers and sales in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-05 step 4, U05 | desktop | ![FL-F6-05 step 4, U05, light](../../images/05-benchmark-additions/u05-accounting/4-usage-billing-desktop-light.png) | ![FL-F6-05 step 4, U05, dark](../../images/05-benchmark-additions/u05-accounting/4-usage-billing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-14-usage-billing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-14-usage-billing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-14-usage-billing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-14-usage-billing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-14-usage-billing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-14-usage-billing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f06-14-usage-billing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f06-14-usage-billing-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Bill usage, commitments and milestones, as the wireframe shows.
- Empty: No usage record yet, with Import usage.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-10 Rate plan and meter](../../data/e-f06-10-rate-plan-and-meter.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-10 Rate plan and meter | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U05 | `u03-sales/s-f06-14-usage-billing-e-f06-10-rate-plan-and-meter-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-14-usage-billing-e-f06-10-rate-plan-and-meter-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F6-05 Benchmark additions](../../flows/fl-f06-05-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F6-13 Rentals](s-f06-13-rentals.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-15 Account](../06-accounts-and-credit/s-f06-15-account.md)
