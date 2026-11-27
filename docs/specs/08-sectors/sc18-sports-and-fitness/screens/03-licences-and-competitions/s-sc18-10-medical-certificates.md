🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-03 Licences and competitions](README.md) ›
🖥️ S-SC18-10 Medical certificates

# 🖥️ S-SC18-10 Medical certificates

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the certificate status of their players.

## Purpose

Record each certificate, or for a minor the health questionnaire, keeping only its date, validity and fitness and never
the medical content; show who is covered and flag the ones that end soon
([CR-FR-284](../../../../10-country-packs/france/non-profit/cr-fr-284-sports-licences-and-medical-certificates.md),
[CR-FR-283](../../../../10-country-packs/france/data-protection/cr-fr-283-health-data-outside-care.md)).

## Entry points

Sports and fitness › Medical certificates; a team's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Certificates: U15 football                                              2 not covered            |
| Player       Proof                           Fit   Covers          Valid to      State           |
| Lena T.      health questionnaire (minor)    yes   competition     2027-09-01    Valid           |
| Karim A.     health questionnaire (minor)    yes   training        2027-09-01    Training only   |
| Eva P.       certificate, after an answer    yes   competition     2026-12-05    Ends in 8 days  |
| Tom R.       -                               -     -               -             Expired         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-03 step 2, U53 | phone | ![FL-SC18-03 step 2, U53, light](../../images/03-licences-and-competitions/u53-coach/2-medical-certificates-phone-light.png) | ![FL-SC18-03 step 2, U53, dark](../../images/03-licences-and-competitions/u53-coach/2-medical-certificates-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-10-medical-certificates-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-10-medical-certificates-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-10-medical-certificates-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-10-medical-certificates-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-10-medical-certificates-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-10-medical-certificates-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-10-medical-certificates-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-10-medical-certificates-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-07 member | link | no | yes |
| Date | E-SC18-07 issued on | date | yes while Received | yes |
| Valid to | E-SC18-07 valid to | date | yes while Received | yes |
| Covers | E-SC18-07 covers | training, competition | yes while Received | yes |
| Proof | certificate or health questionnaire | the questionnaire for a minor, a certificate only if an answer leads to an examination (L231-2 III) | yes while Received | yes |
| Fit | fit or not fit | yes or no; never the medical content | yes while Received | yes |
| Document | E-F2-13 document | file with limited access | yes while Received | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record | header | coach, owner | a certificate is saved Received then Valid |
| Refuse | certificate row | coach, owner | a certificate with a problem is Rejected |
| Ask for a new one | member row | coach | a message goes to the member |

## States

- Normal: the members with their coverage, validity and state.
- Empty: No certificate recorded yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a certificate
  with no date or practice, or a member not covered, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-07 Medical certificate](../../data/e-sc18-07-medical-certificate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-07 Medical certificate | Received | Badge "Received"; a new record starts here; next: Valid or Rejected (BR-SC18-10, UC-SC18-10); fields editable within the role | U53 | `u53-coach/s-sc18-10-medical-certificates-e-sc18-07-medical-certificate-received-phone-{light,dark}.png` |
| E-SC18-07 Medical certificate | Valid | Badge "Valid"; next: Expired (UC-SC18-10); fields editable within the role | U53 | `u53-coach/s-sc18-10-medical-certificates-e-sc18-07-medical-certificate-valid-phone-{light,dark}.png` |
| E-SC18-07 Medical certificate | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U53 | `u53-coach/s-sc18-10-medical-certificates-e-sc18-07-medical-certificate-rejected-phone-{light,dark}.png` |
| E-SC18-07 Medical certificate | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U53 | `u53-coach/s-sc18-10-medical-certificates-e-sc18-07-medical-certificate-expired-phone-{light,dark}.png` |

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

- [FL-SC18-03 Licences and competitions](../../flows/fl-sc18-03-licences-and-competitions.md)

## Open questions

None.

---

⬅️ [S-SC18-09 Federation licences](s-sc18-09-federation-licences.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-11 Teams and competitions](s-sc18-11-teams-and-competitions.md)
