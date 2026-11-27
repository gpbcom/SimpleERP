🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F10-12](README.md) ›
🖥️ S-F10-29 Tap to pay

# 🖥️ S-F10-29 Tap to pay

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md): takes payments at the counter, on a phone.
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md): takes payments at the table, on a phone.

## Purpose

Take a card or phone payment by tap on the seller's phone.

## Entry points

Mobile till › Pay › Tap to pay; the restaurant's table bill.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Tap to pay                                   Device: Claire's phone      Session 17 open    |
| ------------------------------------------------------------------------------------------- |
| Amount to pay                38.50 EUR       Sale 2043, table 6                             |
|                                                                                             |
|                   Ready to tap                                                              |
|           Hold the card or phone to the back of this phone                                  |
|                                                                                             |
| Accepted card: contactless    [Cancel]    [Use another means]                               |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f10-29-tap-to-pay-empty-desktop-{light,dark}.png`,
`s-f10-29-tap-to-pay-empty-phone-{light,dark}.png`, `s-f10-29-tap-to-pay-loading-desktop-{light,dark}.png`,
`s-f10-29-tap-to-pay-loading-phone-{light,dark}.png`, `s-f10-29-tap-to-pay-offline-desktop-{light,dark}.png`,
`s-f10-29-tap-to-pay-offline-phone-{light,dark}.png`, `s-f10-29-tap-to-pay-read-only-desktop-{light,dark}.png`,
`s-f10-29-tap-to-pay-read-only-phone-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-12 step 2, U17 | phone | ![FL-F10-12 step 2, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-phone-light.png) | ![FL-F10-12 step 2, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-phone-dark.png) |
| FL-F10-12 step 2, U17 | desktop | ![FL-F10-12 step 2, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-desktop-light.png) | ![FL-F10-12 step 2, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-desktop-dark.png) |
| FL-F10-12 step 2, U17 | phone | ![FL-F10-12 step 2, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-phone-light.png) | ![FL-F10-12 step 2, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-phone-dark.png) |
| FL-F10-12 step 2, U17 | tablet | ![FL-F10-12 step 2, U17, light](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-tablet-light.png) | ![FL-F10-12 step 2, U17, dark](../../images/12-takeaway-softpos-and-labels/u17-cashier/2-tap-to-pay-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-29-tap-to-pay-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-29-tap-to-pay-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-29-tap-to-pay-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-29-tap-to-pay-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-29-tap-to-pay-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-29-tap-to-pay-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-29-tap-to-pay-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-29-tap-to-pay-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Amount | sale total | money | no | yes |
| Status | payment result | Ready, Accepted, Declined | no | yes |
| Method and last four digits | payment | text | no | no |
| Device | E-F10-14 device | text | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Cancel | screen | the seller | no payment is started |
| Use another means | screen | the seller | the pay screen of the till opens |
| Retry | declined | the seller | a new tap is asked |
| Send the receipt | accepted | the seller | the receipt goes by email or code |

## States

- Normal: the amount, a Ready to tap prompt and the result as soon as the customer taps.
- Empty: No sale to pay: a hint to open a sale on the mobile till first.
- Loading: Waiting for the provider's answer, with the amount kept on screen.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a decline shows
  the provider's reason in plain words.
- Read-only: a session that is closed: the payments are shown, none can be taken.
- Offline: Not available offline: a payment must be authorised online. The screen says so and offers another means
  ([BR-F10-24](../../business-rules/br-f10-24-tap-to-pay-follows-the-card-terminal-rules-and-the-till-log.md)).

Shown entities (VD-15): [E-F10-04 Till payment](../../data/e-f10-04-till-payment.md),
[E-F10-14 Point of sale device](../../data/e-f10-14-point-of-sale-device.md),
[E-F10-15 Till event log](../../data/e-f10-15-till-event-log.md),
[E-F10-02 Till session](../../data/e-f10-02-till-session.md).

## Responsive behaviour

A full-screen phone prompt with the amount in large type.

## Accessibility

The result is shown in words and read aloud; the PIN pad is the provider's accessible one.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

- [FL-F10-12 Takeaway, tap to pay, labels and layaway](../../flows/fl-f10-12-takeaway-softpos-and-labels.md)

## Open questions

None.

---

⬅️ [S-F10-28 Online takeaway](s-f10-28-online-takeaway.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-30 Shelf labels](s-f10-30-shelf-labels.md)
