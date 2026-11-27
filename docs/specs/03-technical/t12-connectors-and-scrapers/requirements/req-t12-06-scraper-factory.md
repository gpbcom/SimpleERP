🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T12-06 Scraper and connector factory

# 📌 REQ-T12-06 Scraper and connector factory

**Status:** ✅ specified

## Statement

A connector or scraper is generated on the fly by a resumable graph: find the target (given by the customer,
or discovered, REQ-T12-13), discover its pages,
sample their structure (largest data block first, not only the visible list), author the code with a model tier ladder
(cheaper model first, stronger on failure), render it from a template, guard it (allowed imports, network only through
the fetch tool), test it in the sandbox, probe it live on one page, feed failures back (up to a set number of attempts),
then submit it for human review and activation; pagination follows the requests the page makes, never stops at a button;
a progress stream and a Stop button; a cost budget per run; generated artefacts versioned.

## Why

Hand-writing every connector does not scale
([D239](../../../06-decisions/f16-customer-support-agents/d239-scraper-factory.md)).

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A request to cover a new portal produces a tested connector proposal with its test evidence, or a clear failure report,
within its budget.

## Measure

Share generated first time; cost per connector.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-05 Browser automation for tools without an API](req-t12-05-browser-automation.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-07 Fetch ladder](req-t12-07-fetch-ladder.md)
