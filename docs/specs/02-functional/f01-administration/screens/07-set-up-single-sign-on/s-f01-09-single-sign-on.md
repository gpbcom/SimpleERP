🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-07 Set up single sign-on](README.md) › 🖥️ S-F1-09 Single sign-on

# 🖥️ S-F1-09 Single sign-on

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Connect the identity provider and set who gets an account.

## Entry points

Administration › Connections › Single sign-on; setup step 5 (D58).

## Wireframe

```text
+------------------------------------------------------------------+
| Single sign-on                                   Status: off     |
|------------------------------------------------------------------|
| Provider  ( ) Google Workspace  (o) Microsoft Entra ID           |
|           ( ) OpenID Connect    ( ) SAML 2.0                     |
| Client ID [ 3f2a...           ]  Secret [ ********** ]           |
| Allowed domains [ acme.fr x ] [+]                                |
| Default role [ Employee v ]   Default site [ Head office v ]     |
| Only administrators keep a password.                             |
|                                  [Test]  [Turn on] (after test)  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-07 step 1, U07 | desktop | ![FL-F1-07 step 1, U07, light](../../images/07-set-up-single-sign-on/u07-administrator/1-provider-and-details-desktop-light.png) | ![FL-F1-07 step 1, U07, dark](../../images/07-set-up-single-sign-on/u07-administrator/1-provider-and-details-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/07-set-up-single-sign-on/u07-administrator/e1-test-failed-desktop-light.png) | ![Error E1, U07, dark](../../images/07-set-up-single-sign-on/u07-administrator/e1-test-failed-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-09-single-sign-on-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-09-single-sign-on-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-09-single-sign-on-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-09-single-sign-on-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-09-single-sign-on-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-09-single-sign-on-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-09-single-sign-on-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-09-single-sign-on-offline-desktop-dark.png) |

## Fields and columns

As [E-F1-10 Single sign-on setting](../../data/e-f01-10-single-sign-on-setting.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Test | administrator | Sign-in in a new window, result shown |
| Turn on | administrator | Only after a passed test |
| Turn off | administrator | Passwords for everyone again |

## States

- Normal: Connect the identity provider and set who gets an account, as the wireframe shows.
- Empty: Off: no identity provider connected yet, with Connect.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: test failed, with the provider's message.
- Read-only: for users other than administrators.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.
- Off, tested, on.
- Warning: secret or certificate expiring within 30 days.

Shown entities (VD-15): [E-F1-10 Single sign-on setting](../../data/e-f01-10-single-sign-on-setting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-10 Single sign-on setting | On | Badge "On"; next: Off (UC-F1-09); fields editable within the role | U07 | `u07-administrator/s-f01-09-single-sign-on-e-f01-10-single-sign-on-setting-on-desktop-{light,dark}.png` |
| E-F1-10 Single sign-on setting | Off | Badge "Off"; a new record starts here; next: Tested (UC-F1-09); fields editable within the role | U07 | `u07-administrator/s-f01-09-single-sign-on-e-f01-10-single-sign-on-setting-off-desktop-{light,dark}.png` |
| E-F1-10 Single sign-on setting | Tested | Badge "Tested"; next: On (UC-F1-09); fields editable within the role | U07 | `u07-administrator/s-f01-09-single-sign-on-e-f01-10-single-sign-on-setting-tested-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

The provider choice is a radio group; the secret field can be shown with a button.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F1-07 Set up single sign-on](../../flows/fl-f01-07-set-up-single-sign-on.md)

## Open questions

None.

---

⬅️ [S-F1-08 AI settings](../06-choose-an-ai-provider/s-f01-08-ai-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-10 Client companies](../08-provider-and-client-companies/s-f01-10-client-companies.md)
