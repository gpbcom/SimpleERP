🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-17 IP portfolio

# 🖥️ S-F15-17 IP portfolio

**Status:** ✅ specified

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the rights, their dates and their costs.

## Purpose

List the company's rights with their renewal dates and make sure none lapses.

## Entry points

Administration › Company records › IP portfolio; the compliance calendar.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| IP portfolio                           Rights 14   Renewing in 90 days 2   Lapsed 0   [+ Add]|
|---------------------------------------------------------------------------------------------|
| RIGHT           TYPE        COUNTRIES    FILED       RENEWS       FEE      STATE            |
| Verdier         Trademark   FR, ES       2016-03-10  2026-03-10   250      Renewal due      |
| Verdier Garden  Design      EU          2020-06-01  2025-06-01   120      Registered       |
| verdier.example Domain      -           2018-03-02  2027-03-02   15       Registered       |
| [Renew] [Let go] [Sell or license]                                                          |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 6, U36 | desktop | ![FL-F15-07 step 6, U36, light](../../images/07-equity-contracts-and-disputes/u36-professional/6-ip-portfolio-desktop-light.png) | ![FL-F15-07 step 6, U36, dark](../../images/07-equity-contracts-and-disputes/u36-professional/6-ip-portfolio-desktop-dark.png) |
| FL-F15-07 step 6, U36 | phone | ![FL-F15-07 step 6, U36, light](../../images/07-equity-contracts-and-disputes/u36-professional/6-ip-portfolio-phone-light.png) | ![FL-F15-07 step 6, U36, dark](../../images/07-equity-contracts-and-disputes/u36-professional/6-ip-portfolio-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-17-ip-portfolio-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-17-ip-portfolio-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-17-ip-portfolio-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-17-ip-portfolio-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-17-ip-portfolio-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-17-ip-portfolio-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-17-ip-portfolio-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-17-ip-portfolio-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Right | E-F15-20 name, type | text | yes | yes |
| Countries | E-F15-20 countries | list | yes | yes |
| Filed and registered | E-F15-20 dates | two dates | yes | yes |
| Renewal date and fee | E-F15-20 renewal | date and amount | yes | yes |
| State | E-F15-20 state | badge | by actions | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add right | header | professional | a right is created with its dates |
| Renew | row | professional | records the payment and the next renewal date |
| Let go | row | professional, owner | the right is marked Lapsed on purpose |
| Sell or license | row | professional, owner | records the buyer or licensee and the date |

## States

- Normal: the rights with type, countries, renewal date and state.
- Empty: No right yet, with Add the company's first right.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing date
  shows which fact is needed.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-20 IP right](../../data/e-f15-20-ip-right.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-20 IP right | Filed | Badge "Filed"; a new record starts here; next: Registered or Refused (UC-F15-19); fields editable within the role | U36 | `u36-professional/s-f15-17-ip-portfolio-e-f15-20-ip-right-filed-{desktop,phone}-{light,dark}.png` |
| E-F15-20 IP right | Registered | Badge "Registered"; next: Due or Sold (BR-F15-23, UC-F15-19); fields editable within the role | U36 | `u36-professional/s-f15-17-ip-portfolio-e-f15-20-ip-right-registered-{desktop,phone}-{light,dark}.png` |
| E-F15-20 IP right | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U36 | `u36-professional/s-f15-17-ip-portfolio-e-f15-20-ip-right-refused-{desktop,phone}-{light,dark}.png` |
| E-F15-20 IP right | Due | Badge "Due"; next: Registered or Lapsed (UC-F15-19); fields editable within the role | U36 | `u36-professional/s-f15-17-ip-portfolio-e-f15-20-ip-right-due-{desktop,phone}-{light,dark}.png` |
| E-F15-20 IP right | Lapsed | Badge "Lapsed"; final: read-only, no next state; the history shows how it got here | U36 | `u36-professional/s-f15-17-ip-portfolio-e-f15-20-ip-right-lapsed-{desktop,phone}-{light,dark}.png` |
| E-F15-20 IP right | Sold | Badge "Sold"; final: read-only, no next state; the history shows how it got here | U36 | `u36-professional/s-f15-17-ip-portfolio-e-f15-20-ip-right-sold-{desktop,phone}-{light,dark}.png` |

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

- [FL-F15-07](../../flows/fl-f15-07-equity-contracts-and-disputes.md)

## Open questions

None.

---

⬅️ [S-F15-16 Shareholder meetings](s-f15-16-shareholder-meetings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-18 Litigation](s-f15-18-litigation.md)
