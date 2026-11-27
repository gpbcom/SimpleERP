🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-01 Set up and profiles](README.md) › 🖥️ S-F17-02 Competitor profile

# 🖥️ S-F17-02 Competitor profile

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Build a profile from registers and filings.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-01 step 2, U12 | desktop | ![FL-F17-01 step 2, U12, light](../../images/01-set-up-and-profiles/u12-marketing/2-profile-desktop-light.png) | ![FL-F17-01 step 2, U12, dark](../../images/01-set-up-and-profiles/u12-marketing/2-profile-desktop-dark.png) |
| FL-F17-01 step 2, U12 | phone | ![FL-F17-01 step 2, U12, light](../../images/01-set-up-and-profiles/u12-marketing/2-profile-phone-light.png) | ![FL-F17-01 step 2, U12, dark](../../images/01-set-up-and-profiles/u12-marketing/2-profile-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-02-competitor-profile-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-02-competitor-profile-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-02-competitor-profile-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-02-competitor-profile-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-02-competitor-profile-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-02-competitor-profile-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-02-competitor-profile-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-02-competitor-profile-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: identity, size, accounts, officers and sites, each fact with its source and date.
- Empty: "No fact yet": the button to fetch registers and filings.
- Loading: the frame and titles show at once with placeholder rows for the profile; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: facts are read-only; only the followed signals change.
- Offline: not available offline: registers are read on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-01 Competitor](../../data/e-f17-01-competitor.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-01 Competitor | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U12 | `u12-marketing/s-f17-02-competitor-profile-e-f17-01-competitor-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F17-01 Set up and profiles](../../flows/fl-f17-01-set-up-and-profiles.md)

## Open questions

None.

---

⬅️ [S-F17-01 Competitors](s-f17-01-competitors.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-03 Products and prices](../02-collect-signals/s-f17-03-products-and-prices.md)
