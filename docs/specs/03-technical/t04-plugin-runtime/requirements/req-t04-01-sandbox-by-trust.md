🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-01 Sandbox by trust level

# 📌 REQ-T04-01 Sandbox by trust level

**Status:** ✅ specified

## Statement

First-party industry modules run as services; store plugins and generated features run in WebAssembly or an isolated
container.

## Why

Confirmed by the owner on 2026-11-12; D405.

## Acceptance criteria

1. **Given** a store plugin tries to read a file, it is refused.
2. **Given** a first-party module, it runs as a service.

## Measure

Escapes found in tests.

## Priority

Must

## Capabilities served

F10 to F14, F19

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T04-02 Only the public API](req-t04-02-public-api-only.md)
