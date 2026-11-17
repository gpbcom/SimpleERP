🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T12-09 Sandbox for connectors and generated code

# 📌 REQ-T12-09 Sandbox for connectors and generated code

**Status:** ✅ specified

## Statement

Connector runs, browsers and generated code run in isolated containers: no access to the database or other
secrets, only the credential injected for that run; network egress limited to the connector's allow-list; memory, CPU
and time limits; no persistence between runs except declared outputs.

## Why

Generated code and outside pages are untrusted.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A generated scraper trying to reach another host is blocked and reported.

## Measure

Escapes: zero.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-08 Credentials stored safely](req-t12-08-credential-vault.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-10 Audit and evidence](req-t12-10-audit-and-evidence.md)
