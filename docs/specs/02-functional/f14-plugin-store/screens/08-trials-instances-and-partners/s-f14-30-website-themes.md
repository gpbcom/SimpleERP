🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-08 Trials, test instances, partners and themes](README.md) › 🖥️ S-F14-30 Website themes

# 🖥️ S-F14-30 Website themes

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md): the themes of their site.
- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md): their own themes and check results.

## Purpose

Browse themes, preview them on the company's pages, check their accessibility and install one.

## Entry points

Plugin store › Themes; Website › Appearance.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Website themes     Sector [Retail v]  Style [Light v]                         Installed: Slate |
|---------------------------------------------------------------------------------------------|
| THEME      PUBLISHER      PRICE        ACCESSIBILITY          STATE                         |
| Slate      Studio Nord    Free         Passed 2026-11-02      Installed                     |
| Harvest    Garden Tools   39 EUR       Passed 2026-10-18      Published                     |
| Neon       Pixel House    19 EUR       Needs a new check      Published                     |
| [Preview] [Install on draft] [Restore previous]                                             |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-08 step 4, U12 | desktop | ![FL-F14-08 step 4, U12, light](../../images/08-trials-instances-and-partners/u12-marketing/4-website-themes-desktop-light.png) | ![FL-F14-08 step 4, U12, dark](../../images/08-trials-instances-and-partners/u12-marketing/4-website-themes-desktop-dark.png) |
| FL-F14-08 step 4, U12 | phone | ![FL-F14-08 step 4, U12, light](../../images/08-trials-instances-and-partners/u12-marketing/4-website-themes-phone-light.png) | ![FL-F14-08 step 4, U12, dark](../../images/08-trials-instances-and-partners/u12-marketing/4-website-themes-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-30-website-themes-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-30-website-themes-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-30-website-themes-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-30-website-themes-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-30-website-themes-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-30-website-themes-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f14-30-website-themes-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f14-30-website-themes-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Theme | E-F14-25 name, publisher | text | publisher | yes |
| Price | E-F14-04 price plan | amount | publisher | yes |
| Accessibility result | E-F14-25 check report | badge and date | no | yes |
| Colours and fonts | E-F14-25 tokens | colour and font pickers | marketing | no |
| State | E-F14-25 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Preview | row | marketing | the theme on the company's own pages |
| Install on draft | row | marketing | the draft site wears the theme |
| Restore previous | header | marketing, administrator | the previous theme comes back |
| Submit theme | publisher view | publisher | sends a theme to the checks |

## States

- Normal: the themes with price, accessibility result and state, and the installed one.
- Empty: No theme matches, with Widen the filters.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed
  install shows the failed check and keeps the current theme.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F14-25 Theme](../../data/e-f14-25-theme.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-25 Theme | Submitted | Badge "Submitted"; a new record starts here; next: Checked (BR-F14-27); fields editable within the role | U12, U46 | `u12-marketing/s-f14-30-website-themes-e-f14-25-theme-submitted-{desktop,phone}-{light,dark}.png`, `u46-plugin-publisher/s-f14-30-website-themes-e-f14-25-theme-submitted-desktop-{light,dark}.png` |
| E-F14-25 Theme | Checked | Badge "Checked"; next: Published or Rejected (BR-F14-27); fields editable within the role | U12, U46 | `u12-marketing/s-f14-30-website-themes-e-f14-25-theme-checked-{desktop,phone}-{light,dark}.png`, `u46-plugin-publisher/s-f14-30-website-themes-e-f14-25-theme-checked-desktop-{light,dark}.png` |
| E-F14-25 Theme | Published | Badge "Published"; next: Withdrawn (BR-F14-27); fields editable within the role | U12, U46 | `u12-marketing/s-f14-30-website-themes-e-f14-25-theme-published-{desktop,phone}-{light,dark}.png`, `u46-plugin-publisher/s-f14-30-website-themes-e-f14-25-theme-published-desktop-{light,dark}.png` |
| E-F14-25 Theme | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U12, U46 | `u12-marketing/s-f14-30-website-themes-e-f14-25-theme-rejected-{desktop,phone}-{light,dark}.png`, `u46-plugin-publisher/s-f14-30-website-themes-e-f14-25-theme-rejected-desktop-{light,dark}.png` |
| E-F14-25 Theme | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U12, U46 | `u12-marketing/s-f14-30-website-themes-e-f14-25-theme-withdrawn-{desktop,phone}-{light,dark}.png`, `u46-plugin-publisher/s-f14-30-website-themes-e-f14-25-theme-withdrawn-desktop-{light,dark}.png` |

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

⬅️ [S-F14-29 Partner directory](s-f14-29-partner-directory.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-L01 Store listings](../00-lists/s-f14-l01-store-listings.md)
