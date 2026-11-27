🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛍️ [F11 Online shop (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F11-01 Build the shop](README.md) › 🖥️ S-F11-01 Website editor

# 🖥️ S-F11-01 Website editor

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Build and design the website.

## Entry points

Online shop in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F11-01 step 1, U12 | desktop | ![FL-F11-01 step 1, U12, light](../../images/01-build-the-shop/u12-marketing/1-website-editor-desktop-light.png) | ![FL-F11-01 step 1, U12, dark](../../images/01-build-the-shop/u12-marketing/1-website-editor-desktop-dark.png) |
| FL-F11-01 step 1, U12 | phone | ![FL-F11-01 step 1, U12, light](../../images/01-build-the-shop/u12-marketing/1-website-editor-phone-light.png) | ![FL-F11-01 step 1, U12, dark](../../images/01-build-the-shop/u12-marketing/1-website-editor-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f11-01-website-editor-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f11-01-website-editor-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f11-01-website-editor-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f11-01-website-editor-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f11-01-website-editor-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f11-01-website-editor-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f11-01-website-editor-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f11-01-website-editor-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Build and design the website, as the wireframe shows.
- Empty: No page yet, with New page.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: placed orders for the shopper; published pages for non-editors.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F11-02 Web page](../../data/e-f11-02-web-page.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F11-02 Web page | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F11-01); fields editable within the role | U07, U12 | `u07-administrator/s-f11-01-website-editor-e-f11-02-web-page-draft-desktop-{light,dark}.png`, `u12-marketing/s-f11-01-website-editor-e-f11-02-web-page-draft-{desktop,phone}-{light,dark}.png` |
| E-F11-02 Web page | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U07, U12 | `u07-administrator/s-f11-01-website-editor-e-f11-02-web-page-published-desktop-{light,dark}.png`, `u12-marketing/s-f11-01-website-editor-e-f11-02-web-page-published-{desktop,phone}-{light,dark}.png` |

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

- [FL-F11-01 Build the shop](../../flows/fl-f11-01-build-the-shop.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F11-02 Catalogue](s-f11-02-catalogue.md)
