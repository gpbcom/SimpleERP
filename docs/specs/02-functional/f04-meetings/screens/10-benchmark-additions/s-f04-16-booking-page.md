🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-10 Benchmark additions](README.md) › 🖥️ S-F4-16 Booking page

# 🖥️ S-F4-16 Booking page

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Let customers book appointments.

## Entry points

Meetings in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-10 step 2, U09 | phone | ![FL-F4-10 step 2, U09, light](../../images/10-benchmark-additions/u09-customer/2-booking-phone-light.png) | ![FL-F4-10 step 2, U09, dark](../../images/10-benchmark-additions/u09-customer/2-booking-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/10-benchmark-additions/u09-customer/e1-slot-taken-phone-light.png) | ![Error E1, U09, dark](../../images/10-benchmark-additions/u09-customer/e1-slot-taken-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f04-16-booking-page-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f04-16-booking-page-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f04-16-booking-page-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f04-16-booking-page-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f04-16-booking-page-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f04-16-booking-page-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-16-booking-page-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-16-booking-page-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Let customers book appointments, as the wireframe shows.
- Empty: no free slot in the coming weeks: the page says so and offers a call-back request.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a booked slot, which the customer changes through its link.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F4-10 Benchmark additions](../../flows/fl-f04-10-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F4-15 Chat](s-f04-15-chat.md) · ⬆️ [Up](README.md) · ➡️ [S-F4-17 Call routing](s-f04-17-call-routing.md)
