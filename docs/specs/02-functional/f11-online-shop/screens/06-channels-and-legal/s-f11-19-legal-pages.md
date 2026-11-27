🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-06 Channels and legal pages](README.md) › 🖥️ S-F11-19 Legal pages

# 🖥️ S-F11-19 Legal pages

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Publish the legal pages.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-06 step 2, U07 | desktop | ![FL-F11-06 step 2, U07, light](../../images/06-channels-and-legal/u07-administrator/2-picking-desktop-light.png) | ![FL-F11-06 step 2, U07, dark](../../images/06-channels-and-legal/u07-administrator/2-picking-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-19-legal-pages-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-19-legal-pages-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-19-legal-pages-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-19-legal-pages-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-19-legal-pages-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-19-legal-pages-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f11-19-legal-pages-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f11-19-legal-pages-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Publish the legal pages, as the wireframe shows.
- Empty: No legal page yet, with Generate the legal pages.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-14 Legal page](../../data/e-f11-14-legal-page.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-14 Legal page | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U12 | `u07-administrator/s-f11-19-legal-pages-e-f11-14-legal-page-active-desktop-{light,dark}.png`, `u12-marketing/s-f11-19-legal-pages-e-f11-14-legal-page-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F11-06 Channels and legal pages](../../flows/fl-f11-06-channels-and-legal.md)

## Open questions

None.

---

⬅️ [S-F11-18 Channels](s-f11-18-channels.md) · ⬆️ [Up](README.md) ·
➡️ [S-F11-20 Shop assistant](../05-grow-the-shop/s-f11-20-shop-assistant.md)
