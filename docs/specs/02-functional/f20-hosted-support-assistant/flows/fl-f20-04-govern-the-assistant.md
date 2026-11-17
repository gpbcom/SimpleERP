🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 🔀 [Flows](README.md) ›
🔀 FL-F20-04 Govern the AI assistant

# 🔀 FL-F20-04 Govern the AI assistant

**Status:** ✅ specified

## Summary

Covers UC-F20-16, UC-F20-17, UC-F20-18, UC-F20-19, UC-F20-20.

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)
- [U48 Hosting engineer](../../../01-users/personas/u48-hosting-engineer.md)

## Flowchart

```mermaid
flowchart LR
  A[Rights] --> B[Masking]
  B --> C[Quality]
  C --> D[Plans and exports]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U07, U48 | [S-F20-16](../screens/04-govern-the-assistant/s-f20-16-quality.md) | [UC-F20-16](../use-cases/04-govern-the-assistant/uc-f20-16-rate-the-help-and-review-quality.md) | Rate the help and review quality |
| 2 | U48 | [S-F20-17](../screens/04-govern-the-assistant/s-f20-17-assistant-rights.md) | [UC-F20-17](../use-cases/04-govern-the-assistant/uc-f20-17-control-and-audit-the-assistant-s-rights.md) | Control and audit the AI assistant's rights |
| 3 | U48 | [S-F20-18](../screens/04-govern-the-assistant/s-f20-18-masking.md) | [UC-F20-18](../use-cases/04-govern-the-assistant/uc-f20-18-mask-personal-data-and-secrets.md) | Mask personal data and secrets |
| 4 | U13 | [S-F20-19](../screens/04-govern-the-assistant/s-f20-19-support-plans.md) | [UC-F20-19](../use-cases/04-govern-the-assistant/uc-f20-19-choose-a-support-plan-and-see-its-times.md) | Choose a support plan and see its times |
| 5 | U07 | [S-F20-20](../screens/04-govern-the-assistant/s-f20-20-export.md) | [UC-F20-20](../use-cases/04-govern-the-assistant/uc-f20-20-export-a-support-conversation.md) | Export a support conversation |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F20-11 Assistant policy](../data/e-f20-11-assistant-policy.md) | Active | 2 [S-F20-17](../screens/04-govern-the-assistant/s-f20-17-assistant-rights.md); 3 [S-F20-18](../screens/04-govern-the-assistant/s-f20-18-masking.md) | Assistant policies |
| [E-F20-10 Rating](../data/e-f20-10-rating.md) | Active | 1 [S-F20-16](../screens/04-govern-the-assistant/s-f20-16-quality.md) | Ratings |
| [E-F20-12 Support plan](../data/e-f20-12-support-plan.md) | Active | 4 [S-F20-19](../screens/04-govern-the-assistant/s-f20-19-support-plans.md) | Support plans |
| [E-F20-18 Support conversation export](../data/e-f20-18-support-conversation-export.md) | Active | 5 [S-F20-20](../screens/04-govern-the-assistant/s-f20-20-export.md) | Support conversation exports |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U07 | desktop | [light](../images/04-govern-the-assistant/u07-administrator/1-quality-desktop-light.png) | [dark](../images/04-govern-the-assistant/u07-administrator/1-quality-desktop-dark.png) |
| 1 | U48 | desktop | [light](../images/04-govern-the-assistant/u48-hosting-engineer/1-quality-desktop-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/1-quality-desktop-dark.png) |
| 1 | U48 | phone | [light](../images/04-govern-the-assistant/u48-hosting-engineer/1-quality-phone-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/1-quality-phone-dark.png) |
| 2 | U48 | desktop | [light](../images/04-govern-the-assistant/u48-hosting-engineer/2-rights-desktop-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/2-rights-desktop-dark.png) |
| 2 | U48 | phone | [light](../images/04-govern-the-assistant/u48-hosting-engineer/2-rights-phone-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/2-rights-phone-dark.png) |
| 3 | U48 | desktop | [light](../images/04-govern-the-assistant/u48-hosting-engineer/3-masking-desktop-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/3-masking-desktop-dark.png) |
| 3 | U48 | phone | [light](../images/04-govern-the-assistant/u48-hosting-engineer/3-masking-phone-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/3-masking-phone-dark.png) |
| 4 | U13 | desktop | [light](../images/04-govern-the-assistant/u13-owner/4-plans-desktop-light.png) | [dark](../images/04-govern-the-assistant/u13-owner/4-plans-desktop-dark.png) |
| 4 | U13 | phone | [light](../images/04-govern-the-assistant/u13-owner/4-plans-phone-light.png) | [dark](../images/04-govern-the-assistant/u13-owner/4-plans-phone-dark.png) |
| 5 | U07 | desktop | [light](../images/04-govern-the-assistant/u07-administrator/5-export-desktop-light.png) | [dark](../images/04-govern-the-assistant/u07-administrator/5-export-desktop-dark.png) |
| E1 | U48 | desktop | [light](../images/04-govern-the-assistant/u48-hosting-engineer/e1-unmasked-desktop-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/e1-unmasked-desktop-dark.png) |
| E1 | U48 | phone | [light](../images/04-govern-the-assistant/u48-hosting-engineer/e1-unmasked-phone-light.png) | [dark](../images/04-govern-the-assistant/u48-hosting-engineer/e1-unmasked-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F20-03 Incidents](fl-f20-03-incidents.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F20-05 Maintenance and releases](fl-f20-05-maintenance-and-releases.md)
