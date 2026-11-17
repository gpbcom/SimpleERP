🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-09 Compliance and carbon](README.md) › 🖥️ S-F7-22 Eco-contributions

# 🖥️ S-F7-22 Eco-contributions

**Status:** ✅ specified

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Set EPR scales and items' packaging, and prepare the declaration.

## Entry points

Purchasing › Eco-contributions.

## Wireframe

```text
+------------------------------------------------------------------+
| Eco-contributions  EPR id FR123456_01ABCD   Packaging scale 2027  |
| Items without a scale: 14                         [Complete]      |
| Declaration Q1 2027: cardboard 8.2 t, plastic 4.2 t = 3,180 EUR   |
|                                     [Export] [Mark declared]      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-09 step 1, U04 | desktop | ![FL-F7-09 step 1, U04, light](../../images/09-compliance-and-carbon/u04-purchasing/1-eco-contributions-desktop-light.png) | ![FL-F7-09 step 1, U04, dark](../../images/09-compliance-and-carbon/u04-purchasing/1-eco-contributions-desktop-dark.png) |
| Error E1, U04 | desktop | ![Error E1, U04, light](../../images/09-compliance-and-carbon/u04-purchasing/e1-eco-contributions-refused-desktop-light.png) | ![Error E1, U04, dark](../../images/09-compliance-and-carbon/u04-purchasing/e1-eco-contributions-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-22-eco-contributions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-22-eco-contributions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-22-eco-contributions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-22-eco-contributions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-22-eco-contributions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-22-eco-contributions-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-22-eco-contributions-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-22-eco-contributions-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Scales, items, declaration | E-F7-18 | scales and weights |

## Actions

| Action | Who | Result |
|---|---|---|
| Export the declaration | purchasing | File for the eco-organisation |

## States

- Normal: set EPR scales and items' packaging, and prepare the declaration.
- Empty: no scale yet: Add the eco-organisation's scale.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: declared periods.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F7-06 Item](../../data/e-f07-06-item.md),
[E-F7-18 Eco-contribution scale](../../data/e-f07-18-eco-contribution-scale.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-06 Item | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-22-eco-contributions-e-f07-06-item-active-desktop-{light,dark}.png` |
| E-F7-18 Eco-contribution scale | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04 | `u04-purchasing/s-f07-22-eco-contributions-e-f07-18-eco-contribution-scale-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-09 Compliance and carbon](../../flows/fl-f07-09-compliance-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F7-21 Stock levels](../03-replenish/s-f07-21-stock-levels.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-23 Dangerous goods](../02-receive-and-store/s-f07-23-dangerous-goods.md)
