🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-08 Planning and calculation workers

# 📌 REQ-T04-08 Planning and calculation workers

**Status:** ✅ specified

## Statement

Planning (rounds, crews, production, deliveries, staff) runs on a constraint solver as a separate worker on the durable
workflow engine, with a time limit, a best-so-far answer, progress and a Stop button; payroll, tax and surcharge
calculations are versioned modules, exact to the cent, explained line by line, with test cases per country-pack version
(REQ-T11-06).

## Why

Confirmed by the owner on 2026-11-12; D405 (long runs), D293; TC-14; the review of 2026-11-12 (R14).

## Acceptance criteria

1. **Given** a plan too large for its time limit, the best plan so far is shown with its progress.
2. **Given** a payslip computed on two pack versions, each matches its test cases to the cent.

## Measure

Plans within their time limit; calculation test pass rate.

## Priority

Must

## Capabilities served

F9, F12, F13, SC04, SC07

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T04-07 Limits and metering per plugin](req-t04-07-plugin-limits.md) · ⬆️ [Up](README.md)
