🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-05 Facilities, events, camps and rentals](README.md) ›
🖥️ S-SC18-19 Holiday camps

# 🖥️ S-SC18-19 Holiday camps

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the camps, groups, ratios and declaration.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own child's registration.

## Purpose

Create camps, register children with their health sheet, build groups and check the supervision ratio.

## Entry points

Sports and fitness › Camp registrations; the parent's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Camp: Summer multisport, 6 to 17 July                                       Declared             |
| Group      Ages     Children   Animators needed   Assigned   Ratio                               |
| Minis      6 to 7   10         2                  2          ok                                  |
| Juniors    8 to 10  14         2                  1          missing 1                           |
| Declaration  reference D-2026-0412, filed 2026-06-02                                             |
| Registrations 38 of 40   Incomplete 2   Health sheets 36                                         |
| [Register a child]  [Assign an animator]  [Print the day sheet]                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-05 step 3, U13 | desktop | ![FL-SC18-05 step 3, U13, light](../../images/05-facilities-events-camps-and-rentals/u13-owner/3-holiday-camps-desktop-light.png) | ![FL-SC18-05 step 3, U13, dark](../../images/05-facilities-events-camps-and-rentals/u13-owner/3-holiday-camps-desktop-dark.png) |
| FL-SC18-05 step 3, U13 | phone | ![FL-SC18-05 step 3, U13, light](../../images/05-facilities-events-camps-and-rentals/u13-owner/3-holiday-camps-phone-light.png) | ![FL-SC18-05 step 3, U13, dark](../../images/05-facilities-events-camps-and-rentals/u13-owner/3-holiday-camps-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-19-holiday-camps-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-19-holiday-camps-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-19-holiday-camps-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-19-holiday-camps-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-19-holiday-camps-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-19-holiday-camps-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-19-holiday-camps-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-19-holiday-camps-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Camp | E-SC18-15 camp | link | no | yes |
| Child and parent | E-SC18-15 child, parent | names | yes while Registered | yes |
| Health sheet | E-SC18-15 health sheet | form | yes while Registered | yes |
| People allowed to collect | E-SC18-15 collectors | list of names | yes while Registered | yes |
| Group | E-SC18-15 group | choice | yes | no |
| Photo consent | E-SC18-15 photo consent | yes or no | yes while Registered | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Register a child | header | parent, owner | a registration is saved Registered |
| Confirm | registration | owner | the registration becomes Confirmed |
| Check in | registration | animator | the child's arrival is recorded |
| Check out | registration | animator | the child is released to a person on the list |
| Cancel | registration | parent, owner | the registration becomes Cancelled |

## States

- Normal: the camp with its groups, ratios, registrations and declaration.
- Empty: No registration yet, with Register a child.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unmet ratio,
  an undeclared camp or an incomplete registration, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-15 Camp registration](../../data/e-sc18-15-camp-registration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-15 Camp registration | Registered | Badge "Registered"; a new record starts here; next: Confirmed, Waiting or Cancelled (UC-SC18-19); fields editable within the role | U13, U09 | `u13-owner/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-registered-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-registered-phone-{light,dark}.png` |
| E-SC18-15 Camp registration | Confirmed | Badge "Confirmed"; next: Attended or Cancelled (BR-SC18-19, UC-SC18-19); fields editable within the role | U13, U09 | `u13-owner/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-confirmed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-confirmed-phone-{light,dark}.png` |
| E-SC18-15 Camp registration | Waiting | Badge "Waiting"; next: Confirmed (UC-SC18-19); fields editable within the role | U13, U09 | `u13-owner/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-waiting-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-waiting-phone-{light,dark}.png` |
| E-SC18-15 Camp registration | Attended | Badge "Attended"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-attended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-attended-phone-{light,dark}.png` |
| E-SC18-15 Camp registration | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-19-holiday-camps-e-sc18-15-camp-registration-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-05](../../flows/fl-sc18-05-facilities-events-camps-and-rentals.md)

## Open questions

None.

---

⬅️ [S-SC18-18 Tournaments](s-sc18-18-tournaments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-20 Equipment rental](s-sc18-20-equipment-rental.md)
