🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC14-07 Hardware, licences, research tax credit and sponsorship](README.md) › 🖥️ S-SC14-25 Sponsorship

# 🖥️ S-SC14-25 Sponsorship

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the tiers, the sponsors and the money raised.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own sponsorship, the next invoice and the
  benefits on the phone.

## Purpose

Define sponsor tiers, follow each sponsor's pledge and invoices, and switch their benefits on and off with the payments.

## Entry points

IT and software › Sponsorship; a sponsor's page; the tiers' settings.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Sponsors: project Lumen                     Raised this year 14,400.00 EUR   [New tier] [Export] |
| Sponsor          Tier    Period   Fee      Next invoice  Benefits               State            |
| Atelier Roche    Gold    Yearly   1,200.00 2027-03-01    Logo, support          Active           |
| Studio Lenoir    Silver  Monthly  100.00   2026-12-01    Logo                   Active           |
| Marie L.         Bronze  Monthly  10.00    2026-12-05    Badge                  Lapsed           |
| Tiers: 3          Sponsors: 41 active, 2 lapsed this quarter                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-07 step 4, U13 | desktop | ![FL-SC14-07 step 4, U13, light](../../images/07-hardware-licences-and-tax-credits/u13-owner/4-sponsorship-desktop-light.png) | ![FL-SC14-07 step 4, U13, dark](../../images/07-hardware-licences-and-tax-credits/u13-owner/4-sponsorship-desktop-dark.png) |
| FL-SC14-07 step 4, U13 | phone | ![FL-SC14-07 step 4, U13, light](../../images/07-hardware-licences-and-tax-credits/u13-owner/4-sponsorship-phone-light.png) | ![FL-SC14-07 step 4, U13, dark](../../images/07-hardware-licences-and-tax-credits/u13-owner/4-sponsorship-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-25-sponsorship-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-25-sponsorship-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-25-sponsorship-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-25-sponsorship-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-25-sponsorship-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-25-sponsorship-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-25-sponsorship-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-25-sponsorship-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Sponsor | E-SC14-20 sponsor | link | no | yes |
| Tier | E-SC14-20 tier | text from the settings | yes while Pledged | yes |
| Period | E-SC14-20 period | monthly or yearly | yes while Pledged | yes |
| Fee | E-SC14-20 fee | amount in EUR | yes while Pledged | yes |
| Next invoice | E-SC14-20 next invoice | date | no | no |
| Benefits | E-SC14-20 benefits | list | no | no |
| Listed publicly | E-SC14-20 consent | yes or no | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New tier | header | owner | a tier with its price, period and benefits |
| Pledge | tier | sponsor | a sponsorship in state Pledged and its first invoice |
| Change tier | sponsorship | sponsor | the new tier applies at the next period |
| End | sponsorship | sponsor | the sponsorship ends at the end of the period paid |

## States

- Normal: the sponsors with tier, period, fee, next invoice, benefits and state.
- Empty: No sponsor yet, with New tier.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a tier without
  a price, a failed payment, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC14-20 Sponsorship](../../data/e-sc14-20-sponsorship.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-20 Sponsorship | Pledged | Badge "Pledged"; a new record starts here; next: Active or Ended (UC-SC14-25); fields editable within the role | U13, U09 | `u13-owner/s-sc14-25-sponsorship-e-sc14-20-sponsorship-pledged-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc14-25-sponsorship-e-sc14-20-sponsorship-pledged-phone-{light,dark}.png` |
| E-SC14-20 Sponsorship | Active | Badge "Active"; next: Lapsed or Ended (BR-SC14-19, UC-SC14-25); fields editable within the role | U13, U09 | `u13-owner/s-sc14-25-sponsorship-e-sc14-20-sponsorship-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc14-25-sponsorship-e-sc14-20-sponsorship-active-phone-{light,dark}.png` |
| E-SC14-20 Sponsorship | Lapsed | Badge "Lapsed"; next: Active (UC-SC14-25); fields editable within the role | U13, U09 | `u13-owner/s-sc14-25-sponsorship-e-sc14-20-sponsorship-lapsed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc14-25-sponsorship-e-sc14-20-sponsorship-lapsed-phone-{light,dark}.png` |
| E-SC14-20 Sponsorship | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc14-25-sponsorship-e-sc14-20-sponsorship-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc14-25-sponsorship-e-sc14-20-sponsorship-ended-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The sponsor's phone shows their tier, the next invoice and a Change tier button.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC14-07](../../flows/fl-sc14-07-hardware-licences-and-tax-credits.md)

## Open questions

None.

---

⬅️ [S-SC14-24 Research tax credit](s-sc14-24-research-tax-credit.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-L01 Software subscriptions](../00-lists/s-sc14-l01-software-subscriptions.md)
