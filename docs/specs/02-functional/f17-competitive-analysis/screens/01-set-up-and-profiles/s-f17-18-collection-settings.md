🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-01 Set up and profiles](README.md) › 🖥️ S-F17-18 Collection settings

# 🖥️ S-F17-18 Collection settings

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Set lawful collection rules.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-01 step 4, U07 | desktop | ![FL-F17-01 step 4, U07, light](../../images/01-set-up-and-profiles/u07-administrator/4-rules-desktop-light.png) | ![FL-F17-01 step 4, U07, dark](../../images/01-set-up-and-profiles/u07-administrator/4-rules-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/01-set-up-and-profiles/u07-administrator/e1-rule-below-pack-desktop-light.png) | ![Error E1, U07, dark](../../images/01-set-up-and-profiles/u07-administrator/e1-rule-below-pack-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-18-collection-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-18-collection-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-18-collection-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-18-collection-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-18-collection-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-18-collection-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f17-18-collection-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f17-18-collection-settings-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: sources with their rules, rates and retention.
- Empty: "No source yet".
- Loading: the frame and titles show at once with placeholder rows for the sources; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads; the administrator edits.
- Offline: not available offline: rules are kept on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F17-15 Collection rule](../../data/e-f17-15-collection-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-15 Collection rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f17-18-collection-settings-e-f17-15-collection-rule-active-desktop-{light,dark}.png` |

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

⬅️ [S-F17-17 Market shares](../03-analyse-and-arm-sales/s-f17-17-market-shares.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-19 Access](../04-alerts-and-sharing/s-f17-19-access.md)
