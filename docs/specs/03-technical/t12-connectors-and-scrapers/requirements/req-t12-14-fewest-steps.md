🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T12-14 Every connector in the fewest steps

# 📌 REQ-T12-14 Every connector in the fewest steps

**Status:** ✅ specified

## Statement

Every connector is enabled in as few steps as possible: OAuth sign-in where offered, settings discovered and pre-filled.

## Why

Confirmed by the owner on 2026-11-12; D429, BR-F24-02.

## Acceptance criteria

1. **Given** a connector with OAuth, sign in and confirm.
2. **Given** a key needed, one field with a link.

## Measure

Steps per connector.

## Priority

Must

## Capabilities served

F24 and every connector

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T12-13 Target discovery](req-t12-13-target-discovery.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-15 Office suites' full APIs](req-t12-15-office-suites-api.md)
