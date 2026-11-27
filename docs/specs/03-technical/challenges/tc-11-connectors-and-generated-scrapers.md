🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🕸️ TC-11 Connectors, scrapers and the outside world

# 🕸️ TC-11 Connectors, scrapers and the outside world

**Status:** ✅ listed for the technical interviews

## Challenge

Read and act in every outside system the capabilities need (helpdesks, banks, carriers, registers, registrars, LinkedIn
and Indeed, competitors' sites), with or without an API, with connectors generated on the fly and customers' credentials
kept safe.

## Raised by

- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md)
- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md)

## Why it is hard

- Outside sites change, block automation and have terms and robots rules to respect.
- Generated scraper code must never run outside a sandbox.
- Credentials must never reach a model or a log.

## Already decided

- [D238](../../06-decisions/f16-customer-support-agents/d238-static-or-agentic.md) Static workflows or agents
- [D239](../../06-decisions/f16-customer-support-agents/d239-scraper-factory.md) Connectors and scrapers generated on
  the fly
- [D240](../../06-decisions/security-and-compliance/d240-credential-vault.md) Customers' credentials in a vault

## Options to weigh

- One connector contract (typed actions, dry run, idempotency key) for static workflows and agents.
- Browser automation in isolated, disposable workers.
- A self-hosted vault with envelope encryption per company.

## Settled in

- 19f Security ([chapter](../../../technical/security/security.md))
- 19g Supply chain and licences ([chapter](../../../technical/security/supply-chain-and-licences.md))
- 19n Plugin SDK and developer experience ([chapter](../../../technical/interfaces/plugin-sdk.md))
- Then the technical capabilities: [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md).

## Questions for the interview

- Which connectors must exist on day one?
- Who repairs a broken connector: the factory, the publisher, or the community?

---

⬅️ [TC-10 Capturing meetings on outside platforms](tc-10-meeting-capture.md) · ⬆️ [Up](README.md) ·
➡️ [TC-12 Code written by an AI, running in production](tc-12-generated-code-in-production.md)
