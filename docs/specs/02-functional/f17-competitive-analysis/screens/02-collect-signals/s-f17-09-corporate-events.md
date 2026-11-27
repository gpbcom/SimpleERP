🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-02 Collect signals](README.md) › 🖥️ S-F17-09 Corporate events

# 🖥️ S-F17-09 Corporate events

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Follow funding, deals and legal events.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-02 step 7, U13 | desktop | ![FL-F17-02 step 7, U13, light](../../images/02-collect-signals/u13-owner/7-events-desktop-light.png) | ![FL-F17-02 step 7, U13, dark](../../images/02-collect-signals/u13-owner/7-events-desktop-dark.png) |
| FL-F17-02 step 7, U13 | phone | ![FL-F17-02 step 7, U13, light](../../images/02-collect-signals/u13-owner/7-events-phone-light.png) | ![FL-F17-02 step 7, U13, dark](../../images/02-collect-signals/u13-owner/7-events-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-09-corporate-events-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-09-corporate-events-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-09-corporate-events-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-09-corporate-events-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-09-corporate-events-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-09-corporate-events-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-09-corporate-events-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-09-corporate-events-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: funding, acquisitions and legal events with their sources.
- Empty: "No event found".
- Loading: the frame and titles show at once with placeholder rows for the events; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: read-only facts.
- Offline: not available offline: events are read on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-08 Mention](../../data/e-f17-08-mention.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-08 Mention | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f17-09-corporate-events-e-f17-08-mention-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F17-02 Collect signals](../../flows/fl-f17-02-collect-signals.md)

## Open questions

None.

---

⬅️ [S-F17-08 News](s-f17-08-news.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-10 Data providers](../01-set-up-and-profiles/s-f17-10-data-providers.md)
