🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-08 Trials, test instances, partners and themes](README.md) › 🖥️ S-F14-28 Free trials

# 🖥️ S-F14-28 Free trials

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the trials of their company.

## Purpose

Start a trial, see the days left and decide: buy, extend or remove cleanly.

## Entry points

Plugin store › Free trials; a paid plugin's listing; a reminder.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Free trials                                                   2 running       [Browse plugins] |
|---------------------------------------------------------------------------------------------|
| PLUGIN           STARTED     ENDS         DAYS LEFT  PRICE            STATE                  |
| Garden planner   2026-11-01  2026-11-15   1          29 EUR/month     Active                 |
| Route optimiser  2026-10-10  2026-10-24   -          49 EUR/month     Ended, data kept 30 d  |
| [Buy] [Extend] [Uninstall and export]                                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-08 step 2, U07 | desktop | ![FL-F14-08 step 2, U07, light](../../images/08-trials-instances-and-partners/u07-administrator/2-free-trials-desktop-light.png) | ![FL-F14-08 step 2, U07, dark](../../images/08-trials-instances-and-partners/u07-administrator/2-free-trials-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-28-free-trials-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-28-free-trials-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-28-free-trials-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-28-free-trials-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-28-free-trials-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-28-free-trials-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-28-free-trials-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-28-free-trials-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Plugin | E-F14-23 plugin | text | no | yes |
| Start and end | E-F14-23 dates | two dates | once by Extend | yes |
| Days left | E-F14-23 days left | number | no | yes |
| Price | E-F14-04 price plan | amount with period | no | yes |
| State | E-F14-23 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Try free | listing | administrator | starts a trial and installs the plugin |
| Buy | row | administrator | opens the purchase and converts the trial |
| Extend | row | administrator | asks for the one extension the publisher allows |
| Uninstall and export | row | administrator | exports the data and removes the plugin |

## States

- Normal: the company's trials with days left, price and state.
- Empty: No trial yet, with Browse plugins.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused trial
  shows the reason and the purchase option.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F14-23 Trial](../../data/e-f14-23-trial.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-23 Trial | Active | Badge "Active"; a new record starts here; next: Converted, Ended or Removed (UC-F14-30, BR-F14-25); fields editable within the role | U07 | `u07-administrator/s-f14-28-free-trials-e-f14-23-trial-active-desktop-{light,dark}.png` |
| E-F14-23 Trial | Converted | Badge "Converted"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f14-28-free-trials-e-f14-23-trial-converted-desktop-{light,dark}.png` |
| E-F14-23 Trial | Ended | Badge "Ended"; next: Converted or Removed (UC-F14-30, BR-F14-25); fields editable within the role | U07 | `u07-administrator/s-f14-28-free-trials-e-f14-23-trial-ended-desktop-{light,dark}.png` |
| E-F14-23 Trial | Removed | Badge "Removed"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f14-28-free-trials-e-f14-23-trial-removed-desktop-{light,dark}.png` |

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

- [FL-F14-08](../../flows/fl-f14-08-trials-instances-and-partners.md)

## Open questions

None.

---

⬅️ [S-F14-27 Test instances](s-f14-27-test-instances.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-29 Partner directory](s-f14-29-partner-directory.md)
