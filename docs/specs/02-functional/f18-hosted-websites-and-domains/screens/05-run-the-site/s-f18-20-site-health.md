🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F18-05 Run the site](README.md) › 🖥️ S-F18-20 Site health

# 🖥️ S-F18-20 Site health

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Watch uptime, renewals and expiry.

## Entry points

Hosted websites and domains in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F18-05 step 2, U48 | desktop | ![FL-F18-05 step 2, U48, light](../../images/05-run-the-site/u48-hosting-engineer/2-health-desktop-light.png) | ![FL-F18-05 step 2, U48, dark](../../images/05-run-the-site/u48-hosting-engineer/2-health-desktop-dark.png) |
| FL-F18-05 step 2, U48 | phone | ![FL-F18-05 step 2, U48, light](../../images/05-run-the-site/u48-hosting-engineer/2-health-phone-light.png) | ![FL-F18-05 step 2, U48, dark](../../images/05-run-the-site/u48-hosting-engineer/2-health-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f18-20-site-health-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f18-20-site-health-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f18-20-site-health-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f18-20-site-health-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f18-20-site-health-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f18-20-site-health-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f18-20-site-health-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f18-20-site-health-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: uptime, domain renewals and certificates with their dates.
- Empty: "No site live yet".
- Loading: the frame and titles show at once with placeholder rows for the health; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads.
- Offline: The last status loaded stays visible with its time. Nothing else is queued: D38 keeps only today's schedule,
  time and intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F18-12 Uptime event](../../data/e-f18-12-uptime-event.md),
[E-F18-07 Domain](../../data/e-f18-07-domain.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F18-12 Uptime event | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-f18-20-site-health-e-f18-12-uptime-event-recorded-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f18-20-site-health-e-f18-12-uptime-event-recorded-{desktop,phone}-{light,dark}.png` |
| E-F18-07 Domain | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U48 | `u07-administrator/s-f18-20-site-health-e-f18-07-domain-active-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f18-20-site-health-e-f18-07-domain-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F18-05 Run the site](../../flows/fl-f18-05-run-the-site.md)

## Open questions

None.

---

⬅️ [S-F18-19 Shop link](../01-build-the-site/s-f18-19-shop-link.md) · ⬆️ [Up](README.md) ·
➡️ [S-F18-21 Blog](../06-content-and-search/s-f18-21-blog.md)
