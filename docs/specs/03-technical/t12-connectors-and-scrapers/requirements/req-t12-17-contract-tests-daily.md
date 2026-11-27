🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T12-17 Connector contract tests daily

# 📌 REQ-T12-17 Connector contract tests daily

**Status:** ✅ specified

## Statement

Each connector's contract tests run daily against the outside tool's sandbox.

## Why

Confirmed by the owner on 2026-11-12; TC-23.

## Acceptance criteria

1. **Given** an outside API change, caught the same day.
2. **Given** a passing run, recorded.

## Measure

Breaks caught.

## Priority

Must

## Capabilities served

F24

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T12-16 The default 25 CRM and 25 ATS](req-t12-16-fifty-ats-crm.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-18 Meeting capture](req-t12-18-meeting-capture.md)
