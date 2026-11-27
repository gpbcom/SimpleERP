🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F25-03 Bugs

# 🔀 FL-F25-03 Bugs

**Status:** ✅ specified

## Summary

Covers UC-F25-08, UC-F25-09, UC-F25-10, UC-F25-11.

## Personas

- [U47 SimpleERP maintainer](../../../01-users/personas/u47-simpleerp-maintainer.md)
- [U48 Hosting engineer](../../../01-users/personas/u48-hosting-engineer.md)

## Flowchart

```mermaid
flowchart LR
  A[Reproduce] --> B[Root cause]
  B --> C[Failing test and fix]
  C --> D[PRODUCT ticket]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U47, U48 | [S-F25-08](../screens/03-bugs/s-f25-08-reproduce.md) | [UC-F25-08](../use-cases/03-bugs/uc-f25-08-reproduce-a-bug-on-the-managed-simpleerp.md) | Reproduce a bug on the managed SimpleERP |
| 2 | U47 | [S-F25-09](../screens/03-bugs/s-f25-09-root-cause.md) | [UC-F25-09](../use-cases/03-bugs/uc-f25-09-find-the-cause-in-the-code.md) | Find the cause in the code |
| 3 | U47 | [S-F25-10](../screens/03-bugs/s-f25-10-fix-pull-request.md) | [UC-F25-10](../use-cases/03-bugs/uc-f25-10-propose-the-fix-as-a-pull-request-tests-first.md) | Propose the fix as a pull request, tests first |
| 4 | U47 | [S-F25-11](../screens/03-bugs/s-f25-11-product-ticket.md) | [UC-F25-11](../use-cases/03-bugs/uc-f25-11-create-the-product-ticket.md) | Create the PRODUCT ticket |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F25-04 Study note](../data/e-f25-04-study-note.md) | Recorded | Shown elsewhere: [S-F25-05 Study](../screens/02-feature-requests/s-f25-05-study.md) | Study notes |
| [E-F25-05 Agent pull request](../data/e-f25-05-agent-pull-request.md) | In review, Proposed, Declined, Checked, Open, Waiting | 3 [S-F25-10](../screens/03-bugs/s-f25-10-fix-pull-request.md) | Agent pull requests |
| [E-F25-06 Agent ticket](../data/e-f25-06-agent-ticket.md) | Active | 4 [S-F25-11](../screens/03-bugs/s-f25-11-product-ticket.md) | Agent tickets |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U47 | desktop | [light](../images/03-bugs/u47-simpleerp-maintainer/1-reproduce-desktop-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/1-reproduce-desktop-dark.png) |
| 1 | U47 | phone | [light](../images/03-bugs/u47-simpleerp-maintainer/1-reproduce-phone-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/1-reproduce-phone-dark.png) |
| 1 | U48 | desktop | [light](../images/03-bugs/u48-hosting-engineer/1-reproduce-desktop-light.png) | [dark](../images/03-bugs/u48-hosting-engineer/1-reproduce-desktop-dark.png) |
| 1 | U48 | phone | [light](../images/03-bugs/u48-hosting-engineer/1-reproduce-phone-light.png) | [dark](../images/03-bugs/u48-hosting-engineer/1-reproduce-phone-dark.png) |
| 2 | U47 | desktop | [light](../images/03-bugs/u47-simpleerp-maintainer/2-cause-desktop-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/2-cause-desktop-dark.png) |
| 2 | U47 | phone | [light](../images/03-bugs/u47-simpleerp-maintainer/2-cause-phone-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/2-cause-phone-dark.png) |
| 3 | U47 | desktop | [light](../images/03-bugs/u47-simpleerp-maintainer/3-fix-pr-desktop-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/3-fix-pr-desktop-dark.png) |
| 3 | U47 | phone | [light](../images/03-bugs/u47-simpleerp-maintainer/3-fix-pr-phone-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/3-fix-pr-phone-dark.png) |
| 4 | U47 | desktop | [light](../images/03-bugs/u47-simpleerp-maintainer/4-product-ticket-desktop-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/4-product-ticket-desktop-dark.png) |
| 4 | U47 | phone | [light](../images/03-bugs/u47-simpleerp-maintainer/4-product-ticket-phone-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/4-product-ticket-phone-dark.png) |
| E1 | U47 | desktop | [light](../images/03-bugs/u47-simpleerp-maintainer/e1-cannot-reproduce-desktop-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/e1-cannot-reproduce-desktop-dark.png) |
| E1 | U47 | phone | [light](../images/03-bugs/u47-simpleerp-maintainer/e1-cannot-reproduce-phone-light.png) | [dark](../images/03-bugs/u47-simpleerp-maintainer/e1-cannot-reproduce-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F25-02 Feature requests](fl-f25-02-feature-requests.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F25-04 Approve and govern](fl-f25-04-approve-and-govern.md)
