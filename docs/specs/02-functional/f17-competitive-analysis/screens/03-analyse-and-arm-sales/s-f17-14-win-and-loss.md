🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-03 Analyse and arm sales](README.md) › 🖥️ S-F17-14 Win and loss

# 🖥️ S-F17-14 Win and loss

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Analyse wins and losses.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-03 step 4, U03 | desktop | ![FL-F17-03 step 4, U03, light](../../images/03-analyse-and-arm-sales/u03-sales/4-win-loss-desktop-light.png) | ![FL-F17-03 step 4, U03, dark](../../images/03-analyse-and-arm-sales/u03-sales/4-win-loss-desktop-dark.png) |
| FL-F17-03 step 4, U03 | phone | ![FL-F17-03 step 4, U03, light](../../images/03-analyse-and-arm-sales/u03-sales/4-win-loss-phone-light.png) | ![FL-F17-03 step 4, U03, dark](../../images/03-analyse-and-arm-sales/u03-sales/4-win-loss-phone-dark.png) |
| FL-F17-03 step 4, U03 | tablet | ![FL-F17-03 step 4, U03, light](../../images/03-analyse-and-arm-sales/u03-sales/4-win-loss-tablet-light.png) | ![FL-F17-03 step 4, U03, dark](../../images/03-analyse-and-arm-sales/u03-sales/4-win-loss-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-14-win-and-loss-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-14-win-and-loss-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-14-win-and-loss-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-14-win-and-loss-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-14-win-and-loss-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-14-win-and-loss-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-14-win-and-loss-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-14-win-and-loss-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: deals won and lost per competitor with reasons.
- Empty: "No deal names a competitor yet".
- Loading: the frame and titles show at once with placeholder rows for the deals; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: sales see their own deals; managers their team's.
- Offline: not available offline: deals are read from F6 on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-12 Win-loss record](../../data/e-f17-12-win-loss-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-12 Win-loss record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f17-14-win-and-loss-e-f17-12-win-loss-record-recorded-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f17-14-win-and-loss-e-f17-12-win-loss-record-recorded-{desktop,phone,tablet}-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F17-03 Analyse and arm sales](../../flows/fl-f17-03-analyse-and-arm-sales.md)

## Open questions

None.

---

⬅️ [S-F17-13 Battle cards](s-f17-13-battle-cards.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-15 Alerts](../04-alerts-and-sharing/s-f17-15-alerts.md)
