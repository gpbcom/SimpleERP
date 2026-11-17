🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-01 Till session](README.md) › 🖥️ S-F10-01 Till session

# 🖥️ S-F10-01 Till session

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Open and close a till session.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-01 step 2, U17 | desktop | ![FL-F10-01 step 2, U17, light](../../images/01-till-session/u17-cashier/2-open-and-close-desktop-light.png) | ![FL-F10-01 step 2, U17, dark](../../images/01-till-session/u17-cashier/2-open-and-close-desktop-dark.png) |
| FL-F10-01 step 2, U17 | phone | ![FL-F10-01 step 2, U17, light](../../images/01-till-session/u17-cashier/2-open-and-close-phone-light.png) | ![FL-F10-01 step 2, U17, dark](../../images/01-till-session/u17-cashier/2-open-and-close-phone-dark.png) |
| FL-F10-01 step 2, U17 | tablet | ![FL-F10-01 step 2, U17, light](../../images/01-till-session/u17-cashier/2-open-and-close-tablet-light.png) | ![FL-F10-01 step 2, U17, dark](../../images/01-till-session/u17-cashier/2-open-and-close-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/01-till-session/u17-cashier/e1-cash-difference-desktop-light.png) | ![Error E1, U17, dark](../../images/01-till-session/u17-cashier/e1-cash-difference-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/01-till-session/u17-cashier/e1-cash-difference-phone-light.png) | ![Error E1, U17, dark](../../images/01-till-session/u17-cashier/e1-cash-difference-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/01-till-session/u17-cashier/e1-cash-difference-tablet-light.png) | ![Error E1, U17, dark](../../images/01-till-session/u17-cashier/e1-cash-difference-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-01-till-session-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-01-till-session-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-01-till-session-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-01-till-session-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-01-till-session-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-01-till-session-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-01-till-session-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-01-till-session-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Open and close a till session, as the wireframe shows.
- Empty: No session opened today yet, with Open a session.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The till keeps selling, numbering and chaining its sales locally and syncs on reconnect
  ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)); a card terminal that loses its link cancels
  the payment; a warning shows after 24 hours offline.

Shown entities (VD-15): [E-F10-02 Till session](../../data/e-f10-02-till-session.md),
[E-F10-06 Closure](../../data/e-f10-06-closure.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-02 Till session | Open | Badge "Open"; a new record starts here; next: Closing (UC-F10-01); fields editable within the role | U02, U17 | `u02-manager/s-f10-01-till-session-e-f10-02-till-session-open-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-01-till-session-e-f10-02-till-session-open-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-06 Closure | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U17 | `u02-manager/s-f10-01-till-session-e-f10-06-closure-active-{desktop,phone}-{light,dark}.png`, `u17-cashier/s-f10-01-till-session-e-f10-06-closure-active-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F10-01 Till session](../../flows/fl-f10-01-till-session.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F10-02 Till](../02-sell-at-the-counter/s-f10-02-till.md)
