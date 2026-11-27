🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-13 Security and audit](README.md) › 🖥️ S-F1-21 Security policies

# 🖥️ S-F1-21 Security policies

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Set the password, session, two-factor, IP and device rules.

## Entry points

Administration › Security policies.

## Wireframe

```text
+------------------------------------------------------------------+
| Security policies                                                |
| Password   length [14]  expiry [none v]                          |
| Session    length [8 h v]  idle timeout [30 min v]               |
| Two-factor required for  [x] Administrators [x] Accounting       |
| Allowed IPs  Administrators [192.0.2.0/24        ]               |
| This change affects 5 users.                       [Save]        |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-13 step 1, U07 | desktop | ![FL-F1-13 step 1, U07, light](../../images/13-security-and-audit/u07-administrator/1-security-policies-desktop-light.png) | ![FL-F1-13 step 1, U07, dark](../../images/13-security-and-audit/u07-administrator/1-security-policies-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/13-security-and-audit/u07-administrator/e1-security-policies-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/13-security-and-audit/u07-administrator/e1-security-policies-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-21-security-policies-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-21-security-policies-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-21-security-policies-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-21-security-policies-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-21-security-policies-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-21-security-policies-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f01-21-security-policies-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f01-21-security-policies-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Password, session, two-factor, IPs and devices | E-F1-19 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Save | administrator | Applied; stricter rules at next sign-in |

## States

- Normal: the policies and who a change affects.
- Empty: never: the defaults are shown until changed.
- Loading: placeholders in the form.
- Error: a rule that would lock out every administrator (D122).
- Read-only: password rules when single sign-on is on.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-19 Security policy](../../data/e-f01-19-security-policy.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-19 Security policy | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f01-21-security-policies-e-f01-19-security-policy-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F1-13 Security and audit](../../flows/fl-f01-13-security-and-audit.md)

## Open questions

None.

---

⬅️ [S-F1-20 API tokens](../12-portal-accounts-and-integrations/s-f01-20-api-tokens.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-22 Audit trail](s-f01-22-audit-trail.md)
