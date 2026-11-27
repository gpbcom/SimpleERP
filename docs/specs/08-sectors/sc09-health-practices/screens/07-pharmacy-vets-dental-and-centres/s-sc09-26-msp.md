🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC09-07 Pharmacy, eyewear, vets, dental and health centres](README.md) ›
🖥️ S-SC09-26 Multi-professional practice

# 🖥️ S-SC09-26 Multi-professional practice

**Status:** ✅ specified

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md): the indicators and the evidence.
- [U36 Professional](../../../../01-users/personas/u36-professional.md): the team's points and the funding.

## Purpose

Follow the indicators of the funding contract, enter the evidence and see the points and the funding of the year.

## Entry points

Health practice › Funding indicators; the practice's dashboard; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| MSP Les Tilleuls: contract 2026                         Points 320 / 400   Funding estimate 38,4 |
| Indicator                         Target   Value    Points   Source                              |
| Patients with a named doctor       90 %    93 %     60       records                             |
| Shared team meetings per year      6       4        20       declared, evidence added            |
| Certified software in use          yes     yes      40       certified module                    |
| Open indicators 3                       [Declare an indicator]   [Confirm the year]              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC09-07 step 6, U33 | desktop | ![FL-SC09-07 step 6, U33, light](../../images/07-pharmacy-vets-dental-and-centres/u33-medical-secretary/6-msp-desktop-light.png) | ![FL-SC09-07 step 6, U33, dark](../../images/07-pharmacy-vets-dental-and-centres/u33-medical-secretary/6-msp-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc09-26-msp-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc09-26-msp-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc09-26-msp-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc09-26-msp-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc09-26-msp-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc09-26-msp-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc09-26-msp-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc09-26-msp-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Indicator | E-SC09-19 indicator | choice | no | yes |
| Target and value | E-SC09-19 target, value | numbers | yes while Open | no |
| Points | E-SC09-19 points | number | no | no |
| Source | E-SC09-19 source | records or declared | no | no |
| Evidence | E-SC09-19 evidence | files | yes while Open | no |
| Funding estimate | E-SC09-19 funding | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Declare an indicator | row | coordinator | a value with its evidence, marked as declared |
| Confirm the year | header | coordinator | the points are confirmed and the funding computed |
| Recompute | header | coordinator | the indicators are recounted from the records |
| Export | header | coordinator | the points as a file for the health insurance |

## States

- Normal: each indicator with target, value, points and source, and the funding estimate.
- Empty: No contract yet, with Add the contract's indicators.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an indicator
  with no source or a confirmation before the year ends, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC09-19 ACI indicator](../../data/e-sc09-19-aci-indicator.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC09-19 ACI indicator | Open | Badge "Open"; a new record starts here; next: Confirmed (BR-SC09-21); fields editable within the role | U33, U36 | `u33-medical-secretary/s-sc09-26-msp-e-sc09-19-aci-indicator-open-desktop-{light,dark}.png`, `u36-professional/s-sc09-26-msp-e-sc09-19-aci-indicator-open-{desktop,phone}-{light,dark}.png` |
| E-SC09-19 ACI indicator | Confirmed | Badge "Confirmed"; next: Paid or Open (UC-SC09-26); fields editable within the role | U33, U36 | `u33-medical-secretary/s-sc09-26-msp-e-sc09-19-aci-indicator-confirmed-desktop-{light,dark}.png`, `u36-professional/s-sc09-26-msp-e-sc09-19-aci-indicator-confirmed-{desktop,phone}-{light,dark}.png` |
| E-SC09-19 ACI indicator | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U33, U36 | `u33-medical-secretary/s-sc09-26-msp-e-sc09-19-aci-indicator-paid-desktop-{light,dark}.png`, `u36-professional/s-sc09-26-msp-e-sc09-19-aci-indicator-paid-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC09-07](../../flows/fl-sc09-07-pharmacy-vets-dental-and-centres.md)

## Open questions

None.

---

⬅️ [S-SC09-25 Health centre](s-sc09-25-health-centre.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-L01 Appointments](../00-lists/s-sc09-l01-appointments.md)
