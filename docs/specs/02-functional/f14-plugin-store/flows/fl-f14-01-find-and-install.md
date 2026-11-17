🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
🔀 [Flows](README.md) › 🔀 FL-F14-01 Find and install

# 🔀 FL-F14-01 Find and install

**Status:** ✅ specified

## Summary

Covers UC-F14-01, UC-F14-02, UC-F14-03, UC-F14-04, UC-F14-20.

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)

## Flowchart

```mermaid
flowchart LR
  A[Browse] --> B[Install]
  B --> C[Update]
  C -.-> D[Uninstall]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U07, U13 | [S-F14-01](../screens/01-find-and-install/s-f14-01-store.md) | [UC-F14-01](../use-cases/01-find-and-install/uc-f14-01-browse-and-search-the-store.md) | Browse and search the store |
| 2 | U07 | [S-F14-02](../screens/01-find-and-install/s-f14-02-install.md) | [UC-F14-02](../use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md) | Install a plugin or sector pack |
| 3 | U07 | [S-F14-03](../screens/01-find-and-install/s-f14-03-updates.md) | [UC-F14-03](../use-cases/01-find-and-install/uc-f14-03-update-with-compatibility-checks.md) | Update with compatibility checks |
| 4 | U07 | [S-F14-04](../screens/01-find-and-install/s-f14-04-uninstall.md) | [UC-F14-04](../use-cases/01-find-and-install/uc-f14-04-uninstall-and-export-the-plugin-s-data.md) | Uninstall and export the plugin's data |
| 5 | U07, U13 | [S-F14-20](../screens/01-find-and-install/s-f14-20-store-assistant.md) | [UC-F14-20](../use-cases/01-find-and-install/uc-f14-20-ask-the-assistant-to-find-or-set-up-a-plugin.md) | Ask the AI assistant to find or set up a plugin |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U07 | desktop | [light](../images/01-find-and-install/u07-administrator/1-browse-desktop-light.png) | [dark](../images/01-find-and-install/u07-administrator/1-browse-desktop-dark.png) |
| 1 | U13 | desktop | [light](../images/01-find-and-install/u13-owner/1-browse-desktop-light.png) | [dark](../images/01-find-and-install/u13-owner/1-browse-desktop-dark.png) |
| 1 | U13 | phone | [light](../images/01-find-and-install/u13-owner/1-browse-phone-light.png) | [dark](../images/01-find-and-install/u13-owner/1-browse-phone-dark.png) |
| 2 | U07 | desktop | [light](../images/01-find-and-install/u07-administrator/2-install-desktop-light.png) | [dark](../images/01-find-and-install/u07-administrator/2-install-desktop-dark.png) |
| 3 | U07 | desktop | [light](../images/01-find-and-install/u07-administrator/3-update-desktop-light.png) | [dark](../images/01-find-and-install/u07-administrator/3-update-desktop-dark.png) |
| 4 | U07 | desktop | [light](../images/01-find-and-install/u07-administrator/4-uninstall-desktop-light.png) | [dark](../images/01-find-and-install/u07-administrator/4-uninstall-desktop-dark.png) |
| 5 | U07 | desktop | [light](../images/01-find-and-install/u07-administrator/5-assistant-desktop-light.png) | [dark](../images/01-find-and-install/u07-administrator/5-assistant-desktop-dark.png) |
| 5 | U13 | desktop | [light](../images/01-find-and-install/u13-owner/5-assistant-desktop-light.png) | [dark](../images/01-find-and-install/u13-owner/5-assistant-desktop-dark.png) |
| 5 | U13 | phone | [light](../images/01-find-and-install/u13-owner/5-assistant-phone-light.png) | [dark](../images/01-find-and-install/u13-owner/5-assistant-phone-dark.png) |
| E1 | U07 | desktop | [light](../images/01-find-and-install/u07-administrator/e1-bad-signature-desktop-light.png) | [dark](../images/01-find-and-install/u07-administrator/e1-bad-signature-desktop-dark.png) |

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [FL-F14-02 Buy and licence](fl-f14-02-buy-and-licence.md)
