🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D276 The AI assistant reaches every capability

# 📜 D276 The AI assistant reaches every capability

**Status:** ✅ decided

## Context

The owner: "Ensure that every F1 to F14 MUST be triggable from the AI assistant with permission related to the user
role(s) in the company."

## Options

- Every action of every capability is an AI assistant tool, within the user's roles.

## Choice

Every action of F1 to F14 (and F15, F16) is exposed to the AI assistant as a tool, through the one action contract
(REQ-T12-04); the AI assistant offers only the tools the user's roles allow (D12, the role matrix of F1), and each call
is checked again on the server.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F3-34; changes still follow D140 (confirmation) and BR-F3-07 (irreversible and outward acts prepared, finished by the
user); a capability is not done until its actions are reachable from the AI assistant.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [D140](d140-assistant-confirms-changes.md)
- [REQ-T12-04](../../03-technical/t12-connectors-and-scrapers/requirements/req-t12-04-one-action-contract.md)

---

⬅️ [D275 No negative stock](../f07-purchasing-and-stock/d275-no-negative-stock.md) · ⬆️ [Up](README.md) ·
➡️ [D277 Accounting coverage](../f08-accounting/d277-accounting-coverage.md)
