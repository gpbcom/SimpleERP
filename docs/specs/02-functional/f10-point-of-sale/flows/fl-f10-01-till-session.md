🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F10-01 Till session

# 🔀 FL-F10-01 Till session

**Status:** ✅ specified

## Summary

Covers UC-F10-16, UC-F10-01.

## Personas

- [U02 Manager](../../../01-users/personas/u02-manager.md)
- [U17 Cashier](../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../01-users/personas/u18-waiter.md)
- [U19 Kitchen staff](../../../01-users/personas/u19-kitchen-staff.md)

## Flowchart

```mermaid
flowchart LR
  A[Staff login] --> B[Open session, count float]
  B --> C[Sell]
  C --> D[Close: count cash]
  D --> E[Daily closure and posting]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U17, U18, U19, U02 | [S-F10-16](../screens/01-till-session/s-f10-16-staff-login.md) | [UC-F10-16](../use-cases/01-till-session/uc-f10-16-log-in-staff-and-set-till-rights.md) | Log in staff and set till rights |
| 2 | U17, U02 | [S-F10-01](../screens/01-till-session/s-f10-01-till-session.md) | [UC-F10-01](../use-cases/01-till-session/uc-f10-01-open-and-close-a-till-session.md) | Open and close a till session |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F10-02 Till session](../data/e-f10-02-till-session.md) | Open | 2 [S-F10-01](../screens/01-till-session/s-f10-01-till-session.md) | Till sessions |
| [E-F10-06 Closure](../data/e-f10-06-closure.md) | Active | 2 [S-F10-01](../screens/01-till-session/s-f10-01-till-session.md) | Closures |
| [E-F8-03 Journal entry](../../f08-accounting/data/e-f08-03-journal-entry.md) | Draft, Posted, Reversed | Shown elsewhere: [S-F8-02 Journal entries](../../f08-accounting/screens/01-set-up-and-post/s-f08-02-journal-entries.md) | Journal entries |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U17 | desktop | [light](../images/01-till-session/u17-cashier/1-staff-login-desktop-light.png) | [dark](../images/01-till-session/u17-cashier/1-staff-login-desktop-dark.png) |
| 1 | U17 | phone | [light](../images/01-till-session/u17-cashier/1-staff-login-phone-light.png) | [dark](../images/01-till-session/u17-cashier/1-staff-login-phone-dark.png) |
| 1 | U17 | tablet | [light](../images/01-till-session/u17-cashier/1-staff-login-tablet-light.png) | [dark](../images/01-till-session/u17-cashier/1-staff-login-tablet-dark.png) |
| 1 | U02 | desktop | [light](../images/01-till-session/u02-manager/1-staff-login-desktop-light.png) | [dark](../images/01-till-session/u02-manager/1-staff-login-desktop-dark.png) |
| 1 | U02 | phone | [light](../images/01-till-session/u02-manager/1-staff-login-phone-light.png) | [dark](../images/01-till-session/u02-manager/1-staff-login-phone-dark.png) |
| 1 | U18 | phone | [light](../images/01-till-session/u18-waiter/1-staff-login-phone-light.png) | [dark](../images/01-till-session/u18-waiter/1-staff-login-phone-dark.png) |
| 1 | U18 | tablet | [light](../images/01-till-session/u18-waiter/1-staff-login-tablet-light.png) | [dark](../images/01-till-session/u18-waiter/1-staff-login-tablet-dark.png) |
| 1 | U19 | desktop | [light](../images/01-till-session/u19-kitchen-staff/1-staff-login-desktop-light.png) | [dark](../images/01-till-session/u19-kitchen-staff/1-staff-login-desktop-dark.png) |
| 2 | U17 | desktop | [light](../images/01-till-session/u17-cashier/2-open-and-close-desktop-light.png) | [dark](../images/01-till-session/u17-cashier/2-open-and-close-desktop-dark.png) |
| 2 | U17 | phone | [light](../images/01-till-session/u17-cashier/2-open-and-close-phone-light.png) | [dark](../images/01-till-session/u17-cashier/2-open-and-close-phone-dark.png) |
| 2 | U17 | tablet | [light](../images/01-till-session/u17-cashier/2-open-and-close-tablet-light.png) | [dark](../images/01-till-session/u17-cashier/2-open-and-close-tablet-dark.png) |
| 2 | U02 | desktop | [light](../images/01-till-session/u02-manager/2-open-and-close-desktop-light.png) | [dark](../images/01-till-session/u02-manager/2-open-and-close-desktop-dark.png) |
| 2 | U02 | phone | [light](../images/01-till-session/u02-manager/2-open-and-close-phone-light.png) | [dark](../images/01-till-session/u02-manager/2-open-and-close-phone-dark.png) |
| E1 | U17 | desktop | [light](../images/01-till-session/u17-cashier/e1-cash-difference-desktop-light.png) | [dark](../images/01-till-session/u17-cashier/e1-cash-difference-desktop-dark.png) |
| E1 | U17 | phone | [light](../images/01-till-session/u17-cashier/e1-cash-difference-phone-light.png) | [dark](../images/01-till-session/u17-cashier/e1-cash-difference-phone-dark.png) |
| E1 | U17 | tablet | [light](../images/01-till-session/u17-cashier/e1-cash-difference-tablet-light.png) | [dark](../images/01-till-session/u17-cashier/e1-cash-difference-tablet-dark.png) |

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [FL-F10-02 Sell at the counter](fl-f10-02-sell-at-the-counter.md)
