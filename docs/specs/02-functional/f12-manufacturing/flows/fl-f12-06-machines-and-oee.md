🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F12-06 Machines and OEE

# 🔀 FL-F12-06 Machines and OEE

**Status:** ✅ specified

## Summary

Covers UC-F12-13, UC-F12-14.

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)
- [U21 Production planner](../../../01-users/personas/u21-production-planner.md)

## Flowchart

```mermaid
flowchart LR
  A[Connect machine] --> B[Signals]
  B --> C[Stops and counts]
  C --> D[OEE]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U21, U13 | [S-F12-13](../screens/06-machines-and-oee/s-f12-13-oee-measure.md) | [UC-F12-13](../use-cases/06-machines-and-oee/uc-f12-13-measure-oee-and-downtime.md) | Measure OEE and downtime |
| 2 | U07, U21 | [S-F12-14](../screens/06-machines-and-oee/s-f12-14-machine-connections.md) | [UC-F12-14](../use-cases/06-machines-and-oee/uc-f12-14-connect-machines-and-sensors.md) | Connect machines and sensors |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F12-09 Equipment](../data/e-f12-09-equipment.md) | Active | Shown elsewhere: [S-F12-08 Maintenance](../screens/04-quality-and-maintenance/s-f12-08-maintenance.md) | Equipments |
| [E-F12-13 Machine signal](../data/e-f12-13-machine-signal.md) | Recorded | 1 [S-F12-13](../screens/06-machines-and-oee/s-f12-13-oee-measure.md); 2 [S-F12-14](../screens/06-machines-and-oee/s-f12-14-machine-connections.md) | Machine signals |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U07 | desktop | [light](../images/06-machines-and-oee/u07-administrator/1-connect-machine-desktop-light.png) | [dark](../images/06-machines-and-oee/u07-administrator/1-connect-machine-desktop-dark.png) |
| 1 | U13 | desktop | [light](../images/06-machines-and-oee/u13-owner/1-connect-machine-desktop-light.png) | [dark](../images/06-machines-and-oee/u13-owner/1-connect-machine-desktop-dark.png) |
| 1 | U13 | phone | [light](../images/06-machines-and-oee/u13-owner/1-connect-machine-phone-light.png) | [dark](../images/06-machines-and-oee/u13-owner/1-connect-machine-phone-dark.png) |
| 1 | U21 | desktop | [light](../images/06-machines-and-oee/u21-production-planner/1-connect-machine-desktop-light.png) | [dark](../images/06-machines-and-oee/u21-production-planner/1-connect-machine-desktop-dark.png) |
| 1 | U21 | phone | [light](../images/06-machines-and-oee/u21-production-planner/1-connect-machine-phone-light.png) | [dark](../images/06-machines-and-oee/u21-production-planner/1-connect-machine-phone-dark.png) |
| 2 | U21 | desktop | [light](../images/06-machines-and-oee/u21-production-planner/2-oee-desktop-light.png) | [dark](../images/06-machines-and-oee/u21-production-planner/2-oee-desktop-dark.png) |
| 2 | U21 | phone | [light](../images/06-machines-and-oee/u21-production-planner/2-oee-phone-light.png) | [dark](../images/06-machines-and-oee/u21-production-planner/2-oee-phone-dark.png) |
| 2 | U07 | desktop | [light](../images/06-machines-and-oee/u07-administrator/2-oee-desktop-light.png) | [dark](../images/06-machines-and-oee/u07-administrator/2-oee-desktop-dark.png) |
| E1 | U21 | desktop | [light](../images/06-machines-and-oee/u21-production-planner/e1-connector-down-desktop-light.png) | [dark](../images/06-machines-and-oee/u21-production-planner/e1-connector-down-desktop-dark.png) |
| E1 | U21 | phone | [light](../images/06-machines-and-oee/u21-production-planner/e1-connector-down-phone-light.png) | [dark](../images/06-machines-and-oee/u21-production-planner/e1-connector-down-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F12-05 Subcontracting and costs](fl-f12-05-subcontracting-and-costs.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F12-07 Compliance and safety](fl-f12-07-compliance-and-safety.md)
