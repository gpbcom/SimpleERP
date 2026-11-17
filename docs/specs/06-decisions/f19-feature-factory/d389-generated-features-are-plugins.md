🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🏭 [Decisions: F19 Feature factory (hosted edition)](README.md) › 📜 D389 Generated features are plugins

# 📜 D389 Generated features are plugins

**Status:** ✅ decided

## Context

The owner: simple-ERP is able to modify its own code; a feature a customer promotes becomes available to every hosted
customer.

## Options

- A generated plugin.
- A change to the core code.

## Choice

A generated plugin, confirmed by the owner on 2026-11-12: the closed factory (D388) writes each feature as a plugin on
the plugin runtime (T4), with its tests, checked, reviewed and signed like any store plugin (F14), installed for the
customer; the core is never changed per customer, so upgrades stay safe. The generated plugin is AGPL-3.0 like every
plugin (D377); the factory itself, its prompts and its pipeline stay closed.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F19-02 to BR-F19-07; a promoted feature is published in the hosted store.

## Related

- [F19 Feature factory](../../02-functional/f19-feature-factory/README.md)

---

⬅️ [D388 Hosted edition: closed services around the open core](../vision/d388-hosted-edition-open-core.md) ·
⬆️ [Up](README.md) · ➡️ [D390 Feature price and promotion credit](d390-feature-price-and-promotion-credit.md)
