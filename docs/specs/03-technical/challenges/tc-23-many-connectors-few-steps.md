🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) ›
🔌 TC-23 Many connectors, connected in few steps, kept working

# 🔌 TC-23 Many connectors, connected in few steps, kept working

**Status:** ✅ listed for the technical interviews

## Challenge

Offer the office suites' full APIs, 50 ATS and CRM by default and many more tools, each enabled in as few steps as
possible, synced both ways, usable by the AI assistant, and kept working when the outside tools change.

## Raised by

- [F24 Integrations hub](../../02-functional/f24-integrations-hub/README.md)
- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md)

## Why it is hard

- Every tool has its own sign-in, scopes, limits and data model, and they change without notice.
- Two-way sync needs field owners, conflict handling and idempotency.
- Fewest steps means discovering settings the outside tool does not always expose.
- Each connector action must also be an AI assistant tool, within rights.

## Already decided

- [D238](../../06-decisions/f16-customer-support-agents/d238-static-or-agentic.md) Static workflows or agents
- [D240](../../06-decisions/security-and-compliance/d240-credential-vault.md) Customers' credentials in a vault
- [D427](../../06-decisions/f24-integrations-hub/d427-integrations-hub-coverage.md) Integrations hub
- [D428](../../06-decisions/f24-integrations-hub/d428-office-suites-full-api.md) Office suites: full read and write API
- [D429](../../06-decisions/f24-integrations-hub/d429-fewest-steps-for-every-connector.md) Fewest steps for every
  connector
- [D430](../../06-decisions/f24-integrations-hub/d430-fifty-ats-and-crm.md) The 50 ATS and CRM by default

## Options to weigh

- One connector contract (T12) with generated tool descriptions.
- Contract tests against each outside API's sandbox, run daily.
- Change data capture where offered, polling with cursors elsewhere.

## Settled in

- 19d API design and contracts ([chapter](../../../technical/interfaces/api.md))
- 19n Plugin SDK and developer experience ([chapter](../../../technical/interfaces/plugin-sdk.md))
- 19o Tests: unit, GUI, E2E and load ([chapter](../../../technical/delivery/tests-and-traceability.md))
- 19x MCP ([chapter](../../../technical/interfaces/mcp.md))
- Then the technical capabilities: [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md).

## Questions for the interview

- Who maintains 50+ connectors: the publisher, partners or the community?
- How fast must a broken connector be repaired?

---

⬅️ [TC-22 Simulating the whole company on copies](tc-22-simulation-on-copies.md) · ⬆️ [Up](README.md) ·
➡️ [TC-24 Agents that read production and write code](tc-24-agents-on-code-and-production.md)
