🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-03 Agentic mode

# 📌 REQ-T12-03 Agentic mode

**Status:** ✅ specified

## Statement

An agent follows the intent's procedure and calls connector actions as tools: only the actions allowed for
that intent, writes confirmed or automatic per the intent's mode, a step cap and a cost budget per run, a stop at any
time, every reasoning step and action in the audit trail.

## Why

Complex requests need judgement (D238).

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

In shadow mode, write actions are dry runs; in automatic mode, they run; outside the allow-list, refused.

## Measure

Accuracy per intent; cost per run.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-02 Static workflow mode](req-t12-02-static-workflow-mode.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-04 One action contract](req-t12-04-one-action-contract.md)
