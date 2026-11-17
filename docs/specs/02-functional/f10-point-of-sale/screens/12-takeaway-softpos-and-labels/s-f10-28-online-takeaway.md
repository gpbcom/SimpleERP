🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F10-12](README.md) ›
🖥️ S-F10-28 Online takeaway

# 🖥️ S-F10-28 Online takeaway

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): orders and collects, on a phone.
- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md): prepares the orders, on a desktop screen.

## Purpose

Order ahead for a pickup slot, and prepare and hand over takeaway orders.

## Entry points

The shop's takeaway page; the kitchen screen's Online tab; the till's order list.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Online takeaway - Kitchen                  Online orders: ON   [Pause 30 min]   Capacity per slot: 8 |
| ------------------------------------------------------------------------------------------- |
| SLOT    ORDER   CUSTOMER   LINES              STATE            ACTION                       |
| 12:30   41      Sonia M.   2 burgers           Accepted         [Start]                     |
| 12:30   42      Julien R.  1 salad, 1 soup     In preparation   [Ready]                     |
| 12:45   43      Marc D.    3 pizzas            Placed           [Accept] [Refuse]           |
| Slots: 12:30 full   12:45 5 of 8   13:00 2 of 8         Orders today: 17                    |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f10-28-online-takeaway-empty-desktop-{light,dark}.png`,
`s-f10-28-online-takeaway-empty-phone-{light,dark}.png`, `s-f10-28-online-takeaway-loading-desktop-{light,dark}.png`,
`s-f10-28-online-takeaway-loading-phone-{light,dark}.png`, `s-f10-28-online-takeaway-offline-desktop-{light,dark}.png`,
`s-f10-28-online-takeaway-offline-phone-{light,dark}.png`,
`s-f10-28-online-takeaway-read-only-desktop-{light,dark}.png`,
`s-f10-28-online-takeaway-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-12 step 1, U09 | phone | ![FL-F10-12 step 1, U09, light](../../images/12-takeaway-softpos-and-labels/u09-customer/1-online-takeaway-phone-light.png) | ![FL-F10-12 step 1, U09, dark](../../images/12-takeaway-softpos-and-labels/u09-customer/1-online-takeaway-phone-dark.png) |
| FL-F10-12 step 1, U09 | phone | ![FL-F10-12 step 1, U09, light](../../images/12-takeaway-softpos-and-labels/u09-customer/1-online-takeaway-phone-light.png) | ![FL-F10-12 step 1, U09, dark](../../images/12-takeaway-softpos-and-labels/u09-customer/1-online-takeaway-phone-dark.png) |
| Error E1, U09 | phone | ![Error E1, U09, light](../../images/12-takeaway-softpos-and-labels/u09-customer/e1-the-kitchen-is-full-phone-light.png) | ![Error E1, U09, dark](../../images/12-takeaway-softpos-and-labels/u09-customer/e1-the-kitchen-is-full-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f10-28-online-takeaway-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f10-28-online-takeaway-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f10-28-online-takeaway-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f10-28-online-takeaway-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f10-28-online-takeaway-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f10-28-online-takeaway-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-28-online-takeaway-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-28-online-takeaway-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Slot and capacity | E-F10-22 pickup slot, point of sale | time and n of m | capacity only | yes |
| Order lines | E-F10-22 lines | list | customer, before acceptance | yes |
| Payment | E-F10-22 payment | choice | customer | yes |
| Pause | E-F10-01 online orders | switch and minutes | store manager | no |
| State | E-F10-22 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Order | customer page | the customer | an order is placed (UC-F10-29) |
| Accept, Refuse | kitchen row | kitchen staff | the order is accepted or refused |
| Start, Ready | kitchen row | kitchen staff | the order moves on and the customer is told |
| Collected | kitchen row, till | kitchen staff, cashier | the order is handed over |
| Pause | header | kitchen staff, store manager | no slot is offered for the minutes set |

## States

- Normal: the customer's menu and open slots; the kitchen's orders by slot with their state and the capacity.
- Empty: No order for this slot yet: a hint on the slots open and the pause switch.
- Loading: The menu and slots as placeholders, then the capacity.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a full slot or
  a paused kitchen says so ([BR-F10-23](../../business-rules/br-f10-23-online-orders-stay-within-kitchen-capacity.md)).
- Read-only: a closed day: orders shown with no action.
- Offline: The customer cannot order offline. The kitchen screen keeps the orders already received and shows that new
  ones will arrive when the network is back ([BR-F10-06](../../business-rules/br-f10-06-offline-keeps-selling.md)).

Shown entities (VD-15): [E-F10-22 Takeaway order](../../data/e-f10-22-takeaway-order.md),
[E-F10-01 Point of sale](../../data/e-f10-01-point-of-sale.md),
[E-F10-03 Point of sale order](../../data/e-f10-03-point-of-sale-order.md),
[E-F10-13 Preparation ticket](../../data/e-f10-13-preparation-ticket.md),
[E-F11-09 Customer account](../../../f11-online-shop/data/e-f11-09-customer-account.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-22 Takeaway order | Placed | Badge "Placed"; a new record starts here; next: Accepted or Refused or Cancelled (BR-F10-23, UC-F10-29); fields editable within the role | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-placed-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-placed-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | Accepted | Badge "Accepted"; next: In preparation or Cancelled (UC-F10-29); fields editable within the role | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-accepted-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-accepted-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | Refused | Badge "Refused"; final state, read-only | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-refused-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-refused-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | In preparation | Badge "In preparation"; next: Ready (UC-F10-29); fields editable within the role | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-in-preparation-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-in-preparation-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | Ready | Badge "Ready"; next: Collected or Not collected (UC-F10-29); fields editable within the role | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-ready-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-ready-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | Collected | Badge "Collected"; final state, read-only | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-collected-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-collected-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | Cancelled | Badge "Cancelled"; final state, read-only | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-cancelled-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-cancelled-desktop-{light,dark}.png` |
| E-F10-22 Takeaway order | Not collected | Badge "Not collected"; final state, read-only | U09, U19 | `u09-customer/s-f10-28-online-takeaway-e-f10-22-takeaway-order-not-collected-phone-{light,dark}.png`; `u19-kitchen-staff/s-f10-28-online-takeaway-e-f10-22-takeaway-order-not-collected-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

The customer page is a phone page with large buttons; the kitchen screen is a wide screen with one column per slot.

## Accessibility

States are words and sounds; the pickup time is read aloud; touch targets are at least 44 pixels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-12 Takeaway, tap to pay, labels and layaway](../../flows/fl-f10-12-takeaway-softpos-and-labels.md)

## Open questions

None.

---

⬅️ [S-F10-27 Store reports](../11-store-reports/s-f10-27-store-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-29 Tap to pay](s-f10-29-tap-to-pay.md)
