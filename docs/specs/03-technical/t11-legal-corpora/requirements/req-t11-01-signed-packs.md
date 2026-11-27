🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🏛️ [T11 Legal corpora](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T11-01 Signed, versioned packs

# 📌 REQ-T11-01 Signed, versioned packs

**Status:** ✅ specified

## Statement

Each country pack is signed, versioned data with validity dates, released apart from the software.

The raw law texts pulled for the legal assistant's corpus are not packs: they are official texts, pulled unattended, and
change no rule value (REQ-T11-03, D448).

## Why

Confirmed by the owner on 2026-11-12; D405, D423.

Clarified by D448 on 2026-11-12.

## Acceptance criteria

1. **Given** a pack update, installed without a software release.
2. **Given** an unsigned pack, refused.

## Measure

Pack releases.

## Priority

Must

## Capabilities served

All: F1 to F25 and the sectors SC01 to SC16.

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T11-02 One rules library by date](req-t11-02-rules-library.md)
