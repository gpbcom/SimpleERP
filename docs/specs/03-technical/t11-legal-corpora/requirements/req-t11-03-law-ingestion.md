🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🏛️ [T11 Legal corpora](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T11-03 Law ingested and versioned

# 📌 REQ-T11-03 Law ingested and versioned

**Status:** ✅ specified

## Statement

Law sources are ingested, articles versioned by date in force, repealed ones kept.

Pulls run unattended on a schedule (D205); copyrighted standards are excluded (D448).

## Why

Confirmed by the owner on 2026-11-12; D199.

## Acceptance criteria

1. **Given** an article amended, both versions kept.
2. **Given** a repealed article, marked.

## Measure

Articles ingested.

## Priority

Must

## Capabilities served

F15

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T11-02 One rules library by date](req-t11-02-rules-library.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T11-04 Changes flag rules](req-t11-04-change-flags.md)
