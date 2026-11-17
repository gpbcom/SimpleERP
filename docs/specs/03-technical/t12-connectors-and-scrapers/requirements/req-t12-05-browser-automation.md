🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T12-05 Browser automation for tools without an API

# 📌 REQ-T12-05 Browser automation for tools without an API

**Status:** ✅ specified

## Statement

For a tool with no API, a connector logs in with the stored credential and drives the web interface in a
sandboxed browser: recorded or generated steps, a screenshot of each write as evidence, multi-factor authentication
through a TOTP seed stored under its own key, apart from the password (REQ-T12-08), or by asking the credential's owner
for the code, and a stop when the page differs from what
the steps expect.

## Why

Many back-office tools have no API.

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A policy system without an API: the connector logs in, finds the policy, reads its status; a changed page stops the run
and flags it.

## Measure

Runs stopped on drift; success rate.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-04 One action contract](req-t12-04-one-action-contract.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-06 Scraper and connector factory](req-t12-06-scraper-factory.md)
