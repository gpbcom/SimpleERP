🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-03 Citizen services](README.md) › 🖥️ S-SC20-12 Council decisions

# 🖥️ S-SC20-12 Council decisions

**Status:** 🔄 waiting for the owner

## Personas

- [U55 Elected official](../../../../01-users/personas/u55-elected-official.md): the decisions to sign, publish and
  transmit, with their dates.

## Purpose

Sign, post, publish and transmit the council's decisions and show when each is enforceable.

## Entry points

Public bodies › Council decisions; an adopted deliberation.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Council decisions                                          [Sign] [Publish] [Transmit]           |
| Decision   Kind           Signed    Posted    Transmitted   Enforceable   State                  |
| D-2027-31  Deliberation   10 Mar    11 Mar    11 Mar        11 Mar        Enforceable            |
| D-2027-32  Mayor's order  12 Mar    12 Mar    -             -             Published              |
| D-2027-33  Deliberation   -         -         -             -             Prepared               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-03 step 4, U55 | desktop | ![FL-SC20-03 step 4, U55, light](../../images/03-citizen-services/u55-elected-official/4-council-decisions-desktop-light.png) | ![FL-SC20-03 step 4, U55, dark](../../images/03-citizen-services/u55-elected-official/4-council-decisions-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-12-council-decisions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-12-council-decisions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-12-council-decisions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-12-council-decisions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-12-council-decisions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-12-council-decisions-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-12-council-decisions-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-12-council-decisions-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind | E-SC20-10 kind | deliberation, mayor's order, decision | yes while Prepared | yes |
| Text | E-SC20-10 text | document | yes while Prepared | yes |
| Signed on | E-SC20-10 signed | date | no | yes to publish |
| Posted on | E-SC20-10 posted | date | no | no |
| Transmitted on | E-SC20-10 transmitted | date and receipt | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sign | row | elected official | the decision is signed |
| Publish | row | elected official | the decision is posted on the website and the register |
| Transmit | row | elected official | the decision is sent to the prefecture |

## States

- Normal: the decisions with kind, signature, posting, transmission, enforceable date and state.
- Empty: No decision yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a transmission
  failed, a text unsigned, with the decision named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-10 Council decision](../../data/e-sc20-10-council-decision.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-10 Council decision | Prepared | Badge "Prepared"; a new record starts here; next: Published (BR-SC20-12); fields editable within the role | U55 | `u55-elected-official/s-sc20-12-council-decisions-e-sc20-10-council-decision-prepared-desktop-{light,dark}.png` |
| E-SC20-10 Council decision | Published | Badge "Published"; next: Enforceable or Withdrawn (BR-SC20-12, UC-SC20-12); fields editable within the role | U55 | `u55-elected-official/s-sc20-12-council-decisions-e-sc20-10-council-decision-published-desktop-{light,dark}.png` |
| E-SC20-10 Council decision | Enforceable | Badge "Enforceable"; next: Withdrawn (UC-SC20-12); fields editable within the role | U55 | `u55-elected-official/s-sc20-12-council-decisions-e-sc20-10-council-decision-enforceable-desktop-{light,dark}.png` |
| E-SC20-10 Council decision | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U55 | `u55-elected-official/s-sc20-12-council-decisions-e-sc20-10-council-decision-withdrawn-desktop-{light,dark}.png` |

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

- [FL-SC20-03 Citizen services](../../flows/fl-sc20-03-citizen-services.md)

## Open questions

None.

---

⬅️ [S-SC20-11 Public payments](s-sc20-11-public-payments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-13 Grades and steps](../04-public-hr-and-pay/s-sc20-13-grades-and-steps.md)
