🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-05 Copies and scenario overlays isolated

# 📌 REQ-T01-05 Copies and scenario overlays isolated

**Status:** ✅ specified

## Statement

Copies (F19 try-outs, F20 reproductions) and scenario overlays (F23) are isolated from live data and from each other.

## Why

Confirmed by the owner on 2026-11-12; D402, D389.

## Acceptance criteria

1. **Given** a scenario changes a price, the live price list is unchanged.
2. **Given** two scenarios run, neither sees the other's changes.

## Measure

Overlay leak tests.

## Priority

Must

## Capabilities served

F19, F20, F23, F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T01-04 A dedicated namespace or cluster when needed](req-t01-04-dedicated-plans.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T01-06 A company created from a template in under a minute](req-t01-06-company-from-template.md)
