🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-06 A quality drop blocks the update

# 📏 BR-F15-06 A quality drop blocks the update

**Status:** 🚫 withdrawn

## Statement

🚫 Withdrawn on 2026-11-10 by
[D206](../../../06-decisions/f15-legal-assistant/d206-unattended-pulls-without-test-gate.md): law packs are refreshed
unattended and always applied, with no test-set gate.

## Why

A refresh or a new model must not silently worsen answers. See
[D200](../../../06-decisions/f15-legal-assistant/d200-legal-quality-test-set.md).

## Examples

| Case | Result |
|---|---|
| Refresh, 96 % to 96 % | Applied |
| New model, 96 % to 89 % | Not applied; administrators told which questions failed |
| A thumbs down "wrong article" | Proposed as a new test question to the law pack's maintainers |

## Applies to

Nothing: withdrawn.

## Exceptions

None.

## Configurable

The thresholds, by the law pack.

## Open questions

None.

---

⬅️ [BR-F15-05 The law of the contract or the site](br-f15-05-the-law-of-the-contract-or-the-site.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F15-07 Warnings inform, never block](br-f15-07-warnings-inform-never-block.md)
