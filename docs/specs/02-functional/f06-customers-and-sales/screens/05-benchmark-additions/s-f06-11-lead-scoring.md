🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-05 Benchmark additions](README.md) › 🖥️ S-F6-11 Lead scoring

# 🖥️ S-F6-11 Lead scoring

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Score, assign and enrich leads.

## Entry points

Customers and sales in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-05 step 1, U03 | desktop | ![FL-F6-05 step 1, U03, light](../../images/05-benchmark-additions/u03-sales/1-lead-scoring-desktop-light.png) | ![FL-F6-05 step 1, U03, dark](../../images/05-benchmark-additions/u03-sales/1-lead-scoring-desktop-dark.png) |
| FL-F6-05 step 1, U03 | phone | ![FL-F6-05 step 1, U03, light](../../images/05-benchmark-additions/u03-sales/1-lead-scoring-phone-light.png) | ![FL-F6-05 step 1, U03, dark](../../images/05-benchmark-additions/u03-sales/1-lead-scoring-phone-dark.png) |
| FL-F6-05 step 1, U03 | tablet | ![FL-F6-05 step 1, U03, light](../../images/05-benchmark-additions/u03-sales/1-lead-scoring-tablet-light.png) | ![FL-F6-05 step 1, U03, dark](../../images/05-benchmark-additions/u03-sales/1-lead-scoring-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-11-lead-scoring-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-11-lead-scoring-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-11-lead-scoring-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-11-lead-scoring-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-11-lead-scoring-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-11-lead-scoring-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-11-lead-scoring-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-11-lead-scoring-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Score, assign and enrich leads, as the wireframe shows.
- Empty: No scoring rule yet, with Add a rule.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-20 Lead](../../data/e-f06-20-lead.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-20 Lead | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f06-11-lead-scoring-e-f06-20-lead-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f06-11-lead-scoring-e-f06-20-lead-active-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F6-10 Price lists](../01-lead-to-quote/s-f06-10-price-lists.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-12 Product configurator](s-f06-12-product-configurator.md)
