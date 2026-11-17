🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-03 Analyse and arm sales](README.md) › 🖥️ S-F17-13 Battle cards

# 🖥️ S-F17-13 Battle cards

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Prepare battle cards for sales.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-03 step 3, U03 | desktop | ![FL-F17-03 step 3, U03, light](../../images/03-analyse-and-arm-sales/u03-sales/3-battle-card-desktop-light.png) | ![FL-F17-03 step 3, U03, dark](../../images/03-analyse-and-arm-sales/u03-sales/3-battle-card-desktop-dark.png) |
| FL-F17-03 step 3, U03 | phone | ![FL-F17-03 step 3, U03, light](../../images/03-analyse-and-arm-sales/u03-sales/3-battle-card-phone-light.png) | ![FL-F17-03 step 3, U03, dark](../../images/03-analyse-and-arm-sales/u03-sales/3-battle-card-phone-dark.png) |
| FL-F17-03 step 3, U03 | tablet | ![FL-F17-03 step 3, U03, light](../../images/03-analyse-and-arm-sales/u03-sales/3-battle-card-tablet-light.png) | ![FL-F17-03 step 3, U03, dark](../../images/03-analyse-and-arm-sales/u03-sales/3-battle-card-tablet-dark.png) |
| Error E1, U03 | desktop | ![Error E1, U03, light](../../images/07-sales-enablement/u03-sales/e1-battle-cards-refused-desktop-light.png) | ![Error E1, U03, dark](../../images/07-sales-enablement/u03-sales/e1-battle-cards-refused-desktop-dark.png) |
| Error E1, U03 | phone | ![Error E1, U03, light](../../images/07-sales-enablement/u03-sales/e1-battle-cards-refused-phone-light.png) | ![Error E1, U03, dark](../../images/07-sales-enablement/u03-sales/e1-battle-cards-refused-phone-dark.png) |
| Error E1, U03 | tablet | ![Error E1, U03, light](../../images/07-sales-enablement/u03-sales/e1-battle-cards-refused-tablet-light.png) | ![Error E1, U03, dark](../../images/07-sales-enablement/u03-sales/e1-battle-cards-refused-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-13-battle-cards-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-13-battle-cards-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-13-battle-cards-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-13-battle-cards-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-13-battle-cards-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-13-battle-cards-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-13-battle-cards-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-13-battle-cards-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: one card per competitor with strengths, traps, answers, the date and pending proposals from call topics.
- Empty: "No battle card yet": the button to generate one.
- Loading: the frame and titles show at once with placeholder rows for the cards; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: sales read cards; marketing edits and approves proposals.
- Offline: Cards last opened stay readable on the phone before a call; updates need the network. Nothing else is queued:
  D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost and the
  actions come back with it.

Shown entities (VD-15): [E-F17-20 Call topic signal](../../data/e-f17-20-call-topic-signal.md),
[E-F17-11 Battle card](../../data/e-f17-11-battle-card.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-20 Call topic signal | Counted | Badge "Counted"; a new record starts here; next: Used or Dismissed (UC-F17-13, UC-F17-24); fields editable within the role | U02, U03 | `u02-manager/s-f17-13-battle-cards-e-f17-20-call-topic-signal-counted-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f17-13-battle-cards-e-f17-20-call-topic-signal-counted-{desktop,phone,tablet}-{light,dark}.png` |
| E-F17-20 Call topic signal | Used | Badge "Used"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f17-13-battle-cards-e-f17-20-call-topic-signal-used-{desktop,phone,tablet}-{light,dark}.png` |
| E-F17-20 Call topic signal | Dismissed | Badge "Dismissed"; final: read-only, no next state; the history shows how it got here | U02, U03 | `u02-manager/s-f17-13-battle-cards-e-f17-20-call-topic-signal-dismissed-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f17-13-battle-cards-e-f17-20-call-topic-signal-dismissed-{desktop,phone,tablet}-{light,dark}.png` |
| E-F17-11 Battle card | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U03 | `u02-manager/s-f17-13-battle-cards-e-f17-11-battle-card-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f17-13-battle-cards-e-f17-11-battle-card-active-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-F17-12 SWOT and positioning](s-f17-12-swot-and-positioning.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-14 Win and loss](s-f17-14-win-and-loss.md)
