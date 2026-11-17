🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🏭 TC-12 Code written by an AI, running in production

# 🏭 TC-12 Code written by an AI, running in production

**Status:** ✅ listed for the technical interviews

## Challenge

Generate each feature factory request as a plugin with its tests, check, review and sign it, keep it working across
every upgrade, and never let closed factory code into an AGPL plugin.

## Raised by

- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md)
- [T4 Plugin runtime](../t04-plugin-runtime/README.md)

## Why it is hard

- The generated code is as risky as any outside plugin, and there may be many of them.
- Each upgrade of simple-ERP must run every generated feature's tests first.
- The open-core boundary must be checked by a machine, not by trust.

## Already decided

- [D377](../../06-decisions/vision/d377-plugins-agpl-only.md) Plugins and sector packs are AGPL too
- [D388](../../06-decisions/vision/d388-hosted-edition-open-core.md) Hosted edition: closed services around the open
  core
- [D389](../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md) Generated features are plugins

## Options to weigh

- The same pipeline as the store (checks, review, signing) with a boundary check added.
- Compatibility tests of all features in the release pipeline.
- A model ladder and a cost budget per request.

## Settled in

- 19g Supply chain and licences ([chapter](../../../technical/security/supply-chain-and-licences.md))
- 19l Release and versioning ([chapter](../../../technical/delivery/release-and-versioning.md))
- 19o Tests: unit, GUI, E2E and load ([chapter](../../../technical/delivery/tests-and-traceability.md))
- 19n Plugin SDK and developer experience ([chapter](../../../technical/interfaces/plugin-sdk.md))
- Then the technical capabilities: [T4 Plugin runtime](../t04-plugin-runtime/README.md).

## Questions for the interview

- How many generated features must one upgrade carry?
- Who fixes a feature the factory cannot fix?

---

⬅️ [TC-11 Connectors, scrapers and the outside world](tc-11-connectors-and-generated-scrapers.md) · ⬆️ [Up](README.md) ·
➡️ [TC-13 Hosted operations helped by an AI](tc-13-operations-run-by-an-ai.md)
