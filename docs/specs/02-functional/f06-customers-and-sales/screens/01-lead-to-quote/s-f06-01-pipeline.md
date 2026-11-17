🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F6-01 Lead to quote](README.md) › 🖥️ S-F6-01 Pipeline

# 🖥️ S-F6-01 Pipeline

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Manage the pipeline and forecast.

## Entry points

Sales in the menu; the portal for customers.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-01 step 2, U03 | desktop | ![FL-F6-01 step 2, U03, light](../../images/01-lead-to-quote/u03-sales/2-pipeline-desktop-light.png) | ![FL-F6-01 step 2, U03, dark](../../images/01-lead-to-quote/u03-sales/2-pipeline-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-01-pipeline-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-01-pipeline-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-01-pipeline-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-01-pipeline-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-01-pipeline-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-01-pipeline-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-01-pipeline-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-01-pipeline-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use cases' main flows.

## States

- Normal: Manage the pipeline and forecast, as the wireframe shows.
- Empty: No opportunity yet, with New opportunity.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: sent, signed or posted documents, changed only by a new version, a credit note or an amendment.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F6-02 Opportunity](../../data/e-f06-02-opportunity.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-02 Opportunity | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f06-01-pipeline-e-f06-02-opportunity-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f06-01-pipeline-e-f06-02-opportunity-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone; quotes on a phone at the customer's site.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F6-01 Lead to quote](../../flows/fl-f06-01-lead-to-quote.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F6-02 Lead](s-f06-02-lead.md)
