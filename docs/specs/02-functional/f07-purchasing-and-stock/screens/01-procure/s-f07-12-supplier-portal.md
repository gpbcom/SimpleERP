🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F7-01 Procure](README.md) ›
🖥️ S-F7-12 Supplier portal

# 🖥️ S-F7-12 Supplier portal

**Status:** ✅ specified

## Personas

- [U10 Supplier](../../../../01-users/personas/u10-supplier.md)

## Purpose

Use the supplier portal.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-01 step 4, U10 | phone | ![FL-F7-01 step 4, U10, light](../../images/01-procure/u10-supplier/4-supplier-portal-phone-light.png) | ![FL-F7-01 step 4, U10, dark](../../images/01-procure/u10-supplier/4-supplier-portal-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-12-supplier-portal-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-12-supplier-portal-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-12-supplier-portal-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-12-supplier-portal-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-12-supplier-portal-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-12-supplier-portal-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-12-supplier-portal-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-12-supplier-portal-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Use the supplier portal, as the wireframe shows.
- Empty: No order for this supplier yet, with Contact the buyer.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: an outside user's page served live (D407 keeps portals and website apart from the
  offline-first app); the browser shows that the page cannot be reached.

Shown entities (VD-15): [E-F7-03 Purchase order](../../data/e-f07-03-purchase-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-03 Purchase order | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F7-02); fields editable within the role | U10 | `u10-supplier/s-f07-12-supplier-portal-e-f07-03-purchase-order-draft-phone-{light,dark}.png` |
| E-F7-03 Purchase order | Sent | Badge "Sent"; next: Confirmed (UC-F7-02); fields editable within the role | U10 | `u10-supplier/s-f07-12-supplier-portal-e-f07-03-purchase-order-sent-phone-{light,dark}.png` |
| E-F7-03 Purchase order | Confirmed | Badge "Confirmed"; next: Received (UC-F7-04); fields editable within the role | U10 | `u10-supplier/s-f07-12-supplier-portal-e-f07-03-purchase-order-confirmed-phone-{light,dark}.png` |
| E-F7-03 Purchase order | Received | Badge "Received"; next: Billed (UC-F7-01); fields editable within the role | U10 | `u10-supplier/s-f07-12-supplier-portal-e-f07-03-purchase-order-received-phone-{light,dark}.png` |
| E-F7-03 Purchase order | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U10 | `u10-supplier/s-f07-12-supplier-portal-e-f07-03-purchase-order-billed-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; receipts, picking and counts on phones, offline.

## Accessibility

Labelled controls; quantities and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F7-01 Procure](../../flows/fl-f07-01-procure.md)

## Open questions

None.

---

⬅️ [S-F7-11 Stock analytics](../05-count-trace-and-analyse/s-f07-11-stock-analytics.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-13 Warehouse setup](../03-replenish/s-f07-13-warehouse-setup.md)
