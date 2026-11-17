🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-08 Credits, SaaS subscriptions, carbon and routing](README.md) › 🖥️ S-F22-28 SaaS subscriptions

# 🖥️ S-F22-28 SaaS subscriptions

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every subscription, its seats and its
  renewal.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the costs, the allocation and the invoices.

## Purpose

Keep the company's software subscriptions, see unused seats and decide before each renewal.

## Entry points

Platform costs › SaaS subscriptions; a seat warning; the cost screen.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| SaaS subscriptions                              Active 24   Renewals in 30 days 3     [+ Add] |
|---------------------------------------------------------------------------------------------|
| TOOL         SEATS PAID  SEATS USED  PRICE/SEAT  RENEWS      NOTICE BY    STATE              |
| Design tool  20          14          12 EUR      2027-01-31  2026-12-31   Renewal near       |
| Mail suite   40          39          6 EUR       2027-03-01  2027-02-01   Active             |
| [Reduce seats] [Cancel] [Confirm renewal] [Open invoices]                                    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-08 step 2, U07 | desktop | ![FL-F22-08 step 2, U07, light](../../images/08-credits-saas-and-carbon/u07-administrator/2-saas-subscriptions-desktop-light.png) | ![FL-F22-08 step 2, U07, dark](../../images/08-credits-saas-and-carbon/u07-administrator/2-saas-subscriptions-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-28-saas-subscriptions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-28-saas-subscriptions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-28-saas-subscriptions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-28-saas-subscriptions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-28-saas-subscriptions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-28-saas-subscriptions-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-28-saas-subscriptions-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-28-saas-subscriptions-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tool | E-F22-20 tool | text | yes | yes |
| Seats paid and used | E-F22-20 seats | two numbers | paid yes, used by the connection | yes |
| Price per seat | E-F22-20 price | amount with currency | yes | yes |
| Renews and notice by | E-F22-20 dates | two dates | yes | yes |
| Allocation | E-F22-20 allocation | department or project | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add | header | accounting, administrator | records a subscription |
| Reduce seats | row | administrator | records the new number of seats |
| Cancel | row | administrator | records the cancellation before the notice date |
| Confirm renewal | row | administrator | sets the next renewal date |

## States

- Normal: the subscriptions with seats, price, renewal, notice date and state.
- Empty: No subscription yet, with Add and a short note on how to read seats from a connected tool.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a tool whose
  seats cannot be read shows the last known figure and its date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F22-20 SaaS subscription](../../data/e-f22-20-saas-subscription.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-20 SaaS subscription | Active | Badge "Active"; a new record starts here; next: Renewal near or Cancelled (BR-F22-19, UC-F22-28); fields editable within the role | U07, U05 | `u07-administrator/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-active-desktop-{light,dark}.png`, `u05-accounting/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-active-desktop-{light,dark}.png` |
| E-F22-20 SaaS subscription | Renewal near | Badge "Renewal near"; next: Active or Cancelled (UC-F22-28); fields editable within the role | U07, U05 | `u07-administrator/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-renewal-near-desktop-{light,dark}.png`, `u05-accounting/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-renewal-near-desktop-{light,dark}.png` |
| E-F22-20 SaaS subscription | Cancelled | Badge "Cancelled"; next: Ended (UC-F22-28); fields editable within the role | U07, U05 | `u07-administrator/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-cancelled-desktop-{light,dark}.png`, `u05-accounting/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-cancelled-desktop-{light,dark}.png` |
| E-F22-20 SaaS subscription | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U07, U05 | `u07-administrator/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-ended-desktop-{light,dark}.png`, `u05-accounting/s-f22-28-saas-subscriptions-e-f22-20-saas-subscription-ended-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F22-08](../../flows/fl-f22-08-credits-saas-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F22-27 Credit packs](s-f22-27-credit-packs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-29 Compute carbon](s-f22-29-compute-carbon.md)
