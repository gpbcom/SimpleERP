🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D425 Plugin SDK and developer tools

# 📜 D425 Plugin SDK and developer tools

**Status:** ✅ decided

## Context

Step 19n of the technical interview, from TC-02 and TC-12.

## Options

- An SDK, a CLI and a local sandbox.
- An SDK and a local sandbox, with the developer tools reached through the sandbox's API, pytest fixtures and the
  scripts of the plugin template, and no CLI.
- The API only.

## Choice

Confirmed by the owner on 2026-11-12: a Python SDK (TypeScript for widgets), a local Compose sandbox, the store's
checks, generated documentation; the feature factory uses the same SDK.

Changed by the owner on 2026-11-27: the SDK has no CLI. A plugin is scaffolded, tested, packaged and signed through the
local sandbox's API, the SDK's pytest fixtures and the scripts of the plugin template, all outside the `sdk/` package.
No package of SimpleERP has a command line ([D406](d406-back-end.md)).

## Decided by

The owner, on 2026-11-12, in the specification interview, and on 2026-11-27 for the developer tools without a CLI.

## Consequences

The plugin SDK chapter's target design. `sdk/` is a library with no console script, which the tests of
`tests/conventions/entrypoints/` enforce (`AGENT.md`, "Layout").

## Related

- [Plugin SDK and developer experience](../../../technical/interfaces/plugin-sdk.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D424 Importers from other ERPs](d424-importers.md) · ⬆️ [Up](README.md) ·
➡️ [D426 Testing strategy](d426-testing-strategy.md)
