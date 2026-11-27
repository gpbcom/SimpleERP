🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) ›
🧩 TC-02 Modules switched on in one click, and a plugin-first core

# 🧩 TC-02 Modules switched on in one click, and a plugin-first core

**Status:** ✅ listed for the technical interviews

## Challenge

Let a non-technical person switch any functional module on or off at once, keep its data read-only when off, and build
the industry modules, store plugins and generated features on the same public plugin API.

## Raised by

- [F21 Onboarding and module activation](../../02-functional/f21-onboarding-and-modules/README.md)
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md)
- [F11 Online shop (plugin)](../../02-functional/f11-online-shop/README.md)
- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md)
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md)
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [T4 Plugin runtime](../t04-plugin-runtime/README.md)

## Why it is hard

- A module adds tables, screens, menus, roles, rules, notifications and assistant tools: all must appear and disappear
  without a restart or a lost record.
- Dependencies between modules and plugins must be checked before each switch and each upgrade.
- The industry modules prove the API: whatever they need that the API lacks is added to the API, never reached around.

## Already decided

- [D15](../../06-decisions/foundations/d15-industry-areas-as-plugins.md) Point of sale, shop, manufacturing and payroll
  as plugins
- [D26](../../06-decisions/foundations/d26-technical-and-functional-capabilities.md) Technical and functional
  capabilities
- [D377](../../06-decisions/vision/d377-plugins-agpl-only.md) Plugins and sector packs are AGPL too
- [D389](../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md) Generated features are plugins
- [D395](../../06-decisions/f21-onboarding-and-modules/d395-onboarding-and-modules-coverage.md) Onboarding and one-click
  modules

## Options to weigh

- A module registry with feature flags per company, against loading plugins per company.
- Schema changes per plugin: migrations run on activation, or every schema always present.
- In-process plugins, separate services, or a sandbox (for example WebAssembly) per trust level.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19n Plugin SDK and developer experience ([chapter](../../../technical/interfaces/plugin-sdk.md))
- 19k Backups, recovery and upgrades ([chapter](../../../technical/operations/operations.md))
- Then the technical capabilities: [T4 Plugin runtime](../t04-plugin-runtime/README.md).

## Questions for the interview

- Which modules form the core that can never be switched off?
- May an untrusted plugin run in the same process as the core?

---

⬅️ [TC-01 Isolation of companies at every layer](tc-01-isolation-at-every-layer.md) · ⬆️ [Up](README.md) ·
➡️ [TC-03 No-code configuration against schema and upgrades](tc-03-no-code-configuration-and-schema.md)
