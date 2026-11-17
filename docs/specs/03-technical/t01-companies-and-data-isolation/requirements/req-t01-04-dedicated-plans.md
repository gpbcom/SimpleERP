🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-04 A dedicated namespace or cluster when needed

# 📌 REQ-T01-04 A dedicated namespace or cluster when needed

**Status:** ✅ specified

## Statement

Plans that need it (health data, large companies) get a dedicated namespace or cluster.

## Why

Confirmed by the owner on 2026-11-12; D405, D409.

## Acceptance criteria

1. **Given** a health-practice company, it runs on the certified profile only.
2. **Given** a dedicated plan, no shared service holds its data.

## Measure

Dedicated placements.

## Priority

Must

## Capabilities served

SC09, F18 to F20

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T01-03 Provider access visible and audited](req-t01-03-provider-access-visible.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T01-05 Copies and scenario overlays isolated](req-t01-05-copies-and-overlays.md)
