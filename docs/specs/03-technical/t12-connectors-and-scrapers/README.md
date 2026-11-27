🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🕸️ T12 Connectors and scrapers

# 🕸️ T12 Connectors and scrapers

**Status:** ✅ specified

## Summary

Connectors to every outside system the company uses, with or without an API, driven by static workflows or by
agents, and a factory that generates new connectors and scrapers on the fly, tested in a sandbox; customers' credentials
kept in a vault ([D237](../../06-decisions/f16-customer-support-agents/d237-customer-support-agents.md) to
[D240](../../06-decisions/security-and-compliance/d240-credential-vault.md)).

## Scope

- Connector catalogue and one action contract (REQ-T12-01, REQ-T12-04).
- Static and agentic modes (REQ-T12-02, REQ-T12-03).
- Browser automation for tools without an API (REQ-T12-05).
- Scraper and connector factory, fetch ladder (REQ-T12-06, REQ-T12-07).
- Credential vault, sandbox, audit, health, lawful collection (REQ-T12-08 to REQ-T12-12).
- Target discovery when no URL is given (REQ-T12-13).

- Meeting capture: platform transcripts and the recorder bot (REQ-T12-18).

## Functional capabilities served

F16 Customer support agents first; also F3 (outside tools), F4 (meeting platforms, calendars, telephony), F5 (social
networks), F6, F7 and F8 (payment, carriers, banks, e-invoicing), F15 and T11 (official sources).

## Out of scope

- The MCP and A2A gateway itself: T6.
- The workflow designer: F2.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🏗️ |  | [Architecture](architecture.md) | ✅ |
| 📌 |  | [Requirements](requirements/README.md) | ✅ |
| 🔌 |  | [Interfaces](interfaces/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |
| 🛡️ |  | [Security](security.md) | ✅ |
| ⚙️ |  | [Operations](operations.md) | ✅ |
| 🚨 |  | [Errors](errors.md) | ✅ |
| 🧪 |  | [Tests](tests.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |

---

⬅️ [Legal corpora](../t11-legal-corpora/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Maps and geodata](../t13-maps-and-geodata/README.md)
